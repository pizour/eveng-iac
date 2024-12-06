from evengsdk.client import EvengClient
import requests

def eveng_connect(host, username, password, protocol):
    conn = EvengClient(host=host, protocol=protocol, ssl_verify=False)
    conn.disable_insecure_warnings()
    conn.login(username=username, password=password)
    return conn


def check_eveng_password(host, username, password, protocol):
    try:
        conn = EvengClient(host=host, protocol=protocol, ssl_verify=False)
        conn.disable_insecure_warnings()
        conn.login(username=username, password=password)
        conn.logout()
        return True
    except Exception as e:
        return False

def check_eveng_connection(host, protocol, timeout=1):
    url = f"{protocol}://{host}/" 

    try:
        response = requests.get(url, timeout=timeout, verify=False)
        if response.status_code == 200:
            print(f"Connection successful: {protocol}://{host} (Status Code: {response.status_code})")
            return True
        else:
            print(f"Connection failed: {protocol}://{host} (Status Code: {response.status_code})")
            return False

    except requests.exceptions.Timeout:
        print(f"Timeout occurred while trying to connect to {protocol}://{host}")
        return False
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while trying to connect to {protocol}://{host}: {e}")
        return False