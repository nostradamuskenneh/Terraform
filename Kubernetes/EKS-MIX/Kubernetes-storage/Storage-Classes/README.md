## Storage Classes [here](https://kubernetes.io/docs/concepts/storage/storage-classes/#provisioner)


- It is the volume for the cluster. It is the entire volume that kubernetes is going to used
- it doesn't have anything to with nodes virtual machine
- local storage class is used if you are running kubernetes in `kind, minuke`

## Create a storage class
vim gp2-storage-class.yaml
kubectl create -f gp2-storage-class.yaml

```yaml
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: gp2
  annotations:
    storageclass.kubernetes.io/is-default-class: "true"
provisioner: kubernetes.io/aws-ebs
parameters:
  type: gp2
  fsType: ext4



A typical YAML file of storage class using AWS EBS storage looks like this:
```yml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: standard
provisioner: kubernetes.io/aws-ebs
parameters:
  type: gp2
reclaimPolicy: Retain
allowVolumeExpansion: true
mountOptions:
  - debug
volumeBindingMode: Immediate
```

### Get storage classes
```
kubectl get storageclass
kubectl get sc
``