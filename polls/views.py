# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import FlashAnim
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.db.models import Q
import logging

# Create your views here.


def index(request):
    flashAnim_list = FlashAnim.objects.all()

    page = request.GET.get('page')
    datesort = request.GET.get('sort')
    keyword = request.GET.get('keyword')
    category = request.GET.get('category')

    change_order_link = ""
    paging_link_tail = ""
    if category:
        change_order_link += ("&category=" + category)
        paging_link_tail += ("&category=" + category)
    if datesort:
        paging_link_tail += ("&sort=" + datesort)
    if keyword:
        change_order_link += ("&keyword=" + keyword)
        paging_link_tail += ("&keyword=" + keyword)
    if page:
        change_order_link += ("&page=" + page)

    change_order_link += "&sort=date_asc" if datesort == 'date_desc' else '&sort=date_desc'
    change_order_link = change_order_link.replace("&", "?", 1)
    logging.warning(change_order_link)

    if category:
        flashAnim_list = flashAnim_list.filter(category__startswith=category)

    if keyword:
        flashAnim_list = flashAnim_list.filter(Q(english_name__icontains=keyword)|Q(chinese_name__icontains=keyword))

    paginator = Paginator(flashAnim_list, 50)

    try:
        flashAnim = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        flashAnim = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        flashAnim = paginator.page(paginator.num_pages)

    index = flashAnim.number - 1
    max_index = len(paginator.page_range)

    start_index = index - 4 if index >= 4 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index

    page_range = list(paginator.page_range)[start_index:end_index]

    return render(request, 'polls/list.html', {'flashAnim': flashAnim,
                                               "page_range": page_range,
                                               "paging_link_tail": paging_link_tail,
                                               "change_order_link": change_order_link})
