# LinkedIn Job Auto-Apply Bot (Python + Selenium)

This script automates the process of applying for jobs on LinkedIn using Selenium WebDriver. It filters job listings and attempts to apply using the "Easy Apply" feature. Complex applications are skipped.

---

## 🚀 Features

- Logs into LinkedIn using your credentials
- Filters job listings based on your search
- Clicks on job postings and attempts to apply
- Skips complex applications that require more than just a click
- Automatically fills in your phone number if not pre-filled

---

## ⚠️ Disclaimer

> **Use this script responsibly and at your own risk.**  
LinkedIn may suspend your account for using automation tools in violation of their Terms of Service. This is for educational purposes only.

---

## 🧰 Requirements

- Python 3.x
- Google Chrome
- ChromeDriver (must match your Chrome version)
- LinkedIn account with Easy Apply-enabled profile

---

## 📦 Installation

1. **Clone the repository** or copy the script into a `.py` file.
2. **Install dependencies:**
   ```bash
   pip install selenium
## Download ChromeDriver from: https://sites.google.com/a/chromium.org/chromedriver/downloads
Ensure it's in your PATH or same directory as your script.
##🔧 Configuration
Edit the following variables in the script to match your credentials:

ACCOUNT_EMAIL = 'your-email@example.com'
ACCOUNT_PASSWORD = 'your-password'
PHONE = 'your-phone-number'
## You may also modify the job search URL to fit your needs:
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=...&keywords=...")

## 🛑 Limitations
Only supports "Easy Apply" jobs.

Does not handle multi-step applications.

Assumes certain LinkedIn UI structures — subject to break if LinkedIn updates their layout.

## ✅ Tips
Run it with a test LinkedIn account to avoid risking your main one.

Use chrome_options.add_argument('--headless') if you want to run it in background mode.

Add error logging or email notifications to track status at scale.


