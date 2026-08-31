"""
Temporary in-memory store for tracked wallets, keyed by Telegram user id.

Postgres-backed tracking is the documented long-term plan (see CLAUDE.md
Roadmap), but `backend/database/connection.py` doesn't work yet and the
configured POSTGRES_HOST is a Docker-network-internal hostname only
reachable on the VPS -- not from local dev. This module exists so /track
can actually be tested locally in the meantime. Data does not survive a
bot restart.
"""

from dataclasses import dataclass


@dataclass
class TrackedWallet:
    address: str
    name: str | None = None


_tracked: dict[int, dict[str, TrackedWallet]] = {}


def add_wallet(user_id: int, address: str, name: str | None = None) -> None:
    _tracked.setdefault(user_id, {})[address] = TrackedWallet(address=address, name=name)


def remove_wallet(user_id: int, address: str) -> bool:
    return _tracked.get(user_id, {}).pop(address, None) is not None


def list_wallets(user_id: int) -> list[TrackedWallet]:
    return list(_tracked.get(user_id, {}).values())
