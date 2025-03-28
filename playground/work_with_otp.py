import jwt

secret = "kjhkjjjjhikhkjk"

payload = {"my_name": "Vasyl", "age": 45}

encode_jwt = jwt.encode(payload=payload, key=secret, algorithm="HS256")
print(encode_jwt)

decoded = jwt.decode(encode_jwt, secret, algoritms=["HS256"])
print(decoded)

decoded = jwt.decode(encode_jwt, secret, algorithms=["HS256"])
print(decoded)
