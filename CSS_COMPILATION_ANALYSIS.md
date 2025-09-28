# CSS Compilation Error Analysis

## Error Details

**Error Message:**
```
Error: Invalid CSS after "...family: 'Lato';": expected "}", was "#000000;"
on line 3753:37 of /stdin
```

**Bundle Affected:**
`web.report_assets_common` - This is Odoo's main CSS bundle for reports

## Root Cause Analysis

### 1. **Error Location**
- Line 3753:37 in the compiled SCSS
- The error occurs after `font-family: 'Lato';`
- SCSS compiler expects `}` but finds `#000000;` (a color value)

### 2. **Likely Causes**

#### **Option A: QWeb Template Variable Issue**
Our CSS template uses:
```css
color: <t t-esc='primary'/>;
color: <t t-esc='secondary'/>;
```

**Problem**: If `primary` or `secondary` variables are not properly formatted or contain invalid characters, they could break CSS compilation.

#### **Option B: SCSS Syntax Conflict** 
Our CSS might be conflicting with SCSS compilation when mixed with other stylesheets.

#### **Option C: Template Inheritance Position**
Our CSS injection point might be interfering with existing SCSS compilation.

## Diagnostic Steps

### Step 1: Check Company Colors
```sql
-- Check if company colors are properly formatted
SELECT id, name, primary_color, secondary_color 
FROM res_company 
WHERE id = 1;
```

**Expected Format**: `#000000` or `black` or `rgb(0,0,0)`
**Problematic**: Empty values, invalid formats, or special characters

### Step 2: Verify CSS Template Compilation
Check if our template generates valid CSS by examining the generated stylesheet:
```
/web/content/xxxx-xxxxx/1/web.report_assets_common.css
```

### Step 3: Test Template in Isolation
Temporarily disable our CSS inheritance to confirm it's the source:
```xml
<!-- Temporarily comment out our CSS template -->
<!--
<template id="spacey_layout_styles" inherit_id="web.styles_company_report">
    ...
</template>
-->
```

## Potential Solutions

### Solution 1: Safer Color Variable Handling
Replace direct color variables with fallbacks:
```css
/* Instead of: */
color: <t t-esc='primary'/>;

/* Use: */
color: <t t-esc='primary or "#2C5282"'/>;
```

### Solution 2: Remove CSS Template Inheritance
Move styling to external CSS file instead of dynamic generation:
- Create `/static/src/scss/spacey_layout.scss`
- Remove the inheritance template
- Use static styling with CSS variables

### Solution 3: Simplify CSS Rules
Remove all dynamic color variables and use fixed colors:
```css
/* Fixed colors instead of dynamic */
color: #2C5282; /* Instead of <t t-esc='primary'/> */
color: #4A5568; /* Instead of <t t-esc='secondary'/> */
```

### Solution 4: Change Inheritance Strategy
Instead of inheriting `web.styles_company_report`, create independent CSS:
```xml
<template id="spacey_layout_styles">
    <style>
        .o_report_layout_spacey table thead tr th {
            border-top: 2px solid #4A5568 !important;
            border-bottom: 2px solid #4A5568 !important;
        }
        /* ... other rules ... */
    </style>
</template>
```

## Testing Procedure

1. **Apply fix**
2. **Restart Odoo service**
3. **Clear browser cache**
4. **Test invoice printing**
5. **Check logs for CSS warnings**
6. **Verify layout appearance**

## Production Deployment Notes

- **Backup**: Always backup before changes
- **Test environment**: Apply to test instance first
- **Rollback plan**: Keep original template ready
- **Monitor**: Watch logs during first few reports

## Contact Information

If issues persist, provide:
1. Company color settings (`res_company` table)
2. Generated CSS content (from browser developer tools)
3. Full error logs with timestamps
4. Odoo version and module list