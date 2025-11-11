import pickle 
import streamlit as st
import requests
import numpy as np

API_KEY = "200f55a73b5f4a2e262e576c28c671e4"

def load_similarity():
    with open('artificats/similarity_part1.pkl', 'rb') as f:
        part1 = pickle.load(f)
    with open('artificats/similarity_part2.pkl', 'rb') as f:
        part2 = pickle.load(f)
    return np.vstack((part1, part2))

similarity_data = load_similarity()

# Usage
similarity_data = load_similarity()

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    data = requests.get(url)
    data = data.json()
    
    if 'poster_path' in data and data['poster_path']:
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path  # w1995 -> w500 karo
        return full_path
    else:
        return None  

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies_name = []
    recommended_movies_poster = []
    
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]]['movie_id'] 
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies_name.append(movies.iloc[i[0]].title)
    
    return recommended_movies_name, recommended_movies_poster

st.header("Movies Recommendation System using Machine Learning")

movies = pickle.load(open('artificats/movie_list.pkl', 'rb'))
similarity = similarity_data

movie_list = movies['title'].values
selected_movie = st.selectbox(
    'Type or select a movie to get recommendation', movie_list
)

if st.button('show recommendation'):
    recommended_movies_name, recommended_movies_poster = recommend(selected_movie)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.text(recommended_movies_name[0])
        st.image(recommended_movies_poster[0] if recommended_movies_poster[0] else "default_poster.jpg")

    with col2:
        st.text(recommended_movies_name[1])
        st.image(recommended_movies_poster[1] if recommended_movies_poster[1] else "default_poster.jpg")

    with col3:
        st.text(recommended_movies_name[2])
        st.image(recommended_movies_poster[2] if recommended_movies_poster[2] else "default_poster.jpg")

    with col4:
        st.text(recommended_movies_name[3])
        st.image(recommended_movies_poster[3] if recommended_movies_poster[3] else "default_poster.jpg")

    with col5:
        st.text(recommended_movies_name[4])
        st.image(recommended_movies_poster[4] if recommended_movies_poster[4] else "default_poster.jpg")

        

st.markdown("""
<div style="text-align:center;margin-bottom:8px;">
    <span style="
        font-size:23px;
        font-weight:700;
        font-family: 'Segoe UI', 'Roboto', 'Arial', sans-serif;
        color: #fff;
        letter-spacing:1.2px;
        padding-bottom:2px;">
        Made by Salim
    </span>
</div>
<div style="display:flex;justify-content:center;">
    <a href="https://github.com/SalimXcode" target="_blank" style="
        text-decoration:none;
        ">
        <span style="
            font-family: 'Segoe UI', 'Roboto Mono', monospace;
            font-size:1.09rem;
            font-weight:700;
            color:#fff;
            background:#202231;
            border-left:4px solid #05d8fe;
            border-radius:7px;
            padding:6px 24px;
            margin-top:5px;
            box-shadow:0 1px 10px rgba(5,216,254,0.09);
            transition: box-shadow 0.3s;
            display:inline-block;
        ">
            <span style="color:#05d8fe;">&#128187; </span>
            GitHub : SalimXcode
        </span>
    </a>
</div>
""", unsafe_allow_html=True)
