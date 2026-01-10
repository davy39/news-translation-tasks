---
title: Comment intégrer Tailwind avec Django – Avec des exemples de code
subtitle: ''
author: Abhijeet Dave
co_authors: []
series: null
date: '2024-11-05T13:52:23.556Z'
originalURL: https://freecodecamp.org/news/how-to-integrate-tailwind-with-django
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1730270888412/a440ff74-6e8b-4879-8b47-15aedca45bc4.png
tags:
- name: tailwind
  slug: tailwind
- name: Django
  slug: django
seo_title: Comment intégrer Tailwind avec Django – Avec des exemples de code
seo_desc: Integrate Tailwind CSS with Django using this step-by-step guide to enhance
  your web application's appearance and development efficiency.
---

Dans le développement web moderne, choisir la bonne technologie est crucial car cela impacte à la fois le processus et le résultat de vos projets. Utiliser Django comme framework backend et Tailwind CSS comme framework CSS utilitaire offre une manière efficace de créer des applications web réactives et visuellement attrayantes.

Cet article expliquera pourquoi Django et Tailwind CSS fonctionnent bien ensemble, comment démarrer un projet Django, comment ajouter facilement Tailwind CSS, et comment accélérer votre développement avec Prettier pour une meilleure mise en forme des classes.

## Table des matières

