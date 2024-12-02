module "shared_infra" {
  source = "./modules/tf-mod-general/"

  resource_group_name = local.iac["infra"]["rg"]
  location            = local.iac["infra"]["azure_location"]
}

module "networking" {
  source   = "./modules/tf-mod-networking/"
  for_each = { for vnet in local.iac["infra"]["networks"] : vnet.name => vnet }

  vnet_name           = each.value.name
  address_space       = each.value.net
  subnets             = each.value.subnets
  resource_group_name = local.iac["infra"]["rg"]
  location            = local.iac["infra"]["azure_location"]
}

module "compute" {
  source   = "./modules/tf-mod-compute/"
  for_each = { for vm in local.iac["infra"]["vms"] : vm.vm_name => vm }

  vm_name             = each.value.vm_name
  vm_size             = each.value.vm_size
  vnet_name           = each.value.vnet_name
  subnet_name         = each.value.subnet_name
  ssh_username        = each.value.ssh_username
  ssh_pubkey          = each.value.ssh_pubkey
  unique_vm_alias     = each.value.unique_vm_alias
  resource_group_name = local.iac["infra"]["rg"]
  location            = local.iac["infra"]["azure_location"]
  depends_on = [
    module.networking
  ]
}
