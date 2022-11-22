
from django import template
register = template.Library()

@register.filter(name='ajeitaHora')
def ajeitaHora(obj):

        from datetime import time, timedelta        
        from django.utils.timezone import localtime        
        import pytz

        local_tz = pytz.timezone('Etc/GMT+1')
        
        time_str = localtime(obj.replace(tzinfo=local_tz)).strftime("%H:%M")

        # start_date = local_tz.localize(datetime(2012, 9, 27), is_dst=None)
        # now_utc = datetime.utcnow().replace(tzinfo=pytz.utc)

        print(time_str)
        return 'obj-c'

