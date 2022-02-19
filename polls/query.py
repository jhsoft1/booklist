from polls.models import *
from django.db.models import F
Voter.objects.annotate(value=F('vote__value'), year=F('vote__year')).values('name', 'value', 'year')
