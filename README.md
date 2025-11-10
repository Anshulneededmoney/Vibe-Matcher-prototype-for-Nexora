# Vibe Matcher

A lightweight vibe-based recommendation prototype built for the Nexora internship task.  
It takes a natural language vibe query (e.g. “energetic urban chic”), embeds both the query and product descriptions into vector space, and returns the top-3 most similar products by cosine similarity.

---

## Overview
- Small fashion catalog (8 products) with names, descriptions, and vibe tags  
- Embeddings generated using `sentence-transformers` (`all-MiniLM-L6-v2`), or OpenAI `text-embedding-3-small` if API key available  
- Cosine similarity used to match vibe queries to products  
- Evaluates three example queries and reports hit-rate and latency

---

## Repository Structure

<pre>
vibe-matcher/
├── data/
│   ├── mock_fashion.csv
│   └── fashion_with_embeddings.pkl
├── src/
│   ├── embed.py
│   ├── search.py
├── notebooks/
│   └── runner.ipynb
├── requirements.txt
└── README.md
</pre>

---

## Setup

```bash
git clone https://github.com/<your-username>/vibe-matcher.git
cd vibe-matcher
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
pip install -r requirements.txt
```

Running the Notebook

Open notebooks/runner.ipynb in VS Code or Jupyter

Run cells from top to bottom

Results include product embeddings, top-3 matches per query, evaluation table, and latency plot

Example Queries
Query	Top Match
energetic urban chic	Streetwear Hoodie
warm cozy minimal	Cozy Knit Sweater
traditional festive elegance	Elegant Silk Saree
Improvements

Combine description and tags for richer embeddings

Use FAISS or Pinecone for scalable search

Add query rewriting and hybrid ranking

Cache embeddings to reduce compute time
