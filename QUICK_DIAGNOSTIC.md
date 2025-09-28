# Quick CSS Error Diagnostic Checklist

## Step 1: Verify Error Source
```bash
# Check if error disappears when module is uninstalled
# If YES → Our module is the cause
# If NO → Different issue
```

## Step 2: Check Company Color Values
```sql
SELECT primary_color, secondary_color FROM res_company WHERE id = 1;
```

**Look for:**
- ❌ NULL or empty values
- ❌ Invalid formats (missing #, wrong length)
- ❌ Special characters or spaces
- ✅ Valid hex codes like `#2C5282`

## Step 3: Most Likely Quick Fixes

### Fix A: Add Color Fallbacks (Safest)
In `views/report_templates.xml`, replace:
```xml
<t t-esc='primary'/>
```
With:
```xml
<t t-esc='primary or "#2C5282"'/>
```

### Fix B: Use Static Colors (Fastest)
Replace all dynamic colors with fixed ones:
- `<t t-esc='primary'/>` → `#2C5282`
- `<t t-esc='secondary'/>` → `#4A5568`

### Fix C: Disable CSS Template (Emergency)
Comment out the CSS inheritance:
```xml
<!--
<template id="spacey_layout_styles" inherit_id="web.styles_company_report">
    ...
</template>
-->
```

## Step 4: Test Results
1. Apply fix
2. Restart Odoo
3. Print invoice
4. Check for CSS warnings in logs

## Expected Outcome
✅ No CSS compilation warnings
✅ Invoice prints successfully
✅ Layout styling maintained