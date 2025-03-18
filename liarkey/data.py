from enum import Enum
from pydantic import BaseModel

class Sisters(Enum):
    MABEL = 1
    DOROTHY = 2
    JULIETTA = 3
    ISABELLA = 4
    MADELINE = 5

class Reliability(BaseModel):
    truth_teller: bool = False
    liar: bool = False
    
    def __post_init__(self):
        if self.truth_teller and self.liar:
            raise("Reliability Conflict!!!")
    
    def is_truth_teller(self) -> bool:
        return self.truth_teller and not self.liar
    
    def is_liar(self) -> bool:
        return not self.truth_teller and self.liar
    
    def is_unknown(self) -> bool:
        return not self.truth_teller and not self.liar
    
    def get_name(self):
        if self.truth_teller:
            if self.liar:
                return "CONFLICT"
            else:
                return "TRUTH-TELLER"
        else:
            if self.liar:
                return "LIER"
            else:
                return "UNKNOWN"

class Possibility(BaseModel):
    crimer: bool = False
    innocence: bool = False
    
    """
    def __post_init__(self):
        if self.crimer and self.innocence:
            raise("Possibility Conflict!!!")
    """
    
    def is_crimer(self) -> bool:
        return self.crimer and not self.innocence
    
    def is_innocence(self) -> bool:
        return not self.crimer and self.innocence
    
    def is_unknown(self) -> bool:
        return not self.crimer and not self.innocence
    
    def get_name(self) -> str:
        if self.crimer:
            if self.innocence:
                return "CONFLICT"
            else:
                return "YOU ARE CRIMER"
        else:
            if self.innocence:
                return "SAFE"
            else:
                return "UNKNOWN"

