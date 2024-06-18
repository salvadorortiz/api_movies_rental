workon apis
python manage.py runserver
localhost:8000



https://github.com/jazzband/django-auditlog/blob/master/docs/source/usage.rst
https://django-auditlog.readthedocs.io/en/latest/usage.html

pip install django-auditlog
manage.py migrate


path /Users/salvadorortiz/apis/lib/python3.8/site-packages/auditlog/ for JSONField conflict

from jsonfield import JSONField
field = JSONField(max_length=200)