from django.contrib import admin

# Register your models here.
from .models import Stock1
from .models import UserProfile
from .models import Useer
from .models import Dummy
admin.site.register(Stock1)
admin.site.register(UserProfile)
admin.site.register(Useer)

admin.site.register(Dummy)