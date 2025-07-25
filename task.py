class Task:
    def __init__(self, title):
        self.title = title
        self.is_completed = False

    def toggle_status(self):
        self.is_completed = not self.is_completed

    def __str__(self):
        status = "✓" if self.is_completed else "✗"
        return f"{self.title} [{status}]"
