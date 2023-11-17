# waf_engine.py
class WAFEngine:
    def __init__(self):
        self.rules = []
        self.rate_limits = []

    def load_rules(self, rules):
        self.rules = rules

    def load_rate_limits(self, rate_limits):
        self.rate_limits = rate_limits

    def process_request(self, request):
        for rule in self.rules:
            if rule.matches(request):
                self.log_request(request, f"Rule Match: {rule.name}")
                return "Blocked by WAF"

        if self.is_rate_limited(request):
            self.log_request(request, "Rate Limit Exceeded")
            return "Blocked by Rate Limit"

        return "Request Allowed"

    def is_rate_limited(self, request):
        return len(request) > max([rate_limit.limit for rate_limit in self.rate_limits], default=float('inf'))

    def log_request(self, request, message):
        print(f"WAF: {message} - {request}")
