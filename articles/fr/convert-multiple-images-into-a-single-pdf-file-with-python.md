---
title: Projet Python – Comment convertir plusieurs images en un seul fichier PDF
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2023-07-19T20:13:36.000Z'
originalURL: https://freecodecamp.org/news/convert-multiple-images-into-a-single-pdf-file-with-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/alvaro-reyes-fSWOVc3e06w-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: Projet Python – Comment convertir plusieurs images en un seul fichier PDF
seo_desc: 'Creating projects is the best way to learn a programming language. It is
  fun and it''s a creative way to learn new things.

  Whenever I try to learn a new language or new technology, I try to create a project,
  whether it''s a small byte-sized or big proj...'
---

Créer des projets est la meilleure façon d'apprendre un langage de programmation. C'est amusant et c'est une manière créative d'apprendre de nouvelles choses.

Chaque fois que j'essaie d'apprendre un nouveau langage ou une nouvelle technologie, j'essaie de créer un projet, qu'il soit petit ou grand.

Dans cet article, je vais vous montrer un petit mais très cool projet si vous êtes un débutant complet en Python.

Vous allez créer un projet qui va récupérer tous les fichiers image d'un répertoire particulier et créer un seul fichier PDF qui inclut toutes les images.

L'intérêt de Python est que vous n'aurez besoin que de 4 lignes de code pour y parvenir ! Alors, commençons, d'accord ?

## 📆 Structure du répertoire du projet

Voici à quoi ressemble mon répertoire de projet sans Git.

```python
📆img2singlePDF
 ✓ 📄ImageContainingBook.pdf
 ✓ 📄jakub-neskora-A9tqu5iCFCQ-unsplash.jpg
 ✓ 📄raphael-renter-csae9W8JAsw-unsplash.jpg
 ✓ 📄README.md
 ✓ 📄sam-moghadam-khamseh-cU5TUyEaZXQ-unsplash.jpg
 ✓ 📄Script.py
 ✓ 📄sherry-christian-8Myh76_3M2U-unsplash.jpg
 └ 📄sunder-muthukumaran-fd6K_OFlnRA-unsplash.jpg
```

