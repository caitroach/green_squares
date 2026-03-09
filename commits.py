'''
people on github are LYING TO YOU!!!!!
i too have been intimidated by large arrays of green squares, but it's really easy to automate and fake github activity.
i'm keeping this public as a demonstration but here's how it's done ! ! !! ! I am not trying to con you
but some people are........ this is an expose 
i'm gonna test it on my repo then probably turn it off
maybe
sorry
'''

import os 
import random 
import datetime 
import json 
import subprocess


quotes = [ # various selected tweets, bumper stickers, and thoughts
    "I am batman",
    "just remember that you are ENOUGH. we don't need any more of you.",
    "if at first you don't succeed, skydiving is not for you.",
    "every dead body on mt everest was once highly motivated. being lazy could save your life. stay lazy.",
    "ricky gervais is horrificially overrated imo",
    "i'm not really sure how many quotes to put in here",
    "the repo I'm looking at had a lot but",
    "i think maybe it was vibe coded because that's way too many emojis",
    "just a ton of emojis",
    "or maybe the plural of emoji is emoji?",
    ":3",
    "meow",
    "mnemotic to memorize the great lakes: Leslie Likes Licking Lettuce Lightly (Lake Ontario, Lake Huron, Lake Erie, Lake Michigan, Lake... whatever the last one is)",
    "I'm an adult, i should know what the great lakes are",
    "if anyone reads this it'll look really unprofessional",
    "sorry whoever is reading this",
    "i am but a humble nigiri on the rotating sushi conveyor belt of life",
    "ios11",
    "brought to you by clippy",
    "visit https://cait.lol (BUT NOT ON MOBILE PLEASE I DON'T KNOW REACT YET)",
    "though tbh maybe vanilla HTML/CSS/JS is sometimes harder than just giving up and learning react",
    "meow again",
    "keep honking! i'm listening to honking", 
    "honk if you honk",
    "no baby on board so feel free to hit me",
    "bigfoot saw me and nobody believed her", 
    "criminalize bumper stickers",
    "red delicious is, like, the least delicious apple",
    "honeycrisp and granny smith for life!",
    "actually who the hell is granny smith? what a diva. love her",
    "my other car is another car with a sticker on the car that says this my other car",
    "don't like my driving? STAY OFF THE SIDEWALK!",
    "jk i don't advocate for violence against pedestrians. i am more often a pedestrian than i am a driver tbh",
    "nothing bad can happen. it can only good happen"


]

commit_messages = [
    "I am but a liar",
    "commit message",
    "am I a human?",
    "do automated commit messages dream of electric sheep?",
    "gamestop2themoon!",
    "idk how to parallel park",
    "committing commits",
    "commitment issues",
    "sent emails",
    "ran for mayor",
    "assassinated a political figure",
    "won the olympics",
    "we love you Alysa Liu!",
    "cait wasn't here",
    "this is how people lie",
    "LIED",
    "throwing away your morals for a green box",
    "LCDSOUNDSYSTEM2026!"
    # i cant think of any more tbh
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
    num_days = random.randint(3, 5)
    week_commits = sorted(random.sample(range(7), num_days))
    week_data[week_key] = week_commits  #  fixed
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

    subprocess.run(["git", "push"])
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
