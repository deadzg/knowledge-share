# Git Usage : Tips

## Overwrite Git profile
### Use case
Global git profile is configured with user account A. For a particular repository I want to set the config for user account B

Prequisites:
- Clone the repository for which git profile for B has to be set
- Make a note of user name for user B (testuserB)
- Make a note of user email for user B (configured in github)

Steps
- Navigate to the repository for which needs to be configured
- Set username: `git config user.name "testuserB"`
- Set useremail: `git config user.email "testuserB@abc.com"`
- Verify using: `git config --list`

## MD file editor
### Use case
I want to see runtime changes to my md files before committing to github

Use the below app to develop md file:
[https://stackedit.io/](https://stackedit.io/)

## Adding and Committing code in one command
I want to add and commit the changed file in the repository in single command

Use the below git command:
`git commit -a -m "Placeholder for message"`

## Delete a git tag
```
git tag -d <tag_name>
git push origin :refs/tags/<tag_name>
```