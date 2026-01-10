---
title: Comment j'ai créé un site web pour ma collection Apple
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-08T16:42:49.000Z'
originalURL: https://freecodecamp.org/news/creating-a-website-for-my-apple-collection
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/collection.jpg
tags:
- name: mac
  slug: mac
- name: projects
  slug: projects
- name: Website design
  slug: website-design
seo_title: Comment j'ai créé un site web pour ma collection Apple
seo_desc: "By Leonardo Faria\nA while ago I started an Apple collection. I've been\
  \ following Apple hardware (and its aesthetics) since I was a teenager, but at that\
  \ time I didn't the have money to own a Mac. \nI got my first Mac when I was 19.\
  \ It was an iBook 700..."
---

Par Leonardo Faria

Il y a quelque temps, j'ai commencé une collection Apple. Je suis les produits Apple (et leur esthétique) depuis mon adolescence, mais à l'époque, je n'avais pas les moyens de posséder un Mac.

J'ai obtenu mon premier Mac à 19 ans. C'était un iBook 700 MHz, acheté sur un site similaire à eBay au Brésil. L'argent provenait d'un projet Flash.

Après avoir vécu au Canada pendant quelques années, j'ai un peu d'argent supplémentaire à dépenser pour un hobby. La plupart du temps, j'achète les appareils à des particuliers sur Craigslist.

Après quelques ordinateurs portables et iDevices, j'ai décidé de commencer à collecter des informations sur mes iThings. Au début, j'ai créé un Gist contenant le modèle, le numéro de série, comment j'ai obtenu l'appareil, le système d'exploitation minimum/maximum, etc.

La liste n'a fait que s'allonger et le contenu a commencé à paraître désordonné. J'ai pensé que montrer ce contenu sur un site web serait parfait, et je n'avais pas besoin d'engager un développeur :D

Au début, j'ai décidé d'organiser mes données dans une base de données SQL, avec les informations réparties dans différentes colonnes et tables. Ensuite, j'aurais créé une API graphQL pour me fournir les données nécessaires à la population de mon interface utilisateur – probablement écrite en React, compilée avec Babel et emballée avec Webpack.

En lisant le paragraphe précédent à voix haute, vous pouvez voir qu'il y a beaucoup de technologies, et que j'ai même ignoré le langage backend et les détails de l'interface utilisateur comme SASS ou styled-components. Tout cela semblait un peu écrasant alors que mon objectif ultime était de montrer une liste d'objets dans un design agréable.

Cela dit, j'ai pensé à la manière dont je pourrais livrer ce contenu sans :

- Une API ou tout travail backend
- Aucun framework/bibliothèque JS
- Aucun outil JS (Webpack, Babel, etc.)
- Aucun travail CSS

En plus de ces contraintes, j'avais quelques objectifs supplémentaires :

- Créer un site web avec une bonne accessibilité
- Créer un site web qui fonctionne sur les anciens navigateurs, puisque j'ai des ordinateurs fonctionnant sous Mac OS 9.2 et des iDevices fonctionnant sous iOS 3

Défi accepté. Un index.html, quelques fichiers JS vanilla, et pas de CSS personnalisé. J'aimerais partager avec vous l'expérience de la construction du site.

TL,DR :

