from odoo import api, models, fields

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    custom_serial_number = fields.Char(string="Serial Number", readonly=True)

    def button_confirm(self):
        if not self.custom_serial_number:
            # Assign default prefix if available
            prefix = self.product_id.default_serial_prefix_id.prefix or 'XX'
            # Generate new sequence based on prefix
            sequence_code = f'serial.number.{prefix.lower()}'
            serial_number = self.env['ir.sequence'].next_by_code(sequence_code)

            # Store serial number
            self.custom_serial_number = f"{prefix}{serial_number}"

            # Record in history
            self.env['serial.number.history'].create({
                'prefix_id': self.product_id.default_serial_prefix_id.id,
                'serial_number': self.custom_serial_number,
                'reference': f"mrp.production,{self.id}"
            })
            return super(MrpProduction, self).button_confirm()