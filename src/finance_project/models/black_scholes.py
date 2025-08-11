from __future__ import annotations
from dataclasses import dataclass
from typing import Literal

OptionType = Literal["call", "put"]

@dataclass(frozen=True)
class BSInputs:
    S: float     # spot
    K: float     # strike
    T: float     # time in years
    r: float     # cont. risk-free rate
    sigma: float # volatility

def d1_d2(x: BSInputs) -> tuple[float, float]:
    """TODO: implement d1,d2 per Black–Scholes; return (d1, d2)."""
    raise NotImplementedError

def price(x: BSInputs, opt: OptionType = "call") -> float:
    """TODO: implement BS price using CDF of std normal."""
    raise NotImplementedError

def greeks(x: BSInputs, opt: OptionType = "call") -> dict[str, float]:
    """TODO: compute delta, gamma, vega, theta, rho."""
    raise NotImplementedError
