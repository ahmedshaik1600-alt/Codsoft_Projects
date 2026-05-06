# Recommendation System

A simple content-based recommendation system built with Python and Streamlit.

The app suggests movies, books, or products based on the user's selected preferences. It uses a small local CSV dataset and a cosine-similarity matching algorithm. The UI uses a black and red glassmorphic style.

## Features

- Recommend movies, books, and products
- Select preferences from the UI
- Filter recommendations by category
- Local CSV dataset
- Simple content-based recommendation logic
- Black and red glassmorphic Streamlit interface
- No API keys required

## Tech Stack

- Python
- Streamlit
- CSV data
- Content-based filtering
- Cosine similarity

## Folder Structure

```text
recommendation_system_project/
|-- app.py
|-- recommender.py
|-- requirements.txt
|-- README.md
|-- .gitignore
`-- data/
    `-- items.csv
```

## Installation

1. Clone or download this project.

2. Open the project folder:

```powershell
cd recommendation_system_project
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

4. Run the app:

```powershell
streamlit run app.py
```

## How It Works

1. The user selects a category and preferences.
2. The app reads items from `data/items.csv`.
3. User preferences and item details are converted into word vectors.
4. Cosine similarity is used to rank the closest matches.
5. The best matching items are displayed as recommendations.

## Dataset

The dataset is stored locally in:

```text
data/items.csv
```

You can add more items by editing the CSV file and keeping the same columns:

```text
id,title,category,tags,description
```

## Output

The app displays recommended items with:

- Title
- Category
- Tags
- Description

## License

This project is free to use for learning and academic purposes.
