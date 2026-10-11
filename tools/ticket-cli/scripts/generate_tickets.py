"""Generate a deterministic synthetic support-ticket dataset for development.

Run from anywhere with: `uv run python scripts/generate_tickets.py`
Writes 10,000 rows to tools/ticket-cli/data/tickets.csv.
"""

import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

from faker import Faker

SEED = 42
NUM_TICKETS = 10_000
CATEGORIES = ["billing", "shipping", "account", "bug", "other"]
PRIORITIES = ["low", "medium", "high", "urgent"]
UNRESOLVED_RATE = 0.20  # roughly 20% of tickets have no resolved_at

OUTPUT_PATH = Path(__file__).resolve().parent.parent / "data" / "tickets.csv"

HEADER = [
    "id",
    "customer_email",
    "subject",
    "body",
    "category",
    "priority",
    "created_at",
    "resolved_at",
]


def main() -> None:
    # Seed both RNGs: Python's global one and Faker's internal one.
    random.seed(SEED)
    fake = Faker()
    Faker.seed(SEED)

    # Make sure tools/ticket-cli/data/ exists.
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    now = datetime.now()
    seconds_in_90_days = 90 * 24 * 60 * 60

    with OUTPUT_PATH.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(HEADER)

        for ticket_id in range(1, NUM_TICKETS + 1):
            # Pick how long ago the ticket was created (1 second to 90 days).
            age_seconds = random.randint(1, seconds_in_90_days)
            created_at = now - timedelta(seconds=age_seconds)

            # ~20% unresolved; otherwise pick a resolution time
            # between created_at and now (inclusive of now, exclusive of created_at).
            if random.random() < UNRESOLVED_RATE:
                resolved_at_str = ""
            else:
                delay_seconds = random.randint(1, age_seconds)
                resolved_at = created_at + timedelta(seconds=delay_seconds)
                resolved_at_str = resolved_at.isoformat(timespec="seconds")

            writer.writerow(
                [
                    ticket_id,
                    fake.email(),
                    fake.sentence(nb_words=6).rstrip("."),
                    fake.paragraph(nb_sentences=3),
                    random.choice(CATEGORIES),
                    random.choice(PRIORITIES),
                    created_at.isoformat(timespec="seconds"),
                    resolved_at_str,
                ]
            )

    print(f"Wrote {NUM_TICKETS:,} tickets to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
