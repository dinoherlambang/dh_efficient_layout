# Odoo Report Elements Control Guide

## Core Template Hierarchy

### 1. Base Layout Templates (web module)
- `web.external_layout` - Main layout controller
- `web.address_layout` - Customer address section
- `web.external_layout_standard` - Standard layout style
- `web.external_layout_clean` - Clean layout style
- `web.external_layout_boxed` - Boxed layout style
- `web.external_layout_background` - Background layout style

### 2. Document-Specific Templates

#### Invoice Templates (account module)
- `account.report_invoice_document` - Main invoice template
- Location: `/usr/lib/python3/dist-packages/odoo/addons/account/views/report_invoice.xml`

#### Sales Order Templates (sale module)
- `sale.report_saleorder_document` - Main sales order template
- Location: `/usr/lib/python3/dist-packages/odoo/addons/sale/report/sale_report_templates.xml`

#### Purchase Order Templates (purchase module)
- `purchase.report_purchaseorder_document` - Main purchase order template
- Location: `/usr/lib/python3/dist-packages/odoo/addons/purchase/report/purchase_report_templates.xml`

#### Delivery Note Templates (stock module)
- `stock.report_delivery_document` - Main delivery template
- Location: `/usr/lib/python3/dist-packages/odoo/addons/stock/report/report_deliveryslip.xml`

## Elements You Can Control

### 1. Document Title and Type
**Location**: Within each document template
**Xpath Examples**:
```xml
<!-- Invoice title -->
<xpath expr="//h2[contains(text(), 'Invoice')]" position="replace">
    <!-- Custom title or hide -->
</xpath>

<!-- Sales Order title -->
<xpath expr="//h2[@class='mt16']" position="replace">
    <!-- Custom title or hide -->
</xpath>
```

### 2. Document Name/Number
**Location**: Document-specific sections
**Xpath Examples**:
```xml
<!-- Invoice number -->
<xpath expr="//span[@t-field='o.name']" position="replace">
    <!-- Custom number format or hide -->
</xpath>
```

### 3. Customer Name and Address
**Location**: `web.address_layout` template
**Xpath Examples**:
```xml
<!-- Hide entire address block -->
<xpath expr="//t[@t-call='web.address_layout']" position="replace">
    <!-- Custom address layout or hide -->
</xpath>

<!-- Hide specific address components -->
<xpath expr="//div[@name='address']" position="replace">
    <!-- Custom address or hide -->
</xpath>

<!-- Hide information block -->
<xpath expr="//div[@name='information_block']" position="replace">
    <!-- Custom info or hide -->
</xpath>
```

### 4. Company Information (Header)
**Location**: Base layout templates
**Xpath Examples**:
```xml
<!-- Hide company logo -->
<xpath expr="//img[@t-if='company.logo']" position="replace">
    <!-- Custom logo or hide -->
</xpath>

<!-- Hide company name -->
<xpath expr="//strong[@t-field='company.partner_id.name']" position="replace">
    <!-- Custom company name or hide -->
</xpath>

<!-- Hide company address -->
<xpath expr="//div[@name='company_address']" position="replace">
    <!-- Custom company address or hide -->
</xpath>
```

### 5. VAT/Tax Information (NPWP)
**Location**: Footer sections and company details
**Xpath Examples**:
```xml
<!-- Hide VAT in footer -->
<xpath expr="//li[@t-if='company.vat']" position="replace">
    <!-- Custom VAT display or hide -->
</xpath>

<!-- Hide customer VAT -->
<xpath expr="//span[@t-field='o.partner_id.vat']" position="replace">
    <!-- Custom customer VAT or hide -->
</xpath>
```

### 6. Information Sections (Invoice Date, Due Date, etc.)
**Location**: Document-specific informations sections
**Xpath Examples**:
```xml
<!-- Invoice informations -->
<xpath expr="//div[@id='informations']" position="replace">
    <!-- Custom informations layout -->
</xpath>

<!-- Specific information fields -->
<xpath expr="//div[@name='invoice_date']" position="replace">
    <!-- Custom date display or hide -->
</xpath>

<xpath expr="//div[@name='due_date']" position="replace">
    <!-- Custom due date or hide -->
</xpath>
```

### 7. Footer Information
**Location**: Footer sections in base layouts
**Xpath Examples**:
```xml
<!-- Hide phone -->
<xpath expr="//li[@t-if='company.phone']" position="replace">
    <!-- Custom phone or hide -->
</xpath>

<!-- Hide email -->
<xpath expr="//li[@t-if='company.email']" position="replace">
    <!-- Custom email or hide -->
</xpath>

<!-- Hide website -->
<xpath expr="//li[@t-if='company.website']" position="replace">
    <!-- Custom website or hide -->
</xpath>

<!-- Hide entire footer -->
<xpath expr="//div[@class='footer']" position="replace">
    <!-- Custom footer or hide -->
</xpath>
```

## Precise Xpath Strategies

### 1. Use Named Elements
```xml
<!-- More reliable than class-based -->
<xpath expr="//div[@name='invoice_date']" position="replace">
<xpath expr="//div[@name='company_address']" position="replace">
```

### 2. Use Child Element Selectors
```xml
<!-- Target parent by child -->
<xpath expr="//div[div[@name='div_origin']]" position="replace">
<xpath expr="//div[span[@t-field='o.name']]" position="replace">
```

### 3. Use OR Logic for Conditionals
```xml
<!-- Handle conditional elements -->
<xpath expr="//div[div[@name='invoice_date'] or div[@name='due_date']]" position="replace">
```

### 4. Target by Content
```xml
<!-- Target by text content -->
<xpath expr="//strong[contains(text(), 'Invoice Date')]/.." position="replace">
```

## Conditional Display Control

### Hide Based on Conditions
```xml
<!-- Hide element conditionally -->
<xpath expr="//div[@name='vat_info']" position="attributes">
    <attribute name="t-if">False</attribute>
</xpath>

<!-- Show only for specific document types -->
<xpath expr="//div[@name='custom_section']" position="attributes">
    <attribute name="t-if">o.type == 'out_invoice'</attribute>
</xpath>
```

## Dependencies for Full Control

### Required Modules to Inherit:
1. **web** - Base layouts and address templates
2. **account** - Invoice templates
3. **sale** - Sales order templates  
4. **purchase** - Purchase order templates
5. **stock** - Delivery note templates

### Your Current Inheritance:
- ✅ account (invoice)
- ✅ sale (sales order)
- ✅ purchase (purchase order)
- ✅ stock (delivery note)
- ❌ web (base layouts) - **MISSING**

## Recommended Next Steps

1. **Add web module inheritance** to control base layouts
2. **Create address_layout override** to control customer information
3. **Add conditional logic** for selective hiding
4. **Use named element targeting** for precise xpath