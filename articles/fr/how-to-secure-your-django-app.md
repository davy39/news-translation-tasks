---
title: Comment sécuriser votre application Django – Bonnes pratiques et exemples de
  code
subtitle: ''
author: Sophia Iroegbu
co_authors: []
series: null
date: '2024-05-22T15:05:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-secure-your-django-app
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/Blog-Banner
seo_title: Comment sécuriser votre application Django – Bonnes pratiques et exemples
  de code
---

Template--2-.png
étiquettes:
- nom: Django
  slug: django
- nom: Python
  slug: python
- nom: Sécurité
  slug: securite
seo_title: null
seo_desc: En tant que développeur ou ingénieur logiciel, il ne suffit pas de savoir construire des solutions utiles – vous devez également vous assurer qu'elles sont sécurisées. Prioriser vos utilisateurs est crucial lors du développement et du déploiement de votre logiciel, car si les utilisateurs ne peuvent pas utiliser votre application, elle devient inutile.
---

En tant que développeur ou ingénieur logiciel, il ne suffit pas de savoir construire des solutions utiles – vous devez également vous assurer qu'elles sont sécurisées. Prioriser vos utilisateurs est crucial lors du développement et du déploiement de votre logiciel, car si les utilisateurs ne peuvent pas utiliser votre application, elle devient inutile.

Dans ce guide, nous allons discuter de certaines mesures de sécurité pour un projet Django sécurisé avant votre prochain déploiement.

Apprenons !

## Mesures de sécurité pour l'authentification et l'autorisation

Lors de la création d'une application Django, la gestion des utilisateurs nécessite de prioriser l'authentification et l'autorisation comme mesures de sécurité clés.

Voici quelques pratiques de sécurité lors de la mise en œuvre des fonctionnalités d'authentification et d'autorisation :

1. Lors de la gestion de l'authentification des utilisateurs, il est préférable de mettre en œuvre une authentification sécurisée comme l'authentification basée sur un mot de passe, un jeton ou une authentification multifactorielle. Cela garantit que vous vérifiez vos utilisateurs plus d'une fois et lorsqu'ils souhaitent utiliser votre application.
2. Si vous utilisez une authentification basée sur un mot de passe, assurez-vous d'utiliser un algorithme de hachage robuste comme la fonction [`make_password`](https://docs.djangoproject.com/en/5.0/ref/contrib/auth/) de Django pour éviter de stocker le mot de passe en texte brut.
3. Lors du hachage des mots de passe des utilisateurs, assurez-vous de mettre en œuvre la génération de sel. Générez des données aléatoires uniques (sel) pour renforcer le processus de hachage du mot de passe et prévenir les attaques pré-calculées.
4. Envisagez d'utiliser une authentification basée sur des jetons et définissez une minuterie d'expiration pour ajouter une autre couche de sécurité. Cela permet au jeton d'accès de l'utilisateur d'expirer après un certain temps et il devra vérifier son identité à nouveau pour continuer à utiliser votre application. Notez que lors de la mise en œuvre de cela, assurez-vous de ne pas régler la minuterie pour qu'elle expire toutes les 5 minutes, 30 minutes ou une heure afin qu'elle n'affecte pas négativement l'expérience utilisateur.
5. Lors de la gestion des utilisateurs, mettez toujours en œuvre un contrôle d'accès basé sur les rôles (RBAC) pour attribuer des rôles à chaque utilisateur. C'est-à-dire que les utilisateurs ne peuvent accéder qu'aux fonctionnalités utilisateur et les administrateurs peuvent accéder aux fonctionnalités utilisateur et à d'autres fonctionnalités étendues.
6. Après avoir haché le mot de passe et avoir un contrôle d'accès, mettez en œuvre des mesures de contrôle d'accès et de chiffrement appropriées afin que seuls les utilisateurs autorisés puissent accéder à leurs mots de passe.

## Mesures de sécurité contre les attaques par injection SQL

Les attaques par injection SQL sont l'une des vulnérabilités web les plus courantes, et les projets Django peuvent être exploités par de telles attaques, en particulier lorsque les données passant du côté client au côté serveur sont vulnérables.

Une excellente façon pour vous de prévenir ces attaques dans vos projets Django est d'utiliser des requêtes paramétrées. Les [requêtes paramétrées](https://sophyia.me/secure-your-django-app-with-parameterized-queries) sont un moyen facile de séparer le code SQL de l'entrée utilisateur, garantissant que les données utilisateur ne font pas partie de la commande SQL en utilisant les ORM Django.

