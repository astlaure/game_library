from django.views.generic.list import ListView
from . import models


class GameListView(ListView):
    template_name = 'games/index.html'
    model = models.Game
    paginate_by = 20
    context_object_name = 'games'
    ordering = ["id"]
