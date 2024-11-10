from odoo import models, fields

class SerialNumberPrefix(models.Model):
    _name = 'serial.number.prefix'
    _description = 'Serial Number Prefix'
    
    name = fields.Char(string="Prefix Name", required=True)
    prefix = fields.Char(string="Prefix Code", required=True)
    serial_numbers = fields.One2many('serial.number.history', 'prefix_id', string="Serial Numbers")