{
    'name': "Academy",
    'author': "Escuela Full Stack",
    'website': "https://escuelafullstack.com/",
    'summary': """Modulo para academia""",
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence_academy_student.xml',
        'views/academy_student_view.xml',
        'views/menu.xml'
    ],
    'installable': True,
    'application': True,
    'auto_installable': False
}
