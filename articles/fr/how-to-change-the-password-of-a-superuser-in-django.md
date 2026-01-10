---
title: Comment changer le mot de passe d'un superutilisateur dans Django
subtitle: ''
author: Udemezue John
co_authors: []
series: null
date: '2025-04-23T13:59:23.545Z'
originalURL: https://freecodecamp.org/news/how-to-change-the-password-of-a-superuser-in-django
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1745416742960/89cce35f-2e91-4329-8fea-0d1551bea2c7.png
tags:
- name: Python
  slug: python
- name: Django
  slug: django
- name: Security
  slug: security
seo_title: Comment changer le mot de passe d'un superutilisateur dans Django
seo_desc: 'Changing a superuser password in Django might sound like a big task, but
  it’s one of the easiest things to do once you know how.

  If you’re working on a Django project – whether it’s a hobby blog, a client’s website,
  or a bigger web application – mana...'
---

Changer le mot de passe d'un superutilisateur dans Django peut sembler une tâche ardue, mais c'est l'une des choses les plus faciles à faire une fois que vous savez comment.

Si vous travaillez sur un projet Django - qu'il s'agisse d'un blog de loisir, du site web d'un client ou d'une application web plus importante - la gestion sécurisée de vos comptes administrateurs est une nécessité.

Et une partie clé de cela ? S'assurer que votre mot de passe de superutilisateur est fort, sécurisé et facile pour *vous* à mettre à jour.

Vous pourriez faire cela parce que vous avez oublié l'ancien mot de passe, que vous transmettez le projet à quelqu'un d'autre, ou que vous renforcez la sécurité après un changement d'équipe.

Quelle que soit votre raison, ce guide vous guidera à travers les moyens les plus faciles et les plus sûrs de changer un mot de passe de superutilisateur dans Django.

Je vais tout décomposer en langage simple, sans jargon technique lourd ni suppositions.

Commençons.

### Ce que nous allons couvrir :

