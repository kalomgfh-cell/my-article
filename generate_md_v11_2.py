import os
import openpyxl
import random
import datetime


# =========================
# V11.2 基础设置
# =========================


excel_file = "标题库.xlsx"

output_folder = "football"

image_file = "../99tee.png"


github_base = (
    "https://github.com/"
    "kalomgfh-cell/"
    "my-article/"
    "blob/main/"
    "football/"
)


today = datetime.date.today().strftime("%Y-%m-%d")



# =========================
# 创建目录
# =========================


if not os.path.exists(output_folder):

    os.makedirs(output_folder)



# =========================
# 读取标题库
# =========================


wb = openpyxl.load_workbook(
    excel_file
)


ws = wb.active


titles=[]


for row in ws.iter_rows(
    min_row=2,
    values_only=True
):

    if row[0]:

        title=str(row[0]).strip()

        if title:

            titles.append(title)



# 去重

titles=list(
    dict.fromkeys(titles)
)



print(
    "标题数量:",
    len(titles)
)



# =========================
# 文件名清理
# =========================


def clean_filename(name):


    chars=[

        "\\",
        "/",
        ":",
        "*",
        "?",
        "\"",
        "<",
        ">",
        "|"

    ]


    for c in chars:

        name=name.replace(
            c,
            "-"
        )


    return name.strip()




# =========================
# 关键词
# =========================


def get_keyword(title):


    title=title.replace(
        "：",
        "-"
    )


    if "-" in title:

        return title.split("-")[-1].strip()


    return title.strip()




# =========================
# 分类
# =========================


def get_category(title):


    t=title.lower()



    sports=[

        "足球",
        "篮球",
        "nba",
        "cba",
        "世界杯",
        "欧冠",
        "赛事",
        "球队",
        "比分",
        "联赛"

    ]



    platform=[

        "滚球",
        "盘口",
        "赔率",
        "体育",
        "平台"

    ]



    digital=[

        "pg",
        "jdb",
        "cq9",
        "ag",
        "mg",
        "bbin",
        "电子",
        "游戏",
        "app",
        "官网"

    ]



    for x in sports:

        if x in t:

            return "sports"



    for x in platform:

        if x in t:

            return "platform"



    for x in digital:

        if x in t:

            return "digital"



    return "normal"




# =========================
# 章节库
# =========================


section_pool={


"sports":[

[
"文章介绍",
"赛事背景",
"比赛特点",
"数据分析",
"未来趋势"
],

[
"项目说明",
"发展变化",
"赛事观察",
"用户关注",
"发展方向"
]

],



"platform":[

[
"相关说明",
"行业背景",
"平台特点",
"数据观察",
"未来趋势"
],

[
"文章介绍",
"功能分析",
"应用环境",
"用户体验",
"发展方向"
]

],



"digital":[

[
"文章介绍",
"技术背景",
"内容特点",
"数据分析",
"发展趋势"
],

[
"相关说明",
"技术发展",
"应用分析",
"用户观察",
"未来方向"
]

],



"normal":[

[
"文章介绍",
"发展背景",
"主要特点",
"数据分析",
"未来趋势"
],

[
"行业说明",
"核心内容",
"影响因素",
"趋势观察",
"发展方向"
]

]


}

# =========================
# V11.2 内容库
# =========================


intro_pool=[

"随着互联网技术不断发展，{key}相关信息逐渐受到关注。近年来，信息传播方式、技术环境以及用户需求不断变化。",

"在数字化环境不断变化的背景下，{key}成为部分用户关注方向，通过资料整理可以观察相关发展特点。",

"近年来互联网应用持续升级，{key}随着技术进步产生新的变化，不同阶段存在不同发展特点。"

]



background_pool=[

"{key}的发展受到技术升级、市场环境以及用户需求变化等多方面影响。",

"从发展过程来看，{key}并不是固定不变的，互联网环境变化会影响相关方向。",

"行业环境变化、技术创新以及信息传播方式都会影响{key}的发展。"

]



feature_pool=[

"{key}通常涉及内容展示、技术表现、系统设计以及用户体验等多个方面。",

"从实际情况来看，{key}越来越重视稳定性、效率以及体验优化。",

"相关内容的发展不仅依赖技术能力，同时也受到用户需求变化影响。"

]


analysis_pool=[

"通过资料整理可以发现，{key}的发展变化与技术环境密切相关。",

"从数据观察角度来看，{key}受到市场变化、用户行为以及技术升级共同影响。",

"数据已经成为分析变化的重要工具，通过整理资料可以进一步了解相关特点。"

]


trend_pool=[

"未来随着人工智能、大数据以及移动互联网技术发展，{key}可能进一步向智能化方向变化。",

"从长期发展来看，技术创新和用户体验优化仍然会影响{key}的发展方向。",

"未来相关领域可能更加重视效率提升、内容优化以及技术融合。"

]


summary_pool=[

"通过以上分析，可以了解到{key}的发展背景、主要特点以及未来变化方向。",

"本文围绕{key}进行了资料整理和内容分析，希望帮助读者了解相关信息变化。",

"综合来看，{key}的发展受到技术、市场以及用户需求共同影响。"

]



# =========================
# FAQ
# =========================


def make_faq(key):


    return f"""

### {key}主要有哪些特点？

{key}相关内容通常涉及技术表现、信息整理以及用户体验等方面。


### 如何了解{key}的发展变化？

可以通过公开资料、行业观察以及数据整理等方式进行分析。


### {key}未来有哪些发展趋势？

随着技术持续发展，相关领域可能继续优化调整。


"""




# =========================
# SEO描述
# =========================


