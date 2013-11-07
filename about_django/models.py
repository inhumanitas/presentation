# coding: utf-8

from mongoengine import (
    StringField, ReferenceField, Document, ListField,
    IntField, CASCADE)


class Page(Document):
    page_num = IntField()
    title = StringField(required=True, max_length=50)
    body = StringField(max_length=1250)


class AboutDjangoChapter(Document):
    chapter = StringField(max_length=550)
    pages = ListField(ReferenceField(
        Page, reverse_delete_rule=CASCADE))
