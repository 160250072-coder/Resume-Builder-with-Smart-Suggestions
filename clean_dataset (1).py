import pandas as pd

df = pd.read_csv("Resume.csv")

# Clean column names (VERY IMPORTANT)
df.columns = df.columns.str.strip()

print("Columns after cleaning:", df.columns.tolist())

# Create new dataframe safely
clean_df = pd.DataFrame({
    "role": df["Category"],
    "skills": df["Resume_str"]
})

# Save file
clean_df.to_csv("dataset/resumes.csv", index=False)

print("✅ Dataset cleaned and saved successfully!")