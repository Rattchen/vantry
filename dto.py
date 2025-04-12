from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class ProductDTO:
    barcode: int
    name: str
    brand: Optional[str]
    calories: Optional[float] #per 100g

    @classmethod
    def from_json(cls, json: dict):
        return cls(
            barcode = json.get("code", "No known barcode"),
            name = json.get("product_name", "No known name"),
            brand = json.get("brands", "No known brand"),
            calories = json.get("nutriments", {}).get("energy-kcal_100g")
        )
