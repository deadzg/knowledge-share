# Key Components
## JWKS: Json Web Key Signature

## JWT: Json Web Token
- Token for sharing claims
- Represent a set of claims as a JSON object that is encoded in a JWS and/or JWE structure
- JWT does NOT exist by itself. It has to be JWS or JWE. It's like an abstract class and JWS/JWE are concrete implementation
- Three main parts of JWT
    - Header: type of encoded object in the payload and any extra encoding
        Eg: {"typ":"JWT","alg":"HS256"} 
        - we have a JWT that is integrity protected with the HMAC SHA-256 algorithm
        - The payload with a JWE including this header will be of a JWT signed and encrypted with the HMAC SHA-256 algorithm
        - The type may be left out if the JWSs and JWEs used by the application are JWT types
    - Payload: JWT claims set
    - Signature: 
        - encoding of the header and payload using the algorithm specified in the header. It ensures the integrity
        - The signature is essential to detect unauthorized tampering with a token.
- Format of JWT: `{header}.{payload}.{signature}`


## JWK: Json Web Key

## JWE: Json Web Encryption

## JWS: Json Web Signature
- Signed JWT is knowns as JWS

# Symmetric JWT signatures
For generating a JWT
- Input to Alg specified in header : Header + Payload
- Secret Key to the Alg specified in the header
- Out: Signature

For Validating the JWT
- Service uses the secret key to generate the signature and if this signature matches with the one in the JWT - Validation is successful

Limitation:
- all services would need to have access to the same secret key.
- possession of the secret key is enough to generate arbitrary JWTs with a valid signature.
- Sharing the HMAC secret with a third-party service creates a significant vulnerability.
- Even sharing the secret between different services within a single architecture is not recommended
- If all services share the same key, the compromise of a single service immediately becomes an architecture-wide problem

# Asymmetric JWT signatures
- An asymmetric signature uses a public/private key pair
- A signature generated with a private key can be verified with the public key
- the public key can be shared with other services
-  the private key can be kept in a confidential location, only known to the issuer of the JWT tokens

## Validating beyond signatures:
- JWT can contain a few other security-related properties in form of reserved claims
- most crucial security claim is the `exp` claim. The issuer uses this claim to indicate the expiration date of a JWT.
- JWTs can contain the `nbf` claim. This abbreviation stands for "not before." It indicates the point in time when the JWT becomes valid. A JWT can only be accepted if this timestamp lies in the past
- Another security-relevant reserved claim is `iss` This claim indicates the identity of the party that issued the JWT. The claim holds a simple string, of which the value is at the discretion of the issuer. The consumer of a JWT should always check that the `iss` claim matches the expected issuer
- Another claim is the `aud` claim. This abbreviation stands for audience. It indicates for whom the token is intended. The consumer of a JWT should always verify that the audience matches its own identifier

the specification mentions that all of these claims are optional. Nonetheless, it is highly recommended that your application includes them when issuing JWTs. Presence of these claims must be verified when validating JWTs

## Identifying Key




## Reference
- https://www.pingidentity.com/en/company/blog/posts/2019/jwt-security-nobody-talks-about.html
- https://pragmaticwebsecurity.com/files/cheatsheets/jwt.pdf
- https://tools.ietf.org/html/rfc7519
- https://medium.facilelogin.com/jwt-jws-and-jwe-for-not-so-dummies-b63310d201a3

