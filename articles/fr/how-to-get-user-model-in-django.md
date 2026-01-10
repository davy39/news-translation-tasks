---
title: Comment obtenir le modèle d'utilisateur dans Django – Un guide simple avec
  des exemples
subtitle: ''
author: Udemezue John
co_authors: []
series: null
date: '2025-04-30T15:19:33.742Z'
originalURL: https://freecodecamp.org/news/how-to-get-user-model-in-django
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1746026362647/7b47e9e7-6baf-409a-8654-0ad1eb528e31.png
tags:
- name: Python
  slug: python
- name: Django
  slug: django
seo_title: Comment obtenir le modèle d'utilisateur dans Django – Un guide simple avec
  des exemples
seo_desc: 'When I’m working with Django, one of the first things I often need to do
  is work with users – like getting the logged-in user, creating a new one, or extending
  the default user model to add more information.

  Now, Django has a built-in User model, but...'
---

Lorsque je travaille avec Django, l'une des premières choses que je dois souvent faire est de travailler avec les utilisateurs – comme obtenir l'utilisateur connecté, en créer un nouveau ou étendre le modèle d'utilisateur par défaut pour ajouter plus d'informations.

Maintenant, Django dispose d'un modèle `User` intégré, mais parfois vous pourriez vouloir un modèle personnalisé. C'est là que les choses peuvent devenir un peu confuses si vous débutez.

La bonne nouvelle ? Obtenir le modèle d'utilisateur dans Django est très simple une fois que vous comprenez comment Django est configuré.

Aujourd'hui, je vais vous expliquer exactement comment obtenir le modèle d'utilisateur dans Django, pourquoi c'est important, vous montrer du code réel que vous pouvez utiliser, et répondre à quelques questions courantes que les gens ont généralement sur ce sujet.

Commençons sans plus tarder.

## Table des matières

