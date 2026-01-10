---
title: Comment afficher des blocs de code dans Medium
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2016-09-18T17:49:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-code-to-medium-and-get-syntax-highlighting-d699761a5883
coverImage: https://cdn-media-1.freecodecamp.org/images/1*SKIAmwDYVnrMvFOopOCwPQ.png
tags:
- name: medium
  slug: medium
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment afficher des blocs de code dans Medium
seo_desc: 'And how to write inline code and embed code for syntax highlighting

  Medium makes it easy to add code blocks and inline

  Medium has a hidden shortcut that will turn text plain text…

  if (developer === true) {

  follow(this.mediumPublication);

  }

  …into a fo...'
---

#### Et comment écrire du code en ligne et intégrer du code pour la coloration syntaxique

Medium facilite l'ajout de blocs de code et de code en ligne

#### Medium a un raccourci caché qui transformera du texte brut...

if (developer === true) {

follow(this.mediumPublication);

}

#### ...en un bloc de code formaté :

```
if (developer === true) {
```

```
  follow(this.mediumPublication);
```

```
}
```

Pour ce faire, sélectionnez le texte, puis appuyez sur :

* **Windows** : Control + Alt + 6
* **Mac** : Command + Option + 6
* **Linux** : Control + Alt + 6

**Mise à jour du 19 octobre 2016** : Medium supporte désormais la convention courante de commencer un bloc de code avec trois backticks. Si vous tapez ``` sur une nouvelle ligne, Medium passera en mode saisie de code. Un grand merci à [Luke Esterkyn](https://www.freecodecamp.org/news/how-to-add-code-to-medium-and-get-syntax-highlighting-d699761a5883/undefined) et au reste de l'équipe Medium pour avoir implémenté cela !

Vous pouvez également mettre en évidence du code en ligne en le sélectionnant, puis en cliquant sur la touche backtick (`). Par exemple, vous pouvez formater du texte en tant que code `freeCodeCamp()` directement au milieu d'une phrase.

Vous pouvez également intégrer des extraits GitHub en collant leur URL dans une ligne vide, puis en appuyant sur entrée :

### Comment intégrer des applications web

En bonus, vous pouvez intégrer des applications exécutables directement dans Medium. Au cas où celles-ci ne s'afficheraient pas correctement dans les applications mobiles de Medium, je recommande d'inclure des liens sous chaque intégration comme solution de repli.

Collez une URL CodePen.io dans Medium, puis appuyez sur entrée :

_View my CodePen [here](http://codepen.io/FreeCodeCamp/pen/NNvBQW)._

Vous pouvez également le faire avec JSFiddle.net :

_View my JSFiddle [here](https://jsfiddle.net/avegt5e5/3/)._

### Mais n'utilisez pas d'images de code.

Même si cela peut sembler pratique de prendre des captures d'écran de votre code et de les coller dans Medium, ne faites pas cela.

Medium n'a pas encore d'option de texte alternatif, ce qui rendra votre code complètement inaccessible aux développeurs malvoyants. Et oui, [ils existent](https://medium.freecodecamp.com/looking-back-to-what-started-it-all-731ef5424aec#.fae9jgbx6).

Vous ne pouvez pas non plus changer la taille de la police des images statiques, ce qui rend la lecture difficile sur un téléphone mobile (où la plupart des gens lisent Medium).

Enfin, cela rend impossible pour les lecteurs de copier et coller votre code.

Je sais, je sais — vous ne devriez pas copier et coller du code de toute façon.

Mais soyons réalistes — les gens le font. Et la plupart des gens abandonneront rapidement votre tutoriel s'ils doivent taper manuellement beaucoup de code.

Donc, pour résumer :

* utilisez les blocs de code natifs de Medium
* ou intégrez des extraits GitHub
* utilisez des exemples fonctionnels de CodePen et JSFiddle lorsque cela est possible
* mais ne collez pas d'images de code

Bon codage et bon écriture sur le codage !

**Je n'écris que sur la programmation et la technologie. Si vous [me suivez sur Twitter](https://twitter.com/ossia), je ne perdrai pas votre temps. ?**