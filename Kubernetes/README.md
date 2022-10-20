# Kubernetes system administrator

- **Lab reference 1:** https://kubernetes.io/docs/tutorials/kubernetes-basics/create-cluster/cluster-interactive/

* Base64 encode [here](https://www.base64encode.org/)

- **Lab reference 1:** ](https://www.katacoda.com/courses/kubernetes/)playground

* [Kubernetes Documentation](https://kubernetes.io/docs/concepts/)

* [Terraform and EKS: a Step-by-Step Guide to Deploying Your First Cluster](https://www.fairwinds.com/blog/terraform-and-eks-a-step-by-step-guide-to-deploying-your-first-cluster)


### Install kubectl on Linux
```sh
curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl
```
$ aws eks update-kubeconfig --name [cluster_name] --region [region]
Example: aws eks update-kubeconfig --name eks --region us-east-1