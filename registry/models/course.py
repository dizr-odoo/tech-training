from odoo import fields, models

class Course(models.Model):
    _name = "motorcycle.registry"
    _description = "Course Info"
    _rec_name = "first_name"

    registry_number = fields.Char(required=True)
    vin = fields.Char(required=True)
    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    picture = fields.Image()
    current_mileage = fields.Float()
    license_plat = fields.Char()
    certificate_title = fields.Binary()
    register_date = fields.Date()