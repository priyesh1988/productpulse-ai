from app.api.models import PrioritizationItem
from app.services.prioritizer import rank_items


def test_rank_items_orders_highest_score_first() -> None:
    items = [
        PrioritizationItem(
            title="Low value item", frequency=2, revenue_impact=0.1, complexity=0.9, churn_risk=0.1
        ),
        PrioritizationItem(
            title="High value item", frequency=90, revenue_impact=0.9, complexity=0.2, churn_risk=0.8
        ),
    ]
    ranked = rank_items(items)
    assert ranked[0]["title"] == "High value item"
