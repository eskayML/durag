LLM Providers
=============

Du-RAG supports multiple LLM providers. Set the corresponding environment variable before use.

.. list-table::
   :header-rows: 1

   * - Provider
     - Env Variable
     - Used For
   * - OpenAI (default)
     - ``OPENAI_API_KEY``
     - Embeddings + LLM
   * - Anthropic
     - ``ANTHROPIC_API_KEY``
     - LLM
   * - Google Gemini
     - ``GOOGLE_API_KEY``
     - Embeddings + LLM
   * - DeepSeek
     - ``DEEPSEEK_API_KEY``
     - LLM
   * - Together AI
     - ``TOGETHER_API_KEY``
     - Embeddings + LLM
   * - Groq
     - ``GROQ_API_KEY``
     - LLM
   * - MiniMax
     - ``MINIMAX_API_KEY``
     - LLM
   * - Ollama (local)
     - ``OLLAMA_HOST``
     - Embeddings + LLM
   * - vLLM
     - ``VLLM_API_KEY``
     - LLM