def make_description(key):


    return (
        f"{key}相关信息整理，"
        "包含发展背景、内容特点、"
        "数据分析以及未来趋势观察。"
    )




# =========================
# 示例代码
# =========================


code_pool=[


'''info = {{

    "keyword":"{key}",

    "year":2026,

    "version":"V11.2"

}}

print(info)

''',



'''data=[

"{key}",

"technology",

"analysis"

]


for item in data:

    print(item)

''',



'''article={{

"title":"{key}",

"status":"generated"

}}

print(article)

'''

]




# =========================
# 开始生成文章
# =========================


all_files=[]


for index,title in enumerate(titles):


    key=get_keyword(title)


    category=get_category(title)


    sections=random.choice(
        section_pool[category]
    )



    intro=random.choice(
        intro_pool
    ).format(
        key=key
    )



    background=random.choice(
        background_pool
    ).format(
        key=key
    )



    feature=random.choice(
        feature_pool
    ).format(
        key=key
    )



    analysis=random.choice(
        analysis_pool
    ).format(
        key=key
    )


    trend=random.choice(
        trend_pool
    ).format(
        key=key
    )


    summary=random.choice(
        summary_pool
    ).format(
        key=key
    )



    code=random.choice(
        code_pool
    ).format(
        key=key
    )



    description=make_description(
        key
    )



    article=""


    # 图片

    article += f"![99tee]({image_file})\n\n"



    # 标题

    article += "# "+title+"\n\n"



    # SEO信息

    article += f"> 关键词：{key}\n\n"

    article += f"> 描述：{description}\n\n"



    article += f"> 发布时间：{today}\n\n"



    # 正文

    article += "## "+sections[0]+"\n\n"

    article += intro+"\n\n"



    article += "## "+sections[1]+"\n\n"

    article += background+"\n\n"



    article += "## "+sections[2]+"\n\n"

    article += feature+"\n\n"



    article += "## 数据分析\n\n"

    article += analysis+"\n\n"



    article += "## 示例代码\n\n"

    article += "```python\n"

    article += code

    article += "\n```\n\n"



    article += "## 常见问题\n\n"

    article += make_faq(key)



    article += "\n## "+sections[4]+"\n\n"

    article += trend+"\n\n"



    article += "## 总结\n\n"

    article += summary



    # =========================
    # 保存文件
    # =========================


    filename=clean_filename(title)+".md"


    filepath=os.path.join(
        output_folder,
        filename
    )


    with open(
        filepath,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(article)



    all_files.append(
        filename
    )



    print(
        "生成:",
        filename
    )



print(
    "V11.2 Markdown生成完成:",
    len(all_files)
)

# =========================
# V11.2 添加相关文章内链
# =========================


for file in all_files:


    filepath=os.path.join(
        output_folder,
        file
    )


    with open(
        filepath,
        "r",
        encoding="utf-8"
    ) as f:

        content=f.read()



    # 随机推荐文章

    recommend=random.sample(
        [
            x for x in all_files 
            if x != file
        ],
        min(5,len(all_files)-1)
    )



    content += "\n\n## 相关文章\n\n"



    for item in recommend:


        name=item.replace(
            ".md",
            ""
        )


        content += (
            f"- [{name}]({item})\n"
        )



    with open(
        filepath,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(content)



print(
    "相关文章内链生成完成"
)





# =========================
# 生成 sitemap.xml
# =========================


sitemap_file="sitemap.xml"



with open(
    sitemap_file,
    "w",
    encoding="utf-8"
) as f:


    f.write(
"""<?xml version="1.0" encoding="UTF-8"?>

<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">

"""
    )


    for file in all_files:


        f.write(
f"""
<url>

<loc>{github_base}{file}</loc>

<lastmod>{today}</lastmod>

<changefreq>weekly</changefreq>

<priority>0.8</priority>

</url>

"""
        )



    f.write(
"""
</urlset>
"""
    )



print(
    "sitemap.xml生成完成"
)





# =========================
# 生成首页 index.html
# =========================


index_html=f"""

<!DOCTYPE html>

<html lang="zh-CN">


<head>

<meta charset="UTF-8">


<meta name="viewport"
content="width=device-width,initial-scale=1.0">


<title>文章中心</title>


<style>


body{{

max-width:900px;

margin:auto;

padding:20px;

font-family:
Arial,
"Microsoft YaHei";

line-height:1.8;

}}


h1{{

text-align:center;

}}


.article{{

padding:12px 0;

border-bottom:1px solid #ddd;

}}


a{{

color:#0366d6;

text-decoration:none;

}}


</style>


</head>



<body>



<h1>

文章中心

</h1>


<p>

更新时间：

{today}

</p>



<p>

文章数量：

{len(all_files)}

篇

</p>


"""



for file in all_files:


    name=file.replace(
        ".md",
        ""
    )


    index_html += f"""

<div class="article">

<a href="football/{file}">

{name}

</a>

</div>

"""



index_html += """

</body>

</html>

"""



with open(
    "index.html",
    "w",
    encoding="utf-8"
) as f:


    f.write(
        index_html
    )



print(
    "index.html生成完成"
)





# =========================
# 生成 README.md
# =========================


readme="""

# 文章目录


"""


for file in all_files:


    name=file.replace(
        ".md",
        ""
    )


    readme += (
        f"- [{name}](football/{file})\n"
    )




with open(
    "README.md",
    "w",
    encoding="utf-8"
) as f:


    f.write(
        readme
    )



print(
    "README.md生成完成"
)





# =========================
# 最终提示
# =========================


print(
"""

============================
V11.2生成完成
============================

生成:

✔ football/*.md

✔ 自动相关文章内链

✔ sitemap.xml

✔ index.html

✔ README.md


文章数量:

""",
len(all_files)

)