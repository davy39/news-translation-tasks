---
title: Comment étendre le modèle d'utilisateur Django
subtitle: ''
author: Udemezue John
co_authors: []
series: null
date: '2025-04-10T13:50:46.764Z'
originalURL: https://freecodecamp.org/news/how-to-extend-the-django-user-model
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1744293031605/8b4f148d-2e5f-49bd-90a8-7c295be2c2db.png
tags:
- name: Python
  slug: python
- name: Django
  slug: django
seo_title: Comment étendre le modèle d'utilisateur Django
seo_desc: 'If you''re working with Django and building anything that involves user
  accounts – like a blog, a store, or a membership site – you’ll likely hit a point
  where the default user model just isn’t enough.

  Maybe you want to add a profile picture, a phone ...'
---

Si vous travaillez avec Django et construisez quelque chose qui implique des comptes utilisateurs - comme un blog, une boutique ou un site d'adhésion - vous atteindrez probablement un point où le modèle d'utilisateur par défaut ne suffit tout simplement pas.

Peut-être souhaitez-vous ajouter une photo de profil, un numéro de téléphone ou des permissions supplémentaires.

Le problème est que l'extension du modèle d'utilisateur Django peut sembler déroutante au début. Cela semble technique, et Internet regorge de conseils qui sautent des détails importants ou deviennent trop complexes.

J'ai été là aussi.

Alors, dans ce guide, je vais vous expliquer comment étendre correctement le modèle d'utilisateur Django, étape par étape, sans ajouter de stress inutile à votre projet.

Je vous montrerai quelle méthode utiliser, quand l'utiliser, et comment éviter les erreurs courantes qui pourraient causer des problèmes plus tard.

Décomposons tout cela.

## Qu'est-ce qu'un modèle d'utilisateur dans Django ?

Django, un framework web Python populaire, est livré avec un modèle d'utilisateur intégré qui gère l'authentification et l'autorisation.

Le **modèle d'utilisateur** est essentiellement une table de base de données et une classe Python correspondante qui stocke les informations de base sur les utilisateurs de votre application, comme les noms d'utilisateur, les mots de passe, les adresses e-mail et autres détails essentiels.

Parce que de nombreux projets nécessitent des données ou des comportements utilisateur supplémentaires, l'extension ou la mise à jour du modèle d'utilisateur peut être très utile.

Dans de nombreuses applications, vous pourriez vouloir ajouter des champs supplémentaires pour capturer plus de détails sur vos utilisateurs. Par exemple, vous pourriez avoir besoin d'ajouter :

* Une photo de profil pour afficher un avatar pour chaque utilisateur.

* Un numéro de téléphone pour le contact ou l'authentification multifactorielle.

* Une biographie ou une courte description

* Des permissions ou des attributs supplémentaires qui ne sont pas couverts par les champs par défaut de Django, permettant à votre application de contrôler l'accès ou de personnaliser le contenu plus efficacement.

Vous pourriez également vouloir faire des choses comme suivre les préférences et les rôles des utilisateurs. Ou vous pourriez utiliser un e-mail comme nom d'utilisateur et vouloir personnaliser le comportement de connexion.

Ces modifications sont significatives car elles vont au-delà des capacités par défaut du modèle d'utilisateur intégré de Django. Et essayer de faire entrer ces informations supplémentaires dans le modèle d'utilisateur intégré sans le faire correctement peut causer des bugs ou casser vos migrations de base de données. Heureusement, Django nous offre quelques façons propres de le faire.

En étendant le modèle, vous vous assurez que toutes les parties de votre système - formulaires, vues, backends d'authentification et interfaces administratives - disposent des données supplémentaires dont elles ont besoin pour gérer correctement les utilisateurs.

Sans de telles personnalisations, vous pourriez rencontrer des limitations lorsque vous essayez de mettre en œuvre des fonctionnalités qui nécessitent des informations supplémentaires liées aux utilisateurs.

## **Prérequis**

Avant de plonger dans l'extension du modèle d'utilisateur Django, vous devriez avoir :

* **Connaissance de base de Django** : Familiarité avec la structure du projet Django, les modèles, les vues et les templates.

* **Compréhension de Python** : Puisque Django est un framework Python, une connaissance pratique de Python est nécessaire.

* **Expérience avec le modèle d'utilisateur par défaut de Django** : Savoir comment Django gère l'authentification et les sessions utilisateur fournit une base solide pour personnaliser le modèle d'utilisateur.

* **Un environnement de développement** : Assurez-vous d'avoir une installation Django fonctionnelle, un éditeur de code et une base de données appropriée configurée (par exemple, SQLite pour le développement).

Je supposerai ces prérequis si vous êtes à l'aise avec la création et l'exécution de projets Django.

Avec ces bases en place, vous serez mieux préparé à étendre le modèle d'utilisateur efficacement, que vous ajoutiez des champs supplémentaires pour des photos de profil, des numéros de téléphone ou des permissions supplémentaires.

## Trois façons d'étendre le modèle d'utilisateur

Il existe trois approches principales pour étendre le modèle d'utilisateur dans Django :

### 1. **Créer un modèle de profil utilisateur (relation un-à-un)**

C'est l'option la plus facile et la plus sûre si votre projet utilise déjà le modèle d'utilisateur par défaut de Django et que vous ne voulez pas le changer.

