#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office - one auto-reply, no pretending.

A single out-of-office email auto-reply of at most 200 characters: honest
about the inbox, polite enough for a manager to let stand. Pure stdlib,
deterministic, no network, no secrets; writes the reply to /output/entry.txt.
"""
import os

# The reply, assembled from its three beats so each stays easy to audit:
# a polite opening, the honest confession, and a professional close.
_OPENING = "Thank you for your email. I am out of the office, and in the interest of full honesty:"
_CONFESSION = "I will not be checking this inbox, thinking about this inbox, or missing this inbox."
_CLOSING = "I will reply on my return."


def build_reply():
    """Return the full auto-reply, exactly 198 characters."""
    return " ".join((_OPENING, _CONFESSION, _CLOSING))


def main():
    reply = build_reply()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as out:
        out.write(reply)


if __name__ == "__main__":
    main()
