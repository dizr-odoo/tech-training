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
    'depends': ['base'],
    'data': [
        'security/registry_groups.xml',
        'security/ir.model.access.csv',
        'views/registry_menuitems.xml',
    ],
    'demo': ['demo/course_demo.xml',
             ],
    'application': True,
}