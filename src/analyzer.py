from __future__ import annotations


def generate_recommendation(metrics: dict) -> dict:
    """Generate an educational recommendation based on rule-based scoring."""
    score = 0
    reasons: list[str] = []

    if metrics["current_price"] > metrics["ma50"]:
        score += 2
        reasons.append("Current price is above the 50-day moving average.")
    else:
        score -= 2
        reasons.append("Current price is below the 50-day moving average.")

    if metrics["ma20"] > metrics["ma50"]:
        score += 2
        reasons.append("20-day moving average is above the 50-day moving average, showing positive short-term momentum.")
    else:
        score -= 1
        reasons.append("20-day moving average is not above the 50-day moving average.")

    if metrics["six_month_return"] > 0.10:
        score += 2
        reasons.append("Six-month performance is strong.")
    elif metrics["six_month_return"] > 0:
        score += 1
        reasons.append("Six-month performance is positive.")
    else:
        score -= 2
        reasons.append("Six-month performance is negative.")

    vol = metrics["annualized_volatility"]
    if vol < 0.25:
        score += 2
        reasons.append("Volatility is relatively moderate.")
    elif vol < 0.40:
        reasons.append("Volatility is elevated but still manageable.")
    else:
        score -= 2
        reasons.append("Volatility is high, which increases risk.")

    rsi = metrics["rsi14"]
    if rsi > 70:
        score -= 1
        reasons.append("RSI suggests the stock may be overbought.")
    elif rsi < 30:
        reasons.append("RSI suggests the stock may be oversold.")
    else:
        score += 1
        reasons.append("RSI is in a balanced range.")

    if score >= 5:
        label = "Better suited for long-term investing"
        risk_score = 3 if vol < 0.25 else 4
    elif score >= 2:
        label = "May be suitable for short-term trading"
        risk_score = 5 if vol < 0.40 else 6
    else:
        label = "Use caution"
        risk_score = 7 if vol < 0.50 else 8

    summary = build_summary(label, metrics)

    return {
        "label": label,
        "score": score,
        "risk_score": risk_score,
        "reasons": reasons,
        "summary": summary,
    }


def build_summary(label: str, metrics: dict) -> str:
    if label == "Better suited for long-term investing":
        return (
            "This stock shows a relatively healthy trend with supportive momentum and manageable risk levels "
            "based on the indicators used in this project."
        )
    if label == "May be suitable for short-term trading":
        return (
            "This stock shows movement and activity that may interest short-term traders, but it has enough risk "
            "that it should be monitored carefully."
        )
    return (
        "This stock currently shows weaker trend conditions or higher risk based on the project rules, so a beginner "
        "investor should be careful."
    )