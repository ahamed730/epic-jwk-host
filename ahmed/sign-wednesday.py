import jwt
import time
import uuid
import requests
from datetime import datetime, timezone, timedelta
from requests.structures import CaseInsensitiveDict


def main():
    client_id = 'ecb0df59-0c0b-4122-ad7f-df7ae889d558'
    token_url = 'https://fhir.epic.com/interconnect-fhir-oauth/oauth2/token'

    # Load RSA private key from PEM file
    with open('privatekey.pem', 'r') as f:
        private_key = f.read()

    now = int(time.time())
    payload = {
        "iss": client_id,
        "sub": client_id,
        "aud": token_url,
        "jti": str(uuid.uuid4()),
        "iat": now,
        "exp": now + 240,  # 4 minutes
    }

    # Encode JWT using RS384 (or change to RS256 if needed)
    encoded_jwt = jwt.encode(payload, private_key, algorithm="RS256")

    print("🔐 JWT:")
    print(encoded_jwt)

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/x-www-form-urlencoded"

    data = {
        "grant_type": "client_credentials",
        "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
        "client_assertion": encoded_jwt
    }

    response = requests.post(token_url, headers=headers, data=data)
    print("📡 Epic OAuth Response:")
    print(response.status_code)
    print(response.text)


if __name__ == "__main__":
    main()
