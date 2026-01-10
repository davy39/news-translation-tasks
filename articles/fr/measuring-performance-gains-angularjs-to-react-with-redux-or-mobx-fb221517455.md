---
title: Migration d'AngularJS vers React — comment mesurer vos gains de performance
  ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-23T07:14:07.000Z'
originalURL: https://freecodecamp.org/news/measuring-performance-gains-angularjs-to-react-with-redux-or-mobx-fb221517455
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Dbqp6gglYpKlXuzA1sHuaQ.jpeg
tags:
- name: Angular
  slug: angularjs
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Migration d'AngularJS vers React — comment mesurer vos gains de performance
  ?
seo_desc: 'By Gupta Garuda

  Are you looking into migrating a large AngularJS single page application to React?
  If so, you may be wondering what sort of performance gains you are going to get
  with React and how the code will morph (with state management libraries...'
---

Par Gupta Garuda

Vous envisagez de migrer une grande application monopage AngularJS vers React ? Si oui, vous vous demandez peut-être quels gains de performance vous allez obtenir avec React et comment le code va évoluer (avec les bibliothèques de gestion d'état Redux ou Mobx).

Dans cet article, je vais essayer de répondre à certaines de ces questions et vous fournir de nombreuses données que vous pouvez utiliser pour prendre des décisions plus éclairées.

Tout d'abord, je vais passer en revue les profils de performance et de mémoire de divers scénarios d'interface utilisateur implémentés avec AngularJS, React/Redux et React/Mobx. Nous allons comparer les performances de ces frameworks en termes de temps d'exécution des scripts, de frames par seconde et de usedJSHeapSize pour chaque scénario.

J'ai fourni les liens vers les pages de test et le code source afin que vous puissiez essayer ces scénarios et examiner le code pour vous familiariser avec les constructions que React (avec Redux ou Mobx) apporte.

### Configuration du test de performance

Pour évaluer les performances d'AngularJS et de React, j'ai créé une application de référence, un tableau de bord de ticker boursier. Cette application affiche une liste d'actions et dispose de certains contrôles pour automatiser les actions de test de l'interface utilisateur. Pour chaque action, l'application affiche le symbole du ticker, le nom de l'entreprise, le nom du secteur, le prix actuel, le volume et les moyennes mobiles simples (10 jours, 50 jours et 200 jours), ainsi qu'un indicateur visuel montrant si le prix a augmenté ou diminué. Le jeu de données de test se compose de 5000 tickers boursiers et est chargé lors du chargement de la page via une balise de script.

J'ai créé trois versions de cette application en utilisant AngularJS, React/Redux et React/Mobx. Cela nous permet de comparer facilement les métriques de performance pour chaque scénario entre les frameworks.

![Image](https://cdn-media-1.freecodecamp.org/images/EhA-FdGhYq33bnzqOERvMcuypgwCVg29k5l3)
_Page de test de performance_

#### Scénarios de test

* **Changement de vues**  
Nous naviguons à travers une liste de 5000 tickers boursiers, affichant 150 tickers à la fois toutes les 0,5 seconde. Ce scénario mesure la rapidité avec laquelle le framework peut mettre à jour la vue lorsque les données du modèle de collection visible changent.   
_Cas d'utilisation réel : changements de route, pagination à travers une liste, défilement virtuel, etc._
* **Ajout de tickers**   
Nous ajoutons 50 tickers à la collection visible toutes les 100 ms jusqu'à ce que nous affichions l'ensemble de la collection de 5000 tickers. Ce scénario mesure la rapidité avec laquelle le framework peut créer de nouveaux éléments. Afficher 5000 tickers n'est pas un scénario réaliste, mais nous pouvons visualiser les limites où les choses vont se dégrader avec chaque framework.  
_Cas d'utilisation réel : défilement infini de style Pinterest où de nouveaux éléments d'interface utilisateur sont ajoutés au DOM lorsque l'utilisateur fait défiler._
* **Mises à jour rapides du prix/volume**  
Nous affichons 1500 tickers et commençons à mettre à jour les données de prix/volume pour des tickers aléatoires une fois toutes les 10 ms. Ce scénario mesure la rapidité avec laquelle les frameworks peuvent appliquer les mises à jour partielles à l'interface utilisateur.   
_Cas d'utilisation réel : mises à jour des indicateurs de présence, des likes, des retweets, des applaudissements, des prix des actions, etc._
* **Suppression de tickers**  
Nous allons d'abord ajouter tous les 5000 tickers, puis commencer à supprimer 50 tickers de la collection visible une fois toutes les 100 ms.

#### Liens vers les pages de test et le code source

Tous les exemples sont écrits en TypeScript et la compilation/bundling est effectuée à l'aide de Webpack. La page Readme pour l'URL source liste les instructions pour construire et exécuter les applications.

* AngularJS — [https://guptag.github.io/js-frameworks/AngularJS/examples/angularjs-perf-test/index.html](https://guptag.github.io/js-frameworks/AngularJS/examples/angularjs-perf-test/index.html) ([Source](https://github.com/guptag/js-frameworks/tree/master/AngularJS/examples/angularjs-perf-test))
* React/Redux — [https://guptag.github.io/js-frameworks/Redux/examples/redux-perf-test/index.html](https://guptag.github.io/js-frameworks/Redux/examples/redux-perf-test/index.html)   
([Source](https://github.com/guptag/js-frameworks/tree/master/Redux/examples/redux-perf-test))
* React/Mobx — [https://guptag.github.io/js-frameworks/Mobx/examples/mobx-perf-test/index.html](https://guptag.github.io/js-frameworks/Mobx/examples/mobx-perf-test/index.html)   
([Source](https://github.com/guptag/js-frameworks/tree/master/Mobx/examples/mobx-perf-test))

### Avant de commencer…

* Toutes les métriques ci-dessous sont mesurées sur Win10/Intel Xeon E5 @ 2.4GHz, 6 cœurs, 32GB de RAM avec le navigateur Chrome v60. Les chiffres varieront sur différentes machines/navigateurs.
* Pour voir les données précises de la mémoire heap sur les pages de test, ouvrez Chrome avec le flag « --enable-precise-memory-info ».
* React est une bibliothèque plutôt qu'un framework complet comme AngularJS. Dans cet article, j'ai utilisé le terme framework pour simplifier.
* Les pages de test montrent la taille live du heap JavaScript sous Memory.  
À propos de la taille du heap JavaScript : Dans Chrome TaskManager,

> Dans Chrome TaskManager, « La colonne Mémoire représente la mémoire native. Les nœuds DOM sont stockés dans la mémoire native. Si cette valeur augmente, des nœuds DOM sont créés. La colonne Mémoire JavaScript représente le heap JS. Cette colonne contient deux valeurs. La valeur qui vous intéresse est le nombre live (le nombre entre parenthèses). Le nombre live représente la quantité de mémoire utilisée par les objets accessibles sur votre page. Si ce nombre augmente, soit de nouveaux objets sont créés, soit les objets existants grandissent. » [De Fix Memory Issues par Kayce Basques](https://developers.google.com/web/tools/chrome-devtools/memory-problems/)

* À propos des frames par seconde :

> « La plupart des appareils aujourd'hui rafraîchissent leurs écrans 60 fois par seconde. Si une animation ou une transition est en cours d'exécution, ou si l'utilisateur fait défiler les pages, le navigateur doit correspondre au taux de rafraîchissement de l'appareil et afficher une nouvelle image, ou frame, pour chacun de ces rafraîchissements d'écran. Chacune de ces frames a un budget de juste plus de 16 ms (1 seconde / 60 = 16,66 ms). En réalité, cependant, le navigateur a du travail de maintenance à faire, donc tout votre travail doit être terminé en moins de 10 ms. Lorsque vous ne respectez pas ce budget, le taux de frames chute, et le contenu s'affiche par saccades à l'écran. Cela est souvent appelé jank, et cela impacte négativement l'expérience de l'utilisateur. » [De Rendering Performance par Paul Lewis](https://developers.google.com/web/fundamentals/performance/rendering/)

### DOM - Composants AngularJS vs. Composants React

Les directives AngularJS (ou composants) créent un élément wrapper supplémentaire autour du template. Pour les vues simples, ce n'est pas un problème. Cependant, dans les vues complexes contenant un grand nombre de directives (surtout lorsqu'elles sont répétées dans ng-repeat), tous les éléments supplémentaires s'ajouteront à la taille totale de l'arbre DOM — potentiellement impactant la mémoire, les performances des sélecteurs, etc.

Bien que vous puissiez définir la propriété 'replace=true' pour désactiver le rendu de l'élément wrapper, cela provoque un ensemble de problèmes et est [actuellement marqué comme obsolète](https://github.com/angular/angular.js/commit/eec6394a342fb92fba5270eee11c83f1d895e9fb).

Voici le HTML rendu pour le composant ticker dans AngularJS :

![Image](https://cdn-media-1.freecodecamp.org/images/kTJ0GNtycTKAdofCEjHbbiv-UIg7OlHMVCsq)
_Directive/composant AngularJS (côté gauche), HTML rendu (côté droit) - Un élément wrapper est créé pour chaque directive enfant._

Voici le HTML rendu pour le composant ticker similaire dans React :

![Image](https://cdn-media-1.freecodecamp.org/images/s4cxv5BoHVqYqpqFkrWbnaLppQOMvqrVqFMw)
_Composant React (côté gauche), HTML rendu (côté droit) - Aucun élément wrapper créé pour les composants enfants_

Dans notre exemple spécifique, AngularJS a créé 1400 nœuds DOM supplémentaires par rapport à React pour rendre le même nombre de tickers (200).

![Image](https://cdn-media-1.freecodecamp.org/images/cp0RpJDvv2Ko88EKSfogOaTmVEFGNuc-irCa)
_Compte des nœuds DOM — AngularJS vs. React_

### Scénario 1 — Changement de vues

Nous naviguons à travers une liste de 5000 tickers, affichant 150 tickers à la fois toutes les 0,5 seconde.

Le graphique ci-dessous trace le temps d'exécution du script pour chaque rafraîchissement à partir de la timeline de performance de Chrome. AngularJS a systématiquement pris >200 ms pour supprimer les 150 tickers existants et en afficher de nouveaux. Alors que React/Redux a effectué le même travail en 90–100 ms (la moitié du temps par rapport à ng1). La version React/Mobx a pris légèrement plus de temps que la version Redux, mais pas beaucoup plus.

![Image](https://cdn-media-1.freecodecamp.org/images/EavjKTdDoodsQ1DE3SGvtxxJAzRBLK2EVQ7J)
_Comparaison du temps d'exécution des scripts (AngularJS vs. React/Redux vs. React/Mobx) — Remplacement de 150 tickers toutes les 0,5 seconde_

Le graphique ci-dessous montre les frames par seconde (fps) lors du rafraîchissement. Les versions Redux et Mobx sont restées autour de 45 fps alors qu'AngularJS est resté autour de 30 fps pendant toute l'exécution.

![Image](https://cdn-media-1.freecodecamp.org/images/Pz5M93atTLYJnCuuTLKyPoPIilOAiokrT78b)

#### **Mémoire et pauses GC**

Le graphique ci-dessous montre la taille du heap JavaScript (« usedJSHeapSize ») mesurée pendant le rafraîchissement. Les versions AngularJS et Mobx ont montré un motif en escalier pour la consommation de mémoire, indiquant que Chrome a déclenché le GC pour récupérer la mémoire. La version Redux est très constante avec son faible profil mémoire tout au long de l'exécution.

![Image](https://cdn-media-1.freecodecamp.org/images/AvWVCzs4F7DZxNSAU6-VMtmm0tIN1m4wxg5r)

Examinons de près les profils de timeline pour les trois versions.

L'exécution d'AngularJS a provoqué plusieurs pauses GC lors du rafraîchissement de la liste des tickers. [V8 essaie de masquer les pauses GC en les planifiant pendant les périodes d'inactivité non utilisées pour améliorer la réactivité de l'interface utilisateur](https://v8project.blogspot.com/2015/08/getting-garbage-collection-for-free.html). Contrairement à ce comportement idéal, les pauses GC se sont produites pendant l'exécution du script, contribuant au temps d'exécution global.

![Image](https://cdn-media-1.freecodecamp.org/images/-BtwuertIbQDuGJCblQlG0QJITNwvU6L8sDG)
_AngularJS a émis de nombreux événements GC lors du rafraîchissement de la liste des tickers avec 150 nouveaux éléments_

Le profil de performance de Redux ne montre aucune pause GC pendant l'exécution du script.

![Image](https://cdn-media-1.freecodecamp.org/images/ZiB4Ufc9iquZQzjP1vctBmLayeAMX9aflDqF)
_React/Redux — Aucune pause GC_

Le profil Mobx montre quelques pauses GC, mais pas autant que la version AngularJS.

![Image](https://cdn-media-1.freecodecamp.org/images/k4AUDMMOj1WtfiOAfGvhCGNIktRc-K4Cowd6)
_React/Mobx — Quelques pauses GC mais pas autant que la version AngularJS_

### Scénario 2 — Ajout de tickers

Nous allons ajouter 50 tickers à la collection visible toutes les 100 ms jusqu'à ce que nous affichions tous les tickers. Le résultat de l'affichage de tous les 5000 tickers n'est pas un scénario réaliste, mais il serait intéressant de voir comment chaque framework le gère.

Le graphique ci-dessous trace le temps d'exécution du script à partir de la timeline de performance de Chrome. Dans le cas d'AngularJS, le temps d'exécution du script a augmenté linéairement à mesure que de plus en plus de tickers étaient ajoutés à la page. AngularJS a pris plus de temps pour ajouter de nouveaux tickers dès le début par rapport aux autres versions.

De manière intéressante, les versions Redux et Mobx montrent des performances impressionnantes même vers la droite du graphique avec des milliers de tickers sur la page. L'algorithme de diffing du DOM virtuel de React montre sa force par rapport au dirty checking d'AngularJS.

![Image](https://cdn-media-1.freecodecamp.org/images/NIeetxK6i7T8N9wH-137uWZ-Ef39pBLng936)
_Ajout de tickers — Comparaison du temps d'exécution des scripts_

Avec AngularJS, l'ajout de nouveaux éléments a provoqué des saccades dans le navigateur dès le début (barres rouges) et le nombre de frames par seconde est tombé de 60 tôt et n'a jamais récupéré (zone verte) pendant toute l'opération d'ajout.

![Image](https://cdn-media-1.freecodecamp.org/images/0IM4iKnHIb795zyDko1lBWHNMYcjsnaw0Oni)
_AngularJS — Timeline d'ajout de tickers_

Redux a provoqué des saccades une fois au début, mais tout est clair jusqu'à ce que nous ayons dépassé le point médian de l'ajout de nouveaux tickers. Les FPS ont également bien récupéré à 60 entre les opérations d'ajout.

![Image](https://cdn-media-1.freecodecamp.org/images/9SQzLRly315H5bmYc7K1PzvYL3vXiAzP64tj)
_Redux — Timeline d'ajout de tickers_

Mobx a provoqué des saccades quelques fois de plus que Redux, mais rien de comparable à AngularJS.

![Image](https://cdn-media-1.freecodecamp.org/images/Iu3DqyihMvKsoJPIrZZF0ZtLRuZYrdKCJ21r)
_Mobx — Timeline d'ajout de tickers_

#### **Mémoire et événements GC**

Redux a consommé environ la moitié de la taille du heap par rapport à AngularJS pendant toute l'exécution. Mobx est resté entre les deux.

![Image](https://cdn-media-1.freecodecamp.org/images/T91WZQF9HJ9p1Eb3Tkn3W47Ra3fbUqyj9ULD)
_Ajout de tickers — Comparaison de la mémoire_

L'ajout de nouveaux tickers a également déclenché quelques pauses GC avec AngularJS (presque une fois avec chaque opération d'ajout). Redux a déclenché moins de pauses GC dans l'ensemble. Mobx a commencé à déclencher plus de pauses GC vers la fin à mesure que nous ajoutions de plus en plus de tickers à la liste.

![Image](https://cdn-media-1.freecodecamp.org/images/Oz8qWGRaltyJ1L9lrrPWLlRvOWrAnp1kMqpe)
_Ajout de tickers — Événements GC AngularJS (timeline partielle)_

![Image](https://cdn-media-1.freecodecamp.org/images/sa5nuYHeg2-h3cdu5Y4c775B5HreFKwLcFUk)
_Ajout de tickers — Événements GC React/Redux (timeline partielle)_

![Image](https://cdn-media-1.freecodecamp.org/images/B3sCDnsuAlzHYAW9Qnn4YCfW0vAaOBRfGB99)
_Ajout de tickers — Événements GC Mobx (timeline partielle)_

### Scénario 3 — Mises à jour rapides du prix/volume

Il s'agit du scénario le plus courant dans les applications en temps réel. Une fois la vue rendue, il y aura une succession rapide de mises à jour arrivant dans l'application via des web-sockets, des appels xhr, etc. Imaginez les cas d'utilisation comme les mises à jour de présence, les changements de prix des actions, les changements de compte de likes/retweets/claps, et plus encore. Voyons comment chaque framework se comporte dans ce scénario.

Toutes les métriques ci-dessous sont prises avec 1500 tickers sur la page et lorsque les changements de prix/volume se produisent toutes les 10 ms.

AngularJS a à nouveau eu du mal à suivre les mises à jour se produisant en succession rapide. L'exécution du script pour chaque mise à jour a pris environ 35 ms. Redux a pris 6 ms pour mettre à jour la vue. Mobx brille, mettant à jour la vue en 2 ms. Le graphe de dérivation de Mobx sait exactement quel composant mettre à jour en fonction de l'état de l'observable qui a changé.

![Image](https://cdn-media-1.freecodecamp.org/images/OMPlXhWpNtJsRX9R69q0XpWftRvelqzOqofZ)
_Mises à jour — Comparaison du temps d'exécution des scripts_

Voici les profils de timeline montrant l'exécution du script pour chaque version.

![Image](https://cdn-media-1.freecodecamp.org/images/SKU7rg0WPZHRXoTGeMGL3UTCN6Vl1Flk4br5)
_AngularJS — Mises à jour du prix/volume_

![Image](https://cdn-media-1.freecodecamp.org/images/15yZ2hcVcPB9wZgc27n85oGbOHgSCb5ZDNJe)
_Redux — Mises à jour du prix/volume_

![Image](https://cdn-media-1.freecodecamp.org/images/2XyT5qWBw6Oz1fpdre0Ex2BHHipSfkFZ8uKJ)
_Mobx — Mises à jour du prix/volume_

Les FPS sont restés constamment à 60 avec Redux et Mobx, alors qu'ils ont oscillé un peu en dessous de 30 avec AngularJS.

![Image](https://cdn-media-1.freecodecamp.org/images/-HspGSYy0PukZo0TqJ-h-B7Zp4oLAg8IeGvJ)
_Mises à jour du prix/volume — Frames par seconde_

### Scénario 4 — Suppression de tickers

Nous allons ajouter tous les 5000 tickers à la page et commencer à supprimer 50 tickers de la collection visible toutes les 100 ms.

Les images ci-dessous montrent le profil de performance des premières itérations de suppression. AngularJS est presque 4 fois plus lent par rapport aux versions React. Redux et Mobx ont pris un peu plus de temps dans les premières itérations mais se sont stabilisés entre 50–70 ms pour chaque opération de suppression.

![Image](https://cdn-media-1.freecodecamp.org/images/QU4wRyQDQpK6xMCQKP95ISP6PRvxe4xtepCa)
_AngularJS — Suppression de 50 tickers parmi 5000 tickers toutes les 100 ms (premières itérations)_

![Image](https://cdn-media-1.freecodecamp.org/images/9GESwmbGwHXE50FwaPpxJwVmmT6-LKafQ--J)
_Redux — Suppression de 50 tickers parmi 5000 tickers toutes les 100 ms (premières itérations)_

![Image](https://cdn-media-1.freecodecamp.org/images/qeqR9f6RklGhNYRQmbvWDQ26Ljs3KtTkf5Az)
_Mobx — Suppression de 50 tickers parmi 5000 tickers toutes les 100 ms (premières itérations)_

Il est assez clair d'après tous les tests ci-dessus que React offre des gains de performance significatifs par rapport à AngularJS.

À mesure que les applications deviennent plus grandes et que les vues deviennent plus complexes, le profil d'exécution des frameworks commence à différer de diverses manières. Notre objectif était de reproduire les scénarios que nous ciblions, de mesurer l'impact sur les performances/mémoire et d'examiner les avantages/inconvénients des constructions avec chaque framework.

Même avec le framework le plus performant, nous devons encore appliquer beaucoup de discipline et suivre les bons modèles pour rendre les applications scalables et performantes.

Je passe en revue les concepts de base, les avantages et les pièges de Redux et Mobx dans [un article séparé](https://hackernoon.com/introduction-to-redux-and-mobx-e6fa98b6479).

Merci d'avoir lu. J'espère que cela est utile.

P.S. Merci à [Shyam Arjarapu](https://www.freecodecamp.org/news/measuring-performance-gains-angularjs-to-react-with-redux-or-mobx-fb221517455/undefined) et [Adam Carr](https://www.freecodecamp.org/news/measuring-performance-gains-angularjs-to-react-with-redux-or-mobx-fb221517455/undefined) pour avoir révisé cet article.