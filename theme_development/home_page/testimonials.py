```python
import json
from odoo import http, fields, api, models

class Testimonials(models.Model):
    _name = 'theme.testimonials'
    _description = 'Testimonials'

    user_image = fields.Binary("User Image", attachment=True)
    user_name = fields.Char("User Name")
    testimonial_text = fields.Text("Testimonial Text")

class Website(http.Controller):
    @http.route(['/testimonials'], type='http', auth="public", website=True)
    def render_testimonials(self, **kwargs):
        testimonials = http.request.env['theme.testimonials'].sudo().search([])
        return http.request.render('theme.testimonials', {
            'testimonials': testimonials
        })

class TestimonialCarousel(models.AbstractModel):
    _name = 'theme.testimonial.carousel'
    _description = 'Testimonial Carousel'

    @api.model
    def render_testimonial_carousel(self):
        testimonials = self.env['theme.testimonials'].sudo().search([])
        testimonial_data = json.dumps([{
            'user_image': testimonial.user_image,
            'user_name': testimonial.user_name,
            'testimonial_text': testimonial.testimonial_text,
        } for testimonial in testimonials])
        return {
            'testimonial_data': testimonial_data,
        }
```