from evengsdk.client import EvengClient

def eveng_connect(host, username, password):
    conn = EvengClient(host=host, ssl_verify=False, protocol="https")
    conn.disable_insecure_warnings()
    conn.login(username=username, password=password)
    return conn
