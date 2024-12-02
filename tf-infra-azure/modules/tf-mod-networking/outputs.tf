# output "virtual_network_subnets" {
#   description = "Maps out virtual network subnets created with names and ids"
#   value = tomap({
#     for k, subnet in azurerm_subnet.subnet : k => { id : subnet.id, name : subnet.name, address_prefixes : subnet.address_prefixes }
#   })
# }