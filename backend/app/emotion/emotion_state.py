class EmotionState:
    def __init__(self):
        self.state = "calm"

    def update(self, signals: dict):
        """
        signals may include:
        - tension
        - frustration
        - repeated_errors
        """
        if signals.get("tension") == "high":
            self.state = "calm"
        elif signals.get("repeated_errors"):
            self.state = "encouraging"
        elif signals.get("unsafe_intent"):
            self.state = "restrained"
        else:
            self.state = "neutral"
