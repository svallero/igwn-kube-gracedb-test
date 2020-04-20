#!/bin/sh
#kubectl create configmap lvalert-no-certificate --from-file=configmaps/__init__.py -n gracedb-test
kubectl create configmap lvalert-no-certificate --from-file=configmaps/__init__.py -n test
