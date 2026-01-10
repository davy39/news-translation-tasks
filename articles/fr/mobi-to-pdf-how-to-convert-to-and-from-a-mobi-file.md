---
title: Mobi vers PDF – Comment convertir une extension de fichier Mobi dans le navigateur
  ou depuis la ligne de commande
subtitle: ''
author: Kristofer Koishigawa
co_authors: []
series: null
date: '2020-10-01T02:05:00.000Z'
originalURL: https://freecodecamp.org/news/mobi-to-pdf-how-to-convert-to-and-from-a-mobi-file
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9872740569d1a4ca1a19.jpg
tags:
- name: ebook
  slug: ebook
- name: pdf
  slug: pdf
seo_title: Mobi vers PDF – Comment convertir une extension de fichier Mobi dans le
  navigateur ou depuis la ligne de commande
seo_desc: If you've bought a book online recently, or downloaded a free public domain
  book at a site like Project Guttenberg, there's a good chance that it's a .mobi
  file. But you probably weren't able to open it because you didn't have the right
  software inst...
---

Si vous avez acheté un livre en ligne récemment, ou téléchargé un livre du domaine public gratuit sur un site comme [Project Gutenberg](https://www.gutenberg.org/), il y a de fortes chances qu'il s'agisse d'un fichier `.mobi`. Mais vous n'avez probablement pas pu l'ouvrir parce que vous n'aviez pas le bon logiciel installé.

Dans cet article, vous apprendrez ce que sont les fichiers `.mobi` et comment convertir vers et depuis le format `.mobi` pour une lecture plus facile entre différents appareils.

## Qu'est-ce qu'un fichier `.mobi` ?

Les fichiers `.mobi` sont un format de fichier eBook créé par la société Mobipocket pour leur logiciel Mobipocket Reader.

Amazon a racheté Mobipocket en 2005 et a basé les formats de fichiers des liseuses Kindle (`.azw` et `.azw3`) sur le format `.mobi`. Grâce à cela, il est possible de lire la plupart des fichiers `.mobi` sur les appareils Kindle.

## Comment ouvrir un fichier `.mobi`

Il existe plusieurs façons d'ouvrir les eBooks `.mobi`. Parmi les suggestions courantes, on trouve [Calibre](https://calibre-ebook.com/), [FBReader](https://fbreader.org/), et l'application officielle [Kindle](https://www.amazon.com/b/ref=ruby_redirect?ie=UTF8&node=16571048011).

Parmi ceux-ci, Calibre et FBReader sont disponibles pour Windows, macOS et Linux. En outre, FBReader est également disponible pour Android et iOS.

## Comment convertir un fichier `.mobi`

Convertir des eBooks `.mobi` dans d'autres formats est vraiment simple, que ce soit en ligne ou localement.

### Comment convertir vers ou depuis un fichier `.mobi` en ligne

Il existe plusieurs sites comme [docspal](https://www.docspal.com/) qui vous permettent de télécharger un fichier `.mobi` et de sélectionner un format pour le convertir, comme PDF. Une fois la conversion terminée, vous pouvez télécharger le nouveau fichier.

Pour convertir un fichier `.mobi` en PDF, allez sur le site et téléchargez le fichier :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-43.png)

Ensuite, sélectionnez le type de fichier dans lequel vous souhaitez convertir le fichier `.mobi` depuis le menu déroulant à droite :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-44.png)

Enfin, cliquez sur le bouton "Convertir" et téléchargez le fichier converti.

Cela fonctionne également si vous souhaitez convertir un fichier PDF en `.mobi` – téléchargez le fichier PDF, sélectionnez `.mobi` dans le menu déroulant à droite, puis cliquez sur le bouton "Convertir".

### Comment convertir vers ou depuis un fichier `.mobi` localement sur votre ordinateur

Bien que la conversion de fichiers `.mobi` vers et depuis d'autres formats sur votre machine locale soit un peu plus complexe, Calibre la simplifie.

Pour convertir un fichier `.mobi` en PDF, commencez par [télécharger](https://calibre-ebook.com/download) et installer Calibre pour votre système d'exploitation.

Ensuite, ouvrez Calibre, cliquez sur "Ajouter des livres" dans le coin supérieur droit et sélectionnez votre eBook :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-45.png)
_Sélection d'un eBook `.mobi` dans Linux Mint_

Ensuite, sélectionnez l'eBook dans votre bibliothèque Calibre et cliquez sur le bouton "Convertir des livres" dans le menu en haut.

Dans le menu "Convertir des livres", sélectionnez PDF dans le menu déroulant "Format de sortie" dans le coin supérieur droit :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-47.png)

Enfin, cliquez sur le bouton "OK" dans le coin inférieur droit.

Une fois la conversion terminée, votre nouveau fichier PDF se trouvera dans le répertoire `/Calibre Library/[Auteur du livre]/`.

Pour convertir un PDF en fichier `.mobi` dans Calibre, commencez par ajouter le fichier PDF, cliquez sur "Convertir des livres", sélectionnez `.mobi` dans le menu déroulant "Format de sortie", puis cliquez sur le bouton "OK".

### Comment convertir vers ou depuis un fichier `.mobi` depuis la ligne de commande

Si vous souhaitez une méthode plus rapide pour convertir des fichiers vers et depuis le format `.mobi`, Calibre inclut un petit outil en ligne de commande pratique, `ebook-convert`.

**Note :** Ces instructions ont été écrites pour Linux, mais devraient également s'appliquer à macOS et éventuellement à Windows avec [WSL (Windows Subsystem for Linux)](https://docs.microsoft.com/en-us/windows/wsl/install-win10) configuré.

Pour convertir un fichier `.mobi` en PDF, ouvrez un terminal et utilisez la commande `cd` pour accéder au répertoire contenant le fichier eBook :

```bash
cd ~/Documents/ebooks
```

Ensuite, exécutez la commande `ebook-convert` avec les options suivantes :

```bash
ebook-convert <fichier_source>.<format_source> <fichier_destination>.<format_destination>
```

Par exemple :

```bash
ebook-convert pride-and-prejudice.mobi pride-and-prejudice.pdf
```

Passer de PDF à `.mobi` est tout aussi simple :

```bash
ebook-convert pride-and-prejudice.pdf pride-and-prejudice.mobi
```

## Conclusion

Bien que les fichiers `.mobi` soient un format plus ancien, ils sont toujours bien supportés et peuvent être facilement convertis vers d'autres formats de fichiers. Que vous convertissiez les fichiers en ligne ou localement, c'est à vous de choisir.

Quelle que soit la méthode que vous choisissez pour convertir vos fichiers eBook, restez en sécurité et lisez un bon livre.