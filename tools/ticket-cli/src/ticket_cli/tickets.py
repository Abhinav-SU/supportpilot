PRIORITY_ORDER = {"low": 1, "medium": 2, "high": 3, "urgent": 4}


def priority_rank(priority: str) -> int:
    """Turn a priority name into a number so tickets can be sorted."""
    key = priority.lower()
    if key not in PRIORITY_ORDER:
        raise ValueError(f"Unkown priority: {priority}")
    return PRIORITY_ORDER[key]
