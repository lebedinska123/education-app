from django.shortcuts import render
from .models import Content, Section
from django.http import Http404, HttpResponseRedirect, HttpResponse
import pytils.translit as translit

# Create your views here.
def index(request):
    try:
        sections = Section.objects.all()
    except:
        raise Http404("Ошибка")

    return render(request, 'main_page.html', {'sections':sections})

def section(request, section_id):
    try:
        items = Content.objects.filter(section_id=section_id)
        section_name = Section.objects.get(id = section_id)
        authors_list = Content.objects.filter(section_id=section_id).values('author').distinct()
    except:
        raise Http404('Страница не найдена')

    if(authors_list):
        for i in authors_list:
            i['author_link'] = translit.translify('_'.join(i['author'].split(' ')))
            print(i)

    return render(request, 'section_page.html', {'items':items, 'section_id':section_id, 'section_name':section_name, 'authors_list':authors_list})


def detail(request, section_id, content_id):
    try:
        info = Content.objects.get(id = content_id)
    except:
        raise Http404('Страница не найдена')

    return render(request, 'info.html', {'info':info, 'section_id':section_id})

def author_filter(request, section_id, author_filter):
    try:
        items = Content.objects.filter(section_id=section_id, author = author_filter)
        section_name = Section.objects.get(id = section_id)
        authors_list = Content.objects.filter(section_id=section_id).values('author').distinct()
    except:
        raise Http404('Страница не найдена')

    return render(request, 'section_page.html', {'items':items, 'section_id':section_id, 'section_name':section_name, 'authors_list':authors_list})

def date_filter(request, section_id):
    date = request.POST['calendar']
    print('date: ', date)
    try:
        items = Content.objects.filter(section_id=section_id, pub_date = date)
        section_name = Section.objects.get(id = section_id)
        authors_list = Content.objects.filter(section_id=section_id).values('author').distinct()
    except:
        raise Http404('Страница не найдена')
    return render(request, 'section_page.html', {'items':items, 'section_id':section_id, 'section_name':section_name, 'authors_list':authors_list})

def title_filter(request, section_id):
    title = request.POST['title']
    print('----- title: ', title)
    # flag = request.POST['flag']
    try:
        items = Content.objects.filter(section_id = section_id, title__icontains = title)
        section_name = Section.objects.get(id = section_id)
        authors_list = Content.objects.filter(section_id=section_id).values('author').distinct()
    except:
        raise Http404('Страница не найдена')

    return render(request, 'section_page.html', {'items':items, 'section_id':section_id, 'section_name':section_name, 'authors_list':authors_list})