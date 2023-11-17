from flask import Flask, request, abort
from waf.waf_engine import WAFEngine
from waf.database import Database
from waf.rules import SQLInjectionRule, XSSRule
from waf.nginx_integration import NginxModule

app = Flask(__name__)
app.logger.setLevel('DEBUG')

database = Database()
waf_engine = WAFEngine()
waf_engine.load_rules(database.get_rules() + [SQLInjectionRule(), XSSRule])
waf_engine.load_rate_limits(database.get_rate_limits())
nginx_module = NginxModule(waf_engine)

@app.route('/')
def index():
    test_param = request.args.get('test', '')
    app.logger.info(f"Received request data: {test_param}")

    result = nginx_module.handle_request(test_param)

    if result == "Blocked by WAF":
        app.logger.warning("Request blocked by WAF")
        abort(406)

    app.logger.info(f"Response: {result}")
    return f"Response: {result}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
