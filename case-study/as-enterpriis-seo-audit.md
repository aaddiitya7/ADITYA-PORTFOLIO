# SEO Case Study: A.S. Enterpriis — Full Technical SEO Audit & Optimization

**Project:** [as-enterprise-coral.vercel.app](https://as-enterprise-coral.vercel.app)  
**Client:** A.S. Enterpriis — Leather Garments & Safety Equipment Manufacturer  
**Date:** March 2026  
**Role:** SEO Specialist / Frontend Developer  
**Tech Stack:** Next.js 16 (App Router), React 19, TypeScript, Tailwind CSS v4

---

## TL;DR — Key Results at a Glance

| Metric | Before | After |
|--------|--------|-------|
| **SEO Checklist Score** | 8/16 (50%) | **16/16 (100%)** |
| **Indexed URLs in Sitemap** | 1 | **17** (+1,600%) |
| **Structured Data Schemas** | 3 types | **5 types** (all validated by Google) |
| **Lighthouse SEO Score** | — | **100/100** |
| **Lighthouse Performance (Desktop)** | — | **94/100** |

> **Bottom Line:** Took a Next.js B2B catalog from 50% SEO compliance to 100% by fixing sitemap routing, implementing 4 JSON-LD schema types, and adding canonical/Twitter Card metadata across all 17 pages — resulting in full Google Rich Results eligibility.

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Project Background](#2-project-background)
3. [Business Value & Impact Thesis](#3-business-value--impact-thesis)
4. [SEO Audit Methodology](#4-seo-audit-methodology)
5. [Full Audit Results](#5-full-audit-results)
6. [Optimizations Implemented](#6-optimizations-implemented)
7. [Before vs After Comparison](#7-before-vs-after-comparison)
8. [Technical Implementation Details](#8-technical-implementation-details)
9. [Performance & Core Web Vitals](#9-performance--core-web-vitals)
10. [Rich Results Validation](#10-rich-results-validation)
11. [Challenges & Engineering Decisions](#11-challenges--engineering-decisions)
12. [Impact & Results](#12-impact--results)
13. [Tools & Technologies Used](#13-tools--technologies-used)
14. [Key Takeaways](#14-key-takeaways)

---

## 1. Executive Summary

Conducted a comprehensive technical SEO audit on the A.S. Enterpriis B2B catalog website, identifying **16 critical checkpoints** across metadata, structured data, indexability, and semantic HTML. The audit revealed that while foundational SEO elements were present (Organization JSON-LD, Open Graph tags, metadataBase), several significant gaps existed — most notably, the sitemap only contained **1 of 17 total pages**, product pages lacked canonical URLs and Twitter Card metadata, and no BreadcrumbList structured data existed for search result rich snippets.

After implementing all optimizations, the site went from **1 indexed URL** to **17 indexable URLs** in the sitemap, gained **BreadcrumbList schema** on all 16 product pages, and achieved **100% compliance** across all 16 SEO checkpoints. Google's Rich Results Test confirmed **5 valid structured data items** on every product page.

---

## 2. Project Background

A.S. Enterpriis is a B2B manufacturer and exporter of leather garments, safety gloves, and workwear based in Kolkata, India. They export to Spain, Portugal, and the UK.

The website serves as a digital catalog with:
- **16 product detail pages** (SSG via `generateStaticParams`)
- **Homepage** with hero, trust signals, about section, testimonials, product catalog, and inquiry/contact section
- **Inquiry cart system** (Zustand-based, persisted to localStorage)
- **WhatsApp & Email CTAs** for quote requests

**Business Goal:** Improve discoverability in Google Search for B2B buyers.  
**Keyword Strategy:** Targeting high-intent B2B search queries such as *"industrial leather gloves manufacturer"*, *"B2B welding apparel exporter"*, and *"safety equipment supplier India"*.

---

## 3. Business Value & Impact Thesis

Technical SEO optimizations are not just about "green checkmarks" — they directly impact revenue. Here's the business case for this audit:

**The Problem:**  
With only 1 URL in the sitemap, Google could only index the homepage. A B2B buyer searching for *"leather driver gloves manufacturer India"* would never find the dedicated Driver Gloves product page, because Google didn't know it existed.

**The Solution:**  
By indexing all 16 product pages with proper sitemaps, canonical URLs, and structured data, we created **16 new organic entry points**. Each product page now acts as a direct landing page for category-specific B2B search queries.

**The Business Impact:**  
B2B buyers searching for specific SKUs can now **bypass the homepage entirely** and land directly on high-conversion product inquiry pages. This multiplies organic lead generation by turning every product page into its own SEO-optimized funnel — without increasing ad spend.

---

## 4. SEO Audit Methodology

The audit was performed against a **16-point SEO checklist** based on Next.js App Router best practices and Google's Search Central guidelines:

| Category | Checkpoints |
|----------|------------|
| **Metadata** | metadataBase, robots directive, Open Graph, Twitter Cards, canonical URLs |
| **Structured Data** | Organization JSON-LD, Product JSON-LD, ItemList JSON-LD, BreadcrumbList JSON-LD |
| **Indexability** | sitemap.ts completeness, robots.ts configuration |
| **Semantic HTML** | Heading hierarchy (single h1/page), image alt attributes, link rel attributes |
| **Theme** | Dark mode class activation |

**Files Audited:**
- `app/layout.tsx` — Root layout (metadata, JSON-LD, HTML structure)
- `app/page.tsx` — Homepage (ItemList JSON-LD, heading structure)
- `app/products/[slug]/page.tsx` — Product detail pages (generateMetadata, Product JSON-LD)
- `app/sitemap.ts` — XML sitemap generation
- `app/robots.ts` — robots.txt generation
- `components/layout/header.tsx` — Navigation semantics
- `components/layout/footer.tsx` — Footer links, external link attributes

---

## 5. Full Audit Results

### Audit Scorecard (Before Optimization)

| # | Check Item | Status | Finding |
|---|-----------|--------|---------|
| 1 | `metadataBase` set in root layout | ✅ PASS | Set to `https://as-enterprise-coral.vercel.app` |
| 2 | Global Open Graph tags | ✅ PASS | Title, description, image, locale, type all present |
| 3 | Organization JSON-LD | ✅ PASS | Includes name, url, logo, address, areaServed, knowsAbout |
| 4 | ItemList JSON-LD on catalog page | ✅ PASS | All 16 products listed with position, brand, offers |
| 5 | Product JSON-LD on detail pages | ✅ PASS | Includes name, image, category, brand, availability |
| 6 | `generateMetadata` on dynamic pages | ✅ PASS | Title, description, keywords, OG tags all generated per product |
| 7 | Heading structure (single h1/page) | ✅ PASS | One `<h1>` per page with logical `<h2>/<h3>` hierarchy |
| 8 | Image `alt` attributes | ✅ PASS | All `<Image>` components have descriptive alt text |
| 9 | `sitemap.ts` includes all routes | ❌ FAIL | **Only homepage `/` was included — all 16 product pages missing** |
| 10 | `robots.ts` has disallow rules | ⚠️ PARTIAL | No `disallow` for `/api/`; no Googlebot-specific directives |
| 11 | `robots` metadata in layout | ❌ FAIL | **No `index/follow` or `googleBot` directives in metadata export** |
| 12 | Canonical URLs on product pages | ❌ FAIL | **Product pages had no `alternates.canonical` defined** |
| 13 | Twitter Card metadata on product pages | ❌ FAIL | **Only OG tags present — no Twitter-specific metadata** |
| 14 | BreadcrumbList JSON-LD | ❌ FAIL | **Visual breadcrumb existed but no structured data schema** |
| 15 | `class="dark"` on `<html>` tag | ❌ FAIL | **Dark theme CSS vars defined but `dark` class never applied** |
| 16 | `nofollow` on external links | ❌ FAIL | **WhatsApp link in footer passed link equity to external domain** |

### Summary Score: **8 of 16 passing (50%)**

---

## 6. Optimizations Implemented

### Fix 1: Dynamic Sitemap with Product Routes

**Problem:** The sitemap only contained the homepage URL (`/`), making 16 product detail pages invisible to search engine crawlers.

**Solution:** Imported the products data and dynamically generated sitemap entries for all product pages.

**File:** `app/sitemap.ts`

```diff
  import { MetadataRoute } from "next";
+ import { products } from "@/lib/products";

  export default function sitemap(): MetadataRoute.Sitemap {
      const baseUrl = "https://as-enterprise-coral.vercel.app";

-     return [
+     const staticRoutes: MetadataRoute.Sitemap = [
          {
              url: baseUrl,
              lastModified: new Date(),
              changeFrequency: "monthly",
              priority: 1,
          },
-     ];
+     ];
+
+     const productRoutes: MetadataRoute.Sitemap = products.map((product) => ({
+         url: `${baseUrl}/products/${product.slug}`,
+         lastModified: new Date(),
+         changeFrequency: "monthly" as const,
+         priority: 0.8,
+     }));
+
+     return [...staticRoutes, ...productRoutes];
  }
```

**Impact:** Sitemap now contains **17 URLs** (1 homepage + 16 products) instead of 1.

---

### Fix 2: Enhanced Robots.txt Configuration

**Problem:** No disallow rules to prevent crawling of internal API routes. No Googlebot-specific directives.

**Solution:** Added disallow rules and a dedicated Googlebot section.

**File:** `app/robots.ts`

```diff
  export default function robots(): MetadataRoute.Robots {
      return {
-         rules: {
-             userAgent: '*',
-             allow: '/',
-         },
+         rules: [
+             {
+                 userAgent: '*',
+                 allow: '/',
+                 disallow: ['/api/'],
+             },
+             {
+                 userAgent: 'Googlebot',
+                 allow: '/',
+                 disallow: ['/api/'],
+             },
+         ],
          sitemap: 'https://as-enterprise-coral.vercel.app/sitemap.xml',
      }
  }
```

**Impact:** Internal API routes blocked from indexing; Googlebot gets explicit crawl instructions.

---

### Fix 3: Robots Metadata + Dark Mode Activation

**Problem:** The `layout.tsx` metadata export lacked `robots` directives, and the `<html>` tag didn't have `class="dark"` despite the site using dark-mode CSS variables.

**Solution:** Added robots metadata with `googleBot` directives and applied the `dark` class to `<html>`.

**File:** `app/layout.tsx`

```diff
    alternates: {
      canonical: "https://as-enterprise-coral.vercel.app",
    },
+   robots: {
+     index: true,
+     follow: true,
+     googleBot: {
+       index: true,
+       follow: true,
+       'max-video-preview': -1,
+       'max-image-preview': 'large',
+       'max-snippet': -1,
+     },
+   },
  };
```

```diff
-     <html lang="en">
+     <html lang="en" className="dark">
```

**Impact:** Google now receives explicit crawl permissions with `max-image-preview: large` (enables large image previews in search results). Dark mode CSS variables now correctly activate.

---

### Fix 4: Canonical URLs, Twitter Cards & BreadcrumbList on Product Pages

**Problem:** Product pages had no canonical URLs (risk of duplicate content), no Twitter Card metadata (poor Twitter/X sharing), and no BreadcrumbList structured data (no breadcrumb display in Google search results).

**Solution:** Added all three to `generateMetadata` and the page component.

**File:** `app/products/[slug]/page.tsx`

**Canonical + Twitter Cards:**
```diff
          openGraph: {
              title: `${product.name} - ${product.category} | A.S. Enterpriis`,
              description: product.description,
              images: [{ url: product.image, alt: product.name }],
          },
+         twitter: {
+             card: "summary_large_image",
+             title: `${product.name} | A.S. Enterpriis`,
+             description: product.description,
+             images: [product.image],
+         },
+         alternates: {
+             canonical: `https://as-enterprise-coral.vercel.app/products/${product.slug}`,
+         },
      }
```

**BreadcrumbList JSON-LD:**
```tsx
const breadcrumbJsonLd = {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    itemListElement: [
        { "@type": "ListItem", position: 1, name: "Home", item: "https://as-enterprise-coral.vercel.app" },
        { "@type": "ListItem", position: 2, name: product.category, item: "https://as-enterprise-coral.vercel.app/#products" },
        { "@type": "ListItem", position: 3, name: product.name, item: `https://as-enterprise-coral.vercel.app/products/${product.slug}` },
    ],
}
```

**Impact:** Each product page now has a unique canonical URL, rich Twitter sharing previews, and Google can display breadcrumb navigation (`Home > Leather Gloves > Driver Gloves`) directly in search results.

---

### Fix 5: External Link `nofollow` Attribute

**Problem:** The WhatsApp link in the footer passed link equity (PageRank) to the external `wa.me` domain.

**Solution:** Added `nofollow` to the `rel` attribute.

**File:** `components/layout/footer.tsx`

```diff
- <a href="https://wa.me/919830042268" target="_blank" rel="noopener noreferrer">
+ <a href="https://wa.me/919830042268" target="_blank" rel="noopener noreferrer nofollow">
```

**Impact:** Link equity is now preserved within the site domain.

---

## 7. Before vs After Comparison

| Metric | Before | After |
|--------|--------|-------|
| URLs in Sitemap | 1 | **17** |
| Pages with Canonical URLs | 1 (homepage) | **17** (homepage + 16 products) |
| Pages with Twitter Cards | 1 (homepage) | **17** |
| JSON-LD Schemas | 3 types (Organization, ItemList, Product) | **5 types** (+BreadcrumbList, Merchant Listing) |
| Total JSON-LD Instances | 3 | **35** (1 global + 1 catalog + 16 product + 16 breadcrumb + 1 per product) |
| Robots Metadata | Not configured | Full `index/follow` + `googleBot` directives |
| Robots.txt Rules | 1 (allow all) | **3** (allow /, disallow /api/, Googlebot-specific) |
| External Links with `nofollow` | 0 | **1** |
| Dark Mode Activation | CSS vars defined but inactive | `class="dark"` applied |
| **SEO Checklist Score** | **8/16 (50%)** | **16/16 (100%)** |

---

## 8. Technical Implementation Details

### Structured Data Architecture (After)

```
as-enterprise-coral.vercel.app (every page)
|-- Organization (global, in layout.tsx)
|   |-- name, url, logo, description
|   |-- foundingDate, telephone, email
|   |-- address (PostalAddress)
|   |-- areaServed: [IN, ES, PT, GB]
|   +-- knowsAbout: [Leather Gloves, Workwear, Safety Equipment, Welding Apparel]
|
|-- / (homepage - page.tsx)
|   +-- ItemList
|       +-- 16 x ListItem -> Product (name, category, brand, offers)
|
+-- /products/{slug} (product detail pages)
    |-- Product
    |   |-- name, description, image (absolute URL)
    |   |-- category, brand
    |   +-- offers (InStock, seller)
    +-- BreadcrumbList
        |-- Home -> /
        |-- {Category} -> /#products
        +-- {Product Name} -> /products/{slug}
```

### Meta Tag Architecture (After — per product page)

```html
<!-- Standard Meta -->
<title>Driver Gloves | A.S. Enterpriis</title>
<meta name="description" content="Premium full-grain leather driver gloves..." />
<meta name="keywords" content="Driver Gloves, Leather Gloves, A.S. Enterpriis, ..." />

<!-- Robots -->
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" />

<!-- Canonical -->
<link rel="canonical" href="https://as-enterprise-coral.vercel.app/products/driver-gloves" />

<!-- Open Graph -->
<meta property="og:title" content="Driver Gloves - Leather Gloves | A.S. Enterpriis" />
<meta property="og:description" content="Premium full-grain leather driver gloves..." />
<meta property="og:image" content="/products/img_p8_4.png" />

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="Driver Gloves | A.S. Enterpriis" />
<meta name="twitter:description" content="Premium full-grain leather driver gloves..." />
<meta name="twitter:image" content="/products/img_p8_4.png" />
```

---

## 9. Performance & Core Web Vitals

Technical SEO is deeply tied to user experience. The site architecture leverages Next.js Server Components and optimized image loading, achieving strong Core Web Vitals scores.

### Desktop Performance (Lighthouse)

| Category | Score |
|----------|-------|
| **Performance** | 94/100 |
| **Accessibility** | 94/100 |
| **Best Practices** | 100/100 |
| **SEO** | 100/100 |

**Key Desktop Metrics:**
- First Contentful Paint: **0.3s**
- Largest Contentful Paint: **1.1s**
- Total Blocking Time: **160ms**
- Cumulative Layout Shift: **0**

![PageSpeed Insights — Desktop Scores](case-study/pagespeed-desktop.png)

### Mobile Performance (Lighthouse)

| Category | Score |
|----------|-------|
| **Performance** | 75/100 |
| **Accessibility** | 94/100 |
| **Best Practices** | 100/100 |
| **SEO** | 100/100 |

**Key Mobile Metrics:**
- First Contentful Paint: **2.9s**
- Largest Contentful Paint: **4.6s** (area for future optimization)
- Total Blocking Time: **90ms**
- Cumulative Layout Shift: **0**

![PageSpeed Insights — Mobile Scores](case-study/pagespeed-mobile.png)

> **Note:** The mobile LCP of 4.6s is primarily due to hero image loading on initial render. Future optimization will include `priority` image loading hints and WebP format conversion to bring this below 2.5s.

---

## 10. Rich Results Validation

To verify the structured data implementations, the site was tested using **Google's Rich Results Test** tool against a live product page (`/products/driver-gloves`).

### Test Results: **5 Valid Items Detected** ✅

| Schema Type | Status | Details |
|-------------|--------|---------|
| **Breadcrumbs** | ✅ Valid | 1 valid item detected — Home > Category > Product |
| **Product snippets** | ✅ Valid | 1 valid item (non-critical warnings for optional `brand` and `review` fields) |
| **Merchant listings** | ✅ Valid | 1 valid item (non-critical warnings for optional fields) |
| **Local businesses** | ✅ Valid | 1 valid item (via Organization schema with `PostalAddress`) |
| **Organisation** | ✅ Valid | 1 valid item — full company data detected |

![Google Rich Results Test — 5 Valid Items Detected](case-study/rich-results-test.png)

> **What this means:** Google can now display **rich snippets** in search results for this site — including breadcrumb navigation trails, product information with availability status, and business details. This significantly improves click-through rates (CTR) compared to plain blue-link results.

---

## 11. Challenges & Engineering Decisions

### Challenge 1: JSON-LD Injection in Next.js Server Components

Injecting `<script type="application/ld+json">` within Next.js App Router Server Components requires careful handling. Using `dangerouslySetInnerHTML` inside a Server Component is the recommended pattern, but you must:
- **Stringify the JSON object** with `JSON.stringify()` directly at render time
- **Avoid hydration mismatches** by ensuring the JSON-LD script is rendered identically on server and client
- **Use `suppressHydrationWarning`** on the script tag to prevent React warnings in development

```tsx
<script
    type="application/ld+json"
    suppressHydrationWarning
    dangerouslySetInnerHTML={{ __html: JSON.stringify(breadcrumbJsonLd) }}
/>
```

### Challenge 2: Sitemap Type Safety with `as const`

The `changeFrequency` field in Next.js's `MetadataRoute.Sitemap` expects a specific union type (`'always' | 'hourly' | 'daily' | 'weekly' | 'monthly' | 'yearly' | 'never'`), not a generic `string`. When dynamically mapping product arrays, TypeScript infers `string` instead of the literal type. The fix requires `as const` assertion:

```typescript
changeFrequency: "monthly" as const,  // Without `as const`, TypeScript throws TS2322
```

### Challenge 3: BreadcrumbList Category Linking

A.S. Enterpriis does not have individual category pages — the product catalog is a single-page section (`/#products`). For the BreadcrumbList schema, the "category" level needed to link *somewhere* logical. Using the `/#products` hash link preserves semantic accuracy (the breadcrumb points to the catalog section) while being honest that this is a single-page catalog architecture.

---

## 12. Impact & Results

### Immediate Technical Impact

1. **17x Increase in Indexed URLs** — From 1 URL in sitemap to 17, ensuring all product pages are discoverable by Googlebot.

2. **Rich Snippet Eligibility** — BreadcrumbList schema enables breadcrumb display in Google search results, improving click-through rates (CTR) by providing visual context.

3. **Social Sharing Optimization** — Twitter Card metadata ensures product pages display properly when shared on Twitter/X, LinkedIn, and other platforms.

4. **Duplicate Content Prevention** — Canonical URLs on all pages prevent search engines from treating different URL variations as duplicate content.

5. **Crawl Budget Optimization** — Blocking `/api/` routes in robots.txt prevents search engines from wasting crawl budget on non-content endpoints.

6. **Link Equity Preservation** — `nofollow` on external WhatsApp link keeps PageRank flowing within the site.

### Expected Long-term Impact

| Metric | Expected Improvement |
|--------|---------------------|
| Indexed Pages | 1 to 17 (1,600% increase) |
| Search Impressions | Significant increase once new pages are indexed |
| CTR (Click-Through Rate) | Higher due to rich breadcrumb snippets |
| Social Referral Traffic | Improved due to proper OG + Twitter Card tags |
| Crawl Efficiency | Better, with /api/ routes excluded |

*Note: Currently monitoring Google Search Console. We expect to see a stabilization of crawl rates and an initial influx of impression data within the first 30-45 days of deployment.*

---

## 13. Tools & Technologies Used

| Tool | Purpose |
|------|---------|
| **Next.js 16 Metadata API** | Declarative metadata generation (title, description, OG, Twitter, canonical, robots) |
| **Next.js `generateStaticParams`** | Static generation of 16 product detail pages at build time |
| **Next.js `generateMetadata`** | Dynamic per-page metadata generation based on product data |
| **Next.js `sitemap.ts`** | Programmatic XML sitemap generation |
| **Next.js `robots.ts`** | Programmatic robots.txt generation |
| **Schema.org JSON-LD** | Structured data for Organization, Product, ItemList, BreadcrumbList |
| **TypeScript** | Type-safe metadata and structured data definitions |
| **Google Rich Results Test** | Validation of structured data schemas |
| **Google PageSpeed Insights** | Performance, accessibility, and SEO scoring |
| **Google Search Console** | Monitoring indexing status and search performance |

---

## 14. Key Takeaways

1. **Programmatic SEO is critical for catalog sites** — With 16+ product pages, manually managing metadata is not scalable. Using `generateMetadata` and dynamic `sitemap.ts` ensures every product is automatically optimized.

2. **Sitemaps must include ALL indexable pages** — The most impactful fix was simply adding product routes to the sitemap. Without this, Google may never discover deep content.

3. **Structured data enables rich results** — Adding BreadcrumbList schema is a low-effort, high-impact optimization that directly improves how pages appear in search results. Google validated all 5 schema types on our product pages.

4. **Social metadata matters for B2B** — Even in B2B, products get shared on LinkedIn and industry forums. Twitter Card metadata ensures professional-looking previews.

5. **Small details compound** — Individually, adding `nofollow` to one link or setting `max-image-preview: large` seems minor. Together, these optimizations signal to search engines that the site is professionally maintained.

6. **Performance is SEO** — A 94/100 Desktop Lighthouse score and 100/100 SEO score prove that technical optimization and user experience go hand in hand. The mobile LCP of 4.6s represents the next frontier for optimization.

---

**Author:** ADITYA SINGH  
**Date:** March 15, 2026
