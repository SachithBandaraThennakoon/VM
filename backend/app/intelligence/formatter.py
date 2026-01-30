def format_intelligence_feedback(feedback_list: list) -> str:
    """
    Converts intelligence module outputs into a clean text summary
    suitable for LLM context.
    """
    lines = []

    for item in feedback_list:
        if "guidance" in item:
            lines.append(f"- {item['guidance']}")
        if item.get("block"):
            lines.append(f"- {item.get('message')}")

    if not lines:
        return "No critical issues detected."

    return "\n".join(lines)
