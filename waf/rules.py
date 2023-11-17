# waf/rules.py
from waf.waf import Rule

class SQLInjectionRule(Rule):
    def __init__(self):
        super().__init__("SQL Injection", "")

    def matches(self, request):
        print(f"Checking SQL Injection Rule for request: {request}")
        sql_injection_patterns = ["'", "--", "SELECT", "UNION", "INSERT", "UPDATE", "DELETE", "DROP"]
        result = any(pattern in request for pattern in sql_injection_patterns)
        print(f"Rule Match Result: {result}")
        return result

class XSSRule(Rule):
    def __init__(self):
        super().__init__("Cross-Site Scripting (XSS)", "")

    def matches(self, request):
        xss_patterns = ["<script>", "onerror", "alert(", "eval(", "prompt("]
        return any(pattern in request for pattern in xss_patterns)

class XXERule(Rule):
    def __init__(self):
        super().__init__("XML External Entity (XXE)", "")

    def matches(self, request):
        xxe_patterns = ["<!ENTITY", "SYSTEM"]
        return any(pattern in request for pattern in xxe_patterns)

class LFIRule(Rule):
    def __init__(self):
        super().__init__("Local File Inclusion (LFI)", "")

    def matches(self, request):
        lfi_patterns = ["../", "../../", "%2e%2e/", "%252e%252e/"]
        return any(pattern in request for pattern in lfi_patterns)

class RFIRule(Rule):
    def __init__(self):
        super().__init__("Remote File Inclusion (RFI)", "")

    def matches(self, request):
        rfi_patterns = ["http://", "https://", "ftp://"]
        return any(pattern in request for pattern in rfi_patterns)
