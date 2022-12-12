from enum import Enum
from typing import Tuple
from molt.src.parser.structures.running.EvaluationVariables import EvaluationVariables

from molt.src.parser.structures.syntax.conditions.Condition import Condition
from molt.src.parser.structures.syntax.expressions.Expression import Expression
from molt.src.parser.structures.syntax.expressions.base_literals.Variable import Variable

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
        
    def get_finite_set(self) -> set['EvaluationResult']:
        if self.type == EvaluationResultType.FINITE_SET:
            return self.value
        else:
            raise(Exception("Value is not a finite set"))
            
    def get_infinite_set(self) -> Tuple[Variable,set[set[Condition]]]:
        """
        An infinite set is expressed as:
        a tuple of
        - a variable, which is the "bound variable of the set"; `x` in `{ x |: x > 3 }`
        - a set of
            - sets of
                - conditions, each of which has the given bound variable as their left-hand side.
                
        If the following is the set of sets of conditions which expresses the infinite set:
        
        ```
        {
            {x > 2, x < 4},
            {x = 9}
        }
        ```
        
        then the infinite set should be understood as "all numbers which are (greater than 2 AND less than 4), OR (equal to 9)". Having both
        AND and OR allows us to express unions of sets. 
        """
        if self.type == EvaluationResultType.INFINITE_SET:
            return self.value
        else:
            raise ("Value is not an infinite set")
            
    def __repr__(self) -> str:
        if self.type == EvaluationResultType.NUMBER:
            if self.value == int(self.value):
                return str(int(self.value))
            return str(self.value)
        elif self.type == EvaluationResultType.SYMBOL:
            return str(self.value)
        elif self.type == EvaluationResultType.FINITE_SET:
            return str(self.value)
        elif self.type == EvaluationResultType.FUNCTION:
            func = self.get_function_attributes()
            return f"{', '.join(v.name for v in func[1])} => {func[0]}"
        elif self.type == EvaluationResultType.UNDEFINED_OUT_OF_DOMAIN:
            return "undefined"
        elif self.type == EvaluationResultType.INFINITE_SET:
            return '#infinite set'
            
    
    def get_function_attributes(self) -> Tuple[Expression,list[Variable]]:
        if self.type == EvaluationResultType.FUNCTION:
            return self.value
        else:
            raise ("Value is not a function")
