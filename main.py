import requests
from bs4 import BeautifulSoup

print('''
 __      __.__                           .___
/  \    /  \__|____________  _____     __| _/
\   \/\/   /  \___   /\__  \ \__  \   / __ | 
 \        /|  |/    /  / __ \_/ __ \_/ /_/ | 
  \__/\  / |__/_____ \(____  (____  /\____ | 
       \/           \/     \/     \/      \/ 
        https://github.com/Wizaad/WizSpyda
           https://twitter.com/MrWizaad
''')

response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".question-summary")
for question in questions:
    print(question.select_one(".question-hyperlink").getText())
    print(question.select_one(".vote-count-post").getText())


