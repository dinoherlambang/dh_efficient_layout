# DH Efficient Layout

Professional document layout system for Odoo 13 reports with comprehensive document inheritance.

## Overview

This module provides a complete **Spacey Layout** system for Odoo reports that features enhanced visual design, document-specific formatting inheritance, and follows Odoo's standard layout implementation patterns. The system includes a sophisticated 3-section header, document-specific content formatting, and simplified footer design with comprehensive inheritance for all major Odoo document types.

## Features

### Complete Document System
- **Comprehensive Inheritance**: Dedicated formatting for all major document types
  - **Invoices & Credit Notes**: Enhanced informations section with Invoice Date, Due Date, Source, Customer Code, Reference
  - **Sales Orders & Quotations**: Professional layout with Customer Reference, Order Date, Salesperson, Expiration Date
  - **Purchase Orders & RFQs**: Structured formatting with Purchase Representative, Vendor Reference, Order Date
  - **Delivery Notes**: Clean presentation with Source Order and Shipping Date information
- **Document-Specific Styling**: Each document type has tailored formatting while maintaining visual consistency
- **Modular Architecture**: Separate inheritance files for easy maintenance and extensibility

### Spacey Layout Core Features
- **Professional 3-section header design:**
  - **Left**: Company Logo with optimal sizing
  - **Center**: Document title with enhanced typography and state-aware detection (18px, uppercase, blue color #2C5282)
  - **Right**: Company information with right-aligned layout and refined typography
- **Smart document type and state detection:**
  - **Account Documents**: Invoice, Draft Invoice, Cancelled Invoice, Credit Note, Vendor Credit Note, Vendor Bill
  - **Sales Documents**: Quotation (draft/sent), Sales Order (confirmed)
  - **Purchase Documents**: Request for Quotation (draft), Purchase Order (sent/confirmed), Cancelled Purchase Order
  - **Stock Operations**: Delivery Note (all picking types)
  - **Generic Documents**: Automatic fallback with consistent styling
- **Enhanced Document Headers**: All document titles and numbers appear in the unified header (no duplication)
- **Clean footer design:**
  - **Merged layout**: Combined company information (8 columns)
  - **Simple page numbering**: "Page X / Y" format without decorations (4 columns)
  - **Minimal styling**: No borders, boxes, or unnecessary decorations

### Document Content Formatting
- **Bordered Information Sections**: Professional containers with company color borders and subtle backgrounds
- **Centered Field Layout**: All field labels and values are center-aligned for clean presentation
- **Responsive Grid System**: Automatic column adjustment (col-md-4, col-sm-6) for optimal display
- **Enhanced Typography**: Consistent field label styling with company colors (#2C5282)
- **Professional Table Styling**: Clean borders and formatting that matches modern design standards
- **Company Color Integration**: Dynamic color scheme using company's primary and secondary colors

## Installation

1. Copy this module to your Odoo addons directory
2. Update the apps list in Odoo
3. Install the "DH Efficient Layout" module
4. **Dependencies**: The module automatically handles dependencies for `account`, `sale`, `purchase`, and `stock` modules for comprehensive document support

## Usage

1. Go to **Settings** > **Companies** > **Configure Document Layout**
2. Select **"Spacey Layout"** from the available options
3. The selected layout will be automatically applied to all reports with document-specific formatting

## Supported Document Types with Inheritance

The layout system provides dedicated inheritance and formatting for these document types:

### Account Module Documents
- **Invoices**: Enhanced informations section with Invoice Date, Due Date, Source, Customer Code, Reference
- **Credit Notes**: Professional formatting with Credit Note Date and relevant fields
- **Vendor Bills**: Structured layout with vendor-specific information
- **Draft/Cancelled States**: Proper state indication in document headers

### Sales Module Documents  
- **Sales Orders**: Professional layout with Customer Reference, Order Date, Salesperson, Expiration Date
- **Quotations**: Clean presentation with quotation-specific fields and expiration dates
- **State-Aware Headers**: Automatic detection between Quotations and confirmed Sales Orders

### Purchase Module Documents
- **Purchase Orders**: Structured formatting with Purchase Representative, Vendor Reference, Order Date/Deadline
- **Requests for Quotation**: Professional RFQ layout with appropriate field presentation
- **State Detection**: Automatic handling of draft, sent, confirmed, and cancelled states

### Stock Module Documents
- **Delivery Notes**: Clean presentation with Source Order and Shipping Date information
- **All Picking Types**: Universal formatting for deliveries, receipts, and internal transfers

### Fallback Support
- **Generic Documents**: Professional formatting for any other document types using the layout system

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
├── INHERITANCE_SUMMARY.md
└── views/
    ├── report_templates.xml      # Main Spacey Layout template
    ├── invoice_inherit.xml       # Invoice & Credit Note inheritance
    ├── sale_order_inherit.xml    # Sales Order & Quotation inheritance
    ├── purchase_order_inherit.xml # Purchase Order & RFQ inheritance
    └── delivery_note_inherit.xml # Delivery Note inheritance
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
### Document Type Detection
Add or modify document type detection logic in the template's conditional blocks:
```xml
<t t-if="o._name == 'your.custom.model'">
    <!-- Custom document type handling -->
</t>
```

## Document Inheritance System

### Architecture Overview
The module uses a **modular inheritance architecture** where each document type has its own dedicated inheritance file. This approach provides:

- **Separation of Concerns**: Each document type's formatting is isolated in its own file
- **Easy Maintenance**: Changes to one document type don't affect others  
- **Extensibility**: New document types can be easily added without modifying existing templates
- **Consistency**: All documents share the unified header/footer while having customized content areas

### Inheritance Files and Their Purpose

#### `invoice_inherit.xml` - Account Module Documents
- **Inherits**: `account.report_invoice_document`
- **Customizes**: Invoice Date, Due Date, Source, Customer Code, Reference fields
- **Removes**: Original invoice title (moved to header)
- **Styling**: Bordered information section with centered field layout

#### `sale_order_inherit.xml` - Sales Module Documents  
- **Inherits**: `sale.report_saleorder_document`
- **Customizes**: Customer Reference, Order/Quotation Date, Expiration, Salesperson
- **Handles**: State detection between quotations and confirmed orders
- **Removes**: Original sales order title (moved to header)

#### `purchase_order_inherit.xml` - Purchase Module Documents
- **Inherits**: `purchase.report_purchaseorder_document` 
- **Customizes**: Purchase Representative, Vendor Reference, Order Date/Deadline
- **Handles**: Multiple purchase order states and title variations
- **Removes**: All original purchase order titles (moved to header)

#### `delivery_note_inherit.xml` - Stock Module Documents
- **Inherits**: `stock.report_delivery_document`
- **Customizes**: Source Order, Shipping Date information
- **Adds**: Professional information section structure (original has minimal formatting)
- **Removes**: Original delivery note title (moved to header)

### Header Integration
All document titles and states are now handled in the **main layout header** (`report_templates.xml`):

```xml
<!-- Account Move (Invoice) with States -->
<t t-elif="o._name == 'account.move'">
    <span t-if="o.type == 'out_invoice' and o.state == 'posted'">Invoice</span>
    <span t-if="o.type == 'out_invoice' and o.state == 'draft'">Draft Invoice</span>
    <!-- ... more states ... -->
</t>

<!-- Sales Order with States -->
<t t-elif="o._name == 'sale.order'">
    <span t-if="o.state in ['draft', 'sent']">Quotation</span>
    <span t-if="o.state not in ['draft', 'sent']">Sales Order</span>
</t>

<!-- Purchase Order with States -->
<t t-elif="o._name == 'purchase.order'">
    <span t-if="o.state == 'draft'">Request for Quotation</span>
    <span t-if="o.state in ['sent', 'to approve']">Purchase Order</span>
    <!-- ... more states ... -->
</t>
```

This unified approach ensures:
- **No Title Duplication**: Document titles appear only in the header
- **Consistent Positioning**: All document types show their title in the same location
- **State Awareness**: Headers automatically reflect document states (Draft, Posted, Cancelled, etc.)
- **Professional Appearance**: Clean document body focused on content rather than redundant titles

## Development Notes
```

## Technical Details

- **Odoo Version**: 13.0+ (Community and Enterprise)
- **Dependencies**: `base`, `web`, `account`, `sale`, `purchase`, `stock` (handles all major document types)
- **License**: LGPL-3
- **Template ID**: `external_layout_spacey`
- **Model Integration**: `report.layout` (standard Odoo layout system)
- **CSS Integration**: `web.styles_company_report` (dynamic styling system)
- **Color System**: Uses company primary (#2C5282 default) and secondary colors
- **Architecture**: Modular inheritance system with separate files for each document type

## Development Notes

### How Odoo's Layout System Works

Understanding Odoo's layout adaptation mechanism is crucial for proper implementation:

#### The Layout Dispatcher Pattern
Odoo uses a sophisticated dispatcher system where all base addons (account, sale, stock, purchase, etc.) use a generic call:

```xml
<!-- All reports use this generic call -->
<t t-call="web.external_layout">
    <!-- Document content goes here -->
</t>
```

#### The Core Mechanism
The `web.external_layout` template acts as a **dispatcher** that dynamically selects the appropriate layout:

```xml
<!-- From web/views/report_templates.xml -->
<template id="external_layout">
    <!-- Company and document context setup -->
    <t t-if="company.external_report_layout_id" 
       t-call="{{company.external_report_layout_id.key}}">
        <t t-raw="0"/>
    </t>
    <t t-else="" t-call="web.external_layout_standard">
        <t t-raw="0"/>
    </t>
</template>
```

#### Key Components:
1. **Dynamic Template Calling**: `t-call="{{company.external_report_layout_id.key}}"` 
2. **Runtime Resolution**: Layout is determined when the report is generated
3. **Fallback System**: Uses `web.external_layout_standard` if no layout is selected
4. **Universal Compatibility**: All existing reports automatically support any new layout

#### Layout Registration System:
- **Standard Layout**: `key = "web.external_layout_standard"`
- **Clean Layout**: `key = "web.external_layout_clean"`
- **Boxed Layout**: `key = "web.external_layout_boxed"`
- **Background Layout**: `key = "web.external_layout_background"`
- **Our Spacey Layout**: `key = "dh_efficient_layout.external_layout_spacey"`

This explains why our custom layout works seamlessly with:
- Invoice reports (`account` module)
- Sales orders (`sale` module) 
- Purchase orders (`purchase` module)
- Delivery slips (`stock` module)
- All other standard and custom reports

### Content Area Implementation
The layout's content/body area is architecturally identical to `external_layout_clean` to ensure full compatibility with all Odoo documents. The key difference lies in the CSS styling system that controls how content is formatted and displayed.

### Content Formatting Differences Between Layouts

During development, we discovered that different layouts (Standard, Clean, Boxed, Background) produce different content formatting even though they use identical content area structure. Here's how it works:

#### The Content Area Structure (Identical Across All Layouts):
```xml
<div class="article o_report_layout_[name] o_company_#{company.id}_layout" 
     t-att-data-oe-model="o and o._name" 
     t-att-data-oe-id="o and o.id" 
     t-att-data-oe-lang="o and o.env.context.get('lang')">
    <t t-call="web.address_layout"/>
    <t t-raw="0"/>
</div>
```

#### The Formatting Control System:
The visual differences come from **CSS styling rules** that target the layout-specific class:

1. **CSS Class Assignment**: Each layout assigns its own class (`o_report_layout_clean`, `o_report_layout_spacey`, etc.)
2. **Dynamic CSS Generation**: The `web.styles_company_report` template generates CSS rules conditionally
3. **Content Styling**: CSS rules control table borders, text colors, heading styles, and spacing

#### Example CSS Generation Pattern:
```xml
<!-- From web.styles_company_report -->
<t t-elif="layout == 'web.external_layout_clean'">
    /* Clean layout specific styling */
    &.o_report_layout_clean {
        table { /* table styling */ }
        h1, h2, h3 { /* heading styling */ }
    }
</t>
<t t-elif="layout == 'dh_efficient_layout.external_layout_spacey'">
    /* Our spacey layout styling */
    &.o_report_layout_spacey {
        table { /* our table styling */ }
        h1, h2, h3 { /* our heading styling */ }
    }
</t>
```

This system allows:
- **Consistent Content Structure**: All layouts use the same content injection mechanism
- **Visual Differentiation**: Each layout can have unique styling for tables, text, and elements
- **Company Branding**: Dynamic color integration using company theme colors

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