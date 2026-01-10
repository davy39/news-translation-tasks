---
title: Comment améliorer instantanément l'apparence de vos projets front end
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-09T11:07:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-your-front-end-projects
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c3f740569d1a4ca30eb.jpg
tags:
- name: Bootstrap
  slug: bootstrap
- name: colors
  slug: colors
- name: CSS
  slug: css
- name: Design
  slug: design
- name: front end
  slug: front-end
- name: Front-end Development
  slug: front-end-development
- name: frontend
  slug: frontend
- name: HTML
  slug: html
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Comment améliorer instantanément l'apparence de vos projets front end
seo_desc: 'By Peter Gleeson

  We’ve all been there. You’ve been learning the basics of front end Web development,
  and you are keen to try out some new ideas.

  You take the time to code up the perfect HTML page, and add some styles and JavaScript
  for good measure.

  ...'
---

Par Peter Gleeson

Nous y sommes tous passés. Vous apprenez les bases du développement Web front end et vous êtes impatient d'essayer de nouvelles idées.

Vous prenez le temps de coder la page HTML parfaite et ajoutez quelques styles et du JavaScript pour faire bonne mesure.

Puis vous faites une pause. Il est temps de faire un pas en arrière et de voir à quoi ressemblent vos efforts dans le navigateur.

Assez terrible, n'est-ce pas ?

C'était certainement mon expérience lorsque j'ai appris pour la première fois un peu de développement front end.

J'avais mis beaucoup de réflexion dans la fonctionnalité du site. Mais lorsque j'ai tout assemblé, cela avait l'air affreux.

Je voulais partager mon travail avec quelques amis pour obtenir des commentaires. Mais dans son état actuel, mon site n'était pas prêt.

Vous voyez, la fonctionnalité n'est que la moitié de l'histoire. Nous, les humains, pour une raison quelconque, sommes biaisés envers l'apparence ou la présentation de quelque chose.

Peut-être sommes-nous plus susceptibles de faire confiance à un site qui semble professionnel et bien conçu. Ou peut-être que la valeur esthétique d'un site bien conçu peut nous aider à ignorer les petits défauts de fonctionnalité.

Quelle que soit la raison, une sorte d'[effet de halo](https://en.wikipedia.org/wiki/Halo_effect) existe bel et bien dans le développement Web.

Dans cet article, vous apprendrez quelques conseils faciles pour améliorer l'apparence de votre projet front end laid en un rien de temps.

### Le point de départ

Ci-dessous se trouve un exemple de simple page HTML sans aucun style.

