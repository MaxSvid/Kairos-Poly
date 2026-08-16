"""
positions.py — every CURRENTLY ACTIVE position for a wallet, via GET /positions.

"Active" = the market hasn't resolved yet, so the token is still worth
something and its price can still move. redeemable=false
gives you: it excludes markets that have already finished

mergeable is intentionally NOT filtered on. It only tells you whether you
happen to be holding shares of BOTH outcomes of the same still-open market
"""

import requests
import pandas as pd

DATA_API_BASE = "https://data-api.polymarket.com"


def fetch_positions(wallet: str, limit: int = 100, size_threshold: float = 1) -> list[dict]:
    """
    size_threshold filters out dust (tiny leftover balances worth pennies).
    Lower it to 0 if you want to see literally everything, including dust.
    """
    all_positions = []
    offset = 0

    while True:
        response = requests.get(
            f"{DATA_API_BASE}/positions",
            params={
                "user": wallet,
                "sizeThreshold": size_threshold,
                "redeemable": "false",  
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

    df = pd.DataFrame(positions)

    columns_we_care_about = [
        "title", "outcome", "size", "avgPrice", "curPrice",
        "currentValue", "cashPnl", "percentPnl", "mergeable", "endDate",
    ]
    existing_columns = [c for c in columns_we_care_about if c in df.columns]

    return df[existing_columns]


def summarize(df: pd.DataFrame) -> None:
    """
    Breaks active value into single-sided vs hedged (mergeable), then the
    combined total. Every row here is already "active" -- redeemable=false
    was applied upstream in fetch_positions, so there's no resolved/dead
    bucket to show.
    """
    if df.empty:
        print("No active positions.\n")
        return

    live = df[df["mergeable"] == False]
    mergeable = df[df["mergeable"] == True]

    print(f"Live / open (single-sided):     {len(live):>3}  -- ${live['currentValue'].sum():,.2f}")
    print(f"Mergeable (holding both sides): {len(mergeable):>3}  -- ${mergeable['currentValue'].sum():,.2f}")
    print(f"Total position value:                -- ${df['currentValue'].sum():,.2f}\n")


if __name__ == "__main__":
    wallet = "0x91667e40b80c447050904b042f3b85d22fc6b479"
    positions = fetch_positions(wallet)
    print(f"{len(positions)} active position(s) for {wallet}\n")

    if positions:
        df = positions_to_dataframe(positions)
        summarize(df)
        print(df.to_string(index=False))

# 0x91667e40b80c447050904b042f3b85d22fc6b479

# 0x8e74984fb998be82444627906740dc1a19c35972