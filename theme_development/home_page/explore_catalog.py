```python
import os
from odoo import models, fields, api

class ExploreCatalog(models.Model):
    _name = 'theme_gaming.explore_catalog'
    _description = 'Explore Our Catalog Section'

    name = fields.Char(string='Name')
    image = fields.Binary(string='Image')
    parallax_effect = fields.Boolean(string='Parallax Effect')
    cta_text = fields.Char(string='CTA Text')
    cta_link = fields.Char(string='CTA Link')

    @api.model
    def render_explore_catalog(self):
        catalog_data = self.search([])
        catalog_html = """
        <section id="exploreCatalog">
            <div class="parallax-container">
                <div class="parallax">
                    <img src="data:image/png;base64,{}" alt="{}">
                </div>
                <div class="section white">
                    <div class="row container">
                        <h2 class="header">{}</h2>
                        <p class="grey-text text-darken-3 lighten-3">{}</p>
                        <a href="{}" class="waves-effect waves-light btn-large">{}</a>
                    </div>
                </div>
            </div>
        </section>
        """.format(catalog_data.image, catalog_data.name, catalog_data.name, catalog_data.name, catalog_data.cta_link, catalog_data.cta_text)
        return catalog_html
```