import os

base_url = "https://kalomgfh-cell.github.io/my-article"

urls = []

current_dir = os.getcwd()

for root, dirs, files in os.walk(current_dir):
    for file in files:

        if file.endswith(".html"):

            full_path = os.path.join(root, file)

            # 获取相对于 my-article 的路径
            relative_path = os.path.relpath(full_path, current_dir)

            # Windows路径改成网址格式
            relative_path = relative_path.replace("\\", "/")

            # 跳过首页
            if relative_path != "index.html":

                urls.append(f"{base_url}/{relative_path}")


with open("sitemap.xml", "w", encoding="utf-8") as f:

    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')

    for url in urls:
        f.write("  <url>\n")
        f.write(f"    <loc>{url}</loc>\n")
        f.write("  </url>\n")

    f.write("</urlset>\n")


print("sitemap.xml生成完成，共生成", len(urls), "个地址")