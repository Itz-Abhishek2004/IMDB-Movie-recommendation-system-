# IMDB Movie Recommendation System Using Storylines

A simple content-based movie recommendation system that suggests similar movies based on storyline text using TF-IDF and cosine similarity. The project includes a Streamlit app where users can enter a storyline and get the top 5 recommended movies.

## Tech Stack
- Python
- Pandas
- Scikit-learn
- Streamlit

## Project Files
- `app.py` - Streamlit user interface
- `recommender.py` - Recommendation logic using TF-IDF and cosine similarity
- `movies_data.csv` - Movie titles and storylines dataset
- `requirements.txt` - Required Python libraries

## How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## How It Works
1. Load movie data from CSV
2. Clean storyline text
3. Convert text into TF-IDF vectors
4. Compare similarity using cosine similarity
5. Show top 5 matching movies

## Sample Input
A young hero joins warriors to fight a powerful empire and discover his destiny.

## Output
Top 5 movies with similar storylines and similarity scores.

## Note
This project is built as a stable prototype using a structured CSV dataset of movie names and storylines.

