---
title: Sécurité Web dans Django – Comment construire une application Web sécurisée
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-08-31T18:52:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-secure-django-web-app
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/Web-Security-in-Django
seo_title: Sécurité Web dans Django – Comment construire une application Web sécurisée
---

How-to-Build-a-Secure-Web-Application.png
tags:
- name: Django
  slug: django
- name: sécurité de l'information
  slug: information-security
- name: Python
  slug: python
- name: Sécurité Web
  slug: web-security
seo_title: null
seo_desc: "Par Jacob Isah \nLa sécurité Web est un aspect important du processus de développement d'applications Web. Surtout alors que de plus en plus de données sont stockées, gérées et partagées. \n\
En tant que développeur Web, il est essentiel de prioriser les mesures de sécurité pour protéger les utilisateurs et les données de votre entreprise contre les menaces potentielles.   
  
Dans cet article, je vais démontrer les meilleures pratiques de sécurité Web en construisant une application Web sécurisée en utilisant Django, un puissant framework Web Python. Je couvrirai le hachage des mots de passe, la gestion sécurisée des sessions, l'authentification, l'autorisation et d'autres considérations clés de sécurité avec des exemples de code accompagnateurs.  
  
Avant de continuer avec cet article, gardez à l'esprit que cela n'est pas destiné aux débutants absolus. Vous devez avoir une bonne compréhension de Python pour tirer le meilleur parti de ce guide. 

Si vous devez rafraîchir vos compétences de base en programmation Python et Django avant de continuer, voici quelques ressources pour vous aider :

