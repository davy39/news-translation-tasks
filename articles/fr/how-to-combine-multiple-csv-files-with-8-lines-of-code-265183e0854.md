---
title: Comment combiner plusieurs fichiers CSV avec 8 lignes de code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-01T20:19:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-combine-multiple-csv-files-with-8-lines-of-code-265183e0854
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NQgINaLXYMzvowRHHa6Plw.jpeg
tags:
- name: automation
  slug: automation
- name: excel
  slug: excel
- name: Productivity
  slug: productivity
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: Comment combiner plusieurs fichiers CSV avec 8 lignes de code
seo_desc: 'By Ekapope Viriyakovithya

  Why do you need this?

  Manually copy-pasting is fine if you don’t have too many files to work with.

  But imagine if you have 100+ files to concatenate — are you willing to do it manually?
  Doing this repetitively is tedious and...'
---

Par Ekapope Viriyakovithya

### Pourquoi en avez-vous besoin ?

Copier-coller manuellement est acceptable si vous n'avez pas trop de fichiers à traiter.

Mais imaginez si vous avez 100+ fichiers à concaténer — êtes-vous prêt à le faire manuellement ? Faire cela de manière répétitive est fastidieux et sujet aux erreurs.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uRBGXWKaeRjw6Ck2NrhcIA.png)

Si tous les fichiers ont la même structure de tableau (mêmes en-têtes et nombre de colonnes), laissez ce petit [script Python](https://github.com/ekapope/Combine-CSV-files-in-the-folder/blob/master/Combine_CSVs.py) faire le travail.

#### Étape 1 : Importer les packages et définir le répertoire de travail

Changez « /mydir » par votre répertoire de travail souhaité.

```python
import os
import glob
import pandas as pd
os.chdir("/mydir")
```

#### Étape 2 : Utiliser glob pour correspondre au motif 'csv'

Correspondez au motif ('csv') et enregistrez la liste des noms de fichiers dans la variable 'all_filenames'. Vous pouvez consulter [ce lien](https://regexr.com/) pour en savoir plus sur la correspondance d'expressions régulières.

```py
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
```

#### Étape 3 : Combiner tous les fichiers de la liste et exporter en CSV

Utilisez pandas pour concaténer tous les fichiers de la liste et exporter en CSV. Le fichier de sortie est nommé « combined_csv.csv » situé dans votre répertoire de travail.

```py
#combiner tous les fichiers de la liste
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#exporter en csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
```

L'encodage = 'utf-8-sig' est ajouté pour surmonter le problème lors de l'exportation de langues 'non-anglaises'.

Et… c'est fait !

Cet article a été inspiré par un problème réel de tous les jours, et la structure de codage provient d'une discussion sur [stackoverflow](https://stackoverflow.com/questions/9234560/find-all-csv-files-in-a-directory-using-python/12280052). Le script complet pour ce guide est [documenté sur GitHub](https://github.com/ekapope/Combine-CSV-files-in-the-folder/blob/master/Combine_CSVs.py).

Merci d'avoir lu. Veuillez l'essayer, amusez-vous et faites-moi savoir vos commentaires !

Si vous aimez ce que j'ai fait, envisagez de me suivre sur [GitHub](https://ekapope.github.io/), [Medium](https://medium.com/@ekapope.v) et [Twitter](https://twitter.com/EkapopeV). Assurez-vous [de le mettre en favoris sur GitHub](https://github.com/Ekapope) :P