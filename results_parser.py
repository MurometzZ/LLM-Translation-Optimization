import json
from pathlib import Path

# target_dir = Path("EN to RU/llama3.1_8b/Crime and Punishment/Chapter_1/ratings")
target_dir = Path("ratings")

average_score = 0
counter = 0

for file in target_dir.glob("*.txt"):
    with open(file) as f:
        data = json.load(f)
        
        average_score += int(data["rating"]["Meaning"])
        counter += 1


average_score = average_score / counter
print(average_score)