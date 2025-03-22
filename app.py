import streamlit as st
import pandas as pd
import pickle

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    dist = sim[movie_index]
    movie_list = sorted(list(enumerate(dist)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie = []
    for i in movie_list:
        recommended_movie.append(movies.iloc[i[0]].title)
    return recommended_movie

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

sim = pickle.load(open('sim.pkl', 'rb'))

st.title("Movies Recommender System")

selected_movie_name = st.selectbox("Select a movie", movies['title'].values)

if st.button('Recommend'):
    names = recommend(selected_movie_name)
    
    st.write("Recommended Movies:")
    st.write(names) 


