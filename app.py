import pickle
import streamlit as st
import numpy as np

st.header("Book Recommendation System Using Machine Learning")

# Load the models and datasets
model = pickle.load(open('artifacts/model.pkl', 'rb'))
book_names = pickle.load(open('artifacts/book_names.pkl', 'rb'))
final_rating = pickle.load(open('artifacts/final_rating.pkl', 'rb'))
book_pivot = pickle.load(open('artifacts/book_pivot.pkl', 'rb'))


def fecth_poster(suggestion):
    book_name = []
    ids_index = []
    poster_url = []

    # Get book names from the suggestions
    for book_id in suggestion[0]:
        book_name.append(book_pivot.index[book_id])

    # Find corresponding indices in `final_rating`
    for name in book_name:
        try:
            ids = np.where(final_rating['title'] == name)[0][0]
            ids_index.append(ids)
        except IndexError:
            st.warning(f"Poster not found for book: {name}")
            poster_url.append("https://via.placeholder.com/150")  # Placeholder image

    # Fetch poster URLs
    for idx in ids_index:
        try:
            url = final_rating.iloc[idx]['image_url']
            poster_url.append(url)
        except IndexError:
            poster_url.append("https://via.placeholder.com/150")  # Placeholder image

    return poster_url


def recommend_books(book_name):
    book_list = []
    poster_url = []
    
    # Get the book index from book_pivot
    try:
        book_id = np.where(book_pivot.index == book_name)[0][0]
    except IndexError:
        st.error("The selected book is not in the recommendation system!")
        return [], []
    
    # Find similar books using the model
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6)

    # Fetch poster URLs for the recommendations
    poster_url = fecth_poster(suggestion)

    for i in range(len(suggestion[0])):
        books = book_pivot.index[suggestion[0][i]]
        book_list.append(books)

    return book_list, poster_url


# Streamlit app logic
selected_books = st.selectbox(
    "Type or select a book",
    book_pivot.index  # Use book titles directly from the pivot table
)

if st.button('Show Recommendation'):
    recommendation_book, poster_url = recommend_books(selected_books)
    if recommendation_book:
        cols = st.columns(len(recommendation_book))
        for i, col in enumerate(cols):
            with col:
                st.text(recommendation_book[i])
                st.image(poster_url[i])