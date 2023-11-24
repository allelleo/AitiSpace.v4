import httpx

client = httpx.Client()

while True:
    try:
        client.post('http://127.0.0.1/oauth/v1/sign-in/vk', timeout=0.00000001)
    except: pass