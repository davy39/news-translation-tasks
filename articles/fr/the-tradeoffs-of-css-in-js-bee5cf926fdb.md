---
title: Les compromis du CSS-in-JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-05T13:40:18.000Z'
originalURL: https://freecodecamp.org/news/the-tradeoffs-of-css-in-js-bee5cf926fdb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Y-OFV7iQafRToGdyhAf8yQ.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Les compromis du CSS-in-JS
seo_desc: 'By Oleg Isonen

  Recently I wrote a higher level overview of CSS-in-JS, mostly talking about the
  problems this approach is trying to solve. Library authors rarely invest time into
  describing the tradeoffs of their solution. Sometimes it’s because they ...'
---

Par Oleg Isonen

Récemment, j'ai écrit un aperçu de plus haut niveau [du CSS-in-JS](https://medium.com/@oleg008/what-is-actually-css-in-js-f2f529a2757), parlant principalement des problèmes que cette approche tente de résoudre. Les auteurs de bibliothèques investissent rarement du temps pour décrire les compromis de leur solution. Parfois, c'est parce qu'ils sont trop partial, et parfois ils ne savent tout simplement pas comment les utilisateurs appliquent l'outil. Donc, voici une tentative de décrire les compromis que j'ai observés jusqu'à présent. Je pense qu'il est important de mentionner que je suis l'auteur de [JSS](https://cssinjs.org/), donc je devrais être considéré comme partial.

### Impact social

Il existe une catégorie de personnes qui travaillent sur la plateforme web et ne connaissent pas JavaScript. Ces personnes sont payées pour écrire du HTML et du CSS. Le CSS-in-JS a eu un impact énorme sur le flux de travail des développeurs. Un changement véritablement transformateur ne peut jamais être fait sans laisser certaines personnes derrière. Je ne sais pas si le CSS-in-JS doit être la seule façon, mais l'adoption massive est un signe clair des problèmes liés à l'utilisation du CSS dans les applications modernes.

Une grande partie du problème est notre incapacité à communiquer avec précision les cas d'utilisation où le CSS-in-JS excelle et comment l'utiliser correctement pour une tâche. De nombreux enthousiastes du CSS-in-JS ont réussi à promouvoir la technologie, mais peu de critiques ont parlé des compromis de manière constructive, sans prendre des raccourcis faciles envers les outils. En conséquence, nous avons laissé de nombreux compromis cachés et n'avons pas fait un effort fort pour fournir des explications et des solutions de contournement.

**Le CSS-in-JS est une tentative de rendre les cas d'utilisation complexes plus faciles à gérer, alors ne le poussez pas là où il n'est pas nécessaire !**

### Coût d'exécution

Lorsque le CSS est généré à partir de JavaScript à l'exécution, dans le navigateur, il y a un surcoût inhérent. Le surcoût d'exécution varie d'une bibliothèque à l'autre. [Ceci](http://necolas.github.io/react-native-web/benchmarks/) est un bon benchmark générique, mais assurez-vous de faire vos propres tests. Les différences majeures à l'exécution apparaissent en fonction du besoin d'avoir une analyse complète du CSS des chaînes de modèles, du nombre d'optimisations, des détails de mise en œuvre des styles dynamiques, de l'algorithme de hachage et du coût des intégrations de framework.

Outre le potentiel surcoût d'exécution, vous devez considérer 4 stratégies de bundling différentes, car certaines bibliothèques CSS-in-JS supportent plusieurs stratégies et c'est à l'utilisateur de les appliquer.

### Stratégie 1 : Génération uniquement à l'exécution

La génération de CSS à l'exécution est une technique qui génère une chaîne CSS en JavaScript puis injecte cette chaîne en utilisant une balise de style dans le document. Cette technique produit une feuille de style, PAS des styles en ligne.

Le compromis de la génération à l'exécution est l'incapacité à fournir un contenu stylisé dès le début, lorsque le document commence à se charger. Cette approche convient généralement aux applications sans contenu qui peut être utile immédiatement. Habituellement, de telles applications nécessitent des interactions utilisateur avant de devenir vraiment utiles pour un utilisateur. Souvent, ces applications travaillent avec un contenu si dynamique qu'il devient obsolète dès que vous le chargez, donc vous devez établir un pipeline de mise à jour tôt, par exemple, Twitter. De plus, lorsqu'un utilisateur est connecté, il n'est pas nécessaire de fournir du HTML pour le SEO.

Si l'interaction nécessite JavaScript, le bundle doit être chargé avant que l'application soit prête. Par exemple, vous pouvez afficher le contenu d'un canal par défaut lors du chargement de Slack dans le document, mais il est probable que l'utilisateur veuille changer de canal juste après. Donc, si vous avez chargé le contenu initial pour le jeter immédiatement.

La performance perçue de telles applications peut être améliorée avec des placeholders et d'autres astuces pour donner à l'application une sensation plus instantanée qu'elle ne l'est réellement. De telles applications sont généralement gourmandes en données de toute façon, donc elles ne seront pas utiles aussi rapidement qu'un article.

### Stratégie 2 : Génération à l'exécution avec CSS critique

Le CSS critique est la quantité minimale de CSS nécessaire pour styliser la page dans son état initial. Il est rendu en utilisant une balise de style dans l'en-tête du document. Cette technique est largement utilisée avec et sans CSS-in-JS. Dans les deux cas, vous risquez de charger deux fois les règles CSS, une fois dans le cadre du CSS critique et une fois dans le cadre du bundle JavaScript ou CSS. La taille du CSS critique peut être assez grande en fonction de la quantité de contenu. Habituellement, le document ne sera pas mis en cache.

Sans CSS critique, une application à page unique statique et gourmande en contenu avec CSS-in-JS à l'exécution devra afficher des placeholders au lieu du contenu. Cela est mauvais car cela aurait pu être utile à un utilisateur beaucoup plus tôt, améliorant l'accessibilité sur les appareils bas de gamme et pour les connexions à faible bande passante.

Avec le CSS critique, la génération de CSS à l'exécution peut être effectuée à un stade ultérieur, sans bloquer l'interface utilisateur dans la phase initiale. Soyez averti cependant, sur les appareils mobiles bas de gamme, qui ont environ 5 ans ou plus, la génération de CSS à partir de JavaScript peut avoir un impact négatif sur les performances. Cela dépend fortement de la quantité de CSS générée et de la bibliothèque utilisée, donc cela ne peut pas être généralisé.

Le compromis de cette stratégie est le coût de l'extraction du CSS critique et le coût de la génération de CSS à l'exécution.

### Stratégie 3 : Extraction uniquement au moment de la construction

Cette stratégie est celle par défaut sur le web sans CSS-in-JS. Certaines bibliothèques CSS-in-JS vous permettent d'extraire le CSS statique au moment de la construction. Dans ce cas, aucun surcoût d'exécution n'est impliqué, le CSS est rendu sur la page en utilisant une balise de lien. Le coût de la génération de CSS est payé une fois à l'avance.

Il y a 2 compromis majeurs ici :

1. Vous ne pouvez pas utiliser certaines des API dynamiques que CSS-in-JS offre à l'exécution, car vous n'avez pas accès à l'état. Souvent, vous ne pouvez toujours pas utiliser les propriétés personnalisées CSS, car elles ne sont pas supportées dans tous les navigateurs et ne peuvent pas être polyfillées au moment de la construction par nature. Dans ce cas, vous devrez faire des contournements pour le théming dynamique et le stylage basé sur l'état.
2. Sans CSS critique et avec un cache vide, vous bloquerez le premier rendu, jusqu'à ce que votre bundle CSS soit chargé. Un élément de lien dans l'en-tête du document bloque le rendu du HTML.
3. Spécificité non déterministe avec la division de bundle basée sur les pages dans les applications à page unique.

### Stratégie 4 : Extraction au moment de la construction avec CSS critique

Cette stratégie n'est pas non plus unique au CSS-in-JS. L'extraction statique complète avec CSS critique offre les meilleures performances lors du travail avec une application plus statique. Cette approche a toujours les compromis mentionnés précédemment d'un CSS statique, sauf que la balise de lien bloquante peut être déplacée vers le bas du document.

**Il existe 4 stratégies principales de rendu CSS. Seules 2 d'entre elles sont spécifiques au CSS-in-JS et aucune ne s'applique à toutes les bibliothèques.**

### Accessibilité

Le CSS-in-JS peut diminuer l'accessibilité lorsqu'il est utilisé de manière incorrecte. Cela se produira lorsqu'un site de contenu largement statique est implémenté sans extraction de CSS critique de sorte que le HTML ne peut pas être peint avant que le bundle JavaScript soit chargé et évalué. Cela peut également se produire lorsqu'un gros fichier CSS est rendu en utilisant une balise de lien bloquante dans l'en-tête du document, ce qui est le problème actuel le plus populaire avec l'intégration traditionnelle et non spécifique au CSS-in-JS.

Les développeurs doivent prendre la responsabilité de l'accessibilité. Il existe encore une idée erronée forte qu'une connexion internet instable est un problème des pays économiquement faibles. Nous avons tendance à oublier que nous avons des problèmes de connectivité chaque jour lorsque nous entrons dans un système de rail souterrain ou un grand bâtiment. Une connexion mobile stable sans fil est un mythe. Il n'est même pas facile d'avoir une connexion WiFi stable, par exemple, un réseau WI-FI 2,4 GHz peut subir des interférences d'un four à micro-ondes !

### Le coût du CSS critique avec le rendu côté serveur

Pour obtenir l'extraction de CSS critique pour CSS-in-JS, nous avons besoin de SSR. SSR est un processus de génération du HTML final pour un état donné d'une application sur le serveur. En fait, cela peut être un processus assez complexe et coûteux. Il nécessite une certaine quantité de cycles CPU sur le serveur pour chaque requête HTTP.

CSS-in-JS utilise généralement le fait qu'il est intégré dans le pipeline de rendu HTML. Il sait quel HTML a été rendu et quel CSS il nécessite afin de pouvoir produire la quantité absolue minimale de celui-ci. Le CSS critique ajoute un surcoût supplémentaire au rendu HTML sur le serveur car ce CSS doit également être compilé en une chaîne CSS finale. Dans certains scénarios, il est difficile ou même impossible de mettre en cache sur le serveur.

### Boîte noire de rendu

Vous devez être conscient de la manière dont une bibliothèque CSS-in-JS que vous utilisez rend votre CSS. Par exemple, les gens ne sont souvent pas conscients de la manière dont Styled Components et Emotion implémentent les styles dynamiques. Les styles dynamiques sont une syntaxe qui permet l'utilisation de fonctions JavaScript à l'intérieur de votre déclaration de styles. Ces fonctions acceptent des props et retournent un bloc CSS.

Afin de garder la spécificité de l'ordre source cohérente, les deux bibliothèques nommées ci-dessus génèrent une nouvelle règle CSS si elle contient une déclaration dynamique et que le composant se met à jour avec de nouveaux props. Pour démontrer ce que je veux dire, j'ai créé [ce sandbox](https://codesandbox.io/s/1rm705jnlq). Dans [JSS](https://cssinjs.org/), nous avons décidé de prendre un compromis différent, qui nous permet de mettre à jour les propriétés dynamiques sans générer de nouvelles règles CSS.

### Courbe d'apprentissage abrupte

Pour les personnes qui sont familières avec CSS, mais nouvelles en JavaScript, la quantité initiale de travail pour se mettre à niveau avec CSS-in-JS peut être assez importante.

Vous n'avez pas besoin d'être un développeur JavaScript professionnel pour écrire du CSS-in-JS, jusqu'au point où une logique complexe est impliquée. Nous ne pouvons pas généraliser la complexité du stylage, car cela dépend vraiment du cas d'utilisation. Dans les cas où CSS-in-JS devient complexe, il est probable que la mise en œuvre avec du CSS vanilla serait encore plus complexe.

Pour le stylage de base CSS-in-JS, il faut savoir comment déclarer des variables, comment utiliser des chaînes de modèles et interpoler des valeurs JavaScript. Si la notation par objet est utilisée, il faut savoir comment travailler avec des objets JavaScript et la syntaxe basée sur les objets spécifique à la bibliothèque. Si le stylage dynamique est impliqué, il faut savoir comment utiliser des fonctions JavaScript et des conditionnelles.

Globalement, il y a une courbe d'apprentissage, nous ne pouvons pas le nier. Cette courbe d'apprentissage n'est généralement pas beaucoup plus grande, cependant, que l'apprentissage de Sass. En fait, j'ai créé ce [cours egghead](https://egghead.io/courses/convert-scss-sass-to-css-in-js) pour démontrer cela.

### Pas d'interopérabilité

La plupart des bibliothèques CSS-in-JS ne sont pas interopérables. Cela signifie que les styles écrits avec une bibliothèque ne peuvent pas être rendus avec une bibliothèque différente. Pratiquement, cela signifie que vous ne pouvez pas basculer facilement toute votre application d'une implémentation à une autre. Cela signifie également que vous ne pouvez pas facilement partager votre UI sur NPM sans apporter votre bibliothèque CSS-in-JS de choix dans le bundle du consommateur, sauf si vous avez une extraction statique au moment de la construction pour votre CSS.

Nous avons commencé à travailler sur le format [ISTF](https://github.com/cssinjs/istf-spec) qui est censé résoudre ce problème, mais malheureusement, nous n'avons pas encore eu le temps de le rendre prêt pour la production.

Je pense que le partage de composants UI réutilisables et agnostiques des frameworks dans le domaine public est encore un problème généralement difficile à résoudre.

### Risques de sécurité

Il est possible d'introduire des fuites de sécurité avec CSS-in-JS. Comme avec toute application côté client, vous devez échapper les entrées utilisateur avant de les rendre, toujours.

[Cet article](https://reactarmory.com/answers/how-can-i-use-css-in-js-securely) vous donnera plus d'informations et quelques exemples de défacement.

### Noms de classe illisibles

Certaines personnes pensent encore qu'il est important que nous gardions des noms de classe significatifs et lisibles sur le web. Actuellement, de nombreuses bibliothèques CSS-in-JS fournissent des noms de classe significatifs basés sur le nom de la déclaration ou le nom du composant en mode développement. Certaines d'entre elles vous permettent même de personnaliser la fonction de génération des noms de classe.

En mode production, cependant, la plupart d'entre elles génèrent des noms plus courts pour une charge utile plus petite. C'est un compromis que l'utilisateur de la bibliothèque doit faire et personnaliser la bibliothèque si nécessaire.

### Conclusion

Les compromis existent, et je n'ai probablement même pas mentionné tous. Mais la plupart d'entre eux ne s'appliquent pas universellement à tous les CSS-in-JS. Ils dépendent de la bibliothèque que vous utilisez et de la manière dont vous l'utilisez.

* Il faudra un article dédié pour expliquer cette phrase. Faites-moi savoir sur Twitter ([@oleg008](https://twitter.com/oleg008)) celui que vous aimeriez lire plus.