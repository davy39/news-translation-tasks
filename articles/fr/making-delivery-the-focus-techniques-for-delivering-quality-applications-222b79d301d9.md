---
title: Comment faire de la livraison votre priorité vous aidera à construire des applications
  de qualité
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-26T01:05:59.000Z'
originalURL: https://freecodecamp.org/news/making-delivery-the-focus-techniques-for-delivering-quality-applications-222b79d301d9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*B8jyD4Cli4xIFtdTD4st_g.png
tags:
- name: agile
  slug: agile
- name: Devops
  slug: devops
- name: Productivity
  slug: productivity
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment faire de la livraison votre priorité vous aidera à construire des
  applications de qualité
seo_desc: 'By Simon Schwartz

  I was recently asked by our company’s executive team why our team was able to develop
  improvements to our product so quickly. This blog outlines some key guidelines,
  from a technical point of view, that our team followed to x iterat...'
---

Par Simon Schwartz

_On m'a récemment demandé par l'équipe dirigeante de notre entreprise pourquoi notre équipe était capable de développer des améliorations à notre produit si rapidement. Ce blog décrit quelques directives clés, d'un point de vue technique, que notre équipe a suivies pour itérer notre produit rapidement et en toute sécurité. J'ai fait de mon mieux pour rester à un niveau élevé dans cet article tout en fournissant des détails techniques. Les techniques dont nous parlons ne sont pas des choses que nous avons inventées._

Mes camarades techniciens de l'équipe et moi avons vu notre rôle comme étant de réduire les frictions pour livrer de la valeur à nos utilisateurs. Nous visions également à maintenir une haute qualité des applications dont nous étions responsables. Nous avons fait une grande partie de cela en supprimant, simplifiant et automatisant les processus autour de la livraison des mises à jour à notre base de code de production.

Gardez à l'esprit qu'il existe certains projets qui peuvent avoir une complexité inhérente. Certaines des techniques que notre équipe a utilisées peuvent ne pas convenir à votre projet. D'après mon expérience, travailler avec des logiciels hérités peut rendre difficile ou impossible de simplifier véritablement certains processus.

### Faire de la livraison la priorité

Notre équipe a priorisé la livraison de fréquentes améliorations à la base de code de production par-dessus tout. Presque tout — nous avons placé des choses comme la santé mentale, permettre aux gens de prendre un jour de congé s'ils étaient malades, et être gentil avant la livraison.

**Le code en production est l'objectif.** Nous nous sommes assurés que toutes les idées, conceptions et demandes de fonctionnalités avaient un chemin clair pour atteindre la production. Une technique que nous avons utilisée pour renforcer cela était de ne montrer que du code fonctionnel lors des présentations. Nous avons interdit les powerpoints et les maquettes de conception. Nous avons également trouvé que cela rendait nos présentations plus engageantes et intéressantes.

**Les réunions sont optionnelles.** Nous avons trouvé que cela encourageait les personnes qui organisaient des réunions à articuler clairement le but et la valeur de la réunion. C'était aux membres de l'équipe de décider s'ils devaient assister à une réunion. Nous voulions éviter que les développeurs soient interrompus inutilement. Il peut falloir jusqu'à 30 minutes pour que quelqu'un retrouve un état productif après avoir été interrompu.

