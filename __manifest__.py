# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : ' Gestion des chantiers',
    'version' : '0.1',
    'category': 'Gestion de projets',

    'description' : """
Main Features
-------------


""",
    'depends': [
        'sale',
        'partner_wkf',
    ],
    'data': [
       # 'report/layouts.xml',
        'report/report.xml',
        'report/bordereau.xml',
       'views/sale_order_view.xml',
       'views/account_invoice_view.xml',
       'report/sale_order_report_template.xml',
       'report/report_invoice.xml'
    ],

    'demo': [],

    'installable': True,
    'application': False,
}
