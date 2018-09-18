import pickle
import os


class Article:
    def __init__(self, title='Default Title', content='Default Content\nParagraph 1\nParagraph 2'):
        self.title = title
        self.content = content

    def save_article(self):
        with open('./data/'+self.title+'.art', 'wb') as art:
            pickle.dump(self, art, protocol=True)

    @staticmethod
    def load_article(article_title):
        with open('./data/'+article_title+'.art', 'rb') as art:
            tmp_art = pickle.load(art)
        return tmp_art

    @staticmethod
    def load_articles():
        os.chdir('./data')
        dirs = os.listdir(os.getcwd())
        os.chdir('..')
        return dirs



