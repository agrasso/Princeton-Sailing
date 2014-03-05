from jinja2 import Environment, FileSystemLoader
import json
import markdown

env = Environment(loader=FileSystemLoader('templates'))

tabs = [('Home','index'),
        ('Roster','roster'),
        ('News','news'),
        ('Alumni','alumni'),
        ('Photos','photos'),
        ('Schedule','schedule')
        ]

def make_index():
   template = env.get_template('index.html')
   with open('text/home_text.text','r') as f:
      home_text = markdown.markdown(f.read(),['extra'])
   output = template.render(tabs=tabs,selected="index",home_text=home_text)
   with open('site/index.html','w') as f:
      f.write(output)

def make_roster():
   template = env.get_template('roster.html')
   with open('data/roster.json','r') as f:
      team = json.load(f)
   output = template.render(tabs=tabs,selected="roster",team=team)
   with open('site/roster.html','w') as f:
      f.write(output)

def make_news():
   template = env.get_template('news.html')
   with open('text/news_text.text','r') as f:
     news_text = markdown.markdown(f.read(),['extra'])
     output = template.render(tabs=tabs,selected="news",news_text=news_text)
   with open('site/news.html','w') as f:
      f.write(output)

def make_alumni():
   template = env.get_template('alumni.html')
   output = template.render(tabs=tabs,selected="alumni")
   with open('site/alumni.html','w') as f:
      f.write(output)

def make_photos():
   template = env.get_template('photos.html')
   output = template.render(tabs=tabs,selected="photos")
   with open('site/photos.html','w') as f:
      f.write(output)

def make_schedule():
   template = env.get_template('schedule.html')
   with open('data/schedule.json','r') as f:
      schedule = json.load(f)
   output = template.render(tabs=tabs,selected="schedule", schedule=schedule)
   with open('site/schedule.html','w') as f:
     f.write(output)

def main():
   make_index()
   make_roster()
   make_news()
   make_alumni()
   make_photos()
   make_schedule()

if __name__ == '__main__':
   main()
