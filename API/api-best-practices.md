# API Best Practices

- Versioning
	- URI Path
	- Query Params
	- Custom Header
	- Content-negotiation header
		- Eg: headers = "Accept=application/users-v1+json"

- Security
    - CORS
	- Spike Arrest
	- IP Whitelisting
	- CSRF
        - Analyze traffic patterns to put bots away using ML
        - Threat Protection: XML Poisioning, SQL and JSON Injection, Bot attacks
	- Authentication and Authorization
		- Authorization Header
			- Schemes
				- Basic Authentication
				- Hash based message authentication (HMAC)
				- JWT
				- OAuth 2.0 Bearer authentication token
		- SAML
		- Open ID Connect
		- OAuth2
			- Client Credentials (Usecase: Machine to Machine communication)
			- OAuth 2.0 Mutual-TLS Client Authentication and Certificate-Bound Access Tokens
			- Authorization Codeflow with Proof Key for Code Exchange(PKCE)
			- Authorization Code - Three legged OAuth
			- Implicit
			- Password
			- Scope
			- Expiry Time
			- Access Token, Refresh Token, ID Token	
		- API Key
- Open API Specification (Swagger)
- Logging
- HATEOS
- Analytics
- Compliance with PCI DSS, HIPAA, SOC 2 whereever applicable
- Scale and Compute: Handle massive number of API keys and tokens and compile policies at runtime
- Alerting and Notification
- Rate Limiting
- Idempotent
- Pagination
- Error and exception logging
- Statelessness
- API Deprecation Plan
