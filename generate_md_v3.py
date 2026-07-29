import os
import openpyxl
import random
import datetime


# =========================
# V9 基础设置
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


today = datetime.date.today().strftime(
    "%Y-%m-%d"
)



# =========================
# 创建目录
# =========================


if not os.path.exists(output_folder):

    os.makedirs(output_folder)



# =========================
# 读取标题
# =========================


wb = openpyxl.load_workbook(
    excel_file
)


ws = wb.active



titles = []



for row in ws.iter_rows(
    min_row=2,
    values_only=True
):

    if row[0]:

        title = str(
            row[0]
        ).strip()


        if title:

            titles.append(title)



# 去重

titles = list(
    dict.fromkeys(titles)
)



print(
    "读取标题数量:",
    len(titles)
)




# =========================
# 文件名清理
# =========================


def clean_filename(name):


    bad = [

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


    for x in bad:

        name = name.replace(
            x,
            "-"
        )


    return name.strip()






# =========================
# 提取关键词
# =========================


def get_keyword(title):


    title = title.replace(
        "：",
        "-"
    )


    if "-" in title:

        key = title.split("-")[-1]


    else:

        key = title



    return key.strip()






# =========================
# 自动分类 V9
# =========================


def get_category(title):


    t = title.lower()



    sports_event = [

        "足球",
        "篮球",
        "nba",
        "cba",
        "世界杯",
        "欧冠",
        "赛事",
        "比赛",
        "比分",
        "球队",
        "联赛"

    ]



    sports_platform = [

        "买球",
        "滚球",
        "盘口",
        "赔率",
        "体育网站",
        "体育平台",
        "注册"

    ]



    digital = [

        "pg",
        "jdb",
        "cq9",
        "ag",
        "mg",
        "bbin",
        "电子",
        "游戏",
        "app",
        "官网",
        "平台"

    ]



    for w in sports_event:


        if w in t:

            return "sports_event"




    for w in sports_platform:


        if w in t:

            return "sports_platform"




    for w in digital:


        if w in t:

            return "digital"




    return "normal"






# =========================
# 章节模板
# =========================


section_pool = {


"sports_event":[


[
"文章介绍",
"赛事背景",
"球队表现",
"数据分析",
"未来趋势"
],


[
"项目说明",
"历史变化",
"比赛数据",
"影响因素",
"发展方向"
]


],



"sports_platform":[


[
"相关说明",
"行业背景",
"平台特点",
"用户关注",
"未来变化"
],


[
"文章介绍",
"发展历程",
"功能分析",
"市场观察",
"趋势分析"
]


],



"digital":[


[
"文章介绍",
"行业背景",
"内容特点",
"数据分析",
"发展趋势"
],


[
"相关说明",
"发展历程",
"技术分析",
"用户观察",
"未来变化"
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
# 正文素材库 V9
# =========================


intro_pool = [

"随着互联网技术快速发展，{key}相关内容逐渐进入更多用户视野。近年来信息传播方式、技术环境以及用户需求不断变化，相关领域也持续调整。",

"在数字化环境不断变化的背景下，{key}成为部分用户关注的方向。通过资料整理和信息分析，可以观察相关内容的发展特点。",

"近年来互联网应用持续升级，{key}相关内容也随着技术进步产生新的变化，不同阶段的发展方向存在一定差异。"

]



background_pool = [

"{key}的发展受到技术升级、市场环境以及用户需求变化等多方面影响。随着网络环境完善，相关内容逐渐形成新的特点。",

"从发展过程来看，{key}并不是固定不变的，互联网环境变化以及技术能力提升都会影响相关方向。",

"行业环境变化对{key}产生影响，技术创新、信息传播方式以及用户习惯改变都是重要因素。"

]



feature_pool = [

"{key}通常涉及内容展示、技术表现、系统设计以及用户体验等多个方面，不同方向会形成不同特点。",

"从实际情况来看，{key}越来越重视稳定性、效率以及体验优化，技术能力成为重要参考因素。",

"相关内容的发展不仅依赖技术能力，同时也受到用户需求变化影响，数据整理和内容优化逐渐成为重要方向。"

]



analysis_pool = [

"通过资料整理可以发现，{key}的发展变化与技术环境密切相关，数据分析能够帮助观察相关趋势。",

"从数据观察角度来看，{key}受到市场变化、用户行为以及技术升级等因素共同影响。",

"信息时代中，数据已经成为分析变化的重要工具，通过整理资料可以进一步了解相关特点。"

]



trend_pool = [

"未来随着人工智能、大数据以及移动互联网技术继续发展，{key}相关领域可能进一步向智能化方向变化。",

"从长期发展来看，技术创新和用户体验优化仍然会影响{key}的发展方向。",

"未来相关领域可能更加重视效率提升、内容优化以及技术融合。"

]



summary_pool = [

"通过以上分析，可以了解到{key}的发展背景、主要特点以及未来变化方向。随着技术持续升级，相关领域仍会不断调整和优化。",

"本文围绕{key}进行了资料整理和内容分析，希望帮助读者更全面了解相关信息变化。",

"综合来看，{key}的发展受到技术、市场以及用户需求共同影响，未来仍可能出现新的变化。"

]





# =========================
# 分类扩展内容
# =========================


extra_pool = {


"sports_event":[

"体育赛事相关内容通常涉及比赛记录、球队表现、历史数据以及赛事资料等方面，通过公开资料整理，可以更加全面观察赛事变化。",

"现代体育行业不仅关注比赛结果，同时也重视数据统计、赛事分析以及信息传播方式。"

],



"sports_platform":[

"体育平台相关内容通常涉及信息展示、功能体验以及用户需求变化等方面。",

"随着互联网技术发展，体育信息服务越来越重视效率和体验优化。"

],



"digital":[

"数字内容相关领域通常涉及系统设计、技术应用、内容展示以及用户体验等方面。",

"随着技术不断升级，数字内容越来越重视稳定性、效率以及整体体验优化。"

],



"normal":[

"不同领域的发展受到技术、市场以及用户需求共同影响，需要结合实际情况进行分析。",

"随着数字化进程推进，多个行业正在通过技术升级提升效率。"

]


}






# =========================
# FAQ生成
# =========================


def make_faq(key):


    return f"""

### {key}主要有哪些特点？

{key}相关内容通常涉及技术表现、信息整理以及用户体验等方面。


### 如何了解{key}的发展变化？

可以通过公开资料、行业观察以及数据整理等方式进行分析。


### 未来{key}可能有哪些发展方向？

随着技术持续发展，相关领域可能继续优化调整。


"""







# =========================
# 信息模块
# =========================


def make_info(key,category):


    return f"""

## 信息整理


关键词：

{key}


更新时间：

{today}


分类：

{category}


"""






# =========================
# 相关文章
# =========================


def related_articles(current,files):


    result=[]


    for f in files:


        if f != current:


            result.append(
                f.replace(".md","")
            )


        if len(result)>=3:

            break



    if not result:

        return ""



    text="\n## 相关文章\n\n"



    for r in result:

        text += "- "+r+"\n"



    return text

# =========================
# 生成文章
# =========================


all_files=[]



for index,title in enumerate(titles, start=1):


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



    extra=random.choice(
        extra_pool[category]
    )



    description=f"{key}相关信息整理，包含发展背景、内容特点、数据分析以及未来趋势观察。"



    # =====================
    # Markdown
    # =====================


    article=""



    # Front Matter

    article += "---\n"

    article += f"title: {title}\n"

    article += f"description: {description}\n"

    article += f"date: {today}\n"

    article += f"category: {category}\n"

    article += "---\n\n"



    # 图片

    article += f"![99tee]({image_file})\n\n"



    # 标题

    article += "# "+title+"\n\n"



    # 章节1

    article += "## "+sections[0]+"\n\n"

    article += intro+"\n\n"



    # 章节2

    article += "## "+sections[1]+"\n\n"

    article += background+"\n\n"



    # 章节3

    article += "## "+sections[2]+"\n\n"

    article += feature+"\n\n"



    # 分类内容

    article += extra+"\n\n"



    # 数据分析

    article += "## 数据分析\n\n"

    article += analysis+"\n\n"



    # 信息整理

    article += make_info(
        key,
        category
    )



    # FAQ

    article += "## 常见问题\n\n"

    article += make_faq(
        key
    )



    # 趋势

    article += "## "+sections[4]+"\n\n"

    article += trend+"\n\n"



    # 相关文章

    filename = clean_filename(title)+".md"

    article += related_articles(
        filename,
        all_files
    )



    # 总结

    article += "## 总结\n\n"

    article += summary




    # 保存文件


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
    "\nMarkdown生成完成:",
    len(all_files)
)






# =========================
# sitemap.xml
# =========================


with open(
    "sitemap.xml",
    "w",
    encoding="utf-8"
) as f:


    f.write(
'''<?xml version="1.0" encoding="UTF-8"?>

<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">

'''
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
# README.md
# =========================


readme="# 文章目录\n\n"


readme+=f"更新时间：{today}\n\n"

readme+=f"文章数量：{len(all_files)}\n\n"



for file in all_files:


    name=file.replace(
        ".md",
        ""
    )


    readme+=f"- [{name}](football/{file})\n"



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
# index.html
# =========================


html="""

<!DOCTYPE html>

<html lang="zh-CN">

<head>

<meta charset="UTF-8">

<title>文章中心</title>

<meta name="viewport" content="width=device-width,initial-scale=1.0">

<style>

body{

max-width:900px;

margin:auto;

padding:20px;

font-family:"Microsoft YaHei";

line-height:1.8;

}

a{

color:#0366d6;

text-decoration:none;

}

.item{

padding:8px;

border-bottom:1px solid #ddd;

}

</style>

</head>


<body>


<h1>文章中心</h1>


"""



html+=f"<p>更新时间：{today}</p>\n"

html+=f"<p>文章数量：{len(all_files)}篇</p>\n"



for file in all_files:


    name=file.replace(
        ".md",
        ""
    )


    html+=f"""

<div class="item">

<a href="football/{file}">

{name}

</a>

</div>

"""



html+="""


</body>

</html>

"""



with open(
    "index.html",
    "w",
    encoding="utf-8"
) as f:


    f.write(
        html
    )



print(
    "index.html生成完成"
)





print(
"""

========================

V9全部生成完成

生成目录：

football/*.md

sitemap.xml

README.md

index.html


========================

"""
)