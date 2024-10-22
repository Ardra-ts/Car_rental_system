from django.contrib import admin
from rent_app.models import CAR
from .forms import CarForm

class CARAdmin(admin.ModelAdmin):
    form = CarForm

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.user = request.user  # Pass the logged-in user to the form
        return form

admin.site.register(CAR, CARAdmin)
