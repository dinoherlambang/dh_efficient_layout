# DH Efficient Layout

Professional document layout for Odoo 13 reports.

## Overview

This module provides a professional **Spacey Layout** option for Odoo reports that can be selected through the standard Odoo layout configuration.

## Features

### Spacey Layout
- **Modern spacey design** with enhanced visual elements
- **3-section header layout:**
  - **Left**: Company Logo (responsive sizing)
  - **Center**: Styled document title and number with background box
  - **Right**: Enhanced company information with contact details
- **Smart document type detection:**
  - Invoices (Draft/Posted)
  - Credit Notes
  - Sales Orders/Quotations with state detection
  - Purchase Orders
  - Stock Pickings (Delivery/Receipt/Transfer)
  - Payment Receipts
  - Generic document fallback
- **Enhanced footer**: Centered page numbers with styled background
- **Clean design**: Uses Bootstrap classes and proper spacing
- **Print-friendly**: Optimized styling for print output

## Installation

1. Copy this module to your Odoo addons directory
2. Update the apps list in Odoo
3. Install the "DH Efficient Layout" module

## Usage

1. Go to **Settings** > **Companies** > **Configure Document Layout**
2. Select **"Spacey Layout"** from the available options
3. The selected layout will be automatically applied to all reports

## Supported Document Types

The layout automatically detects and properly formats:
- Account Moves (Invoices, Bills, Credit Notes)
- Sales Orders and Quotations
- Purchase Orders
- Stock Pickings (Delivery Orders, Receipts, Transfers)
- Payment Receipts
- Generic Documents

## Technical Implementation

- **Follows Odoo 13 standards**: Uses `external_layout_*` template naming convention
- **Bootstrap integration**: Leverages Odoo's Bootstrap classes for responsive design
- **Inline styling**: Uses inline styles for better print compatibility
- **Standard registration**: Registers with `report.layout` model like built-in layouts

## File Structure

```
dh_efficient_layout/
├── __init__.py
├── __manifest__.py
├── README.md
└── views/
    └── report_templates.xml
```

## Customization

The layout can be easily customized by modifying the template in `views/report_templates.xml`. The template uses:
- Bootstrap 4 classes for layout structure
- Inline CSS for specific styling
- QWeb conditional rendering for document type detection

## Technical Details

- **Odoo Version**: 13.0+
- **Dependencies**: base, web
- **License**: LGPL-3
- **Template ID**: `external_layout_spacey`
- **Model**: `report.layout`

## Author

**Dino Herlambang**
- GitHub: [dinoherlambang](https://github.com/dinoherlambang)

## License

This module is licensed under LGPL-3.