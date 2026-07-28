@echo off
chcp 65001 >nul

echo 正在生成 sitemap.xml...

(
echo ^<?xml version="1.0" encoding="UTF-8"?^>
echo ^<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"^>

for /r %%i in (*.html) do (
    if /i not "%%~nxi"=="index.html" (
        echo ^<url^>
        echo ^<loc^>https://kalomgfh-cell.github.io/my-article/%%~pi%%~nxi^</loc^>
        echo ^</url^>
    )
)

echo ^</urlset^>

) > sitemap.xml

echo sitemap.xml生成完成
pause