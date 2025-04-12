import requests

url = 'https://moemisto.ua/img/cache/blog_show_photo/blog/0004/75/fe2a5835d6d62a84d64cc357061c8186a244a1a8.jpeg'

responce = requests.get(url)

with open('spring.jpeg', mode="wb") as file:
    content = responce.content
    content += b'327637 Moks'
    file.write(content)
with open('spring.jpeg', mode='rb') as f:
    print(f.read())
pass