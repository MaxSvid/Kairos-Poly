"""
positions.py — current open positions for a wallet, via GET /positions.

Same fetch-then-page pattern as history.py, but for /positions. Field
names below are taken directly from a real response, not guessed.
"""

import requests
import pandas as pd

DATA_API_BASE = "https://data-api.polymarket.com"


def fetch_positions(wallet: str, limit: int = 100) -> list[dict]:
    """
    Fetch all current open positions for a wallet.

    A single wallet rarely holds more than one page of positions, but
    we page defensively anyway -- same reasoning as history.py.
    """
    all_positions = []
    offset = 0

    while True:
        response = requests.get(
            f"{DATA_API_BASE}/positions",
            params={
                "user": wallet,
                "sizeThreshold": 1,
                "redeemable": "false",
                "mergeable": "false",
                "limit": limit,
                "offset": offset,
                "sortBy": "CASHPNL",
                "sortDirection": "DESC",
            },
            timeout=15,
        )
        response.raise_for_status()
        page = response.json()

        if not page:
            break

        all_positions.extend(page)

        if len(page) < limit:
            break

        offset += limit

    return all_positions


def positions_to_dataframe(positions: list[dict]) -> pd.DataFrame:
    """
    pd.DataFrame() turns a list of dicts straight into a table -- each
    dict's keys become columns, each dict becomes a row. The raw
    response has 25 fields; we only pull out the ones worth a glance.
    """
    df = pd.DataFrame(positions)

    columns_we_care_about = [
        "title", "outcome", "size", "avgPrice", "curPrice",
        "currentValue", "cashPnl", "percentPnl", "endDate",
    ]
    # keep only columns that actually exist, in case the API changes later
    existing_columns = [c for c in columns_we_care_about if c in df.columns]

    return df[existing_columns]


if __name__ == "__main__":
    wallet = "0x9db82de5a71ae539bc82f4d9ac3a007c7d742eff"
    positions = fetch_positions(wallet)
    print(f"{len(positions)} open position(s) for {wallet}\n")

    if positions:
        df = positions_to_dataframe(positions)
        print(df.to_string(index=False))