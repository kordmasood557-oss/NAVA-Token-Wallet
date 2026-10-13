"""
NAVA Wallet
Early development prototype.

Security rules:
- Never store private keys in this repository.
- Never enter a real recovery phrase into this prototype.
- Do not use this prototype to store or transfer real funds.
"""

PROJECT_NAME = "NAVA Wallet"
VERSION = "0.1.0"
STATUS = "Development Prototype"

FEATURES = [
    "Digital asset wallet design",
    "Transparent transaction records",
    "User-controlled key security",
    "AMANAT charitable allocation support",
]


def wallet_status():
    return {
        "project": PROJECT_NAME,
        "version": VERSION,
        "status": STATUS,
        "features": FEATURES,
        "ready_for_real_funds": False,
    }


if __name__ == "__main__":
    for key, value in wallet_status().items():
        print(f"{key}: {value}")
