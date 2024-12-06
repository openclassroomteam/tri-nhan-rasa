from __future__ import annotations
from typing import Any, Dict, List, Optional, Text

from rasa.engine.recipes.default_recipe import DefaultV1Recipe
from rasa.engine.graph import ExecutionContext
from rasa.engine.storage.resource import Resource
from rasa.engine.storage.storage import ModelStorage
from rasa.nlu.tokenizers.tokenizer import Token, Tokenizer
from rasa.shared.nlu.training_data.message import Message


@DefaultV1Recipe.register(
    DefaultV1Recipe.ComponentType.MESSAGE_TOKENIZER, is_trainable=False
)
class VietnameseTokenizer(Tokenizer):

    @staticmethod
    def supported_languages() -> Optional[List[Text]]:
        return ["vi"]

    @staticmethod
    def get_default_config() -> Dict[Text, Any]:
        """Returns the component's default config."""
        return {
            # Flag to check whether to split intents
            "intent_tokenization_flag": False,
            # Symbol on which intent should be split
            "intent_split_symbol": "_",
            # Regular expression to detect tokens
            "token_pattern": None,
            # Symbol on which prefix should be split
            "prefix_separator_symbol": None,
            # Tokenizer to use        
            "tokenizer": "pyvi",
        }

    def __init__(self, config: Dict[Text, Any]) -> None:
        """Initialize the tokenizer."""
        super().__init__(config)
        if config.get('tokenizer') == 'underthesea':
            self.tokenizer = 'underthesea'
        else:
            self.tokenizer = 'pyvi'

    @classmethod
    def create(
        cls,
        config: Dict[Text, Any],
        model_storage: ModelStorage,
        resource: Resource,
        execution_context: ExecutionContext
    ) -> VietnameseTokenizer:
        return cls(config)

    @staticmethod
    def required_packages() -> List[Text]:
        return ["pyvi"]

    def tokenize(self, message: Message, attribute: Text) -> List[Token]:
        text = message.get(attribute)
        text = text.replace('òa', 'oà').replace('óa', 'oá').replace('ỏa', 'oả').replace('õa', 'oã').replace('ọa', 'oạ').replace('òe', 'oè').replace('óe', 'oé').replace('ỏe', 'oẻ').replace('õe', 'oẽ').replace('ọe', 'oẹ').replace('ùy', 'uỳ').replace('úy', 'uý').replace('ủy', 'uỷ').replace('ũy', 'uỹ').replace('ụy', 'uỵ')
        if self.tokenizer == 'underthesea':
            from underthesea import word_tokenize
            words = word_tokenize(text, format="text").split()
        else:
            from pyvi import ViTokenizer
            words = ViTokenizer.tokenize(text).split()
        text = ' '.join(words)

        return self._convert_words_to_tokens(words, text)
