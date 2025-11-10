
from __future__ import annotations
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import normalize

def build_index(df: pd.DataFrame, embed_col: str = "embedding"):
    """Return (matrix, meta_df) where matrix shape = [N, D]."""
    if embed_col not in df.columns:
        raise ValueError(f"DataFrame missing '{embed_col}' column.")
    mat = np.vstack(df[embed_col].values).astype(np.float32)
    meta = df[["name", "desc", "vibes"]].copy()
    return mat, meta



def rank_by_cosine(query_vec, matrix, meta, top_k=3):
    q = np.asarray(query_vec, dtype=np.float32).reshape(1, -1)
    q = normalize(q)
    m = normalize(matrix)
    sims = (q @ m.T)[0]
    out = meta.copy()
    out["score"] = sims
    return out.sort_values("score", ascending=False).head(top_k).reset_index(drop=True)


def fallback_if_weak(results: pd.DataFrame, min_sim: float = 0.30) -> pd.DataFrame:
    """
    If best match is below threshold, we still return top-3 but annotate.
    Caller can show a gentle message like 'No strong match; here are closest'.
    """
    results = results.copy()
    results["weak_match"] = results["score"].max() < min_sim
    return results
