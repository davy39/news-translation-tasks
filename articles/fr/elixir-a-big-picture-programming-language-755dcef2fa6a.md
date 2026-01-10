---
title: 'Elixir : Un langage de programmation à grande échelle'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-22T16:40:02.000Z'
originalURL: https://freecodecamp.org/news/elixir-a-big-picture-programming-language-755dcef2fa6a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tLIXa6jWWjxfB-6AYjm2Hg.jpeg
tags:
- name: Elixir
  slug: elixir
- name: Erlang
  slug: erlang
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: 'Elixir : Un langage de programmation à grande échelle'
seo_desc: 'By CityBase

  Elixir makes programmers better at their work, and it makes their work better

  About a year ago, I decided to pursue the chance to work with Elixir full time as
  lead engineer at CityBase. Since I began using the programming language in 201...'
---

Par CityBase

#### Elixir rend les programmeurs meilleurs dans leur travail, et améliore leur travail

Il y a environ un an, j'ai décidé de saisir l'opportunité de travailler avec Elixir à temps plein en tant qu'ingénieur principal chez CityBase. Depuis que j'ai commencé à utiliser ce langage de programmation en 2014, mon objectif a été d'utiliser, de faire grandir et d'apprendre davantage d'Elixir.

CityBase m'a également attiré pour d'autres raisons. J'ai toujours été curieux de faire fonctionner des systèmes complexes de manière plus efficace. Avec la technologie gouvernementale, nous avons le défi de faire fonctionner certains des systèmes les plus complexes de manière plus efficace pour les gens à grande échelle, avec un impact massif.

Ces objectifs — faire grandir Elixir et coder pour un impact à grande échelle — sont, à mon avis, les mêmes. Je crois vraiment que, de nos jours, la fiabilité, la concurrence et la tolérance aux pannes sont des qualités fondamentales sur lesquelles la plupart des applications devraient être construites. Elixir peut aider à cela grâce à une liste éprouvée d'applications et de concepts.

