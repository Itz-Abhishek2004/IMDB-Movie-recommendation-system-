import streamlit as st
from recommender import recommend_movies

st.set_page_config(page_title="Movie Recommendation System", page_icon="🎬")

st.title("🎬 IMDB Movie Recommendation System Using Storylines")
st.write("Enter a movie storyline and get top 5 similar movie recommendations.")

user_input = st.text_area("Enter storyline here:")

if st.button("Get Recommendations"):
    if user_input.strip():
        results = recommend_movies(user_input)

        st.subheader("Top 5 Recommended Movies")
        for i, row in results.iterrows():
            st.markdown(f"### {i+1}. {row['Movie Name']}")
            st.write(row['Storyline'])
            st.write(f"**Similarity Score:** {row['Similarity Score']:.4f}")
            st.write("---")
    else:
        st.warning("Please enter a storyline.")