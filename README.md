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
  <a href="https://github.com/eskayML/durag">
    <img src="https://img.shields.io/github/repo-size/eskayML/durag?color=orange" alt="Repo Size">
  </a>
</p>

---

```bash
pip install durag[local]
```

```python
from durag import Memory

m = Memory()

m.add("Alice loves Python and open source", user_id="alice")
m.add("Alice built Du-RAG", user_id="alice")

history = m.get_all(filters={"user_id": "alice"})
print(history)
```

No API keys. No cloud. Runs entirely on your machine.

## Features

- Persistent memory across conversations — agents remember what they learn
- Semantic search via vector embeddings — find the right context fast
- Fully local — HuggingFace embeddings + FAISS by default, no data leaves your machine
- Multiple backends — swap in OpenAI, Qdrant, Chroma, Pinecone, Weaviate when you need them

## License

Apache 2.0
