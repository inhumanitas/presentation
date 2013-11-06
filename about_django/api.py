# coding: utf-8

from bson import ObjectId
from mongoengine import connect#, disconnect
from about_django.models import Page, AboutDjangoChapter

DB_CONN = None


def connect_to_db():
    global DB_CONN
    if DB_CONN:
        return True

    try:
#        disconnect()
        DB_CONN = connect('about_django')
    except Exception as err:
        print err.message
        return False

    return True


def create_about_django_pages(pages_tpl):
    pages = []
    for page in pages_tpl:
        page_obj = Page()
        page_obj.page_num = page[0]
        page_obj.title = page[1]
        page_obj.body = page[2]
        page_obj.save()
        pages.append(page_obj)
    return pages


def create_about_django_db():
    from about_django.data import about_django_data
    connect_to_db()
    AboutDjangoChapter.objects.filter().delete()
    Page.objects.filter().delete()
    for chapter in about_django_data.keys():
        print chapter
        adc = AboutDjangoChapter()
        adc.chapter = str(chapter)
        adc.pages = create_about_django_pages(about_django_data[chapter])
        adc.save()
    print "created AboutDjangoChapter"


def get_chapters():
    chapters = AboutDjangoChapter.objects().values_list(
        'id', 'chapter')
    return chapters


def get_chapter_titles(chapter_id):
    try:
        chapter = AboutDjangoChapter.objects.get(id=ObjectId(chapter_id))
    except (AboutDjangoChapter.DoesNotExist,
            AboutDjangoChapter.MultipleObjectreturned):
        print "error in get_chapter_titles"
        return []

    if not hasattr(chapter, 'pages'):
        return []

    titles = []
    for page in chapter.pages:
        titles.append([page.id, page.title])

    return titles


def get_page_body(page_id):
    try:
        page = Page.objects.get(id=ObjectId(page_id))
    except (Page.DoesNotExist,
            Page.MultipleObjectsReturned):
        print 'error in get_page_body'
        return []
    return {'title':page.title, 'body':page.body}


connect_to_db()
