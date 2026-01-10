---
title: Comment localiser votre application Django
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-11-16T18:07:43.000Z'
originalURL: https://freecodecamp.org/news/localize-django-app
coverImage: https://www.freecodecamp.org/news/content/images/2024/08/pexels-christian-heitz-285904-842711.jpg
tags:
- name: Django
  slug: django
- name: localization
  slug: localization
- name: Python
  slug: python
seo_title: Comment localiser votre application Django
seo_desc: "By Jess Wilk\nHave you ever wondered how websites can offer their content\
  \ in multiple languages, perfectly tailored to different cultures and regions? \n\
  Well, that magic is called localization, and it's a game-changer for web development\
  \ – especially w..."
---

Par Jess Wilk

Vous êtes-vous déjà demandé comment les sites web peuvent offrir leur contenu dans plusieurs langues, parfaitement adapté à différentes cultures et régions ?

Eh bien, cette magie s'appelle la localisation, et c'est un changement de jeu pour le développement web – surtout lorsque vous utilisez Django, un framework Python super polyvalent.

Il ne s'agit pas seulement de traduire du texte – il s'agit aussi d'adapter votre application pour qu'elle s'intègre à différentes cultures, avec leurs coutumes et préférences uniques.

Alors, aujourd'hui, je vais vous guider à travers la localisation d'une application Django. Plongeons-nous dans le sujet !

### Prérequis

Tout d'abord, assurez-vous d'avoir **Python** installé sur votre machine. Pour ce tutoriel, je suppose que vous possédez déjà des connaissances de base en **Django** – nous passerons rapidement sur certaines parties.

