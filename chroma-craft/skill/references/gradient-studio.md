# Chroma-Craft Gradient Studio

> **Mathematically Harmonized CSS Gradient Formulas.**  
> Ready-to-copy CSS linear, radial, and mesh gradients engineered using the Chroma-Craft 46-color palette library.

---

## 1. Linear Background Gradients by Website Topic

Background linear gradients should provide subtle atmospheric depth without reducing readability or creating visual noise.

### A. Corporate & Enterprise Backgrounds (Subtle, Clean Washes)

```css
/* 1. Corporate Executive Wash - Gentle descent from cool white into pearl */
.bg-corporate-wash {
  background: linear-gradient(180deg, #FBFBFD 0%, #F8F6F0 100%);
}

/* 2. Enterprise Cloud Tint - Gentle descent into soft Arctic Blue */
.bg-enterprise-tint {
  background: linear-gradient(180deg, #FBFBFD 0%, #C6E2FF 100%);
}

/* 3. Deep Corporate Header / Security Anchor */
.bg-corporate-dark-anchor {
  background: linear-gradient(135deg, #121214 0%, #191970 100%);
}
```

### B. E-Commerce Storefront Backgrounds (Product-Prominent, Neutral Washes)

```css
/* 1. Neutral Retail Canvas - Pure neutral backdrop keeping product photos true */
.bg-ecom-neutral {
  background: linear-gradient(180deg, #FBFBFD 0%, #F8F6F0 100%);
}

/* 2. Soft Peach Cosmetic / Lifestyle Glow */
.bg-ecom-lifestyle {
  background: linear-gradient(180deg, #FBFBFD 0%, #FEE2E2 100%);
}

/* 3. Tech Gadget Ice Wash */
.bg-ecom-tech {
  background: linear-gradient(180deg, #FBFBFD 0%, #DDF2FD 100%);
}
```

### C. Hackathon & Developer Showcases (High-Voltage Dark Gradients)

```css
/* 1. Cyber Nebula Hero - Deep charcoal through midnight navy to vivid electric blue */
.bg-hackathon-nebula {
  background: linear-gradient(135deg, #121214 0%, #191970 50%, #0066FF 100%);
}

/* 2. Quantum Violet Pulse - Obsidian purple into vibrant royal purple and cyan */
.bg-hackathon-quantum {
  background: linear-gradient(135deg, #36013F 0%, #7851A9 50%, #00E5FF 100%);
}

/* 3. Terminal Matrix Void */
.bg-hackathon-terminal {
  background: linear-gradient(135deg, #121214 0%, #008080 70%, #00FF00 100%);
}
```

### D. Luxury, Editorial & Hospitality (Tactile Organic Gradients)

```css
/* 1. Champagne Silk - Warm ivory to soft beige and pearl */
.bg-luxury-champagne {
  background: linear-gradient(135deg, #FFFFF0 0%, #E8DCC4 50%, #F8F6F0 100%);
}

/* 2. Velvet Noir - Deep espresso brown into roast coffee */
.bg-luxury-noir {
  background: linear-gradient(135deg, #3D1C02 0%, #4A2C2A 100%);
}
```

---

## 2. Hero & Mesh Gradients

Hero banners create the visual signature of the website. These formulas use multi-stop angles and radial glow points.

### 1. Midnight Blue to Electric Blue (The Authoritative SaaS Hero)
```css
.hero-midnight-electric {
  background: linear-gradient(135deg, #191970 0%, #0066FF 100%);
  color: #FBFBFD;
}
```

### 2. Plum Purple to Rose Red (The Creative / Lifestyle Header)
```css
.hero-plum-rose {
  background: linear-gradient(135deg, #5A1846 0%, #C21E56 100%);
  color: #FBFBFD;
}
```

### 3. Deep Purple to Royal Purple (The Modern AI / Web3 Hero)
```css
.hero-deep-royal-purple {
  background: linear-gradient(135deg, #36013F 0%, #7851A9 100%);
  color: #FBFBFD;
}
```