%[https://codepen.io/pg2020/pen/PoqOQmG]

Ce sera le point de départ pour le reste de l'article. Chaque conseil s'appuiera sur les précédents jusqu'à ce que vous ayez une page plus belle à travailler.

Nous allons procéder par ordre d'impact. C'est-à-dire que nous commencerons par le conseil qui vous apporte l'amélioration la plus rapide et ferons des gains de plus en plus petits au fur et à mesure.

### Ajoutez de l'espace négatif

Le premier conseil est facile à imaginer, mais doit être mis en pratique avec soin.

L'espace négatif' fait référence à l'espace vide entre les éléments de la page.

Obtenir la bonne quantité d'espace négatif contribue grandement à rendre votre page plus belle.

Plus précisément, cela fait deux choses :

* Cela rend la page moins encombrée. Il est plus facile de trouver les différents éléments, car l'espace négatif les aide à se démarquer les uns des autres.
* Cela utilise mieux l'espace disponible à l'écran. Espacer soigneusement les éléments peut aider à remplir les parties de l'écran qui sont plus centrales et réduire le contenu dans les parties sur les bords.

Vérifiez le CSS dans l'exemple ci-dessous. Cela ajoute un peu d'espace négatif de base à l'exemple simple que vous avez vu précédemment.

Et voici le résultat :

%[https://codepen.io/pg2020/pen/oNXoEWK]

Remarquez ce qui s'est passé ici :

* Le padding crée de l'espace à l'intérieur d'un élément
* La marge crée de l'espace entre les éléments
* La taille de la ligne rend le texte moins encombré

Trop d'espace vide n'est pas une bonne chose. Il peut être difficile d'obtenir le bon équilibre.

### Associez vos polices

Le conseil suivant est un autre qui a un impact rapide.

Les polices système par défaut sont très sûres et sensées. Elles sont garanties pour fonctionner.

Mais le choix de la police fait une énorme déclaration sur le but et le ressenti de votre site.

* Les polices légères et ludiques disent au spectateur que cette page est amusante et accessible
* Les polices sensées et simples donnent une apparence plus professionnelle
* Les polices traditionnelles ou d'affichage donnent une apparence plus intemporelle et classique.

Vous comprenez l'idée.

Mais comment le mettre en pratique ?

La clé est d'utiliser des paires de polices.

L'idée est que l'utilisation de deux polices pour différents éléments sur la page fournit un contraste utile. Encore une fois, cela aide à faire ressortir les éléments et rend votre page plus facile à visualiser.

Mais vous ne devriez pas associer n'importe quelles polices.

Pour [plusieurs raisons esthétiques](https://www.canva.com/learn/combining-fonts-10-must-know-tips-from-a-designer/), certaines associations de polices ont beaucoup mieux l'air que d'autres.

Ne vous inquiétez pas de comprendre cela par vous-même, cependant. Comme d'habitude, il y a des ressources sur Internet pour vous aider.

Consultez [fontpair.co](https://www.freecodecamp.org/news/how-to-make-your-front-end-projects/fontpair.co). Il vous permet de parcourir différentes associations de polices et de voir à quoi elles ressemblent ensemble.

Une fois que vous avez trouvé une association que vous aimez, le moyen le plus rapide de les utiliser dans votre projet est de vous rendre sur [Google Fonts](https://fonts.google.com/).

* Recherchez les polices que vous voulez
* Ajoutez-les à votre projet
* Incluez le lien dans votre élément HTML `<head>`
* Référencez les polices dans la feuille de style

Voir ci-dessous pour un exemple construit sur la base de la page de base que vous avez vue précédemment.

%[https://codepen.io/pg2020/pen/ZEGaraM]

Vous pouvez également améliorer l'apparence en contrôlant la taille de la police et l'alignement du texte.

Cela ne semble-t-il pas considérablement mieux ? Et après seulement deux étapes faciles.

### Obtenez une palette de couleurs

Je ne suis pas designer, mais j'apprécie la valeur d'apprendre [les bases de la théorie des couleurs](https://lifehacker.com/learn-the-basics-of-color-theory-to-know-what-looks-goo-1608972072).

En bref, les couleurs que vous utilisez sur votre page contribuent grandement à créer une impression.

Par exemple :

* Des couleurs vives et exubérantes créent une sensation énergique
* Des teintes légères et atténuées créent une impression plus corporative
* Des couleurs sombres et contrastées créent une impression plus dramatique
* Les couleurs de marque créent une identité cohérente

Encore une fois, il est payant de choisir vos couleurs avec soin.

La théorie veut que la relation entre les couleurs que vous utilisez impacte également l'apparence de votre site.

* Les couleurs analogues peuvent créer une apparence cohérente et harmonieuse
* Les couleurs complémentaires créent un contraste agréable
* Les couleurs triadiques fournissent à la fois contraste et équilibre

Il est payant de choisir une palette de couleurs avec soin.

Heureusement, il existe de nombreuses façons de le faire. Il suffit de chercher "générateur de palette de couleurs" sur Google et vous serez gâté par le choix.

Un de mes outils préférés est [colormind.io](http://colormind.io/template/paper-dashboard/). Il génère une palette de couleurs et vous permet de la prévisualiser sur un modèle.

Bien sûr, les règles peuvent être enfreintes. Utiliser une palette de couleurs plus discordante peut être déstabilisant, mais utilisée avec soin peut donner à une page une apparence plus audacieuse et plus distinctive.

Voir le code ci-dessous a été mis à jour pour utiliser une palette de couleurs simple.

%[https://codepen.io/pg2020/pen/MWwOQXq]

### Ajoutez une structure

Peu importe à quel point votre page est bien présentée maintenant, elle peut être améliorée en secouant un peu les choses.

Ajouter des sections et une structure peut briser la monotonie d'une page plus longue.

En créant des limites claires entre les éléments, vous pouvez créer une structure logique et/ou une hiérarchie. Cela facilitera la compréhension de la disposition de votre page par le spectateur.

Gardez la même palette de couleurs, mais variez un peu les choses.

Voir l'exemple ci-dessous a été étendu pour inclure plus de structure. Le contenu est divisé en éléments `<header>`, `<footer>` et `<div class="content">`.

L'exemple utilise également une requête média pour que la page se présente mieux sur les petits appareils.

%[https://codepen.io/pg2020/pen/zYGPRVg]

Si vous voulez en savoir plus, essayez de vous renseigner sur :

* [CSS Grid](https://css-tricks.com/snippets/css/complete-guide-grid/) pour créer une mise en page
* [Flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox) pour créer des mises en page
* [Bootstrap](https://getbootstrap.com/docs/3.4/css/) pour créer des designs réactifs
* Design réactif avec [media queries](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Media_queries)

Cela n'a pas pris beaucoup de réécriture, mais l'effet est très noticeable.

### Ajoutez des images et des icônes

Les humains sont typiquement des créatures visuelles. Une image ou une icône bien placée peut grandement contribuer à rendre une page plus facile à visualiser et à comprendre.

Le code ci-dessous ajoute une image simple au contenu principal. Voyez comment elle est incluse dans l'élément `<div class="content">` et la largeur est définie à 100 % ? Cela maintient la structure de la page cohérente.

N'oubliez pas que les images doivent être considérées dans le contexte de la palette de couleurs globale.

Vous n'avez pas besoin d'être un artiste CSS en herbe ou un magicien de Photoshop pour faire cela. Si vous avez besoin d'un accès rapide à des photos de haute qualité, vous pouvez rechercher sur [Unsplash](https://unsplash.com/) des images libres de droits.

Même quelques icônes gratuites peuvent faire la différence.

L'exemple ci-dessous ajoute une simple icône de menu en haut à droite. Vous pourriez également ajouter des icônes à votre profil Github, ou à d'autres profils en ligne.

%[https://codepen.io/pg2020/pen/zYGPWrY]

Vous pouvez rapidement ajouter des icônes gratuites à partir de ces ressources :

* [Fontawesome](https://fontawesome.com/)
* [Bootstrap](https://icons.getbootstrap.com/)
* [Google](https://material.io/resources/icons/?style=baseline)
* [Plenty of others](https://www.keycdn.com/blog/icon-library)

### Ajoutez des animations

Ce dernier conseil est un plus, c'est sûr.

Comme le sait toute personne ayant utilisé PowerPoint dans les années 2000, les animations doivent être utilisées avec soin.

Trop d'animations peuvent être déroutantes et irritantes pour les utilisateurs.

Mais utilisées correctement, elles peuvent rendre une page beaucoup plus interactive et visuellement attrayante.

Il existe de nombreuses façons d'ajouter des animations à votre site. Vous pouvez utiliser des [sélecteurs CSS](https://www.w3schools.com/cssref/sel_hover.asp) pour changer de style en réponse à certains événements, comme lorsque l'utilisateur survole cet élément.

L'exemple ci-dessous change l'opacité de l'image à 50 % lorsque l'utilisateur la survole.

Une autre option est d'utiliser [Animate.css](https://daneden.github.io/animate.css/). Cela fournit un certain nombre d'animations pré-construites que vous pouvez utiliser directement.

Le code ci-dessous ajoute une animation subtile aux boutons lorsqu'ils sont cliqués.

%[https://codepen.io/pg2020/pen/xxGPWEZ]

N'oubliez pasavec l'animation, moins est généralement plus !

#### Le résultat final

Voir [ce dépôt Github](https://github.com/pg0408/frontend-demo) pour l'évolution globale de la page.

Le design a encore un long chemin à parcourir. Mais en suivant simplement quelques directives, il a beaucoup mieux l'air qu'au début.

Voici un rapide récapitulatif de chacun des conseils :

1. Ajoutez de l'espace négatif
2. Choisissez une paire de polices
3. Sélectionnez une palette de couleurs cohérente
4. Ajoutez une structure
5. Ajoutez quelques icônes ou images
6. (Optionnellement) ajoutez des animations

Laissez une réponse ci-dessous si vous avez trouvé ce guide rapide utile. Avez-vous des conseils ou astuces à partager ?

Merci d'avoir lu !