* [Pourquoi changer le mot de passe du superutilisateur est important](#heading-pourquoi-changer-le-mot-de-passe-du-superutilisateur-est-important)

* [3 méthodes simples pour changer un mot de passe de superutilisateur Django](#heading-3-methodes-simples-pour-changer-un-mot-de-passe-de-superutilisateur-django)

    * [Méthode 1 : Utiliser la commande intégrée de Django](#heading-methode-1-utiliser-la-commande-integree-de-django)

    * [Méthode 2 : Utiliser le shell Django](#heading-methode-2-utiliser-le-shell-django)

    * [Méthode 3 : Utiliser l'admin Django (si vous êtes connecté)](#heading-methode-3-utiliser-ladmin-django-si-vous-etes-connecte)

* [Bonus : Vous avez oublié votre nom d'utilisateur de superutilisateur ?](#heading-bonus-vous-avez-oublie-votre-nom-dutilisateur-de-superutilisateur)

* [FAQ](#heading-faq)

    * [Que faire si j'ai oublié à la fois le nom d'utilisateur et le mot de passe ?](#heading-que-faire-si-jai-oublie-a-la-fois-le-nom-dutilisateur-et-le-mot-de-passe)

    * [Cela déconnectera-t-il les autres utilisateurs ?](#heading-cela-deconnectera-t-il-les-autres-utilisateurs)

    * [Puis-je changer le mot de passe directement depuis la base de données ?](#heading-puis-je-changer-le-mot-de-passe-directement-depuis-la-base-de-donnees)

    * [Comment savoir si mon nouveau mot de passe est sécurisé ?](#heading-comment-savoir-si-mon-nouveau-mot-de-passe-est-securise)

* [Réflexions finales](#heading-reflexions-finales)

* [Lectures complémentaires et outils](#heading-lectures-complementaires-et-outils)

## Pourquoi changer le mot de passe du superutilisateur est important

Votre superutilisateur Django a un accès complet au tableau de bord d'administration. Cela signifie qu'il peut ajouter ou supprimer des utilisateurs, modifier des données, gérer les paramètres - tout. Si ce compte est compromis, c'est tout le site qui est en danger.

Voici ce qui pourrait mal se passer si le mot de passe est faible ou obsolète :

* Quelqu'un pourrait supprimer votre base de données.

* Un pirate pourrait injecter des données malveillantes.

* Des informations privées des utilisateurs pourraient être exposées.

Selon le [Rapport d'enquête sur les violations de données de Verizon](https://www.verizon.com/business/en-sg/resources/articles/analyzing-covid-19-data-breach-landscape/), plus de **80%** des violations liées au piratage sont dues à des mots de passe compromis ou faibles. C'est un énorme risque pour quelque chose qui peut être corrigé en quelques minutes.

Alors assurons-nous que votre admin Django est bien verrouillé - sans rien casser.

## 3 méthodes simples pour changer un mot de passe de superutilisateur Django

Je vais vous montrer trois méthodes différentes pour mettre à jour votre mot de passe de superutilisateur. Vous n'avez besoin de choisir qu'une seule méthode qui correspond à votre configuration actuelle.

### Méthode 1 : Utiliser la commande intégrée de Django

Si vous avez accès à la ligne de commande et à l'environnement virtuel de votre projet, c'est la méthode la plus propre.

#### **Activez votre environnement virtuel**

Cela dépend de votre configuration, mais si vous utilisez `venv`, cela pourrait ressembler à ceci :

```bash
source venv/bin/activate
```

Ou sur Windows :

```python
venv\Scripts\activate
```

#### **Accédez à votre dossier de projet**

C'est là que se trouve `manage.py` :

```bash
cd votre_dossier_de_projet
```

#### **Exécutez la commande suivante :**

```bash
python manage.py changepassword votre_nom_dutilisateur_superutilisateur
```

Exemple :

```bash
python manage.py changepassword admin
```

Django vous demandera ensuite de saisir un nouveau mot de passe. Tapez-le, appuyez sur Entrée, confirmez-le à nouveau, et c'est fait.

C'est tout. Vous venez de changer votre mot de passe de superutilisateur !

### Méthode 2 : Utiliser le shell Django

Peut-être que vous ne vous souvenez pas du nom d'utilisateur ou que vous voulez plus de contrôle. Le shell Django vous permet d'interagir directement avec votre base de données en utilisant Python.

Voici comment faire :

Tout d'abord, ouvrez le shell :

```bash
python manage.py shell
```

Ensuite, exécutez le code suivant :

```python
from django.contrib.auth import get_user_model

User = get_user_model()

user = User.objects.get(username="admin")  # Remplacez 'admin' par votre nom d'utilisateur
user.set_password("nouveau_mot_de_passe_securise")   # Remplacez par votre nouveau mot de passe
user.save()
```

Maintenant, quittez le shell :

```python
exit()
```

C'est tout. Cette méthode est particulièrement utile si vous travaillez dans un environnement de staging ou si vous faites des choses de manière programmatique.

### Méthode 3 : Utiliser l'admin Django (si vous êtes connecté)

Cette méthode ne fonctionne que si vous pouvez encore vous connecter avec le compte superutilisateur actuel.

1. Allez sur votre page d'administration Django, généralement à l'adresse `http://127.0.0.1:8000/admin/`.

2. Connectez-vous avec vos identifiants actuels.

3. Cliquez sur **Utilisateurs**.

4. Trouvez votre compte superutilisateur et cliquez dessus.

5. Faites défiler jusqu'à la section "Mot de passe" et cliquez sur **"ce formulaire"** sous le message "Les mots de passe en clair ne sont pas stockés...".

6. Saisissez votre nouveau mot de passe deux fois et enregistrez.

Cette méthode est super rapide et ne nécessite aucun code.

## Bonus : Vous avez oublié votre nom d'utilisateur de superutilisateur ?

Si vous ne vous souvenez pas du nom d'utilisateur exact de votre superutilisateur, pas de problème. Vous pouvez lister tous les utilisateurs comme ceci :

```bash
python manage.py shell
```

Ensuite :

```python
from django.contrib.auth import get_user_model

User = get_user_model()

for user in User.objects.all():
    print(user.username)
```

Cela affichera tous les noms d'utilisateur de votre système, y compris votre superutilisateur.

## FAQ

### **Que faire si j'ai oublié à la fois le nom d'utilisateur et le mot de passe ?**

Utilisez la méthode shell ci-dessus pour lister tous les noms d'utilisateur, puis réinitialisez-le en utilisant soit le shell soit la commande `changepassword`.

### **Cela déconnectera-t-il les autres utilisateurs ?**

Changer votre mot de passe de superutilisateur n'affectera pas les autres utilisateurs sauf si vous avez une logique personnalisée liée aux sessions. Pour la plupart des projets, tout le reste continue de fonctionner normalement.

### **Puis-je changer le mot de passe directement depuis la base de données ?**

Techniquement oui, mais **ne le faites pas**. Les mots de passe dans Django sont hachés en utilisant PBKDF2 par défaut. Si vous entrez quelque chose manuellement dans la base de données, cela ne fonctionnera pas sauf si c'est haché de la bonne manière. Utilisez toujours le shell Django ou le panneau d'administration à la place.

### **Comment savoir si mon nouveau mot de passe est sécurisé ?**

Django vérifie la force du mot de passe par défaut. Mais si vous voulez être extra prudent, utilisez un outil comme [Bitwarden Password Generator](https://bitwarden.com/password-generator/) ou [1Password's Generator](https://1password.com/password-generator/).

## Réflexions finales

C'est à peu près tout ce que vous devez savoir pour changer votre mot de passe de superutilisateur dans Django. C'est rapide, sûr, et une fois que vous l'avez fait une fois, cela deviendra une seconde nature.

Ce sont des actions comme celle-ci qui vont loin pour garder vos projets Django sécurisés. Et comme cela ne prend qu'une minute ou deux, il n'y a aucune raison de le reporter.

Continuons la conversation, connectez-vous avec moi sur [x.com/_udemezue](http://X.com/_udemezue)

### Lectures complémentaires et outils

* [Documentation officielle de Django sur le changement de mot de passe](https://docs.djangoproject.com/en/stable/ref/django-admin/#changepassword)

* [Comment Django stocke les mots de passe de manière sécurisée](https://docs.djangoproject.com/en/stable/topics/auth/passwords/)

* [PBKDF2 expliqué sur OWASP](https://owasp.org/www-community/vulnerabilities/Using_Insufficiently_Random_Values)