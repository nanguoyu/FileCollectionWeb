# coding=utf-8
from datetime import datetime
from flask import url_for, redirect, session, render_template, request, jsonify
import logging
import time
from mdb import ActivationCodeProducer
from . import main
from flask_qiniu import Qiniu

logging.basicConfig(filename=time.strftime("%Y-%m-%d", time.localtime()) + 'fileshare.log', level=logging.DEBUG)
logging.info(time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime()) + 'file upload  start')
qiniu_store = Qiniu()
activation_code_producer = ActivationCodeProducer()


@main.route('/', methods=['GET', 'POST'])
def index():
    # form = log_on_form()
    # if form.validate_on_submit():
    #     uid = form.uid.data
    #     password = form.password.data
    #     resultJson = result2json(query2json(user_confirm_query(uid=uid, password=password)))
    #     if len(resultJson) == 1:
    #         session['uid'] = uid
    #         session['name'] = resultJson[0][2]
    #         # 这里验证用户账户
    #         return redirect(url_for('main.dashboard'))
    #     elif len(resultJson) == 0:
    #         return render_template('/index.html', form=form)

    return render_template('/index.html')


@main.route('/save', methods=['GET', 'POST'])
def save():
    data = request.files['kartik-input-700']
    code = activation_code_producer.activation_code(6)
    filename = code + '_' + data.filename
    ret, info = qiniu_store.save(data, filename)
    logging.info(time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime()) + "save" + filename)
    logging.info(time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime()) + str(ret) + ' ' + str(info))
    return jsonify(code)

# class log_on_form(Form):
#     uid = StringField(U'帐号', validators=[DataRequired()])
#     password = PasswordField(U'密码', validators=[DataRequired()])
#     submit = SubmitField(U'登录')
