from app import app
from flask import render_template, flash, redirect
from app.forms.postForm import PostForm
import requests
from func_pack import create_rec_hash, get_current_time, get_api_info
from config import Config
# 内存泄露函数
from exhaust_mem import exhaust_mem


@app.route('/memory-err-injection', methods=['POST'])
def post():
    form = PostForm()
    # 处理 POST 的逻辑
    if form.validate_on_submit():
        # 点击发言按钮后, 注入 500mb 的内存泄露
        exhaust_mem()
        flash('Memory injection success! Injection 500Mb to RAM.')
        return redirect('/memory-err-injection')


# 获取最新评论消息
@app.route('/memory-err-injection', methods=['GET'])
def welcome():
    form = PostForm()
    queries_list = [
        {
            "Username": "Leon_Tian",
            "Post": "Click the button upside and you can inject 500mb to you RAM.",
            "PostTime": "2019-04-27/15:34:09"
        }
    ]
    # 处理 GET 的逻辑
    return render_template('frontPage.html', title='Memory Err Injection', comments=queries_list, form=form)
    pass
#
#
# # 获取 username 为 admin 的用户所发出的信息
# @app.route('/announcement', methods=['GET'])
# def announcement():
#     query_url = 'http://' + Config.DB_CONNECTOR_URL + '/queries/' + 'Administer'
#     # 获取最新的 comments 信息
#     result = requests.get(query_url)
#     queries_list = get_api_info(result)
#     # 逆序，将最新的留言放置最前
#     queries_list.reverse()
#     # 处理 GET 的逻辑
#     return render_template('announcement.html', title='Rules', comments=queries_list)
#     pass


