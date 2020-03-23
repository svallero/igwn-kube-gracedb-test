#!/bin/sh

openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout tls.key -out tls.crt -subj "/CN=vm-131-154-161-31.cr.cnaf.infn.it"

mv tls.key tls.crt certs/
