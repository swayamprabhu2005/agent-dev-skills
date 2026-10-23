# Chroma-Craft Section-by-Section Color Assignment Guide

> **Structural Blueprint for Frontend UI Layouts.**  
> Specifies exact color token roles, contrast targets, border opacities, and gradient implementations across every standard website section in both Light Mode and Dark Mode.

---

## 1. Overview of Website Visual Distribution

A polished website maintains rhythm and hierarchy from top to bottom. It alternates between calm reading canvases and energetic focal zones, avoiding uniform monotony without introducing chaotic noise.

```text
┌─────────────────────────────────────────────────────────────┐
│ 1. NAVBAR / HEADER                                          │  ◄── Glassmorphic wash / Clean Anchor
├─────────────────────────────────────────────────────────────┤
│ 2. HERO SECTION                                             │  ◄── Atmospheric gradient or clean wash
│    [ H1 Headline ]                                          │  ◄── High contrast (18:1)
│    [ Primary CTA ]  [ Secondary Ghost ]                     │  ◄── High-impact action / 1px border
├─────────────────────────────────────────────────────────────┤
│ 3. SOCIAL PROOF / LOGO STRIP                                │  ◄── Muted monochrome logos (Grey / Silver)
├─────────────────────────────────────────────────────────────┤
│ 4. FEATURE GRID / CARDS                                     │  ◄── Alternating surface (#F8F6F0 / Cards #FBFBFD)
│    ┌──────────┐  ┌──────────┐  ┌──────────┐                 │
│    │ Card 1   │  │ Card 2   │  │ Card 3   │                 │  ◄── 1px Silver border, 15% brand icon tint
│    └──────────┘  └──────────┘  └──────────┘                 │
├─────────────────────────────────────────────────────────────┤
│ 5. PRICING / PRODUCT SHOWCASE                               │  ◄── Pure white card canvas, high-vis badge
│    ┌──────────┐  ┌──────────┐ (Featured)                    │
│    │ Tier 1   │  │ Tier 2   │                               │  ◄── Highlight border (Brand Primary / Accent)
│    └──────────┘  └──────────┘                               │
├─────────────────────────────────────────────────────────────┤
│ 6. TESTIMONIALS & TRUST                                     │  ◄── Subtle surface shift or anchored dark block
├─────────────────────────────────────────────────────────────┤
│ 7. FINAL CONVERSION BANNER (CTA)                            │  ◄── High-urgency brand gradient
├─────────────────────────────────────────────────────────────┤
│ 8. FOOTER                                                   │  ◄── Grounded dark or quiet pearl base
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Section Specifications

### Section 1: Sticky Navigation Bar & Header

The navigation bar is the permanent orientation layer. It should be legible over any scrolling background without visually weighing down the viewport.

| Token / Element | Light Mode Recommendation | Dark Mode Recommendation | Contrast Target |
| :--- | :--- | :--- | :---: |
| **Surface** | `rgba(251, 251, 253, 0.85)` + `backdrop-filter: blur(12px)` | `rgba(18, 18, 20, 0.85)` + `backdrop-filter: blur(12px)` | — |
| **Border Bottom** | `1px solid rgba(192, 192, 200, 0.4)` (`Silver`) | `1px solid rgba(255, 255, 255, 0.1)` | — |
| **Logo / Brand Name** | `#121214` (`Charcoal Onyx`) | `#FBFBFD` (`Snow White`) | **18.1:1** (AAA) |
| **Nav Links (Default)** | `#6B7280` (`Grey`) | `#C0C0C8` (`Silver`) | **5.2:1 / 7.5:1** (AA) |
| **Nav Links (Hover)** | Brand Primary (`#0077BE`, `#4682B4`, `#E07A5F`) | `#00E5FF` (`Cyan`) or `#0066FF` (`Electric Blue`) | — |
| **Active Tab Pill** | `rgba(0, 119, 190, 0.1)` with Brand Primary text | `rgba(0, 102, 255, 0.15)` with `#C6E2FF` text | — |
| **Header CTA Button** | Brand Primary solid (`#0077BE`) or Accent Highlight | Electric Blue (`#0066FF`) or Accent Highlight | **4.5:1+** (AA) |

---

### Section 2: Hero Section (First Fold)

The hero section sets the emotional tone and captures immediate engagement.

#### Light Mode Hero Architecture:
- **Background:** Soft vertical wash:
  - *Tech / Corporate:* `linear-gradient(180deg, #FBFBFD 0%, #F8F6F0 100%)`
  - *Fintech / SaaS:* `linear-gradient(180deg, #FBFBFD 0%, #DDF2FD 100%)`
  - *Editorial / Studio:* `linear-gradient(180deg, #FFFFF0 0%, #E8DCC4 100%)`
- **Headline (H1):** `#121214` (`Charcoal Onyx`) for maximum crispness and zero optical fringe.
- **Subheadline:** `#6B7280` (`Grey`) for distinct reading hierarchy (5.2:1 contrast).
- **Primary CTA:** High-conversion button:
  - Corporate: `linear-gradient(135deg, #0077BE 0%, #4682B4 100%)` with `#FBFBFD` text.
  - E-Commerce: `linear-gradient(135deg, #F59E0B 0%, #AF6E4D 100%)` with `#121214` text.
  - Creative / Studio: `#E07A5F` (`Terracotta`) with `#FBFBFD` text.
- **Secondary CTA (Ghost Button):** Transparent background with `1px solid #C0C0C8` (`Silver`) and `#121214` text.
- **Social Proof Pill:** `#DDF2FD` (`Ice Blue`) pill with `#0077BE` text and `1px solid #C6E2FF`.

