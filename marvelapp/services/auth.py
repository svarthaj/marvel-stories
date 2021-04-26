import os, time, hashlib

def get_auth_params():
    ts = str(time.time_ns())
    auth_params = {
        'ts': ts,
        'apikey': os.environ['PUBLIC_API_KEY'],
        'hash': hashlib.md5("".join((ts,os.environ['PRIVATE_API_KEY'],os.environ['PUBLIC_API_KEY'])).encode("utf-8")).hexdigest()
    }
    return auth_params
