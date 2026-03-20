from collections import Counter

from app.api.models import Signal


def summarize_signals(signals: list[Signal]) -> dict:
    sources = Counter([s.source for s in signals])
    segments = Counter([s.segment for s in signals])
    avg_severity = round(sum(s.severity for s in signals) / len(signals), 2) if signals else 0.0
    top_terms = Counter()
    for signal in signals:
        for token in signal.text.lower().split():
            cleaned = token.strip(",.!?;:()[]{}\"'")
            if len(cleaned) > 4:
                top_terms[cleaned] += 1

    return {
        "signal_count": len(signals),
        "source_breakdown": dict(sources),
        "segment_breakdown": dict(segments),
        "average_severity": avg_severity,
        "top_terms": [word for word, _ in top_terms.most_common(10)],
        "summary": "Signals indicate the strongest concentration around repeated customer friction themes and should be reviewed for roadmap or release follow-up.",
    }
