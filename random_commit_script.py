import os
from random import randint, random, choice
from datetime import datetime, timedelta

# Automatically set start and end dates
start_date = datetime.now() - timedelta(days=1)  # Yesterday
end_date = datetime.now()  # Today

# Commit range and zero-commit chance
commit_range = (0, 13)  # Min and max commits per day
zero_commit_chance = 20  # Percentage chance of a zero-commit day

# List of random commit messages
commit_messages = [
  "Refactored code",
  "Fixed minor bug",
  "Updated documentation",
  "Improved performance",
  "Added new feature",
  "Code cleanup",
  "Updated dependencies",
  "Fixed typos",
  "Optimized algorithm",
  "Improved error handling"
]

# Calculate total days between dates
total_days = (end_date - start_date).days

for i in range(total_days + 1):  # +1 to include the end date
  # Calculate the date for the commit
  commit_date = start_date + timedelta(days=i)

  # Determine time range based on whether it's a weekday or weekend
  if commit_date.weekday() < 5:  # Monday to Friday
    time_ranges = [(8, 9), (15, 21)]
  else:  # Saturday and Sunday
    time_ranges = [(10, 22)]

  # Select a random hour within the allowed time range
  selected_range = choice(time_ranges)
  commit_hour = randint(selected_range[0], selected_range[1])
  commit_minute = randint(0, 59)
  commit_second = randint(0, 59)
  commit_date_str = commit_date.replace(hour=commit_hour, minute=commit_minute, second=commit_second).strftime('%Y-%m-%dT%H:%M:%S')

  # Determine if today will be a 0-commit day based on the zero_commit_chance
  if random() < zero_commit_chance / 100:
    print(f"Skipping commits for {commit_date.strftime('%Y-%m-%d')}")
    continue  # Skip this day (0 commits)

  # Randomize the number of commits for the day within range x - y
  for j in range(randint(commit_range[0], commit_range[1])):
    # Choose a random commit message
    commit_message = choice(commit_messages)
    
    # Decide randomly whether to add a line or remove a line
    if random() < 0.5:
      # Add a line to the file
      with open('file.txt', 'a') as file:
        file.write(f"Commit on {commit_date_str}\n")
    else:
      # Remove a line from the file (if not empty)
      with open('file.txt', 'r') as file:
        lines = file.readlines()
      if lines:
        with open('file.txt', 'w') as file:
          file.writelines(lines[:-1])  # Remove the last line

    # Stage the file and create a commit with a random message and specific date
    os.system('git add file.txt')
    os.system(f'git commit --date="{commit_date_str}" -m "{commit_message}"')

# Push all commits for the day to the remote repository
os.system('git push --set-upstream origin master')
