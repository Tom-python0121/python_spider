import requests
from bs4 import BeautifulSoup

url = "https://movie.douban.com/top250?start=0"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://movie.douban.com/",
    "Accept-Language": "zh-CN,zh;q=0.9",
}

res = requests.get(url, headers=headers, timeout=10)
print("HTTP 状态码：", res.status_code)
print("页面前 500 字符：")
print(res.text[:500])

if res.status_code == 200:
    soup = BeautifulSoup(res.text, "html.parser")
    items = soup.select("div.item")
    print(f"🎬 共检测到 {len(items)} 个电影项。")
    if len(items) > 0:
        title = items[0].select_one("span.title").get_text(strip=True)
        print("示例标题：", title)
        print("页面长度：", len(res.text))
        print("包含 div.item 吗？", "div class=\"item\"" in res.text)
else:
    print("❌ 访问异常，可能被反爬或封禁。")
