resource "azurerm_windows_virtual_machine" "example" {
  name                  = "example-vm"
  resource_group_name   = azurerm_resource_group.example.name
  location              = azurerm_resource_group.example.location
  size                  = "Standard_DS1_v2"
  admin_username        = "adminuser"
  admin_password        = "Password1234!"
  network_interface_ids = [azurerm_network_interface.example.id]

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "MicrosoftWindowsServer"
    offer     = "WindowsServer"
    sku       = "2019-Datacenter"
    version   = "latest"
  }
}