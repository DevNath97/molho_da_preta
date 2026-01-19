from django.db import models
from django.utils import timezone


# ==================================================
# RECEITAS
# ==================================================
class Receita(models.Model):
    """
    Model principal de receitas do site Molho da Preta.
    """

    CATEGORIAS = [
        ('tradicao-baiana', 'Tradição Baiana'),
        ('terreiro', 'Receita de Terreiro'),
        ('ancestral', 'Receita Ancestral'),
    ]

    titulo = models.CharField(
        max_length=100,
        verbose_name='Título'
    )

    slug = models.SlugField(
        unique=True,
        verbose_name='Slug (URL)'
    )

    categoria = models.CharField(
        max_length=50,
        choices=CATEGORIAS,
        default='tradicao-baiana',
        verbose_name='Categoria'
    )

    tempo_preparo = models.PositiveIntegerField(
        verbose_name='Tempo de preparo (minutos)'
    )

    descricao_curta = models.CharField(
        max_length=150,
        verbose_name='Descrição curta'
    )

    imagem = models.ImageField(
        upload_to='receitas/',
        verbose_name='Imagem da receita'
    )

    ingredientes = models.TextField(
        verbose_name='Ingredientes',
        blank=True
    )

    modo_preparo = models.TextField(
        verbose_name='Modo de preparo',
        blank=True
    )

    historia = models.TextField(
        verbose_name='História / Contexto cultural',
        blank=True
    )

    destaque = models.BooleanField(
        default=False,
        verbose_name='Receita em destaque'
    )

    criada_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criada em'
    )

    class Meta:
        ordering = ['-criada_em']
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'

    def __str__(self):
        return self.titulo


# ==================================================
# PÁGINAS INSTITUCIONAIS
# ==================================================
class PaginaInstitucional(models.Model):
    """
    Páginas institucionais editáveis pelo admin.
    Exemplo: Sobre
    """

    titulo = models.CharField(
        max_length=150,
        verbose_name='Título'
    )

    slug = models.SlugField(
        unique=True,
        verbose_name='Slug (URL)'
    )

    conteudo = models.TextField(
        verbose_name='Conteúdo'
    )

    atualizado_em = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em'
    )

    class Meta:
        verbose_name = 'Página Institucional'
        verbose_name_plural = 'Páginas Institucionais'

    def __str__(self):
        return self.titulo


# ==================================================
# HISTÓRIAS — PROTAGONISMO NEGRO
# ==================================================
class Historia(models.Model):
    """
    Histórias de mulheres negras protagonistas
    na gastronomia, cultura e empreendedorismo.
    """

    titulo = models.CharField(
        max_length=200,
        verbose_name='Título da história'
    )

    slug = models.SlugField(
        unique=True,
        verbose_name='Slug (URL)'
    )

    protagonista = models.CharField(
        max_length=150,
        verbose_name='Nome da protagonista'
    )

    local = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Local / Território'
    )

    imagem = models.ImageField(
        upload_to='historias/',
        verbose_name='Imagem da protagonista',
        blank=True,
        null=True
    )

    resumo = models.TextField(
        verbose_name='Resumo (para listagem)',
        blank=True
    )

    texto = models.TextField(
        verbose_name='Texto completo da história'
    )

    # ============================
    # CONTROLE DE PUBLICAÇÃO
    # ============================
    publicada = models.BooleanField(
        default=True,
        verbose_name='Publicada'
    )

    publicada_em = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Data de publicação'
    )

    criada_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criada em'
    )

    class Meta:
        ordering = ['-publicada_em', '-criada_em']
        verbose_name = 'História'
        verbose_name_plural = 'Histórias'

    def save(self, *args, **kwargs):
        """
        Garante que a data de publicação seja definida
        automaticamente quando a história for publicada.
        """
        if self.publicada and not self.publicada_em:
            self.publicada_em = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo
