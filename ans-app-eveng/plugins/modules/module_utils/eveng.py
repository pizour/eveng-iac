from evengsdk.client import EvengClient

def eveng_connect(host, username, password):
    conn = EvengClient(host=host)
    conn.login(username=username, password=password)
    return conn


def change_admin_password(conn, new_password):
    try:
        response = conn.api.auth_change_password(new_password)
        return response
        if response.get('status') == 'success':
            print("Password changed successfully.")
        else:
            print("Failed to change password: ", response.get('message'))

    except Exception as e:
        print(f"Error occurred: {e}")