# Design System: Aditya Singh | AI-Driven Marketer Portfolio
**Project ID:** local-portfolio-v1

## 1. Visual Theme & Atmosphere
The portfolio employs a "High-Contrast Brutalist" yet highly professional aesthetic. It relies on stark contrast, utilizing vast expanses of pure white space against deep, light-absorbing blacks and precise neutral greys. This creates a minimalist, clinical, and data-driven environment perfectly suited for an "AI-Driven Marketer." The atmosphere is confident and highly legible, with a sharp underlying tension provided by striking, action-oriented red accents.

## 2. Color Palette & Roles
*   **Void Black (#000000):** Used as the primary background for the heavy left-hand navigation sidebar and active state hover backgrounds. It grounds the design.
*   **Deep Charcoal (#0a0a0a / neutral-950):** Used for the contact information block within the sidebar to provide subtle visual separation from the main navigation area without breaking the dark theme.
*   **Crisp White (#ffffff):** Used as the primary background for the main content area and individual content cards. It ensures maximum readability and a clean, modern feel.
*   **Slate Grey (#737373 / neutral-500):** Used for secondary text, metadata, and subtle borders. It provides necessary information hierarchy without distracting from primary content.
*   **Off-White Frost (#f5f5f5 / neutral-100):** Used for subtle card backgrounds (like the bio block) or hover states to provide gentle elevation and interactivity.
*   **High-Velocity Red (#dc2626 / red-600):** The sole accent color. Used strictly for primary calls to action, interactive hover states, active navigation indicators, and key data points in charts. It signifies action, speed, and conversion.

## 3. Typography Rules
*   **Primary Font:** Inter (or system sans-serif fallback). The typography leans heavily on geometric, clean sans-serif fonts to maintain the modern, tech-forward aesthetic.
*   **Headers (h1, h2, h3):** Heavily weighted (font-bold) with tight tracking (tracking-tight to tracking-wider depending on context). Headers are deeply contrasted against the background (using pure black/white depending on the section).
*   **Body Text (p):** Highly legible, medium-weight text (text-slate-600 or neutral equivalents), ensuring long-form readability for case studies and summaries.
*   **Microcopy:** Small, uppercase, widely tracked text (text-xs uppercase tracking-widest) used for category labels and secondary status indicators.

## 4. Component Stylings
*   **Navigation Buttons:** Rectangular with completely sharp or very subtly rounded corners. They rely on stark color inversion on hover (transitioning to pure black or deep grey backgrounds) rather than shadows or depth. Active states are indicated by a sharp red (#dc2626) background.
*   **Project & Skill Cards:** Clean, white containers (bg-white) with sharp or subtly rounded corners (rounded-xl/rounded-lg). They utilize whisper-soft, highly diffused drop shadows (shadow-sm to shadow-md) just to lift them off the background canvas, maintaining the flat, minimalist look but preventing them from blending in.
*   **Interactive Links/Tags:** Pill-shaped (rounded-full) or softly rounded rectangles (rounded-md) often featuring a very subtle background tint (e.g., a 10% opacity red) that deepens on hover, ending with a sharp arrow indicator (↗) to signify external movement.

## 5. Layout Principles
*   **Structure:** A robust, fixed left-axis sidebar navigation pattern paired with a fluid, wide-canvas main content area. This classic SaaS dashboard layout reinforces the "software/tooling" feel rather than a traditional creative portfolio.
*   **Whitespace:** Generous and intentional. Standardized padding and margins (p-6, p-8, gap-8) are used to create distinct breathing room between sections, preventing cognitive overload and ensuring the content (rather than the design itself) remains the focal point.
