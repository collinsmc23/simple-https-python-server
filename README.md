# Simple HTTPS Python Server
Inspired by: https://blog.anvileight.com/posts/simple-python-http-server/

## Description
A simple python script to provide HTTPS functionality for serving a basic HTTP server. 

## Download
`git clone https://github.com/collinsmc23/simple-https-python-server.git`

## Generate SSL/TLS Certificate
Using the "OpenSSL" library, you can generate a self-signed certificate, including the certificate and key file. 

### Create Certificate (CRT) and Key
Install Openssl on Linux (Ubuntu/Debian): `sudo apt install openssl`
Linux: `openssl req -x509 -newkey rsa:2048 -keyout your_selfsigned.key -out your_selfsigned.crt -days 365`
* req -x509: Request x509 format certificate
* -newkey rsa:2048: Use RSA of 2048 size
* -keyout your_selfsigned.key: File to place key
* -out your_selfsigned.crt: File to place certificate 
* -days 365: Set to expire after 365 days of generation

## Script Details
* Enter listening IP address and port number under IP_ADDRESS, PORT_NUM
* Place .crt and .key file locations under your_selfsigned.key and your_selfsigned.crt
