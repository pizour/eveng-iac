module "shared_infra" {
  source = "./modules/tf-mod-general/"

  resource_group_name = local.iac["infra"]["rg"]
  location            = local.iac["infra"]["azure_location"]
}

module "networking" {
  source   = "./modules/tf-mod-networking/"
  for_each = vnet in local.iac["infra"]["networks"]

  vnet_name = vnet.name
  address_space = vnet.address_space
  subnets = vnet.subnets
  resource_group_name = local.iac["infra"]["rg"]
  location            = local.iac["infra"]["azure_location"]
}
