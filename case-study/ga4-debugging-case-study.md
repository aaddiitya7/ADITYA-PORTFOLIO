# Case Study: Diagnosing & Fixing a Silent Google Analytics 4 Failure

> **[Your Name]** — Digital Marketing Strategist  
> **Date:** March 2026  
> **Client / Project:** A.S. Enterpriis — Leather Garments & Safety Equipment Manufacturer  
> **Website:** [asenterpriis.com](https://www.asenterpriis.com)

---

## At a Glance

| Detail | Info |
|---|---|
| **Industry** | B2B Manufacturing & Export |
| **Platform** | Next.js on Vercel |
| **Analytics Tool** | Google Analytics 4 |
| **Issue Duration** | ~7 days of lost data |
| **Time to Resolution** | Under 2 hours |
| **Outcome** | Full data collection restored ✅ |

---

## The Challenge

After launching a new company website for A.S. Enterpriis — a Kolkata-based leather garments and safety equipment manufacturer — I set up Google Analytics 4 (GA4) to track website traffic, user behavior, and lead generation performance.

Everything appeared to be configured correctly:
- ✅ The GA4 property was created
- ✅ The Measurement ID was embedded in the website code
- ✅ The site was deployed and live on Vercel

**But after 7 days, the GA4 dashboard showed zero data. No users. No sessions. No page views. Nothing.**

The "Data collection isn't active" warning persisted, and the Realtime overview was completely empty — even when visiting the site in real time from different devices and networks.

<!-- 📸 INSERT SCREENSHOT: GA4 dashboard showing "No data received from your website yet" -->
<!-- Suggested image: assets/ga4-no-data-received.png -->

---

## The Impact

Without working analytics, the entire digital marketing strategy was flying blind:

- **No visibility** into which pages users were visiting
- **No conversion tracking** for the inquiry form
- **No data** on traffic sources (organic, referral, direct)
- **No way to measure ROI** on any marketing campaigns
- **~7 days of traffic data permanently lost** — data that could never be recovered

For a B2B manufacturing company targeting international buyers, every website visit is a potential high-value lead. Losing visibility into that traffic was not an option.

---

## The Investigation

### Step 1: Verify the Setup (Surface-Level Check)

I first confirmed the basics:

| Check | Status |
|---|---|
| Measurement ID in website code | ✅ Present |
| Measurement ID matches GA4 dashboard | ✅ Match |
| Website URL in Data Stream | ✅ Correct |
| Code deployed to production (Vercel) | ✅ Live |
| Enhanced Measurement enabled | ✅ On |

Everything looked correct on paper. This is the trap that catches most people — when all the visible configuration is right, but data still isn't flowing.

### Step 2: Network-Level Debugging (Going Deeper)

I opened the browser developer tools on the live production site and inspected the network requests. This is where I found the smoking gun:

**The Google Analytics tracking script was failing to load.**

The browser was requesting:
```
https://www.googletagmanager.com/gtag/js?id=G-4JGJ4J601K
```

But instead of returning the tracking JavaScript code, **Google's servers were responding with a 404 (Not Found) error.**

| Request | Expected Response | Actual Response |
|---|---|---|
| `gtag/js?id=G-4JGJ4J601K` | 200 OK (JavaScript) | **404 Not Found (HTML error page)** |

This meant:
- The tracking code on the website was executing correctly
- It was calling out to Google's servers as expected
- But Google's servers did not recognize the Measurement ID as valid
- **No tracking data was ever transmitted**

### Step 3: Root Cause Analysis

The Measurement ID `G-4JGJ4J601K` existed in the GA4 admin panel and was assigned to the correct property. So why was Google's own server rejecting it?

**Root Cause:** The GA4 property had recently been migrated between accounts (moved from "Default Account for Firebase" to a new "A.S. Enterpriis" account). During this account-level migration, the existing Data Stream and its associated Measurement ID became orphaned — the ID was visible in the GA4 admin interface but was no longer recognized by Google's global tag-serving infrastructure.

This is a rare but documented edge case where GA4's admin UI falls out of sync with its backend data collection pipeline after a property move.

---

## The Solution

### Action 1: Remove the Broken Data Stream
I deleted the non-functional data stream (Measurement ID: `G-4JGJ4J601K`) from the GA4 property settings.

### Action 2: Create a Fresh Data Stream
I created a brand-new Web data stream within the same property:
- **Stream URL:** `https://as-enterprise-coral.vercel.app`
- **Stream Name:** AS Enterprise Website
- **New Measurement ID:** `G-W35DVT07PR`

### Action 3: Verify the New ID Works
Before updating the website, I verified that Google's servers recognized the new ID:

| Request | Response |
|---|---|
| `gtag/js?id=G-W35DVT07PR` | **200 OK ✅** |

### Action 4: Update & Deploy
I updated the Measurement ID in the website code and deployed via the CI/CD pipeline (GitHub → Vercel). The change was live within 60 seconds.

### Action 5: Confirm Data Collection
Within minutes of deployment, the GA4 Realtime overview showed:
- **1 active user** 
- **Location:** Kolkata, India
- **Data collection status:** Active 🎉

<!-- 📸 INSERT SCREENSHOT: GA4 Realtime overview showing 1 active user in Kolkata -->
<!-- Suggested image: assets/ga4-realtime-success.png -->

---

## The Results

| Metric | Before | After |
|---|---|---|
| Data Collection Status | ❌ Inactive | ✅ Active |
| Realtime Users Visible | 0 | 1+ |
| Page Views Tracked | 0 | Recording |
| Events Captured | None | Page views, scrolls, clicks, outbound clicks |
| Time to Fix | — | < 2 hours |

---

## Key Takeaways

### 1. "Configured" Does Not Mean "Working"
The GA4 admin panel showed everything was set up correctly. The Measurement ID was present, the stream URL was right, and enhanced measurement was enabled. But without verifying at the network level that data was actually flowing, the issue remained invisible for days.

### 2. Always Verify at the Network Level
The single most effective debugging step was checking whether `googletagmanager.com/gtag/js?id=YOUR_ID` returns a **200 status code**. If it returns 404, your tracking is completely broken — no matter how perfect your configuration looks.

### 3. Account Migrations Can Break Data Streams
Moving a GA4 property between accounts is a supported feature, but it can cause data streams to become disconnected from Google's tag-serving infrastructure. After any account-level migration, always verify data collection is still active.

### 4. Use Realtime Reports for Instant Verification
The GA4 Realtime overview is the fastest way to confirm tracking is working. Open your website in one tab, the Realtime report in another, and you should see activity within seconds.

---

## Tools & Skills Demonstrated

- **Google Analytics 4** — Property setup, data stream management, realtime monitoring
- **Web Analytics Debugging** — Network inspection, HTTP status verification, tag validation
- **Digital Marketing Analytics** — Understanding the business impact of data loss
- **CI/CD Deployment** — Vercel auto-deploy pipeline via GitHub
- **AI-Assisted Problem Solving** — Leveraging AI tools for systematic diagnosis and resolution

---

## About

> **[Your Name]**  
> [Your Title] — Digital Marketing  
> [Your Email] | [Your Phone] | [Your LinkedIn]  
>  
> I help businesses build, measure, and optimize their digital presence — combining marketing strategy with technical expertise and modern AI tools to deliver results.

---

*This case study documents a real incident encountered and resolved during the launch of the A.S. Enterpriis company website in March 2026.*
