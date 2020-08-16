# DNS Basics

## Key Terminologies
### A record
- A record maps a domain to the IP address
- `A` stands for address
- Multiple A records can be mapped to single domain. Used for redundancy and fallbacks
- Multiple names can point to the same address, in which case each will have it's own A record pointing to the same IP address

### CNAME
- Stands for Canonical Name
- Used to alias one domain name to another. For eg: **A record** for pointing `abc.com` to IP address. **CNAME** record for `www.abc.com` to point to `abc.com`
- A CNAME record must always point to another domain name and never directly to an IP address
- A CNAME record cannot co-exist with another record for the same name. It’s not possible to have both a CNAME and TXT record for www.abc.com
- A CNAME can point to another CNAME, although this configuration is generally not recommended for performance reasons

### Nameservers
- Nameservers are part of a large database called the Domain Name System (DNS), which acts like a directory for devices and the IP addresses attached to them
- You simply type in a URL, the nameserver lets your browser know where that website is located, and the desired page loads