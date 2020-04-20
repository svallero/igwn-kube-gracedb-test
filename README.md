# igwn-kube-gracedb-test
Test deployment of GraceDB on Kubernetes cluster on premises. It was developed for a Kubernetes cluster managed by Rancher on OpenStack. Some details might change for different Cloud providers. For instance, you might need to adjust the StorageClass for persistent volumes. 

**TODO:** 
- external IP provisioning and certificate handling

Apply the following manifests with:

```kubectl apply -f <manifest_name>.yaml```

## 1 - namespace.yaml
Group all resources under the same namespace.


