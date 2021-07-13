# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from ..models import FlashAnim
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.db.models import Q
import logging

# Create your views here.


def retroplayer(request):
   
    filename = request.GET.get('filename')
    category = request.GET.get('category')

    playaddress = "https://famicn-1255835060.file.myqcloud.com/flash/"+category+"/"+filename
    
    return render(request, 'polls/player_retro.html', {'playaddress': playaddress})
