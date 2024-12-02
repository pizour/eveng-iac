module "shared_infra" {
  source = "./modules/tf-mod-general/"

  resource_group_name = local.iac["infra"]["rg"]
  location            = local.iac["infra"]["azure_location"]
}

module "networking" {
  source   = "./modules/tf-mod-networking/"
  for_each = { for vnet in local.iac["infra"]["networks"] : vnet.name => vnet }

  vnet_name           = each.value.name
  address_space       = each.value.address_space
  subnets             = each.value.subnets
  resource_group_name = local.iac["infra"]["rg"]
  location            = local.iac["infra"]["azure_location"]
}
