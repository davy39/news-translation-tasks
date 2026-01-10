---
title: Comment auto-formater votre code Python avec Black
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-12T17:25:57.000Z'
originalURL: https://freecodecamp.org/news/auto-format-your-python-code-with-black
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b14740569d1a4ca2991.jpg
tags:
- name: automation
  slug: automation
- name: Python
  slug: python
seo_title: Comment auto-formater votre code Python avec Black
seo_desc: 'By Davis David

  Writing Python code is one thing and writing the code in a good format is another
  thing. Junior programmers often focus on making sure their code is working and forget
  to format the code properly along the way.

  If you write a small pro...'
---

Par Davis David

Écrire du code Python est une chose, et écrire du code bien formaté en est une autre. Les programmeurs juniors se concentrent souvent sur le fait de s'assurer que leur code fonctionne et oublient de le formater correctement en cours de route.

Si vous écrivez un petit programme (avec 1000 lignes de code), vous pouvez probablement vous en sortir sans formater votre code.

Mais à mesure que les programmes deviennent de plus en plus complexes, ils deviennent de plus en plus difficiles à comprendre. À un certain point (autour de 15 000 lignes de code), il devient plus difficile de comprendre le code que vous avez vous-même écrit.

La différence entre travailler sur un code bien formaté et travailler sur un code mal formaté est comme la différence entre vivre dans un palais et vivre dans une maison sale.

# **Pourquoi formater votre code Python est important**

### Lisibilité

Formater votre code vous aidera à **lire** votre code **efficacement**. Il semble plus organisé, et lorsque quelqu'un regarde votre code, il aura une bonne impression.

### Cela vous aidera lors de vos entretiens de codage

Lors d'un entretien de codage, parfois les intervieweurs se soucient de savoir si vous formatez correctement votre code. Si vous oubliez de faire ce formatage, vous pourriez perdre vos perspectives d'emploi, juste à cause de votre code mal formaté.

### Support d'équipe

Formater votre code devient plus important lorsque vous travaillez en **équipe**. Plusieurs personnes travailleront probablement sur le même projet logiciel et le code que vous écrivez doit être compris par vos coéquipiers. Sinon, il devient plus difficile de travailler ensemble.

### Cela facilite la détection des bugs

Un code mal formaté peut rendre vraiment, vraiment difficile la détection des bugs ou même le travail sur un programme. C'est aussi vraiment horrible à regarder. _C'est une offense pour vos yeux._

# Pylint et Flake8

La plupart des développeurs Python aiment utiliser [Pylint](https://www.pylint.org/) ou [Flake8](http://flake8.pycqa.org/en/latest/) pour vérifier leur code pour les erreurs et les guides de style.

**Pylint** est un outil qui vérifie les erreurs dans Python. Il essaie de faire respecter une norme de codage et recherche les mauvaises pratiques de code. Il peut également rechercher certains types d'erreurs, recommander des suggestions sur la façon dont certains blocs peuvent être refactorisés, et vous offrir des détails sur la complexité du code.

**Flake8** est une bibliothèque Python qui enveloppe **PyFlakes**, **pycodestyle** et le script **McCabe de Ned Batchelder**. C'est un excellent kit d'outils pour vérifier votre base de code par rapport au style de codage **(PEP8)**, aux erreurs de programmation comme "bibliothèque importée mais non utilisée", "Nom non défini" et au code qui n'est pas indenté.

Le problème est que ces outils ne signalent que les problèmes qu'ils identifient dans le code source et laissent la charge aux développeurs Python de les corriger !

Mais que se passerait-il si nous avions un outil qui pourrait identifier et résoudre le problème en même temps ? **Black** est un outil qui vous permet d'**identifier les erreurs** et de **formater votre code Python** en même temps. Ainsi, il vous rend plus productif.

# **Introduction à Black**

![Image](https://www.freecodecamp.org/news/content/images/2020/05/1_bxzXidSUpkEaj7j0rC5ygg.png)
_Logo de Black_

D'après le README du projet :

> _En utilisant _Black_, vous acceptez de céder le contrôle sur les minuties de la mise en forme manuelle. En retour, _Black_ vous offre rapidité, déterminisme et liberté face aux naggings de pycodestyle concernant la mise en forme. Vous économiserez du temps et de l'énergie mentale pour des questions plus importantes._

Black peut reformater l'intégralité de votre fichier selon le style de code de Black. Il aide votre cerveau à se concentrer sur le problème que vous voulez résoudre et sur les solutions de code, plutôt que d'être distrait par la structure du code et les petites différences stylistiques.

Alors voyons comment l'utiliser.

### Installer Black

Black peut être installé en exécutant `pip install black`. Il nécessite Python 3.6.0+ pour fonctionner. Une fois Black installé, vous aurez un nouvel outil en ligne de commande appelé black disponible dans votre shell, et vous êtes prêt à commencer !

Pour commencer immédiatement avec des paramètres par défaut sensés, choisissez le fichier Python que vous souhaitez formater, puis écrivez **black filename.py** dans le terminal. Ensuite, Black formatera votre fichier Python.

Maintenant, nous allons voir ce que Black peut nous aider à faire.

### Formater un seul fichier

Regardons cet exemple simple : voici mes deux fonctions Python dans mon fichier Python appelé sample_code.py.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/1_OKkCLUmuspv8IHiU25NVTw.png)
_sample_code.py_

Vous pouvez utiliser `black sample_code.py` dans le terminal pour changer le format. Après avoir exécuté Black, vous verrez la sortie suivante :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/d.png)

