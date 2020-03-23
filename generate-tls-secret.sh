#!/bin/sh

kubectl -n gracedb-test create secret tls traefik-gracedb-test-tls-cert --key=certs/tls.key --cert=certs/tls.crt
