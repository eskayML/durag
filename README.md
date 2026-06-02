<p align="center">
  <img src="assets/durag-banner.jpg" alt="Du-RAG" width="600">
</p>

<h1 align="center">Du-RAG</h1>
<p align="center"><b>Durable RAG</b> — a persistent memory layer for AI agents built on retrieval-augmented generation.</p>

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
