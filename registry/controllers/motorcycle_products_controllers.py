# -*- encoding: utf-8 -*-

from odoo import http

class MotorcycleProducts(http.Controller):
    @http.route('/registry/', auth='public', website=True)
    def index(self, **kw):
        return "Hello World!"
    
    @http.route('/registry/compare/', auth='public', website=True)
    def compare(self, **kw):
        motorcycle_products = http.request.env['product.template'].search([('detailed_type', '=','motorcycle')])
        return http.request.render('registry.compare_website',{
            'motorcycle_products': motorcycle_products,
        })
    
    