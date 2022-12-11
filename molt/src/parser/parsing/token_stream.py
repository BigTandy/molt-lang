from typing import Iterator
from parser.structures.Token import Token


class TokenStream:
    def __init__(self, tokens: Iterator[Token]):
        self.tokens = tokens
        self.top_token = None
    
    def peek(self) -> Token:
        if self.top_token != None:
            return self.top_token
        else:
            self.top_token = self.tokens.__next__()
            return self.top_token
    
    def pop(self) -> Token:
        if self.top_token != None:
            swap = self.top_token
            self.top_token = None
            return swap
        else:
            return self.tokens.__next__()
    