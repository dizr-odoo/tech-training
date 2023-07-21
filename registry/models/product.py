# -*- coding: utf-8 -*-
from odoo import api, fields, models

class Product(models.Model):
    _inherit = 'product.template'

    horsepower = fields.Float()
    top_speed = fields.Float()
    torque = fields.Float()
    battery_capacity = fields.Char()
    charge_time = fields.Float()
    range = fields.Float()
    curb_weight = fields.Float()
    make = fields.Char()
    model = fields.Char()
    launch_date = fields.Date()

    detailed_type = fields.Selection(selection_add=[
        ('motorcycle', 'Motorcycle'),
        ], ondelete={'motorcycle': 'set product'})
    

    
    def _detailed_type_mapping(self):
        type_mapping = super()._detailed_type_mapping()
        type_mapping['motorcycle'] = 'product'
        return type_mapping