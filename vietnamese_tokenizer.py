from typing import Any, Dict, List, Text
from rasa.nlu.tokenizers.tokenizer import Token, Tokenizer
from rasa.shared.nlu.training_data.message import Message
from rasa.nlu.constants import TOKENS_NAMES, MESSAGE_ATTRIBUTES


class VietnameseTokenizer(Tokenizer):

    provides = [TOKENS_NAMES[attribute] for attribute in MESSAGE_ATTRIBUTES]
    defaults = {'tokenizer': 'pyvi'}

    def __init__(self, component_config: Dict[Text, Any] = None) -> None:
        super().__init__(component_config)
        if component_config.get('tokenizer') == 'underthesea':
            self.tokenizer = 'underthesea'
        else:
            self.tokenizer = 'pyvi'

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
