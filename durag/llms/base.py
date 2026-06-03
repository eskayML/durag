from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Union

from durag.configs.llms.base import BaseLlmConfig


class LLMBase(ABC):
    """
    Base class for all LLM providers.
    Handles common functionality and delegates provider-specific logic to subclasses.
    """

    def __init__(self, config: Optional[Union[BaseLlmConfig, Dict]] = None):
        """Initialize a base LLM class

        :param config: LLM configuration option class or dict, defaults to None
        :type config: Optional[Union[BaseLlmConfig, Dict]], optional
        """
        if config is None:
            self.config = BaseLlmConfig()
        elif isinstance(config, dict):
            # Handle dict-based configuration (backward compatibility)
            self.config = BaseLlmConfig(**config)
        else:
            self.config = config

        # Validate configuration
        self._validate_config()

    def _validate_config(self):
        """
        Validate the configuration.
        Override in subclasses to add provider-specific validation.
        """
        if not hasattr(self.config, "model"):
            raise ValueError("Configuration must have a 'model' attribute")

        if not hasattr(self.config, "api_key") and not hasattr(self.config, "api_key"):
            # Check if API key is available via environment variable
            # This will be handled by individual providers
            pass

    @staticmethod
    def _uses_max_completion_tokens(model: str) -> bool:
        """
        Check if the model requires max_completion_tokens instead of max_tokens.
        
        This applies to:
        - o1, o3 series (o1, o1-preview, o1-2024-12-17, o3-mini, etc.)
        - gpt-5 series (gpt-5, gpt-5-mini, gpt-5o, gpt-5o-mini, gpt-5o-micro, gpt-5.x, etc.)
        
        Args:
            model: The model name to check
            
        Returns:
            bool: True if the model uses max_completion_tokens
        """
        model_lower = model.lower()
        base_model = model_lower.rsplit("/", 1)[-1]

        # Exact match on known models
        max_completion_models = {
            "o1", "o1-preview", "o3-mini", "o3",
            "gpt-5", "gpt-5-mini", "gpt-5o", "gpt-5o-mini", "gpt-5o-micro",
        }
        if base_model in max_completion_models:
            return True

        # Prefix match: o1/o3 family (o1-*, o3-*) and gpt-5 variants (gpt-5.*, gpt-5-*)
        if any(base_model.startswith(p) for p in ["o1-", "o1.", "o3-", "o3.", "gpt-5"]):
            return True

        return False

    def _is_strict_reasoning_model(self, model: str) -> bool:
        """
        Check if the model is a strict reasoning model (o1/o3 series) that
        doesn't support temperature, top_p, or max_tokens.
        
        These models only support: messages, response_format, tools, tool_choice,
        reasoning_effort, and max_completion_tokens.
        
        Args:
            model: The model name to check
            
        Returns:
            bool: True if the model is a strict reasoning model
        """
        model_lower = model.lower()
        base_model = model_lower.rsplit("/", 1)[-1]

        strict_models = {"o1", "o1-preview", "o3-mini", "o3"}
        if base_model in strict_models:
            return True

        # Match o1/o3 family with prefixes (o1-2024-12-17, o3-2025-04-16)
        # but NOT gpt-5 variants (which support temperature and top_p)
        if any(base_model.startswith(p) for p in ["o1-", "o1.", "o3-", "o3."]):
            return True

        return False

    def _get_supported_params(self, **kwargs) -> Dict:
        """
        Get parameters that are supported by the current model.
        Handles differences between reasoning models, GPT-5 series, and regular models.
        
        Args:
            **kwargs: Additional parameters to include
            
        Returns:
            Dict: Filtered parameters dictionary
        """
        model = getattr(self.config, 'model', '')
        
        if self._is_strict_reasoning_model(model):
            # o1/o3 series: strip temperature, top_p, max_tokens
            supported_params = {}
            
            if "messages" in kwargs:
                supported_params["messages"] = kwargs["messages"]
            if "response_format" in kwargs:
                supported_params["response_format"] = kwargs["response_format"]
            if "tools" in kwargs:
                supported_params["tools"] = kwargs["tools"]
            if "tool_choice" in kwargs:
                supported_params["tool_choice"] = kwargs["tool_choice"]

            # Add reasoning_effort if configured
            reasoning_effort = getattr(self.config, 'reasoning_effort', None)
            if reasoning_effort:
                supported_params["reasoning_effort"] = reasoning_effort

            # Add max_completion_tokens for reasoning models that need it
            if self.config.max_tokens is not None:
                supported_params["max_completion_tokens"] = self.config.max_tokens

            return supported_params
        else:
            # For regular models (including GPT-5 series), include all common params
            return self._get_common_params(**kwargs)

    @abstractmethod
    def generate_response(
        self, messages: List[Dict[str, str]], tools: Optional[List[Dict]] = None, tool_choice: str = "auto", **kwargs
    ):
        """
        Generate a response based on the given messages.

        Args:
            messages (list): List of message dicts containing 'role' and 'content'.
            tools (list, optional): List of tools that the model can call. Defaults to None.
            tool_choice (str, optional): Tool choice method. Defaults to "auto".
            **kwargs: Additional provider-specific parameters.

        Returns:
            str or dict: The generated response.
        """
        pass

    def _get_common_params(self, **kwargs) -> Dict:
        """
        Get common parameters that most providers use.
        Uses max_completion_tokens for models that require it (GPT-5, o1/o3 series).
        Temperature and top_p are always passed (strict reasoning models like o1/o3
        are handled by _get_supported_params which returns early).

        Returns:
            Dict: Common parameters dictionary.
        """
        model = getattr(self.config, 'model', '')
        uses_max_completion = self._uses_max_completion_tokens(model)
        
        token_key = "max_completion_tokens" if uses_max_completion else "max_tokens"
        
        params = {}
        
        params["temperature"] = self.config.temperature
        params["top_p"] = self.config.top_p
        
        params[token_key] = self.config.max_tokens

        # Add provider-specific parameters from kwargs
        params.update(kwargs)

        return params
