---
title: Comment gérer l'authentification des utilisateurs dans Python Django
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-17T19:49:11.000Z'
originalURL: https://freecodecamp.org/news/user-authentication-in-django-bae3a387f77d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*SA3NDT1VMUBn9g0emx9TUg.png
tags:
- name: Django
  slug: django
- name: learning to code
  slug: learning-to-code
- name: Python
  slug: python
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Comment gérer l'authentification des utilisateurs dans Python Django
seo_desc: 'By Mohammed Subhan Khan

  In this tutorial, I’ll show how to do user login, logout and signup in Django. All
  the code that I describe here is in this GitHub repository. This tutorial will be
  using Python 2.7 and Django 1.9.

  Project installation and str...'
---

Par Mohammed Subhan Khan

Dans ce tutoriel, je vais montrer comment faire la connexion, la déconnexion et l'inscription des utilisateurs dans Django. Tout le code que je décris ici se trouve dans ce dépôt GitHub [repository](https://github.com/khansubhan95/Django-User-Auth). Ce tutoriel utilisera Python 2.7 et Django 1.9.

### Installation et structure du projet

Pour commencer, exécutez les commandes suivantes depuis le terminal :

```bash
django-admin startproject src
cd src
python manage.py startapp mysite
python manage.py migrate
```

En résumé, ces quatre commandes créent un nouveau projet Django nommé src, entrent dans le projet, créent une nouvelle application, mysite, à l'intérieur du projet src, puis créent une base de données SQLite pour le projet nommée db.sqlite3. Assurez-vous également d'inclure l'application mysite dans src/settings.py.

```py
INSTALLED_APPS = [
    'src',
    'django.contrib.admin',
    'django.contrib.auth',
    ...
]
```

Créez un répertoire nommé templates à l'intérieur de l'application mysite. Ensuite, créez deux autres répertoires à l'intérieur de mysite/templates nommés « registration » et « mysite ».

De plus, je vais faire référence aux templates stockés dans ces deux répertoires, en utilisant registration/{template_name} et mysite/{template_name}.

La structure de votre projet devrait finalement ressembler à ceci :

```
.
|-- db.sqlite3
|-- manage.py
|-- mysite
|   |-- admin.py
|   |-- apps.py
|   |-- __init__.py
|   |-- migrations
|   |   `-- __init__.py
|   |-- models.py
|   |-- templates
|   |   |-- mysite
|   |   `-- registration
|   |-- tests.py
|   `-- views.py
`-- src
    |-- __init__.py
    |-- settings.py
    |-- urls.py
    `-- wsgi.py
```

Vous pouvez déjà comprendre à quoi les templates dans mysite peuvent servir (par exemple, les vues définies dans mysite). Nous verrons bientôt l'importance de registration.

De plus, nous aurons besoin d'utilisateurs pour tester notre site. Vous pouvez le faire en créant un superutilisateur (`python manage.py createsuperuser`). Mais ne vous inquiétez pas, tout ce que ce tutoriel décrit peut être appliqué aux utilisateurs normaux également, sans aucun changement. Vous pouvez créer des utilisateurs normaux pour ce tutoriel en créant un superutilisateur, en exécutant votre serveur de développement (`python manage.py runserver`), en naviguant vers localhost:8000/admin, en naviguant vers Users, puis en créant un nouvel utilisateur.

### Gestion de la connexion

Selon la documentation, Django fournit des [vues](https://docs.djangoproject.com/en/1.10/topics/auth/default/#all-authentication-views) pour gérer les méthodes d'authentification des utilisateurs comme la connexion, la déconnexion et la récupération de mot de passe. Cela nous évite d'avoir à définir nos propres vues pour gérer ces choses. De plus, ces vues sont assez configurables et sont incluses dans django.contrib.auth.views, que nous importerons comme suit :

```py
from django.contrib.auth import views as auth_views
```

Nous voulons que la page de connexion s'ouvre lorsque l'utilisateur va sur /login. Pour utiliser la vue [login](https://docs.djangoproject.com/en/1.10/topics/auth/default/#django.contrib.auth.views.login), ajoutez ce qui suit dans src/urls.py

```py
url(r'^login/$', auth_views.login),
```

La vue rend par défaut un template qui se trouve dans registration/login.html.

Notre registration/login.html inclut le formulaire HTML simple suivant :

```html
<!DOCTYPE html>
<html>

