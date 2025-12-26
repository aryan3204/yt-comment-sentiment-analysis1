import os
import pandas as pd
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("YT_API_KEY")


def get_youtube_client():
    """Create an authenticated YouTube API client."""
    if API_KEY is None:
        raise ValueError("YT_API_KEY not set in .env")
    return build("youtube", "v3", developerKey=API_KEY)


def fetch_comments(video_id: str, max_results: int = 100) -> pd.DataFrame:
    """
    Fetch top-level comments for a YouTube video.

    Parameters
    ----------
    video_id : str
        ID of the YouTube video.
    max_results : int
        Maximum number of comments to fetch.

    Returns
    -------
    pd.DataFrame
        DataFrame with a single column: 'comment_text'.
    """
    youtube = get_youtube_client()
    comments = []

    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=min(max_results, 100),
        textFormat="plainText",
        order="relevance",
    )

    while request and len(comments) < max_results:
        response = request.execute()
        for item in response.get("items", []):
            snippet = item["snippet"]["topLevelComment"]["snippet"]
            comments.append(snippet["textDisplay"])

        request = youtube.commentThreads().list_next(request, response)

    return pd.DataFrame({"comment_text": comments})
