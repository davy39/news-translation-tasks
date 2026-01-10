---
title: Comment lancer un projet secondaire en 10 jours
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-08T13:50:30.000Z'
originalURL: https://freecodecamp.org/news/launching-a-side-project-in-10-days-615df3b0e808
coverImage: https://cdn-media-1.freecodecamp.org/images/1*f56dIm5pjl0DLSu9996-tA.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: Product Design
  slug: product-design
- name: React
  slug: react
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment lancer un projet secondaire en 10 jours
seo_desc: 'By Kyle Gill

  Tools for conquering the process from Idea -> Design -> Development -> Deployment


  Like many people, I have no shortage of ideas for apps that don’t genuinely need
  to exist. I tend to hold onto those ideas waiting for some imaginary occa...'
---

Par Kyle Gill

#### Outils pour maîtriser le processus de l'Idée -> Design -> Développement -> Déploiement

![Image](https://cdn-media-1.freecodecamp.org/images/1*f56dIm5pjl0DLSu9996-tA.png)

Comme beaucoup de gens, je n'ai pas de pénurie d'idées pour des applications qui n'ont pas vraiment besoin d'exister. J'ai tendance à m'accrocher à ces idées en attendant une occasion imaginaire où le temps libre est abondant et où je peux toutes les construire sans penser au revenu ou aux dépenses. Pour moi, souvent, l'obstacle à la réalisation d'un projet secondaire n'est pas de savoir **comment** faire quelque chose, mais de trouver la motivation et le temps de le concrétiser.

C'est pourquoi je me suis fixé un objectif : lancer un projet secondaire en 10 jours.

Cet article ne parle pas des avantages de la construction avec une nouvelle technologie que je ne connaissais pas, ni des 7 choses que j'ai apprises en le faisant. Il s'agit plutôt de mon processus de création rapide d'une application web, en évitant que des idées sans rapport ne brouillent ma concentration, et de ma boîte à outils pour y parvenir. Le résultat final était [Card Surge](https://card.surge.sh/).

### Idée (1 jour)

Je passe beaucoup de temps à concevoir et à construire des sites, ce qui signifie que je passe aussi beaucoup de temps à examiner des sites bien conçus de marques populaires. J'ouvre presque inévitablement l'inspecteur Chrome pour examiner comment les styles sont appliqués ou les éléments sont disposés, car je veux voir ce qui peut quantifier ces designs comme **bons**.

Ensuite, je me retrouve à construire mon propre site et à me référer à ces exemples. Je répète le processus d'ouverture de l'inspecteur, de modification de leurs styles, d'ajout de mes propres styles, de ne pas obtenir ce que je veux, de positionner tout en `absolute` ce qui ne fonctionne toujours pas, et finalement de trouver quelque chose de raisonnable.

Ayant trouvé d'autres outils de design en ligne comme [Coolors](https://coolors.co/), ou [Hero Patterns](https://www.heropatterns.com/) qui m'ont été utiles, j'ai pensé que je pourrais créer quelque chose de similaire pour répondre à mes propres intérêts. Et c'est ainsi que j'ai entrepris de construire un moyen plus rapide d'itérer sur l'interface utilisateur des cartes.

J'ai fouillé dans les outils existants et j'ai trouvé qu'ils avaient l'air un peu moyens. Ils ne facilitaient pas la création d'une ombre décente (parce que des curseurs étaient souvent utilisés pour des entrées qui devaient rarement être ajustées plus qu'un ou deux nombres), et il n'y avait aucune référence à des designs qui fonctionnaient réellement. J'ai eu l'impression que c'était une validation suffisante pour mon idée.

### Design (2 jours)

On voit des cartes dans les mises en page partout : pages de tarification, pages de produits, listes, et ainsi de suite. Elles sont un excellent moyen de regrouper des informations pertinentes et peuvent également se démarquer sur la page avec une ombre portée ou un contour. Vous pouvez vous référer à certains de ces exemples pour voir comment elles peuvent varier :

