# yt-comment-sentiment-analysis1

Python project to fetch YouTube comments and run Hugging Face sentiment analysis.

## Features

- Fetches comments from YouTube Data API v3 for a given video ID.
- Cleans and preprocesses comment text (lowercasing, URL/emoji removal).
- Uses a Hugging Face `sentiment-analysis` pipeline to label each comment.
- Saves results as a CSV with sentiment labels and scores.

## Tech Stack

- Python, pandas
- YouTube Data API v3
- Hugging Face `transformers`
- Jupyter Notebook (optional, for exploration)

## Getting Started

1. Clone this repository and create a virtual environment.
2. Install dependencies:
3. Create a `.env` file in the project root:
4. Run the sentiment analyzer:
This will create `data/results.csv` with comments and sentiment scores.

## Project Structure

- `src/fetch_comments.py` – Fetch comments via YouTube Data API.
- `src/preprocess.py` – Text cleaning utilities.
- `src/sentiment_analyzer.py` – Pipeline to clean text, run sentiment model, and save CSV.
- `requirements.txt` – Python dependencies.

## Future Work

- Add visualizations for sentiment distribution.
- Support multiple videos or channels.
- Experiment with different transformer models and fine-tuning.

## Example run – Imran Khan on Unfiltered by Samdish

This project was tested on comments from the YouTube episode **“The Film Critic No One Asked For ft. Imran Khan”**. The script fetched comments using the YouTube Data API, cleaned the text, ran a transformer-based sentiment model, and saved outputs to `data/results_imran_unfiltered.csv`. [file:148]

Out of 30 analysed comments, 22 were labelled POSITIVE and 8 NEGATIVE, indicating that audience sentiment towards the interview is strongly positive. The model’s average confidence was about 0.97 for POSITIVE and 0.99 for NEGATIVE predictions. [file:148][file:204]

![Sentiment distribution for Imran Khan interview](figures/imranscreenshot.png)