Voici comment cela fonctionne. Vous pouvez interroger directement les données dans votre base de données comme ceci :

```
from .models import User  

def user_search(request):
    username = request.GET.get('username')
    
    # Construction de requête vulnérable
    query = "SELECT * FROM users WHERE username = '" + username + "'"

    # Retourner une réponse
    return HttpResponse("User search query: " + query)
```

Vous pouvez utiliser la méthode Django QuerySet `filter()` pour filtrer les données et les assainir, comme ceci :

```python
from .models import User

def user_search(request):
    username = request.GET.get('username')
    
    # Requête sécurisée utilisant une requête paramétrée
    users = User.objects.filter(username=username)
    
    # Retourner une réponse
    return HttpResponse("Recherche d'utilisateur exécutée de manière sécurisée.")
```

## Mesures de sécurité contre les attaques par script inter-sites (XSS)

Les attaques par script inter-sites ou XSS se produisent en injectant des scripts malveillants dans une page web ou une application accessible par d'autres utilisateurs. Ces attaques pourraient être exploitées dans vos projets Django si vous oubliez de valider les données utilisateur, d'empêcher les navigateurs d'interpréter votre contenu web ou d'omettre une politique de sécurité du contenu.

Voici quelques pratiques de sécurité pour éviter les attaques XSS :

### Valider les données utilisateur

Lors de la gestion des données générées par les utilisateurs, assurez-vous de toujours valider les données. Vous pouvez utiliser des outils de validation intégrés comme la fonction `[django.core.validators](https://docs.djangoproject.com/en/1.8/_modules/django/core/validators/)`.

Voici un exemple de validation d'une adresse e-mail obtenue du côté client :

```python
from django.core.validators import validate_email

email = request.GET.get('email')

if not validate_email(email):
    raise ValueError("Adresse e-mail invalide.")
```

Voici un autre exemple de validation d'une URL obtenue de l'utilisateur :

```python
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def validate_url(url):
    validator = URLValidator()
    try:
        validator(url)
    except ValidationError as e:
        return e.message
    return None

```

### Toujours encoder les données utilisateur lors de leur affichage

