```python
from odoo import models, fields, api

class ThemeViews(models.Model):
    _name = 'theme.views'
    _description = 'Theme Views'

    name = fields.Char(string='View Name', required=True)
    type = fields.Selection([('tree', 'Tree'), ('form', 'Form')], string='View Type')
    model_id = fields.Many2one('ir.model', string='Model', required=True)

    @api.model
    def create(self, vals):
        view = super(ThemeViews, self).create(vals)
        # Add additional logic here if needed
        return view

class ThemeActions(models.Model):
    _name = 'theme.actions'
    _description = 'Theme Actions'

    name = fields.Char(string='Action Name', required=True)
    type = fields.Selection([('client', 'Client'), ('server', 'Server')], string='Action Type')
    view_id = fields.Many2one('theme.views', string='View', required=True)

    @api.model
    def create(self, vals):
        action = super(ThemeActions, self).create(vals)
        # Add additional logic here if needed
        return action
```