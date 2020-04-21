# igwn-kube-gracedb-test
Test deployment of GraceDB on Kubernetes cluster on premises. It was developed for a Kubernetes cluster managed by Rancher on OpenStack. Some details might change for different Cloud providers. For instance, you might need to adjust the StorageClass for persistent volumes. 

**Prerequisites:**
- [Helm (and Tiller if required by the Helm version)](https://helm.sh/docs/intro/install/) 
- [Traefik controller](https://docs.traefik.io/v1.7/user-guide/kubernetes/) 

**TODO:** 
- external IP provisioning and certificate handling
- once everything is setup, you neeed to login to the admin console and set the *Sites* variable to the correct value. This step should be automated.

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

## 4 - gracedb-volume-ha.yaml
Create a persistent volume for the folder */app/db_data*. You might need to edit this file.

## 5 - Generate ConfigMaps
Generate some useful ConfigMap:
```
./generate-configmap.sh 
./generate-configmap-hack.sh 
```
The latest script will not be needed once the certificates are in place for Lvalert. 

## 6 - deployment-ha.yaml
This creates the actual deployment.

## 7 - Initialize the database (manual steps)
This is required only the first time, when the database needs to be initialized. 
Get the list of pods belonging to the deployment:
```
kubectl get pods -n gracedb-test
...
gracedb-test-ha-xxx         1/1     Running   0          13d
gracedb-test-ha-yyy         1/1     Running   0          13d
gracedb-test-ha-zzz         1/1     Running   0          13d
...
```

Then login to one of the replicas:
```
kubectl exec -it gracedb-test-ha-xxx bash -n gracedb-test
```
And execute the following commands:
```
python3 manage.py migrate
python3 manage.py createcachetable
python3 manage.py createsuperuser 
```
(you need to choose a username and password for the admin user).

## 8 - service-ha.yaml
Allow the Pods to be reached from the outside. You might need to edit this file if you want to use a different service type. 

## 9 - Traefik Ingress and certificates
**TODO** once the network configuration is finalized.

## A note on local user login
Latest releases of GraceDB do not support local user login. To enable this feature for testing purposes, you should use an older release of the project. You can configure a separate deployment running the old release by applying the following manifests:
```
deployment-login-ha.yaml
service-login-ha.yaml
```
Then, you should route only the path */login* to this deployment. To do so, please take a look at the file: *ingress.yaml*.

Finally, you can login to the admin console, create the local users and assign them the desired permissions. 
