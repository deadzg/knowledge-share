# Basic Certificate Related Commands

## Prerequisites:
- Install openssl
- OS: Mac or Linux

### Import public certificate for any website
`openssl s_client -showcerts -connect <host>:<port> </dev/null 2>/dev/null|openssl x509 -outform PEM > public-cert.pem`
