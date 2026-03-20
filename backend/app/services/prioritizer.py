from app.api.models import PrioritizationItem


def score_item(item: PrioritizationItem) -> float:
    return round(
        (item.frequency * 0.35)
        + (item.revenue_impact * 100 * 0.25)
        + (item.churn_risk * 100 * 0.25)
        + ((1 - item.complexity) * 100 * 0.15),
        2,
    )


def rank_items(items: list[PrioritizationItem]) -> list[dict]:
    ranked = []
    for item in items:
        ranked.append(
            {
                "title": item.title,
                "score": score_item(item),
                "reason": "Weighted by request volume, revenue impact, churn risk, and delivery simplicity.",
            }
        )
    return sorted(ranked, key=lambda x: x["score"], reverse=True)
