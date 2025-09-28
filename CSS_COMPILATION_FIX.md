# CSS Compilation Error Fix Guide

## Problem Description

The Spacey Layout module is causing CSS compilation errors in Odoo:

```
Error: Invalid CSS after "...family: 'Lato';": expected "}", was "#000000;"
```

This error occurs because our CSS template inheritance contains syntax that conflicts with Odoo's SCSS compiler. The issue appears when:
- Installing the dh_efficient_layout module
- Generating PDF reports (invoices, etc.)
- The error disappears when the module is uninstalled

## Root Cause

The problem is in the `spacey_layout_styles` template that inherits from `web.styles_company_report`. The QWeb template variables `<t t-esc='primary'/>` and `<t t-esc='secondary'/>` are being inserted into CSS in a way that breaks SCSS compilation.

## Solution Options

### Option 1: Completely Remove CSS Inheritance (RECOMMENDED)

This is the safest approach - remove the problematic CSS template entirely and rely on inline styles in the main template.

**Steps:**

1. **Backup the current template file:**
   ```bash
   cp /path/to/dh_efficient_layout/views/report_templates.xml /path/to/dh_efficient_layout/views/report_templates.xml.backup
   ```

2. **Remove the entire CSS inheritance template section:**
   
   Delete everything from line ~135 to ~200 (the entire `spacey_layout_styles` template block):
   ```xml
   <!-- DELETE THIS ENTIRE SECTION -->
   <template id="spacey_layout_styles" inherit_id="web.styles_company_report">
       <xpath expr="//t[@t-if=&quot;layout == 'web.external_layout_background'&quot;]" position="after">
           <!-- ... all the CSS content ... -->
       </xpath>
   </template>
   <!-- DELETE UP TO HERE -->
   ```

3. **Add inline styles to the main template instead:**
   
   In the `external_layout_spacey` template, add a `<style>` section in the header:
   ```xml
   <template id="external_layout_spacey">
       <style>
           .o_report_layout_spacey table {
               border-collapse: collapse;
               width: 100%;
               margin: 15px 0;
           }
           .o_report_layout_spacey table thead tr th {
               border-top: 2px solid #333 !important;
               border-bottom: 2px solid #333 !important;
               padding: 8px 5px;
               font-weight: bold;
           }
           .o_report_layout_spacey table tbody tr td {
               border-bottom: 1px solid #dee2e6;
               padding: 6px 5px;
           }
           .o_report_layout_spacey table tbody tr:last-child td {
               border-bottom: 2px solid #333 !important;
           }
           .o_spacey_footer {
               border-top: 2px solid #333;
               margin-top: 25px;
               padding-top: 15px;
           }
           .o_report_layout_spacey #total {
               border-top: 1px solid #333;
               margin-top: 15px;
               padding-top: 10px;
           }
       </style>
       
       <!-- Rest of the template remains the same -->
       <div t-attf-class="header o_company_#{company.id}_layout" t-att-style="report_header_style">
           <!-- ... existing header content ... -->
       </div>
       <!-- ... rest of template ... -->
   </template>
   ```

### Option 2: Simplify CSS Template (ALTERNATIVE)

If you want to keep the dynamic color system, try this minimal approach:

**Replace the entire `spacey_layout_styles` template with:**

```xml
<template id="spacey_layout_styles" inherit_id="web.styles_company_report">
    <xpath expr="//t[@t-foreach=&quot;company_ids&quot;]/t[last()]" position="after">
        <t t-if="company.external_report_layout_id.key == 'dh_efficient_layout.external_layout_spacey'">
            .o_company_<t t-esc="company.id"/>_layout.o_report_layout_spacey table thead tr th {
                border-top: 2px solid <t t-esc="secondary"/> !important;
                border-bottom: 2px solid <t t-esc="secondary"/> !important;
            }
            .o_company_<t t-esc="company.id"/>_layout.o_report_layout_spacey table tbody tr:last-child td {
                border-bottom: 2px solid <t t-esc="secondary"/> !important;
            }
        </t>
    </xpath>
</template>
```

### Option 3: Use Static CSS File (MOST STABLE)

Create a separate CSS file instead of template inheritance:

1. **Create a static CSS file:**
   ```bash
   mkdir -p /path/to/dh_efficient_layout/static/src/scss
   ```

2. **Create file `/static/src/scss/spacey_layout.scss`:**
   ```scss
   .o_report_layout_spacey {
       table {
           border-collapse: collapse;
           width: 100%;
           margin: 15px 0;
           
           thead tr th {
               border-top: 2px solid #333 !important;
               border-bottom: 2px solid #333 !important;
               padding: 8px 5px;
               font-weight: bold;
           }
           
           tbody tr {
               td {
                   border-bottom: 1px solid #dee2e6;
                   padding: 6px 5px;
               }
               
               &:last-child td {
                   border-bottom: 2px solid #333 !important;
               }
           }
       }
       
       #total {
           border-top: 1px solid #333;
           margin-top: 15px;
           padding-top: 10px;
       }
   }

   .o_spacey_footer {
       border-top: 2px solid #333;
       margin-top: 25px;
       padding-top: 15px;
   }
   ```

3. **Add to manifest data:**
   ```python
   'data': [
       'views/report_templates.xml',
   ],
   'assets': {
       'web.report_assets_common': [
           'dh_efficient_layout/static/src/scss/spacey_layout.scss',
       ],
   },
   ```

## Testing Steps

After applying any fix:

1. **Restart Odoo:**
   ```bash
   service odoo restart
   # or
   sudo systemctl restart odoo
   ```

2. **Upgrade the module:**
   - Go to Apps
   - Search for "DH Efficient Layout"
   - Click Upgrade

3. **Test invoice generation:**
   - Create or open an invoice
   - Set company layout to "Spacey Layout"
   - Try to print PDF
   - Check logs for CSS compilation errors

4. **Verify no errors in logs:**
   ```bash
   tail -f /var/log/odoo/odoo-server.log | grep -i "error\|warning"
   ```

## Emergency Rollback

If issues persist:

1. **Quick disable:**
   ```bash
   # Rename the module directory temporarily
   mv /path/to/dh_efficient_layout /path/to/dh_efficient_layout_disabled
   service odoo restart
   ```

2. **Or uninstall via UI:**
   - Apps → Search "DH Efficient Layout" → Uninstall

## Recommended Approach

**Use Option 1 (Remove CSS Inheritance)** as it's the most stable and eliminates the root cause of the compilation conflict. The styling will still work perfectly with inline CSS, just without dynamic company colors.

## Files to Modify

- Primary: `/path/to/dh_efficient_layout/views/report_templates.xml`
- Backup location: `/path/to/dh_efficient_layout/views/report_templates.xml.backup`

## Expected Outcome

After the fix:
- ✅ No CSS compilation warnings/errors
- ✅ Invoice PDF generation works smoothly  
- ✅ Spacey layout displays with professional borders
- ✅ No interference with other Odoo functionality

---

*Created: 2025-09-28*  
*Module: dh_efficient_layout*  
*Issue: CSS compilation error in production*