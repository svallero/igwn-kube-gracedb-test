#!/bin/sh
kubectl create configmap django-settings-cnaf-test --from-file=configmaps/cnaf_test.py -n gracedb-test
kubectl create configmap django-update-site --from-file=configmaps/0002_update_site.py -n gracedb-test
