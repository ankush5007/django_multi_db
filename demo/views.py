from django.shortcuts import render
from django.conf import  settings as conf_settings
from rest_framework import  viewsets,status,generics,mixins,permissions,filters
from django.http import  JsonResponse,HttpResponseNotFound,Http404, request,response
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import api_view,renderer_classes,action,permission_classes,authentication_classes
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .models import *

from django.contrib.auth.models import User,Group
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser,FormParser
from django.db.models import Q
import operator
from functools import reduce
from operator import or_
from django.contrib.auth import authenticate,login,logout
from django.contrib.sessions.models import Session
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.authentication import SessionAuthentication,BaseAuthentication,TokenAuthentication
from django.dispatch import Signal,receiver
#social login