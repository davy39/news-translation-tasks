---
title: Apprendre le HTML en 5 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-27T11:48:40.000Z'
originalURL: https://freecodecamp.org/news/learn-html-in-5-minutes-ccd378d2ab72
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4psHn7qR2v1O5kBhJQ_T2w.png
tags:
- name: HTML5
  slug: html5
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Apprendre le HTML en 5 minutes
seo_desc: 'By Eric Tirado

  A quick tutorial to help you get started building websites.

  HTML is the markup language used for structuring and presenting content on the World
  Wide Web. Together with CSS and JavaScript, it enables us to have beautiful and
  interactiv...'
---

Par Eric Tirado

#### Un tutoriel rapide pour vous aider à commencer à construire des sites web.

Le HTML est le langage de balisage utilisé pour structurer et présenter le contenu sur le World Wide Web. Avec CSS et JavaScript, il nous permet d'avoir des sites web beaux et interactifs.

Puisque le HTML est la base du web, c'est aussi le langage le plus essentiel pour toute carrière en développement web. Dans ce tutoriel rapide, je vais vous enseigner les bases.

> Et quand vous aurez terminé, **j'ai déjà lancé un cours gratuit en 14 parties sur le HTML5** sur Scrimba.com — une plateforme interactive où vous pouvez plonger dans le code d'un screencast à tout moment.

Vous pouvez consulter la première leçon ici :

![Image](https://cdn-media-1.freecodecamp.org/images/oq6Q3enVyEjlrywgdjb6A4Sti2KLmGkl-j5i)

Très bien, avant de plonger dans le HTML, je veux commencer par vous parler un peu de l'architecture du web. Cela mettra en perspective le rôle du HTML pour nous.

### Architecture web de base

Une fois que vous avez développé un site web, vous devez l'héberger sur un serveur pour le rendre accessible sur le World Wide Web. Tous les serveurs ont une adresse IP (par exemple, 149.56.240.169) que vous pouvez considérer comme un numéro de téléphone. Nous plaçons généralement un nom de domaine (par exemple, scrimba.com) sur cette adresse IP, afin qu'elle soit plus facile à retenir.

Lorsque vous tapez ce nom de domaine dans le navigateur, il appelle le serveur. Le serveur envoie ensuite un ensemble de fichiers HTML, CSS et JavaScript, comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/BRF0UCTRXQwPmChUfudbIZnnelGaVxlnpiN1)

Votre navigateur commence par charger le fichier HTML principal, avant de continuer avec le CSS et le JavaScript. Ces fichiers permettent au navigateur de rendre un site web beau et interactif.

Maintenant, examinons de plus près les rôles que jouent ces trois langages.

#### Qu'est-ce que le HTML ?

Imaginons un site web comme une personne. Nous utiliserons cette analogie pour comprendre notre site web. Le HTML est mieux décrit comme le squelette :

