# DH Efficient Layout

Professional document layout for Odoo 13 reports.

## Overview

This module provides a professional **Spacey Layout** option for Odoo reports that features enhanced visual design and follows Odoo's standard layout implementation patterns. The layout includes a sophisticated 3-section header, clean content formatting, and simplified footer design.

## Features

### Spacey Layout
- **Professional 3-section header design:**
  - **Left**: Company Logo with optimal sizing
  - **Center**: Document title with enhanced typography (18px, uppercase, blue color #2C5282)
  - **Right**: Company information with right-aligned layout and refined typography
- **Smart document type detection:**
  - Stock Operations (Transfer, Delivery, Receipt)
  - Account Documents (Invoice, Credit Note, Vendor Bill, etc.)
  - Sales Orders and Purchase Orders
  - Generic document fallback with consistent styling
- **Clean footer design:**
  - **Merged layout**: Combined company information (8 columns)
  - **Simple page numbering**: "Page X / Y" format without decorations (4 columns)
  - **Minimal styling**: No borders, boxes, or unnecessary decorations
- **Content formatting system:**
  - **Professional table styling**: Matches Clean layout standards
  - **Dynamic color scheme**: Uses company's primary (#2C5282) and secondary colors
  - **Bootstrap integration**: Responsive grid system with proper spacing
  - **Print optimization**: Enhanced readability for PDF generation

## Installation

1. Copy this module to your Odoo addons directory
2. Update the apps list in Odoo
3. Install the "DH Efficient Layout" module

## Usage

1. Go to **Settings** > **Companies** > **Configure Document Layout**
2. Select **"Spacey Layout"** from the available options
3. The selected layout will be automatically applied to all reports

## Supported Document Types

The layout automatically detects and formats these document types with consistent styling:
- **Account Documents**: Invoices, Bills, Credit Notes, Refunds
- **Sales Documents**: Sales Orders, Quotations
- **Purchase Documents**: Purchase Orders, Requests for Quotation
- **Stock Operations**: Delivery Orders, Receipts, Internal Transfers
- **Generic Documents**: Automatic fallback with professional formatting

## Content Formatting System

The Spacey Layout includes a sophisticated content formatting system that controls how document content is displayed:

### CSS Styling Integration
- **Dynamic CSS Generation**: Integrates with Odoo's `web.styles_company_report` template
- **Company Color Scheme**: Automatically uses your company's primary and secondary colors
- **Professional Table Styling**: Clean borders, headers, and formatting that matches Clean layout standards
- **Typography Enhancement**: Consistent heading styles and text formatting throughout documents

### Table Formatting Features
- **Header Styling**: Professional table headers with company secondary color
- **Border System**: Clean 3px borders for professional appearance
- **Total Sections**: Enhanced formatting for invoice totals and subtotals
- **Responsive Design**: Proper spacing and alignment across different document types

## Technical Implementation

### Architecture
- **Standard Compliance**: Follows Odoo 13 `external_layout_*` template conventions
- **Content Area Compatibility**: Uses identical body structure to `external_layout_clean` for maximum compatibility
- **CSS Integration**: Inherits from `web.styles_company_report` for dynamic styling
- **Bootstrap Framework**: Leverages Odoo's Bootstrap 4 classes for responsive design

### Key Components
- **Header Template**: 3-section responsive header with enhanced typography
- **Content Area**: Standard Odoo content injection with `web.address_layout` and `t-raw="0"`
- **CSS Styling**: Dynamic color generation using company theme colors
- **Footer Design**: Simplified 2-column footer with clean page numbering

### Quality Assurance
- **QWeb Validation**: All templates validated for proper syntax
- **Database Integration**: Properly registers with `report.layout` model
- **Module Standards**: Follows Odoo module development best practices

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

The layout provides multiple customization options:

### Template Customization
- **Header Sections**: Modify logo positioning, document title styling, or company information layout
- **Color Scheme**: Customize colors by modifying CSS variables or company theme settings
- **Typography**: Adjust font sizes, weights, and spacing in the template
- **Footer Layout**: Modify column distribution or page numbering format

### CSS Styling Customization
The template includes comprehensive CSS rules in `views/report_templates.xml`:
- **Content Formatting**: Table styling, borders, and text formatting rules
- **Company Branding**: Dynamic color integration with company theme
- **Print Optimization**: Specific styling for PDF generation

### Document Type Detection
Add or modify document type detection logic in the template's conditional blocks:
```xml
<t t-if="o._name == 'your.custom.model'">
    <!-- Custom document type handling -->
</t>
```

## Technical Details

- **Odoo Version**: 13.0+ (Community and Enterprise)
- **Dependencies**: `base`, `web` (standard Odoo core modules)
- **License**: LGPL-3
- **Template ID**: `external_layout_spacey`
- **Model Integration**: `report.layout` (standard Odoo layout system)
- **CSS Integration**: `web.styles_company_report` (dynamic styling system)
- **Color System**: Uses company primary (#2C5282 default) and secondary colors

## Development Notes

### Content Area Implementation
The layout's content/body area is architecturally identical to `external_layout_clean` to ensure full compatibility with all Odoo documents. The key difference lies in the CSS styling system that controls how content is formatted and displayed.

### CSS Generation Process
1. **Layout Selection**: When user selects "Spacey Layout" 
2. **CSS Generation**: Odoo generates CSS rules using company colors
3. **Content Styling**: Document tables, text, and formatting are styled automatically
4. **Print Rendering**: CSS rules optimize appearance for PDF generation

### Template Structure
```xml
<!-- Header: Custom 3-section design -->
<div class="header">...</div>

<!-- Content: Standard Odoo content injection -->
<div class="article o_report_layout_spacey">
    <t t-call="web.address_layout"/>
    <t t-raw="0"/>
</div>

<!-- Footer: Clean 2-column layout -->
<div class="footer">...</div>

<!-- CSS: Dynamic styling rules -->
<template inherit_id="web.styles_company_report">...</template>
```

## Author

**Dino Herlambang**
- GitHub: [dinoherlambang](https://github.com/dinoherlambang)

## License

This module is licensed under LGPL-3.