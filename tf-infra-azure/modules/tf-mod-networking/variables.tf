variable "resource_group_name" {
  type        = string
  description = "Resource Group name for VNET"
}

variable "location" {
  type        = string
  description = "Location for Virtual Network"
  default     = "swedencentral"
}

variable "vnet_name" {
  type        = string
  description = "Name for Virtual Network"
}

variable "address_space" {
  type        = string
  description = "Address space for Virtual Network"
}

variable "subnets" {
  type = list[object({
    name = string
    net  = string
  })]
  description = "Address space for Virtual Subnet"
}
