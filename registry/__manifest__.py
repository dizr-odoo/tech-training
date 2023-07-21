{
    'name': 'Motorcycle Registry',
    'summary': """Manage Registration of Motorcycles""",
    'description': """Motorcycle Registry
====================
This Module is used to keep track of the Motorcycle Registration and Ownership of each motorcycled of the brand.""",
    'license': 'OPL-1',
    'author': 'dizr',
    'website': 'https://github.com/dizr-odoo/tech-training',
    'category': 'Kawiil/Kawiil',
    'depends': ['stock'],
    'data': [
        'security/registry_groups.xml',
        'security/registry_security.xml',
        'security/ir.model.access.csv',
        'data/registry_data.xml',
        'views/registry_menuitems.xml',
        'views/registry_views.xml',
        'views/product_views_inheritance.xml'
    ],
    'demo': ['demo/course_demo.xml',
             ],
    'application': True,
}