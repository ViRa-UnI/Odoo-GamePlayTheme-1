```python
from odoo import models, fields

class CustomModule(models.Model):
    _name = 'theme.custom.module'
    _description = 'Custom Module for Theme Development'

    name = fields.Char(string='Module Name', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)

    def create_custom_module(self, module_name, module_description):
        """
        Function to create a custom module
        """
        self.env['theme.custom.module'].create({
            'name': module_name,
            'description': module_description,
        })

    def deactivate_module(self, module_name):
        """
        Function to deactivate a module
        """
        module = self.env['theme.custom.module'].search([('name', '=', module_name)])
        if module:
            module.write({'active': False})

    def activate_module(self, module_name):
        """
        Function to activate a module
        """
        module = self.env['theme.custom.module'].search([('name', '=', module_name)])
        if module:
            module.write({'active': True})
```