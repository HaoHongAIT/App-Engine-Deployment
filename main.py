import math

from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from app import utils, app, login_manager
from app.analysis import Analysis


@app.context_processor
def common_response():
    return {
        'categories': utils.load_categories()
    }


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/news/<int:category_id>/', methods=['GET', 'POST'])
def news_list(category_id=0):
    category_name = {0: " ", 1: "Lúa Gạo", 2: "Cà Phê", 3: "Cao Su"}
    page = request.args.get('page', 1)
    kw = request.args.get('keyword')
    news = utils.load_news(category_id=category_id, page=int(page), keyword=kw)
    counter = utils.count_news(category_id)
    return render_template('news.html',
                           category_name=category_name[category_id],
                           cate_id=category_id,
                           news=news,
                           pages=math.ceil(counter / app.config['PAGE_SIZE']))


@app.route('/read/')
def read():
    return render_template('read.html')


@app.route('/login', methods=['get', 'post'])
def user_signin():
    error_msg = ""
    if request.method.__eq__('POST'):  # check method
        username = request.form.get('username')  # get value from form
        password = request.form.get('password')
        user = utils.check_login(username, password)  # check  (user, pass) match  between form submit and database
        if user:
            login_user(user=user)
            return redirect(url_for('index'))  # direct to index.html
        else:
            error_msg = "Wrong password or username"  # assign variable to show error
    return render_template('login.html', error_msg=error_msg)


@login_manager.user_loader
def user_load(user_id):
    return utils.get_user_by_id(user_id=user_id)


@app.route('/logout')
def user_logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['get', 'post'])
def user_signup():
    error_msg = ""
    if request.method.__eq__('POST'):
        name = str(request.form.get('name')).strip()
        username = str(request.form.get('username')).strip()
        password = str(request.form.get('password')).strip()
        email = str(request.form.get('email')).strip()
        confirm = str(request.form.get('confirm')).strip()
        try:
            if password.__eq__(confirm):
                utils.add_user(name=name, username=username, password=password, email=email)
                return redirect(url_for('user_signin'))
            else:
                error_msg = "Mật khẩu xác nhận không khớp, vui lòng kiểm tra lại"
        except Exception as ex:
            error_msg = "Error: " + str(ex)
    return render_template('register.html', error_msg=error_msg)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')


@app.route('/analysis', methods=['GET', 'POST'])
def analysis():
    if current_user.is_authenticated:
        return render_template('login.html')

    if request.method.__eq__('POST'):
        news_sentence = f"{request.form['headline']} {request.form['brief']}"  # Get review from input
        model = Analysis(api_key="YOUR API KEY")
        final_output = model.get_response(news_sentence)
        return render_template("analysis.html",
                               predict=final_output)
    else:
        return render_template("analysis.html")


if __name__ == '__main__':
    app.run(debug=True)
