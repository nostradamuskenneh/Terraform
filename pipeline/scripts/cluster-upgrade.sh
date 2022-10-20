AWS_REGION="us-east-1" 
EKS_KUBE_PROXY_VERSION="1.20.4-eksbuild.2"
EKS_CORE_DNS_VERSION="1.8.3"

## Check the Pod security policy (PSP)
echo "Verifying if the pod security privilege exist"

kubectl get psp eks.privileged 

if [[ $? -eq 0 ]]
then 
    echo -e "Pod security privilege exist"
    sleep 3
else
    echo "Pod security privilege Do not exist on this cluster and you must enable before you can proceed"
    sleep 3
    exit 2
fi

## Patch kubeproxy
echo "Verifying The kubeproxy version"
KUBE_PROXY=`kubectl get daemonset kube-proxy \
                --namespace kube-system \
                -o=jsonpath='{$.spec.template.spec.containers[:1].image}' \
                | awk -F":" '{print$2}' \
                | awk '{print substr($1,2); }'`

if [[ $KUBE_PROXY == $EKS_KUBE_PROXY_VERSION ]]
then 
    echo "The kube proxy was already ugraded to $EKS_KUBE_PROXY_VERSION"
    echo "kubectl set image daemonset.apps/kube-proxy -n kube-system kube-proxy=602401143452.dkr.ecr.$AWS_REGION.amazonaws.com/eks/kube-proxy:v$EKS_KUBE_PROXY_VERSION"
    exit 2
else
    kubectl set image daemonset.apps/kube-proxy -n kube-system kube-proxy=602401143452.dkr.ecr.$AWS_REGION.amazonaws.com/eks/kube-proxy:$EKS_KUBE_PROXY_VERSION

    echo -e "The new version of the kube proxy is:\n "
    kubectl get daemonset kube-proxy \
                --namespace kube-system \
                -o=jsonpath='{$.spec.template.spec.containers[:1].image}' \
                | awk -F":" '{print$2}' \
                | awk '{print substr($1,2); }'
    sleep 3
    echo "Verify if the kube-proxy pods are running in kube-system namespace"
    
    kubectl get po -n kube-system |grep kube-proxy
    sleep 3
    
fi

## Patch CoreDNS
echo "Verifying The kubeproxy version"
CORE_DNS1=`kubectl describe deployment coredns \
            --namespace kube-system \
            | grep Image \
            | cut -d "/" -f 3 \
            | awk -F":" '{print$2}' \
            | awk '{print substr($1,2); }' \
            | awk -F"-" '{print$1}'`

CORE_DNS2=`kubectl describe deployment coredns \
            --namespace kube-system \
            | grep Image \
            | cut -d "/" -f 3 \
            | awk -F":" '{print$2}' \
            | awk '{print substr($1,2); }' \
            | awk -F"-" '{print$2}'`


if [[ $CORE_DNS1 == $EKS_CORE_DNS_VERSION ]]
then 
    echo "The kube coredns was already ugraded to $EKS_CORE_DNS_VERSION"
    exit 2
else
    kubectl set image --namespace kube-system deployment.apps/coredns \
        coredns=602401143452.dkr.ecr.$AWS_REGION.amazonaws.com/eks/coredns:v$CORE_DNS1-$CORE_DNS2

    echo "The new version of the kube proxy is: $CORE_DNS1"
    sleep 3

    echo "Verifying if the kube-proxy pods are running in kube-system namespace"
    kubectl get po -n kube-system |grep kube-proxy
    sleep 3
fi

## Patch AWS VPC CNI

echo "Verifying the current version of the AWS VPC CNI"
kubectl describe daemonset aws-node --namespace kube-system | grep Image | cut -d "/" -f 2
sleep 3

curl -o aws-k8s-cni.yaml https://raw.githubusercontent.com/aws/amazon-vpc-cni-k8s/release-1.10/config/master/aws-k8s-cni.yaml
sed -i.bak -e "s/us-west-2/$AWS_REGION/" aws-k8s-cni.yaml
kubectl apply -f aws-k8s-cni.yaml
rm aws-k8s-cni.yaml

echo "Verifying the AWS VPC CNI version after update"
kubectl describe daemonset aws-node --namespace kube-system | grep Image | cut -d "/" -f 2
sleep 3

echo "Verifying if the daemonset aws-node pods are running in kube-system namespace"
kubectl get daemonset aws-node -n kube-system
sleep 3