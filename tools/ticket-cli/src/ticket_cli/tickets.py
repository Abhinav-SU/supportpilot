PRIORITY_ORDER = {"low": 1, "medium": 2, "high": 3, "urgent": 4}


def priority_rank(priority: str) -> int:
    """Turn a priority name into a number so tickets can be sorted."""
    return PRIORITY_ORDER[priority.lower()]
