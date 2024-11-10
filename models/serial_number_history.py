from odoo import models, fields

class SerialNumberHistory(models.Model):
    _name = 'serial.number.history'
    _description = 'Serial Number History'
    
    prefix_id = fields.Many2one('serial.number.prefix', string="Prefix", required=True)
    serial_number = fields.Char(string="Serial Number", required=True)
    reference = fields.Reference(selection=[('mrp.production', 'Manufacturing Order'),
                                            ('stock.picking', 'Delivery Order'),
                                            ('repair.order', 'Repair Order')], 
                                 string="Reference")