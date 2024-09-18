from django.contrib import admin
from .models import (About,
                     Discounts,
                     Service)


admin.site.register(About),
admin.site.register(Discounts),
admin.site.register(Service),
