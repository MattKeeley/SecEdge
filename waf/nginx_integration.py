# nginx_integration.py
class NginxModule:
    def __init__(self, waf_engine):
        self.waf_engine = waf_engine

    def handle_request(self, request):
        return self.waf_engine.process_request(request)
