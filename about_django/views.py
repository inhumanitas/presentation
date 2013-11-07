# coding: utf-8

from django.template import RequestContext, Context
from django.views.generic.base import View
from django.shortcuts import render_to_response
from django.utils import simplejson
from django.http import HttpResponse

from about_django.api import (
    get_chapters, get_chapter_titles, get_page_body)

from about_django.models import AboutDjangoChapter


def index(request):
    chapters = get_chapters()
    data = {}
    print chapters
    for chapter_id, chapter in chapters:
        print chapter_id, chapter
        titles = get_chapter_titles(chapter_id)
        data[chapter] = titles

    context = Context({"chapters":sorted(data.iteritems())})
    return render_to_response('index.html', context,
                              context_instance = RequestContext(request))


def get_body(request):
    data = []
    if request.method == "GET":
        page_id = request.GET.get("page_id", "")
        print 'page_id', page_id
        if page_id:
            data = get_page_body(page_id)
            # to json object
            data = simplejson.dumps(data)
            print sorted(data)
    return HttpResponse(data, mimetype = 'application/json')


class GetBody(View):
    def get(self, request):
        data = []
        if request.method == "GET":
            page_id = request.GET.get("page_id", "")
            print 'page_id', page_id
            if page_id:
                data = get_page_body(page_id)
                # to json object
                data = simplejson.dumps(data)
                print data
        return HttpResponse(data)
