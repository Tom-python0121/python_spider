# douban_spider.py
import requests
from bs4 import BeautifulSoup  # 网页解析器
import pandas as pd
import time                    # 控制访问间隔
from feishu_uploader import get_token, upload_to_feishu

# ==============================
# 1️⃣ 爬取豆瓣 Top250 前 100 条
# ==============================
def get_douban_top100():
    """
    从豆瓣 Top250 页面抓取前 100 条电影信息。
    使用 requests + BeautifulSoup。
    """

    # 设置请求头，模拟浏览器访问，防止被封
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36",
        "Referer": "https://movie.douban.com/",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }

    movies = []  # 用于存放所有电影字典的列表

    # 这里通过分页参数 start，每页 25 条
    for start in range(0, 100, 25):
        url = f"https://movie.douban.com/top250?start={start}"
        res = requests.get(url, headers=headers, timeout=10)
        res.encoding = "utf-8"  # 指定中文编码
        soup = BeautifulSoup(res.text, "html.parser")

        # 查找所有电影条目 div
        for item in soup.select("div.item"):
            title = item.select_one("span.title").get_text(strip=True)
            rating = item.select_one("span.rating_num").get_text(strip=True)
            link = item.select_one("a")["href"]
            info = item.select_one("div.bd p").get_text(strip=True)

            # 将一条电影信息存入字典
            movies.append({
                "电影名称": title,
                "评分": rating,
                "链接": link,
                "详情": info
            })

        print(f"📄 已抓取 {len(movies)} 条...")
        time.sleep(1)  # 每页暂停 1 秒，防止封 IP

    print(f"✅ 共抓取到 {len(movies)} 条电影数据")

    # 转为 DataFrame，方便后续保存/上传
    return pd.DataFrame(movies)


# ==============================
# 2️⃣ 主函数入口
# ==============================
if __name__ == "__main__":
    print("🎬 正在爬取豆瓣 Top100...")

    # 调用爬取函数
    df = get_douban_top100()

    # 保存本地备份
    df.to_csv("douban_top100.csv", index=False, encoding="utf-8-sig")
    print("✅ 已保存到 douban_top100.csv")

    # 上传到飞书
    print("🔐 正在连接飞书...")
    token = get_token()
    upload_to_feishu(df, token)
    print("🚀 全部上传完毕！")
