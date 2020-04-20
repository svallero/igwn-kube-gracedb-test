# igwn-kube-gracedb-test
Test deployment of GraceDB on Kubernetes cluster on premises. It was developed for a Kubernetes cluster managed by Rancher on OpenStack. Some details might change for different Cloud providers. For instance, you might need to adjust the StorageClass for persistent volumes. 

**Prerequisites:**
- [Helm (and Tiller if required by the Helm version)](https://helm.sh/docs/intro/install/) 
- [Traefik controller](https://docs.traefik.io/v1.7/user-guide/kubernetes/) 

**TODO:** 
- external IP provisioning and certificate handling

Apply the following manifests with:

```kubectl apply -f <manifest_name>.yaml```

## 1 - namespace.yaml
Group all resources under the same namespace.

## 2 - kustomization.yaml
Insert your secrets here. The kustomization file is applied with:

```kubectl apply -k .```

The file name must be *kustomization.yaml*.

## 3 - database in HA (mariadb-galera)
First you need to create the persistent volumes for each replica of the StatefulSet. Apply the following manifest (first edit the file to suit your setup):
```
kubectl apply -f mariadb-galera/pv.yaml
``` 

Then create the replicated database with the script:
```
./mariadb-galera/create-cluster.sh
```
