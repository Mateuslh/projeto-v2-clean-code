from enum import Enum


class TipoQuarto(str, Enum):
    STANDARD = "S"
    DELUXE = "D"
    PREMIUM = "P"

    @property
    def tarifa(self) -> int:
        return {"S": 100, "D": 200, "P": 300}[self.value]
