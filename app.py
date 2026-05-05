import streamlit as st
import pickle
import requests
import pandas as pd

st.set_page_config(layout="wide")

def fetch_poster(movie_id):
    api_key = '6b95799a3d3dfcc8a9dd2a05b0f7a3f2'
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
    
    try:
        data = requests.get(url)
        data.raise_for_status()
        data = data.json()
        poster_path = data.get('poster_path')
        if poster_path:
            full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
            return full_path
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching poster: {e}")
    return "https://placehold.co/500x750/333/FFFFFF?text=No+Poster"

def recommend(movie):
    """Recommends 5 similar movies based on the selected movie."""
    try:
        index = movies[movies['title'] == movie].index[0]
    except IndexError:
        st.error("Movie not found in the dataset. Please select another one.")
        return [], [], [], []
        
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_movie_ratings = []
    recommended_movie_reviews=[]

    for i in distances[1:6]:
        # fetch the movie details
        movie_id = movies.iloc[i[0]].movie_id
        
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_ratings.append(movies.iloc[i[0]].vote_average)
        recommended_movie_reviews.append(movies.iloc[i[0]].vote_count)

    return recommended_movie_names, recommended_movie_posters, recommended_movie_ratings,recommended_movie_reviews


st.set_page_config(layout="wide")
st.header('Movie Recommender System Using Machine Learning')

# Load the data files
try:
    movies_dict = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
    similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))
except FileNotFoundError:
    st.error("Model files not found. Please run the data processing notebook first.")
    st.stop()


movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    with st.spinner('Finding recommendations...'):
        recommended_movie_names, recommended_movie_posters, recommended_movie_ratings,recommended_movie_reviews = recommend(selected_movie)
    
    if recommended_movie_names:
        cols = st.columns(5)
        for i, col in enumerate(cols):
            with col:
                st.text(recommended_movie_names[i])
                st.image(recommended_movie_posters[i])
                
                rating = recommended_movie_ratings[i]
                st.caption(f"Rating: {rating:.1f} ⭐")

                reviews = recommended_movie_reviews[i]
                st.caption(f"💬 Reviews: {reviews:.1f} ")