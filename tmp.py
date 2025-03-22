# Description: This file contains the code for the Streamlit web app.
#  if you want to see the poster as well. You can use the following code snippet in app.py:

import streamlit as st
import pandas as pd
import requests
import pickle

# def fetch_poster(movies_id):
#     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movies_id))
#     data = response.json()
import requests

def fetch_poster(movies_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movies_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
        response = requests.get(url, timeout=5)  # Timeout set to 5 seconds
        response.raise_for_status()  # Raise error for failed requests
        data = response.json()

        return 'https://image.tmdb.org/t/p/w500/' + data.get('poster_path', '')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster for movie ID {movies_id}: {e}")
        return "https://via.placeholder.com/500x750.png?text=No+Image"  # Placeholder image






## https://api.themoviedb.org/3/movie/65?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US
    return  'https://image.tmdb.org/t/p/w500/' + data['poster_path']



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    dist = sim[movie_index]
    movie_list = sorted(list(enumerate(dist)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie =[]
    recommended_movie_posters = []
    for i in movie_list:
        movies_id = (movies.iloc[i[0]].movie_id)

        recommended_movie.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movies_id))
    return recommended_movie,recommended_movie_posters


movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

sim = pickle.load(open('sim.pkl','rb'))

st.title("Movies Recommender system")

selected_movie_name  = st.selectbox(
    "hello",
    (movies['title'].values))
if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)


    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])


