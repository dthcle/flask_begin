from flask import Flask
from flask import render_template
from flask import Markup
from flask import redirect
from flask import request
# from flask import url_for

from static import constant
# from article import Article
import sqlite3

# from urllib.parse import unquote

app = Flask(__name__)
info = constant.Info()


# 主界面
@app.route('/')
def index_page():
    conn = sqlite3.connect('./data/blog.db')
    c = conn.cursor()
    article_list = c.execute('SELECT * FROM main.article').fetchall()
    article_content_list = []
    for each_article in article_list:
        article_content_list.append(each_article[2][:20]+'......')
    conn.close()
    return render_template('index.html', article_list=article_list, article_content_list=article_content_list
                           , footer=Markup(info.footer), background_image_address=Markup(info.background_image_address))


# 文章界面
@app.route('/article/<article_name>')
def get_article(article_name):
    conn = sqlite3.connect('./data/blog.db')
    c = conn.cursor()
    article = c.execute('SELECT * FROM main.article WHERE title = ?', (article_name, )).fetchone()
    conn.close()
    return render_template('article.html', article_title=article[1]
                           , article_content=Markup(article[2].replace('\n', '<br>'))
                           , footer=Markup(info.footer), background_image_address=Markup(info.background_image_address)
                           , image_address=Markup(article[4]))


# 登陆界面
@app.route('/login_now')
def login():
    return render_template('login.html')


# 跳转界面
@app.route('/redirect', methods=['POST'])
def redirect_to_admin():
    conn = sqlite3.connect('./data/blog.db')
    c = conn.cursor()
    if request.form['id_username'] in c.execute('SELECT username FROM user').fetchall() \
            and request.form['id_password'] == \
            c.execute('SELECT password FROM user WHERE username = \'?\'', (request.form['id_username'],)):
        conn.close()
        return redirect('/dthclesama')
    else:
        conn.close()
        return redirect('/wrong_information')


# 账号或密码错误跳转界面
@app.route('/wrong_information')
def wrong_information():
    return render_template('wrong_information.html')


# 管理界面
@app.route('/dthclesama', methods=['POST', 'GET'])
def admin():
    return render_template('admin.html')


# # 网址中带有变量名
# @app.route('/home/<username>')
# def web_home(username):
#     return 'Hello, %s' % username


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

    # conn = sqlite3.connect('./data/blog.db')
    # c = conn.cursor()

    # create_table = '''CREATE TABLE article
    # (
    #     ID        int            primary key        not null  ,
    #     title     varchar(10)                                 ,
    #     content   text                                        ,
    #     label     varchar(10)
    # );
    # '''

    # create_admin_table = '''CREATE TABLE user
    # (
    #     ID         INT         PRIMARY KEY      NOT NULL ,
    #     username   char(20)    NOT NULL ,
    #     password   char(30)    NOT NULL
    # )
    # '''

    # alter = '''ALTER TABLE article ADD COLUMN image_address char(60)'''

    # insert = '''INSERT INTO main.article (ID, title, content, image_address) VALUES \
    # (1, 'Beginning!' , '哈哈哈，第一篇博客！\n庆祝博客上线！来张色图开森一哈！' \
    # , 'https://i.loli.net/2018/09/18/5ba0c5c461fcc.jpg')
    # '''

    # insert_admin = '''INSERT INTO main.user (ID, username, password) VALUES \
    # (0, 'dthcle', 'dthclesama')
    # '''

    # delete = '''DELETE FROM main.article WHERE ID = 2'''

    # update = '''UPDATE article SET title = 'Beginning of all' WHERE ID = 1'''

    # select = '''SELECT * FROM article'''
    # article_list = c.execute(select).fetchmany(1)

    # c.execute(delete)
    # conn.commit()
    # conn.close()

