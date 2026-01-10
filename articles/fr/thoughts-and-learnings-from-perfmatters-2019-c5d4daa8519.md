---
title: 'Ce que j''ai appris en assistant à la conférence #PerfMatters'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-05T21:38:11.000Z'
originalURL: https://freecodecamp.org/news/thoughts-and-learnings-from-perfmatters-2019-c5d4daa8519
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5ECCYqZOEG5Tui_YIWybRw.png
tags:
- name: conference
  slug: conference
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 'Ce que j''ai appris en assistant à la conférence #PerfMatters'
seo_desc: 'By Stacey Tay

  Notes from a front-end web performance conference

  This week I had the privilege of attending #PerfMatters, a conference focused on
  front-end web performance. I’ve never been to a conference before, but I was thrilled
  to be attending bec...'
---

Par Stacey Tay

#### Notes d'une conférence sur la performance web front-end

Cette semaine, j'ai eu le privilège d'assister à [#PerfMatters](https://perfmattersconf.com), une conférence axée sur la performance web front-end. Je n'avais jamais assisté à une conférence auparavant, mais j'étais ravie d'y participer car elle promettait une [liste impressionnante d'intervenants](https://perfmattersconf.com/2019) et de [sujets](https://perfmattersconf.com/schedule/).

J'ai commencé à [me plonger dans la performance web](https://medium.com/carousell-insider/how-we-made-carousells-mobile-web-experience-3x-faster-bbb3be93e006) il y a un peu plus d'un an, et j'ai donc pensé que ce serait une excellente occasion d'approfondir mes connaissances et de rencontrer d'autres personnes de la communauté.

Cet article se compose de trois parties :

(1) mon expérience de la conférence,

(2) certaines des choses que j'ai apprises à la conférence, et

(3) mes réflexions finales.

### Réflexions sur l'expérience de la conférence

#### Tout le monde est si amical et accessible

Je suis venue seule et c'était une expérience assez intimidante, car je suis généralement une personne timide et il me faut un certain temps pour m'ouvrir. Mais je me suis fixé une règle : ne pas rester seule pendant le déjeuner et essayer de parler à au moins 2 personnes chaque jour. Je suis contente de l'avoir fait car toutes les personnes que j'ai rencontrées étaient gentilles et agréables à discuter.

J'ai fini par rencontrer beaucoup de gens, discutant de sujets allant du [modèle PRPL](https://developers.google.com/web/fundamentals/performance/prpl-pattern/), en passant par l'expérimentation avec les [Cloudflare workers](https://blog.cloudflare.com/introducing-cloudflare-workers/) pour mieux servir les utilisateurs en Australie (à partir de serveurs aux États-Unis), la prévalence croissante de la programmation fonctionnelle dans le développement web front-end, et comment commencer le snowboard (sans rapport avec la performance, au cas où vous vous poseriez la question).

#### Les conférences étaient absolument incroyables

Tous les intervenants avaient quelque chose à dire sur la performance web sous une forme ou une autre, et il était évident qu'ils avaient mis beaucoup d'efforts dans leurs présentations. La [conférence](https://perfmattersconf.com/talks/#jenna) de [Jenna Zeigen](https://mobile.twitter.com/zeigenvector) couvrait une longue liste d'astuces de performance et chacun de ses points était accompagné d'une lyric de chanson, ce qui était à la fois divertissant et informatif. Elle m'a dit qu'il lui fallait environ 15 minutes par chanson et qu'il y en avait plus de 30 ?

> Les vidéos des conférences devraient être annoncées prochainement sur [@perfmattersconf](https://mobile.twitter.com/perfmattersconf), mais un certain nombre de diapositives ont déjà été publiées avec [#perfmattersconf](https://mobile.twitter.com/hashtag/perfmattersconf).

#### Les conférences couvrent les nombreux aspects du travail sur la performance web

Améliorer la performance d'une page web ne se limite pas à un audit ponctuel, à la correction des problèmes qui rendent cette page lente, puis à passer à autre chose. Cela nécessite **un effort concerté de toutes les parties prenantes**—commercial, design, ingénierie, marketing, produit—au sein d'une organisation pour obtenir et rester rapide.

Les conférences ne portaient pas toutes sur la manière d'améliorer les [_TTI_](http://Improving%20a%20web%20page%E2%80%99s%20performance%20isn%E2%80%99t%20just%20a%20one-off%20audit,%20fixing%20the%20problems%20that%20makes%20that%20page%20slow,%20and%20moving%20on.%20It%20takes%20a%20concerted%20effort%20from%20all%20stakeholders%E2%80%94business,%20design,%20engineering,%20marketing,%20product%E2%80%94in%20an%20organisation%20to%20get%20and%20stay%20fast.)s ou les temps de chargement, qui sont importants. Mais elles couvraient également les autres aspects importants de **rendre le web accessible et utilisable pour le plus grand nombre de personnes possible**. De [la manière dont les gens perçoivent la performance](https://mobile.twitter.com/GemmaPetrie/status/1113508695428612097) à [l'instauration d'une culture de la performance](https://perfmatters.alfre.do), et de [**comment le privilège définit la performance**](https://mobile.twitter.com/fox/status/1113675170374475776?s=20) à [l'intersection de la performance et de l'accessibilité](https://noti.st/ericwbailey/Yfyaxa).

![Image](https://cdn-media-1.freecodecamp.org/images/1*5ECCYqZOEG5Tui_YIWybRw.png)
_F497FE0F Des cadeaux réfléchis de la conférence F1F7FE0F_

### Une liste non exhaustive d'astuces et de conseils de performance appris

Certains, sinon tous, de ces conseils peuvent être des connaissances courantes, mais beaucoup étaient nouveaux pour moi.

#### Culture de la performance

* [**Donnez aux développeurs les outils**](https://perfmattersconf.com/talks/#greg) pour permettre une meilleure performance. De plus, [intégrez la performance dans le processus de développement](https://perfmatters.alfre.do/#/27).
* **Comparez votre site avec ceux de vos concurrents** pour obtenir l'adhésion de la direction sur la performance. Utilisez la [comparaison vidéo côte à côte de WebPagetest](https://www.webpagetest.org/video/) de votre page web par rapport au parcours de chargement d'un concurrent pour faire passer votre point de vue de manière concise.
* **Mesurez les gains de revenus annuels potentiels** liés à l'augmentation de la vitesse du site avec [l'outil Test My Site de Google](https://www.thinkwithgoogle.com/feature/testmysite).

#### Performance sur le Web

* [**La latence a un impact disproportionné sur la bande passante**](http://www.stuartcheshire.org/rants/latency.html) sur les requêtes réseau.
* [**Les animations SVG**](https://css-tricks.com/book-release-svg-animations/) **sont idéales pour animer les chargeurs** en raison de leur taille (relativement) plus petite.
* [**Compressez votre page en 14KB** si possible, pour éviter plusieurs allers-retours en raison du démarrage lent de TCP](https://calendar.perfplanet.com/2018/tcp-slow-start/).
* **Tous les CDN ne font pas [la priorisation HTTP/2 comme prévu](https://github.com/andydavies/http2-prioritization-issues).**
* **Si vous devez utiliser des polices web**, [Zach Leatherman](https://mobile.twitter.com/zachleat) a écrit un [guide complet sur la manière de les charger correctement](https://www.zachleat.com/web/comprehensive-webfonts/).
* **La performance perçue est influencée** par la **_durée_** (durée réelle qu'un processus prend, appelée « performance »), la **_réactivité_**, la **_fluidité_** (smoothness perçue d'un processus) et la **_tolérance_** (combien de temps l'utilisateur s'attend à ce qu'un processus prenne). [Diapositives](https://docs.google.com/presentation/d/1mMgpxtnyqBJsyhY5jOmh1DF0eqOPEijCH23ef9uya3U/edit) de la conférence de [Gemma Petrie](https://gemmapetrie.com) et [Heather McGaw](https://mobile.twitter.com/HeatherMcGaw) sur _Mesurer la performance perçue pour prioriser le travail produit_.

#### Quelques outils pratiques

* **L'outil de couverture de code de Chrome** est utile pour déterminer où et quand diviser le code. Interagissez un peu avec la page pour voir comment les chiffres changent, et selon [Tim Kaldec](https://timkadlec.com), environ 45 % de code inutilisé est normal et il y aura des gains marginaux décroissants à optimiser au-delà de cela.
* **La fonctionnalité de remplacement des ressources réseau de Chrome** permet aux développeurs de retourner un fichier enregistré localement, ce qui est utile pour déboguer quelque chose à la volée.
* [**Feuille de calcul Google Docs pour effectuer des audits WebPagetest en masse**](https://calendar.perfplanet.com/2014/driving-webpagetest-from-a-google-docs-spreadsheet/).
* [**Explorateur AST JavaScript en ligne**](https://astexplorer.net) (bon, celui-ci n'est pas exactement lié à la performance web, mais je l'ai découvert pendant la conférence et je ne peux pas m'arrêter de jouer avec).
* [**Request Map**](http://requestmap.webperf.tools/render/190405_F1_ab827a1745d3fb3eac56185132ebb952) crée un graphe de réseau à partir d'une page web et est utile pour visualiser les requêtes tierces.

### Réflexions finales

Si une chose est ressortie de la conférence, c'est que pour être bon en performance web, il est crucial de comprendre [comment](https://www.slideshare.net/KatrinaSylorMiller/happy-browser-happy-user-perfmatters-conference-2019) [le navigateur](https://jenna.is/slides/at-perfmatters.pdf) [_fonctionne_](https://github.com/ksylor/happy-browser-happy-user) (des choses comme comment le [rendering](https://developers.google.com/web/fundamentals/performance/critical-rendering-path/render-tree-construction) se produit et le [chemin de rendu critique](https://developers.google.com/web/fundamentals/performance/critical-rendering-path/)). Mais, **la performance ne s'arrête pas aux gains techniques**.

> Obtenir l'adhésion de toutes les parties prenantes, pas seulement de l'ingénierie, est crucial pour améliorer et maintenir la performance car la performance web va au-delà du chargement d'une page aussi rapidement que possible.

Il y a aussi la **performance perçue** à considérer, puis déterminer si des améliorations supplémentaires de la performance créent **des améliorations significatives supplémentaires pour l'entreprise ou les utilisateurs**. Il est important de garder à l'esprit que **la performance n'est qu'une partie de l'expérience utilisateur**.

Je n'ai pas pris beaucoup de photos pendant la conférence (note à moi-même pour en prendre davantage la prochaine fois), mais j'ai réussi à capturer celle-ci.

![Image](https://cdn-media-1.freecodecamp.org/images/1*C7ySQkNv1gOAYOf-UOS9_w.jpeg)
_F31F Diapositive de la [conférence](https://perfmattersconf.com/talks/#addy" rel="noopener" target="_blank" title=") d'Addy Osmani sur Le Coût de JavaScript ?_

Si vous êtes intéressé par la performance web ou simplement par le développement web en général, c'est une conférence incroyable à [découvrir](https://mobile.twitter.com/perfmattersconf) et elle est prévue pour se tenir également l'année prochaine ! Il y a aussi un [programme de bourses](https://perfmattersconf.com/diversity/) pour ceux qui ne peuvent pas assister sans aide financière. Au plaisir de vous y voir l'année prochaine !

_Merci à [Hui Yi](https://www.freecodecamp.org/news/thoughts-and-learnings-from-perfmatters-2019-c5d4daa8519/undefined), [Jingwen Chen](https://www.freecodecamp.org/news/thoughts-and-learnings-from-perfmatters-2019-c5d4daa8519/undefined), et [Yao Hui Chua](https://www.freecodecamp.org/news/thoughts-and-learnings-from-perfmatters-2019-c5d4daa8519/undefined) pour avoir lu une version précédente et partagé leurs commentaires._