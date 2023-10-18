```python
from odoo import api, fields, models

class ThemeFooter(models.Model):
    _name = 'theme.footer'
    _description = 'Footer for the Theme'

    link_ids = fields.One2many('theme.footer.link', 'footer_id', string='Footer Links')
    newsletter_cta = fields.Char(string='Newsletter CTA')
    copyright_info = fields.Char(string='Copyright Info')

    @api.multi
    def render_footer(self):
        self.ensure_one()
        return {
            'footer_links': self.link_ids,
            'newsletter_cta': self.newsletter_cta,
            'copyright_info': self.copyright_info,
        }

class ThemeFooterLink(models.Model):
    _name = 'theme.footer.link'
    _description = 'Footer Link for the Theme'

    footer_id = fields.Many2one('theme.footer', string='Footer')
    name = fields.Char(string='Link Name')
    url = fields.Char(string='URL')

    @api.multi
    def render_link(self):
        self.ensure_one()
        return {
            'name': self.name,
            'url': self.url,
        }
```