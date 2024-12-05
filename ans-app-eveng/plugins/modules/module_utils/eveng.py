from evengsdk.client import EvengClient

def eveng_connect(host, username, password):
    conn = EvengClient(host=host)
    conn.login(username=username, password=password)
    return conn

def change_admin_password(conn, new_password):
    return conn.api.auth_change_password(new_password)
