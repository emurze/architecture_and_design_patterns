import uuid
from dataclasses import dataclass, field
from datetime import date


@dataclass
class User:
    birthday: date
    first_name: str
    last_name: str
    user_id: str = field(default_factory=lambda: str(uuid.uuid4()))
