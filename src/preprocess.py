import re
import pandas as pd


URL_PATTERN = re.compile(r"http\S+|www\.\S+")
EMOJI_PATTERN = re.compile(
    "["
    "\U0001F600-\U0001F64F"
    "\U0001F300-\U0001F5FF"
    "\U0001F680-\U0001F6FF"
    "\U0001F1E0-\U0001F1FF"
    "]+",
    flags=re.UNICODE,
)


def clean_text(text: str) -> str:
    """Basic text cleaning: lowercasing, remove URLs, emojis, and extra spaces."""
    text = text.lower()
    text = URL_PATTERN.sub("", text)
    text = EMOJI_PATTERN.sub("", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def add_clean_column(df: pd.DataFrame, text_col: str = "comment_text") -> pd.DataFrame:
    """Return a copy of df with an extra 'clean_text' column."""
    df = df.copy()
    df["clean_text"] = df[text_col].astype(str).apply(clean_text)
    return df
