import pandas as pd

# Create a sample DataFrame with columns
columns = [
    'Organization Name', 
    'Organization Type', 
    'Organization Description', 
    'Contact Person', 
    'Contact Email', 
    'Contact Phone',
    'Technical Skills', 
    'Industry Domains', 
    'Research Areas', 
    'Service Offerings', 
    'Technologies Used',
    'Keywords for Matching'
]

# Create an empty DataFrame
df = pd.DataFrame(columns=columns)

# Example rows to demonstrate structure
sample_data = [
    [
        'Brightlands Smart Services', 
        'Innovation Campus', 
        'Open innovation ecosystem focused on AI and Data Science', 
        'Campus Director', 
        'director@brightlands.com', 
        '+31 XX XXX XXXX',
        'AI, Machine Learning, Data Analysis', 
        'Technology Transfer, Innovation', 
        'AI Ethics, Smart Services', 
        'Ecosystem Facilitation, Matchmaking', 
        'Python, Jupyter, TensorFlow',
        'innovation, AI, data science, ecosystem'
    ],
    [
        'Local University AI Department', 
        'Research Institute', 
        'Leading AI research and education center', 
        'Head of AI Research', 
        'ai.research@university.edu', 
        '+31 XX XXX XXXX',
        'Machine Learning, Natural Language Processing', 
        'Healthcare, Education', 
        'AI Ethics, Deep Learning', 
        'Research Collaboration, Consulting', 
        'Python, PyTorch, Scikit-learn',
        'research, machine learning, healthcare'
    ]
]

# Add sample data to DataFrame
for row in sample_data:
    df.loc[len(df)] = row

# Save to Excel
df.to_excel('Brightlands_Stakeholder_Mapping.xlsx', index=False)

print("Excel template created successfully!")
