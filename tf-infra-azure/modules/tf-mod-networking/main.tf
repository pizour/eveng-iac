resource "azurerm_virtual_network" "virtual_network" {
  name                = var.vnet_name
  address_space       = [var.address_space]
  location            = var.resource_group_name
  resource_group_name = var.location
}

resource "azurerm_subnet" "subnet" {
  for_each = subnet in var.subnets

  name                 = subnet.name
  resource_group_name  = var.resource_group_name
  virtual_network_name = azurerm_virtual_network.virtual_network.name
  address_prefixes     = [subnet.net]
}

# resource "azurerm_public_ip" "eveng-pip" {
#   name                = "-pip"
#   location            = azurerm_resource_group.example.location
#   resource_group_name = azurerm_resource_group.example.name
#   allocation_method   = "Dynamic"
# }

# resource "azurerm_network_interface" "example" {
#   name                = "example-nic"
#   location            = azurerm_resource_group.example.location
#   resource_group_name = azurerm_resource_group.example.name

#   ip_configuration {
#     name                          = "internal"
#     subnet_id                     = azurerm_subnet.example.id
#     private_ip_address_allocation = "Dynamic"
#     public_ip_address_id          = azurerm_public_ip.example.id
#   }
# }