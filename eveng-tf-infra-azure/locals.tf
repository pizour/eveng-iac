locals {
  eveng_iac = yamldecode(file(var.eveng_infra_iac_path))
}