![Image](https://cdn-media-1.freecodecamp.org/images/VjV6nvDloznKazqZhXbn6tXzcb5zVPleJLn5)

#### Qu'est-ce que le CSS ?

Cependant, un site web en HTML seul semble assez laid, donc vous devez le styliser avec du CSS. Il peut être vu comme la peau et les vêtements du site web.

![Image](https://cdn-media-1.freecodecamp.org/images/lZv-vAkRnVxCmzO0utjYN6iAa8bQxRveAY4n)

#### Qu'est-ce que le JavaScript ?

Une fois que vous maîtrisez le CSS, vous devriez continuer avec le JavaScript. Dans notre analogie, cela ressemble au cerveau et aux muscles de notre site web :

![Image](https://cdn-media-1.freecodecamp.org/images/dsna40xpfnzPvB8Nymr1UbyfcUdXc6e7PfGa)

### Écrire votre premier fichier HTML

Pour pouvoir écrire du HTML, vous aurez besoin d'un document HTML, qui est simplement un document avec une extension _.html_. Peu importe quel éditeur de texte vous utilisez, mais les plus populaires ces jours-ci sont [Sublime Text](https://www.sublimetext.com/3), [VS Code](https://code.visualstudio.com/download) et [Atom](https://atom.io/). Vous pouvez également utiliser [Scrimba](http://scrimba.com) comme éditeur dans le navigateur.

Créons un nouveau fichier, appelons-le _index.html_, et écrivons `Bonjour le monde !` dedans.

```
Bonjour le monde !
```

Si nous glissons ce fichier dans le navigateur, ou si nous pointons le navigateur vers l'adresse de ce fichier, nous obtiendrons ce qui suit.

![Image](https://cdn-media-1.freecodecamp.org/images/rTzDGGpCh3jeFfxV-AcUrppuVUP1Ao003VXj)
_Comment cela apparaît dans Scrimba lorsque vous ouvrez notre fichier index.html dans une fenêtre de navigateur._

Félicitations, vous venez de créer votre premier site web !

### Votre première balise HTML

Cependant, nous n'avons pas encore écrit de balises HTML. Pour cela, enveloppons le texte `Bonjour le monde !` dans des balises `<h1>`, comme ceci :

```
<h1>Bonjour le monde !</h1>
```

La première `<h1>` est une balise ouvrante, et la seconde, `</h1>`, est une balise fermante. Comme vous pouvez le voir, la différence est seulement la barre oblique dans la balise fermante. Cela donnera le résultat suivant sur la page :

![Image](https://cdn-media-1.freecodecamp.org/images/-MC8Z3OmD4TJUQXM5ZXe7HuQdLAQwA7tDFcL)

Vous venez de dire au navigateur que vous voulez que le texte `Bonjour le monde !` soit un titre. Ainsi, le navigateur applique un certain style, augmentant essentiellement la taille du texte.

C'est donc aussi simple que cela pour commencer à écrire du HTML.

### Écrire un document HTML correct

Mais ceci n'est en fait pas un document HTML valide, car ils doivent suivre une structure clairement définie. Dans le cadre de ce tutoriel, je vais simplement vous le montrer brièvement, puis nous continuerons avec les choses amusantes.

Voici à quoi devrait ressembler notre exemple `Bonjour le monde !` :

```
<!DOCTYPE html><html>  <head>  </head>  <body>    <h1>Bonjour le monde !</h1>  </body></html>
```

Vous n'avez pas à vous soucier de la balise `<!DOCTYPE html>`, `<html>` et `<head>` pour l'instant, car nous allons simplement écrire notre contenu dans la balise `<body>`. Continuons avec cela !

#### Paragraphes

Sous la balise h1, nous allons ajouter un paragraphe. Cette balise est généralement utilisée pour, eh bien, des paragraphes de texte.

```
<h1>Bonjour le monde !</h1><p>Bonjour, et bienvenue sur mon site web !</p>
```

Voici à quoi cela ressemble :

![Image](https://cdn-media-1.freecodecamp.org/images/ENf-gB8JjSydpHEnFQ2P23EU1ED6sq59Ex6q)

#### Listes

Maintenant, ajoutons une liste. Pour cela, nous devons ajouter deux balises différentes, `<ul>` et `<li>`. La première signifie _liste non ordonnée_ et la seconde signifie _élément de liste_. Nous devons envelopper les balises `<li>` à l'intérieur de la balise `<ul>`.

```
<ul>  <li>Manger</li>  <li>Dormir</li>  <li>Coder</li></ul>
```

![Image](https://cdn-media-1.freecodecamp.org/images/8R5TVf7aPKSVX-KjJKDhFCkfAyQ-Yi32sAR8)

Si vous changez `<ul>` en `<ol>`, alors les puces seront remplacées par des nombres, car cela signifie _liste ordonnée_.

#### Champs de saisie

Obtenir des entrées des utilisateurs est une activité critique sur les sites web. Ajoutons un champ de saisie.

```
<input type="text" placeholder="Entrez votre email" />
```

Ce qui ajouterait le champ de saisie en bas de notre site :

![Image](https://cdn-media-1.freecodecamp.org/images/eWzjBQ8hS6ACs66Ptp4tlBtSiegkxBuK-eJj)

Il y a deux nouveaux concepts à apprendre ici : les _attributs_ et les _balises auto-fermantes_. Le premier, les _attributs_, fournit des informations supplémentaires sur les éléments HTML.

Dans notre cas, nous ajoutons deux attributs : _type_ et _placeholder_. Le _type_ indique au navigateur que cela doit être un champ de texte. Ici, nous aurions pu choisir parmi une gamme de types (radio, select, checkbox, date) qui l'auraient transformé en éléments complètement différents.

Le _placeholder_ dicte le texte d'aide à l'intérieur de l'élément.

Enfin, la balise input est également un élément _auto-fermant_ (également connu sous le nom d'élément vide), ce qui signifie qu'elle ne se compose pas d'une balise ouvrante et fermante, mais d'une seule balise qui se ferme elle-même.

### Prochaines étapes

Il y a tellement plus de choses à apprendre en HTML, et ce n'est pas difficile du tout. Mon cours complet peut être terminé en moins d'une heure, et il vous donnera une solide compréhension des bases et vous permettra de commencer à construire de vrais sites web !

> Si vous en voulez plus, nous avons un repas gratuit en 14 cours...
> sur mon cours [Apprendre le HTML5 gratuitement](https://scrimba.com/g/ghtml) sur Scrimba.com.

À bientôt. ?