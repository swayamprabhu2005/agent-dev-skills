# UI/UX Specification: Freelance Invoice Manager

## 1. Visual Direction & Design Tokens
* **Aesthetic:** Minimalist, editorial typography with high contrast data tables.
* **Palette:**
  * Neutral Dark: `#0F172A` (Slate 900)
  * Surface Neutral: `#F8FAFC` (Slate 50)
  * Primary Accent: `#2563EB` (Blue 600)
  * Success / Paid: `#16A34A` (Green 600)
  * Warning / Overdue: `#DC2626` (Red 600)
* **Typography:** `Inter` for UI controls, `JetBrains Mono` for currency amounts and invoice numbers.

## 2. Core Layouts & Component States

### Invoice Builder Screen (REQ-004)
* **Header Bar:** Invoice Number (e.g. `INV-2026-001`), Status Badge (`DRAFT`), Save Draft Button, Publish Button.
* **Client Selector:** Autocomplete dropdown for selecting or creating a Client.
* **Line Items Table:**
  * Dynamic rows: Description input, Quantity (numeric stepper), Unit Price, Computed Subtotal.
  * "+ Add Line Item" button.
* **Summary Panel:** Subtotal, Tax Rate (%) input, Calculated Tax, Total Due.

### State Matrix
| State | Behavior / Appearance |
| :--- | :--- |
| **Default** | Clean inputs with subtle border `#CBD5E1`. |
| **Loading** | Skeleton loaders for invoice line items; disabled primary actions. |
| **Empty** | "No invoices found. Create your first invoice to get paid." with primary CTA button. |
| **Error** | Red border `#EF4444` with inline validation hint text below offending input. |
| **Paid** | Green badge `#16A34A`, lock icon, all inputs disabled. |
