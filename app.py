import streamlit as st
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class StakeholderMatchmaker:
    def __init__(self, excel_path):
        # Load stakeholder data
        self.df = pd.read_excel(excel_path)
        
        # Prepare text for matching
        self.df['matching_text'] = (
            self.df['Organization Name'] + ' ' + 
            self.df['Organization Description'] + ' ' + 
            self.df['Technical Skills'] + ' ' + 
            self.df['Industry Domains'] + ' ' + 
            self.df['Research Areas'] + ' ' + 
            self.df['Service Offerings'] + ' ' + 
            self.df['Keywords for Matching']
        )
        
        # Create TF-IDF vectorizer
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df['matching_text'])
    
    def find_matches(self, query, top_n=3):
        # Vectorize the query
        query_vector = self.vectorizer.transform([query])
        
        # Calculate cosine similarity
        cosine_similarities = cosine_similarity(query_vector, self.tfidf_matrix)[0]
        
        # Get top matches
        top_indices = cosine_similarities.argsort()[-top_n:][::-1]
        
        # Prepare match results
        matches = []
        for idx in top_indices:
            match = self.df.iloc[idx]
            matches.append({
                'organization': match['Organization Name'],
                'type': match['Organization Type'],
                'description': match['Organization Description'],
                'contact_person': match['Contact Person'],
                'contact_email': match['Contact Email'],
                'technical_skills': match['Technical Skills'],
                'service_offerings': match['Service Offerings'],
                'similarity_score': cosine_similarities[idx]
            })
        
        return matches

def main():
    # Set page configuration
    st.set_page_config(
        page_title="Brightlands Stakeholder Matchmaker",
        page_icon="🤝",
        layout="wide"
    )

    # Title and introduction
    st.title("🤝 Brightlands Stakeholder Matchmaker")
    st.markdown("""
    ### Connecting Innovators in Our Ecosystem
    Enter your expertise, service request, or area of interest to find the most relevant stakeholders.
    """)

    # Initialize matchmaker
    try:
        matchmaker = StakeholderMatchmaker('Brightlands_Stakeholder_Mapping.xlsx')
    except FileNotFoundError:
        st.error("Excel file not found. Please ensure 'Brightlands_Stakeholder_Mapping.xlsx' is in the same directory.")
        return

    # Search input
    query = st.text_input("What expertise or service are you looking for?", 
                           placeholder="E.g., AI in healthcare, data science consulting")

    # Match button
    if st.button("Find Matches") or query:
        if query:
            # Find matches
            matches = matchmaker.find_matches(query)
            
            # Display results
            st.subheader(f"🔍 Matching Results for '{query}'")
            
            for i, match in enumerate(matches, 1):
                # Create an expandable section for each match
                with st.expander(f"{i}. {match['organization']} (Relevance: {match['similarity_score']:.2%})"):
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown(f"**Organization Type:** {match['type']}")
                        st.markdown(f"**Description:** {match['description']}")
                        st.markdown(f"**Technical Skills:** {match['technical_skills']}")
                    
                    with col2:
                        st.markdown(f"**Contact Person:** {match['contact_person']}")
                        st.markdown(f"**Contact Email:** {match['contact_email']}")
                        st.markdown(f"**Service Offerings:** {match['service_offerings']}")
                    
                    # Optional: Add a contact button
                    st.button(f"Request Connection with {match['organization']}", key=f"contact_{i}")

    # Sidebar for additional information
    st.sidebar.header("About Brightlands Matchmaker")
    st.sidebar.info("""
    This tool helps connect stakeholders in the Brightlands Smart Services Campus ecosystem.
    
    🔍 How to use:
    - Enter keywords about your expertise or needs
    - Get matched with relevant organizations
    - Explore potential collaborations
    """)

if __name__ == "__main__":
    main()
