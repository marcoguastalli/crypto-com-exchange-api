from datetime import datetime

from dotenv import dotenv_values

REST_API_ENDPOINT_SANDBOX = "https://uat-api.3ona.co/v2/"
REST_API_ENDPOINT_PRODUCTION = "https://api.crypto.com/v2/"
REST_API_ENDPOINT = REST_API_ENDPOINT_PRODUCTION


def main():
    config = dotenv_values(".env")
    url = REST_API_ENDPOINT + 'public/get-ticker'
    print("Reading account from API url '%s' at '%s'" % (url, datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")))


if __name__ == "__main__":
    main()
