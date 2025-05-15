import json, smtplib, os, random
from dotenv import load_dotenv

load_dotenv()

# Load all problems
with open("leetcode_problems_30.json", "r") as f:
    all_problems = json.load(f)

# Load previously sent problem titles
sent_file = "sent_questions.json"
if os.path.exists(sent_file):
    with open(sent_file, "r") as f:
        sent_titles = json.load(f)
else:
    sent_titles = []

# Filter unsent problems
unsent = [q for q in all_problems if q["title"] not in sent_titles]

if not unsent:
    print("All questions have been sent! Resetting the list.")
    # Optionally reset:
    sent_titles = unsent = []
    unsent = all_problems.copy()

# Pick a new problem
question = random.choice(unsent)

# --- Send Email ---
conn = smtplib.SMTP("smtp.gmail.com", 587)
conn.starttls()
conn.login(os.getenv("MY_EMAIL"), os.getenv("EMAIL_PASSWORD"))

subject = f"LeetCode Easy: {question['title']}"
body = f"""\
Description:
{question['description']}

Topic: {question['topic']}

Real-World Use:
{question['real_world_intuition']}

Simple Explanation:
{question['simple_explanation']}

Link:
{question['url']}
"""
msg = f"Subject: {subject}\n\n{body}"
conn.sendmail(from_addr=os.getenv("MY_EMAIL"), to_addrs=os.getenv("TO_EMAIL"), msg=msg)
conn.quit()

# Save the sent title
sent_titles.append(question["title"])
with open(sent_file, "w") as f:
    json.dump(sent_titles, f, indent=2)

print(f"Sent: {question['title']}")
