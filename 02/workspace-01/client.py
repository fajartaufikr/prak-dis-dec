import requests

url = "http://localhost:8000/graphql"

query = """
{
  books {
    title
    author
  }
}
"""

response = requests.post(url, json={"query": query})

print(response.json())