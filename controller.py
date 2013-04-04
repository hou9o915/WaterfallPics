# -*- coding: utf-8 -*-

from bottle import Bottle,request,jinja2_template as template,static_file,debug
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
    
    results = Picture.raw('''SELECT * FROM Picture AS r1 JOIN
        (SELECT ROUND(RAND() *
        (SELECT MAX(id)
        FROM Picture)) AS id)
        AS r2
        WHERE r1.id >= r2.id
        ORDER BY r1.id ASC
        LIMIT 10; ''')
    if  results is not None:
	   for entry in results:
        	entries.append({'id':entry.id,'name':entry.img_url,"index":entry.index})
        
    return template("static/template/index.html",entries=entries,pagenavi=page)


@app.route('/image/<index:re:[0-9]+>')
def detail(index):
    index = int(index)

    entry = Picture.select().where(Picture.index == index).get()

    return template("static/template/detail.html",entry=entry)



@app.route('/static/style/:filename')
def route_css(filename):
    return static_file(filename,'static/style/')

@app.route('/static/img/:filename')
def route_img(filename):
    return static_file(filename,'static/img/')

@app.route('/static/js/:filename')
def route_js(filename):
    return static_file(filename,'static/js/')

    
