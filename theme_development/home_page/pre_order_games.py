```python
from odoo import api, fields, models

class PreOrderGames(models.Model):
    _name = 'theme_gaming.pre_order_games'
    _description = 'Pre-Order Games'

    name = fields.Char('Game Name', required=True)
    image = fields.Binary('Game Image', attachment=True)
    release_date = fields.Date('Release Date')
    teaser = fields.Html('Teaser')

    @api.model
    def create(self, vals):
        record = super(PreOrderGames, self).create(vals)
        self.env['theme_gaming.update'].create({
            'message': f"New game {record.name} available for pre-order!",
            'game_id': record.id,
        })
        return record

class PreOrderGamesUpdate(models.Model):
    _name = 'theme_gaming.update'
    _description = 'Pre-Order Games Update'

    message = fields.Char('Update Message', required=True)
    game_id = fields.Many2one('theme_gaming.pre_order_games', string='Game')

    def render_pre_order_games(self):
        pre_order_games = self.env['theme_gaming.pre_order_games'].search([])
        return {
            'pre_order_games': pre_order_games,
        }
```