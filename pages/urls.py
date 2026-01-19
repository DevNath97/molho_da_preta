from django.urls import path
from . import views

# ==================================================
# ROTAS DO APP PAGES
# ==================================================

urlpatterns = [

    # ============================
    # HOME
    # ============================
    path(
        "",
        views.home,
        name="home"
    ),

    # ============================
    # PÁGINAS INSTITUCIONAIS
    # ============================
    path(
        "sobre/",
        views.sobre,
        name="sobre"
    ),

    # ============================
    # HISTÓRIAS
    # ============================
    path(
        "historias/",
        views.historias,
        name="historias"
    ),

    path(
        "historias/<slug:slug>/",
        views.historias_detalhe,
        name="historias_detalhe"
    ),

    # ============================
    # RECEITAS
    # ============================
    path(
        "receitas/",
        views.receitas,
        name="receitas"
    ),

    path(
        "receitas/receita/<slug:slug>/",
        views.receita_detalhe,
        name="receita_detalhe"
    ),

    path(
        "receitas/<slug:categoria>/",
        views.receitas_categoria,
        name="receitas_categoria"
    ),
]
