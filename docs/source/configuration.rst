Configuration
=============

Memory Config
-------------

.. autoclass:: durag.configs.base.MemoryConfig
   :members:
   :noindex:

Example:

.. code-block:: python

   from durag import Memory
   from durag.configs.base import MemoryConfig
   from durag.configs.llms.base import BaseLlmConfig

   config = MemoryConfig(
       llm=BaseLlmConfig(model="gpt-4.1-nano", temperature=0.3),
   )
   m = Memory(config=config)
