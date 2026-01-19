from django.contrib import admin
from django.utils import timezone
from .models import Receita, PaginaInstitucional, Historia


# ==================================================
# ADMIN DE RECEITAS
# ==================================================

@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    """
    Painel administrativo de Receitas.
    """

    list_display = (
        'titulo',
        'categoria',
        'tempo_preparo',
        'destaque',
        'criada_em',
    )

    list_filter = (
        'categoria',
        'destaque',
        'criada_em',
    )

    search_fields = (
        'titulo',
        'descricao_curta',
        'ingredientes',
    )

    list_editable = (
        'destaque',
    )

    ordering = (
        '-criada_em',
    )

    prepopulated_fields = {
        'slug': ('titulo',)
    }

    fieldsets = (
        (
            '📌 Informações principais',
            {
                'fields': (
                    'titulo',
                    'slug',
                    'categoria',
                    'imagem',
                    'tempo_preparo',
                    'descricao_curta',
                    'destaque',
                )
            }
        ),
        (
            '🧂 Ingredientes',
            {
                'fields': (
                    'ingredientes',
                ),
            }
        ),
        (
            '🍳 Receita',
            {
                'fields': (
                    'modo_preparo',
                ),
            }
        ),
        (
            '📖 História',
            {
                'fields': (
                    'historia',
                ),
            }
        ),
        (
            '🕒 Controle',
            {
                'fields': (
                    'criada_em',
                )
            }
        ),
    )

    readonly_fields = (
        'criada_em',
    )


# ==================================================
# ADMIN DE PÁGINAS INSTITUCIONAIS
# ==================================================

@admin.register(PaginaInstitucional)
class PaginaInstitucionalAdmin(admin.ModelAdmin):
    """
    Admin de páginas institucionais (ex: Sobre).
    """

    list_display = (
        'titulo',
        'slug',
        'atualizado_em',
    )

    search_fields = (
        'titulo',
        'conteudo',
    )

    ordering = (
        'titulo',
    )

    prepopulated_fields = {
        'slug': ('titulo',)
    }

    fieldsets = (
        (
            '📄 Informações da página',
            {
                'fields': (
                    'titulo',
                    'slug',
                )
            }
        ),
        (
            '✍🏾 Conteúdo',
            {
                'fields': (
                    'conteudo',
                ),
            }
        ),
        (
            '🕒 Controle',
            {
                'fields': (
                    'atualizado_em',
                )
            }
        ),
    )

    readonly_fields = (
        'atualizado_em',
    )


# ==================================================
# ADMIN DE HISTÓRIAS — PROTAGONISMO NEGRO
# ==================================================

@admin.register(Historia)
class HistoriaAdmin(admin.ModelAdmin):
    """
    Painel administrativo das Histórias.
    """

    # ============================
    # LISTAGEM
    # ============================
    list_display = (
        'titulo',
        'protagonista',
        'local',
        'publicada',
        'publicada_em',
    )

    list_filter = (
        'publicada',
        'publicada_em',
    )

    search_fields = (
        'titulo',
        'protagonista',
        'resumo',
        'texto',
    )

    ordering = (
        '-publicada_em',
        '-criada_em',
    )

    list_editable = (
        'publicada',
    )

    # ============================
    # SLUG
    # ============================
    prepopulated_fields = {
        'slug': ('titulo',)
    }

    # ============================
    # FORMULÁRIO
    # ============================
    fieldsets = (
        (
            '👩🏾 Protagonista',
            {
                'fields': (
                    'protagonista',
                    'local',
                    'imagem',
                ),
            }
        ),
        (
            '📝 História',
            {
                'fields': (
                    'titulo',
                    'slug',
                    'resumo',
                    'texto',
                ),
            }
        ),
        (
            '🕒 Publicação',
            {
                'fields': (
                    'publicada',
                    'publicada_em',
                ),
                'description': (
                    'Marque como publicada para exibir no site. '
                    'Se a data não for preenchida, ela será definida automaticamente.'
                )
            }
        ),
        (
            'ℹ️ Controle interno',
            {
                'fields': (
                    'criada_em',
                )
            }
        ),
    )

    readonly_fields = (
        'criada_em',
    )

    # ============================
    # COMPORTAMENTO AUTOMÁTICO
    # ============================
    def save_model(self, request, obj, form, change):
        """
        Garante consistência da publicação.
        """
        if obj.publicada and not obj.publicada_em:
            obj.publicada_em = timezone.now()

        if not obj.publicada:
            obj.publicada_em = None

        super().save_model(request, obj, form, change)

    # ============================
    # AÇÕES
    # ============================
    actions = ['publicar_historias']

    def publicar_historias(self, request, queryset):
        """
        Publica histórias em massa.
        """
        queryset.update(
            publicada=True,
            publicada_em=timezone.now()
        )

    publicar_historias.short_description = "Publicar histórias selecionadas"