**Passer du temps à résoudre les problèmes des utilisateurs, pas les problèmes technologiques.** Nous voulions éviter de passer d'innombrables heures à discuter de la technologie à utiliser ou à construire notre propre technologie. Nous avons utilisé [AWS Lambda](https://aws.amazon.com/lambda/) pour ne pas avoir à penser aux serveurs et à la mise à l'échelle. Nous avons utilisé [Create React App](https://github.com/facebook/create-react-app) pour ne pas avoir à nous soucier de la configuration de build pour notre application front-end. Nous avons pris des décisions technologiques précoces et nous nous y sommes tenus.

#### ❌ **_Ce que nous avons essayé d'éviter._**

* Nous avons évité de passer des semaines à construire nos propres outils ou frameworks lorsque nous pouvions les réutiliser d'ailleurs.
* Nous avons évité d'ajouter des processus ou des cérémonies inutilement complexes à l'équipe. Cela incluait des tableaux kanban compliqués ou des processus agiles qui ne nous bénéficiaient pas.
* Nous avons évité de passer des semaines à concevoir, construire et supporter des fonctionnalités qui n'avaient **aucune preuve** qu'elles seraient utiles à nos utilisateurs. Notre équipe de conception a fait un excellent travail de conception de fonctionnalités basées sur les retours des utilisateurs et les analyses.

### Rendre les déploiements sans importance

Avoir un cycle de publication rapide signifiait que nous pouvions livrer de nouvelles fonctionnalités à nos utilisateurs dès qu'elles étaient prêtes. Nous nous sommes également remis des bugs et des pannes beaucoup plus rapidement. Un défi majeur des déploiements à haute fréquence est de se déplacer rapidement sans introduire de bugs. Automatiser ce processus est crucial car cela réduit considérablement le temps et les efforts nécessaires pour déployer des mises à jour.

**Automatiser le déploiement.** Une livraison rapide nécessite que le processus de déploiement soit aussi fluide que possible. Heureusement, de nos jours, nous avons de nombreux outils qui peuvent automatiser l'ensemble du processus de déploiement. Je recommande des outils tels que [CircleCI](https://circleci.com/) et [TravisCI](https://travis-ci.org/). Notre configuration était telle que lorsque le nouveau code était ajouté à la branche de publication, le code était automatiquement déployé par notre outil de déploiement.

**Écrire (et automatiser) des tests.** Lors du déploiement automatique des modifications de code, il est crucial de comprendre les impacts des modifications et d'arrêter les déploiements qui introduisent des bugs ou des régressions. Cela signifie que nous devions écrire des tests qui confirment que le code fonctionne comme prévu.

Chaque fois que nous intégrions un nouveau code à une branche de publication, l'outil CI exécutait automatiquement notre suite de tests. Toute échec dans la suite de tests annulerait le processus de déploiement. Les développeurs exécutaient également cette suite de tests localement pour confirmer que tout fonctionnait avant de pousser les modifications. Les tests automatisés sont également beaucoup plus rapides, moins encombrants et moins sujets aux erreurs humaines que les tests manuels.

Livrer rapidement ne fonctionne pas si tout le nouveau code doit être testé manuellement par un humain pendant une heure. En tant qu'équipe, nous avons convenu que nous écririons des tests pour tout le code que nous écrivions. Pour les cas où il n'était pas pratique d'écrire des tests, nous devions donner une raison. Chaque fois que nous corrigeions un bug, nous écrivions également un test qui couvrait le bug. Nous nous sommes assurés que nous avions des tests pour les interactions et parcours courants des utilisateurs (tests d'intégration). Ainsi que des tests pour les fonctions individuelles qui composaient nos applications (tests unitaires).

