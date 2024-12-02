locals {
  iac = yamldecode(file(var.iac_path))
}