Si votre projet prend des données utilisateur et les affiche, assurez-vous de les encoder correctement en utilisant le [modèle d'échappement automatique de Django](https://www.w3schools.com/django/ref_tags_autoescape.php), `{% autoescape %}`. La balise `autoescape` est utilisée pour vérifier si l'`autoescape` est activé ou désactivé. S'il est activé, il garantit que le code HTML dans vos variables est échappé.

Voici un exemple :

```python
{% autoescape on %}
    {{ user_input }}
{% endautoescape %}
```

### Utiliser les bons en-têtes HTTP

Dans votre projet Django, définissez toujours les en-têtes HTTP appropriés pour empêcher les navigateurs d'interpréter le contenu comme des scripts exécutables. Cela peut sembler mineur, mais cela empêchera les navigateurs de deviner le type de votre réponse.

Voici deux en-têtes HTTP que vous pouvez implémenter :

1. `X-Content-Type-Options` : Cette configuration garantit que les navigateurs ne détectent ou ne devinent pas le type Multipurpose Internet Mail Extensions (MIME) d'une réponse. MIME est utilisé pour spécifier le format des messages Internet.
2. `Content-Type: text/html: charset=UTF-8` : Cette configuration garantit que votre contenu web est traité comme du HTML et correctement encodé comme tel.

Vous pouvez définir ces en-têtes dans vos fichiers de modèle pour éviter les attaques XSS.

### Toujours utiliser la politique de sécurité du contenu

La politique de sécurité du contenu (CSP) est une mesure de sécurité utilisée dans les navigateurs web pour prévenir les attaques malveillantes, les attaques XSS et les injections de données. Cette politique permet aux développeurs web de définir des sources de confiance comme les images, les scripts, les styles CSS, etc., sur leurs projets.

Les politiques de sécurité du contenu sont généralement livrées via des en-têtes HTTP ou des balises méta HTML pour renforcer la sécurité de vos applications web.

Dans votre projet Django, vous pouvez implémenter CSP comme ceci :

```python
from django.http import HttpResponse

response = HttpResponse("Votre contenu ici")
response['Content-Security-Policy'] = "default-src 'self'; script-src 'self' https://trusted-cdn.com;"

```

## Mesures de sécurité contre la falsification de requête inter-sites (CSRF)

La falsification de requête inter-sites (CSRF) est une vulnérabilité qui attaque en trompant les utilisateurs pour qu'ils effectuent des actions à leur insu ou sans leur consentement. Ces attaques utilisent une requête pour tromper l'utilisateur en lui faisant soumettre un lien ou un formulaire sur un site web ou une application web différente et, comme la requête provient de la session authentifiée de l'utilisateur, elle est exécutée, et l'attaquant a accès pour effectuer une manipulation de données ou toute action non autorisée.

Pour prévenir de telles attaques dans votre projet Django, vous pouvez implémenter ces pratiques :

### Utiliser la limitation de débit basée sur le middleware

La limitation de débit est utilisée pour contrôler la fréquence des requêtes faites par un serveur, une API ou un utilisateur. Cela fonctionne en ayant une limite sur le nombre de requêtes qui peuvent être faites dans un certain laps de temps.

Dans votre projet Django, il est bon de créer ou d'implémenter un middleware personnalisé pour suivre et limiter les requêtes de l'utilisateur en fonction de l'adresse IP de l'utilisateur. Si vous ne pouvez pas créer un middleware personnalisé, vous pouvez utiliser le package [django-rate limiting](https://django-ratelimit.readthedocs.io/en/stable/).

### Activer le middleware CSRF

Le middleware de falsification de requête inter-sites (CSRF) dans Django est un outil de sécurité intégré qui protège contre les attaques CSRF en validant le jeton CSRF lors de la réalisation de requêtes, comme lorsqu'un utilisateur souhaite se connecter.

Il est bon d'activer le middleware CSRF de Django dans votre **settings.py**.

```python
MIDDLEWARE = [
 ...
 'django.middleware.csrf.CsrfViewMiddleware'
 ...
]
```

### Toujours utiliser les jetons CSRF

Les jetons de falsification de requête inter-sites (CSRF) sont des données aléatoires générées par votre serveur et incluses comme champs cachés dans vos formulaires HTML ou ajoutées aux requêtes AJAX.

Les jetons CSRF fonctionnent avec le middleware CSRF, vous ne pouvez pas utiliser l'un sans l'autre. Lors de l'utilisation des jetons CSRF, Django gère automatiquement les jetons pour vous lorsque vous utilisez la balise de modèle `{% csrf_token %}`.

```html
&lt;form method="post">
    {% csrf_token %}
    ...
&lt;/form>

```

## Liste de contrôle de sécurité intégrée de Django

Peu de développeurs le savent, mais Django dispose d'une liste de contrôle de sécurité intégrée pour vous assurer de déployer un projet sécurisé.

Il s'agit d'une commande qui analyse votre **settings.py** et vérifie si vous respectez les directives de sécurité de Django ou si vous avez des vulnérabilités que les pirates pourraient exploiter. La commande est `python manage.py check --deploy`

Lorsque vous exécutez la commande, vous devriez voir tous les avertissements et pouvez voir certaines erreurs de projet (si vous en avez), quelque chose comme ceci :

![preencoded.png](https://lh7-us.googleusercontent.com/TJJQfxXbJaC4e9Jnwdu16ESNJa4rr6Ju84ltFfc9cIY_CtCUzNtY7ovh1k-fv9HamrY-dPVUn1izNw5_0siyuCSlP3dQNIN4YU57L1TNTj2e5ZLc2LIKx-WQV2yTCPNZcC8CWwcbYmW5MD5-z0oe-zRPmNo0x_hy=s2048)
_Capture d'écran montrant les résultats de la commande_

## Autres pratiques de sécurité

En plus des pratiques de sécurité ciblant des vulnérabilités web spécifiques, la mise en œuvre de pratiques mineures peut également renforcer la sécurité globale de votre application.

1. Implémentez un moyen de surveiller en continu votre application Django déployée pour détecter et répondre aux incidents de sécurité ou aux vulnérabilités en temps réel.
2. Mettez à jour votre framework Django, vos dépendances et vos bibliothèques tierces tous les 2 à 4 mois afin que votre projet soit à jour et utilise les derniers correctifs de sécurité et soit exempt de bugs.
3. Vous pouvez également implémenter la journalisation pour surveiller et enregistrer les changements ou activités liés à la sécurité se produisant dans vos projets. Cela peut également prendre note des incidents de sécurité possibles.

## Conclusion

En conclusion, sécuriser une application Django nécessite beaucoup d'attention et une stratégie multicouche. Cela inclut la mise en œuvre d'une authentification sécurisée, la validation des entrées utilisateur, la garantie d'une communication chiffrée de bout en bout (qu'il s'agisse de client à serveur ou d'utilisateur à utilisateur), et l'application de mesures de limitation de débit.

Ces pratiques contribuent à un projet plus robuste et sécurisé.