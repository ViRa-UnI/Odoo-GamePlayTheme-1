```python
from odoo import api, fields, models

class MainAnnouncement(models.Model):
    _name = 'theme.main_announcement'
    _description = 'Main Announcement'

    name = fields.Char(string='Announcement Title', required=True)
    image = fields.Binary(string='Image', required=True)
    cta_text = fields.Char(string='CTA Text', required=True)
    cta_link = fields.Char(string='CTA Link', required=True)

    @api.model
    def create(self, vals):
        record = super(MainAnnouncement, self).create(vals)
        self.env['bus.bus'].sendone(
            (self._cr.dbname, 'theme.main_announcement', record.id),
            {'type': 'new_announcement', 'announcement_id': record.id}
        )
        return record

    def write(self, vals):
        res = super(MainAnnouncement, self).write(vals)
        if 'image' in vals or 'cta_text' in vals or 'cta_link' in vals:
            self.env['bus.bus'].sendone(
                (self._cr.dbname, 'theme.main_announcement', self.id),
                {'type': 'update_announcement', 'announcement_id': self.id}
            )
        return res

    def unlink(self):
        self.env['bus.bus'].sendone(
            (self._cr.dbname, 'theme.main_announcement', self.id),
            {'type': 'delete_announcement', 'announcement_id': self.id}
        )
        return super(MainAnnouncement, self).unlink()
```