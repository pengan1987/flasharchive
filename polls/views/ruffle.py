# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from ..models import FlashAnim
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.db.models import Q
import logging
from ..models import FlashAnim

# Create your views here.


def ruffle(request):
    animId = request.GET.get('id')
    flashAnim = FlashAnim.objects.get(id=animId)
    category = flashAnim.category
    filename = flashAnim.filename
    chinese_name = flashAnim.chinese_name
    english_name = flashAnim.english_name

    playaddress = "https://famicn-1255835060.file.myqcloud.com/flash/"+category+"/"+filename

    return render(request, 'polls/ruffle.html', {'playaddress': playaddress,
                                                 'chinese_name': chinese_name,
                                                 'english_name': english_name})
