# 🧠 Mental Health Professionals in Punjab – Data Analysis Project

This project automates the identification, profiling, and digital presence analysis of mental health professionals across Punjab, India. It includes data scraping, cleaning, enrichment with social media and SEO metrics, and visualization through Power BI dashboards. The goal is to support data-driven decisions in outreach, marketing, and collaboration within the mental health sector.

---

## 📚 Table of Contents

1. [Abstract](#abstract)  
2. [Introduction](#introduction)  
3. [Objectives](#objectives)  
4. [Scope of Work](#scope-of-work)  
5. [Data Collection](#data-collection)  
6. [Social Media & SEO Data Extraction](#social-media--seo-data-extraction)  
7. [Data Cleaning and Preparation](#data-cleaning-and-preparation)  
8. [Dashboard Development](#dashboard-development)  
9. [Insights and Analysis](#insights-and-analysis)  
10. [Conclusion](#conclusion)  
11. [References](#references)  
12. [Appendix](#appendix)

---

## 📌 Abstract

This project aimed to automate the end-to-end process of identifying and profiling mental health professionals across Punjab. The workflow included web scraping, social media profiling, SEO performance evaluation, data cleaning using Python (Pandas), and dashboard visualization using Power BI. The final deliverables consist of structured data and three interactive dashboards focused on Personal Information, Social Media Optimization (SMO), and Search Engine Optimization (SEO). This project supports data-driven decisions for outreach, marketing, and partnerships within the mental health sector.

---

## 🧾 Introduction

In an era where digital presence influences professional reach and trust, it is critical to understand how healthcare professionals engage online. Especially in mental health—a field driven by visibility, credibility, and outreach—evaluating digital metrics becomes essential.  
This project tackles the challenge of identifying and assessing mental health professionals (psychologists, counsellors, rehab centres, etc.) across Punjab by automating data collection and creating meaningful dashboards to highlight their online presence and opportunities for digital growth.

---

## 🎯 Objectives

- Extract valid leads of psychologists and mental health professionals from Google Maps using automation tools.  
- Gather detailed social media metrics (Instagram, Facebook, LinkedIn).  
- Extract SEO performance metrics for each professional's website.  
- Clean and prepare data using the Python library Pandas.  
- Design three user-friendly dashboards for data interpretation.  
- Derive meaningful insights that support digital outreach and decision-making.

---

## 📦 Scope of Work

- Focused on professionals in psychology, counselling, psychiatry, therapy, and mental wellness.  
- Covered all districts and cities across Punjab, India.  
- Used publicly available data from web platforms and SEO tools.  
- Delivered three Power BI dashboards: Personal Info, SMO, and SEO.

---

## 🗂️ Data Collection

### 🔧 Tools Used:
- **Playwright (Python)** – For headless browser automation (Google Maps scraping)  
- **BeautifulSoup (bs4)** – For HTML parsing and data extraction  
- **Custom Scripts** – To handle dynamic loading, pagination, and metadata

### 📄 Data Columns Extracted:
- Name  
- Workplace / Clinic  
- Profession  
- Address (City, State, PIN)  
- Contact Number  
- Email ID  
- Website URL  

> 🔹 **Raw Records**: 1700+  
> 🔹 **Cleaned & Valid Entries**: 1000+

---

## 📱 Social Media & SEO Data Extraction

### 🔍 Platforms Tracked:
- Instagram  
- Facebook  
- LinkedIn

### 📊 Fields Extracted:
- Number of followers / following  
- Last post date  
- Profile bio  
- Activity status (Active/Inactive)

### 🌐 Website SEO Metrics (via Moz, PageSpeed, etc.):
- Domain Authority (DA)  
- Page Authority (PA)  
- Spam Score (SS)  
- Page Load Speed (Mobile & Desktop)

> Combined these metrics to evaluate overall digital discoverability and site performance.

---

## 🧹 Data Cleaning and Preparation

Performed using **Pandas (Python)** with steps like:

- Removed special characters, emojis, and invisible Unicode  
- Trimmed spaces and normalized string formats  
- Handled missing values using placeholders  
- Standardized city names and profession categories  
- Verified and corrected URLs  
- Adjusted formatting to aid dashboard filtering  

> Included manual validation for SEO/social links to ensure accuracy.

---

## 📊 Dashboard Development

Three dashboards were developed in **Power BI** with slicers, filters, cards, and advanced visuals.

### 🧾 1. Personal Information Dashboard
- **Purpose**: Show identity, contact, and education details  
- **Visuals**:  
  - Table with Name, Contact, Address, Website  
  - Donut Chart: Education breakdown  
  - Bar Chart: Distribution by city  
  - Filters: Profession, City, Education  

### 📱 2. SMO Dashboard (Social Media Optimization)
- **Purpose**: Highlight social media activity & engagement  
- **Visuals**:  
  - KPI Cards: Profile count, Active %  
  - Top 5 Followed Professionals  
  - Line Chart: Posting Trends  
  - Pie Chart: Platform activity share  
  - Filters: Platform, Status, Profession  

### 🌐 3. SEO Dashboard (Search Engine Optimization)
- **Purpose**: Evaluate site performance and ranking  
- **Visuals**:  
  - Table with DA, PA, SS, Speed  
  - Conditional formatting for strong/weak SEO  
  - KPI Cards: Avg DA/PA, Speed scores  
  - Bar Chart: Top sites by DA  
  - Filters: City, DA range

---

## 📈 Insights and Analysis

### 🧾 From Personal Info:
- Ludhiana, Chandigarh, Amritsar, and Patiala had the most professionals.  
- M.A. Clinical Psychology and M.Phil. were common qualifications.  
- Many lacked professional websites or email addresses.

### 📱 From SMO:
- Over 40% lacked active Instagram or Facebook profiles.  
- A few had 10K+ followers, showing influencer potential.  
- Facebook had higher inactivity compared to Instagram.

### 🌐 From SEO:
- Only ~25% had DA above 20 → need for SEO improvement.  
- Poor mobile speeds and missing HTTPS were common.  
- Several sites were outdated or lacked optimization.

---

## ✅ Conclusion

This project successfully automated the entire lead generation and digital profiling pipeline—from scraping and enrichment to dashboard creation. It delivers valuable insights into the online presence of mental health professionals in Punjab and can be scaled to other regions or industries for similar digital outreach assessments.

---

## 🔗 References

1. Google Maps  
2. Playwright & BeautifulSoup (Python)  
3. Moz, PageSpeed Insights  
4. Instagram, Facebook, LinkedIn  
5. Pandas, Power BI

---
