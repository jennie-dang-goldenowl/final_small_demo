from http.server import ThreadingHTTPServer
from json import JSONDecodeError
from multiprocessing.connection import deliver_challenge
from operator import itemgetter
from turtle import left
from django.db import models

from developers.models import Dev

info_dev = (
    ('Thien Thanh', 'Thien Thanh'),
    ('Phuong Thao', 'Phuong Thao'),
    ('Thanh Liem', 'Thanh Liem'),
    ('Nha Thanh', 'Nha Thanh'),
    ('Phan Oanh', 'Phan Oanh'),
    ('Dinh Kha', 'Dinh Kha'),
    ('Binh Luat', 'Binh Luat'),
    ('Hong Hanh', 'Hong Hanh'),
    ('My Linh', 'My Linh'),
    ('Tuan Le', 'Tuan Le'),
    ('Duy An', 'Duy An'),
    ('Minh Anh', 'Minh Anh'),
    ('Tuan Rider', 'Tuan Rider'),
)

class Projects(models.Model):
    name = models.TextField()
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    dev = models.TextField(
        max_length=50,
        choices= info_dev,
        default= '1'
    )
