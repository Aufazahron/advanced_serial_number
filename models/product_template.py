from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    default_serial_prefix_id = fields.Many2one('serial.number.prefix', string="Default Serial Prefix")