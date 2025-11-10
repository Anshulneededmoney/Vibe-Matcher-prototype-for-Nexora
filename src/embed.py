import os
import pandas as pd
from tqdm import tqdm
from dotenv import load_dotenv

# 🔸 temporary local model
from sentence_transformers import SentenceTransformer
model_local = SentenceTransformer("all-MiniLM-L6-v2")

# keep these even if unused (so you can switch back easily)
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def embed_texts(texts, model="text-embedding-3-small", use_local=True):
    """Batch-embed a list of strings and return list of vectors."""
    embeddings = []
    for desc in tqdm(texts, desc="Embedding descriptions"):
        if use_local:
            vec = model_local.encode(desc)
            embeddings.append(vec.tolist())
        else:
            resp = client.embeddings.create(model=model, input=desc)
            embeddings.append(resp.data[0].embedding)
    return embeddings

def embed_csv(csv_path="data/mock_fashion.csv", model="text-embedding-3-small", save_path=None, use_local=True):
    """Load a CSV, embed 'desc', and optionally save as pickle."""
    df = pd.read_csv(csv_path)
    df["embedding"] = embed_texts(df["desc"].tolist(), model=model, use_local=use_local)
    if save_path:
        df.to_pickle(save_path)
    return df