![Image](https://cdn-media-1.freecodecamp.org/images/1*dBzNYvbplK5YexmbLoGIpQ.png)
_[https://crisp.chat/en/pricing](https://crisp.chat/en/pricing" rel="noopener" target="_blank" title=")_

![Image](https://cdn-media-1.freecodecamp.org/images/1*c4GkBQGdGT1H5DXO5Td3Pg.png)
_[https://flat.io/pricing](https://flat.io/pricing" rel="noopener" target="_blank" title=")_

![Image](https://cdn-media-1.freecodecamp.org/images/1*efyloQvuzODqy7Agc-9D7Q.png)
_[https://www.intercom.com](https://www.intercom.com/?ref=pages.xyz" rel="noopener" target="_blank" title=")_

![Image](https://cdn-media-1.freecodecamp.org/images/1*PsMDL8A6I4jpINJU2lPYIg.png)
_[https://www.timekit.io](https://www.timekit.io/" rel="noopener" target="_blank" title=")_

Elles peuvent avoir des ombres portées, des bordures sur certains côtés et pas sur d'autres, des styles de survol, peuvent varier en couleur, et vous pouvez même appliquer plusieurs ombres à un seul élément pour créer un dégradé plus exponentiel dans l'ombre portée.

Je voulais que mon outil aide les designers et les développeurs à créer des cartes qui ressemblent à celles-ci. J'ai pensé qu'il devait être esthétiquement plaisant et utiliser des cartes lui-même pour aider à démontrer ce qui peut être fait pour les faire briller 💡

J'ai commencé à façonner mes idées dans [Figma](https://www.figma.com/), je me suis empêché de me concentrer excessivement sur des pièces sans importance que je pourrais facilement faire plus tard (comme ajouter des logos pour les marques, ajouter des icônes sociales, etc.) et j'ai fini par obtenir ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*WDr4WzVZNUjdCUkcHrLY6g.png)
_[https://www.figma.com/file/Cav6jxGjiOSOJLaZrnWUtiG1/Cards](https://www.figma.com/file/Cav6jxGjiOSOJLaZrnWUtiG1/Cards" rel="noopener" target="_blank" title=")_

Je savais que je voulais plusieurs choses dans mon produit final :

1. Un éditeur pour ajuster les styles qui mettra à jour l'UI en direct
2. Un curseur qui pourrait faire défiler des exemples frais et agréables
3. Un endroit pour exporter le code en le copiant dans le presse-papiers

Ces 3 éléments essentiels ont fait le design, ainsi que d'autres choses comme le contenu en dessous et comment exactement je formaterais les pieds de page et les en-têtes que j'avais laissés inachevés. Ce n'était pas entièrement élaboré, car je voulais commencer à construire avant de me laisser trop emporter en changeant inutilement des choses qui étaient probablement bien telles quelles.

### Développement (7 jours)

J'ai pensé que la partie la plus chronophage serait d'écrire le code de l'application, et je n'avais pas tort. Il semble toujours y avoir des problèmes à craindre qui ne deviennent un problème que lorsque vous êtes dans le code. Des choses surgissent comme une bonne UX avec les éléments de formulaire, des décisions de design qui n'ont pas été réfléchies dans les designs initiaux, des fonctionnalités non supportées par les bibliothèques que vous prévoyez d'utiliser, ou Twitter qui exige votre attention au détriment de votre projet. 🤦‍♂️

J'ai amorcé le processus de développement avec [Gatsby](https://www.gatsbyjs.org/) parce que :

* Je pouvais construire l'interface en utilisant React
* Convertir le site en une PWA serait aussi simple que d'ajouter quelques lignes à un fichier de configuration (voir [ce](https://twitter.com/gill_kyle/status/1019949271309725696) tweet)
* L'hébergement serait un jeu d'enfant avec juste des fichiers statiques à déployer
* Je pourrais sauter beaucoup de la plaque de chaudière initiale et commencer à construire les pièces amusantes tout de suite
* Gatsby est juste trop cool ✨

J'ai commencé à partir du [gatsby-default-starter](https://github.com/gatsbyjs/gatsby-starter-default) et j'ai construit une grande partie de la fonctionnalité sans problème. J'ai implémenté des bibliothèques tierces comme [react-color](https://github.com/casesandberg/react-color) et [react-slick](https://github.com/akiran/react-slick) pour éliminer le besoin de construire des composants de curseur et de couleur compliqués.

Pendant ce temps, j'ai décidé comment disposer le contenu sur d'autres parties de la page que mes designs n'avaient pas incluses, et j'ai construit ces parties aussi. J'ai profité des nouvelles tendances comme CSS Grid qui ont rendu les mises en page réactives beaucoup plus faciles.

À un moment donné, j'ai réalisé que le diviseur diagonal que j'avais inclus dans la mise en page de mon application pouvait être abstrait et transformé en un package npm que d'autres personnes pourraient utiliser. Après avoir construit un composant simple et publié le package sur npm, j'ai réalisé que je m'étais complètement écarté de mes objectifs initiaux pour terminer mon projet. Cela prendrait trop de temps, alors j'ai abandonné cette aventure (après l'avoir ajoutée à ma liste susmentionnée d'applications et de projets inutiles à terminer à une date ultérieure, bien sûr).

J'ai utilisé un projet GitHub [project](https://github.com/gillkyle/card-surge/projects/1) pour suivre certaines des petites choses que je voulais faire et qui étaient de moindre priorité, et j'ai finalement pris des mesures pour ajouter des [plugins Gatsby](https://www.gatsbyjs.org/plugins/) pour Google Analytics, certaines métadonnées, et j'ai inclus des icônes pour les navigateurs, les appareils mobiles et les configurations du manifeste PWA.

### Déploiement (~45 minutes)

**...et lancement !**

Une fois que j'ai atteint un point où mon application fonctionnait et agissait comme je l'avais conçu et imaginé, j'ai pensé qu'elle n'était toujours pas assez bonne. J'ai imaginé un portail où les utilisateurs pourraient s'authentifier, sauvegarder et partager les styles qu'ils avaient créés, puis utiliser l'application comme référence pour y revenir. J'en suis venu à la conclusion que ce n'était pas mon intention initiale, et j'ai décidé de simplement finaliser ce que j'avais réellement fait. Je pourrais construire par-dessus si j'avais la motivation plus tard ou si je trouvais que c'était quelque chose que les gens utiliseraient réellement.

Passer outre ces inhibitions d'incertitude tout au long du processus a été facile puisque j'avais un objectif en vue.

J'ai finalement réalisé que je pouvais regarder mon travail acharné et apprécier une chose vraiment cool que j'avais faite :

![Image](https://cdn-media-1.freecodecamp.org/images/1*I4pgLix-CdtIO2bvqxKuxQ.png)
_Le produit fini dans son habitat naturel_

Étant plus ou moins complet, le déploiement était la prochaine étape. Le déploiement a été un processus vraiment simple. Je ne voulais pas vraiment dépenser de l'argent dans un domaine pour un projet secondaire qui pourrait ne plus m'intéresser dans un an ou deux. J'ai donc profité de la façon dont [Surge](http://surge.sh/) héberge vos sites dans le niveau gratuit et je l'ai nommé card surge, donc tout ce que je devais faire était de prendre le sous-domaine card et j'avais un domaine de marque gratuit à card.surge.sh 🎉. J'ai exécuté `gatsby build` puis `surge`, et mon code était en ligne et distribué sur un CDN avec SSL automatique.

J'aime aussi beaucoup [Netlify](https://www.netlify.com/) pour ne pas l'utiliser, alors j'ai pointé mon dépôt GitHub vers un projet sur Netlify pour construire automatiquement les pull requests ou les commits vers Master ([ce qui](https://github.com/gillkyle/card-surge/pull/1) s'est avéré utile juste quelques heures après le lancement lorsque la première pull request est arrivée).

Sans besoin de backend, mon site était en ligne et je n'avais pas dépensé un centime.

J'ai pris quelques captures d'écran et des enregistrements en utilisant [Kap](https://getkap.co/), j'ai écrit une description et j'ai posté Card Surge sur [Product Hunt](https://www.producthunt.com/posts/card-surge).

### Rétrospective

Travailler vite et se diriger vers une date de fin (que j'avais en vue sur le calendrier) était vraiment gratifiant. J'ai dû simplifier les problèmes à ce qui comptait et ne m'attaquer qu'aux préoccupations qui interféraient réellement avec la fin et le lancement à ma date limite.

Si je trouve un autre projet que je pense réalistement pouvoir terminer en quelques semaines, je ferai définitivement un autre sprint comme celui-ci.

Surmontez toutes les réserves que vous avez pour finaliser ce projet secondaire que vous attendez de terminer — vous ne le regretterez pas !

### Merci d'avoir lu !

Si vous avez des questions sur la façon dont j'ai fait quelque chose, pourquoi je l'ai fait, ou ce que j'ai horriblement mal fait, je suis heureux de vous entendre ici dans les commentaires, sur Twitter, ou par email.

Si vous avez trouvé ce que vous avez lu intéressant ou utile, n'hésitez pas à laisser un ou deux applaudissements, à vous abonner pour les mises à jour futures, ou à retweeter/partager ce tweet : 👏