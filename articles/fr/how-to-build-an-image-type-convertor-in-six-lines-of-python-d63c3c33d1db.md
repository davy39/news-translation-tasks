---
title: Comment créer un convertisseur de types d'images en six lignes de Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-13T16:26:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-image-type-convertor-in-six-lines-of-python-d63c3c33d1db
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qzCM-NW3YK5gYx0tXTMJgQ.jpeg
tags:
- name: coding
  slug: coding
- name: image processing
  slug: image-processing
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: Comment créer un convertisseur de types d'images en six lignes de Python
seo_desc: 'By AMR

  One of the advantage of being a programmer is your ability to build utility tools
  to improve your life. Unlike a non-programmer, you are probably not spending hours
  digging through multiple Google search result pages to find a tool that, in th...'
---

Par AMR

L'un des avantages d'être programmeur est votre capacité à créer des outils utilitaires pour améliorer votre vie. Contrairement à un non-programmeur, vous ne passez probablement pas des heures à fouiller plusieurs pages de résultats de recherche Google pour trouver un outil qui, en premier lieu, était censé améliorer votre productivité (_l'ironie gagne_). Cela vous donne probablement un sentiment de puissance de connaître un langage de programmation — surtout si ce langage est aussi polyvalent et génial que Python.

L'un des points dans [The Zen of Python](https://www.python.org/dev/peps/pep-0020/#id3) dit :

> Simple est mieux que complexe.

Avec cette philosophie en place, beaucoup de développements d'outils de niche utilisant Python peuvent être faits de manière si concise que cela me fait me demander s'il vaut la peine de l'appeler un outil du tout. Parfois, le mot `script` serait plus précis. Dans tous les cas, nous nous lançons ici pour construire un tel `script` qui convertit les images d'un format de fichier (type d'image) à un autre — en seulement 6 lignes de code Python.

> _Avertissement : Le nombre de lignes (6) exclut les lignes vides et les commentaires_

Dans ce tutoriel, nous allons construire un convertisseur de types d'images qui convertit une image PNG en une image JPG. Avant que vos cellules de matière grise ne se précipitent pour juger si je suis fou de construire cet outil, laissez-moi dire que ce n'est pas juste pour une image — mais pour toutes les images à l'intérieur d'un dossier. Cela nécessiterait définitivement plus d'efforts manuels à faire sans codage (_je sais que vous pouvez sentir le `bash` ing)._

#### Package Python

Nous allons utiliser le package Python `PIL` (qui signifie Python Image Library) à cette fin. Le `PIL` original n'a pas reçu de mises à jour pour la dernière version de Python, donc quelques bonnes âmes ont créé [un fork convivial appelé `Pillow`](https://python-pillow.org/) qui supporte même > Python 3.0.

Installez-le en utilisant `pip3 install Pillow`.

#### **Script de début**

Il y a deux sections principales dans ce code. La première section est celle où nous importons les packages requis, et la deuxième section est celle où l'opération réelle se produit. L'opération réelle peut être encore décomposée comme suit :

* Itérer à travers tous les fichiers avec l'extension donnée — dans notre cas `.png` — et répéter toutes les étapes suivantes :
* Ouvrir le fichier image (en tant que fichier image)
* Convertir le fichier image dans un format différent (`RGB`)
* Enfin, enregistrer le fichier — avec la nouvelle extension `.jpg`

**Lignes 1 et 2 :**

```
from PIL import Image  # Python Image Library - Traitement d'image
```

```
import glob
```

Cette section importe simplement les packages requis. `PIL` pour le traitement d'image et `glob` pour itérer à travers les fichiers du dossier donné dans le système d'exploitation.

**Lignes 3–6 :**

```
# basé sur la réponse SO : https://stackoverflow.com/a/43258974/5086335
```

```
for file in glob.glob("*.png"):
```

```
 im = Image.open(file)
```

```
 rgb_im = im.convert('RGB')
```

```
 rgb_im.save(file.replace("png", "jpg"), quality=95)
```

#### FIN

C'est la fin de notre outil ! Vous pouvez enregistrer ces 6 lignes dans un fichier `.py` et les invoquer sur votre ordinateur où vous avez des images à convertir.

#### Développement ultérieur

Si vous prévoyez d'améliorer ce script davantage, vous pouvez convertir l'ensemble de ce script en un outil d'interface de ligne de commande — alors tous ces détails comme `Format de fichier` et `Chemin de dossier` peuvent être donnés en tant qu'arguments, étendant ainsi son pouvoir.

#### **Références**

* Le code complet utilisé ici est disponible sur [mon github](https://github.com/amrrs/py_img_convertor)
* [Zen of Python](https://www.python.org/dev/peps/pep-0020/#id3)
* [Pillow](https://python-pillow.org/)