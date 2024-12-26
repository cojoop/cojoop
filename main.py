import feedparser, time

URL = "https://kmseunh.github.io/index.xml"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 2

markdown_text = """

## Hi there 👋, my name is Seunghyun

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FimseunghyunK&count_bg=%23CEB0BB&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

## I'm a Department of Computer Science student at Korea National Open University

- 🔥 I’m currently learning SpringBoot.
- 🌱 I'm looking to study Next.js soon.
- 👥 I'm looking to collaborate with anyone on any project.
- 💬 Ask me anything.
- ⭐️ Fun fact: I watch all the major European football matches live.

## 🔍 Find me on:

<p align="center">
  <a href="https://kmseunh.github.io/"><img src="https://img.shields.io/badge/Tech Blog-000000?style=for-the-badge&logo=GitHub&logoColor=white&link=https://kmseunh.github.io/"/></a>
  <a href="mailto:tmdgus8779@gmail.com"><img src="https://img.shields.io/badge/Gmail-d14836?style=for-the-badge&logo=Gmail&logoColor=white&link=mailto:tmdgus8779@gmail.com"/></a>
  <a href="https://www.linkedin.com/in/seunghyun-kim-250b562a6/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/seunghyun-kim-250b562a6/"/></a>
</p>

## 🛠️ Tech Stack:

<div align="center">
  <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
  <img src="https://img.shields.io/badge/css3-1572B6?style=for-the-badge&logo=css3&logoColor=white">
  <img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=JavaScript&logoColor=white">
  <img src="https://img.shields.io/badge/jquery-0769AD?style=for-the-badge&logo=jquery&logoColor=white">
</div>
&nbsp;
<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=Flask&logoColor=white">
  <img src="https://img.shields.io/badge/Java-007396?style=for-the-badge&logo=openjdk&logoColor=white">
  <img src="https://img.shields.io/badge/spring-6DB33F?style=for-the-badge&logo=spring&logoColor=white">
  <img src="https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=MariaDB&logoColor=white">
</div>
&nbsp;
<div align="center">
  <img src="https://img.shields.io/badge/dbeaver-382923?style=for-the-badge&logo=dbeaver&logoColor=white">
  <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white">
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white">
  <img src="https://img.shields.io/badge/Vim-019733?style=for-the-badge&logo=Vim&logoColor=white">
  <img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=for-the-badge&logo=Visual Studio Code&logoColor=white">
</div>
&nbsp;
<div align="center">
  <img src="https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white">
  <img src="https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=Ubuntu&logoColor=white">
  <img src="https://img.shields.io/badge/macos-000000?style=for-the-badge&logo=macos&logoColor=white">
</div>

## ✍🏻 Latest Blog Post

"""  # list of blog posts will be appended here

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"

f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
