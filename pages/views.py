from django.shortcuts import render, get_object_or_404
from .models import Receita, PaginaInstitucional, Historia


# ==================================================
# PÁGINA INICIAL (HOME)
# ==================================================
def home(request):
    """
    Exibe a página inicial do site.

    REGRAS:
    - Mostra APENAS receitas marcadas como destaque
    - Ordena pelas mais recentes
    """

    receitas_destaque = (
        Receita.objects
        .filter(destaque=True)
        .order_by('-criada_em')
    )

    return render(
        request,
        'pages/home.html',
        {
            'receitas': receitas_destaque,
        }
    )


# ==================================================
# PÁGINA SOBRE
# ==================================================
def sobre(request):
    """
    Página institucional "Sobre".
    Conteúdo gerenciado pelo admin.
    """

    pagina = (
        PaginaInstitucional.objects
        .filter(slug='sobre')
        .first()
    )

    return render(
        request,
        'pages/sobre.html',
        {
            'pagina': pagina,
        }
    )


# ==================================================
# PÁGINA RECEITAS (LISTAGEM GERAL)
# ==================================================
def receitas(request):
    """
    Página principal de receitas.
    """

    receitas = Receita.objects.all().order_by('-criada_em')

    return render(
        request,
        'pages/receitas.html',
        {
            'receitas': receitas,
            'categoria_nome': 'Todas as Receitas',
        }
    )


# ==================================================
# PÁGINA RECEITAS POR CATEGORIA
# ==================================================
def receitas_categoria(request, categoria):
    """
    Exibe receitas filtradas por categoria.
    """

    categorias = {
        'tradicao-baiana': 'Tradição Baiana',
        'terreiro': 'Receitas de Terreiro',
        'ancestral': 'Receitas Ancestrais',
    }

    categoria_nome = categorias.get(categoria, 'Receitas')

    receitas = (
        Receita.objects
        .filter(categoria=categoria)
        .order_by('-criada_em')
    )

    return render(
        request,
        'pages/receitas.html',
        {
            'receitas': receitas,
            'categoria_nome': categoria_nome,
        }
    )


# ==================================================
# PÁGINA DETALHE DA RECEITA
# ==================================================
def receita_detalhe(request, slug):
    """
    Página individual da receita.
    """

    receita = get_object_or_404(
        Receita,
        slug=slug
    )

    return render(
        request,
        'pages/receita_detalhe.html',
        {
            'receita': receita,
        }
    )


# ==================================================
# PÁGINA HISTÓRIAS (LISTAGEM)
# ==================================================
def historias(request):
    """
    Listagem de histórias publicadas
    de mulheres negras protagonistas.
    """

    historias = (
        Historia.objects
        .filter(publicada=True)
        .order_by('-publicada_em', '-criada_em')
    )

    return render(
        request,
        'pages/historias.html',
        {
            'historias': historias,
        }
    )


# ==================================================
# PÁGINA DETALHE DA HISTÓRIA
# ==================================================
def historias_detalhe(request, slug):
    """
    Página individual da história.
    Apenas histórias publicadas.
    """

    historia = get_object_or_404(
        Historia,
        slug=slug,
        publicada=True
    )

    return render(
        request,
        'pages/historias_detalhe.html',
        {
            'historia': historia,
        }
    )
