from flask import Flask
from flask import render_template
from flask import Markup
from flask import redirect
from flask import request
# from flask import url_for

from static import constant
from article import Article

app = Flask(__name__)
info = constant.Info()


# 主界面
@app.route('/')
def index_page():
    return render_template('index.html', article_content=Markup('第一段<br>第二段<br>第三段')
                           , footer=Markup(info.footer), background_image_address=Markup(info.background_image_address))


# 文章界面
@app.route('/article/<article_name>')
def get_article(article_name):
    article = Article.load_article(article_name)
    return render_template('article.html', article_title=article.title
                           , article_content=Markup(article.content.replace('\n', '<br>'))
                           , footer=Markup(info.footer), background_image_address=Markup(info.background_image_address))


# 登陆界面
@app.route('/login_now')
def login():
    return render_template('login.html')


# 跳转界面
@app.route('/redirect', methods=['POST'])
def redirect_to_admin():
    if request.form['id_username'] == info.username and request.form['id_password'] == info.password:
        return redirect('/dthclesama')
    else:
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
