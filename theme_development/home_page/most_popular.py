```python
import json
from odoo import http, fields, api, models

class MostPopular(http.Controller):
    @http.route('/most_popular', type='http', auth='public', website=True)
    def render_most_popular(self, **kwargs):
        games = self.get_most_popular_games()
        return http.request.render('theme_development.most_popular', {
            'games': games
        })

    def get_most_popular_games(self):
        Game = http.request.env['game.store']
        games = Game.search([], order='popularity desc', limit=10)
        return games

class GameStore(models.Model):
    _name = 'game.store'
    _description = 'Game Store'

    name = fields.Char('Name')
    category = fields.Char('Category')
    price = fields.Float('Price')
    popularity = fields.Integer('Popularity')
    image = fields.Binary('Image')
    discount_price = fields.Float('Discount Price')
    is_discounted = fields.Boolean('Is Discounted')

    @api.onchange('discount_price')
    def _onchange_discount_price(self):
        if self.discount_price:
            self.is_discounted = True
        else:
            self.is_discounted = False
```
This Python code creates a controller for the "Most Popular" section of the home page. It fetches the most popular games from the 'game.store' model and passes them to the 'theme_development.most_popular' template. The 'game.store' model is also defined with fields for name, category, price, popularity, image, discount price, and a boolean field to check if the game is discounted. An onchange method is added to update the 'is_discounted' field whenever the 'discount_price' field is changed.