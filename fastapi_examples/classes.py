from dataclasses import dataclass, field
from typing import List, Union


@dataclass
class Item:
    name: str
    price: float
    tags: List[str] = field(default_factory=list)
    description: Union[str, None] = None
    tax: Union[float, None] = None
