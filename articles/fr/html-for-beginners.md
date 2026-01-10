---
title: HTML pour débutants – Comment commencer avec les bases du développement web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-01T23:34:27.000Z'
originalURL: https://freecodecamp.org/news/html-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/jackson-sophat-_t-l5FFH8VA-unsplash.jpg
tags:
- name: beginner
  slug: beginner
- name: HTML
  slug: html
seo_title: HTML pour débutants – Comment commencer avec les bases du développement
  web
seo_desc: 'By Patrick Cyubahiro

  Have you always been interested in learning HTML but didn''t know where or how to
  start? Well, this guide is for you.

  In it, we will look at:


  An introduction to HTML

  A Brief History of HTML

  Why Learn HTML?

  Prerequisites for learn...'
---

Par Patrick Cyubahiro

Avez-vous toujours été intéressé à apprendre le HTML mais vous ne saviez pas où ni comment commencer ? Eh bien, ce guide est pour vous.

Dans ce guide, nous allons examiner :

* Une introduction au HTML
* Un bref historique du HTML
* Pourquoi apprendre le HTML ?
* Les prérequis pour apprendre le HTML
* Une page HTML simple
* Comment commencer avec le HTML

## Introduction au HTML

![Image](https://www.freecodecamp.org/news/content/images/2023/03/_l2KHAg0A.jpg)

HTML est l'abréviation de HyperText Markup Language.

Cet acronyme est composé de deux parties principales : HyperText et Markup Language.

### Que signifie "HyperText" ?

HyperText fait référence aux hyperliens ou simplement aux liens qu'une page HTML peut contenir. Un HyperText peut contenir un lien vers un site web, un contenu web ou une page web.

### Qu'est-ce qu'un "Markup language" ?

Un langage de balisage est un langage informatique qui se compose de mots-clés, de noms ou de balises facilement compréhensibles qui aident à formater la vue globale d'une page et les données qu'elle contient. En d'autres termes, il fait référence à la manière dont les balises sont utilisées pour définir la mise en page et les éléments d'une page.

Maintenant que nous savons ce que signifient HyperText et Markup Language, nous pouvons également comprendre ce que ces termes signifient lorsqu'ils sont combinés.

### Qu'est-ce que le HTML ?

HTML ou HyperText Markup Language est un langage de balisage utilisé pour décrire la structure d'une page web. Il utilise une syntaxe ou une notation spéciale pour organiser et fournir des informations sur la page au navigateur.

Le HTML se compose d'une série d'éléments qui indiquent au navigateur comment afficher le contenu. Ces éléments étiquetent des morceaux de contenu tels que "ci-ci est un titre", "ci-ci est un paragraphe", "ci-ci est un lien", et ainsi de suite. Ils ont généralement des balises d'ouverture et de fermeture qui entourent et donnent un sens à chaque morceau de contenu.

Il existe différentes options de balises que vous pouvez utiliser pour envelopper du texte afin de montrer si le texte est un titre, un paragraphe ou une liste. Les balises ressemblent à `<h1>` (balise d'ouverture) et `</h1>` (balise de fermeture).

Voyons quelques autres exemples :

```html

<h1> Ceci est pour le titre de niveau supérieur ; et dans la plupart des cas, c'est un titre de page</h1> 

<p>Un paragraphe. C'est ici que l'information que nous souhaitons communiquer au spectateur est placée. Cela peut être aussi long ou court que nous le souhaitons. Remarque : Un paragraphe commence toujours sur une nouvelle ligne, et les navigateurs ajoutent automatiquement un espace vide unique (ou une ligne) avant et après un paragraphe.</p> 

<ol> 
<li>Voici le premier élément</li> 
<li>Voici le deuxième élément</li> 
<li>Voici le troisième élément</li> 
</ol>   
```

## Un bref historique du HTML

La première version du HTML a été écrite en 1993 ; depuis lors, de nombreuses versions différentes de HTML ont été publiées, permettant aux développeurs de créer des pages web interactives avec des images animées, du son et des gadgets de toutes sortes.

La version la plus largement utilisée tout au long des années 2000 était HTML 4.01, qui est devenue une norme officielle en décembre 1999.

Une autre version, XHTML, était une réécriture de HTML en tant que langage XML.

En 2014, HTML5 a été publié, et il a pris le relais des versions précédentes de HTML. Cette version inclut de nouveaux éléments et capacités ajoutés au langage. Ces nouvelles fonctionnalités vous permettent de créer des sites web et des applications web plus puissants et complexes, tout en gardant le code plus facile à lire.

## Pourquoi apprendre le HTML ?

Le HTML est la base de toutes les pages web. Sans HTML, vous ne pourriez pas organiser du texte ou ajouter des images ou des vidéos à vos pages web. Le HTML est la racine de tout ce que vous devez savoir pour créer des pages web magnifiques !

Comme le suggère le nom, l'hypertexte fait référence à la référence croisée (ou au lien) entre différentes sections ou pages web liées sur le world-wide-web.

Le langage de balisage hypertexte est un langage de balisage standard qui permet aux développeurs de structurer, lier et présenter des pages web sur le world-wide-web. Il est donc important de connaître la structure et la mise en page du site web que vous souhaitez construire.

## Prérequis pour apprendre le HTML

Le HTML est un langage relativement facile et ne nécessite aucune éducation formelle. Donc, en gros, il n'y a pas de prérequis pour l'apprendre.

Le HTML est un codage informatique basé sur du texte, et tout le monde peut l'apprendre et l'exécuter, tant qu'il comprend les lettres et les symboles de base. Donc, tout ce dont vous avez besoin, ce sont des connaissances de base en informatique et la capacité de travailler avec des fichiers.

Bien sûr, toute connaissance d'autres langages de programmation améliorera vos capacités avec le HTML et le développement web, mais ce n'est pas un prérequis pour apprendre le HTML.

## À quoi ressemble une page HTML simple

```html

<!DOCTYPE html> 
<html> 
<head> 
<title> Patrick Cyubahiro </title> 
</head> 

<body> 
<h1>Ceci est mon premier titre</h1> 

<p>Ceci est mon premier paragraphe.</p> 

</body> 
</html>
```

D'accord, voyons ce qui se passe ici :

```

La déclaration <!DOCTYPE html> indique que ce document est un document HTML5.

L'élément <html> est l'élément racine d'une page HTML.

L'élément <head> contient des méta-informations sur la page HTML.

L'élément <title> spécifie un titre pour la page HTML (qui est affiché dans la barre de titre du navigateur ou dans l'onglet de la page).

L'élément <body> définit le corps du document et est un conteneur pour tout le contenu visible, tel que les titres, les paragraphes, les images, les hyperliens, les tableaux, les listes, etc.

L'élément <h1> définit un grand titre.

L'élément <p> définit un paragraphe. 
```

**Remarque :** En HTML, une balise d'ouverture commence une section de contenu de page, et une balise de fermeture la termine.

Par exemple, pour marquer une section de texte comme un paragraphe, vous ouvrirez le paragraphe avec une balise d'ouverture de paragraphe, qui est "<p>", et vous le fermerez avec une balise de fermeture de paragraphe, qui est "</p>".

Dans les balises de fermeture, l'élément est toujours précédé d'une barre oblique ("/").

## Comment commencer avec le HTML

Il existe de nombreuses ressources en ligne différentes qui peuvent vous aider à apprendre le HTML. Je recommande les suivantes :

1. [freeCodecamp](https://www.freecodecamp.org/learn/) : une plateforme d'apprentissage interactive et gratuite qui vise à rendre l'apprentissage du développement web possible pour tous. Cette plateforme propose un contenu bien structuré, de bons exercices pour vous aider à comprendre le concept et une communauté de soutien qui peut vous aider en cas de difficultés pendant le cours.
2. [W3Schools](https://www.w3schools.com/html/) : une plateforme d'apprentissage qui couvre tous les aspects du développement web. Elle explique les balises HTML de manière très compréhensible et approfondie, ce qui facilite également l'apprentissage de leur utilisation.

## Conclusion

Apprendre certaines des bases du HTML peut ne pas prendre beaucoup de temps pour certaines personnes. Mais devenir vraiment bon en HTML, comme pour toute compétence, prend définitivement du temps. Vous pourriez être capable de comprendre les balises HTML de base en quelques heures, mais assurez-vous de prendre le temps d'apprendre à travailler correctement avec elles.

Je m'appelle Patrick Cyubahiro, je suis un développeur de logiciels et web, un designer UI/UX, un rédacteur technique et un constructeur de communauté.

J'espère que vous avez apprécié la lecture de cet article ; et s'il vous a été utile, n'hésitez pas à me le faire savoir sur Twitter : @[Pat_Cyubahiro](https://twitter.com/Pat_Cyubahiro) ou par email : ampatrickcyubahiro[at]gmail.com

Merci pour la lecture et bon apprentissage !