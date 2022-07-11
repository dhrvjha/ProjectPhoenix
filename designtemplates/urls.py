
from django.contrib.auth.decorators import login_required
from django.urls import path

from designtemplates.views import DesignAddView, DesignListView

urlpatterns = [
    path("", DesignListView.as_view(), name="design_list_view"),
    path("add/", login_required(DesignAddView.as_view()), name="design_add_view")
]
