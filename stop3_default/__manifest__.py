{
    'name': 'stop3',
    'version': '13.0.0.0',
    'category': 'Tools',
    'summary': "Proyecto stop3",
    'author': 'Ing. Gabriela Rivero',
    'depends': [
        'base',
    ],
    'data': [
    ],
    'installable': True,
    'application': False,

    'limit_request': '8196',
    'limit_memory_soft': '640000000',
    'limit_memory_hard': '760000000',
    'limit_time_cpu': '60',
    'limit_time_real': '120',

    # manifest version, if omitted it is backward compatible
    'env-ver': '2',

    # if Enterprise it installs in a different directory than community
    'odoo-license': 'CE',

    # port where odoo starts serving pages
    'port': '8069',

    # list of url repos to install in the form 'repo-url directory'
    'git-repos': [
        'https://github.com/regaby/cl-stop3.git',
        'https://github.com/regaby/odoo-custom.git',
        # 'https://github.com/jobiols/odoo-addons.git',
        ## localización
        'https://github.com/ingadhoc/odoo-argentina.git',
        'https://github.com/ingadhoc/odoo-argentina-ce.git',
        'https://github.com/ingadhoc/argentina-sale.git',
        'https://github.com/ingadhoc/account-payment.git',
        'https://github.com/ingadhoc/account-invoicing.git',
        'https://github.com/ingadhoc/account-financial-tools.git',
        'https://github.com/ingadhoc/sale.git',
        'https://github.com/ingadhoc/stock.git',
        'https://github.com/ingadhoc/aeroo_reports.git',
        'https://github.com/OCA/account-financial-reporting.git',
        'https://github.com/OCA/reporting-engine.git',
        'https://github.com/OCA/server-ux.git',
        'https://github.com/OCA/mis-builder.git',
        'https://github.com/OCA/sale-workflow.git',
        'https://github.com/OCA/web.git',
    ],

    'docker-images': [
        'odoo regaby/odoo-ce:13.0',
        'postgres postgres:10.1-alpine',
        'nginx nginx'
    ]
}