<head>
    <title>Connexion</title>
</head>
    
<body>
    <form method="POST">
        {% csrf_token %}
        <p>
            <label>Nom d'utilisateur</label>
            <input type="text" name="username">
        </p>
        <p>
            <label>Mot de passe</label>
            <input type="password" name="password">
        </p>
        <button type="submit">Connexion</button>
    </form>
</body>
    
</html>
```

Vous ne voulez pas utiliser registration/login.html ? Vous pouvez spécifier les templates à utiliser en donnant un dictionnaire python comme troisième paramètre dans le urlpattern, avec 'template_name' comme clé et l'emplacement du template comme valeur. Si vous voulez utiliser mysite/login_user.html comme template :

```py
url(r'^login/$', auth_views.login, {'template_name': 'mysite/login_user.html'})
```

De plus, vous pouvez également utiliser d'autres arguments de la vue, de la même manière. Pour une liste complète des arguments, consultez la [documentation](https://docs.djangoproject.com/en/1.10/topics/auth/default/#django.contrib.auth.views.login).

Lorsque l'utilisateur clique sur le bouton de soumission, la vue de connexion gère la connexion pour nous. Après que l'utilisateur s'est connecté, nous pouvons définir où la page doit être redirigée en spécifiant LOGIN_REDIRECT_URL dans src/settings.py. Par défaut, nous serons redirigés vers /login si la connexion échoue.

```py
LOGIN_REDIRECT_URL = '/'
```

Maintenant, exécutez le serveur de développement (`python manage.py runserver`) et naviguez vers localhost:8000/login/. Entrez les informations d'identification de l'utilisateur pour votre exemple de superutilisateur. Vous serez redirigé vers / si la connexion a réussi. Sinon, vous serez redirigé vers /login.

Même si votre connexion a réussi, vous serez redirigé vers / et verrez une erreur. Cela se produira parce que nous n'avons pas défini de `urlpattern` pour cela.

### Gestion de la déconnexion

Ensuite, nous voulons que les utilisateurs se déconnectent lorsqu'ils naviguent vers /logout. Nous pouvons étendre la même analogie que pour la connexion à la déconnexion, en accédant à la vue correspondant à [logout](https://docs.djangoproject.com/en/1.10/topics/auth/default/#django.contrib.auth.views.logout) en ajoutant le urlpattern suivant à src/settings.py

```py
url(r'^logout/$', auth_views.logout)
```

La vue de déconnexion rend le template registration/logged_out.html par défaut. Voici un simple template de déconnexion :

```html
<!DOCTYPE html>
<html>
    
<head>
    <title></title>
</head>
    
<body>
    Vous avez été déconnecté avec succès.
    <a href="/">Accueil</a>
</body>
    
</html>
```

Comme pour la connexion, vous pouvez changer l'emplacement du template en incluant un objet avec une clé 'template_name' et l'emplacement du template comme valeur.

### Inscription

Nous voulons que nos utilisateurs s'inscrivent sur notre site web en naviguant vers /register. Avant de faire cela, nettoyons un peu le projet. Tout d'abord, nous voulons un `urlpattern` pour notre page d'accueil /. Nous allons utiliser l'application mysite à cette fin, donc ajoutez ce qui suit dans src/urls.py

```py
url(r'^', include('mysite.urls'))
```

Maintenant, nous devons inclure le `urlpattern` pour / dans mysite/urls.py, donc incluez le `urlpattern` suivant (après avoir importé les bibliothèques pertinentes)

```py
from django.conf.urls import url, include
from django.contrib import admin
from .views import home, register

urlpatterns = [
    url(r'^$', home),
    url(r'^register/', register),
]
```

Ici, `home` fait référence à la vue pour /, et `register` fait référence à la vue pour gérer l'inscription. Pour créer un formulaire d'inscription d'utilisateur, nous utiliserons les formulaires intégrés de Django. Pour ce faire, créez un fichier mysite/forms.py et incluez ce qui suit :

```py
from django import forms

