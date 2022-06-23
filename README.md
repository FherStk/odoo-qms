# odoo-qms
Odoo module for QMS

## UNDER DEVELOPMENT - DO NOT USE IN PRODUCTION ENVIRONMENTS!
### In order to download
Just clone the repo into Odoo addons folder with:

`sudo git clone https://github.com/FherStk/odoo-qms.git /usr/lib/python3/dist-packages/odoo/addons/qms`

### In order to install
1. Login into Odoo
2. Enable the developer mode
3. Refresh the app list
4. Find 'QMS' and install it.

### Devel tips
#### Module permissions for remote access
Set the proper permissions for the devel user, in order to allow remote access and write permissions:

`sudo chown <username>:<username> +R /usr/lib/python3/dist-packages/odoo/addons/qms`

VSCode is recommended to perform any kind of modifications, using the Microsoft's SSH plugin for remote developing.

#### Updating the module using the CLI interface
The process must be stopped before any command execution.

`sudo service odoo stop && sudo -u odoo bash -c 'odoo -u qms --stop-after-init -c /etc/odoo/odoo.conf' && sudo service odoo start`