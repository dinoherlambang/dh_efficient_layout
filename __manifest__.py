# -*- coding: utf-8 -*-
{
    'name': 'DH Efficient Layout',
    'version': '13.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'Professional document layouts for reports',
    'description': """
DH Efficient Layout
===================

This module adds professional layout options for Odoo reports.

**Spacey Layout:**
* Modern spacey design with enhanced visual elements
* 3-section header: Company Logo (left), Document Info (center), Company Details (right)
* Styled document title and number in the center
* Enhanced company information display
* Clean footer with centered page numbers

Features:
* Compatible with all standard Odoo reports (Invoices, Sales Orders, Purchase Orders, etc.)
* Automatic document type detection
* Professional styling with proper spacing
* Follows Odoo 13 standard layout implementation

Usage:
------
1. Go to Settings > Companies > Configure Document Layout
2. Select "Spacey Layout" from the layout options
3. The layout will be applied to all reports automatically

No complex configuration needed - uses Odoo's standard layout selection mechanism.
    """,
    'author': 'Dino Herlambang',
    'website': 'https://github.com/dinoherlambang',
    'license': 'LGPL-3',
    
    # MODULE LOADING ORDER CONTROL
    # High sequence ensures this module loads AFTER potentially conflicting modules
    # like stock_picking_group_by_partner_by_carrier, stock_secondary_unit, etc.
    # This prevents template inheritance conflicts in delivery reports
    'sequence': 1000,  # High sequence = loads later = takes precedence
    'depends': [
        'base',
        'web',
        'account',  # Required for invoice template inheritance
        'sale',     # Required for sales order template inheritance
        'purchase', # Required for purchase order template inheritance
        'stock',    # Required for delivery note template inheritance
    ],
    'data': [
        'views/report_templates.xml',
        'views/invoice_inherit.xml',
        'views/sale_order_inherit.xml',
        'views/purchase_order_inherit.xml',
        'views/delivery_note_inherit.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}