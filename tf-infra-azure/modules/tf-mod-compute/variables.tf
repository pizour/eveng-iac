variable "resource_group_name" {
  type        = string
  description = "Resource Group name for VNET"
}

variable "location" {
  type        = string
  description = "Location for Virtual Network"
}

variable "vm_name" {
  type        = string
  description = "Name of the VM"
}

variable "vnet_name" {
  type        = string
  description = "VM Location for Virtual Network"
}

variable "subnet_name" {
  type        = string
  description = "VM Location for Subnet inside Virtual Network"
}

variable "vm_size" {
  type        = string
  description = "VM size"
}

variable "ssh_username" {
  type        = string
  description = "VM SSH admin username"
}

variable "ssh_pubkey" {
  type        = string
  description = "VM SSH public key"
}
