Du-RAG Documentation
====================

**Du-RAG** (Durable RAG) is a persistent memory layer for AI agents built on retrieval-augmented generation.

.. code-block:: bash

   pip install durag

.. code-block:: python

   from durag import Memory

   m = Memory()
   m.add("Alice loves Python and open source", user_id="alice")
   history = m.get_all(filters={"user_id": "alice"})
   print(history)

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   getting-started
   api-reference
   configuration
   providers
   vector-stores
   contributing
