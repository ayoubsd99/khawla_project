from django.shortcuts import render

# Create your views here.
import string
import random

def _grf(length):
    letters = string.hexdigits
    return ''.join(random.choice(letters) for i in range(length))