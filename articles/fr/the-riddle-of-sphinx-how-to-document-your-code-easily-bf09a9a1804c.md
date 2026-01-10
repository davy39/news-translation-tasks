---
title: 'L''Énigme de Sphinx : Comment Documenter Votre Code Facilement'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-19T11:10:16.000Z'
originalURL: https://freecodecamp.org/news/the-riddle-of-sphinx-how-to-document-your-code-easily-bf09a9a1804c
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca90e740569d1a4ca821e.jpg
tags:
- name: documentation
  slug: documentation
- name: GitHub
  slug: github
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: 'L''Énigme de Sphinx : Comment Documenter Votre Code Facilement'
seo_desc: 'By Dalya Gartzman

  Why Am I Here?

  You, the reader, are here because you wrote some awesome tool in Python, and you
  want to make it accessible and easy to use.

  I, the writer, am here because I was right where you are a few months ago. I wanted
  to use t...'
---

Par Dalya Gartzman

### Pourquoi Suis-Je Ici ?

Vous, le lecteur, êtes ici parce que vous avez écrit un outil génial en Python, et vous souhaitez le rendre accessible et facile à utiliser.

Moi, l'auteure, je suis ici parce que j'étais exactement à votre place il y a quelques mois. Je voulais utiliser le package [Sphinx](http://www.sphinx-doc.org/en/master/) pour créer une documentation de style ReadTheDocs pour mon projet.

J'ai trouvé l'intégration de Sphinx non triviale, c'est pourquoi j'ai créé [ce dépôt GitHub](https://github.com/DalyaG/Sphinx185) qui peut être utilisé comme modèle pour **votre** projet.

**Avant de commencer, quelques hypothèses de base, pour nous assurer que nous sommes sur la même longueur d'onde :**

* Vous écrivez en Python.
* Vous avez écrit des [docstrings](https://en.wikipedia.org/wiki/Docstring#Python) pour les morceaux de code que vous souhaitez documenter.
* Votre objectif est de créer une documentation de style [ReadTheDocs](https://docs.readthedocs.io/en/latest/) qui, au moins partiellement, se générera automatiquement.
* Vous savez que **en 10 minutes vous pourriez publier la première version** de votre documentation, qui ressemblera à quelque chose comme [ci](https://dalyag.github.io/Sphinx185/index.html) :

![Image](https://cdn-media-1.freecodecamp.org/images/g8g3D4mCEhXpqKyjDM2RjySgqLlo4gZcViku)

### Partie 1 - Préparation

* Installez Sphinx : `pip install sphinx`
* Allez sur [github.com/DalyaG/Sphinx185](https://github.com/DalyaG/Sphinx185) :
* Téléchargez le dossier `documentation_template_for_your_next_project`
* Copiez-le dans votre projet
* Renommez le dossier `documentation`

![Image](https://cdn-media-1.freecodecamp.org/images/CYOS9MopVTLHOshtpGkqwYFcddBNWui4WMNx)

### Partie 2 - Personnalisation

* Ouvrez le fichier `<votre_projet>/documentation/conf.py` dans votre éditeur préféré. Cherchez le motif `#CHANGEME#` et suivez les instructions.
* De même, éditez le fichier `<votre_projet>/documentation/index.rst` et suivez les instructions en ligne.

![Image](https://cdn-media-1.freecodecamp.org/images/zx3u0k2vQCGT5NKfSvks3flwgONlK4vi72U8)

![Image](https://cdn-media-1.freecodecamp.org/images/n6a72jLWaFOwE1Dc0ip6CT2K-3Bqp9gD43B0)

![Image](https://cdn-media-1.freecodecamp.org/images/36Kf81INhsKdDkppxQCbETPtFzbUI2C07dFn)

### Partie 3 - Ajoutez le Contenu à Documenter

* Supposons que vous avez un fichier Python appelé `my_amazing_class.py` qui contient une classe que vous souhaitez documenter.
* **Dans le même dossier** que les fichiers `conf.py` et `index.rst`, créez un nouveau fichier appelé `my_amazing_class.rst` et copiez-collez-personnalisez ce modèle :

```
Ceci est un modèle pour inclure des classes========================================|.. autoclass:: my_amazing_class.MyAmazingClass|:ref:`Retour à l'accueil <mastertoc>`
```

> ASTUCE : assurez-vous que le dossier contenant votre classe géniale est dans votre `PYTHONPATH` et qu'il contient un fichier d'initialisation `__init__.py`

* Dans le fichier `index.rst`, éditez la Table des Matières pour inclure le nom du fichier `.rst` :

```
.. toctree::   :maxdepth: 1   :name: mastertoc
```

```
   my_amazing_class
```

### Partie 4 - "Compilation"

* Dans le terminal, à l'intérieur du dossier `documentation`, exécutez `make clean html`.
* **C'est tout !** Vous avez votre première version de votre documentation prête à être consultée !
* Ouvrez le fichier `documentation/_build/html/index.html` dans votre navigateur, et voyez par vous-même :)

![Image](https://cdn-media-1.freecodecamp.org/images/fX7yeyvLr8pcpDbciN9zlmsDcBmm2A36Z96L)

![Image](https://cdn-media-1.freecodecamp.org/images/SGc77JLWj9RwwUjzNO1RfZSd-UF5wL-QlWza)

### Partie 5 - Hébergement sur GitHub Pages

* Sous la racine de votre projet, ouvrez un nouveau dossier appelé `docs` et copiez à l'intérieur le contenu de `<votre_projet>/documentation/_build/html/`
* À l'intérieur de ce nouveau dossier `docs`, créez un fichier vide appelé `.nojekyll`
  (Cela indique à GitHub Pages de contourner les thèmes `Jekyll` par défaut et d'utiliser le `HTML` et le `CSS` de votre projet)
* Poussez vos modifications vers la branche `master`.
* Dans votre dépôt sur GitHub, allez dans `Settings->GitHub Pages->Source` et sélectionnez le dossier `master branch/docs`

![Image](https://cdn-media-1.freecodecamp.org/images/kSaqUUJTnKIHrE3BKjT42cy0rAfCpo1uDObI)

![Image](https://cdn-media-1.freecodecamp.org/images/q1pwJyawKnwyds3ilJqlwj-4nA2eALjAgqov)

### Partie 6 - Partagez !

Oui. C'est tout. Attendez quelques minutes pour que GitHub se mette à jour. Partagez votre beau site de documentation à l'adresse

`https://<votre_nom_utilisateur_git>.github.io/<nom_du_projet>/

> ASTUCE : Lors de la mise à jour de la documentation, vous devez supprimer le dossier `docs` et le recréer. Voir plus de détails [ici](https://dalyag.github.io/Sphinx185/how_to_use_this_for_your_next_project.html).

### Épilogue

C'est la partie où je dis quelque chose de réfléchi sur la beauté de créer du nouveau contenu dans le monde. Et quelle personne merveilleuse vous êtes pour avoir choisi de rendre votre contenu original disponible, accessible et facile à utiliser.

Mais hé, vous êtes arrivé jusqu'ici, donc vous savez déjà tout cela.

Alors, s'il y a autre chose que vous sentez que vous ne savez pas encore, je vous invite à explorer le [site de documentation](https://dalyag.github.io/Sphinx185/index.html) que j'ai créé pour ce tutoriel. Vous pouvez regarder [la conférence que j'ai donnée](https://www.youtube.com/watch?v=3OAAL78PES8) sur Sphinx. Espérons que cela répondra à certaines énigmes que vous avez encore sur Sphinx.