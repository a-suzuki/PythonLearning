# -*- coding: utf-8 -*-

import os

from bottle import route, run, template, request
from bottle import TEMPLATE_PATH
from bottle import static_file
from pybot import pybot
 
# index.pyが設置されているディレクトリの絶対パスを取得
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# テンプレートファイルを設置するディレクトリのパスを指定
TEMPLATE_PATH.append(BASE_DIR + "/views")

@route('/css/<filename>')
def css_dir(filename):
    """ set css dir """
    return static_file(filename, root=BASE_DIR+"/static/css")
 
@route('/js/<filename>')
def js_dir(filename):
    """ set js dir """
    return static_file(filename, root=BASE_DIR+"/static/js")
 
@route('/img/<filename>')
def img_dir(filename):
    """ set img file """
    return static_file(filename, root=BASE_DIR+"/static/img")
 
@route('/font/<filename>')
def font_dir(filename):
    """ set font file """
    return static_file(filename, root=BASE_DIR+"/static/fonts")

@route('/hello')
def hello():
    return template('pybot_template', input_text='', output_text='')

@route('/hello', method='POST')
def do_hello():
    input_text = request.forms.input_text
    output_text = pybot(input_text)
    return template('pybot_template', input_text=input_text, output_text=output_text)

run(host='localhost', port=8090, debug=True)
