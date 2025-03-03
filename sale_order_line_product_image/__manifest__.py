# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
	'name': "Product Image On Sale Order Line",
	'version': "18.0.0.0",
	'category': "Sales",
	'license':'LGPL-3',
	'summary': "Display product image on sale order line print product image on sale order report print image on sale order line product image print product image on sale line product image in sale order line print Product image on sales order line",
	'description': """
	
			Display product image on sale order line. It will also display product image on sale order report. 
	
			Product Image On Sale Order Line in odoo,
			Sale report with product image in odoo,
			product image on sale order line and sale report in odoo,
			Identify product via image in odoo,
			Identify priduct via image on sale report in odoo,

	""",
	'author': "BROWSEINFO",
	"website" : "https://www.browseinfo.com/demo-request?app=sale_order_line_product_image&version=18&edition=Community",
    'depends': ['base', 'sale_management'],
	'data': [
			'report/sale_order_report.xml',
			'views/view_sale_order.xml',
			],
	'currency': "EUR",
	'demo': [],
	'installable': True,
	'auto_install': False,
	'application': False,
	"live_test_url":'https://www.browseinfo.com/demo-request?app=sale_order_line_product_image&version=18&edition=Community',
	"images":['static/description/Banner.gif'],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
