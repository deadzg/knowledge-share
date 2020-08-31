# Key Concepts
- *Terraform Registry*: Registry to search for available providers, resources & modules

- *Terraform Block*: Required to identify which providers to download from Terraform Registry

- *Providers* : Providers are plugins that implement resource types and is responsible for creating and managing resources

- *Resources* : This defines a piece of infrastructure

# Install & Setup
- Install Terraform in Mac: `brew install terraform`
- Help: `terraform -help`
- Help for any command: `terraform -help <command-name>`
Eg: `terraform -help plan`
- Install Autocomplete: `terraform -install-autocomplete`
- Get terraform version: `terraform version`



# Basic Commands
Note: All comands are executed assuming the `*.tf` file is in the same directory

- Initialize Project: `terraform init`
- Format: `terraform fmt`
- Validate: `terraform validate`
- Apply the changes to the infra: `terraform apply`
- Inspect the current state: `terraform show`
- Delete the infra: `terraform destroy`
- See the plan before creation of infra: `terraform plan`


# Resources
- https://learn.hashicorp.com/tutorials/terraform/aws-build

