"""
Global test configuration.
Handles optional dependencies gracefully so tests for unavailable backends
are skipped instead of failing collection.
"""

import importlib
from pathlib import Path

import pytest

# Map test files to their required optional dependencies
_OPTIONAL_DEPS: dict[str, list[str]] = {
    # LLM backends
    "test_gemini.py": ["google.genai"],
    "test_groq.py": ["groq"],
    "test_together.py": ["together"],
    "test_litellm.py": ["litellm"],
    "test_azure_openai.py": ["openai._azure"],
    "test_azure_openai_structured.py": ["openai._azure"],
    # Embedding backends
    "test_azure_openai_embeddings.py": ["openai._azure"],
    "test_gemini_emeddings.py": ["google.genai"],
    "test_vertexai_embeddings.py": ["google.cloud.aiplatform"],
    # Vector stores
    "test_chroma.py": ["chromadb"],
    "test_pinecone.py": ["pinecone"],
    "test_weaviate.py": ["weaviate"],
    "test_milvus.py": ["pymilvus"],
    "test_mongodb.py": ["pymongo"],
    "test_elasticsearch.py": ["elasticsearch"],
    "test_opensearch.py": ["opensearchpy"],
    "test_pgvector.py": ["psycopg2", "pgvector"],
    "test_cassandra.py": ["cassandra"],
    "test_baidu.py": ["baidu"],
    "test_supabase.py": ["supabase"],
    "test_azure_ai_search.py": ["azure.search.documents"],
    "test_azure_mysql.py": ["azure.mysql"],
    "test_upstash_vector.py": ["upstash_vector"],
    "test_valkey.py": ["valkey"],
    "test_vertex_ai_vector_search.py": ["google.cloud.aiplatform"],
    "test_langchain_vector_store.py": ["langchain"],
    "test_s3_vectors.py": ["boto3"],
    "test_turbopuffer.py": ["turbopuffer"],
    "test_redis.py": ["redis"],
}

# Files that need durag.server or durag.client (removed from library-only fork)
_SERVER_CLIENT_DEPS: dict[str, list[str]] = {
    "test_server_auth.py": ["durag.server"],
    "test_server_params.py": ["durag.server"],
    "test_client.py": ["durag.client"],
    "test_client_feedback.py": ["durag.client"],
    "test_proxy.py": ["durag.client", "durag.proxy"],
    "test_telemetry_aliasing.py": ["durag.client"],
    "test_project.py": ["durag.client"],
}


def pytest_collection_modifyitems(config, items):
    """Skip tests whose optional dependencies aren't installed.

    Runs after collection so we can inspect each item's file path.
    """
    for item in items:
        fspath = item.fspath.basename if hasattr(item, "fspath") else Path(str(item.fspath)).name

        # Check optional third-party deps
        deps = _OPTIONAL_DEPS.get(fspath, [])
        for dep in deps:
            if not _module_available(dep):
                item.add_marker(pytest.mark.skip(reason=f"Requires {dep} — install with optional extras"))
                break

        # Check server/client deps (library-only fork)
        deps = _SERVER_CLIENT_DEPS.get(fspath, [])
        for dep in deps:
            if not _module_available(dep):
                item.add_marker(pytest.mark.skip(reason=f"Requires {dep} — only available in full mem0 SDK"))
                break


def _module_available(module_name: str) -> bool:
    """Check if a module can be imported without raising."""
    try:
        importlib.import_module(module_name)
        return True
    except (ImportError, ModuleNotFoundError):
        return False