Vous pouvez voir à quoi ressemble mon projet avec Git [dans ce dépôt](https://github.com/FahimFBA/img2singlePDF/blob/main/README.md). N'oubliez pas de mettre une étoile au dépôt pour montrer votre soutien.

## 🏁 Installation du projet

Pour commencer, créez d'abord un nouveau dossier pour le projet. Assurez-vous de ne pas inclure d'espaces dans le nom du dossier.

Ajoutez quelques fichiers image dans ce répertoire. Pour ce projet, je vais utiliser des fichiers image `.jpg`. Par conséquent, je vous suggère de faire la même chose !

Vous pouvez télécharger des images libres de droits depuis [Unsplash](https://unsplash.com/) ou [Pexels](https://unsplash.com/).

Gardez à l'esprit que notre projet ne peut pas gérer de grands fichiers image. Essayez donc de télécharger des fichiers image de petite taille. Vous pouvez sélectionner des fichiers de petite taille lors du téléchargement depuis Unsplash.

Vous pouvez également trouver les images dans le dossier `img` du dépôt GitHub mentionné précédemment.

Ensuite, ouvrez [Visual Studio Code](https://code.visualstudio.com/). Visual Studio Code est gratuit et un éditeur de code largement utilisé.

Si vous préférez utiliser un autre éditeur, vous pouvez ouvrir le projet avec l'éditeur de votre choix.

Maintenant, créez un fichier Python nommé `Script.py`. C'est ici que vous écrirez le code pour ce projet.

Enfin, installez le package/bibliothèque nommé `img2pdf`. Cette bibliothèque est utilisée pour convertir des images en PDF via une inclusion directe JPEG. Vous pouvez consulter ce [site web](https://pypi.org/project/img2pdf/) pour plus de détails.

Je vais l'installer en utilisant `pip`. Ouvrez une fenêtre de terminal et entrez la commande `pip install img2pdf`.

## ⚙️ Écrivons un peu de code

Nous pouvons travailler avec certaines bibliothèques pré-définies. Si nous faisons cela, alors nous n'avons pas nécessairement besoin d'écrire tout à partir de zéro.

Python dispose déjà d'une tonne de bibliothèques, et nous pouvons utiliser directement leurs fonctionnalités pré-définies. Mais pour cela, nous devons importer ces bibliothèques avant d'essayer de travailler avec elles.

Tout d'abord, vous devez importer les deux packages/modules/bibliothèques pertinents nommés `os` et `img2pdf`. Si vous souhaitez travailler avec certaines bibliothèques/modules pré-définis, il est nécessaire de les mentionner plus tôt car l'interpréteur les trouvera avant de procéder au travail sur ces bibliothèques spécifiques.

Nous avons besoin de la bibliothèque `os`. Ce module fait partie des modules utilitaires standard de Python.

Le module OS en Python fournit des fonctions pour interagir avec le système d'exploitation. OS fait partie des modules utilitaires standard de Python. Ce module fournit un moyen portable d'utiliser les fonctionnalités dépendantes du système d'exploitation. Comme nous allons utiliser le répertoire de fichiers de notre stockage local, il est nécessaire pour notre tâche.

Pour importer une bibliothèque en Python, nous utilisons simplement `import nom_bibliothèque`. Dans ce cas, nous avons utilisé `import os` pour importer la bibliothèque `os`. Après avoir importé une bibliothèque, nous pouvons les utiliser à tout moment dans ce script ou fichier Python.

En ce qui concerne l'autre bibliothèque, `img2pdf`, rappelez-vous que nous allons utiliser cette bibliothèque pour convertir nos fichiers image en fichiers PDF.

Pour importer la bibliothèque `img2pdf`, nous utilisons la même commande d'importation, `import img2pdf`.

Après avoir importé les deux bibliothèques nécessaires, nous pouvons les utiliser dans notre script à tout moment, et nous pouvons également utiliser toutes les fonctionnalités des deux bibliothèques. Cela rend nos tâches plus faciles et notre code plus court. Avant de faire cela, assurez-vous d'avoir déjà installé la bibliothèque `img2pdf` en utilisant `pip` ou `conda`.

Maintenant, je dois spécifier exactement dans quel format de fichier et quel nom de fichier je veux placer mes fichiers image. Je vais créer un fichier PDF spécifique où toutes les images seront intégrées. Par conséquent, je vais spécifier cela en utilisant la commande d'utilisation de fichier.

La structure de la commande est quelque chose comme `with open ("Nom_Fichier_Cible.extension", "mode") as file:`.

Par conséquent, notre commande serait :

```python
with open("ImageContainingBook.pdf", "wb") as file:
```

Cela créera un fichier PDF nommé `ImageContainingBook.pdf` et intégrera tous les fichiers image là.

Si vous souhaitez avoir un nom de fichier différent, vous pouvez changer le nom, mais assurez-vous de ne pas garder d'espaces dans le nom de fichier. Par exemple, n'utilisez pas de noms de fichiers comme `my pdf.pdf`. Au lieu d'utiliser un espace, utilisez un trait de soulignement ( `_` ), comme `my_pdf.pdf`. Mais je préfère utiliser quelque chose comme `myPDF.pdf`.

Et vérifiez que vous avez également inclus l'extension de fichier (dans ce cas, vous travaillez avec un fichier PDF, donc l'extension de fichier doit être `.pdf`).

Comme nous allons écrire dans ce fichier et que nous allons travailler sur des fichiers binaires, nous avons utilisé le formatage comme `wb`. Le `wb` indique que le fichier est ouvert pour l'écriture en mode binaire.

Selon une solution de [StackOverflow](https://stackoverflow.com/questions/2665866/what-does-wb-mean-in-this-code-using-python) :

> "Lorsque vous écrivez en mode binaire, Python ne fait aucune modification aux données lorsqu'elles sont écrites dans le fichier. En mode texte (lorsque le `b` est exclu comme dans juste `w` ou lorsque vous spécifiez le mode texte avec `wt`), cependant, Python encodera le texte en fonction de l'encodage de texte par défaut. De plus, Python convertira les fins de ligne (`\n`) en ce que la fin de ligne spécifique à la plateforme est, ce qui corromprait un fichier binaire comme un fichier `exe` ou `png`."

Ensuite, je dois spécifier ce que je veux faire avec le fichier.

Je veux écrire dans ce fichier et je veux la fonctionnalité de conversion de la bibliothèque `img2pdf`.

Dans mon répertoire, il peut y avoir beaucoup de fichiers différents et c'est naturel. Mais comme je ne veux convertir que les fichiers image qui ont une extension `.jpeg`, je dois spécifier cela explicitement.

De plus, je dois définitivement inclure le répertoire de fichiers où il obtiendra toutes les images.

Par conséquent, la dernière ligne de notre script serait :

```python
file.write(img2pdf.convert([i for i in os.listdir("C:\\Users\\fahim\\Desktop\\ImageToPdf") if i.endswith(".jpg")])) # Changez le répertoire de fichiers en conséquence
```

Permettez-moi d'expliquer le code maintenant.

`os.listdir("C:\\Users\\fahim\\Desktop\\ImageToPdf")` : Cette ligne utilise le module `os` pour lister tous les fichiers dans le répertoire spécifié par le chemin donné. Dans ce cas, il s'agit du répertoire "C:\\Users\\fahim\\Desktop\\ImageToPdf".

`[i for i in os.listdir("C:\\Users\\fahim\\Desktop\\ImageToPdf") if i.endswith(".jpg")]` : Il s'agit d'une compréhension de liste qui filtre les fichiers obtenus à partir de la liste du répertoire. Elle parcourt chaque nom de fichier dans le répertoire et n'inclut que ceux qui se terminent par l'extension ".jpg". Cette étape garantit que seules les images JPEG seront prises en compte pour la conversion en PDF.

`img2pdf.convert(...)` : La bibliothèque `img2pdf` fournit la fonction `convert`, qui prend une liste de chemins de fichiers image et les convertit en un seul fichier PDF. Le code passé à l'intérieur des parenthèses génère la liste des chemins de fichiers image (images JPEG se terminant par ".jpg") en utilisant la compréhension de liste.

`file.write(...)` : Il semble que `file` soit un objet fichier qui a été ouvert en mode écriture. La méthode `write` est utilisée pour écrire le contenu PDF dans le fichier.

Pour utiliser ce code avec succès, vous devez vous assurer des éléments suivants :

* Que la bibliothèque `img2pdf` est installée dans votre environnement Python.

* Remplacez le chemin du répertoire `"C:\\Users\\fahim\\Desktop\\ImageToPdf"` par le chemin du répertoire contenant les images JPEG que vous souhaitez convertir en PDF.

* Que vous avez les permissions d'écriture appropriées pour le répertoire et le fichier spécifiés.

Il est important de noter que le code convertit toutes les images JPEG du répertoire spécifié en un seul fichier PDF. Si d'autres types de fichiers ou des fichiers non image se trouvent dans ce répertoire, ils seront ignorés lors de la conversion.

En résumé, l'ensemble du script Python est :

```python
import os
import img2pdf
with open("ImageContainingBook.pdf", "wb") as file:
    file.write(img2pdf.convert([i for i in os.listdir("C:\\Users\\fahim\\Desktop\\ImageToPdf") if i.endswith(".jpg")])) # Changez le répertoire de fichiers en conséquence
```

Assurez-vous d'inclure un espace supplémentaire dans le répertoire de fichiers. Nous faisons cela parce que nous voulons notifier qu'il ne s'agit pas d'une séquence d'échappement, mais qu'il fait partie de cette chaîne de chemin de répertoire.

Si nous le souhaitons, nous pouvons modifier le code davantage. Un autre exemple d'utilisation du même code en le décomposant en segments individuels peut être comme ci-dessous :

```python
import os
import img2pdf

# Remplacez le chemin du répertoire par le dossier contenant les images JPEG à convertir
chemin_repertoire = "C:\\Users\\fahim\\Desktop\\img2singlePDF"

# Liste tous les fichiers dans le répertoire et filtre uniquement les images JPEG (se terminant par ".jpg")
fichiers_image = [i for i in os.listdir(chemin_repertoire) if i.endswith(".jpg")]

# Convertit la liste des images JPEG en un seul fichier PDF
donnes_pdf = img2pdf.convert(fichiers_image)

# Écrit le contenu PDF dans un fichier (assurez-vous d'avoir les permissions d'écriture pour le fichier spécifié)
with open("output.pdf", "wb") as file:
    file.write(donnes_pdf)
```

Encore une fois, permettez-moi de fournir l'explication pour toutes les lignes en détail :

1. Tout d'abord, nous importons les modules nécessaires : `os` pour interagir avec le système de fichiers et `img2pdf` pour la conversion d'images en PDF.

2. La variable `chemin_repertoire` doit être remplacée par le chemin du dossier contenant les images JPEG qui doivent être converties.

3. En utilisant la compréhension de liste, nous obtenons une liste de fichiers image dans le répertoire spécifié, en filtrant uniquement ceux avec l'extension ".jpg". Ce sont les images qui seront incluses dans le PDF.

4. La fonction `img2pdf.convert(...)` prend la liste des fichiers image et les convertit en un seul fichier PDF, stockant le contenu PDF dans la variable `donnes_pdf`.

5. Nous ouvrons un nouveau fichier nommé "output.pdf" en mode écriture binaire (`"wb"`) en utilisant une instruction `with` pour assurer une gestion et une fermeture appropriées du fichier.

6. Enfin, nous écrivons le contenu `donnes_pdf` dans le fichier "output.pdf", créant ainsi le PDF avec les images converties.

Note : Avant d'exécuter le code, assurez-vous que la bibliothèque `img2pdf` est installée dans votre environnement Python. Vous pouvez l'installer en utilisant `pip install img2pdf`. Assurez-vous également d'avoir les permissions d'écriture nécessaires pour le répertoire et le fichier spécifiés.

## 🏃‍♂️ Exécuter le code

Si vous avez l'extension [Code Runner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner) installée sur votre VS Code, vous pouvez exécuter le fichier en utilisant cette extension.

Mais si vous préférez exécuter le code depuis votre terminal, la commande serait `python nomfichier.py` pour Windows et `python3 nomfichier.py` pour Mac ou Linux.

Comme mon nom de fichier est `Script.py` et que j'utilise ma machine Windows, ma commande serait `python Script.py`.

Instantanément, vous recevrez le fichier PDF qui contient tous les fichiers image (où les fichiers image ont une extension de fichier `.jpeg`).

## 📽️ Tutoriel vidéo

Je sais que beaucoup d'entre vous préfèrent regarder une vidéo plutôt que de suivre un article complet. Ne craignez rien ! J'ai également créé un tutoriel vidéo complet pour vous :

%[https://www.youtube.com/watch?v=zBZhfzgahsk]

## 🙋‍♂️ Conclusion

J'espère que vous avez apprécié cet article court. Vous devriez maintenant être capable de convertir vos images en un seul fichier PDF dans vos propres projets. 😊

Si vous avez des questions, n'hésitez pas à me contacter sur [Twitter](https://twitter.com/Fahim_FBA) ou [LinkedIn](https://www.linkedin.com/in/fahimfba/).

Vous pouvez également me suivre sur :

🎁GitHub : [FahimFBA](https://github.com/FahimFBA)

🎁YouTube : [@FahimAmin](https://www.youtube.com/@FahimAmin?sub_confirmation=1)

Si vous êtes intéressé, vous pouvez également consulter mon site web : [https://fahimbinamin.com/](https://fahimbinamin.com/)

Passez une excellente journée ! 😊

📚 Couverture : Photo par [Alvaro Reyes](https://unsplash.com/@alvarordesign?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) sur [Unsplash](https://unsplash.com/photos/fSWOVc3e06w?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)