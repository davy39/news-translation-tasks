---
title: Comment changer votre clé secrète Django (sans casser votre application)
subtitle: ''
author: Udemezue John
co_authors: []
series: null
date: '2025-04-25T14:40:23.998Z'
originalURL: https://freecodecamp.org/news/how-to-change-your-django-secret-key-without-breaking-your-app
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1745592003292/023f4ddd-61d7-4e06-b616-31de7924f6a9.png
tags:
- name: Python
  slug: python
- name: Django
  slug: django
- name: Security
  slug: security
seo_title: Comment changer votre clé secrète Django (sans casser votre application)
seo_desc: 'If you''re working on a Django project, you''ve probably come across the
  SECRET_KEY in your settings file. It might seem like just another line of code,
  but it''s one of the most important pieces of your project.

  SECRET_KEY keeps your app secure by sign...'
---

Si vous travaillez sur un projet Django, vous avez probablement rencontré la `SECRET_KEY` dans votre fichier de paramètres. Cela peut sembler être juste une autre ligne de code, mais c'est l'un des éléments les plus importants de votre projet.

`SECRET_KEY` maintient votre application sécurisée en signant les cookies, les mots de passe et autres données sensibles. Et si elle est jamais exposée ou divulguée – oui, c'est un problème.

Changer votre `SECRET_KEY` Django est quelque chose que vous devez faire avec soin. Peut-être que votre clé a été commise sur GitHub (nous y sommes tous passés), ou vous voulez simplement la rafraîchir pour une meilleure sécurité.

Quelle que soit la raison, je vais vous guider à travers le processus pour le faire en toute sécurité sans rien casser. Je vais tout expliquer en anglais simple pour que vous ne soyez pas laissé dans l'incompréhension de ce qui vient de se passer.

Commençons.

## Qu'est-ce que la `SECRET_KEY` Django ?

La `SECRET_KEY` est une longue chaîne de caractères aléatoires stockée dans votre fichier `settings.py`. Elle est utilisée en interne par Django pour :

* Signer de manière sécurisée les cookies de session

* Générer des jetons de réinitialisation de mot de passe

* Protéger les données en utilisant la signature cryptographique

Voici à quoi elle ressemble dans votre projet Django :

```python
# settings.py
SECRET_KEY = 'django-insecure-12345supersecretrandomstring'
```

Si quelqu'un obtient accès à votre `SECRET_KEY`, il pourrait potentiellement :

* Forger des cookies de session et usurper l'identité des utilisateurs

* Réinitialiser les mots de passe ou falsifier les données signées

* Compromettre l'ensemble de l'application

Donc oui – c'est un peu un gros problème.

## Quand devez-vous changer votre clé secrète Django ?

Vous devez changer votre `SECRET_KEY` si :

* Vous l'avez accidentellement partagée dans du code public (comme GitHub)

* Elle était codée en dur dans un fichier, et vous voulez passer aux variables d'environnement

* Vous faites tourner les clés dans le cadre d'une politique de sécurité

* Vous suspectez qu'elle a été compromise

Toujours pas sûr que ce soit nécessaire ? Si la clé a déjà été partagée ou stockée là où quelqu'un d'autre pourrait y accéder, changez-la simplement.

## Comment changer votre `SECRET_KEY` Django en toute sécurité

### 1. **Générer une nouvelle clé secrète**

La clé doit être longue, aléatoire et sécurisée. Django ne fournit pas de commande pour cela directement, mais vous pouvez en générer une en utilisant Python.

Voici un script simple :

```python
from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())
```

Pour exécuter cela :

1. Ouvrez votre terminal

2. Lancez le shell Django avec `python manage.py shell`

3. Collez le script

Il retournera quelque chose comme :

```python
x3%6kn$mlg58+as!rcvnmvd8%(2p!p#&yk@r)+tdlj*w9kx!5gx
```

Copiez cela. Vous en aurez besoin dans une seconde.

### 2. **Stocker la clé de manière sécurisée (ne la codez pas en dur)**