* [Aperçu rapide de Django](#heading-aperçu-rapide-de-django)
    
* [Qu'est-ce que Tailwind CSS ?](#heading-quest-ce-que-tailwind-css)
    
* [Pourquoi Django et Tailwind fonctionnent si bien ensemble ?](#heading-pourquoi-django-et-tailwind-fonctionnent-si-bien-ensemble)
    
* [Comment initialiser un projet Django ?](#heading-comment-initialiser-un-projet-django)
    
* [Comment intégrer Tailwind CSS avec Django ?](#heading-comment-integrer-tailwind-css-avec-django)
    
* [Créons une application de bulle de chat.](#heading-creons-une-application-de-bulle-de-chat)
    
* [Comment utiliser Prettier pour la mise en forme des classes ?](#heading-comment-utiliser-prettier-pour-la-mise-en-forme-des-classes)
    
* [Comment créer une bulle de chat en utilisant les composants FlyonUI Tailwind et Django](#heading-comment-creer-une-bulle-de-chat-en-utilisant-les-composants-flyonui-tailwind-et-django)
    
* [Conclusion](#heading-conclusion)
    

## Aperçu rapide de Django

[Django](https://www.djangoproject.com/) est un framework web Python open-source, complet, qui suit l'approche "batteries-included". Django vise à rendre le développement de sites web complexes et pilotés par des bases de données aussi rapide et facile que possible en fournissant de nombreuses fonctionnalités intégrées comme l'ORM, le système d'authentification, le panneau d'administration, et bien plus encore. Django permet un développement rapide en se concentrant sur l'écriture des parties uniques de l'application plutôt que de perdre du temps à écrire beaucoup de code boilerplate.

La raison de sa popularité est qu'il suit le modèle de conception MVT qui maintient les modèles de données, les vues et les templates bien séparés. Dans Django, la sécurité est primordiale : il protège contre les injections SQL, les scripts inter-sites et la falsification de requêtes inter-sites dès la sortie de la boîte. Django est bien scalable et flexible – il convient à la fois aux petits projets et aux grandes applications web complexes, et c'est pourquoi il est utilisé par des sites majeurs tels qu'Instagram et Pinterest.

## Qu'est-ce que Tailwind CSS ?

Il est bien connu que [Tailwind CSS](https://tailwindcss.com/) est un framework CSS utilitaire. Il vous permet de styliser des éléments directement dans votre HTML, grâce à des classes prédéfinies. Contrairement à d'autres frameworks CSS qui offrent des composants pré-construits, Tailwind offre ces classes utilitaires de bas niveau qui vous permettent de créer votre propre système de design. Ainsi, cela rend la création de designs réactifs uniques sans effort, car il n'y a pas grand-chose à faire avec du CSS personnalisé.

## Pourquoi Django et Tailwind fonctionnent si bien ensemble ?

La combinaison de Django et Tailwind CSS offre une manière transparente de construire des applications robustes et complètes. Voici pourquoi :

* **Développement rapide** : Les capacités backend de Django permettent aux développeurs de créer rapidement des applications puissantes, tandis que Tailwind CSS aide à rationaliser le processus de stylisation avec son approche utilitaire.
    
* **Design personnalisable** : Avec Tailwind, vous n'êtes pas confiné à des styles prédéfinis. Vous pouvez créer un design unique et cohérent qui s'adapte facilement à mesure que votre projet grandit.
    
* **Séparation des préoccupations** : Le système de templating de Django travaille main dans la main avec Tailwind CSS, assurant une séparation claire entre la logique backend et le style frontend.
    

## Comment initialiser un projet Django ?

1. **Installer Django** : Installez Django en utilisant pip :
    
    ```bash
    pip install django
    ```
    
2. **Créer un projet Django** : Utilisez la commande admin de Django pour créer un nouveau projet :
    
    ```bash
    django-admin startproject monprojet
    ```
    
3. **Naviguer vers votre répertoire de projet** :
    
    ```bash
    cd monprojet
    ```
    
4. **Modifier** `settings.py` :
    
    * Dans le paramètre `TEMPLATES`, ajoutez un répertoire `templates` :
        
        ```python
        "DIRS": [BASE_DIR / "templates"],
        ```
        
    * Ajoutez un répertoire `static` pour vos fichiers statiques :
        
        ```python
        STATICFILES_DIRS = [BASE_DIR / "static"]
        ```
        

## Comment intégrer Tailwind CSS avec Django ?

1. **Installer Tailwind CSS** : Assurez-vous que Node.js est installé, puis exécutez :
    
    ```bash
    npm install -D tailwindcss
    npx tailwindcss init
    ```
    
2. **Configurer Tailwind CSS** : Dans votre répertoire `static/css`, créez un fichier `main.css` avec le contenu suivant :
    
    ```css
    @tailwind base;
    @tailwind components;
    @tailwind utilities;
    ```
    
3. **Modifier tailwind.config.js** : Ajustez la section content pour inclure les fichiers `templates/*.html`, en vous assurant que Tailwind CSS génère les styles nécessaires.
    
    ```jsx
    /** @type {import('tailwindcss').Config} */
    module.exports = {
        content: ["./templates/**/*.html", "./**/templates/**/*.html"],
        darkMode: "media",
        theme: {
            extend: {},
        },
        plugins: [],
    };
    ```
    
4. **Ajouter un script de build** : Mettez à jour votre `package.json` pour inclure un script de build :
    
    ```json
    "scripts": {  "watch:css": "tailwindcss build static/css/main.css -o static/output.css -w"}
    ```
    
5. **Compiler Tailwind CSS** :
    
    ```bash
    npm run watch:css
    ```
    

## Créons une application de bulle de chat.

1. **Créer une application Django** :
    
    ```bash
    django-admin startapp chat
    ```
    
2. **Configurer les vues** :
    
    * Dans `chat/views.py`, créez une vue simple :
        
        ```python
        from django.shortcuts import render
        def chat(request):
            return render(request, "chat.html")
        ```
        
3. **Configurer les URLs** :
    
    * Dans `chat/urls.py`, définissez le motif d'URL pour votre vue :
        
        ```python
        from django.urls import path
        from . import views
        urlpatterns = [
            path("", views.chat, name="chat"),
        ]
        ```
        
    * Dans le fichier `urls.py` du projet, incluez les URLs de l'application :
        
        ```python
        from django.urls import include, path
        urlpatterns = [
            path("", include("chat.urls")),
        ]
        ```
        
4. **Configurer le template HTML de base** :
    
    * Créez un fichier `templates/base.html` pour servir de fondation à votre application :
        
        ```html
        {% load static %}
        
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>Mon application Django avec Tailwind</title>
            <link rel="stylesheet" href="{% static 'css/output.css' %}" />
          </head>
        
          <body class="h-screen bg-slate-300 dark:bg-slate-400">
            <section class="container mx-auto flex flex-col items-center">
              <h1 class="mb-4 mt-10 text-6xl font-bold text-blue-500 dark:text-blue-200" >
                Bulle de chat
              </h1>
              {% block content %} {% endblock %}
            </section>
          </body>
        </html>
        
        ```
        
5. **Créer le template de chat** :
    
    * Dans `templates/chat.html`, étendez le template de base :
        
    
    ```html
    {% extends "base.html" %}
    
    {% block content %}
    <div class="flex items-start gap-2.5">
        <img class="w-8 h-8 rounded-full" src="<https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png>" alt="Image de Jhon">
        <div class="flex flex-col gap-1 w-full max-w-[320px]">
            <div class="flex items-center space-x-2 rtl:space-x-reverse">
                <span class="text-sm font-semibold text-gray-900 dark:text-white">Jhon Doe</span>
                <span class="text-sm font-normal text-gray-500 dark:text-gray-400">11:46</span>
            </div>
            <div
                class="flex flex-col leading-1.5 p-4 border-gray-200 bg-gray-100 rounded-e-xl rounded-es-xl dark:bg-gray-700">
                <p class="text-sm font-normal text-gray-900 dark:text-white"> C'est génial. Je pense que nos utilisateurs vont vraiment
                    apprécier les améliorations.</p>
            </div>
            <span class="text-sm font-normal text-gray-500 dark:text-gray-400">Livré</span>
        </div>
    </div>
    {% endblock %}
    ```
    
6. **Lancer le serveur de développement** : `bash python manage.py runserver`
    

## Comment utiliser Prettier pour la mise en forme des classes ?

Pour garder vos classes Tailwind CSS propres et organisées, vous pouvez intégrer Prettier dans votre flux de travail.

1. **Installer Prettier et le plugin Tailwind** :
    
    ```bash
    npm install --save-dev prettier prettier-plugin-tailwindcss
    ```
    
2. **Configurer Prettier** : Créez un fichier `.prettierrc` à la racine de votre projet :
    
    ```json
    {  "plugins": ["prettier-plugin-tailwindcss"]}
    ```
    
3. **Formater à la sauvegarde** : Configurez votre éditeur de code pour formater automatiquement les fichiers avec Prettier à la sauvegarde.
    

### Résultat :

Dépôt GitHub : [ts-django-tailwindcss](https://github.com/themeselection/ts-django-tailwind)

![bulle de chat ts](https://cdn.hashnode.com/res/hashnode/image/upload/v1730793420930/6fbdbfbb-2476-4454-9b90-89bcfd405abf.png align="center")

## Comment créer une bulle de chat en utilisant les composants FlyonUI Tailwind et Django

Ici, nous utiliserons FlyonUI, une bibliothèque open-source de [composants Tailwind CSS](https://flyonui.com/). Elle offre une large gamme de composants personnalisables, accessibles et prêts à l'emploi.

Intégrons Django avec les composants FlyonUI et créons une bulle de chat.

**Étape 1 : Installer flyonui**

Installez `flyonui` via npm.

```bash
npm install -D flyonui@latest
```

**Étape 2 : Configurer Tailwind**

Ajoutez le chemin vers les fichiers JavaScript de FlyonUI dans votre fichier `tailwind.config.js`.

```plaintext
module.exports = {
  content: ["./node_modules/flyonui/dist/js/*.js"], // Requis uniquement si vous souhaitez utiliser le composant JS FlyonUI

  plugins: [
    require("flyonui"),
    require("flyonui/plugin") // Requis uniquement si vous souhaitez utiliser le composant JS FlyonUI
  ]
}
```

**Étape 3 : Copier le JavaScript de FlyonUI**

Copiez le JavaScript de FlyonUI (node\_modules/flyonui/flyonui.js) dans le dossier `static/`.

**Étape 4 : Ajouter le JS à votre base.html**

Une fois que vous avez copié le fichier `js` dans votre dossier static, incluez-le dans base.html.

```html
<html lang="en">
 ...
 <body>
  ...
  <script src="{% static 'js/flyonui.js' %}"></script>
 </body>
</html>
```

Mettons à jour le bloc de code de la bulle de chat :

```html
{% extends "base.html" %}
{% block content %}
<div>
  <div class="chat chat-receiver">
    <div class="avatar chat-avatar">
      <div class="size-10 rounded-full">
        <img
          src="<https://cdn.flyonui.com/fy-assets/avatar/avatar-1.png>"
          alt="avatar"
        />
      </div>
    </div>
    <div class="chat-header text-base-content/90">
      Obi-Wan Kenobi
      <time class="text-base-content/50">12:45</time>
    </div>
    <div class="chat-bubble">J'ai commencé à apprendre la guitare aujourd'hui !</div>
    <div class="chat-footer text-base-content/50">
      <div>Livré</div>
    </div>
  </div>
  <div class="chat chat-sender">
    <div class="avatar chat-avatar">
      <div class="size-10 rounded-full">
        <img
          src="<https://cdn.flyonui.com/fy-assets/avatar/avatar-2.png>"
          alt="avatar"
        />
      </div>
    </div>
    <div class="chat-header text-base-content/90">
      Anakin
      <time class="text-base-content/50">12:46</time>
    </div>
    <div class="chat-bubble">
      C'est génial ! Tu vas être super bon à ça !
    </div>
    <div class="chat-footer text-base-content/50">
      Vu
      <span class="icon-[tabler--checks] align-bottom text-success"></span>
    </div>
  </div>
</div>
{% endblock %}

```

### **Résultat :**

![exemple de bulle de chat](https://cdn.hashnode.com/res/hashnode/image/upload/v1730793343310/63ca723e-ef67-4cee-a112-bed110ce8ea6.png align="center")

## Conclusion

Utiliser Tailwind CSS avec Django est une excellente manière de rendre vos applications web attrayantes et fonctionnelles sur différents appareils, tout en profitant des nombreuses fonctionnalités de Django. Cette configuration non seulement booste la productivité, mais aide également à suivre de bonnes pratiques de style et de design.

Voici le dépôt où vous pouvez trouver plus de détails ou voir le code complet : [ts-django-tailwindcss](https://github.com/themeselection/ts-django-tailwind). J'espère que ce tutoriel vous aide avec l'intégration de Django avec Tailwind CSS. J'ai préparé cet article avec l'aide de [Pruthvi Prajapati](https://github.com/PruthviPraj00), un développeur frontend avec 2 ans d'expérience.

Bon codage !