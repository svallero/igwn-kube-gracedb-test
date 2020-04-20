#!/bin/sh

#helm repo add bitnami https://charts.bitnami.com/bitnami

helm upgrade  gracedb-test --namespace gracedb-test -f values.yaml bitnami/mariadb-galera

#helm del --purge gracedb-test
