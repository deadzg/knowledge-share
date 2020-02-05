# Jenkins Tips

## Fetch Secret text/ username-password from Jenkins Credentials
- Go to the respective credentials
- Inspect in browser to copy hash
- Navigate to http://<jenkins-host>/script
- Run this script: `println(hudson.util.Secret.decrypt("<hash from above step>"))`