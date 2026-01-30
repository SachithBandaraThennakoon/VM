class SessionState:
    """
    Simulated awareness layer.
    Tracks what the system is currently doing.
    """

    def __init__(self):
        self.current_focus = None
        self.student_level = None
        self.last_feedback = None

    def update(self, focus=None, feedback=None, level=None):
        if focus:
            self.current_focus = focus
        if feedback:
            self.last_feedback = feedback
        if level:
            self.student_level = level
