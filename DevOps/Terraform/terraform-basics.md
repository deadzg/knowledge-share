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

- `terraform init`: Initialize Project and Downloads the plugin for the provider
- `terraform fmt`: Formats all the tf file in HCL format
- `terraform validate`: Validate
- `terraform apply`: Apply the changes to the infra
- `terraform show`: Inspect the current state
- `terraform destroy`: Delete the infra
- `terraform plan`: See the plan before creation of infra
- `terraform plan -out tfplan` : Saves the plan in a file
- `terraform plan --var-file=<path-of-tfvar file>` : Run the plan using the given tfvar
- `terraform apply tfplan` : Executes plan from a saved plan file
- `terraform show` : Reads the resource files and outputs the resources created
- `terraform console` : Get specific data in show data
- `terraform output` : Shows the output of the variables in outputs.tf

# Notes
TF version used : 0.11.8
HCL - Hashicorp Configuration Language
AWS TF Doc: https://registry.terraform.io/providers/hashicorp/aws/latest/docs

Define the Provider first
Define the resource 
variables.tf => Defined for input variables
outputs.tf => Defined for output variables

AWS Commands:
Create key pair from AWS CLI:
aws ec2 create-key-pair --key-name bastion --query 'KeyMaterial' --output text > bastion.pem

SSH from local:
ssh -i bastion.pem ec2-user@<ec2-public-ip>


# Resources
- https://learn.hashicorp.com/tutorials/terraform/aws-build
- https://registry.terraform.io/providers/hashicorp/aws/latest/docs


