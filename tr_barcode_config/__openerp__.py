# -*- coding: utf-8 -*-
#################################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011 Julius Network Solutions SARL <contact@julius.fr>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#################################################################################

{
    "name" : "Barcode configuration Module",
    "version" : "1.0",
    "author" : "Julius Network Solutions,Odoo Community Association (OCA)",
    "description" : """

Presentation:

This module adds a configuration object and barcode osv to manage the barcode.
You should define your object like this to manage automatically the creation / edition of your barcode:

from tr_barcode_config.barcode import barcode_osv

class product_product(barcode_osv.barcode_osv):
    _inherit = 'product.product'

""",
    "website" : "http://www.julius.fr",
    "depends" : [
        "tr_barcode",
        "tr_barcode_field",
    ],
    "category" : "Customs/Stock",
    "init_xml" : [],
    "demo_xml" : [],
    "update_xml" : [
        'barcode_config_view.xml',
        "security/ir.model.access.csv",
    ],
    'test': [],
    'installable': True,
    'active': False,
}

