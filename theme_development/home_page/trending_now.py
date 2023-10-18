```python
import json
from odoo import http, fields, api, models

class TrendingNow(models.Model):
    _name = 'theme_gaming.trending_now'
    _description = 'Trending Now Games'

    name = fields.Char('Game Name')
    image = fields.Binary('Game Image')
    is_trending = fields.Boolean('Is Trending')

    @api.model
    def get_trending_games(self):
        trending_games = self.search([('is_trending', '=', True)])
        return trending_games

class Website(http.Controller):

    @http.route(['/trending_now'], type='http', auth='public', website=True)
    def render_trending_now(self):
        trending_games = http.request.env['theme_gaming.trending_now'].get_trending_games()
        return http.request.render('theme_gaming.trending_now', {
            'trending_games': trending_games
        })

class TrendingNowTemplate(models.AbstractModel):
    _name = 'theme_gaming.trending_now_template'
    _description = 'Trending Now Template'
    _inherit = 'theme.utils'

    def _theme_gaming_post_copy(self, mod):
        self.disable_view('website.template_trending_now')
        self.enable_view('theme_gaming.template_trending_now')
```
This Python code creates a model for the trending games, a controller to render the trending games on the website, and a template for the trending games section. The model has fields for the game name, image, and a boolean to check if the game is trending. The controller uses the model's method to get the trending games and passes them to the template. The template is enabled and the default one is disabled when the theme is applied.