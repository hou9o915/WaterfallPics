# -*- coding: utf-8 -*-

from lib.bottle import Bottle,request,jinja2_template as template,static_file,debug
import settings
from models import *
app = Bottle()
debug(True)
@app.route('/')
@app.route('/index')
@app.route('/page/<page:re:[0-9]+>')
def index(page='1'):
    page = int(page)
    entries = []
    
    results = Picture.select().offset(page*10+1).limit(10)
    if  results is not None:
	   for entry in results:
        	entries.append({'id':entry.id,'name':entry.img_url})
        
    return template("static/template/index.html",entries=entries,pagenavi=page)



@app.route('/static/style/:filename')
def route_css(filename):
    return static_file(filename,'static/style/')

@app.route('/static/img/:filename')
def route_img(filename):
    return static_file(filename,'static/img/')

@app.route('/static/js/:filename')
def route_js(filename):
    return static_file(filename,'static/js/')

    
