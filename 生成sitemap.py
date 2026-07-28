import os

# GitHub仓库地址
base_url = "https://github.com/kalomgfh-cell/my-article/blob/main"

urls = []

# 当前文件夹
current_dir = os.getcwd()

for root, dirs, files in os.walk(current_dir):

    for file in files:

        # 只生成MD文件
        if file.endswith(".md"):

            full_path = os.path.join(root, file)

            # 转换相对路径
            relative_path = os.path.relpath(full_path, current_dir)

            # Windows路径转换成网址路径
            relative_path = relative_path.replace("\\", "/")

            urls.append(f"{base_url}/{relative_path}")


with open("sitemap.xml", "w", encoding="utf-8") as f:

    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')

    for url in urls:

        f.write("  <url>\n")
        f.write(f"    <loc>{url}</loc>\n")
        f.write("  </url>\n")

    f.write("</urlset>\n")


print("sitemap.xml生成完成，共生成", len(urls), "个MD地址")