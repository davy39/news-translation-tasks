---
title: Comment rendre votre bouton SVG élégant accessible
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-13T14:19:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-your-fancy-svg-button-accessible-83c9172c3c15
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3Femts-5Nx83ChD5l6_IKw.jpeg
tags:
- name: Accessibility
  slug: accessibility
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment rendre votre bouton SVG élégant accessible
seo_desc: 'By Jonathan Speek

  You may very well find yourself one day having to build some crazy button a designer
  dreamed-up. You might start reaching for that good old <div>, but easy there big-shifter
  ? — let’s try and use that <;button> element you’re avoidi...'
---

Par Jonathan Speek

Il se peut très bien que vous vous retrouviez un jour à devoir construire un bouton fou qu'un designer a imaginé. Vous pourriez commencer à utiliser ce bon vieux `<div>`, mais attention, grand changur ? — essayons d'utiliser cet élément `<button>` que vous évitez ?

Nous allons commencer par simplement prendre le code pour une icône SVG que nous voulons utiliser. J'ai rapidement créé une icône Chemex que vous pouvez utiliser [ici](https://codepen.io/JonathanSpeek/pen/pQxYqo) (j'adore le café ). Collez cela entre une balise `<button>` dans votre HTML comme ceci (le code SVG sera assez long).

![Image](https://cdn-media-1.freecodecamp.org/images/QA6qC1qblNFuf4906Gd5zip2X65AIlLbreSY)
_Bouton initial &lt;button&gt; avec le code SVG à l'intérieur_

Nous voulons que ce bouton soit dépouillé de son style par défaut, alors donnons au bouton un "id" et nous le ciblerons avec un peu de CSS.

![Image](https://cdn-media-1.freecodecamp.org/images/9eN7Cfrt9QplVmdH5X-XkbzcIruiogzzphqk)
_Supprimer le style par défaut du &lt;button&gt; pour pouvoir l'améliorer ?_

Donnez au bouton une bonne largeur/hauteur qui est plus grande que notre SVG — cela aidera la visibilité du contour. À propos, assurez-vous que le ratio de contraste entre la couleur de votre contour et la couleur de fond [passe ce test](https://userway.org/contrast-checker). Supprimez cette bordure et ce fond gênants, assurez-vous que le curseur est défini sur le pointeur.

À ce stade, vous avez un bouton cliquable qui, lorsqu'il est cliqué, montre le contour par défaut que votre navigateur a choisi pour les états de focus. Changeons cela et améliorons-le.

![Image](https://cdn-media-1.freecodecamp.org/images/JOqPbxdOEC3bTevV0lZqTGpDYsVWEGXpDzfq)
_Donner au bouton un peu de focus ?_

Maintenant, lorsque nous cliquons ou tabulons vers notre bouton, nous obtenons un petit contour en pointillés qui nous indique où nous sommes focalisés.

Nous voulons également nous assurer que le SVG lui-même ne reçoit pas de contour s'il est cliqué. Et nous voulons nous assurer que Firefox n'ajoute pas son contour en pointillés par défaut. Pendant que nous y sommes, nous pouvons donner au SVG un petit effet de survol.

![Image](https://cdn-media-1.freecodecamp.org/images/dqTv6Xmdit1jeW4tKrmaAUrZbY9ZzVizMfoF)
_Ajout de notre effet de survol savoureux ?_

Maintenant, nous pouvons passer aux parties intéressantes ? Nous ne voulons pas ennuyer ou confondre nos utilisateurs de lecteurs d'écran avec notre bouton. Nous avons donc besoin d'une bonne description courte de ce à quoi s'attendre. Vous voudriez également que les utilisateurs visuels aient une idée de ce qu'ils cliquent, mais pour l'instant, laissons-les deviner...

Nous pouvons facilement y parvenir en mettant un élément `<span>` autour du texte dans notre bouton et en le stylisant hors de vue. Assurez-vous de ne pas définir l'affichage sur "none", car cela empêchera également nos lecteurs d'écran d'y accéder.

![Image](https://cdn-media-1.freecodecamp.org/images/RAJN2axCgcQ70Dz6ZOhbiIuad51OzHmAqcXE)
_Dire à nos utilisateurs de lecteurs d'écran ce qu'ils cliquent ?_

Enfin, assurons-nous que nous avons :

* caché le SVG de toute personne utilisant des technologies d'assistance et
* défini l'index de tabulation sur "0" afin que le navigateur utilise l'ordre de tabulation attendu pour tout utilisateur de clavier.

![Image](https://cdn-media-1.freecodecamp.org/images/wAPj780H1xSCzWJQkOe2Z0miBrj1R2N7n3XT)
_Définir le bon ordre de tabulation _

Vous devriez maintenant avoir un bouton vraiment accessible dont vous pouvez être fier ? En plus de vous féliciter — faites-le maintenant — à l'avenir, vous avez maintenant quelques modèles réutilisables que vous pouvez implémenter pour aider à rendre le web juste un peu plus accessible ?

Voici un [lien vers l'exemple CodePen](https://codepen.io/JonathanSpeek/pen/JeRwgp), n'hésitez pas à fork votre propre copie ?

Merci d'avoir lu. Si vous avez des connaissances à partager sur l'accessibilité, n'hésitez pas à laisser un commentaire.

Et vous pouvez [me suivre sur Twitter ici](https://twitter.com/intent/follow?screen_name=jonspeek).