import argparse
from pathlib import Path

import pandas as pd
from transformers import pipeline

from fetch_comments import fetch_comments
from preprocess import add_clean_column


def load_sentiment_pipeline():
    """Load the default Hugging Face sentiment-analysis pipeline."""
    return pipeline("sentiment-analysis")


def analyze_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Run sentiment analysis on the 'clean_text' column."""
    clf = load_sentiment_pipeline()

    results = clf(df["clean_text"].tolist())
    labels = [r["label"] for r in results]
    scores = [r["score"] for r in results]

    df = df.copy()
    df["sentiment_label"] = labels
    df["sentiment_score"] = scores
    return df


def main():
    parser = argparse.ArgumentParser(
        description="Fetch YouTube comments and run sentiment analysis."
    )
    parser.add_argument("--video_id", required=True, help="YouTube video ID to analyze.")
    parser.add_argument(
        "--max_comments",
        type=int,
        default=100,
        help="Maximum number of comments to fetch.",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="data/results.csv",
        help="Path to output CSV file.",
    )

    args = parser.parse_args()

    print(f"Fetching comments for video: {args.video_id}")
    df = fetch_comments(args.video_id, max_results=args.max_comments)
    df = add_clean_column(df)

    print("Running sentiment analysis with Hugging Face pipeline...")
    df = analyze_dataframe(df)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

    print(f"Saved results to: {output_path.resolve()}")


if __name__ == "__main__":
    main()
