from __future__ import annotations
from .black_scholes import BSInputs, price

def implied_vol(target_price: float, x: BSInputs, opt: str = "call") -> float:
    """TODO: root-find sigma so BS price == target_price (e.g., brentq)."""
    raise NotImplementedError
