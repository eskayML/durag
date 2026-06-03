Getting Started
===============

Installation
------------

.. code-block:: bash

   pip install durag

Quick Start
-----------

Set your API key and create a memory instance:

.. code-block:: python

   import os
   from durag import Memory

   os.environ["OPENAI_API_KEY"] = "sk-..."
   m = Memory()

   # Add memories
   m.add("Alice is a software engineer", user_id="alice")
   m.add("Alice works at a startup", user_id="alice")

   # Retrieve all memories for a user
   history = m.get_all(filters={"user_id": "alice"})
   print(history)

   # Search memories semantically
   results = m.search("What does Alice do?", filters={"user_id": "alice"})
   print(results)
