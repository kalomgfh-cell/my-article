import os

folder = "football"

base = "https://github.com/kalomgfh-cell/my-article/blob/main/football/"

urls = []

for f in os.listdir(folder):
    if f.endswith(".md"):
        urls.append(base + f)

urls.sort()

xml = """<?xml version="1.0" encoding="UTF-8"?>

<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">

<url>
<loc>https://kalomgfh-cell.github.io/my-article/</loc>
</url>

<url>
<loc>https://kalomgfh-cell.github.io/my-article/football/index.html</loc>
</url>

"""

for url in urls:
    xml += f"""
<url>
<loc>{url}</loc>
</url>

"""

xml += """
</urlset>
"""

with open("sitemap.xml","w",encoding="utf-8") as f:
    f.write(xml)

print("sitemap生成完成，共加入文章：", len(urls))