### 4. Ambient Cyber Mesh (Multi-Radial Background)
```css
.hero-cyber-mesh {
  background-color: #121214;
  background-image: 
    radial-gradient(circle at 15% 25%, rgba(0, 102, 255, 0.45) 0%, transparent 45%),
    radial-gradient(circle at 85% 75%, rgba(120, 81, 169, 0.40) 0%, transparent 50%),
    radial-gradient(circle at 50% 50%, rgba(0, 229, 255, 0.15) 0%, transparent 60%);
  background-attachment: fixed;
}
```

---

## 3. High-Conversion CTA & Button Gradients

Buttons require punchy contrast, crisp 2-stop transitions, and distinct hover states.

### 1. Electric Blue to Cyan (SaaS & Hackathon Primary)
```css
.btn-electric-cyan {
  background: linear-gradient(135deg, #0066FF 0%, #00E5FF 100%);
  color: #121214; /* Deep Charcoal Onyx for maximum text sharpness */
  font-weight: 600;
  border: none;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.btn-electric-cyan:hover {
  transform: translateY(-1px);
  box-shadow: 0 8px 24px rgba(0, 229, 255, 0.35);
}
```

### 2. Hot Pink to Magenta (High-Energy Consumer / Social Trigger)
```css
.btn-pink-magenta {
  background: linear-gradient(135deg, #FF69B4 0%, #FF00FF 100%);
  color: #FBFBFD;
  font-weight: 600;
  border: none;
  box-shadow: 0 4px 16px rgba(255, 0, 255, 0.25);
}
```

### 3. Gold to Caramel Brown (Luxury Tier / VIP Upgrade)
```css
.btn-gold-caramel {
  background: linear-gradient(135deg, #D4AF37 0%, #AF6E4D 100%);
  color: #3D1C02; /* Chocolate Brown text */
  font-weight: 700;
  border: 1px solid rgba(212, 175, 55, 0.5);
}
```

### 4. Amber Gold to Terracotta (E-Commerce "Add to Cart")
```css
.btn-amber-checkout {
  background: linear-gradient(135deg, #F59E0B 0%, #E07A5F 100%);
  color: #121214;
  font-weight: 700;
  border: none;
  box-shadow: 0 4px 14px rgba(245, 158, 11, 0.35);
}
```

---

## 4. Subtle Surface Overlays & Glassmorphism

Glassmorphism elevates cards, floating navigation bars, and modals above backgrounds while preserving spatial context.

### 1. Snow White Glassmorphic Tint (Light Mode Floating Navbar)
```css
.glass-surface-light {
  background: linear-gradient(135deg, rgba(251, 251, 253, 0.85) 0%, rgba(248, 246, 240, 0.65) 100%);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(192, 192, 200, 0.4);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.04);
}
```

### 2. Charcoal Onyx Dark Glass (Dark Mode Card / Modal)
```css
.glass-surface-dark {
  background: linear-gradient(135deg, rgba(18, 18, 20, 0.80) 0%, rgba(25, 25, 112, 0.25) 100%);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid rgba(255, 255, 255, 0.08);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.35);
}
```

### 3. Ivory Soft Ambient Wash (Editorial Testimonial Backplate)
```css
.surface-ivory-ambient {
  background: linear-gradient(180deg, rgba(255, 255, 240, 0.90) 0%, rgba(232, 220, 196, 0.35) 100%);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(232, 220, 196, 0.6);
}
```

---

## 5. Performance & CSS Rendering Best Practices

1. **Prevent Color Banding:** When rendering subtle gradients across large 4K displays, browsers can exhibit color stepping. Counteract this by adding a microscopic grain or using high-bitrate RGB stops.
2. **Hardware Acceleration:** Apply `transform: translateZ(0)` or `will-change: transform` to interactive gradient buttons to avoid repainting during hover animations.
3. **Always specify a solid fallback background:**
   ```css
   .hero {
     background-color: #121214; /* Fallback for legacy clients */
     background-image: linear-gradient(135deg, #121214 0%, #191970 50%, #0066FF 100%);
   }
   ```
