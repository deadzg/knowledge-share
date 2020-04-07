# GPG Basics
- Stands for GNU Privacy Guard

## GPG vs PGP [1]
- GPG is a re-write/upgraded version of PGP(Pretty Good Privacy)
- Uses NIST AES algorithm for encryption
- PGP is not free for commerical/business use, but GPG is free

## Use Case
Got some secret message to share with someone else. May be you can mail them, send text messages, send a voice message, call them over phone. All of the above communications are protected but can be peeped by anyone having specilized skills. Thus you secret message is not secret enough. GPG comes to the resuce.

We will be using standard terminology of Alice(Sender), Bob(Receiver) and Eve(Intruder)

### Scenario 1:
Alice wants to share password for an account/portal with Bob.
Steps:
- Alice will ask for public key of Bob
- Bob will send the public key over internet
- Alice will encrpyt the message with public key of Bob and Sign it with her private key
- Alice sends the encrypted and signed message over email to Bob
- Alice also sends her public key to Bob (this is needs for verifying the signature)
- Bob verifies the message is from Alice using Alices public key
- Once verified Bob uses it's private key to decrypt the messages

GPG Commands to achive the above scenario
#### Bob's Machine:
- Bob generates a pub/priv key pair (if already not present): `gpg --generate-key`
    For more controlled key use: `gpg --full-generate-key`
- Verfiy the keys are generated using: 
    For public keys: `gpg --list-keys`
    For private keys: `gpg --list-secret-keys`
- Export the public key to be shared with Alice: `gpg --export -a "bob-email" > bob-public.key`
    Note: user-email is the emailId with which Bob generated the keys
- Once Bob gets the encrypted message, Bob imports public key of Alice as the secret message is signed by Alice: `gpg --import alice-public.key`
- Now Bob decrypts the message: `gpg -d -o decrypt-file secret-file.gpg`

#### Alice's Machine:
- Alice imports the public key of Bob sent over email: `gpg --import bob-public.key`
- Alice signs and encrypt the secret message: `gpg -e -s -r bob-email secret-file`
- Alice sends the encrypted file `secret-file.gpg` and public key `alice-public.key` to Bob



## References
- [1] http://www.differencebetween.net/technology/software-technology/difference-between-pgp-and-gpg/ 
- [2] http://irtfweb.ifa.hawaii.edu/~lockhart/gpg/
