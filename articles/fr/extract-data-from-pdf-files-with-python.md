---
title: Comment extraire des données de fichiers PDF avec Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-06T17:51:46.000Z'
originalURL: https://freecodecamp.org/news/extract-data-from-pdf-files-with-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Shittu-Olumide-Extract-Data-from-PDF-Files-with-Python-1.png
tags:
- name: data analysis
  slug: data-analysis
- name: pdf
  slug: pdf
- name: Python
  slug: python
seo_title: Comment extraire des données de fichiers PDF avec Python
seo_desc: "By Shittu Olumide\nData is present in all areas of the modern digital world,\
  \ and it takes many different forms. \nOne of the most common formats for data is\
  \ PDF. Invoices, reports, and other forms are frequently stored in Portable Document\
  \ Format (PDF)..."
---

Par Shittu Olumide

Les données sont présentes dans tous les domaines du monde numérique moderne, et elles prennent de nombreuses formes différentes. 

L'un des formats les plus courants pour les données est le PDF. Les factures, les rapports et autres formulaires sont fréquemment stockés dans des fichiers au format Portable Document Format (PDF) par les entreprises et les institutions. 

Extraire des données de fichiers PDF peut être fastidieux et chronophage. Heureusement, Python offre une variété de bibliothèques pour une extraction facile des données depuis les fichiers PDF. 

Ce tutoriel expliquera comment extraire des données de fichiers PDF en utilisant Python. Vous apprendrez comment installer les bibliothèques nécessaires et je fournirai des exemples de comment procéder.

Il existe plusieurs bibliothèques Python que vous pouvez utiliser pour lire et extraire des données de fichiers PDF. Parmi celles-ci, on trouve PDFMiner, PyPDF2, PDFQuery et PyMuPDF. Ici, nous utiliserons PDFQuery pour lire et extraire des données de plusieurs fichiers PDF. 

## Comment utiliser PDFQuery

PDFQuery est une bibliothèque Python qui fournit un moyen facile d'extraire des données de fichiers PDF en utilisant des sélecteurs de type CSS pour localiser les éléments dans le document. 

Elle lit un fichier PDF en tant qu'objet, convertit l'objet PDF en un fichier XML, et accède aux informations souhaitées par leur emplacement spécifique à l'intérieur du document PDF.

Considérons un court exemple pour voir comment cela fonctionne.

```py
from pdfquery import PDFQuery

pdf = PDFQuery('example.pdf')
pdf.load()

# Utiliser des sélecteurs de type CSS pour localiser les éléments
text_elements = pdf.pq('LTTextLineHorizontal')

# Extraire le texte des éléments
text = [t.text for t in text_elements]

print(text)

```

Dans ce code, nous créons d'abord un objet PDFQuery en passant le nom de fichier du fichier PDF dont nous voulons extraire les données. Nous chargeons ensuite le document dans l'objet en appelant la méthode `load()`.

Ensuite, nous utilisons des sélecteurs de type CSS pour localiser les éléments de texte dans le document PDF. La méthode `pq()` est utilisée pour localiser les éléments, ce qui retourne un objet PyQuery qui représente les éléments sélectionnés.

Enfin, nous extrayons le texte des éléments en accédant à l'attribut `text` de chaque élément et nous stockons le texte extrait dans une liste appelée `text`.

Considérons une autre méthode que nous pouvons utiliser pour lire des fichiers PDF, extraire certains éléments de données et créer un ensemble de données structuré en utilisant PDFQuery. Nous suivrons les étapes suivantes :

* Installation du package.
* Importation des bibliothèques.
* Lecture et conversion des fichiers PDF.
* Accès et extraction des données.

### Installation du package

Tout d'abord, nous devons installer PDFQuery et également installer Pandas pour certaines analyses et présentations de données.

```bash
pip install pdfquery
pip install pandas

```

### Importation des bibliothèques

```py
import pandas as pd
import pdfquery

```

Nous importons les deux bibliothèques pour pouvoir les utiliser dans notre projet.

### Lecture et conversion des fichiers PDF

```py
# lire le PDF
pdf = pdfquery.PDFQuery('customers.pdf')
pdf.load()


# convertir le pdf en XML
pdf.tree.write('customers.xml', pretty_print = True)
pdf

```

Nous allons lire le fichier PDF dans notre projet en tant qu'objet élément et le charger. Convertir l'objet PDF en un fichier XML (Extensible Markup Language). Ce fichier contient les données et les métadonnées d'une page PDF donnée.

Le XML définit un ensemble de règles pour encoder le PDF dans un format lisible par les humains et les machines. En regardant le fichier XML avec un éditeur de texte, nous pouvons voir où se trouvent les données que nous voulons extraire.

### Accès et extraction des données

Nous pouvons obtenir les informations que nous essayons d'extraire à l'intérieur de la balise `LTTextBoxHorizontal`, et nous pouvons voir les métadonnées qui y sont associées. 

Les valeurs à l'intérieur de la boîte de texte, [68.0, 231.57, 101.990, 234.893] dans le fragment XML font référence aux coordonnées `Gauche, Bas, Droite, Haut` de la boîte de texte. Vous pouvez considérer cela comme les limites autour des données que nous voulons extraire.

Accédons et extrayons le nom du client en utilisant les coordonnées de la boîte de texte.

```py
# accéder aux données en utilisant les coordonnées
customer_name = pdf.pq('LTTextLineHorizontal:in_bbox("68.0, 231.57, 101.990, 234.893")').text()

print(customer_name)

# sortie: Brandon James

```

Et c'est tout, nous avons terminé ! 

**Note** : Parfois, les données que nous voulons extraire ne se trouvent pas exactement au même endroit dans chaque fichier, ce qui peut causer des problèmes. Heureusement, PDFQuery peut également interroger des balises contenant une chaîne de caractères donnée.

## Conclusion

L'extraction de données de fichiers PDF est une tâche cruciale car ces fichiers sont fréquemment utilisés pour le stockage et le partage de documents. 

PDFQuery de Python est un outil puissant pour extraire des données de fichiers PDF. Grâce à sa syntaxe simple et à sa documentation complète, PDFQuery est une excellente option pour quiconque souhaite extraire des données de fichiers PDF. Il est également open-source et peut être modifié pour répondre à des cas d'utilisation spécifiques.

Connectons-nous sur [Twitter](https://www.twitter.com/Shittu_Olumide_) et sur [LinkedIn](https://www.linkedin.com/in/olumide-shittu). Vous pouvez également vous abonner à ma chaîne [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A).

Bon codage !