
---

## 🧾 README.md

```markdown
# 🎬 豆瓣热门电影 Top100 → 飞书多维表格自动同步

一个使用 **Python 爬虫 + 飞书开放平台 API** 实现的自动化项目：
从豆瓣电影获取热门 Top100 数据，并自动上传到飞书多维表格中，支持评分、链接、简介等字段。

---

## 🚀 功能简介

| 功能 | 描述 |
|------|------|
| 🎥 数据爬取 | 自动从豆瓣热门榜抓取前 100 条电影数据 |
| 📊 数据清洗 | 提取电影名、评分、链接、简介等字段 |
| 🪄 自动上传 | 通过 Feishu API 批量上传到飞书多维表格 |
| 💾 数据备份 | 同时将数据保存为 CSV 文件 |
| 🔐 配置灵活 | 支持自定义飞书表格、APP ID、APP Secret |

---

## 🧰 技术栈

- 🐍 **Python 3.10+**
- 🌐 `requests` — 网络请求
- 🍜 `BeautifulSoup4` — 网页解析
- 📦 `pandas` — 数据处理
- 🔑 `yaml` — 配置管理
- 🪶 飞书开放平台 API（bitable + token）

---

## 📂 项目结构

```

📁 python_spider/
├── csdn_hot_to_feishu/       # 核心模块（豆瓣爬虫 + 上传飞书）
│    ├── douban_to_feishu.py  # 主执行文件（含主函数）
│    ├── feishu_config.py     # 飞书配置与 Token 获取
│    └── config.yaml          # 飞书 app_id / secret / 表格配置（建议本地保存，不上传）
├── README.md                 # 项目说明文档
├── .gitignore                # 忽略文件配置
└── douban_top100.csv         # 豆瓣数据备份文件

````

---

## ⚙️ 使用方法

### 1️⃣ 克隆项目
```bash
git clone https://github.com/Tom-python0121/python_spider.git
cd python_spider
````

### 2️⃣ 安装依赖

```bash
pip install -r requirements.txt
```

如果没有 `requirements.txt`，可手动安装：

```bash
pip install requests beautifulsoup4 pandas pyyaml
```

### 3️⃣ 配置飞书信息

在根目录创建 `config.yaml`：

```yaml
feishu:
  app_id: "你的App ID"
  app_secret: "你的App Secret"
  app_token: "你的App Token"
  table_id: "你的表格ID"
```

### 4️⃣ 运行主程序

```bash
python csdn_hot_to_feishu/douban_to_feishu.py
```

执行后会：

* 爬取豆瓣 Top100 热门电影；
* 保存为 `douban_top100.csv`；
* 自动上传至飞书表格。

---

## 🧩 常见问题（踩坑经验）

| 问题                                  | 解决方案                                        |
| ----------------------------------- | ------------------------------------------- |
| ❌ `remote origin already exists`    | 使用 `git remote set-url origin 新地址` 替换       |
| ⚠️ `adding embedded git repository` | 删除子项目的 `.git` 文件夹，执行 `git rm --cached 文件夹名` |
| 🔐 飞书上传失败                           | 检查字段类型（评分要为数字，链接要为 link 类型）                 |
| 🕷 豆瓣反爬                             | 添加 `User-Agent`、`Referer`、Cookie 可有效避免      |

---

## 🧠 学习笔记推荐

> 💡 本项目包含以下 Python 知识点：

* `requests.get()` 网络请求
* `BeautifulSoup.select()` HTML 解析
* `pandas.DataFrame` 数据结构与保存
* `yaml.safe_load()` 配置读取
* `for i in range(0, len(records), 10)` 批量上传逻辑
* `f"字符串{变量}"` 格式化语法
* `if __name__ == "__main__":` 主程序入口

---

## 💬 作者信息

👤 **Tony Wei / 闪光的盼盼**
📍 Shenzhen, China
📧 [GitHub主页](https://github.com/Tom-python0121)
💬 微信公众号：**盼哥PyAI实验室**

---

## ⭐ Star 一下支持我吧！

如果这个项目对你有帮助，欢迎点亮 ⭐ Star！
你的一颗星就是我继续更新的最大动力 ✨

```