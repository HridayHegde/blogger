from django.shortcuts import render
from  blogging.models import *
# Create your views here.
import sys
import logging

logger = logging.getLogger(__name__)


def HomePage(request):
    try:
        user = UserDetails.objects.all()[0]
        blogs = BlogPost.objects.all()
        print(blogs)
        return render(request,'blogging/index.html', {'blogs':blogs, 'user':user})
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.error("HomePage %s at line %s",str(e),str(exc_tb.tb_lineno))
