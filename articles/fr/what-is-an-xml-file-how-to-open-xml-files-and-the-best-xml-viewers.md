---
title: Qu'est-ce qu'un fichier XML ? Comment ouvrir les fichiers XML et les meilleurs
  visualiseurs XML
subtitle: ''
author: Kristofer Koishigawa
co_authors: []
series: null
date: '2020-09-10T17:25:27.000Z'
originalURL: https://freecodecamp.org/news/what-is-an-xml-file-how-to-open-xml-files-and-the-best-xml-viewers
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c98bf740569d1a4ca1bd4.jpg
tags:
- name: xml
  slug: xml
seo_title: Qu'est-ce qu'un fichier XML ? Comment ouvrir les fichiers XML et les meilleurs
  visualiseurs XML
seo_desc: 'If you''ve ever seen the .xml extension in your downloads folder and wondered
  what that is, you''re not alone.

  Keep reading to learn what and XML file is, and how to open it both locally on your
  computer and in online editors.

  What''s an XML file?

  XML s...'
---

Si vous avez déjà vu l'extension `.xml` dans votre dossier de téléchargements et que vous vous êtes demandé ce que c'était, vous n'êtes pas seul.

Continuez à lire pour apprendre ce qu'est un fichier XML et comment l'ouvrir, à la fois localement sur votre ordinateur et dans des éditeurs en ligne.

## Qu'est-ce qu'un fichier XML ?

XML signifie Extensible Markup Language et a été créé par le [W3C](https://www.w3.org/) (World Wide Web Consortium) dans les années 90.

Bien que XML, comme HTML, soit un langage de balisage lisible par l'homme, ils servent des objectifs très différents. HTML décrit la structure d'une page web et son contenu, tandis que XML décrit la structure des données.

XML fournit aux programmes, et plus important encore, aux programmeurs, un format standard et largement accepté pour transmettre des données entre différents systèmes. À cet égard, XML a plus en commun avec JSON qu'avec HTML.

Bien que XML ne soit plus la méthode préférée pour organiser et transmettre des données, il a encore sa place. XML est toujours utilisé dans de nombreux systèmes hérités, et à la fois RSS et SVG sont basés sur le format XML.

Voici un exemple simple d'un fichier XML et comment il est utilisé pour structurer des données :

```xml
<?xml version="1.0" encoding="UTF-8"?>
<fcc_merch>
   <item>
      <name>Triblend T-shirt</name>
      <price>$24.99</price>
      <description>Représentez la communauté freeCodeCamp avec fierté dans ce T-shirt Triblend noir jetant avec le logo emblématique "bonfire function call".</description>
   </item>
   <item>
      <name>Cotton-Poly Pullover Hoodie</name>
      <price>$49.99</price>
      <description>Restez au chaud et habillez-vous comme un développeur avec ce pull à capuche noir jetant en coton-poly.</description>
   </item>
   <item>
      <name>Ceramic Coffee Mug</name>
      <price>$14.99</price>
      <description>Portez un toast à la communauté des développeurs avec votre propre mug freeCodeCamp Bonfire Function Call.</description>
   </item>
</fcc_merch>
```

## Comment ouvrir un fichier XML localement

Retour à votre dossier de téléchargements et à ce fichier avec l'extension `.xml`.

Si vous devez ouvrir un fichier XML, vous avez beaucoup d'options. La grande question est de savoir si vous devez modifier les données dans le fichier XML ou simplement les visualiser.

### Visualiser un fichier XML dans un navigateur

Si tout ce que vous devez faire est de visualiser les données dans un fichier XML, vous avez de la chance. Presque tous les navigateurs peuvent ouvrir un fichier XML.

Dans Chrome, ouvrez simplement un nouvel onglet et faites glisser le fichier XML. Alternativement, faites un clic droit sur le fichier XML, survolez "Ouvrir avec" puis cliquez sur "Chrome".

Lorsque vous le faites, le fichier s'ouvre dans un nouvel onglet.

Voici à quoi ressemble le fichier `fcc-merch.xml` dans Chrome :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-26.png)

**Note :** Les instructions pour votre système d'exploitation peuvent différer légèrement.

### Modifier un fichier XML dans un éditeur de texte

Si vous devez modifier un fichier XML localement, ou si vous préférez le visualiser en dehors du navigateur, la meilleure façon de le faire est dans un éditeur de texte.

Vous avez beaucoup d'options selon votre système d'exploitation. Voici quelques recommandations courantes :

**Windows :**

* [Notepad++](https://notepad-plus-plus.org/)

**Mac/Linux/Windows :**

* [VSCode](https://code.visualstudio.com/)
* [Atom](https://atom.io/)
* [Sublime Text](https://www.sublimetext.com/)

Notez que VSCode, Atom et Sublime Text sont des programmes assez lourds, surtout si tout ce que vous voulez faire est de modifier un fichier XML. Les utilisateurs de Mac et Linux peuvent avoir accès à d'autres éditeurs de texte légers comme gedit ou Leafpad qui peuvent ouvrir et modifier des fichiers XML.

Si vous voulez apprendre à coder, alors essayez sans hésiter l'un des éditeurs listés ci-dessus.

Une fois que vous avez téléchargé un éditeur, vous pouvez ouvrir le fichier XML à partir de l'interface graphique de l'éditeur comme vous le feriez pour n'importe quel autre fichier.

Voici le même fichier `fcc-merch.xml` dans VSCode :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-27.png)

## Comment ouvrir un fichier XML en ligne

Ouvrir un fichier XML en ligne est facile, et les meilleurs visualiseurs XML en ligne fonctionnent également comme des éditeurs et des formateurs.

Voici quelques-uns des visualiseurs/éditeurs XML en ligne les plus populaires :

* [Code Beautify](https://codebeautify.org/xmlviewer)
* [JSON Formatter](https://jsonformatter.org/xml-viewer)
* [Tutorialspoint](https://www.tutorialspoint.com/online_xml_editor.htm)

Chacun fonctionne de manière similaire, vous permettant soit de télécharger le fichier XML depuis votre ordinateur, soit de le copier et de le coller dans l'éditeur à gauche :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-24.png)
_Visualiseur/éditeur XML de Code Beautify_

Une fois que vous avez chargé votre XML, vous pouvez cliquer sur "Tree View" pour faciliter la visualisation de la hiérarchie de vos données et la manière dont les différents champs sont imbriqués :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-33.png)

Faites simplement les modifications nécessaires dans l'éditeur à gauche. Ensuite, lorsque vous avez terminé, cliquez simplement sur "Download" pour télécharger une copie de votre fichier modifié.

Notez que votre copie téléchargée peut avoir un nom différent comme `codebeautify.xml`. Renommez simplement le fichier avant de l'attacher à un email, de le télécharger ou quoi que ce soit d'autre que vous devez faire.

## En résumé

Le format XML a une longue et riche histoire.

Même si les fichiers XML sont assez denses par rapport aux solutions modernes pour la transmission de données comme JSON, il ne fait pas de mal de savoir comment les ouvrir et les modifier. Heureusement, vous avez beaucoup d'options sur votre machine locale et en ligne.

J'espère que cela vous aidera la prochaine fois que vous devrez ouvrir ou modifier un fichier XML.

Restez en sécurité et bon codage.