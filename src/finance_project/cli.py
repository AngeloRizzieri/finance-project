import typer
from .models.black_scholes import BSInputs, price, greeks
from .models.implied_vol import implied_vol

app = typer.Typer(help="Black–Scholes utilities (skeleton).")

@app.command()
def bs_price(S: float, K: float, T: float, r: float, sigma: float, opt: str = "call"):
    """TODO: call price() and print result."""
    raise NotImplementedError

@app.command()
def bs_greeks(S: float, K: float, T: float, r: float, sigma: float, opt: str = "call"):
    """TODO: call greeks() and print dict."""
    raise NotImplementedError

@app.command()
def bs_iv(S: float, K: float, T: float, r: float, mkt: float, opt: str = "call"):
    """TODO: call implied_vol() and print IV."""
    raise NotImplementedError

if __name__ == "__main__":
    app()