* [Python pour tous](https://www.freecodecamp.org/news/python-for-everybody/) du Dr. Chuck
* [Django pour tous](https://www.freecodecamp.org/news/django-for-everybody-learn-the-popular-python-framework-from-dr-chuck/), également du Dr. Chuck

Vous aurez accès au code à la fin de l'article.

## Configuration de la structure de fichiers

Disons que nous voulons stocker notre projet sur le bureau. La première chose à faire est de configurer notre structure de fichiers. Commençons par créer un répertoire racine pour notre projet sur le bureau (`WebSec` dans ce cas).

```python
mkdir WebSec
cd WebSec
```

### Créer un environnement virtuel et l'activer

Sur Linux (Ubuntu) :

```python
python3 -m venv my_env

Source my_env/bin/activate
```

Et sur Windows :

```python
python -m venv my_env

my_env\Scripts\activate.bat
```

## Comment créer le projet Django

Tout d'abord, si vous ne l'avez pas déjà, vous devrez installer Django en utilisant la commande suivante :

```python
python -m pip install Django
```

Ensuite, vous pouvez utiliser cette commande pour créer le projet :

```python
django-admin startproject web_sec_project .
```

Et enfin, utilisez cette commande pour créer l'application :

```python 
django-admin startapp web_sec_app
```

Votre structure de fichiers devrait ressembler à ceci à la fin :

```python
WebSec
    my_env/
    web_sec_app/
        __pycache__/
        migrations/
        templates/
        admin.py
        apps.py
        forms.py
        models.py
        tests.py
        urls.py
        views.py
    web_sec_project/
        __pycache__/
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
    db.sqlite3
    manage.py

```

### Exécuter votre serveur

Dans le terminal de votre IDE, exécutez la commande suivante et testez si votre projet fonctionne. Si c'est le cas, vous êtes prêt à partir.

```python
python manage.py runserver
```

Assurez-vous d'ajouter votre application à votre projet :

![Image](https://lh4.googleusercontent.com/5KMFSFkkzM4T-YPujI0_9tm6FdnoTQRfJ8FbfVAZfChJfnkLRjvOSnyfq3PzIiLLWr-h-r5_mw9OOk55yJtXJ4OOjhu0wIwKiTiX5T_-7TN-oHt4elagFQ_st3mAxFHU-bWlR3JCcpcdn6b1BGgVSg)
_Vérifiez que votre application est ajoutée_

Maintenant, commençons à construire et à implémenter la sécurité Web.

## Hachage des mots de passe

La première ligne de défense lors de la mise en œuvre de la sécurité Web consiste à s'assurer que les mots de passe des utilisateurs sont correctement protégés. Et au lieu de stocker les mots de passe en texte brut, il est bon de les hacher. Nous utiliserons le hachage cryptographique pour protéger les informations sensibles des utilisateurs. 

Le hachage cryptographique, également connu sous le nom de fonctions de hachage ou d'algorithmes de hachage, est un concept fondamental en cryptographie et en sécurité informatique. Il consiste à prendre une entrée (ou "message") et à la transformer en une chaîne de caractères de taille fixe, qui est généralement une séquence de nombres et de lettres. Cette sortie est appelée la "valeur de hachage" ou "code de hachage".

Django fournit un mécanisme de hachage de mot de passe sécurisé par défaut, en utilisant l'algorithme **PBKDF2** avec un hachage **SHA-256**. 

Django utilise un mécanisme de hachage de mot de passe robuste et sécurisé pour protéger les mots de passe des utilisateurs. Ce mécanisme aide à garantir que même si la base de données est compromise, les attaquants ne peuvent pas facilement récupérer les mots de passe en texte brut des utilisateurs. Le mécanisme de hachage de mot de passe de Django est constitué de **PBKDF2**.

**PBKDF2** est une fonction de dérivation de clé cryptographique simple qui est résistante aux [attaques par dictionnaire](https://en.wikipedia.org/wiki/Dictionary_attack) et aux [attaques par table arc-en-ciel](https://en.wikipedia.org/wiki/Rainbow_table). Elle est basée sur la dérivation itérative de **HMAC** de nombreuses fois avec un certain remplissage. Cela garantit que même si la base de données est compromise, les mots de passe restent illisibles.

Pour démontrer cela, nous allons créer un nouvel utilisateur avec un mot de passe haché et enregistrer l'utilisateur avec son mot de passe haché dans la base de données.

Tout d'abord, nous importons l'`User` depuis le modèle User. Ensuite, nous importons `make_password`. Voici le code pour faire cela :

```python
#web_sec_app/views.py

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

# Créer des vues utilisateur ici.
def UserView(request):
    users = User.objects.all()
    password = 'password'
    hashed_password = make_password(password)
    return render(request, 'create_user.html', 
                {'users': users, 'hashed_password': hashed_password})
```

## Gestion sécurisée des sessions

La gestion des sessions est essentielle pour maintenir l'état de l'utilisateur sur plusieurs requêtes. Django dispose d'un système de gestion des sessions intégré qui stocke les données de session côté serveur. Nous veillerons à ce que les données de session soient chiffrées et que l'ID de session soit sécurisé pour prévenir les attaques par détournement de session.

Pour atteindre une gestion sécurisée des sessions, nous allons nous assurer d'avoir un cookie de session sécurisé, ce qui nécessitera HTTPS. Nous allons également empêcher l'accès `JavaScript` au cookie de session. La session expire lorsque le navigateur est fermé.

```python
SESSION_COOKIE_SECURE = True
```

Ce paramètre indique à Django d'envoyer le cookie de session uniquement via des connexions HTTPS. Lorsqu'il est défini sur `True`, le cookie de session ne sera pas envoyé via des connexions HTTP non chiffrées. Cela est important pour protéger les données de session sensibles, telles que les jetons d'authentification des utilisateurs, contre l'interception par des acteurs malveillants sur des réseaux non sécurisés.

```python
SESSION_COOKIE_HTTPONLY = True 
```

Définir `SESSION_COOKIE_HTTPONLY` sur `True` ajoute une couche de sécurité supplémentaire. Lorsque cela est activé, le cookie de session ne peut pas être accessible par le code JavaScript s'exécutant sur le navigateur du client. Cela aide à atténuer certains types d'attaques par cross-site scripting (XSS), où un attaquant tente de voler des données de session à l'aide de scripts malveillants.

```python
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
```

Lorsque `SESSION_EXPIRE_AT_BROWSER_CLOSE` est défini sur `True`, la session expirera et sera supprimée une fois que l'utilisateur fermera son navigateur Web. Cela fournit un mécanisme pour créer des sessions de courte durée qui se terminent automatiquement lorsque l'utilisateur termine sa session de navigation. C'est utile pour les scénarios où vous souhaitez vous assurer que les utilisateurs sont déconnectés lorsqu'ils ferment leur navigateur, améliorant la sécurité pour les ordinateurs partagés ou publics.

Votre fichier `settings.py` doit contenir ce qui suit :

```python
SESSION_COOKIE_SECURE = True 
SESSION_COOKIE_HTTPONLY = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
```

## Authentification et autorisation

Des procédures d'authentification et d'autorisation appropriées sont importantes pour limiter l'accès à certaines parties de l'application Web.

Dans cette section, je vais démontrer comment implémenter la connexion et l'authentification des utilisateurs en utilisant le framework d'authentification de Django. Je vais également définir le contrôle d'accès basé sur les rôles des utilisateurs pour garantir que seuls les utilisateurs autorisés peuvent accéder à certaines vues et fonctionnalités.

```python 
@user_passes_test(lambda u: u.is_superuser)
def admin(request):
    return render(request, 'admin.html', {'username': request.user.username})
```

Le code ci-dessus est utilisé pour restreindre l'accès à la vue admin en fonction de si l'utilisateur est un superutilisateur (admin) ou non. 

Si l'utilisateur est un superutilisateur, il est autorisé à accéder à la vue, et le modèle `admin.html` est rendu avec son nom d'utilisateur affiché. Si l'utilisateur n'est pas un superutilisateur, il sera redirigé vers une vue non autorisée par défaut, sauf si une gestion supplémentaire est implémentée. 

Cela garantit que seuls les utilisateurs autorisés avec des privilèges d'admin peuvent accéder à la page 'admin.html'.

## Protection contre les scripts inter-sites (XSS)

Le Cross-Site Scripting (XSS) est une vulnérabilité courante qui permet aux pirates d'injecter des scripts malveillants dans les pages Web consultées par d'autres utilisateurs. 

Dans cette section, nous allons explorer comment implémenter les en-têtes de politique de sécurité du contenu (CSP) pour empêcher l'exécution de scripts non autorisés et protéger notre application contre les attaques XSS.

Les en-têtes CSP fonctionnent en créant un ensemble de règles qui définissent quelles sources de contenu sont autorisées et lesquelles sont bloquées. Cela réduit considérablement la surface d'attaque pour les vulnérabilités XSS, rendant beaucoup plus difficile pour les attaquants d'exécuter des scripts non autorisés sur votre application. 

Il est important de configurer soigneusement les politiques CSP pour trouver un équilibre entre sécurité et fonctionnalité, car des politiques trop restrictives pourraient potentiellement rompre la fonctionnalité légitime de votre application.

```python
CSP_DEFAULT_SRC = ("'self'",)
```

## Protection contre la falsification de requête inter-sites (CSRF)

Les attaques CSRF se produisent lorsque des sites Web malveillants trompent les utilisateurs pour qu'ils effectuent des actions non autorisées sur d'autres sites où ils sont authentifiés. Django offre une protection intégrée contre les attaques CSRF en utilisant des jetons CSRF.

C'est l'une des méthodes les plus courantes utilisées pour prévenir les attaques CSRF en utilisant des jetons CSRF. 

Lorsque l'utilisateur charge une page Web nécessitant une interaction, le serveur génère un jeton unique et l'inclut dans le formulaire ou les données de la requête. Ce jeton est généralement associé à la session de l'utilisateur. Lorsque l'utilisateur soumet le formulaire ou initie une action, le serveur vérifie si le jeton soumis correspond à celui associé à la session de l'utilisateur. S'ils ne correspondent pas, la requête est rejetée, car il pourrait s'agir d'une tentative de réaliser une attaque CSRF. 

Je vais vous montrer comment inclure ces jetons dans les formulaires pour prévenir les requêtes non autorisées.

```html
<h4>Créer un compte</h4>
<form action="{% url 'create_user' %}" method="post">
   {% csrf_token %}
   <input 
      type="text" 
      id="userName" 
      name="username"
      class="form-control input-sm chat-input" 
      placeholder="nom d'utilisateur" 
    />
</form>
```

## Prévention de l'injection SQL

L'injection SQL est une vulnérabilité sérieuse qui se produit lorsque les attaquants manipulent les entrées des utilisateurs pour exécuter des requêtes SQL malveillantes sur la base de données. Je vais démontrer comment l'ORM (Object-Relational Mapping) de Django nettoie automatiquement les entrées des utilisateurs et protège contre les attaques par injection SQL.

Il est important de noter que même si l'ORM de Django offre une défense robuste contre la majorité des attaques par injection SQL, les développeurs doivent toujours adhérer aux meilleures pratiques de sécurité, telles que la validation des entrées et les vérifications d'autorisation, pour garantir la sécurité globale de leurs applications Web. 

Il est également bon de mettre à jour Django et ses dépendances fréquemment pour tirer parti des mises à jour de sécurité ou d'autres améliorations qui pourraient être publiées à l'avenir.

```python
def search(request):
    query = request.GET.get('q')
    if query is not None:
        results = Search.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    else:
        results = []
    return render(request, 'search.html', {'results': results})
```

Le code ci-dessus définit une fonction de vue Django qui gère la fonctionnalité de recherche en extrayant une requête des paramètres `GET` de la requête, en utilisant cette requête pour effectuer une recherche dans le modèle Search en utilisant la méthode filter de l'ORM Django, puis en rendant un modèle avec les résultats de la recherche. 

La recherche est effectuée sur la base des champs '**name**' et '**description**' du modèle, et les résultats sont des correspondances partielles insensibles à la casse.

En s'appuyant sur l'ORM de Django et ses fonctionnalités intégrées, vous tirez parti d'un niveau d'abstraction plus élevé qui aide intrinsèquement à prévenir les vulnérabilités courantes d'injection SQL. 

La structure et les modèles d'utilisation de ce code sont conformes aux meilleures pratiques pour écrire des requêtes sécurisées dans Django, le rendant moins susceptible aux attaques par injection SQL. Mais il est toujours important de s'assurer que le reste de votre base de code suit les meilleures pratiques de sécurité et que vous maintenez votre version Django et ses dépendances à jour pour bénéficier des derniers correctifs de sécurité.

## Sécurité des téléchargements de fichiers

La gestion des téléchargements de fichiers nécessite une attention particulière pour empêcher les attaquants de télécharger des fichiers malveillants. Nous allons voir comment valider et restreindre les téléchargements de fichiers pour garantir la sécurité de notre application Web.

```python
def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('file')
        if uploaded_file:
            if uploaded_file.content_type in ALLOWED_FILE_EXTENSIONS:
                try:
                    with open('uploads/' + uploaded_file.name, 'wb+') as destination:
                        for chunk in uploaded_file.chunks():
                            destination.write(chunk)
                    return render(request, 'success.html')
                except ValidationError as e:
                    error_message = str(e)
                    return render(request, 'fileUpload.html', {'error_message': error_message})
            else:
                error_message = "Type de fichier invalide."
                return render(request, 'fileUpload.html', {'error_message': error_message})
        else:
            error_message = "Aucun fichier sélectionné."
            return render(request, 'fileUpload.html', {'error_message': error_message})
    else:
        return render(request, 'fileUpload.html')

```

L'extrait de code ci-dessus définit une fonction appelée `upload_file`. Cette fonction prend un objet de requête comme argument et gère les téléchargements de fichiers.

La fonction vérifie d'abord si la méthode de requête est `POST`. Si c'est le cas, la fonction obtient le fichier téléchargé par l'utilisateur en utilisant la méthode `request.FILES.get('file')`.

Si le fichier n'est pas vide, la fonction vérifie si l'extension du fichier est dans la liste `ALLOWED_FILE_EXTENSIONS`. Cette liste contient les types de fichiers autorisés à être téléchargés. Si l'extension du fichier n'est pas dans la liste, la fonction affiche un message d'erreur.

Si l'extension du fichier est dans la liste, la fonction essaie d'enregistrer le fichier dans un répertoire appelé `uploads`. La fonction utilise l'instruction `with open()` pour ouvrir le fichier en mode d'écriture binaire. Le fichier est ensuite enregistré par morceaux en utilisant la boucle `for chunk in file.chunks()`.

Si le fichier est enregistré avec succès, la fonction redirige l'utilisateur vers une page de succès. Sinon, un message d'erreur est affiché.

La liste `ALLOWED_FILE_EXTENSIONS` est une mesure de sécurité qui empêche les utilisateurs de télécharger des fichiers malveillants, tels que des exécutables ou des scripts. La limite de taille maximale du fichier est une autre mesure de sécurité qui empêche les utilisateurs de télécharger des fichiers volumineux qui pourraient provoquer une attaque par déni de service. Le stockage du fichier téléchargé dans un répertoire séparé isole le fichier du reste de l'application et rend plus difficile l'accès des attaquants.

## Conclusion

Construire une application Web sécurisée est un processus continu qui nécessite vigilance et la mise en œuvre des meilleures pratiques. 

Dans cet article, j'ai démontré diverses mesures de sécurité Web avec des exemples de code tout en construisant une application Web en utilisant Django. 

En implémentant le hachage des mots de passe, la gestion sécurisée des sessions, l'authentification, l'autorisation et la protection contre les vulnérabilités Web courantes comme XSS et CSRF, j'ai franchi des étapes importantes vers la création d'une application Web robuste et sécurisée. 

Mais la sécurité Web est un domaine vaste et en constante évolution, et il est crucial de rester à jour avec les dernières tendances et pratiques de sécurité pour garantir que votre application Web reste sûre contre les menaces potentielles. Effectuez toujours des tests de sécurité approfondis et mettez régulièrement à jour votre application et vos bibliothèques pour maintenir une défense solide contre les attaques potentielles. 

Avec les bonnes mesures de sécurité en place, vous pouvez offrir à vos utilisateurs une expérience Web sûre et sécurisée en toute confiance.

Vous pouvez avoir accès au code [ici](https://github.com/Enecode/secure-web-application.git). Merci d'avoir lu !