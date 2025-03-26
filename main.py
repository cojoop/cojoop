import feedparser, time

URL = "https://winn-dev.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 4

markdown_text = """

## Hi there 👋, my name is Seunghyun

## 🎓 I'm a Computer Science student at Korea National Open University.

- 🔥 I’m currently learning SpringBoot.
- 🌱 I'm looking to study Docker & AWS soon.
- 👥 I'm looking to collaborate with anyone on any project.
- 💬 Ask me anything.
- ⭐️ Fun fact: I watch all the major European football matches live.

## 🔍 Find me on:

<p align="center">
  <a href="https://winn-dev.tistory.com/"><img src="https://img.shields.io/badge/Tech Blog-000000?style=for-the-badge&logo=tistory&logoColor=white&link=https://winn-dev.tistory.com/"/></a>
  <a href="mailto:tmdgus8779@gmail.com"><img src="https://img.shields.io/badge/Gmail-d14836?style=for-the-badge&logo=Gmail&logoColor=white&link=mailto:tmdgus8779@gmail.com"/></a>
</p>

## 🛠️ Tech Stack:

<div align="center">
  <img src="https://go-skill-icons.vercel.app/api/icons?i=html,css,bootstrap,js,jquery" />
</div>
&nbsp;
<div align="center">
  <img src="https://go-skill-icons.vercel.app/api/icons?i=py,java,flask,spring,mysql" />
</div>
&nbsp;
<div align="center">
  <img src="https://skillicons.dev/icons?i=docker,git,github,ubuntu" />
</div>
&nbsp;
<div align="center">
  <img src="https://go-skill-icons.vercel.app/api/icons?i=dbeaver,eclipse,idea,vscode,vim" />
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
