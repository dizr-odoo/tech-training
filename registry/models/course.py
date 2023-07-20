from odoo import api, fields, models
from odoo.exceptions import ValidationError

import re

class Course(models.Model):
    _name = "motorcycle.registry"
    _description = "Course Info"
    _rec_name = "first_name"

    registry_number = fields.Char(required=True, default="MRN0000", copy=False)
    vin = fields.Char(required=True)
    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    picture = fields.Image()
    current_mileage = fields.Float()
    license_plat = fields.Char()
    certificate_title = fields.Binary()
    register_date = fields.Date()

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('registry_number', ('MRN0000')) == ('MRN0000'):
                vals['registry_number'] = self.env['ir.sequence'].next_by_code('registry.number')
        return super().create(vals_list)

    @api.constrains('vin')
    def _check_vin(self):
        vin_pattern = r'^[A-Z]{4}\d{2}[A-Z\d]{2}\d{6}$'
        for registry_number in self:
            if re.match(vin_pattern, registry_number.vin) == None:
                raise ValidationError("""The VIN must follow the pattern
                                      Make - 2 Capital Letters
                                      Model - 2 Capital Letters
                                      Year - 2 Digits
                                      Battery Capacity - 2 Capital Letters or Numbers
                                      Serial Number - 6 Digits """)
    @api.constrains('license_plat')
    def _check_license_plat(self):
        license_plat_pattern = r'^[A-Z]{1,4}\d{1,3}([A-Z]{2})?$'
        for registry_number in self:
            if re.match(license_plat_pattern, registry_number.license_plat) == None:
                raise ValidationError("""The License Plate should follow the following Pattern:
                                      1 - 4 Capital Letters
                                      1 - 3 Digits
                                      Optional 2 Capital Letters""")