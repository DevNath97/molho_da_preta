# 🍲 Molho da Preta

> *“Aqui, cada receita carrega uma história.  
> Cada história carrega uma ancestralidade.”*

Molho da Preta é uma plataforma web desenvolvida em **Django** com o objetivo de valorizar a culinária afro-brasileira e dar visibilidade a histórias de protagonismo feminino no universo da gastronomia.

Este projeto faz parte do meu portfólio e foi desenvolvido com foco em identidade cultural, acessibilidade e experiência do usuário.

---

## 🖼️ Demonstração visual

> 📌 *O projeto ainda não está em produção. As imagens abaixo mostram a versão local.*

### Página Inicial

![Home](docs/images/home.png)

### Página de Receitas

![Receitas](docs/images/receitas.png)

### Página de Histórias

![Histórias](docs/images/historias.png)

### Página Sobre

![Sobre](docs/images/sobre.png)

---

## 🎯 Objetivo do Projeto

O Molho da Preta foi criado para:

- Divulgar **receitas afro-brasileiras**
- Compartilhar **histórias de mulheres negras protagonistas**
- Preservar e valorizar a cultura, identidade e memória ancestral
- Criar um espaço comunitário, afetivo e colaborativo

A proposta vai além da culinária: é sobre **representatividade, memória e pertencimento**.

---

## 👥 Público-alvo

- Homens e mulheres da comunidade negra  
- Idade a partir de 30 anos  
- Sem necessidade de conhecimento técnico  
- Acesso via **celular e computador**

---

## 🧭 Estrutura do Site

Páginas implementadas:

- Home  
- Sobre  
- Contato  
- Receitas  
- Histórias  
- Login / Cadastro  
- Painel administrativo (Django Admin)

---

## ⚙️ Funcionalidades

- Listagem de receitas com imagens e categorias  
- Listagem de histórias com destaque editorial  
- Sistema de usuários com perfis diferenciados  
- Formulários de contato  
- Envio de e-mails  
- Painel administrativo customizado para gestão de conteúdo  

---

## 🎨 Identidade Visual

### Conceito

- Afro-brasileira  
- Feminina e potente  
- Afetiva e comunitária  
- Cultural e contemporânea  

Palavras-chave:  
**Ancestralidade · Calor · Terra · Sabor · Comunidade · Protagonismo**

### Paleta de cores

| Uso | Cor | Hex |
|-----|-----|-----|
| Primária (Terra) | Marrom escuro | `#4B2E1E` |
| Secundária (Dendê) | Vermelho queimado | `#A63A2A` |
| Destaque | Amarelo quente | `#E0A100` |
| Fundo | Bege / Off-white | `#F5EFE6` |
| Apoio | Verde escuro | `#2F5D50` |

### Tipografia

- Títulos: *Playfair Display*, *Libre Baskerville*, *Cormorant Garamond*  
- Texto: *Montserrat*, *Poppins*, *Lato*  

Foco em:

- Boa leitura em mobile  
- Alto contraste  
- Fontes generosas (público +30)

---

## ♿ Acessibilidade

- Contraste AA/AAA  
- Fontes legíveis  
- Botões grandes  
- Navegação simples  
- Linguagem clara  

A acessibilidade foi tratada como requisito essencial, não opcional.

---

## 🛠️ Tecnologias Utilizadas

- Python 3  
- Django 6.0  
- HTML5  
- CSS3 (customizado, sem frameworks pesados)  
- JavaScript básico  
- SQLite (ambiente de desenvolvimento)

---

## 🚀 Como rodar o projeto localmente

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/molho-da-preta.git

# Entre na pasta
cd molho-da-preta

# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Rode as migrações
python manage.py migrate

# Inicie o servidor
python manage.py runserver
