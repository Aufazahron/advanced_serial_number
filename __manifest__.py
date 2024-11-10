{
    'name': 'Advanced Serial Number Management',
    'version': '1.0',
    'summary': 'Manage prefixes, generate serial numbers, and track usage across Manufacturing Orders',
    'description': 'Adds functionality to manage custom prefixes, generate unique serial numbers on order confirmation, and track serial number usage.',
    'author': 'Your Name',
    'category': 'Manufacturing',
    'depends': ['mrp', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/serial_number_prefix_views.xml',
        'views/product_template_views.xml',
        'views/mrp_production_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}