import os

# Base directory for Django Roadmap
base_dir = "Django_Roadmap"

# Week names for 15-week roadmap
weeks = [
    "Week01_Fundamentals",
    "Week02_Models_ORM",
    "Week03_Admin_Forms",
    "Week04_Auth_Relationships",
    "Week05_Blog_Part1",
    "Week06_Blog_Part2",
    "Week07_Todo_Ecommerce",
    "Week08_CBVs_Middleware",
    "Week09_CrispyForms_AdvancedForms",
    "Week10_DRF_Deployment",
    "Week11_Signals_Caching",
    "Week12_Testing_Async",
    "Week13_Submodules_DeepDive",
    "Week14_Scaling_FinalProject",
    "Week15_ML_Integration"
]

# Create main roadmap folder
os.makedirs(base_dir, exist_ok=True)

# Create week folders + README.md + Mini_Projects folder inside each

for week in weeks:
    week_path = os.path.join(base_dir, week)
    os.makedirs(week_path, exist_ok=True)
    
    # README.md
    readme_path = os.path.join(week_path, "README.md")
    if not os.path.exists(readme_path):
        with open(readme_path, "w") as f:
            f.write(f"# {week}\n\nNotes and tasks for {week.replace('_', ' ')}.")
    
    # Mini_Projects folder
    mini_project_path = os.path.join(week_path, "Mini_Projects")
    os.makedirs(mini_project_path, exist_ok=True)

print("✅ Django 15-week roadmap directories with README.md and Mini_Projects folders created successfully!")
