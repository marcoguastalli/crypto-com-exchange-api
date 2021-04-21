# https://exchange-docs.crypto.com/spot/index.html?python#digital-signature
import hashlib
import hmac


def sign_request(req, api_key, secret_key):
    if req is None or api_key is None or secret_key is None:
        return None
    # First ensure the params are alphabetically sorted by key
    param_string = ''
    if 'params' in req:
        for key in sorted(req['params']):
            param_string += key
            param_string += str(req['params'][key])
    # Combine method + id + api_key + parameter string + nonce
    sig_pay_load = req['method'] + str(req['id']) + req['api_key'] + param_string + str(req['nonce'])
    # Use HMAC-SHA256 to hash the above using the API Secret as the cryptographic key
    req['api_key'] = api_key
    req['sig'] = hmac.new(
        bytes(str(secret_key), 'utf-8'),
        msg=bytes(sig_pay_load, 'utf-8'),
        digestmod=hashlib.sha256
    ).hexdigest()
    # Encode the output as a hex string
    return req
