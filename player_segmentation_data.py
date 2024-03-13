import random
import csv

# Define the list of features
features = [
    "Player Age",
    "Player Gender",
    "Player Location",
    "Player Activity Level",
    "Player Skill Level",
    "Player Spending Habits",
    "Player Engagement Frequency",
    "Player Game Preferences",
    "Player Social Interactions",
    "Player Device Type",
    "Player Session Duration",
    "Player In-Game Achievements",
    "Player Churn Probability",
    "Player Lifetime Value",
    "Player Feedback and Ratings"
]

# Set the number of rows
num_rows = 10000

# Generate dummy values for each feature
data = []
for _ in range(num_rows):
    row = {}
    for feature in features:
        if feature == "Player Age":
            row[feature] = random.randint(18, 60)
        elif feature == "Player Gender":
            row[feature] = random.choice(["Male", "Female"])
        elif feature == "Player Location":
            row[feature] = random.choice(["USA", "UK", "Canada", "Australia"])
        elif feature == "Player Activity Level":
            row[feature] = random.choice(["Low", "Medium", "High"])
        elif feature == "Player Skill Level":
            row[feature] = random.choice(["Beginner", "Intermediate", "Advanced"])
        elif feature == "Player Spending Habits":
            row[feature] = random.choice(["Low", "Medium", "High"])
        elif feature == "Player Engagement Frequency":
            row[feature] = random.choice(["Daily", "Weekly", "Monthly"])
        elif feature == "Player Game Preferences":
            row[feature] = random.choice(["Action", "Strategy", "Puzzle"])
        elif feature == "Player Social Interactions":
            row[feature] = random.choice(["Low", "Medium", "High"])
        elif feature == "Player Device Type":
            row[feature] = random.choice(["Mobile", "PC", "Console"])
        elif feature == "Player Session Duration":
            row[feature] = random.randint(10, 120)
        elif feature == "Player In-Game Achievements":
            row[feature] = random.randint(0, 100)
        elif feature == "Player Churn Probability":
            row[feature] = random.uniform(0, 1)
        elif feature == "Player Lifetime Value":
            row[feature] = random.randint(100, 1000)
        elif feature == "Player Feedback and Ratings":
            row[feature] = random.randint(1, 5)
    data.append(row)

# Save the generated data in a CSV file
filename = "player_segmentation_data.csv"
with open(filename, "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=features)
    writer.writeheader()
    writer.writerows(data)

print(f"Data saved successfully in {filename}")
