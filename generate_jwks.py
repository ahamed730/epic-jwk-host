from jwcrypto import jwk
import json

# Load your private key (update the filename if needed)
with open("ahmed/privatekey.pem", "rb") as f:
    key = jwk.JWK.from_pem(f.read())

# Export the public part of the key
public_jwk = json.loads(key.export(private_key=False))
jwks = {"keys": [public_jwk]}

# Save to jwks.json
with open("jwks.json", "w") as out:
    json.dump(jwks, out, indent=2)

print("✅ Generated jwks.json")
