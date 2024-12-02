terraform {
  backend "azurerm" {
  }
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~>4.7.0"
    }
  }
  required_version = "1.9.8"
}