#!/usr/bin/env python
#-*-coding:UTF-8-*-

from peewee import *
from settings import *

db = MySQLDatabase(MYSQL_DB, user=MYSQL_USER,passwd=MYSQL_PASSWORD)


class BaseModel(Model):
    class Meta:
        database = db


class Picture(BaseModel):
	index = IntegerField(unique=True)
	img_url = CharField()

	def __unicode__(self):
		return "id:%-6d  index:%-6d img:%s"%(self.id,self.index,self.img_url)


if __name__ == '__main__':
    db.connect()
    for p in Picture.select().offset(0).limit(10).desc():
    	print p
