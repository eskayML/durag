<p align="center">
  <img src="https://raw.githubusercontent.com/eskayML/durag/main/assets/durag-banner.jpg" alt="Du-RAG" width="600">
</p>

<h1 align="center">Du-RAG</h1>
<p align="center"><b>Durable RAG</b> - a persistent memory layer for AI agents built on retrieval-augmented generation.</p>

<p align="center">
  <a href="https://github.com/eskayML/durag/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/eskayML/durag?color=blue" alt="License">
  </a>
  <a href="https://github.com/eskayML/durag/stargazers">
    <img src="https://img.shields.io/github/stars/eskayML/durag?style=flat" alt="Stars">
  </a>
  <a href="https://durag.readthedocs.io">
    <img src="https://img.shields.io/readthedocs/durag?label=docs" alt="Docs">
  </a>
</p>

---

```bash
pip install durag
```

```python
from durag import Memory

m = Memory()

m.add("Alice loves Python and open source", user_id="alice")
m.add("Alice built Du-RAG", user_id="alice")

history = m.get_all(filters={"user_id": "alice"})
print(history)
```

## Why Du-RAG?

Du-RAG is the **fastest** memory library for AI agents. Unlike other libraries that block for 1-2 seconds calling an LLM on every write, Du-RAG stores memories instantly and lets you consolidate in the background.

<p align="center">
  <img src="https://raw.githubusercontent.com/eskayML/durag/main/assets/latency-comparison.png" alt="Latency Comparison" width="640">
</p>

```python
# Fast path - returns in ~50ms, no LLM call
m.add("Alice switched to Enterprise plan", user_id="alice")

# Search works immediately on raw text
results = m.search("What plan is Alice on?", user_id="alice")

# Consolidate later - batch-extract facts with one LLM call
m.consolidate(user_id="alice")
```

## API Keys

Du-RAG requires a provider API key. Set the env var for your preferred provider before first use:

| Provider | Env Var | Used For |
|----------|---------|----------|
| OpenAI (default) | `OPENAI_API_KEY` | Embeddings + LLM |
| Anthropic | `ANTHROPIC_API_KEY` | LLM |
| Google Gemini | `GOOGLE_API_KEY` | Embeddings + LLM |
| DeepSeek | `DEEPSEEK_API_KEY` | LLM |
| Together AI | `TOGETHER_API_KEY` | Embeddings + LLM |
| Groq | `GROQ_API_KEY` | LLM |
| MiniMax | `MINIMAX_API_KEY` | LLM |
| Sarvam AI | `SARVAM_API_KEY` | LLM |
| vLLM | `VLLM_API_KEY` | LLM |

```bash
export OPENAI_API_KEY="sk-..."
```

## Features

- **Fast writes** - add() returns in ~50ms (no blocking LLM call)
- **Async consolidation** - batch-extract facts with consolidate() when idle
- Persistent memory across conversations - agents remember what they learn
- Semantic search via vector embeddings - find the right context fast
- Multiple backends - OpenAI, Anthropic, Gemini, DeepSeek, Ollama, vLLM, and more
- Vector stores - Qdrant (default), FAISS, Chroma, Pinecone, Weaviate, and others

## License

Apache 2.0
