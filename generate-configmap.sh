#!/bin/sh
kubectl create configmap django-settings-cnaf-test --from-file=configmaps/cnaf_test.py -n gracedb-test