Ensuite, vous pouvez ouvrir sample_code.py pour voir le code Python formaté :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/e.png)

Le code Python est maintenant formaté et il est plus lisible.

### Formater plusieurs fichiers

Pour formater plus d'un fichier Python, écrivez `black folder_name/` dans le terminal.

![Image](https://miro.medium.com/max/30/1*VLyk0_7wCnKFOEYPRBpABg.png?q=20)

![Image](https://www.freecodecamp.org/news/content/images/2020/05/f.png)
_Formater tous les fichiers Python à l'intérieur du dossier_

Trois fichiers Python dans le dossier nommé python_with_black ont été reformatés.

### Vérifier les fichiers pour le formatage

Si vous ne voulez pas que Black modifie votre fichier, mais que vous voulez savoir si Black pense qu'un fichier doit être modifié, vous pouvez utiliser l'une des commandes suivantes :

`black --check .` : Cela vérifie quels fichiers Python peuvent être formatés dans le dossier courant (mais ne modifie pas réellement les fichiers Python).

![Image](https://www.freecodecamp.org/news/content/images/2020/05/g.png)
_Vérifier les fichiers à formater_

`black --check --diff file_name.py` : Cela montre ce qui doit être fait sur le fichier mais ne modifie pas le fichier.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/h.png)
_vérifier les différences après le formatage_

### Changer le nombre de caractères par ligne

Notez que Black utilise par défaut 88 caractères pour la longueur de ligne, mais vous pouvez changer cela en utilisant l'option "-l" ou "--line-length".

Par exemple, pour changer à 60 caractères : `black -l 60 python_file.py`.

# Black dans Jupyter Notebook

Pour les utilisateurs de Jupyter Notebook, vous pouvez toujours auto-formater votre code Python avec cette extension simple appelée [Jupyter Black](https://github.com/drillan/jupyter-black). Cette extension reformate/embellit le code dans une cellule de code d'un notebook par [black](https://black.readthedocs.io/en/stable/).

L'extension Jupyter Black fournit :

* Un bouton de barre d'outils.
* Un raccourci clavier pour reformater la cellule de code actuelle (par défaut : Ctrl-B).
* Un raccourci clavier pour reformater toutes les cellules de code (par défaut : Ctrl-Shift-B).

### Installer Jupyter Black

Assurez-vous d'abord d'avoir installé [jupyter-contrib-nbextensions](https://github.com/ipython-contrib/jupyter_contrib_nbextensions) et [black](https://black.readthedocs.io/en/stable/), puis exécutez les commandes suivantes.

```
jupyter nbextension install https://github.com/drillan/jupyter-black/archive/master.zip --user
```

Ensuite, activez l'extension en exécutant :

```
jupyter nbextension enable jupyter-black-master/jupyter-black
```

Maintenant, vous pouvez commencer à formater votre code Python dans chaque cellule de notebook.

Tout d'abord, sélectionnez la cellule de notebook dans laquelle vous souhaitez formater votre code Python, puis cliquez sur le bouton de l'extension appelé Black.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/i.png)
_Avant d'utiliser Jupyter Black_

Ensuite, cliquez sur le bouton Jupyter Black :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/j.png)
_Bouton Jupyter Black_

![Image](https://www.freecodecamp.org/news/content/images/2020/05/k.png)
_Après avoir utilisé Jupyter Black_

# Intégration avec l'éditeur

Vous pouvez intégrer Black avec vos éditeurs préférés. Actuellement, Black supporte PyCharm/IntelliJ IDEA, Wing IDE, Vim, Visual Studio Code, Sublime Text 3, Atom/Nuclide, Kakoune et Thonny. Suivez les instructions [ici](https://black.readthedocs.io/en/latest/editor_integration.html) pour intégrer Black avec votre éditeur préféré.

Si vous voulez en savoir plus sur Black, je vous recommande de regarder la [conférence PyCon 2019](https://youtu.be/esZLCuWs_2Y) de Łukasz Langa.

Si vous avez appris quelque chose de nouveau ou si vous avez aimé lire cet article, veuillez le partager afin que d'autres puissent le voir. En attendant, à la prochaine ! Je peux également être joint sur Twitter [@Davis_McDavid](https://twitter.com/Davis_McDavid).