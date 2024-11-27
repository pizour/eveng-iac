provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "example" {
  name     = local.eveng_iac["infra"]["rg"]
  location = var.location
}

output "resource_group_name" {
  value = azurerm_resource_group.example.name
}