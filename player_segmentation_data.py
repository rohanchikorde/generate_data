import random
import pandas as pd

# Set the number of rows
num_rows = 10000

# Generate dummy values for each feature
data = []
for _ in range(num_rows):
    row = {}
    age = random.randint(18, 60)
    row["Player Age"] = age
    row["Player Gender"] = random.choice(["Male", "Female"])
    if age < 30:
        row["Player Location"] = random.choice(["USA", "UK"])
    else:
        row["Player Location"] = random.choice(["Canada", "Australia"])
    row["Player Activity Level"] = random.choice(["Low", "Medium", "High"])
    row["Player Skill Level"] = random.choice(["Beginner", "Intermediate", "Advanced"])
    row["Player Spending Habits"] = random.choice(["Low", "Medium", "High"])
    if row["Player Activity Level"] == "High":
        row["Player Engagement Frequency"] = random.choice(["Daily", "Weekly"])
    else:
        row["Player Engagement Frequency"] = random.choice(["Weekly", "Monthly"])
    if row["Player Skill Level"] == "Advanced":
        row["Player Game Preferences"] = random.choice(["Action", "Strategy"])
    else:
        row["Player Game Preferences"] = random.choice(["Action", "Puzzle"])
    if row["Player Activity Level"] == "High":
        row["Player Social Interactions"] = random.choice(["Medium", "High"])
    else:
        row["Player Social Interactions"] = random.choice(["Low", "Medium"])
    if row["Player Gender"] == "Male":
        row["Player Device Type"] = random.choice(["Mobile", "PC"])
    else:
        row["Player Device Type"] = random.choice(["PC", "Console"])
    if row["Player Location"] == "USA":
        row["Player Session Duration"] = random.randint(30, 120)
    elif row["Player Location"] == "UK":
        row["Player Session Duration"] = random.randint(20, 90)
    elif row["Player Location"] == "Canada":
        row["Player Session Duration"] = random.randint(10, 60)
    else:
        row["Player Session Duration"] = random.randint(40, 150)
    row["Player In-Game Achievements"] = random.randint(0, 100)
    row["Player Churn Probability"] = random.uniform(0, 1)
    row["Player Lifetime Value"] = random.randint(100, 1000)
    row["Player Feedback and Ratings"] = random.randint(1, 5)
    data.append(row)

# Create a pandas DataFrame from the generated data
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
filename = "player_segmentation_data.csv"
df.to_csv(filename, index=False)

print(f"Data saved successfully in {filename}")
