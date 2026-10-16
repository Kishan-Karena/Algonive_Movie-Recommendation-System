# 🎬 Algonive Movie Recommendation System

A Machine Learning-based movie recommendation system that suggests similar movies based on content analysis. The project leverages a dataset of 5,000 movies to provide personalized suggestions with a clean, interactive web interface.

## 🚀 Features
- **Content-Based Filtering**: Recommends movies based on similarity in genres, keywords, cast, and crew.
- **Interactive UI**: Built with Streamlit for a seamless user experience.
- **Real-time Data**: Integrates with the **TMDB API** to fetch and display movie posters.
- **Quick Analysis**: Displays ratings and review counts for recommended movies.

## 🛠️ Tech Stack
- **Language**: Python 3.x
- **Web Framework**: [Streamlit](https://streamlit.io/)
- **Data Manipulation**: [Pandas](https://pandas.pydata.org/)
- **ML Serialization**: [Pickle](https://docs.python.org/3/library/pickle.html)
- **API Integration**: [Requests](https://requests.readthedocs.io/)
- **Dataset**: TMDB 5000 Movies & Credits Dataset

## 📂 Project Structure
```text
.
├── artifacts/
│   ├── movie_list.pkl      # Serialized dataframe of movies
│   └── similarity.pkl      # Pre-computed cosine similarity matrix
├── tmdb_5000_movies.csv    # Raw movie metadata
├── tmdb_5000_credits.csv    # Raw movie credits
├── Movie Recommendation.ipynb # Data processing and model training
├── app.py                  # Streamlit application
└── README.md               # Project documentation
```

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/Algonive_Movie-Recommendation-System.git
cd Algonive_Movie-Recommendation-System
```

### 2. Install Dependencies
It is recommended to use a virtual environment:
```bash
# Create a virtual environment
python -m venv venv
# Activate it (Windows)
.\venv\Scripts\activate
# Activate it (Mac/Linux)
source venv/bin/activate

# Install required packages
pip install streamlit pandas requests
```

### 3. TMDB API Key (Optional for Posters)
To display movie posters, you need a TMDB API key:
1. Sign up at [The Movie Database (TMDB)](https://www.themoviedb.org/).
2. Generate an API key from your account settings.
3. Open `app.py` and add your key to the `api_key` variable in the `fetch_poster` function:
   ```python
   def fetch_poster(movie_id):
       api_key = 'YOUR_TMDB_API_KEY_HERE'
       # ... rest of the code
   ```

## 🖥️ Usage
Run the application using the following command:
```bash
streamlit run app.py
```
Once the app starts, select a movie from the dropdown menu and click **"Show Recommendation"** to see the top 5 most similar movies.

## 🧠 How It Works
The system uses **Content-Based Filtering**. 
1. **Preprocessing**: Movie tags are created by combining genres, keywords, cast, and crew.
2. **Vectorization**: These tags are converted into vectors using `CountVectorizer` (handled in the `.ipynb` file).
3. **Similarity**: The **Cosine Similarity** between vectors is calculated to determine how similar two movies are.
4. **Recommendation**: When a user selects a movie, the system looks up its vector and finds the five closest vectors in the similarity matrix.

---
Developed by Kishan-Karena