* [Pourquoi obtenir le modèle d'utilisateur correctement est important](#heading-pourquoi-obtenir-le-modele-dutilisateur-correctement-est-important)
    
* [Comment obtenir le modèle d'utilisateur dans Django](#heading-comment-obtenir-le-modele-dutilisateur-dans-django)
    
* [Exemple complet : Utilisation du modèle d'utilisateur](#heading-exemple-complet-utilisation-du-modele-dutilisateur)
    
* [Quand utiliser settings.AUTH\_USER\_MODEL](#heading-quand-utiliser-settingsauthusermodel)
    
* [Résumé rapide](#heading-resume-rapide)
    
* [Erreurs courantes à éviter](#heading-erreurs-courantes-a-eviter)
    
* [FAQ](#heading-faq)
    
    * [1. Puis-je accéder directement à request.user ?](#heading-1-puis-je-acceder-directement-a-requestuser)
        
    * [2. Que se passe-t-il si j'appelle get\_user\_model() plusieurs fois ?](#heading-2-que-se-passe-t-il-si-jappelle-getusermodel-plusieurs-fois)
        
    * [3. Comment savoir si j'utilise un modèle d'utilisateur personnalisé ?](#heading-3-comment-savoir-si-jutilise-un-modele-dutilisateur-personnalise)
        
    * [4. Quand devrais-je créer un modèle d'utilisateur personnalisé ?](#heading-4-quand-devrais-je-creer-un-modele-dutilisateur-personnalise)
        
* [Ressources supplémentaires](#heading-ressources-supplementaires)
    
* [Conclusion](#heading-conclusion)
    

## Pourquoi obtenir le modèle d'utilisateur correctement est important

Avant toute chose, il est important de savoir pourquoi cela compte.

Les projets Django dépendent fortement des informations utilisateur – non seulement pour les connexions, mais aussi pour les permissions, les profils, la gestion administrative, et bien plus.

Si vous obtenez le modèle d'utilisateur de la mauvaise manière, vous pouvez facilement rencontrer des problèmes plus tard, surtout si vous personnalisez votre modèle d'utilisateur.

Django vous avertit même à ce sujet dans sa [documentation officielle](https://docs.djangoproject.com/en/stable/topics/auth/customizing/). Si vous n'utilisez pas la bonne méthode pour accéder au modèle d'utilisateur, votre projet pourrait casser lorsque vous le modifiez ou l'étendez.

C'est pourquoi il est super important d'obtenir toujours le modèle d'utilisateur de la manière *recommandée*, que je vais vous montrer ensuite.

## Comment obtenir le modèle d'utilisateur dans Django

Très bien, voici la manière la plus simple d'obtenir le modèle d'utilisateur dans Django :

```python
from django.contrib.auth import get_user_model

User = get_user_model()
```

**Que se passe-t-il ici ?**

* `get_user_model()` est une fonction intégrée de Django.
    
* Elle retourne le modèle User correct – que vous utilisiez celui par défaut ou un modèle personnalisé que vous avez créé.
    

Si vous vous demandez pourquoi ne pas simplement importer `from django.contrib.auth.models import User`, la raison est la suivante : si vous remplacez un jour le modèle User par défaut par un modèle personnalisé, une importation directe comme celle-ci cassera votre code.

En utilisant `get_user_model()`, vous restez en sécurité et vous préparez votre projet pour l'avenir.

## Exemple complet : Utilisation du modèle d'utilisateur

Regardons un exemple complet et fonctionnel, pas seulement un petit extrait.

Imaginez que vous souhaitez créer un nouvel utilisateur dans une vue Django :

```python
from django.contrib.auth import get_user_model
from django.http import HttpResponse

def create_user_view(request):
    User = get_user_model()
    user = User.objects.create_user(username='newuser', password='securepassword123')
    return HttpResponse(f"Created user: {user.username}")
```

Dans cet exemple :

* D'abord, j'obtiens le modèle d'utilisateur avec `get_user_model()`.
    
* Ensuite, j'utilise la méthode intégrée `create_user` de Django pour créer un utilisateur en toute sécurité.
    
* Enfin, je renvoie une simple réponse HTTP montrant le nom d'utilisateur créé.
    

Remarquez à quel point c'est propre et flexible – peu importe quel modèle d'utilisateur vous utilisez sous le capot.

## Quand utiliser `settings.AUTH_USER_MODEL`

Une autre chose que vous verrez souvent dans les projets Django est quelque chose comme ceci :

```python
from django.conf import settings

settings.AUTH_USER_MODEL
```

Cela ne **récupère** pas le modèle d'utilisateur. Au lieu de cela, cela vous donne le **chemin** sous forme de chaîne vers le modèle d'utilisateur, comme `"auth.User"` (pour le modèle par défaut) ou `"myapp.MyCustomUser"` si vous l'avez personnalisé.

Vous utilisez généralement `settings.AUTH_USER_MODEL` dans votre **models.py** lorsque vous souhaitez lier au modèle User dans un ForeignKey, OneToOneField ou ManyToManyField.

Par exemple :

```python
from django.conf import settings
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField()
```

Ici, le modèle `Profile` est lié au modèle d'utilisateur correct. Encore une fois, cela garde votre projet flexible et prêt pour l'avenir.

## Résumé rapide

| Situation | Que utiliser |
| --- | --- |
| Obtenir le modèle User réel dans le code Python (vues, formulaires, admin, etc.) | `get_user_model()` |
| Faire référence au modèle User dans les relations de base de données (ForeignKey, OneToOneField, etc.) | `settings.AUTH_USER_MODEL` |

Rappelez-vous de ce tableau – il évite beaucoup de maux de tête plus tard !

## Erreurs courantes à éviter

* **Importer directement** `User` : Ne faites jamais simplement `from django.contrib.auth.models import User` sauf si vous êtes sûr à 100 % de rester avec le modèle par défaut pour toujours (non recommandé).
    
* **Coder en dur les relations** : Si vous écrivez quelque chose comme `ForeignKey('auth.User')` au lieu d'utiliser `settings.AUTH_USER_MODEL`, cela cassera si vous passez un jour à un modèle d'utilisateur personnalisé.
    
* **Ne pas créer de modèles d'utilisateur personnalisés tôt** : Si vous pensez que vous pourriez un jour avoir besoin d'un modèle d'utilisateur personnalisé (comme ajouter des numéros de téléphone, des champs de profil supplémentaires), configurez-le tôt. Passer à un modèle personnalisé plus tard est douloureux une fois que vous avez une base de données pleine d'utilisateurs.
    

## FAQ

### 1. Puis-je accéder directement à `request.user` ?

Oui ! Dans les vues, `request.user` vous donne l'objet utilisateur actuellement connecté. En coulisses, Django utilise le modèle d'utilisateur correct, qu'il soit personnalisé ou par défaut.

### 2. Que se passe-t-il si j'appelle `get_user_model()` plusieurs fois ?

Aucun problème. Django le met en cache en interne, donc c'est efficace. N'hésitez pas à l'appeler où vous en avez besoin.

### 3. Comment savoir si j'utilise un modèle d'utilisateur personnalisé ?

Vérifiez votre fichier de paramètres Django (`settings.py`) et cherchez `AUTH_USER_MODEL`. S'il est défini (comme `'myapp.MyCustomUser'`, vous utilisez un modèle personnalisé. S'il n'est pas là, Django utilise le modèle par défaut.

### 4. Quand devrais-je créer un modèle d'utilisateur personnalisé ?

Si vous pensez même *un peu* que vous aurez besoin de champs comme le numéro de téléphone, la date de naissance, les photos de profil, etc., il est préférable de configurer un modèle personnalisé tôt.

Voici un excellent guide de la documentation officielle de Django sur la [personnalisation des modèles d'utilisateur](https://docs.djangoproject.com/en/stable/topics/auth/customizing/).

## Conclusion

Travailler avec les utilisateurs dans Django ne doit pas être compliqué. Une fois que vous savez utiliser `get_user_model()` lorsque vous avez besoin du modèle et `settings.AUTH_USER_MODEL` pour les relations de base de données, votre code reste propre, sûr et prêt pour tous les changements à venir.

Maintenant que vous savez comment obtenir le modèle d'utilisateur dans Django, quelle est une chose que vous aimeriez personnaliser concernant vos utilisateurs dans votre projet ? Envoyez-moi un message sur [X](http://x.com/_udemezue/).

Si vous voulez que je vous montre comment **construire** un modèle d'utilisateur personnalisé à partir de zéro, faites-le moi savoir – ce n'est pas difficile une fois que vous connaissez les étapes.

### Ressources supplémentaires

* [Documentation officielle de Django : Utilisation d'un modèle d'utilisateur personnalisé](https://docs.djangoproject.com/en/stable/topics/auth/customizing/)
    
* [Explication simple sur AbstractBaseUser vs AbstractUser](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html)
    
* [StackOverflow : Bonnes pratiques pour les modèles d'utilisateur Django](https://stackoverflow.com/questions/29725217/django-custom-user-model-best-practice)