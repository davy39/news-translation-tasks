---
title: La stéganographie expliquée en termes simples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/steganography-explained-in-plain-english
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d28740569d1a4ca3637.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: Security
  slug: security
- name: toothbrush
  slug: toothbrush
seo_title: La stéganographie expliquée en termes simples
seo_desc: Steganography is the concept of concealing text, images, files, or videos
  within other text, images, files or videos. An offline example of this is using
  “invisible ink” to conceal a message between the lines of a letter. Lemon juice
  is a popular can...
---

La stéganographie est le concept de dissimuler du texte, des images, des fichiers ou des vidéos dans d'autres textes, images, fichiers ou vidéos. Un exemple hors ligne de cela est l'utilisation d'encre invisible pour dissimuler un message entre les lignes d'une lettre. Le jus de citron est un candidat populaire pour l'encre invisible : [jus de citron encre invisible](https://www.youtube.com/embed/poCnU_crpjQ)

Voici une formule très basique pour le processus stéganographique :

> support_de_couverture + données_cachées + clé_stégano = support_stégano
>
> _Dans ce contexte, le support_de_couverture est le fichier dans lequel nous allons cacher les données_cachées, qui peuvent également être chiffrées en utilisant la clé_stégano. Le fichier résultant est le support_stégano (qui sera, bien sûr, du même type de fichier que le support_de_couverture)._
>
> Source : [Steganography and Its Applications in Security](http://www.ijmer.com/papers/Vol2_Issue6/EN2646344638.pdf)

## La stéganographie dans les images

Sur les ordinateurs, les images sont stockées sous forme de fichiers binaires. Elles contiennent une représentation binaire de la couleur ou de l'intensité lumineuse de chaque élément d'image (pixel) composant l'image. Par exemple, cette image d'un chien :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/American_Eskimo_Dog.jpg)

pourrait commencer par quelque chose comme :

```text
10010101   00001101   11001001
10010110   00001111   11001010
10011111   00010000   11001011
...
```

L'approche la plus simple pour cacher des données dans le fichier est appelée insertion par bit le moins significatif (LSB). Avec cette méthode, vous pouvez prendre la représentation binaire de l'image et écraser le LSB de chaque octet de sorte que le changement soit minimal au point de ne pas être visible à l'œil humain.

Bien que le JPEG puisse être utilisé pour des applications stéganographiques, il est plus courant d'intégrer des données dans des fichiers GIF ou BMP. Les fichiers GIF et BMP 8 bits utilisent ce que l'on appelle la compression sans perte, un schéma qui permet au logiciel de reconstruire exactement l'image originale. Le JPEG, en revanche, utilise une compression avec perte, ce qui signifie que l'image décompressée est très proche de l'originale mais pas un duplicata exact.