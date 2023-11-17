# database.py
class Database:
    def __init__(self):
        # Simplified in-memory database
        self.rules = []
        self.rate_limits = []

    def get_rules(self):
        return self.rules

    def get_rate_limits(self):
        return self.rate_limits
