#!/bin/sh

helm upgrade  gracedb-test --namespace gracedb-test -f values.yaml bitnami/mariadb-galera

