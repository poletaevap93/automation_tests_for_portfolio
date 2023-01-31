from dataclasses import dataclass

@dataclass
class Person:   # в этом классе прописывается какой будет тип у свойств класса
    full_name: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None