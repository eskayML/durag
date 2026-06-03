<p align="center">
  <img src="https://raw.githubusercontent.com/eskayML/durag/main/assets/durag-banner.jpg" alt="Du-RAG" width="600">
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

- Persistent memory across conversations — agents remember what they learn
- Semantic search via vector embeddings — find the right context fast
- Multiple backends — OpenAI, Anthropic, Gemini, DeepSeek, Ollama, vLLM, and more
- Vector stores — FAISS (default), Qdrant, Chroma, Pinecone, Weaviate, and others

## License

Apache 2.0
