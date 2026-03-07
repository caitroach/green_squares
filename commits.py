'''
people on github are LYING TO YOU!!!!!
i too have been intimidated by large arrays of green squares, but it's really easy to automate and fake github activity.
i'm keeping this public as a demonstration but here's how it's done ! ! !! ! I am not trying to con you
but some people are........
'''

import os 
import random 
import datetime 
import json 
import subprocess

quotes = [
    "I am batman",
    "does this work?",
]

commit_messages = [
    "I am but a liar"
]

target_files = ["daily_log.txt", "progress.md", "inspiration.txt"]


counter_file = ".commit_tracker.json"
min_total = 3
max_total = 15

if os.path.exists(counter_file): # grab tracking
    with open(counter_file, "r") as f:
        data = json.load(f)
else:
    data = {}

now = datetime.datetime.now()
weekday = now.weekday()
date_key = now.strftime('%Y-%m-%d')
timestamp = now.strftime('%Y-%m-%d %I:%M:%S %p')

def get_week_key(date): 
    return date.strftime("%Y-W%U") # year-week number 


week_key = get_week_key(now)
week_data = data.get("week_data", {})
week_commits = week_data.get(week_key, [])

if len(week_commits) == 0:
    num_days = random.randint(3, 5) # this makes it look natural, commits 3 to 5 days per week
    week_commits = sorted(random.sample(range(7), num_days)) # pick 3-5 random days, at random
    week_data = [week_key] = week_commits
    data["week_data"] = week_data
    with open(counter_file, "w") as f: 
        json.dump(data, f)
    
if weekday not in week_commits:
    print(f"not committing.")
    exit()

done = data.get(date_key, 0)
remaining = max_total - done 
if remaining <= 0:
    print("max commits reached.")
    exit()

slot_commit = random.randint(1, 5)
slot_commit = min(slot_commit, remaining)

if done + slot_commit < min_total and remaining <= 6:
    slot_commit = min(min_total - done, remaining)

log_entries = []

# picking random useless things to commit
for _ in range(slot_commit):
    quote = random.choice(quotes)
    message = random.choice(commit_messages)
    filename = random.choice(target_files)
    # puts a rnadom quote with a random message in a random file, randomly, at random.
    # random.

    with open(filename, "a") as f:
        f.write(f"[{timestamp}] {quote}\n")

    subprocess.run(["git", "add", filename])
    subprocess.run(["git", "commit", "-m", message])
    log_entries.append(f"[{timestamp}] - {message}")


# then once you've LIED like a LIAR, update your tracking

data[date_key] = done + slot_commit
data["week_data"] = week_data
with open(counter_file, "w") as f:
    json.dump(data, f)

if slot_commit > 0: 
    with open("commit_log.txt", "a") as log:
        log.write(f"[{timestamp}] +{slot_commit} commits\n")
        log.write("\n".join(log_entries) + "\n\n")

print(f"{slot_commit} commits made at {timestamp}. total today: {done + slot_commit}")