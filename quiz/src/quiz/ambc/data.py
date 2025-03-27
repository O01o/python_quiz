from pydantic import BaseModel

class Edge(BaseModel):
    src: str | None = None
    dst: str | None = None
    through: bool | None = None
    
    def __post_init__(self):
        if not self.src and self.dst:
            self.through = True
        if self.src and not self.dst:
            self.through = False