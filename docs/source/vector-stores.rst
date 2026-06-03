Vector Stores
=============

Du-RAG uses **Qdrant** as the default vector store. Other backends are available.

.. list-table::
   :header-rows: 1

   * - Provider
     - Package
     - Default
   * - Qdrant
     - ``qdrant-client``
     - ✓ Default
   * - FAISS
     - ``faiss-cpu`` (optional)
     -
   * - Chroma
     - ``chromadb`` (optional)
     -
   * - Pinecone
     - ``pinecone`` (optional)
     -
   * - Weaviate
     - ``weaviate`` (optional)
     -
   * - Milvus
     - ``pymilvus`` (optional)
     -

Example with FAISS:

.. code-block:: python

   from durag.configs.base import MemoryConfig
   from durag.configs.vector_stores.configs import VectorStoreConfig

   config = MemoryConfig(
       vector_store=VectorStoreConfig(provider="faiss")
   )
   m = Memory(config=config)
