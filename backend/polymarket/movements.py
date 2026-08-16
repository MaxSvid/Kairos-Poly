# connects with bot to inform about wallet movements and transactions

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

# Wallets to monitor
# Format: (label, wallet_address, category)
# Add or remove wallets here -- output is printed in this exact order.
# Needs to add demo database for wallets tabels
WALLETS = [
    ("logos_1",      "0xc65ca4755436f82d8eb461e65781584b8cadea39", "Esports - Valorant"),
    ("logos_2",      "0x5e6e2c3f06686f2607b86c90e35f536e81a1be00", "Esports - CS2:GO"),
    ("logos_3",      "0x8726d2642c9cdd9819a30539ff1acf7666090f36", "Esports - Valorant and CS2:GO"),
    ("dialectic_1",  "0x91667e40b80c447050904b042f3b85d22fc6b479", "Esports - League of Legends")
]



def fetch_positions(wallet: str, limit: int = 100, size_threshold: float = 1) -> list[dict]:
    """
    Fetch every currently active (unresolved) position for a wallet.

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
                "redeemable": "false",  # excludes resolved/finished markets
                # mergeable intentionally omitted to see module docstring
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
        print("  No active positions.\n")
        return

    live = df[df["mergeable"] == False]
    mergeable = df[df["mergeable"] == True]

    print(f"  Live / open (single-sided):     {len(live):>3}  -- ${live['currentValue'].sum():,.2f}")
    print(f"  Mergeable (holding both sides): {len(mergeable):>3}  -- ${mergeable['currentValue'].sum():,.2f}")
    print(f"  Total position value:                -- ${df['currentValue'].sum():,.2f}")


def print_wallet_block(label: str, wallet: str, category: str) -> None:
    """
    Fetches and prints one wallet's full position block, clearly labeled.
    Called once per wallet in the WALLETS list.
    """
    width = 72
    print("=" * width)
    print(f"  {label}  |  {category}")
    print(f"  {wallet}")
    print("=" * width)

    try:
        positions = fetch_positions(wallet)
    except requests.exceptions.RequestException as e:
        print(f"  ERROR fetching positions: {e}\n")
        return

    if not positions:
        print("  No active positions right now.\n")
        return

    print(f"  {len(positions)} active position(s)\n")

    df = positions_to_dataframe(positions)
    summarize(df)
    print()

    # print the full table, indented slightly for readability
    table = df.to_string(index=False)
    for line in table.splitlines():
        print(f"  {line}")
    print()


if __name__ == "__main__":
    pd.set_option("display.max_colwidth", 55)
    pd.set_option("display.float_format", "{:.4f}".format)

    for label, wallet, category in WALLETS:
        print_wallet_block(label, wallet, category)

    print("=" * 72)
    print("  Done.")
    print("=" * 72)