Si vous n'êtes pas encore familier avec les bases de Django, vous voudrez peut-être vous rafraîchir la mémoire d'abord. Ne vous inquiétez pas, Hyperskill, où je travaille en tant qu'expert, a ce qu'il vous faut avec quelques [parcours d'apprentissage](https://hyperskill.org/tracks/11?category=1&utm_source=homepage) géniaux.

### Voici ce que nous allons couvrir :

1. [Comment installer Django](#heading-comment-installer-django)
2. [Comment créer un nouveau projet et une nouvelle application Django](#heading-comment-creer-un-nouveau-projet-et-une-nouvelle-application-django)
3. [Comment créer un sélecteur de langue](#heading-comment-creer-un-selecteur-de-langue)
4. [Comment localiser votre application](#heading-comment-localiser-votre-application)
5. [Comment marquer les chaînes dans les templates en utilisant `{% trans %}`](#heading-comment-marquer-les-chaines-dans-les-templates-en-utilisant-trans)
6. [Pluralisation](#heading-pluralisation)
7. [Conclusion](#heading-conclusion)

## Comment installer Django

### Étape 1 : Créer un environnement virtuel

Habituellement, nous créons un environnement virtuel pour les projets Django. Cela aide à isoler le projet des autres projets Python sur votre machine et à garder les dépendances du projet uniques. Exécutez la commande `python -m venv myenv` pour créer un environnement virtuel.

### Étape 2 : Activer l'environnement virtuel

Exécutez `source myenv/bin/activate` sur Unix/macOS ou `myenv\\Scripts\\activate` sur Windows pour activer l'environnement virtuel.

### Étape 3 : Installer Django

Avec votre environnement virtuel actif, installez Django en utilisant le gestionnaire de paquets Python pip en exécutant la commande `pip install django`.

### Étape 4 : Tester l'installation de Django

Après l'installation, vérifiez que Django est installé correctement en exécutant `django-admin --version`. Il devrait afficher le numéro de version sans aucune erreur.

![Image](https://lh7-us.googleusercontent.com/Up1Ue0QkBKQkvZp6YggoT-2RkQSPOZ_h8EN46rl8Z_ZqZvM5EmRANoBURpN6oU8SP6OrObUHnHJ5HXnYeZEK5DyPADhfNHb4PNu98xcdIbui8gP18wHtmzTTshLQtEz1uXFk0j1l51c94wv5wCDLVcw)

**django-admin** est le script en ligne de commande qui vient avec Django. Il effectue des tâches administratives comme démarrer un nouveau projet et gérer les migrations de base de données.

## Comment créer un nouveau projet et une nouvelle application Django

### Étape 1 : Créer un projet Django

Créons un nouveau projet nommé localization_project en utilisant la commande `django-admin startproject localization_project`.

Cette commande va créer un nouveau répertoire appelé `localization_project`, contenant tous les fichiers nécessaires pour notre projet Django, comme montré ci-dessous.

![Image](https://lh7-us.googleusercontent.com/lasC5Lapd9onrbUJPL_kd51iMMV-n4e31amdbqUl8-452gqE9LPKvw4Tj5S5yGix44fhYAReSF5erlyip6FK4_vUil8pF7zE4hvgt0OZ_emW4QnZYNVUB3MCRse50PoFVeb1QkYgkHUF8grUbTGVc24)
_Un nouveau répertoire appelé `localization_project`_

Pour commencer à travailler sur ce nouveau projet, allez dans le dossier nouvellement créé en exécutant la commande `cd localization_project`.

### Étape 2 : Créer une application Django

Vous avez besoin d'une application avec du contenu pour montrer comment traduire le contenu. J'utiliserai la commande `python manage.py startapp homepage` pour créer une application simple.

Encore une fois, manage.py est un autre **utilitaire en ligne de commande** qui agit comme une enveloppe légère autour de django-admin, vous permettant d'interagir avec votre projet Django de diverses manières.

Une fois que vous avez exécuté cela, vous devriez obtenir un autre dossier appelé homepage avec de nombreux fichiers Python.

### Étape 3 : Définir la vue pour votre application

Ouvrez le fichier `views.py` dans le répertoire de l'application homepage et définissez une vue pour la page d'accueil. Pour simplifier, notre page d'accueil affichera un message de bienvenue, un nombre en milliers et la date actuelle.

```python
from django.shortcuts import render
from django.utils import timezone


def home_view(request):
    context = {
        'greeting': "Bienvenue dans notre Projet de Localisation !",
        'large_number': 12345.67,
        'current_date': timezone.now()
    }
    return render(request, 'home.html', context)
```

### Étape 4 : Configurer les URLs

Tout d'abord, dans le répertoire `localization_project`, modifiez le fichier `urls.py` pour inclure les URLs de l'application homepage.

```python
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
]
```

Ensuite, créez un fichier `urls.py` dans le **répertoire de l'application homepage** et définissez l'URL pour votre vue.

```python
from django.urls import path
from .views import home_view


urlpatterns = [
    path('', home_view, name='home'),
]
```

### Étape 5 : Créer le template de la page d'accueil

Dans le répertoire de l'application homepage, créez un dossier nommé templates. À l'intérieur, créez un fichier nommé `home.html`. C'est ici que vous allez concevoir votre page d'accueil. Ajoutez le code HTML suivant :

```python
<!DOCTYPE html>
<html>
<head>
    <title>Projet de Localisation</title>
</head>
<body>
    <h1>{{ greeting }}</h1>
    <p>Nombre : {{ large_number }}</p>
    <p>Date : {{ current_date }}</p>
</body>
</html>
```

Ajoutez la page d'accueil à la liste **INSTALLED_APPS** dans votre fichier `settings.py` dans le répertoire `localization_project`.

```python
INSTALLED_APPS = [
    # 'other apps',
    'homepage',
]
```

Voici à quoi devrait ressembler votre répertoire final `localization_project` :

![Image](https://lh7-us.googleusercontent.com/OYqBkb5L6wtvrQENqa89O-7F9nJBGdBRA-vb-p-4saAxE1JLFfci3VTM2RENhuB-wdUmf6TLR-QpxrEeT_QdALrNbdTQdMpKNXTwaU2nITbcb6MQgystPD9DJZunddDvX5lGjj6Rc4wpZQIj3VEwnaM)
_Un répertoire final `localization_project`_

### Étape 6 - Exécuter le serveur de développement

Enfin, vous pouvez exécuter votre serveur de développement pour voir la page d'accueil en utilisant la commande `python manage.py runserver`.

Maintenant, lorsque vous visitez http://127.0.0.1:8000/ dans votre navigateur web, vous devriez voir votre page d'accueil simple affichant un message de bienvenue, un nombre en milliers et la date actuelle.

![Image](https://lh7-us.googleusercontent.com/FgKfmYPAti1Q74jKY5l393qNVjGh4GlRJIDEx2n5uxMG0SB3Ru5J19DX0fmaxSAHgllrCpC3Ky8nTH9HwC3rX_wAgSv-qUSFHjFop-HSsBOgcNYuNI635B4RdkzlxVP_ZO2dHGmE3EGZ2Kh2vRFb1Rg)
_Un message de bienvenue, un nombre en milliers et la date actuelle_

## Comment créer un sélecteur de langue

Typiquement, la plupart des sites web affichent du contenu en anglais lorsque vous les visitez pour la première fois.

Si vous avez visité un site web qui supporte la localisation, vous avez peut-être remarqué un menu déroulant permettant aux utilisateurs de sélectionner parmi les langues que le site web supporte. Une fois que l'utilisateur sélectionne sa langue préférée, le site web définit automatiquement celle-ci comme langue par défaut et met à jour le contenu en conséquence.

Ce menu déroulant est appelé un sélecteur de langue, que vous allez créer ensuite. Avec lui, vous aurez une option pour permettre aux utilisateurs de changer la langue et voir la fonctionnalité de localisation en action, que vous ferez après cela.

### Étape 1 : Ajouter un formulaire de sélection de langue

Tout d'abord, modifiez votre template `home.html` pour inclure un formulaire de sélection de langue. Ce formulaire contiendra un menu déroulant avec les options **Anglais**, **Espagnol** et **Français**. Le formulaire sera soumis à la vue intégrée `set_language` de Django, qui gérera le changement de langue.

```python
<!DOCTYPE html>
<html>
<head>
    <title>Projet de Localisation</title>
</head>
<body>
    <h1>{{ greeting }}</h1>
    <p>Nombre : {{ large_number }}</p>
    <p>Date : {{ current_date }}</p>


    <form action="{% url 'set_language' %}" method="post">
        {% csrf_token %}
        <input name="next" type="hidden" value="{{ redirect_to }}" />
        <select name="language">
            <option value="en">Anglais</option>
            <option value="es">Espagnol</option>
            <option value="fr">Français</option>
        </select>
        <input type="submit" value="Changer de Langue">
    </form>
</body>
</html>
```

### Étape 2 : Mettre à jour votre vue

Dans votre fonction `home_view` dans `views.py`, incluez le chemin actuel dans le contexte afin que le formulaire sache où rediriger après avoir changé la langue.

```python
from django.utils.translation import gettext as _


def home_view(request):
    context = {
        'greeting': _("Bienvenue dans notre Projet de Localisation !"),
        'large_number': 12345.67,
        'current_date': timezone.now(),
        'redirect_to': request.path
    }
    return render(request, 'home.html', context)
```

### Étape 3 : Configurer l'URL pour le changement de langue

Assurez-vous que votre fichier `urls.py` dans le répertoire `localization_project` est configuré pour gérer le changement de langue. Django fournit une vue pour cela, mais vous devez la connecter dans votre configuration d'URL.

```python
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
]
```

Le motif d'URL i18n inclut la vue de redirection `set_language`.

### Étape 4 : Activer le middleware pour la locale

Assurez-vous que `LocaleMiddleware` est activé dans votre fichier `settings.py`. Ce middleware permet à Django de détecter automatiquement la préférence de langue de l'utilisateur à partir de la requête.

```python
MIDDLEWARE = [
    # 'other middleware',
    'django.middleware.locale.LocaleMiddleware',
]
```

### Étape 5 : Exécuter le serveur de développement et tester le sélecteur de langue

Exécutez votre serveur de développement et visitez votre page d'accueil. Vous devriez maintenant voir quelque chose de similaire à l'image ci-dessous, présentant le menu déroulant de sélection de langue avec les trois langues que nous avons choisies.

![Image](https://lh7-us.googleusercontent.com/9yNT9lQNvc6xCh_VvgwkOhygjTW0zogXJRdwhRYUlpEqJ3lngsynnXwbzHpwpI4MPLzeey4-HPJJEW0McsNSJSeKd0kBSDdpzliUUbcSaYvTCJzak-GznTRKLqWnV7W62Kf_aOz3Gi_kfzX8GwlVsVg)
_Le menu déroulant de sélection de langue avec les trois langues que nous avons choisies_

## Comment localiser votre application

Cette section vous montrera comment traduire le texte sur notre page d'accueil selon les sélections de l'utilisateur local.

### Étape 1 : Activer l'internationalisation dans les paramètres Django

Avant de commencer, assurez-vous que votre projet Django est configuré pour l'internationalisation. Dans votre fichier `settings.py`, vous devrez vérifier et mettre à jour les paramètres suivants.

Les quatre premiers paramètres dans le code suivant viennent probablement par défaut. Vous devez donc spécifier les langues que vous souhaitez supporter dans votre application – dans ce cas, l'anglais, l'espagnol et le français.

Ensuite, définissez le chemin vers votre répertoire de locale. C'est ici que Django stockera et cherchera les fichiers de traduction. Vous devez créer ce répertoire manuellement dans votre projet (dans le même répertoire que le fichier `manage.py`). N'oubliez pas non plus d'importer le module OS en haut du fichier.

```python
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
LANGUAGES = [
    ('en', 'English'),
    ('es', 'Spanish'),
    ('fr', 'French'),
]
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]
```

### Étape 2 : Marquer le texte pour la traduction

Lors du développement d'une application web utilisant Django, il est essentiel de se souvenir que le texte, les nombres et les dates sont localisés différemment selon la langue et la culture. Cela est dû au fait que leur contenu et leur contexte peuvent varier considérablement.

Par exemple, les chaînes de texte doivent être plus conscientes de leur signification et de leur contexte lorsqu'elles sont utilisées dans une application. Donc, pour rendre votre application accessible aux utilisateurs de différentes cultures, vous devez marquer explicitement chaque chaîne qui doit être traduite.

D'un autre côté, les nombres et les dates sont des types de données que Django peut formater automatiquement selon la locale. Vous n'avez pas besoin de les marquer.

Si vous vérifiez notre application, vous remarquerez que nous avons passé trois valeurs de notre fichier `views.py` au template HTML : une chaîne, un nombre et une date. Bien qu'il ne soit pas nécessaire de marquer le nombre et la date pour la localisation, vous devez marquer la chaîne pour permettre sa localisation. À cette fin, Django fournit la fonction `gettext`.

Lors de la localisation de votre application, marquez toute chaîne que vous passez de la vue au template HTML que vous souhaitez localiser. Dans notre cas, nous allons marquer le texte de salutation avec _().

```python
from django.utils.translation import gettext as _
from django.shortcuts import render
from django.utils import timezone


def home_view(request):
    context = {
        'greeting': _("Bienvenue dans notre Projet de Localisation !"),
         #other data
    }
    return render(request, 'home.html', context)
```

### Étape 3 : Créer des fichiers de messages

Utilisez la commande `makemessages` pour créer des fichiers de langue pour chaque langue. Elle analyse vos fichiers de projet Django pour les chaînes de traduction marquées pour la localisation et génère des fichiers `_._po`, qui stockent les traductions. Exécutez ces commandes dans votre outil de ligne de commande ou terminal.

* Pour l'espagnol : `django-admin makemessages -l es`
* Pour le français : `django-admin makemessages -l fr`

Cela créera des fichiers `.po` dans les répertoires `locale/es/LC_MESSAGES` et `locale/fr/LC_MESSAGES`.

### Étape 4 : Traduire les fichiers de messages

Ouvrez chaque fichier `.po` et ajoutez la traduction pour chaque chaîne sous son `msgstr` correspondant. Par exemple, dans `locale/es/LC_MESSAGES/django.po`, vous ajouteriez ce qui suit :

```py
msgid "Welcome to our Localization Project!"
msgstr "Bienvenido a nuestro Proyecto de Localización!"
```

Et vous ajouteriez le texte suivant dans `locale/fr/LC_MESSAGES/django.po` :

```py
msgid "Welcome to our Localization Project!"
msgstr "Bienvenue dans notre Projet de Localisation!"
```

### Étape 5 : Compiler les fichiers de messages

Après la traduction, compilez ces fichiers en fichiers `.mo`, des fichiers lisibles par machine que Django peut utiliser. Exécutez la commande `django-admin compilemessages` pour traiter tous vos fichiers `_._po` dans le projet et générer les fichiers `.mo` correspondants.

### Étape 6 : Exécuter le serveur et tester les traductions

Maintenant, testez vos traductions en utilisant le sélecteur de langue sur votre site web. Rafraîchissez votre page d'accueil, et vous devriez voir le message de salutation dans la langue sélectionnée :

![Image](https://lh7-us.googleusercontent.com/PvcQ_nIqBHwpavzd-g9XWonKSAsCeZ_Cy80nCxYNZ3pBNIthVug_u-7CGr905Dug41pfXKBoZflcHkeAYHfQI54SutLQKZcU0jw6KlhjTl353pFOz49-I-SVR82gBOYkXiJ8VlzEze4PeLf7fC77YOo)
_Le message de salutation en espagnol_

![Image](https://lh7-us.googleusercontent.com/WVeCHfGGlMqSEtGIBuKtFPmFYiWNEanZv66Btk92avC-rpaBQ1XrvSBwdlphmCqDBxd5JxZ5cnoLv2wiXvaobNKPOS21p6kfUe2FbxOkG7W54onAb6Jun5c2FOn1T74HWPoNIdNOCon2cc_kSC_GHeg)
_Le message de salutation en français_

Comme vous pouvez le voir, le titre du projet, _Bienvenue dans notre Projet de Localisation_, est traduit selon la langue que nous sélectionnons. Vous remarquerez également que le nombre et la date sont automatiquement traduits dans la langue sélectionnée.

Mais vous pouvez voir que les mots _Nombre_ et _Date_ ne sont pas traduits. Nous ne les avons pas marqués pour la traduction dans les étapes précédentes.

Chaque fois que vous mettez à jour votre application web avec du contenu supplémentaire et que vous devez localiser ce nouveau contenu, suivez simplement les étapes mentionnées ci-dessus.

Tout d'abord, marquez les chaînes qui nécessitent une localisation. Ensuite, exécutez la commande `makemessages` pour mettre à jour vos fichiers `.po` avec ces nouvelles chaînes. Ensuite, fournissez les textes traduits pertinents dans les fichiers `.po` pour ces nouvelles chaînes. Enfin, générez les fichiers `.mo` en utilisant la commande `compilemessages`.

## Comment marquer les chaînes dans les templates en utilisant `{% trans %}`

Comme vous le savez, les mots _Nombre_ et _Date_ n'ont pas été localisés dans nos étapes précédentes. Intéressamment, vous ne pouvez pas les marquer en utilisant la méthode `gettext` car ils ne sont pas passés depuis le fichier `views.py`. Ce sont des mots statiques dans le template HTML.

Pour localiser le texte dans les templates Django, vous utilisez la balise de template `{% trans %}` fournie par Django. Cette balise indique à Django de traduire le texte spécifié dans la langue appropriée en fonction de la préférence de langue de l'utilisateur actuel.

Localisons les textes _Nombre_ et _Date_ en utilisant la balise de template `{% trans %}`.

### Étape 1 : Mettre à jour votre template avec les balises `{% trans %}`

Ouvrez votre template `home.html` et modifiez-le pour inclure les balises `{% trans %}` autour du texte que vous souhaitez traduire. Voici un exemple – n'oubliez pas d'ajouter `{% load i18n %}` en haut du fichier HTML :

```python
{% load i18n %}


<!DOCTYPE html>
<html>
<head>
    <title>{% trans "Projet de Localisation" %}</title>
</head>
<body>
    <h1>{{ greeting }}</h1>
    <p>{% trans "Nombre" %}: {{ large_number }}</p>
    <p>{% trans "Date" %}: {{ current_date }}</p>


    <!-- Formulaire de Sélection de Langue -->
    <!-- ... -->
</body>
</html>

```

Dans cet exemple, les mots _Projet de Localisation_, _Nombre_ et _Date_ dans le template sont marqués pour la traduction.

### Étape 2 : Créer/mettre à jour les fichiers de messages de langue

Exécutez la commande `makemessages` pour mettre à jour les fichiers `.po` pour chaque langue.

* Pour l'espagnol : `django-admin makemessages -l es`
* Pour le français : `django-admin makemessages -l fr`

### Étape 3 : Traduire les nouvelles chaînes dans les fichiers `.po`

Dans chaque fichier `.po`, vous trouverez les nouvelles chaînes ajoutées. Ajoutez leurs traductions sous `msgstr` pour chaque langue. Par exemple, voici le contenu lié pour le fichier .po espagnol :

```py
#: .\homepage\templates\home.html:10
msgid "Number"
msgstr "Número"

#: .\homepage\templates\home.html:11
msgid "Date"
msgstr "Fecha"
```

Ensuite, exécutez la commande `django-admin compilemessages` pour compiler les fichiers de messages et exécutez le serveur de développement pour tester l'application web mise à jour. Maintenant, vous pouvez voir la sortie suivante :

![Image](https://lh7-us.googleusercontent.com/36WBImqij72SZsdYIff9LbyEWz2NIiKQCy5Zqh0cGfhxfTwFHh7783qZ_cnyrQ4E7asEbbAg4GMdrwssghE38mMBgIgz52j4Y_6kCPy-YzJ2398j3_PSkZVjMYHK52oj8JXnZZS0h22wXYu4PZNeigc)
_Le message de salutation complètement en espagnol_

![Image](https://lh7-us.googleusercontent.com/x4Dt7zWoVjaFct9qlaHOIc4BVUQjLkufn-_Efl9hr8GcQIg52XDGilPykw-C3DA3arbny8CinIHaJzGPbT7xdNmGkB19CpjXlRieSwOH4wd9gwdf8WeNJJUblGvAf2UP8pLAZw4CKpuxXzGpv5vWNvg)
_Le message de salutation complètement en français_

## Pluralisation

La pluralisation dans le framework Django est un moyen de gérer différentes traductions basées sur une valeur numérique. Elle est essentielle car, dans de nombreuses langues, la forme d'un mot change en fonction du nombre qui le décrit.

Django fournit un moyen de gérer cela en utilisant la balise de template `{% blocktrans %}` avec une forme plurielle.

Démontrons cela en utilisant notre application Django. Supposons que vous souhaitez afficher un message sur le nombre de visiteurs sur votre site, qui change dynamiquement.

### Étape 1 : Mettre à jour votre vue pour passer le nombre de visiteurs

Tout d'abord, modifiez votre `home_view` dans `views.py` pour inclure une variable représentant le nombre de visiteurs. À des fins de démonstration, cela peut être un nombre statique.

```python
from django.shortcuts import render
from django.utils import timezone
from django.utils.translation import gettext as _


def home_view(request):
    num_visitors = 5
    context = {
        'greeting': _("Bienvenue dans notre Projet de Localisation !"),
        'num_visitors': num_visitors,
    }
    return render(request, 'home.html', context)

```

### Étape 2 : Mettre à jour le template avec la pluralisation

Dans votre `home.html`, utilisez la balise `{% blocktrans %}` avec une forme plurielle pour gérer la pluralisation, comme ceci :

```python
<!-- Autres contenus du template -->
   
    <h1>{{ greeting }}</h1>
    <p>
    {% blocktrans count counter=num_visitors %}
        Il y a {{ counter }} visiteur.
    {% plural %}
        Il y a {{ counter }} visiteurs.
    {% endblocktrans %}
    </p>


    <!-- Contenu restant du template -->
```

Ici, `{% blocktrans count counter=num_visitors %}` est utilisé pour gérer le cas singulier, et la section `{% plural %}` est pour le cas pluriel.

### Étape 3 : Mettre à jour les fichiers de messages

Exécutez la commande `makemessages` pour mettre à jour vos fichiers `_._po` pour chaque langue : `django-admin makemessages -l es` pour l'espagnol, et `django-admin makemessages -l fr` pour le français.

### Étape 4 : Traduire et gérer les formes plurielles dans les fichiers `.po`

Dans chaque fichier `.po`, vous trouverez des entrées pour les formes singulières et plurielles.

Par exemple, le fichier .po espagnol devrait avoir le contenu suivant :

```py
msgid "There is %(counter)s visitor."
msgid_plural "There are %(counter)s visitors."
msgstr[0] "Hay %(counter)s visitante."
msgstr[1] "Hay %(counter)s visitantes."
```

Ensuite, exécutez la commande `django-admin compilemessages` pour compiler les fichiers de messages. Exécutez votre serveur, et vous devriez voir le message au singulier ou au pluriel selon le nombre de visiteurs. Changez le nombre dans `num_visitors` dans votre vue et observez comment le message change.

![Image](https://lh7-us.googleusercontent.com/0MLly1OjdLtGZ86I5wfGxcSOw36WoQFSIR-awU40fKB1xwrMOPV7M9GlT2hAD3YFmBeFkUeSxhG7eisZ7x_SCkjbMKZWI8Hox_4Z79ggwdR362xG3By6d4f3yoplWEiCRGDZWPd5eDaAAsQSiBoUZXU)
_Le message au singulier ou au pluriel selon le nombre de visiteurs. Version anglaise_

![Image](https://lh7-us.googleusercontent.com/efgAT1-V3Eh_7QbiOLL0KHo2rEI2xh32A2y1oWXCf8lH1TNADoFF7H1PFT3tNbzt-_N5ss1D94pOK2m6b6Cx5dqIqTcvBjpxYadPUswCS4GCUky_Wj9ZgaBu1eCvDbcs9cYVyrr--aI-CferSD7j8FE)
_Le message au singulier ou au pluriel selon le nombre de visiteurs. Version française_

## Conclusion

Et voilà – un guide complet pour localiser une application Django. Avec la conception accessible de Django, vous avez tous les outils nécessaires pour traduire des nombres et des valeurs DateTime à portée de main. De plus, nous avons vu comment la ligne de commande Django-admin peut faciliter la gestion des fichiers de traduction.

Mais il est essentiel de se rappeler que la localisation d'un site web va au-delà de la simple traduction des mots. Pour exploiter pleinement les capacités de localisation de Django, plongez-vous dans sa documentation, approfondissez votre compréhension et continuez à pratiquer.

Merci d'avoir lu ! Je suis Jess, et je suis une experte chez Hyperskill. Vous pouvez consulter une [piste Django](https://hyperskill.org/tracks/11?category=1&utm_source=homepage) sur la plateforme.