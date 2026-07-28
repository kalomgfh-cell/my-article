@echo off
chcp 65001 >nul

echo 正在生成 sitemap.xml...

echo ^<?xml version="1.0" encoding="UTF-8"?^> > sitemap.xml
echo ^<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"^> >> sitemap.xml


for /r %%a in (*.html) do (

    set "file=%%a"

    call set "path=%%file:%cd%\=%%"

    call echo ^<url^> >> sitemap.xml

    call echo ^<loc^>https://kalomgfh-cell.github.io/my-article/%%path:\=/^</loc^> >> sitemap.xml

    call echo ^</url^> >> sitemap.xml

)


echo ^</urlset^> >> sitemap.xml


echo.
echo sitemap.xml生成完成
pause