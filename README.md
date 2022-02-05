# Simple HTTPS Python Server
Inspired by: https://blog.anvileight.com/posts/simple-python-http-server/

## Description
A simple python script to provide HTTPS functionality for serving a basic HTTP server. 

## Download
`git clone https://github.com/collinsmc23/simple-https-python-server.git`

## Generate SSL/TLS Certificate
Using the "OpenSSL" library, you can generate a self-signed certificate, including the certificate and key file. 

### Create Certificate (CRT) and Key
Linux: `openssl req -x509 -newkey rsa:2048 -keyout your_selfsigned.key -out your_selfsigned.crt -days 365`