![Image](https://cdn-media-1.freecodecamp.org/images/UtGCPFkJSMeNlcix48URAs-F-7-YIhJyx8mf)
_(Photo : [Unsplash](https://unsplash.com/photos/w7ZyuGYNpRQ?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Kevin</a>, <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="))_

### Un nouveau langage avec des racines éprouvées

Elixir est un nouveau langage créé en 2011. Il est construit avec les principes d'Erlang, un système développé en 1986 pour l'industrie des télécommunications. Erlang est la raison pour laquelle votre téléphone n'est jamais temporairement fermé pour maintenance. Il est responsable de la flexibilité et de la scalabilité du matériel, afin que vous puissiez remplacer un téléphone et avoir votre compte qui fonctionne de la même manière, et ajouter de nouvelles lignes téléphoniques sans affecter les performances.

Bien qu'Elixir soit relativement jeune, il repose sur la machine virtuelle (VM) éprouvée d'Erlang, appelée BEAM, et ses principes de haute disponibilité, d'adaptabilité et de scalabilité. Ces fonctionnalités sont exceptionnellement importantes dans les applications govtech, où les services fondamentaux fournis par la technologie doivent être disponibles pour tous.

### Le langage de programmation des programmeurs

Des ingénieurs comme moi sont enthousiastes à l'idée de travailler avec Elixir car cela nous aide à être meilleurs dans notre travail. Pour coder avec Elixir, les développeurs doivent être en phase avec les objectifs commerciaux globaux et coder en gardant à l'esprit la flexibilité future.

Il inclut des outils qui encouragent les programmeurs à planifier autour de ce qui peut mal tourner et à se concentrer sur l'obtention du résultat idéal pour l'utilisateur final.

**Avoir des programmeurs qui comprennent les résultats souhaités à grande échelle peut être un changement de jeu.**

Si vous demandez à quelqu'un d'écrire du code qui effectue une certaine fonction, il écrira ce code. Mais si vous lui demandez d'écrire du code qui mène à une expérience ou résout un problème, il peut penser à une solution que vous n'aviez jamais envisagée — et prévoir des problèmes dont vous ne saviez pas qu'ils existaient.

Elixir encourage ce type de réflexion à grande échelle dans son ADN. Une caractéristique commune d'Elixir et d'Erlang est qu'ils sont des langages de programmation holistiques. Vous pourriez facilement utiliser Elixir pour développer un seul service, mais il est optimisé pour développer de grands systèmes de nombreux services.

### Un langage tolérant aux pannes

Comme la mort et les impôts, une autre certitude dans la vie est que les choses tourneront mal.

Elixir possède une tolérance native aux pannes pour les deux principaux types d'erreurs de programmation.

#### **Type d'erreur 1**

Les problèmes les plus rares sont généralement découverts en production et sont par définition plus difficiles à tester. Par exemple, la connectivité (quand un service tombe en panne ou prend plus de temps que prévu) entre un service tiers ou une ressource système, comme une base de données.

Pour être tolérant aux pannes face à ces problèmes, votre système doit toujours être disponible pour les clients en utilisant au moins deux serveurs. Cela permet de traiter les problèmes matériels, les problèmes réseau ou d'autres erreurs qui existent en dehors de votre programme.

Elixir fonctionne sur la VM BEAM d'Erlang, qui est configurée comme un mini OS au-dessus du système d'exploitation du serveur. La VM est responsable de la communication entre les serveurs et les nœuds. Un nœud sera notifié lorsqu'un autre nœud est hors service, et le système agira en réponse.

#### **Type d'erreur 2**

Les problèmes associés aux données sont plus faciles à tester et peuvent être reproduits localement. Par exemple, si une fonction qui effectue un calcul mathématique reçoit une chaîne de caractères au lieu d'un nombre, cette fonction échouera.

Pour qu'un programme soit tolérant aux pannes ici, votre système doit être capable de se "guérir" lui-même pendant les erreurs découlant de bugs logiques, de données d'entrée incorrectes et d'autres défaillances internes.

Comme Elixir est un langage compilé, toute erreur dans le code empêche l'application de démarrer. Cela garantit que les applications en cours d'exécution ont au moins un état de départ valide.

Pour que cela fonctionne en douceur, la VM Erlang utilise ce qu'on appelle le principe de supervision, qui fonctionne comme suit :

* Les processus sont structurés sur l'idée qu'il existe des modules "travailleurs" et "superviseurs" intégrés dans un programme donné.
* Les travailleurs effectuent des calculs, et les superviseurs surveillent les travailleurs.
* Si quelque chose ne va pas, un superviseur peut redémarrer un travailleur à son état initial valide.

Le principe de supervision est associé à l'isolement des processus, lorsqu'un module peut s'exécuter dans un processus isolé. Cela garantit que les erreurs dans un module n'affecteront pas les autres parties de l'application, et vous pouvez redémarrer ce module en isolation également.

### Un langage modulaire et conçu pour évoluer

Elixir est un langage modulaire, ce qui signifie que vous pouvez modifier des parties autonomes sans vous soucier d'impacter d'autres parties sans rapport. Les microservices fonctionnent de manière concurrente. Ces actions basées sur le code jouent toutes des rôles dans le programme plus large que vous avez créé, mais les tâches sont distribuées de sorte qu'elles ne dépendent pas les unes des autres pour fonctionner. Cela renforce les avantages de l'échec rapide — vous retirez un joueur défectueux, et le jeu continue.

Cela devient également crucial à mesure qu'une base de code grandit : dans les systèmes non modulaires, il n'est pas toujours clair quand une partie impacte les autres — ou quelles autres parties elle pourrait impacter. Cela signifie que même le plus petit changement nécessite que vous testiez tout pour vous assurer que le changement n'a rien cassé. Cela représente une quantité de travail redoutable, ce qui signifie que les projets avancent lentement et nécessitent beaucoup de personnes.

Cela signifie également que la formation de nouveaux développeurs est difficile et chronophage, car ils doivent se familiariser avec un héritage de code complexe afin de l'étendre efficacement.

Avec Elixir, **les développeurs se concentrent sur l'avenir et s'assurent qu'ils codent pour de nouveaux objectifs ou des objectifs évolutifs**, plutôt que pour une vision précédente qui est intégrée dans un code trop complexe.

Au-delà de sa modularité, Elixir est également hautement scalable. Le langage vous permet de commencer à construire une application fonctionnant sur un ou deux serveurs seulement et d'en ajouter plus selon les besoins. Ensemble, les serveurs fonctionnent comme partie d'un cluster dans un système distribué pour atteindre une haute disponibilité et une scalabilité.

Au sein de ce cluster, les serveurs communiquent en utilisant un protocole basé sur Erlang, plutôt que de devoir implémenter ou utiliser un protocole d'application comme HTTP, et choisir une option de sérialisation/désérialisation de données comme JSON ou Protocol Buffers. Cela signifie que vous n'avez pas besoin d'implémenter quoi que ce soit pour passer des données entre les services sur différents serveurs/nœuds. Cela représente un énorme avantage en termes de complexité logique pour la communication.

### Un langage sans niche

Évidemment, je suis un fan d'Elixir. Il a beaucoup d'atouts, de son infrastructure éprouvée à sa scalabilité. Mais peut-être que le plus cool avec ce langage est qu'il est agnostique en termes d'industrie. Déjà, il a été adopté par une gamme d'entreprises, pour diverses fins : WhatsApp, Bleacher Report, Netflix, Pinterest, Postmates, et une poignée de sites .gov utilisent tous Elixir ou Erlang.

Cela présente plusieurs avantages : premièrement, cela signifie que le langage est susceptible de continuer à gagner en popularité à mesure que les entreprises reconnaissent les avantages qu'il peut offrir. Cela, à son tour, signifie que les développeurs continueront à l'apprendre, ce qui signifie qu'il n'est pas probable qu'il y ait une pénurie de développeurs connaissant Elixir. Les entreprises de toutes tailles devraient être en mesure de trouver des développeurs de tous niveaux pour travailler avec Elixir.

Étant donné le pouvoir de ce langage pour améliorer l'expérience utilisateur, minimiser les temps d'arrêt et faciliter la vie des équipes de développement, ce sont des indicateurs que tout le monde devrait applaudir — surtout ceux d'entre nous dans les domaines de l'ingénierie et de la programmation.

Pour ceux d'entre nous dans la govtech, Elixir est particulièrement prometteur, car il incarne le type de résilience et de focus à long terme essentiels pour faire fonctionner les gouvernements de manière meilleure pour tous.



Par [Pedro Assumpcao](http://pedroassumpcao.ghost.io/), Ingénieur Logiciel Principal chez CityBase