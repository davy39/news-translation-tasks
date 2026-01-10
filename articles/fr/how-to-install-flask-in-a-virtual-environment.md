---
title: Comment installer Flask dans un environnement virtuel
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-12T21:19:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-flask-in-a-virtual-environment
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9df1740569d1a4ca3a83.jpg
tags:
- name: Flask Framework
  slug: flask
- name: Python
  slug: python
- name: toothbrush
  slug: toothbrush
seo_title: Comment installer Flask dans un environnement virtuel
seo_desc: "If you wish to use Flask, you are in the right place! This guide will teach\
  \ you how to install Flask if you want to explore web development with it. \nJust\
  \ keep in mind that Flask might not always be the best choice – it gets difficult\
  \ to build large ..."
---

Si vous souhaitez utiliser Flask, vous êtes au bon endroit ! Ce guide vous apprendra à installer Flask si vous souhaitez explorer le développement web avec celui-ci. 

Gardez simplement à l'esprit que Flask n'est peut-être pas toujours le meilleur choix – il devient difficile de construire de grandes applications web avec celui-ci si vous êtes nouveau dans le développement web en Python. Peut-être devriez-vous vérifier Django comme autre option.

Flask est un micro-framework et vous pouvez choisir les fonctionnalités que vous souhaitez avoir par-dessus les fonctionnalités de base déjà présentes dans un framework web standard. 

**Assurez-vous d'abord d'avoir installé Python 3** et de l'utiliser dans un environnement virtuel.

Assurez-vous également de ne pas être déjà dans un environnement virtuel. Ensuite, créez un nouvel environnement virtuel, nommé `py3-flask`

```text
$ mkvirtualenv py3-flask --python=/usr/bin/python3
```

Maintenant, exécutez la commande `workon` pour voir une liste des environnements virtuels sur votre machine. Cela devrait lister `py3-flask` sur une ligne.

Après cela, activez cet environnement :

```text
$ workon py3-flask
```

Votre environnement virtuel sera activé avec une copie de l'interpréteur Python, avec les propriétés de Python 3. Vous devriez exécuter

```text
$ python --version
```

pour vous assurer que vous êtes bien dans un environnement Python 3.

Pour être clair, si vous avez déjà installé Django ou un autre framework, il ne devrait **pas** être dans cet environnement. Nous utilisons un environnement virtuel pour garder nos installations de différents frameworks séparées.

Pour être sûr, exécutez

```text
pip freeze
```

Assurez-vous que Django n'est pas listé dans la liste générée par la commande ci-dessus.

Maintenant, installons Flask. Si vous souhaitez en savoir plus, voici le [guide d'installation officiel](http://flask.pocoo.org/docs/0.10/installation/). Cependant, de nombreux développeurs préfèrent installer quelques paquets supplémentaires avec Flask pour plus de fonctionnalités.

Pour installer uniquement Flask, exécutez

```text
$ pip install flask
```

Lorsque vous exécutez `pip freeze` à nouveau, il devrait vous montrer `Flask` dans les paquets listés.

Il est fastidieux d'exécuter de longues commandes comme celle-ci. Heureusement, il existe quelque chose comme `package.json` dans le domaine Python également - une liste de dépendances, que le gestionnaire de paquets peut utiliser pour dupliquer l'environnement en les téléchargeant avec la version appropriée depuis le dépôt central.

La norme est d'utiliser `pip freeze` et de journaliser la sortie dans un fichier local, qui peut être contrôlé par source.

```text
$ pip freeze > requirements.txt
```

Voici le contenu de `requirements.txt` depuis mon environnement, après avoir installé ces paquets Flask. Vous pouvez ajouter ou supprimer des paquets au fur et à mesure que votre application grandit. Mais pour l'instant, copiez et collez simplement le contenu de ce qui suit dans un fichier texte dans le même répertoire où vous vous trouvez.

```text
Babel==2.2.0
Flask==0.10.1
Flask-Babel==0.9
Flask-Login==0.3.2
Flask-Mail==0.9.1
Flask-OpenID==1.2.5
Flask-SQLAlchemy==2.1
Flask-WTF==0.12
Flask-WhooshAlchemy==0.56
Jinja2==2.8
MarkupSafe==0.23
SQLAlchemy==1.0.12
Tempita==0.5.2
WTForms==2.1
Werkzeug==0.11.4
Whoosh==2.7.2
blinker==1.4
coverage==4.0.3
decorator==4.0.9
defusedxml==0.4.1
flipflop==1.0
guess-language==0.2
itsdangerous==0.24
pbr==1.8.1
python3-openid==3.0.9
pytz==2015.7
six==1.10.0
speaklater==1.3
sqlalchemy-migrate==0.10.0
sqlparse==0.1.18
```

Cette liste de paquets est tirée [d'ici](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).

Une fois que vous avez sauvegardé le fichier, exécutez simplement

```text
$ pip install -r requirements.txt
```

Le gestionnaire de paquets s'occupera d'installer les paquets manquants pour vous ! Et vous devriez commiter ce fichier avec votre système de contrôle de source.

La série de commandes ci-dessus suppose que vous avez une machine Linux ou Mac OSX. Ou que vous utilisez une boîte hébergée dans le cloud sur cloud9 ou Nitrous, ou peut-être que vous utilisez une boîte Vagrant.

Mais, si vous devez utiliser une machine Windows, envisagez d'utiliser Windows Powershell, au lieu de Windows CMD. La plupart des commandes seront les mêmes. Au cas où vous auriez besoin d'assistance, vous pourriez vouloir consulter [cette discussion Stack Overflow](http://stackoverflow.com/questions/17917254/how-to-install-flask-on-windows).