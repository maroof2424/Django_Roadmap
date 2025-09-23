import os

# Base directory for Django Roadmap
base_dir = "Django_Roadmap"

# Week names
weeks = [
    "Week01_Fundamentals",
    "Week02_Models_ORM",
    "Week03_Admin_Forms",
    "Week04_Auth_Relationships",
    "Week05_Blog_Part1",
    "Week06_Blog_Part2",
    "Week07_Todo_Ecommerce",
    "Week08_CBVs_Middleware",
    "Week09_DRF_Deployment",
    "Week10_Signals_Caching",
    "Week11_Testing_Async",
    "Week12_Scaling_FinalProject"
]

# Create main roadmap folder
os.makedirs(base_dir, exist_ok=True)

# Create week folders + README.md inside each
for week in weeks:
    week_path = os.path.join(base_dir, week)
    os.makedirs(week_path, exist_ok=True)
    
    readme_path = os.path.join(week_path, "README.md")
    if not os.path.exists(readme_path):
        with open(readme_path, "w") as f:
            f.write(f"# {week}\n\nNotes and tasks for {week.replace('_', ' ')}.")

print("✅ Django roadmap directories with README.md created successfully!")