Vous créez un nouveau modèle qui se lie à l'utilisateur avec un champ un-à-un. Ensuite, vous stockez toutes les informations supplémentaires dans ce modèle de profil.

**Exemple :**

```python
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    profile_picture = models.ImageField(upload_to='profile_pics', null=True, blank=True)
```

Vous pouvez connecter le profil automatiquement en utilisant les signaux Django :

```python
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()
```

Cette approche est la meilleure pour les projets qui sont déjà en ligne ou où vous voulez garder les choses simples.

### 2. **Étendre AbstractUser**

C'est la meilleure option si vous commencez un nouveau projet et que vous voulez un contrôle total sur le modèle d'utilisateur. Vous créez votre modèle d'utilisateur personnalisé en sous-classant `AbstractUser`.

Cela vous permet d'ajouter des champs supplémentaires directement dans le modèle d'utilisateur sans changer le comportement d'authentification de base.

**Exemple :**

```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', null=True, blank=True)
```

Ensuite, dans vos paramètres :

```python
AUTH_USER_MODEL = 'yourapp.CustomUser'
```

Vous devez définir `AUTH_USER_MODEL` avant d'exécuter la première migration. Ne sautez pas cette étape, ou vous rencontrerez des erreurs de migration plus tard.

Cette approche est la meilleure pour les nouveaux projets où vous voulez une flexibilité totale.

### 3. **Étendre AbstractBaseUser**

C'est l'option la plus avancée. Vous créez votre modèle d'utilisateur à partir de zéro, en contrôlant même le fonctionnement de l'authentification. C'est idéal si vous avez besoin d'utiliser un e-mail au lieu d'un nom d'utilisateur ou si vous voulez personnaliser complètement le processus de connexion.

Mais soyons honnêtes : c'est aussi plus de travail. Vous devrez configurer votre propre gestionnaire et gérer les permissions manuellement.

Cette approche est la meilleure pour les projets avec des exigences utilisateur complexes ou des flux de connexion personnalisés.

## Quelle méthode devez-vous utiliser ?

Si vous avez déjà un projet fonctionnel et que vous avez juste besoin d'ajouter quelques champs supplémentaires, restez avec le modèle de profil utilisateur.

Si vous commencez à partir de zéro et que vous voulez ajouter des champs personnalisés dès le début, optez pour AbstractUser.

N'utilisez AbstractBaseUser que si vous avez besoin d'un contrôle total.

## Erreurs courantes à éviter

* Changer `AUTH_USER_MODEL` après avoir exécuté des migrations (cela casse votre base de données)

* Oublier de définir `AUTH_USER_MODEL` dans `settings.py`

* Ne pas mettre à jour admin.py lors de l'utilisation d'un modèle d'utilisateur personnalisé (plus d'informations à ce sujet dans la section suivante)

* Ne pas créer un `CustomUserManager` lors de l'utilisation de `AbstractBaseUser`

## Le faire fonctionner avec Django Admin

Si vous utilisez `AbstractUser`, vous devrez mettre à jour votre panneau d'administration pour reconnaître votre modèle d'utilisateur personnalisé.

Voici un exemple rapide :

```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'profile_picture')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
```

De cette façon, vous aurez toujours toutes les fonctionnalités d'administration par défaut, mais avec vos champs personnalisés ajoutés.

## FAQ

### Dois-je utiliser AbstractBaseUser pour utiliser un e-mail comme nom d'utilisateur ?

Pas toujours. Vous pouvez utiliser `AbstractUser` et simplement masquer le champ du nom d'utilisateur si vous voulez une connexion par e-mail, mais `AbstractBaseUser` vous donne un contrôle total si nécessaire.

### Puis-je passer à un modèle d'utilisateur personnalisé après avoir commencé mon projet ?

Techniquement, oui, mais c'est très risqué. Vous devriez migrer toutes vos données manuellement, ce qui peut être douloureux. Si vous le pouvez, planifiez-le dès le début.

### Que se passe-t-il si j'oublie de définir `AUTH_USER_MODEL` ?

Django utilisera le modèle `User` par défaut, et le changer plus tard peut causer des problèmes majeurs avec votre base de données et vos migrations. Alors n'oubliez pas !

## Réflexions finales

Étendre le modèle d'utilisateur Django peut sembler une grosse affaire au début, mais une fois que vous savez quelle méthode utiliser, cela devient juste une autre partie de la configuration de votre projet.

Prenez un moment pour réfléchir aux besoins de votre projet avant de vous lancer. Commencer avec la bonne approche vous évitera beaucoup de maux de tête plus tard.

Alors—comment prévoyez-vous d'étendre votre modèle d'utilisateur Django, et quels champs devez-vous ajouter ?

## Ressources supplémentaires

* [Documentation officielle de Django sur les modèles d'utilisateur personnalisés](https://docs.djangoproject.com/en/stable/topics/auth/customizing/)

* [Utilisation efficace des signaux Django](https://docs.djangoproject.com/en/stable/topics/signals/)

* [Conseils et astuces Django sur StackOverflow](https://stackoverflow.com/questions/tagged/django)

* [Comment commencer dans la tech sans expérience](https://tchelete.com/how-to-get-started-in-tech-with-no-experience/)