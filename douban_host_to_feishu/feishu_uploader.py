# feishu_uploader.py
import requests  # 用于 HTTP 请求（访问飞书 API）
import yaml      # 读取 YAML 配置文件（比 JSON 更简洁）

# ==============================
# 1️⃣ 读取飞书配置文件
# ==============================
# YAML 文件是键值结构，例如：
# feishu:
#   app_id: "cli_xxx"
#   app_secret: "xxx"
#   app_token: "bascnxxx"
#   table_id: "tblxxx"
with open("config.yaml", "r", encoding="utf-8") as f:
    CONFIG = yaml.safe_load(f)  # safe_load 会安全地解析 yaml 到字典

# 从配置文件中读取变量，方便后续调用
APP_ID = CONFIG["feishu"]["app_id"]
APP_SECRET = CONFIG["feishu"]["app_secret"]
APP_TOKEN = CONFIG["feishu"]["app_token"]
TABLE_ID = CONFIG["feishu"]["table_id"]


# ==============================
# 2️⃣ 获取 Token
# ==============================
def get_token():
    """
    从飞书开放平台获取租户级 Access Token。
    每个 token 有效期 2 小时。
    """
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    data = {"app_id": APP_ID, "app_secret": APP_SECRET}
    # 向飞书服务器发 POST 请求，请求 token
    res = requests.post(url, json=data)
    token = res.json().get("tenant_access_token")
    if not token:
        # 如果响应中没有 token，则打印错误
        raise Exception(f"获取 Token 失败: {res.text}")
    return token


# ==============================
# 3️⃣ 上传 DataFrame 到飞书多维表格
# ==============================
def upload_to_feishu(df, token):
    """
    将 pandas.DataFrame 数据批量上传到飞书多维表格。
    - 每次最多上传 10 条（飞书 API 限制）
    """
    # 拼接上传接口 URL
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{APP_TOKEN}/tables/{TABLE_ID}/records/batch_create"

    # 设置请求头，包含认证信息
    headers = {
        "Authorization": f"Bearer {token}",  # 认证用 Token
        "Content-Type": "application/json"   # 告诉服务器这是 JSON 格式
    }

    # 将 DataFrame 的每一行转成 JSON 格式
    records = []
    for _, row in df.iterrows():  # iterrows() 逐行遍历 DataFrame
        record = {
            "fields": {
                # str() 确保类型安全
                "电影名称": str(row["电影名称"]),
                # 检查评分是否为数字，防止上传时报错
                "评分": float(row["评分"]) if str(row["评分"]).replace('.', '', 1).isdigit() else 0.0,
                # 链接字段需要是一个对象，包含 link 和 text
                "链接": {
                    "link": row["链接"],
                    "text": "豆瓣页面"
                },
                "详情": str(row["详情"])
            }
        }
        records.append(record)

    # 批量上传，每 10 条一批
    for i in range(0, len(records), 10):
        batch = records[i:i + 10]
        res = requests.post(url, headers=headers, json={"records": batch})
        if res.status_code == 200 and "error" not in res.text:
            print(f"✅ 上传成功：第 {i // 10 + 1} 批")
        else:
            print(f"⚠️ 上传失败：HTTP {res.status_code} -> {res.text[:200]}")
