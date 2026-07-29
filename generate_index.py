import os

folder = "football"

files = []

for f in os.listdir(folder):
    if f.endswith(".md"):
        files.append(f)

files.sort()

html = """<!DOCTYPE html>
<html lang="zh-CN">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>体育行业观察文章中心</title>

<meta name="description" content="体育行业观察原创文章列表">

<style>

body{
max-width:800px;
margin:auto;
padding:20px;
font-family:"Microsoft YaHei",Arial;
color:#333;
}

h1{
text-align:center;
}

.article{
border:1px solid #eee;
border-radius:10px;
padding:15px;
margin-bottom:15px;
}

a{
color:#0066cc;
text-decoration:none;
font-size:18px;
}

.info{
color:#888;
font-size:14px;
margin-top:8px;
}

</style>

</head>

<body>

<h1>
体育行业观察文章中心
</h1>

"""

for f in files:
    title = f.replace(".md","")

    html += f"""
<div class="article">

<a href="https://github.com/kalomgfh-cell/my-article/blob/main/football/{f}">

{title}

</a>

<div class="info">
原创文章 · 2026
</div>

</div>

"""

html += """

</body>

</html>
"""

with open("football/index.html","w",encoding="utf-8") as f:
    f.write(html)

print("生成完成，共生成文章：", len(files))