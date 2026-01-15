import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    data = response.json()
    print("Title:", data["title"])
except requests.exceptions.Timeout:
    print("Request timed out.")
except requests.exceptions.HTTPError:
    print("HTTP error occurred.")
except Exception as e:
    print("Unexpected error:", e)
else:
    print("API call successful.")
finally:
    print("Request attempt finished.")



def get_post(post_id):
    try:
        url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
        r = requests.get(url)
        r.raise_for_status()
        return r.json()
    except:
        return None

post = get_post(2)
if post:
    print("Fetched:", post["title"])
else:
    print("Failed to fetch post")
