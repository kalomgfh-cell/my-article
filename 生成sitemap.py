import os

base_url = "https://kalomgfh-cell.github.io/my-article"

urls = []

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)

            # 转换成网站路径
            path = path.replace(".\\", "")
            path = path.replace("\\", "/")

            # 跳过首页（可选）
            if path != "index.html":
                urls.append(f"{base_url}/{path}")


with open("sitemap.xml", "w", encoding="utf-8") as f:

    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')

    for url in urls:
        f.write("  <url>\n")
        f.write(f"    <loc>{url}</loc>\n")
        f.write("  </url>\n")

    f.write("</urlset>\n")


print("sitemap.xml生成完成，共生成", len(urls), "个地址")