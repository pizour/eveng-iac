variable "resource_group_name" {
  default = "example-rg"
}

variable "location" {
  default = "eastus"
}

variable "eveng_infra_iac_path" {
  type        = string
  description = "Path to the YAML file"
}