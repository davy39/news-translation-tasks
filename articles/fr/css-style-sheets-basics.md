---
title: Comment travailler avec les feuilles de style CSS – les bases pour débutants
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-06-30T16:22:07.000Z'
originalURL: https://freecodecamp.org/news/css-style-sheets-basics
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/pexels-bibek-ghosh-14553706.jpg
tags:
- name: CSS
  slug: css
- name: Web Development
  slug: web-development
seo_title: Comment travailler avec les feuilles de style CSS – les bases pour débutants
seo_desc: "Using HTML tags like , , and so on can help you organize your web page\
  \ content nicely, but only up to a point. \nHTML-only pages can be pleasant and\
  \ easy to read – which is hugely important – but, after a while, they all do tend\
  \ to look the same. \nCas..."
---

L'utilisation de balises HTML comme <head>, <body>, etc., peut vous aider à organiser le contenu de votre page web de manière agréable, mais seulement jusqu'à un certain point.

Les pages HTML seules peuvent être agréables et faciles à lire – ce qui est extrêmement important – mais, après un certain temps, elles finissent toutes par se ressembler.

Les feuilles de style en cascade, universellement connues sous le nom de CSS, ne sont pas vraiment des feuilles, et il peut être nécessaire de faire un certain effort pour comprendre ce que signifie "cascade". Mais ce standard de balisage ajoute une réelle puissance à votre travail de développement web. Examinons quelques-unes de ces magies CSS en action.

Cet article provient de [mon cours complet LPI Web Development Essentials Study Guide](https://www.udemy.com/course/complete-lpi-web-development-essentials-exam-study-guide/?referralCode=C92570BCBB38302A9257). Si vous le souhaitez, vous pouvez suivre la version vidéo ici :

%[https://youtu.be/47Ufb8g8WGc]

## Comment fonctionne le CSS

Ce que le CSS fait réellement, c'est de vous permettre de séparer votre _contenu_ de sa _présentation_. Le HTML gère le contenu – c'est-à-dire le texte, les images et autres médias que vos utilisateurs consommeront. Et le CSS ajoute un contrôle plus sophistiqué sur la manière dont ce contenu apparaît et se comporte.

Au-delà de la gestion de la mise en forme, le CSS vous permet également de modulariser les ressources sur des sites web complexes, offrant une présentation uniforme sur plusieurs pages web. Cela est possible car un seul document CSS peut être référencé par autant de pages web que vous le souhaitez.

En fait, je me souviens qu'il y a de nombreuses années, dans un moment de paresse particulière, j'ai une fois référencé le document CSS d'un grand site web bien connu depuis l'un de mes propres petits sites. (Ne le dites à personne, mais il pourrait avoir appartenu à freeCodeCamp.)

Parce que je n'avais pas envie de comprendre comment ils produisaient un effet que j'aimais, j'ai simplement lié leur code. Je suis presque sûr que c'était complètement légal, d'ailleurs, mais je ne vous recommande certainement pas d'essayer. Il ne faudra que peu de temps avant qu'ils ne fassent des changements à leur feuille de style qui cassera votre site.

## Comment ajouter du CSS à votre HTML

Il existe deux façons d'incorporer du code CSS. Tout d'abord, vous pouvez simplement enregistrer toutes vos balises dans un fichier utilisant l'extension `.css` qui est accessible à vos fichiers `.html` en utilisant une balise `link rel` comme ceci :

```
<link rel="stylesheet" href="/main.css">
```

Cet exemple utilise l'attribut `stylesheet` pour pointer vers un fichier CSS appelé `main.css` qui se trouve dans le répertoire racine web de son serveur.

Alternativement, vous pouvez l'ajouter entre les balises `<style>` dans la section `<head>` de votre HTML. Cela ressemblera à quelque chose comme ceci :

```
<!DOCTYPE html>
<html>
<head>
<style type="text/css">
p {
  color: red;
  text-align: center;
}
/* Ceci est la mise en forme pour les puces : */
ul {
  color: blue;
  text-align: left;
}
</style>
</head>

```

Remarquez comment la balise d'ouverture a un attribut `type` de `text/css`, bien que je ne sois pas sûr de la nécessité de cela aujourd'hui. Le garder là ne peut certainement pas faire de mal, cependant.

Ce CSS a deux sections : la première s'appliquera à tous les éléments `p` (paragraphe) qui pourraient exister dans votre HTML.

## Comment appliquer votre CSS

Lorsque vous regardez le code ci-dessus, vous verrez qu'il y a deux définitions de style dans les accolades : la couleur du texte doit être rouge, et l'alignement du texte doit être centré :

```css
<style type="text/css">
p {
  color: red;
  text-align: center;
}
```

Remarquez comment chaque définition se termine par un point-virgule. C'est vraiment important et omettre ceux-ci cassera des choses. Remarquez également comment nous pouvons faire référence aux couleurs par leur nom. Nous verrons plus d'exemples de cela plus tard, mais sachez que vous pouvez également identifier les couleurs par leurs codes hexadécimaux. Le code hexadécimal pour une belle nuance de rouge pourrait être `#F5733`.

La ligne suivante de notre code est juste un commentaire :

```
/* Ceci est la mise en forme pour les puces : */
```

En général, bien sûr, vous voulez que ce type de note rende votre code plus lisible et compréhensible. Mais je l'ai ajouté ici spécifiquement pour vous montrer comment fonctionnent les commentaires en CSS, en utilisant une barre oblique et un astérisque au début, et un astérisque et une barre oblique à la fin. Les commentaires de style HTML ne fonctionneront pas ici.

Ce style suivant s'appliquera à toute liste non ordonnée dans votre HTML, en utilisant le bleu comme couleur de texte et en alignant le texte à gauche.

```
/* Ceci est la mise en forme pour les puces : */
ul {
  color: blue;
  text-align: left;
}
</style>

```

Il y a beaucoup plus de choses que vous pouvez faire ici et, bien sûr, vous pouvez appliquer des styles à tous types d'éléments HTML. Mais nous devons bien commencer quelque part, n'est-ce pas ?

Le HTML réel se trouve plus bas dans la section `<body>`. Pour vous montrer comment notre CSS fonctionnera, j'ai écrit du texte dans un paragraphe régulier, et quelques puces entre des balises `<ul>`.

```
<body>

<h2>CSS de base</h2>

<p>Ce texte existe dans un paragraphe régulier.</p>

<ul>
   <li>Ceci est une puce
   <li>Ceci est une autre puce
</ul>
</body>
</html>

```

Maintenant, placez ce code dans un fichier texte avec une extension `.html` et ouvrez-le dans un navigateur. Les couleurs et l'alignement devraient refléter nos préférences. Ce n'est pas grand-chose, mais c'est à nous :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/fCC_product.png)
_Le produit final_

## Conclusion

Nous avons réussi à incorporer du code CSS dans notre HTML et appliqué avec précision des styles CSS à notre contenu. Prenez maintenant quelques minutes pour créer quelque chose de similaire pour vous-même. Assurez-vous de jouer avec toutes les valeurs pour comprendre complètement comment elles fonctionnent.

_Cet article provient de [mon cours complet LPI Web Development Essentials Study Guide](https://www.udemy.com/course/complete-lpi-web-development-essentials-exam-study-guide/?referralCode=C92570BCBB38302A9257)._ _Et il y a beaucoup plus de bonnes choses technologiques disponibles sur [bootstrap-it.com](https://bootstrap-it.com/)_