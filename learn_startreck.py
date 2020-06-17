import requests

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print("Сетевая ошибка")
        return False

if name == "main":
    html = get_html("https://www.blog.python.org/")
    if html:
        with open("python.org.html", "w", encoding="utf8") as f:
            f.write(html)