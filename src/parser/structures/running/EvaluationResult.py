from enum import Enum

class EvaluationResultType(Enum):
    NUMBER = 1
    FINITE_SET = 2
    INFINITE_SET = 3
    FUNCTION = 4
    SYMBOL = 5
    UNDEFINED_OUT_OF_DOMAIN = 6
    

class EvaluationResult:
    def __init__(self, type: EvaluationResultType, value: any) -> None:
        self.type = type
        self.value = value