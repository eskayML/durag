"""Du-RAG works!
Install: pip install durag faiss-cpu sentence-transformers
Run with: OPENAI_API_KEY=sk-your-key python3 demo.py
(Or set up Ollama for a fully local experience)"""
import os, shutil, warnings

os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY", "sk-demo")
warnings.filterwarnings("ignore")

from durag import Memory

m = Memory.from_config({
    "llm": {"provider": "openai", "config": {"model": "gpt-4o-mini"}},
    "embedder": {"provider": "huggingface",
        "config": {"model": "sentence-transformers/all-MiniLM-L6-v2", "embedding_dims": 384}},
    "vector_store": {"provider": "faiss",
        "config": {"path": "/tmp/durag_demo", "embedding_model_dims": 384}},
})

print("✅ Du-RAG initialized\n")

m.add("Alice is a software engineer who loves Python", user_id="alice")
print("✅ Stored: Alice is a software engineer who loves Python")

m.add("Alice built Du-RAG from scratch", user_id="alice")
print("✅ Stored: Alice built Du-RAG from scratch")

history = m.get_all(filters={"user_id": "alice"})
print(f"\n📦 Memories for Alice: {len(history.get('results', []))}")
for entry in history.get("results", []):
    print(f"   • {entry.get('memory', entry)}")

shutil.rmtree("/tmp/durag_demo", ignore_errors=True)
print("\n🎉 Du-RAG works!")
