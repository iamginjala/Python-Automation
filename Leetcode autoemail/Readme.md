# 📧 LeetCode Daily Email Automation

Automatically sends a **LeetCode Easy** problem to your email every morning at **8 AM CST**, including:

- 🧠 Problem title + description
- 🌍 Real-world intuition
- 💡 Simple explanation
- 🔗 LeetCode problem link

---

## 🚀 Features

- Sends **one random, unsolved** LeetCode Easy problem daily
- Prevents duplicate sends using a local tracking file
- Fully configurable using `.env` credentials
- Runs automatically using Windows Task Scheduler at 8 AM CST

---

## 🛠️ Tech Stack

- Python 3.10+
- `smtplib` for sending emails via Gmail SMTP
- `dotenv` to manage credentials securely
- `json` for problem tracking and rotation

---

## 📂 Project Structure

leetcode-autoemail/
│
├── main.py # Main script to send email
├── .env # Email credentials and recipient
├── leetcode_problems_30.json # Problem pool (30 easy problems)
├── sent_questions.json # Auto-generated file to track sent problems
└── README.md # This file

1. Add Environment Variables
Create a .env file with:
MY_EMAIL=your.address@gmail.com
EMAIL_PASSWORD=your_16_digit_app_password
TO_EMAIL=recipient@example.com
⚠️ Make sure you generate an App Password from your Google account. Gmail no longer supports plain passwords.

3. Run It Once
python main.py

4. Schedule to Run Daily at 8 AM CST (Windows)
Open Task Scheduler

Create Basic Task → Trigger = Daily at 8:00 AM

Action → Start a Program

Program/script: python

Add arguments: main.py

Start in: C:\path\to\your\project

✅ Make sure the computer is not in sleep or shut down state. You can lock the screen or close the lid (if power settings are adjusted).


## ✨ Future Enhancements
 Add HTML email formatting for nicer styling

 Add dashboard to track solved problems

 Deploy as cloud job (AWS Lambda or Railway)

## 📬 Example Email Output
Subject: LeetCode Easy: Two Sum

Description:
Given an array of integers nums and an integer target...

Topic: Array, Hash Table

Real-World Use:
Used in expense reconciliation tools to find two items that match a total.

Simple Explanation:
Store numbers in a hash map while scanning to find complement values.

Link:
https://leetcode.com/problems/two-sum/
 
