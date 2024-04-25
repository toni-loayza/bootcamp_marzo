{
    'name': "Hotels",
    'author': "Escuela Full Stack",
    'website': "https://escuelafullstack.com/",
    'summary': """Modulo para hoteles""",
    'depends': [
        'mail', 'portal', 'sale'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/hotel_room_view.xml',
        'views/sale_order_view.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_installable': False
}
