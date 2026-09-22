import pandas as pd
from faker import Faker
from pathlib import Path
import random

# -----------------------------
# 1. Configuration
# -----------------------------

SEED = 42

random.seed(SEED)
fake = Faker()
fake.seed_instance(SEED)

# Project root directory
BASE_DIR = Path(__file__).resolve().parents[2]

# Output directory
OUTPUT_DIR = BASE_DIR / "data" / "raw"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# -----------------------------
# 2. Team information
# -----------------------------

teams = [
    {
        "team_id": "T001",
        "team_name": "Backend Engineering",
        "department": "Engineering"
    },
    {
        "team_id": "T002",
        "team_name": "Frontend Engineering",
        "department": "Engineering"
    },
    {
        "team_id": "T003",
        "team_name": "Mobile Engineering",
        "department": "Engineering"
    },
    {
        "team_id": "T004",
        "team_name": "Data Engineering",
        "department": "Data"
    },
    {
        "team_id": "T005",
        "team_name": "DevOps Engineering",
        "department": "Engineering"
    },
    {
        "team_id": "T006",
        "team_name": "QA Engineering",
        "department": "Quality"
    },
    {
        "team_id": "T007",
        "team_name": "AI Engineering",
        "department": "Artificial Intelligence"
    },
    {
        "team_id": "T008",
        "team_name": "Platform Engineering",
        "department": "Engineering"
    }
]


# -----------------------------
# 3. Generate team leads
# -----------------------------

for team in teams:
    team["team_lead_id"] = f"D{teams.index(team) + 1:03d}"
    team["created_date"] = fake.date_between(
        start_date="-5y",
        end_date="-1y"
    )


# -----------------------------
# 4. Convert to DataFrame
# -----------------------------

df = pd.DataFrame(teams)


# -----------------------------
# 5. Save CSV
# -----------------------------

output_file = OUTPUT_DIR / "teams.csv"

df.to_csv(output_file, index=False)

print("Teams dataset generated successfully!")
print(f"File saved to: {output_file}")
print(f"Number of teams: {len(df)}")

print("\nDataset preview:")
print(df)