- [Site web final](https://bit.ly/collection-website)
- [Code source](https://bit.ly/collection-source)

Parlons des contraintes, point par point :

## Pas d'API ou de travail backend

Il y a quelque temps, j'ai vu un produit SaaS appelé [Stein](https://steinhq.com/). Vous créez vos données à l'intérieur d'un document Google Sheets et ils vous donnent un endpoint avec vos données. Leur bibliothèque fonctionne comme Handlebars, et cela semblait parfait pour mon cas d'utilisation :

```html
<div data-stein-url="https://api.steinhq.com/v1/storages/5cc158079ec99a2f484dcb40/Sheet1" data-stein-limit="2">
  <div>
    <h1>{{title}}</h1>
    <h6>Par {{author}}</h6>
 
    {{content}}
 
    Lire sur <a href="{{link}}">Medium</a>
  </div>
</div>
```

## Pas de framework/bibliothèque JS et d'outils

J'ai décidé d'éviter d'ajouter un framework ou une bibliothèque à ce projet puisque le cas d'utilisation n'en avait pas besoin. Toutes les interactions JS sur cette page sont assez simples (afficher/masquer les menus, ouvrir un écran modal, gérer les permaliens).

Puisque je n'utilisais pas de framework/bibliothèque, je pouvais éviter d'ajouter Webpack et Babel. Pas besoin de creuser dans les présélections et les chargeurs.

P.S. Vous pouvez argumenter que j'aurais pu choisir create-react-app ou Next.js et résoudre tous ces problèmes, mais non.

## Pas de travail CSS

J'adore écrire du CSS, surtout quand je peux utiliser SASS, mais j'ai décidé de ne pas écrire de CSS ici. J'avais quelques bonnes raisons d'éviter de le faire :

- Je n'avais pas de designs en tête, et malgré le fait que je pourrais faire quelque chose de décent, je ne voulais pas y mettre du temps et de l'énergie
- Je voulais utiliser [Tailwind CSS](https://tailwindcss.com)

Si vous n'avez jamais entendu parler de Tailwind CSS, ne pensez pas simplement, « C'est juste une alternative à Bootstrap. » Voici une bonne explication courte de leur site web :

> La plupart des frameworks CSS en font trop. 
> … 
> Au lieu de composants prédéfinis et opinionnés, Tailwind fournit des classes utilitaires de bas niveau qui vous permettent de créer des designs complètement personnalisés sans jamais quitter votre HTML.

C'est assez vrai. Une recherche rapide vous donne de nombreuses applications web « reconstruites » avec Tailwind CSS :

- [Whatsapp](https://tailwindcomponents.com/component/whatsapp-web-clone)
- [Telegram](https://tailwindcomponents.com/component/telegram-desktop-using-tailwindcss)
- [Facebook](https://tailwindcomponents.com/component/facebook-clone)
- [Reddit](https://tailwindcomponents.com/component/reddit-clone)
- [Youtube](https://tailwindcomponents.com/component/youtube-clone)
- [Slack](https://tailwindcomponents.com/component/slack-clone-1)
- [Coinbase](https://tailwindcomponents.com/component/coinbase-clone)
- [Github](https://tailwindcomponents.com/component/github-profile-clone)
- [Trello](https://tailwindcomponents.com/component/trello-panel-clone)
- [Twitter](https://codepen.io/drehimself/full/vpeVMx/)
- [Netlify](https://www.youtube.com/watch?v=_JhTaENzfZQ)

## Créer un site web avec une bonne accessibilité

Le mois dernier, j'ai commencé à suivre des cours d'accessibilité à [Deque University](https://dequeuniversity.com/curriculum/packages/full). Leur contenu est excellent et cela m'a rappelé que **le HTML est accessible par défaut**. En utilisant une structure HTML sémantique et en testant des choses de base comme la navigation au clavier et le contraste des couleurs, vous éliminez plusieurs barrières qui éloignent les personnes handicapées de votre contenu. 

Je ne suis pas un expert en accessibilité, mais voici quelques choses liées à l'accessibilité sur lesquelles j'ai travaillé pour ce site web :

- Désactiver les feuilles de style : En désactivant les feuilles de style, vous pouvez vous assurer que votre contenu suit une logique/structure.
- VoiceOver : VoiceOver est inclus dans macOS et iOS. Il est [très simple à utiliser](https://webaim.org/articles/voiceover/), et en expérimentant avec, vous pouvez mieux comprendre comment les gens utilisent cette fonctionnalité. 
- Modales : Les modales peuvent être problématiques. J'ai décidé de suivre l'approche de [Ire Aderinokun](https://bitsofco.de/accessible-modal-dialog/).
- [axe](https://chrome.google.com/webstore/detail/axe-web-accessibility-tes/lhdoppojpmngadmnindnejefpokejbdd) : L'extension est un vérificateur d'accessibilité pour les règles d'accessibilité WCAG 2 et Section 508. 

Ce n'est pas parfait -- il y a quelques choses sur lesquelles je n'ai pas travaillé pour mon site, comme l'ajout d'un lien de saut vers le contenu principal. Si vous êtes curieux, [voici la Pull Request avec toutes les modifications](https://github.com/leonardofaria/collection/pull/1).

## Créer un site web qui fonctionne sur les anciens navigateurs

Je n'ai pas pu atteindre cet objectif puisque je n'avais aucun contrôle sur les scripts et les styles. Cependant, cela ne semble pas impossible. Quelques choses que j'ai remarquées :

- [Expedite](https://github.com/SteinHQ/Expedite) (client Stein) utilise [fetch](https://github.com/SteinHQ/Expedite/blob/master/index.js#L51-L54), qui n'a été ajouté qu'à partir de Safari 10. La requête vers leur serveur pourrait probablement être remplacée par un XMLHttpRequest.
- Tailwind utilise Flexbox dans de nombreux éléments. Safari n'a commencé à supporter Flexbox qu'à partir d'iOS 7. Peut-être pourrais-je écrire quelques propriétés pour leurs éléments existants pour obtenir un look décent.
- Les certificats SSL peuvent poser problème pour les anciens navigateurs.

## Conclusions

Créer ce site web a été super amusant. Avoir ce genre de projet personnel m'a donné une bonne raison de travailler avec des technologies que je n'utilise pas dans mon travail. Peut-être qu'à l'avenir, Stein et/ou TailwindCSS seront utiles pour prototyper une fonctionnalité ou construire un projet de hackathon. 

Le fait que j'ai ajouté des « contraintes » à mon projet m'a fait penser hors des sentiers battus. Même si je n'ai pas atteint tous mes objectifs, cela m'a aidé à comprendre de plus en plus comment toutes les pièces sont connectées.

Je recommande totalement de faire quelque chose comme cela pour vous donner une chance de jouer avec différentes technologies. Cela n'a pas besoin d'être une collection Apple -- vous pouvez créer un site pour lister vos livres préférés ou les meilleures randonnées que vous avez faites. Dans ce cas, le voyage compte plus que le but. 

Par curiosité, j'ai suivi mon temps en utilisant [Clockify](https://clockify.me) et entre le codage, la création des données, les tests et la rédaction de cet article, j'ai travaillé 13 heures sur ce projet. 

_Aussi publié sur [mon blog](http://bit.ly/collection-post). Suivez-moi sur [Twitter](https://twitter.com/leozera)_