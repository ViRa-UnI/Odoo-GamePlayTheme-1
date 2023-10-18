```python
from odoo import api, fields, models

class ThemeCategories(models.Model):
    _name = 'theme.categories'
    _description = 'Theme Categories'

    name = fields.Char('Category Name', required=True)
    image = fields.Binary('Category Image', attachment=True)
    description = fields.Text('Description')
    top_games = fields.Many2many('product.template', string='Top Games')

    @api.multi
    def render_categories(self):
        categories = self.search([])
        for category in categories:
            category_html = """
                <div class="category" onmouseover="showTopGames({})">
                    <img src="data:image/png;base64,{}" alt="{}">
                    <div class="tooltip">{}</div>
                </div>
            """.format(category.id, category.image.decode('utf-8'), category.name, category.description)
            self.env['web_editor.assets'].add(category_html)

    @api.multi
    def show_top_games(self, category_id):
        category = self.browse(category_id)
        top_games_html = """
            <div class="dropdown">
                <ul>
        """
        for game in category.top_games:
            top_games_html += "<li>{}</li>".format(game.name)
        top_games_html += """
                </ul>
            </div>
        """
        self.env['web_editor.assets'].add(top_games_html)
```