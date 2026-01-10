---
title: Comment configurer un environnement de développement Django
subtitle: ''
author: Victoria (Burah) Poromon
co_authors: []
series: null
date: '2023-12-12T15:52:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-a-django-development-environment
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/DDE-cover.jpg
tags:
- name: Django
  slug: django
- name: Python
  slug: python
- name: virtualenv
  slug: virtualenv
seo_title: Comment configurer un environnement de développement Django
seo_desc: 'Django is a high-level web framework written in Python that encourages
  a rapid and realistic functional design. The Django web framework is free and open-source
  and is widely used to create both small and large web applications.

  In this tutorial, you...'
---

Django est un framework web de haut niveau écrit en Python qui encourage une conception fonctionnelle rapide et réaliste. Le framework web Django est gratuit et open-source et est largement utilisé pour créer des applications web petites et grandes.

Dans ce tutoriel, vous apprendrez les points suivants :

* Ce qu'est un environnement de développement,
* Ce qu'est un environnement virtuel,
* Comment créer un environnement virtuel Python, et
* Comment installer Django dans votre environnement virtuel.

Pour tirer le meilleur parti de ce tutoriel, vous devrez avoir une connaissance de base de l'utilisation d'un terminal/ligne de commande et avoir la dernière version stable de Python installée sur votre ordinateur.

## Qu'est-ce qu'un environnement de développement ?

Un environnement de développement est une installation de Django sur votre ordinateur local. La configuration de votre environnement est une étape importante dans le processus de développement de votre site web. Il fournit un espace isolé et contrôlé pour écrire, tester et déboguer votre code avant de le déployer dans un environnement de production.

## Qu'est-ce qu'un environnement virtuel ?

Un environnement virtuel est un espace qui vous permet d'isoler les dépendances et les configurations d'un projet d'un autre. Ainsi, vous pouvez créer différents projets avec différentes versions de bibliothèques, et ils n'interféreront pas les uns avec les autres.

Notez qu'il existe divers types d'environnements virtuels, mais dans ce tutoriel, nous nous concentrerons sur la création d'un environnement Python.

## Comment créer un environnement virtuel Python

En Python, plusieurs outils sont disponibles pour créer et gérer des environnements virtuels. En voici deux couramment utilisés :

### L'outil `venv` :

`venv` est un module intégré qui accompagne les versions de Python 3.3 et ultérieures. C'est un moyen simple et léger de créer un environnement virtuel.

Voici comment créer un environnement virtuel en utilisant `venv` :

```bash
python -m venv myenv

```

`myenv` est le nom de votre environnement virtuel. Vous pouvez utiliser un autre nom, mais utilisez toujours des lettres minuscules et n'ajoutez pas d'espaces. 

De plus, gardez le nom court pour qu'il soit facile à retenir. Les tirets sont autorisés et couramment utilisés. Par exemple, `my-env` au lieu de `myenv`.

### L'outil `virtualenv` :

`virtualenv` est un outil tiers pour créer un environnement virtuel. Ses fonctionnalités vous permettent de créer un environnement avec une version différente de Python de celle utilisée pour exécuter la commande `virtualenv`.

Voici comment créer un environnement virtuel en utilisant `virtualenv` :

```bash
# Pour macOS et Linux
pip install virtualenv
virtualenv myenv

# Pour Windows
pip install virtualenv
python -m virtualenv myenv

```

`pip install virtualenv` est une commande qui utilise le gestionnaire de paquets Python `pip` pour installer `virtualenv` globalement sur votre ordinateur. Après l'installation, `virtualenv myenv` crée un nouvel environnement virtuel nommé `myenv`. 

Tout comme lors de l'utilisation de l'outil `venv`, vous pouvez changer le nom de l'environnement. Mais n'oubliez pas de toujours les garder courts, utilisez des lettres minuscules et n'ajoutez pas d'espaces. Vous pouvez utiliser des tirets également.

## Installation de Django

Django vous fournit un ensemble de scripts Python pour créer et travailler avec des projets Django. Il est très flexible en termes d'endroit et de manière dont vous pouvez l'installer. Mais pour ce tutoriel, vous allez installer Django dans l'environnement virtuel que vous venez de créer.

Voici comment vous pouvez installer Django dans votre environnement virtuel, pour Linux et macOS :

```bash
# Activez votre environnement virtuel
source myenv/bin/activate

# Installez Django
pip install django

# Ou utilisez ceci pour spécifier la version
pip install django==4.2.7

```

Pour Windows :

```bash
# Activez votre environnement virtuel
myenv\Scripts\activate

# Installez Django
pip install django

# Ou utilisez ceci pour spécifier la version
pip install django==4.2.7

```

`pip` est un installeur de paquets pour Python qui est recommandé pour installer Django. La commande `pip install django` télécharge la dernière version de Django et l'installe dans votre environnement Python.

Après avoir travaillé sur votre projet, vous pouvez désactiver votre environnement virtuel en tapant la commande suivante dans votre terminal ou ligne de commande :

```bash
deactivate

```

### Comment vérifier votre installation de Django

Après l'installation, vous devez vérifier que Django est correctement installé dans votre environnement virtuel. Assurez-vous toujours d'activer votre environnement virtuel avant de vérifier votre installation.

Vérifiez votre installation de Django avec la commande suivante :

```bash
python -m django --version

```

La commande ci-dessus affichera la version de Django installée dans votre environnement virtuel.

Félicitations ! Votre environnement de développement Django est maintenant actif sur votre ordinateur.

## Conclusion

Django facilite le développement d'applications web en fournissant une base solide, en réduisant la répétition et en promouvant les meilleures pratiques.

L'installation de Django est la première étape dans la création d'un environnement pour vos projets web. Après ce processus, vous pouvez maintenant configurer votre projet Django, définir sa structure, configurer vos bases de données, créer vos applications et commencer à construire votre application web. Bon codage.