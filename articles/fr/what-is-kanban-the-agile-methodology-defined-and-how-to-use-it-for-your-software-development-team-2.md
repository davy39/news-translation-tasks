---
title: Qu'est-ce que le Kanban ? La méthodologie Agile définie et comment l'utiliser
  pour votre équipe de développement logiciel
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-19T11:12:13.000Z'
originalURL: https://freecodecamp.org/news/what-is-kanban-the-agile-methodology-defined-and-how-to-use-it-for-your-software-development-team-2
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/grafik-8.png
tags:
- name: agile
  slug: agile
- name: kanban
  slug: kanban
- name: Scrum
  slug: scrum
- name: software
  slug: software
- name: technology
  slug: technology
seo_title: Qu'est-ce que le Kanban ? La méthodologie Agile définie et comment l'utiliser
  pour votre équipe de développement logiciel
seo_desc: 'By Bertil Muth

  Kanban was invented in the Japanese automotive industry in the first half of the
  20th century. Inspired by how supermarkets stock their shelves based on demand,
  Toyota''s goal was to reduce inventory and to improve the flow throughout t...'
---

Par Bertil Muth

Le Kanban a été inventé dans l'industrie automobile japonaise dans la première moitié du 20e siècle. Inspiré par la manière dont les supermarchés stockent leurs rayons en fonction de la demande, l'objectif de Toyota était de réduire les stocks et d'améliorer le flux dans l'ensemble de leur système de production.

Dans son livre _Kanban : Successful Evolutionary Change for Your Technology Business_, David Anderson a décrit comment appliquer les principes du Kanban au développement logiciel. Ces principes sont :

* Commencez avec ce que vous faites maintenant
* Acceptez de poursuivre un changement incrémental et évolutif
* Respectez le processus actuel, les rôles, les responsabilités et les titres

## Que signifie cela pour le développement logiciel agile ?

Dans mes formations, je demande aux participants ce qu'ils savent déjà sur le [développement logiciel agile](https://agilemanifesto.org/). Les réponses courantes sont : "Travailler en Sprints", "Il y a un propriétaire de produit", "Gérer les histoires utilisateur dans un backlog." Les gens sont influencés par le cadre agile probablement le plus populaire aujourd'hui, Scrum.

Scrum vient avec ses propres rôles, événements et artefacts prédéfinis. Scrum vous oblige à suivre les règles définies dans le [Guide Scrum](https://www.scrumguides.org/), si vous voulez appeler ce que vous faites Scrum. Kanban est différent.

Kanban commence avec le processus que vous suivez dans votre entreprise maintenant. Visualisez les étapes sur un tableau Kanban. Elles peuvent inclure tout ce que vous faites, de l'idée à la livraison.

Chaque étape devient le titre d'une colonne sur le tableau.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/grafik-7.png)

Pour suivre votre travail au quotidien, il est préférable de le diviser en petits éléments. Peut-être des histoires utilisateur qui peuvent être implémentées en, au plus, 2 jours. Écrivez chaque élément sur un post-it et accrochez-le sur le tableau. Vous pouvez utiliser l'ordre vertical sur le tableau pour la priorisation.

Les cartes se déplacent de gauche à droite. Les personnes qui effectuent le travail tirent les éléments qui ont été terminés par l'étape précédente du processus. Lorsqu'elles ont la capacité de le faire. Ainsi, les développeurs dans l'exemple tirent la carte _Upload Image_ dans _Dev_ lorsqu'ils ont la capacité de l'implémenter.

## Poursuivre un changement incrémental et évolutif

Vous avez donc créé un tableau Kanban qui montre votre processus ? Vous rendez votre travail visible, ce qui est un excellent début !

Pour tirer profit du Kanban, vous devez faire quelques choses de plus. Vous devez :

* Limiter le travail en cours et les files d'attente
* Observer et améliorer le flux
* Collaborer efficacement

### Limiter le travail en cours et les files d'attente

Limiter le travail en cours signifie : vous fixez un maximum pour le nombre d'éléments sur lesquels vous travaillez. Cela s'appelle la limite de travail en cours, ou en abrégé, la limite WiP. Voici le tableau Kanban avec une limite WiP pour certaines étapes du processus.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/grafik-9.png)

Les développeurs peuvent travailler sur 5 éléments à la fois. Au maximum. Si leur colonne contient 5 éléments, ils ne sont pas autorisés à tirer d'autres éléments. Cela a deux conséquences.

Tout d'abord : cela encourage les gens à terminer leur travail, au lieu de commencer plus de travail. Le travail commencé qui n'est pas terminé comporte des risques. À quel point vos clients seront-ils heureux si vous ne pouvez pas livrer votre logiciel comme prévu ? Parce que vous avez commencé à travailler sur toutes ces grandes idées, mais vous ne les avez pas menées à terme ?

La deuxième conséquence de la limitation du travail en cours : les goulots d'étranglement deviennent visibles. Lorsqu'une étape du processus commence un travail qu'elle ne peut pas terminer, les gens le sentiront immédiatement. Parce que l'étape suivante du processus ne pourra pas tirer d'éléments.