#### Dark Mode Hero Architecture:
- **Background:** High-impact dark gradient:
  - *Hackathon / AI:* `linear-gradient(135deg, #121214 0%, #191970 50%, #0066FF 100%)`
  - *Web3 / Creative:* `linear-gradient(135deg, #36013F 0%, #7851A9 50%, #00E5FF 100%)`
- **Headline (H1):** `#FBFBFD` (`Snow White`) (18.1:1 contrast).
- **Subheadline:** `#C0C0C8` (`Silver`) (7.5:1 contrast).
- **Primary CTA:** `linear-gradient(135deg, #0066FF 0%, #00E5FF 100%)` with `#121214` bold text.
- **Secondary CTA:** Transparent background with `1px solid rgba(255, 255, 255, 0.2)` and `#FBFBFD` text.

---

### Section 3: Feature Grid & Service Cards

Provides structural readability for capabilities and feature highlights.

- **Container Background:**
  - *Light Mode:* Shift to `#F8F6F0` (`Pearl White`) to create subtle visual separation from the pure white hero canvas.
  - *Dark Mode:* Ground in `#121214` (`Charcoal Onyx`).
- **Individual Card Surface:**
  - *Light Mode:* `#FBFBFD` (`Snow White`) with `1px solid #C0C0C8` (`Silver`) and soft shadow (`box-shadow: 0 4px 20px rgba(0,0,0,0.04)`).
  - *Dark Mode:* `rgba(255, 255, 255, 0.03)` with `1px solid rgba(255, 255, 255, 0.08)`.
- **Card Icon Box:**
  - *Light Mode:* Soft 12% opacity tint of brand color (e.g. `rgba(0, 119, 190, 0.12)`) with icon in solid Brand Primary (`#0077BE`).
  - *Dark Mode:* `rgba(0, 102, 255, 0.15)` with icon in `#00E5FF` (`Cyan`) or `#0066FF` (`Electric Blue`).
- **Card Title (H3):** `#121214` (Light) or `#FBFBFD` (Dark).
- **Card Body:** `#6B7280` (`Grey`, Light) or `#C0C0C8` (`Silver`, Dark).

---

### Section 4: Pricing Tables & Product Catalog Showcase

The pricing section demands unmistakable visual hierarchy between standard tiers and the "Featured / Recommended" option.

- **Standard Plan Card:**
  - Surface: `#FBFBFD` (`Snow White`, Light) / `rgba(255, 255, 255, 0.03)` (Dark).
  - Border: `1px solid #C0C0C8` (`Silver`).
  - CTA Button: Secondary / Outline button.
- **Featured / "Most Popular" Plan Card:**
  - Surface: Elevated with `2px solid` Brand Primary border (or subtle gradient ring).
  - Badge ("Most Popular" / "Best Value"):
    - E-commerce / SaaS: `#F59E0B` (`Amber Gold`) badge with `#121214` text.
    - Tech / AI: `#7851A9` (`Royal Purple`) or `#0066FF` (`Electric Blue`) with `#FBFBFD` text.
  - CTA Button: Dominant High-Impact Primary CTA.
- **Price Number:** Always rendered in highest contrast (`#121214` in Light Mode, `#FBFBFD` in Dark Mode).
- **Checkmarks / Feature Bullets:**
  - Included: `#228B22` (`Forest Green`) or `#32CD32` (`Lime Green`).
  - Excluded / Not available: `#C0C0C8` (`Silver`) or `#6B7280` (`Grey`) with line-through text.

---

### Section 5: Testimonials & Social Proof

Builds human credibility and trust.

- **Surface Treatment:**
  - *Option A (Light Subtle):* `#FFFFF0` (`Ivory White`) or `#F8F6F0` (`Pearl White`) container.
  - *Option B (Anchored Dark Breakout):* Full-width `#191970` (`Midnight Blue`) or `#121214` (`Charcoal Onyx`) container with white cards.
- **Quotation Mark / Trust Accent:** Use warm editorial accents like **Terracotta (`#E07A5F`)** or **Gold (`#D4AF37`)**.
- **Star Rating Icons:** Strictly **Amber Gold (`#F59E0B`)** or **Gold (`#D4AF37`)**.
- **Customer Name & Role:** Name in `#121214`, Title/Company in `#6B7280`.

---

### Section 6: High-Conversion CTA Banner (Final Call)

The last chance to convert before the footer.

- **Container Background:**
  - *Corporate / SaaS:* Full-bleed `linear-gradient(135deg, #191970 0%, #0077BE 100%)`.
  - *Hackathon / Tech:* Full-bleed `linear-gradient(135deg, #121214 0%, #0066FF 100%)`.
  - *Luxury:* Full-bleed `linear-gradient(135deg, #3D1C02 0%, #4A2C2A 100%)`.
- **Text:** Crisp `#FBFBFD` (`Snow White`) title and `#DDF2FD` (`Ice Blue`) subtitle.
- **Conversion Button:** High-contrast standout:
  - If background is deep blue: `#F59E0B` (`Amber Gold`) button with `#121214` text, OR solid `#FBFBFD` white button with `#191970` Midnight Blue text.

---

### Section 7: Footer & Informational Base

Grounds the layout, terminates the visual flow, and houses compliance and directory links.

- **Surface:**
  - *Minimal Light Footer:* `#F8F6F0` (`Pearl White`) with `1px solid #C0C0C8` top border.
  - *Anchored Dark Footer:* `#121214` (`Charcoal Onyx`) with `1px solid rgba(255,255,255,0.08)` top border.
- **Column Titles:** High contrast bold typography.
- **Navigation Links:** `#6B7280` (`Grey`) transitioning smoothly to Brand Primary on hover.
- **Copyright & Disclaimers:** Subdued `#6B7280` (Light) or `#C0C0C8` (Dark) at 75% opacity.
