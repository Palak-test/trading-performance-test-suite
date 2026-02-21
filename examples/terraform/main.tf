# main.tf

# Example Terraform configuration for loopa infrastructure

provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "loopa" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
