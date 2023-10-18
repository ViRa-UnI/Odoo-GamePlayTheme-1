```python
from odoo import api, fields, models

class LatestNews(models.Model):
    _name = 'theme_gaming.latest_news'
    _description = 'Latest News'

    image = fields.Binary("Image", attachment=True)
    headline = fields.Char("Headline")
    snippet = fields.Text("Snippet")

    @api.multi
    def renderLatestNews(self):
        latest_news = self.search([])
        news_cards = []
        for news in latest_news:
            news_card = {
                'image': news.image,
                'headline': news.headline,
                'snippet': news.snippet,
                'read_more_link': '/news/%s' % news.id
            }
            news_cards.append(news_card)
        return news_cards
```
