
from bs4 import BeautifulSoup

class RedditScrapper():
    def __init__(self, httpClient):
        self.httpClient = httpClient
    
    def execute(self):
        response = self.httpClient.get('/search/?q=bbse3')
        soup = BeautifulSoup(response['body'], 'html.parser')
        titles = []
        
        for title_tag in soup.find_all("a", {"data-testid": "post-title"}):
            titles.append(title_tag.text)

        return titles
      