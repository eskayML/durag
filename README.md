<p align="center">
  <img src="assets/durag-banner.jpg" alt="Du-RAG" width="600">
</p>

<h1 align="center">Du-RAG</h1>
<p align="center"><b>Durable RAG</b> — a persistent memory layer for AI agents built on retrieval-augmented generation.</p>

<p align="center">
  <a href="https://github.com/eskayML/durag/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/eskayML/durag?color=blue" alt="License">
  </a>
  <a href="https://github.com/eskayML/durag/stargazers">
    <img src="https://img.shields.io/github/stars/eskayML/durag?style=flat" alt="Stars">
  </a>
  <a href="https://github.com/eskayML/durag/commits/main">
    <img src="https://img.shields.io/github/last-commit/eskayML/durag?color=blueviolet" alt="Last Commit">
  </a>
  <a href="https://github.com/eskayML/durag">
    <img src="https://img.shields.io/github/repo-size/eskayML/durag?color=orange" alt="Repo Size">
  </a>
  <a href="https://pypi.org/project/durag/">
    <img src="https://img.shields.io/pypi/pyversions/durag?color=green" alt="Python Versions">
  </a>
</p>

---

```bash
pip install durag
```

```python
from durag import Memory

m = Memory()
m.add("User likes Python", user_id="alice")
results = m.search("What does Alice prefer?", user_id="alice")
```

## Features

- Persistent memory across conversations
- Semantic search via vector embeddings
- Supports Qdrant, Chroma, Pinecone, Weaviate and more
- Fully self-hosted, no cloud dependencies

## License

Apache 2.0
