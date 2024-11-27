import pandas as pd
import random

# Lists for generating realistic mock data
organization_types = [
    'Public Service Agency', 'Healthcare Innovation Center', 
    'Circular Economy Startup', 'Innovative SME', 
    'Research Institute', 'Technology Transfer Office', 
    'Environmental Solutions Provider', 
    'Digital Health Startup', 'Smart City Innovator'
]

technical_skills = [
    'AI', 'Machine Learning', 'Data Science', 
    'Blockchain', 'IoT', 'Cloud Computing', 
    'Biotechnology', 'Sustainable Design', 
    'Predictive Analytics', 'Robotics', 
    'Big Data', 'Deep Learning', 
    'Natural Language Processing', 
    'Computer Vision', 'Edge Computing'
]

industry_domains = [
    'Healthcare', 'Public Services', 
    'Circular Economy', 'Sustainability', 
    'Medical Technology', 'Environmental Innovation', 
    'Smart Cities', 'Digital Transformation', 
    'eHealth', 'Green Technology', 
    'Urban Planning', 'Social Innovation'
]

research_areas = [
    'Sustainable Healthcare', 'Urban Innovation', 
    'Waste Reduction', 'Circular Design', 
    'Health Technology', 'Smart Infrastructure', 
    'Resource Optimization', 'Digital Public Services',
    'Climate Adaptation', 'Social Entrepreneurship',
    'Precision Medicine', 'Renewable Energy'
]

service_offerings = [
    'Consulting', 'Research Collaboration', 
    'Technology Development', 'Innovation Workshops', 
    'Pilot Project Support', 'Strategic Advisory',
    'Prototype Development', 'Technology Licensing',
    'Training and Education', 'Impact Assessment'
]

technologies_used = [
    'Python', 'R', 'TensorFlow', 'Blockchain', 
    'Cloud AWS', 'Azure', 'IoT Platforms', 
    'Docker', 'Kubernetes', 'React', 
    'Node.js', 'GraphQL', 'Pytorch', 
    'Scikit-learn', 'Power BI'
]

# Function to generate realistic organization names
def generate_organization_name(org_type):
    prefixes = [
        'Smart', 'Innovative', 'Future', 'Green', 'Next', 
        'Digital', 'Sustainable', 'Urban', 'Global', 'Advanced'
    ]
    suffixes = [
        'Solutions', 'Innovations', 'Technologies', 'Systems', 
        'Lab', 'Collective', 'Institute', 'Network', 'Hub'
    ]
    
    type_specific_prefixes = {
        'Public Service': ['Civic', 'Public', 'Community', 'Urban'],
        'Healthcare': ['Health', 'Medical', 'Clinical', 'Wellness'],
        'Circular': ['Circular', 'Sustainable', 'Eco', 'Green'],
        'SME': ['Dynamic', 'Agile', 'Progressive', 'Innovative']
    }
    
    for key in type_specific_prefixes:
        if key in org_type:
            return f"{random.choice(type_specific_prefixes[key])} {random.choice(suffixes)}"
    
    return f"{random.choice(prefixes)} {random.choice(suffixes)}"

# Generate mock data
def generate_mock_data(num_organizations=150):
    data = []
    
    for _ in range(num_organizations):
        org_type = random.choice(organization_types)
        org_name = generate_organization_name(org_type)
        
        organization = [
            org_name,  # Organization Name
            org_type,  # Organization Type
            f"Innovative organization specializing in {random.choice(industry_domains)} with expertise in {random.choice(technical_skills)}",  # Description
            f"{random.choice(['Dr.', 'Mr.', 'Ms.'])} {random.choice(['Emma', 'Liam', 'Sophia', 'Noah', 'Olivia', 'Lucas', 'Ava', 'Mia', 'Ethan', 'Isabella'])} {random.choice(['Bakker', 'de Vries', 'Jansen', 'Visser', 'Peters', 'Mulder', 'Kooper', 'Smit'])}",  # Contact Person
            f"{org_name.lower().replace(' ', '.')}@brightlands.com",  # Contact Email
            f"+31 {random.randint(10,99)} {random.randint(100,999)} {random.randint(1000,9999)}",  # Contact Phone
            ', '.join(random.sample(technical_skills, random.randint(2,5))),  # Technical Skills
            ', '.join(random.sample(industry_domains, random.randint(1,3))),  # Industry Domains
            ', '.join(random.sample(research_areas, random.randint(1,3))),  # Research Areas
            ', '.join(random.sample(service_offerings, random.randint(2,4))),  # Service Offerings
            ', '.join(random.sample(technologies_used, random.randint(2,5))),  # Technologies Used
            ', '.join(random.sample(technical_skills + industry_domains, random.randint(3,6)))  # Keywords for Matching
        ]
        
        data.append(organization)
    
    return data

# Columns for the Excel file
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

# Generate and save mock data
df = pd.DataFrame(generate_mock_data(), columns=columns)

# Save to Excel
df.to_excel('Brightlands_Stakeholder_Mapping.xlsx', index=False)

print("Mock data Excel file created successfully!")
print(f"\nTotal Organizations Generated: {len(df)}")
print("\nSample of Generated Organizations:")
print(df.head())