Au lieu de la coller dans `settings.py`, il est préférable d'utiliser une variable d'environnement. Ainsi, vous ne risquez pas de l'exposer si vous partagez votre code.

Voici comment faire :

1. Ouvrez votre fichier `.env` (créez-en un s'il n'existe pas) :

```python
# .env
SECRET_KEY='x3%6kn$mlg58+as!rcvnmvd8%(2p!p#&yk@r)+tdlj*w9kx!5gx'
```

2. Installez `python-decouple` si ce n'est pas déjà fait :

```bash
pip install python-decouple
```

3. Mettez à jour votre `settings.py` :

```python
from decouple import config

SECRET_KEY = config('SECRET_KEY')
```

Maintenant, votre clé est stockée en dehors de votre code. Bien plus sûr.

### 3. **Commitez avec prudence**

Assurez-vous que :

* Votre fichier `.env` est ajouté à `.gitignore`

* Vous ne le poussez jamais dans votre dépôt

Voici à quoi devrait ressembler votre `.gitignore` :

```python
# .gitignore
.env
```

Vous seriez surpris de voir à quelle fréquence les fichiers `.env` sont poussés par accident. Vérifiez toujours avant de commiter.

### 4. **Redémarrez votre application**

Après avoir changé la clé, redémarrez votre serveur. Si vous utilisez une plateforme comme Heroku ou Docker, assurez-vous de mettre à jour la `SECRET_KEY` dans votre tableau de bord des variables d'environnement.

Pour Heroku :

```bash
heroku config:set SECRET_KEY='votre-nouvelle-cle'
```

Pour Docker :

```yaml
# docker-compose.yml
environment:
  - SECRET_KEY=votre-nouvelle-cle
```

### 5. **Reconnectez-vous (et demandez aux utilisateurs de faire de même)**

Changer la clé secrète invalide toutes les anciennes sessions. Donc, tout le monde (y compris vous) sera déconnecté. C'est un comportement attendu. Si vous gérez un site public, il est bon de prévenir les utilisateurs à l'avance.

## Que se passe-t-il si vous ne la changez pas ?

Si votre clé est compromise, les attaquants peuvent :

* Forger des données

* Détourner des comptes

* Casser les systèmes d'authentification

Ce n'est pas seulement une question de bonnes pratiques. C'est une question de sécurité dans le monde réel.

## FAQ

### Cela va-t-il casser mon application ?

Non, tant que vous redémarrez votre application et stockez la clé correctement, tout fonctionnera bien. Il faut simplement se rappeler que tous les utilisateurs seront déconnectés.

### Puis-je utiliser la même clé pour plusieurs projets ?

Non. Chaque projet doit avoir sa propre clé secrète unique.

### Puis-je faire tourner la clé régulièrement ?

Oui, mais gardez à l'esprit que la changer trop souvent déconnectera les utilisateurs à plusieurs reprises.

### J'ai oublié d'ajouter `.env` à `.gitignore`. Que faire maintenant ?

Régénérez la clé, mettez à jour votre projet et assurez-vous que le nouveau fichier `.env` n'est pas suivi.

## Réflexions finales

Changer votre `SECRET_KEY` Django peut sembler intimidant la première fois, mais c'est assez simple lorsque vous le décomposez. Tant que vous générez une clé sécurisée, la stockez en toute sécurité et ne l'exposez pas publiquement, vous faites du bon travail.

Une dernière chose – **quand avez-vous vérifié pour la dernière fois si votre clé secrète avait été accidentellement poussée sur GitHub ?** Ce pourrait être un bon moment pour y jeter un coup d'œil rapide.

### Ressources utiles

* [Docs Django – SECRET\_KEY](https://docs.djangoproject.com/en/stable/ref/settings/#std-setting-SECRET_KEY)

* [GitGuardian – Détection des secrets](https://www.gitguardian.com/)

* [12 Factor App – Config](https://12factor.net/config)

* [Python-Decouple GitHub](https://github.com/henriquebastos/python-decouple)