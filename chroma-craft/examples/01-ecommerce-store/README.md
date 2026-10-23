# Example 01: E-Commerce Storefront Palette

> **Domain Archetype:** E-Commerce & High-Conversion Retail  
> **Key Objective:** Frictionless merchandise discovery, maximum product photo fidelity, unambiguous "Add to Cart" conversion.

---

## Aesthetic Rationale (The "Anti-Jigmig" Rule)

In an online store, the products are the hero. This theme enforces:
1. **Pristine Snow White Canvas (`#FBFBFD`):** Ensures white shoe soles, colored apparel, and photography backgrounds match the site without optical clashes.
2. **Distraction-Free Card Frames:** Card containers use `Ivory White` (`#FFFFF0`) with subtle `Silver` (`#C0C0C8`) 1px borders. Zero shiny holograms or animated gradients behind items.
3. **High-Conversion CTA:** Primary purchase actions ("Add to Cart", "Instant Checkout") use **Amber Gold (`#F59E0B`)** or the 2-stop amber gradient `linear-gradient(135deg, #F59E0B 0%, #AF6E4D 100%)` with dark **Charcoal Onyx (`#121214`)** bold text.
4. **Contrast Verification:**
   - Text on Canvas: `#121214` on `#FBFBFD` = **18.10:1** (WCAG AAA)
   - CTA Button Text: `#121214` on `#F59E0B` = **8.71:1** (WCAG AAA)

---

## File Contents
- `tokens.css`: Ready-to-import CSS custom properties with light/dark tokens.
- `palette.json`: Machine-readable token specification.
