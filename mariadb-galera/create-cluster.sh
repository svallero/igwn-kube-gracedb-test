#!/bin/sh

helm repo add bitnami https://charts.bitnami.com/bitnami

helm install --name gracedb-test --namespace gracedb-test -f values.yaml bitnami/mariadb-galera