class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Nom d\'utilisateur',
        max_length = 32
    )
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32,
    )
    password = forms.CharField(
        required = True,
        label = 'Mot de passe',
        max_length = 32,
        widget = forms.PasswordInput()
    )
```

Tout d'abord, nous importons la bibliothèque de formulaires, nous créons `UserRegistrationForm`, qui hérite de `forms.Form`. Nous voulons que nos formulaires aient 3 champs : `username`, `email`, `password` et les affectations de variables font exactement cela. `forms.CharField` représente un champ composé de caractères. Les arguments — `required`, `max_length` et `label` — spécifient si un champ est requis, sa longueur maximale et l'étiquette du champ. Le paramètre widget dans `password` indique que `password` est une entrée de type « password ».

Nous voulons que les utilisateurs puissent voir le formulaire s'ils vont sur /register, ainsi que le remplir et le soumettre. Cela correspond aux requêtes GET et POST sur /register. Ainsi, nous incluons ce qui suit dans mysite/views.py :

```py
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm

# Créez vos vues ici.

def home(request):
    return render(request, 'mysite/home.html')
    
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/')    
            else:
                raise forms.ValidationError('Il semble qu\'un nom d\'utilisateur avec cet email ou mot de passe existe déjà')
                
    else:
        form = UserRegistrationForm()
        
    return render(request, 'mysite/register.html', {'form' : form})
```

La vue home est définie pour rendre le template src/home.html, qui est le suivant :

```html
<!DOCTYPE html>
<html>
    
<head>
    <title>Accueil</title>
</head>
    
<body>
    {% if user.is_authenticated %}
    <p>bonjour</p>
    <p>bienvenue {{ user.username }}</p>
    <p><a href="/logout">Déconnexion</a></p>
    {% else %}
    <p><a href="/login">Connexion</a></p>
    <p><a href="/register">Inscription</a></p>
    {% endif %}
</body>
    
</html>
```

Nous vérifions si l'utilisateur est connecté, en utilisant user.is_authenticated, et affichons notre texte de bienvenue ainsi que le nom d'utilisateur (en utilisant `user.username`) ainsi qu'un lien pour se déconnecter. Si ce n'est pas le cas, nous afficherons des liens pour se connecter et s'inscrire.

Pour la vue register, nous vérifions si la méthode de requête est POST ou non. Si ce n'est pas le cas, alors nous spécifions le formulaire comme étant `UserRegistrationForm` et le rendons en le passant comme paramètre au template mysite/register.html :

```html
<!DOCTYPE html>
<html>
    
<head>
    <title></title>
</head>
    
<body>
    <form method="POST">
        {% csrf_token %} {{ form.as_p }}
        <button type="submit">Soumettre</button>
    </form>
</body>
    
</html>
```

Le formulaire qui est passé en entrée à la vue register est ensuite rendu en utilisant `form.as_p`. Lorsque l'utilisateur clique sur le bouton de soumission, une requête POST est envoyée. Nous prenons les données du formulaire en utilisant la variable form.

Ensuite, nous vérifions si les données du formulaire sont valides (via `[is_valid()](https://docs.djangoproject.com/en/1.10/ref/forms/api/#django.forms.Form.is_valid)`). Si c'est le cas, nous créons un dictionnaire `userObj` que nous obtenons en appliquant `[cleaned_data](https://docs.djangoproject.com/en/1.10/ref/forms/api/#django.forms.Form.cleaned_data)` au formulaire et en extrayons `username`, `email` et `password`.

La condition if vérifie s'il existe un utilisateur avec le même nom d'utilisateur et le même email dans notre base de données. Si c'est le cas, nous créons un nouvel utilisateur, nous connectons en utilisant le même utilisateur et nous redirigeons vers /. Sinon, nous levons une erreur indiquant qu'un tel utilisateur existe déjà.

Voici quelques documentations pertinentes au cas où vous seriez bloqué ou souhaitez en savoir plus :

* [Authentification des utilisateurs](https://docs.djangoproject.com/en/1.10/topics/auth/default/)
* [Formulaires](https://docs.djangoproject.com/en/1.10/topics/forms/)

Si vous souhaitez me donner des commentaires sur ce tutoriel, [contactez-moi](https://www.mohdsubhan.me/contact/).

Si vous avez aimé cet article, veuillez le ❤ et le partager :)