En plus de limiter le travail en cours, vous devez également limiter la taille des files d'attente. Dans le tableau ci-dessus, elles sont représentées par les lignes pointillées entre les colonnes. Cela fonctionne de la même manière que la limitation du travail en cours.

En résumé : _Arrêtez de commencer, commencez à finir_ est la devise. Du concept à la livraison en aussi peu de temps que possible.

### Observer et améliorer le flux

Observer un goulot d'étranglement peut être douloureux au début. Mais au moins vous savez où se situent les principaux problèmes dans votre processus. Et Kanban vous encourage à améliorer le flux en supprimant le goulot d'étranglement. Un flux constant vous permet de livrer de manière plus fiable, et c'est bon pour toutes les parties prenantes, y compris les développeurs.

Pour observer le flux, vous enregistrez l'heure à laquelle une carte entre dans une étape du processus. Et l'heure à laquelle vous terminez l'étape du processus. Ainsi, vous savez combien de temps la carte passe dans chaque étape et dans chaque file d'attente entre les étapes.

Sur la base des données, vous pouvez mettre en place des métriques qui vous aident à améliorer le flux. Les métriques courantes incluent :

* Temps de cycle : le temps qu'une carte prend à partir du moment où une équipe commence à travailler dessus (c'est-à-dire _Dev_) jusqu'à la livraison (c'est-à-dire _Release_). Améliorer cette métrique peut vous aider à améliorer votre temps de mise sur le marché.
* Débit : le nombre de cartes qui passent par le système dans un temps donné. Améliorer cette métrique peut vous aider à améliorer la performance de votre organisation de livraison.

Un moyen courant d'avoir un aperçu du nombre de cartes dans chaque étape du processus au fil du temps est un graphique de flux cumulé. Idéalement, le nombre de cartes dans chaque étape, sauf la dernière, reste à peu près le même au fil du temps. Le nombre de cartes livrées devrait augmenter. Lorsque le graphique s'écarte de cela, vous pourriez avoir un goulot d'étranglement.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Cumulative_Flow_Chart.png)

### Collaborer efficacement

Les métriques Kanban sont un outil puissant pour analyser et améliorer ce que vous faites. Mais elles sont sans valeur sans les personnes qui effectuent le travail. Tout le monde impliqué dans les étapes du processus devrait être ouvert à la transparence que crée Kanban.

Les personnes devraient travailler ensemble de manière constructive pour éliminer les goulots d'étranglement, au lieu de blâmer les individus. Regardez l'état actuel régulièrement. Y a-t-il des goulots d'étranglement ? Y a-t-il trop ou trop peu de travail disponible pour une certaine étape du processus ? Le débit est-il suffisant ? Y a-t-il d'autres sources de mécontentement ? Qu'est-ce qui doit être amélioré ?

Convenez d'expériences qui testent de petits changements dans le système. Réalisez les changements. Plus tard, voyez si les expériences ont fonctionné comme prévu. Pour pouvoir mettre en œuvre les changements, le soutien de la direction est souvent crucial.

## Quand utiliser Kanban

Kanban est très flexible. Il peut être utilisé en combinaison avec Scrum, ce qui s'appelle [Scrumban](https://en.wikipedia.org/wiki/Scrumban). Il peut être utilisé en dehors du développement de produits. Vous pouvez même l'utiliser pour planifier un voyage ou organiser ce que vous faites dans votre temps libre.

Je l'ai trouvé particulièrement utile lorsque le travail en Sprints Scrum n'est pas possible ou est difficile. Exemple : deux entreprises où l'une est cliente et l'autre est fournisseur, et un transfert est inévitable. Un autre exemple est lorsque vous travaillez sur un produit qui implique à la fois du logiciel et du matériel, et que plusieurs disciplines d'ingénierie sont impliquées.

Kanban peut également être utilisé au sein de votre entreprise lorsque le développement travaille de manière agile, mais pas le reste de l'entreprise. Il peut être utilisé pour faciliter la coopération entre la planification stratégique et le développement logiciel.

Ne pensez pas que simplement parce que vous avez des difficultés à mettre en œuvre Scrum, il n'y a aucun moyen de devenir plus agile. Kanban commence avec ce que vous faites maintenant. Et si vous le prenez au sérieux, il vous aidera à vous améliorer. Une petite étape à la fois.

_Pour_ [_en savoir plus sur le développement logiciel agile_](https://skl.sh/2Cq497P)_, visitez mon cours en ligne. Pour suivre ce que je fais ou me laisser un mot, suivez-moi sur_ [_dev.to_](https://dev.to/bertilmuth)_,_ [_LinkedIn_](https://www.linkedin.com/in/bertilmuth/) _ou_ [_Twitter_](https://twitter.com/BertilMuth)_. Ou visitez mon_ [_projet GitHub_](https://github.com/bertilmuth/requirementsascode)_.