![Image](https://cdn-media-1.freecodecamp.org/images/XaSYwzsMVr3-wvoSTa6b1-Zm2vwr5aY-OJtL)
_Une de nos suites de tests automatisés construite avec [Cypress](https://www.cypress.io/" rel="noopener" target="_blank" title="). Nous simulons différentes actions que nos utilisateurs pourraient faire et vérifions que les données correctes et l'interface utilisateur seraient affichées. Nous pouvons exécuter automatiquement des dizaines de scénarios très rapidement, ce qui prendrait sinon des heures si cela était fait manuellement._

**Petites mises à jour fréquentes.** Mettre à jour notre base de code par petites incréments a augmenté le rythme auquel nous livrions des améliorations à nos utilisateurs. Les petites mises à jour sont plus faciles à intégrer dans la base de code. Notre processus de revue de code est devenu plus rigoureux. Il était plus facile et plus rapide pour les développeurs de revoir les petites demandes de tirage. Il est beaucoup plus facile d'identifier les problèmes et les impacts du nouveau code parce que la surface du code était si petite.

Une technique que nous avons trouvée utile était de déplacer le processus d'audit d'assurance qualité (QA) de la conception au niveau de la demande de tirage. Cela a rendu le processus QA plus ciblé et plus rapide par opposition à lorsqu'il était effectué tous les quelques jours sur un grand ensemble de multiples changements. En tant qu'équipe, nous avons convenu que nous garderions les PRs petites.

Nous avons également convenu que nous examinerions les PRs dans la demi-journée. Si nous n'étions pas en mesure de les examiner dans ce délai, nous devions le faire savoir à l'auteur.

#### ❌ **_Ce que nous avons essayé d'éviter._**

* Nous avons évité de faire manuellement des tâches que nous pouvions autrement automatiser.
* Nous avons évité les risques associés au déploiement d'une grande quantité de code en une seule fois. Il n'est pas rare de déployer du code qui contient des bugs qui ne sont pas détectés ou des bugs qui ne se manifestent que lorsque le code s'exécute à grande échelle. Plus la surface de nos déploiements est grande, plus l'impact de ces problèmes sera important.

### Rendre la modification du code simple et sûre

> "Pour moi, il n'y a qu'une seule définition de code bien conçu. Un code bien conçu est un code qui est facile à modifier" — Dave Thomas

Avoir la capacité de déployer des modifications de code à la demande est inutile si modifier le code est difficile et chronophage. Écrire du code qui est facile à comprendre et à mettre à jour nous aide à itérer rapidement. En tant qu'équipe technique, nous nous sommes tenus responsables les uns les autres grâce à notre processus de revue de code pour nous assurer que nous écrivions du code aussi clairement et simplement que possible.

**Écrire du code modulaire et réutilisable.** Les fonctions sont les éléments de base de nos applications. Ces fonctions doivent être petites, découplées et avoir un seul but. Cela rend plus facile pour les développeurs de suivre et de comprendre la logique de l'application. Il est plus facile de réutiliser des fonctions existantes pour réduire la quantité de code écrit. Changer des fonctions est beaucoup plus sûr parce que la surface de la fonction est si petite. Les effets du changement sont plus faciles à comprendre. En tant qu'équipe, nous examinions soigneusement les demandes de tirage des uns et des autres et donnions des retours pour nous aider à écrire le meilleur code possible.

**Écrire du code pour les humains.** Il y a deux utilisateurs principaux du code que nous écrivons : les ordinateurs qui exécutent le code et les humains qui le lisent et le modifient. La plupart des développeurs sont assez bons pour écrire du code pour les ordinateurs. Si votre code s'exécute ou se compile sans bugs — cela signifie que vous avez fait un bon travail en écrivant du code pour l'ordinateur. Certains développeurs oublient d'écrire du code pour les humains. Si le code est difficile à comprendre, il faudra plus de temps aux développeurs pour le comprendre et le mettre à jour. Nous nous sommes concentrés sur la clarification du but, des sorties et des entrées de chaque fonction.

Les entrées et sorties des fonctions étaient clarifiées avec le système de types. Nous avons utilisé le système de types intégré lors de l'utilisation de Go, et Flow lors de l'utilisation de JavaScript.

Nous avons choisi des noms descriptifs pour nos variables. Cela a rendu plus clair les données que la variable contenait ou la fonction qui était exécutée.

```
// Ces deux fonctions font la même chose
```

```
function a(arr) {  return arr.filter(it => it.age < 30)}
```

```
function getUsersUnder30(userList) {  return userList.filter(user => user.age < 30)}
```

**Écrire du code testable.** Chaque fois que nous modifions le code, nous devons être sûrs que nos modifications n'ont pas régressé la fonctionnalité précédente du code. C'est l'un des grands avantages d'avoir des tests. Cela ajoute un niveau de sécurité à la modification du code. Nous avons facilité notre vie en écrivant du code de manière à ce qu'il soit simple d'écrire des tests pour celui-ci. Une technique pour écrire du code qui est facile à tester est d'utiliser des _fonctions pures_.

Une fonction pure est une fonction qui, étant donné les mêmes entrées, retournera toujours les mêmes sorties. Ces fonctions sont super simples à tester. Si vous êtes intéressé à en apprendre davantage sur les fonctions pures, [Eric Elliot](https://medium.com/@_ericelliott) a [un article fantastique décrivant les fonctions pures](https://medium.com/javascript-scene/master-the-javascript-interview-what-is-a-pure-function-d1c076bec976).

Malheureusement, vous ne pouvez pas écrire une fonction comme une fonction pure si elle a des _effets secondaires_. Un effet secondaire est quelque chose qui opère en dehors de la portée de sa fonction. Cela pourrait être des opérations telles que l'écriture d'un fichier ou l'envoi d'une requête API. Les effets secondaires peuvent être difficiles à tester au niveau unitaire, donc ceux-ci étaient séparés de nos fonctions pures.

#### ❌ **_Ce que nous avons essayé d'éviter._**

* Nous avons évité de perdre du temps à tester manuellement des scénarios que nous pouvions automatiser.
* Nous avons évité de compromettre la qualité du code pour la vitesse. Compromettre la qualité du code pour la vitesse est redondant. Non seulement vous êtes plus susceptible d'introduire des bugs, mais vous créez également une base de code qui sera éventuellement très difficile à modifier et à déboguer. Cela ralentira considérablement votre capacité à livrer de nouvelles fonctionnalités et des corrections de bugs.

Merci d'avoir lu !