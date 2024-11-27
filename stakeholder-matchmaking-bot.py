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
                'description': match['Organization Description'],
                'contact_person': match['Contact Person'],
                'contact_email': match['Contact Email'],
                'similarity_score': cosine_similarities[idx]
            })
        
        return matches
    
    def interactive_match(self):
        while True:
            query = input("Enter your expertise or service request (or 'quit' to exit): ")
            if query.lower() == 'quit':
                break
            
            matches = self.find_matches(query)
            
            print("\nTop Matches:")
            for i, match in enumerate(matches, 1):
                print(f"\nMatch {i}:")
                print(f"Organization: {match['organization']}")
                print(f"Description: {match['description']}")
                print(f"Contact Person: {match['contact_person']}")
                print(f"Contact Email: {match['contact_email']}")
                print(f"Relevance Score: {match['similarity_score']:.2%}")

# Example usage
def main():
    matchmaker = StakeholderMatchmaker('Brightlands_Stakeholder_Mapping.xlsx')
    matchmaker.interactive_match()

if __name__ == "__main__":
    main()
