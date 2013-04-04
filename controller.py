# -*- coding: utf-8 -*-

from bottle import Bottle,request,jinja2_template as template,static_file,debug,HTTPError
import settings
from models import *
app = Bottle()
debug(False)
@app.route('/')
@app.route('/index')
@app.route('/page/<page:re:[0-9]+>')
def index(page='1'):
    page = int(page)
    entries = []
    
    results = Picture.raw('''SELECT * FROM Picture AS r1 JOIN
        (SELECT ROUND(RAND() *
        (SELECT MAX(id)
        FROM Picture)) AS _id)
        AS r2
        WHERE r1.id >= r2._id
        ORDER BY r1.id ASC
        LIMIT 10; ''')
    if  results is None:
        HTTPError(404, 'page not found')

    for i in results:
        print i.index
        
    return template("static/template/index.html",entries=results,pagenavi=page)


@app.route('/image/<id:re:[0-9]+>')
def detail(id):
    id = int(id)

    try:
        entry = Picture.select().where(Picture.id == id).get()
    except Exception,e:
        return HTTPError(404, 'page not found')

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

    
