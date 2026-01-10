---
title: Revue de code — Le guide ultime
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-05T16:05:16.000Z'
originalURL: https://freecodecamp.org/news/code-review-the-ultimate-guide-aa45c358bbf5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*c8t6OXt7tMEUpeki-HEobg.jpeg
tags:
- name: code review
  slug: code-review
- name: project management
  slug: project-management
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
seo_title: Revue de code — Le guide ultime
seo_desc: 'By Assaf Elovic

  The ultimate guide for building your team’s code review process


  After conducting hundreds of code reviews, leading R&D teams and pushing several
  unintentional bugs myself, I’ve decided to share my conclusions for building the
  ultimat...'
---

Par Assaf Elovic

#### Le guide ultime pour construire le processus de revue de code de votre équipe

![Image](https://cdn-media-1.freecodecamp.org/images/1*c8t6OXt7tMEUpeki-HEobg.jpeg)

Après avoir effectué des centaines de revues de code, dirigé des équipes de R&D et introduit plusieurs bugs involontaires moi-même, j'ai décidé de partager mes conclusions pour construire le processus ultime de revue de code pour votre équipe.

Cet article suppose que vous savez ce qu'est une revue de code. Donc, si ce n'est pas le cas, [cliquez ici](https://en.wikipedia.org/wiki/Code_review) pour une excellente introduction.

Énonçons rapidement quelques raisons simples pour lesquelles vous devriez faire des revues de code :

1. Peut aider à réduire les bugs dans le code.
2. Valider que toutes les exigences de codage ont été remplies.
3. Une manière efficace d'apprendre de ses pairs et de se familiariser avec la base de code.
4. Aide à maintenir la cohérence du style de code au sein de l'équipe.
5. Cohésion d'équipe — encourage les développeurs à discuter des meilleures pratiques et des normes de codage.
6. Améliore la qualité globale du code grâce à la pression des pairs.

Cependant, les revues de code peuvent être l'une des parties les **plus difficiles et chronophages** du processus de développement logiciel.

Nous y avons tous été. Vous avez peut-être attendu des jours avant que votre code ne soit revu. Une fois revu, vous avez commencé un ping-pong avec le relecteur pour resoumettre votre pull request. Tout à coup, vous passez des semaines à aller et venir. Vous alternez entre de nouvelles fonctionnalités et d'anciens commits qui ont encore besoin d'être polis.

> Si le processus de revue de code n'est pas bien planifié, il pourrait coûter plus qu'il n'apporte.

C'est pourquoi il est extrêmement important de structurer et de construire un processus bien défini pour les revues de code au sein de votre équipe d'ingénierie.

En général, vous devrez avoir en place des directives bien définies pour le relecteur et le revu, avant de créer une pull request et pendant qu'elle est en cours de revue. Plus spécifiquement :

#### Définir les prérequis pour créer des pull requests.

J'ai trouvé que les éléments suivants réduisent grandement les frictions :

1. Assurez-vous que le code compile avec succès.
2. Lisez et annotez votre code.
3. Construisez et exécutez des tests qui valident la portée de votre code.
4. Tout le code dans la base de code doit être testé.
5. Liez les tickets/éléments pertinents dans votre outil de gestion des tâches (JIRA par exemple) à votre pull request.
6. Ne désignez pas de relecteur tant que vous n'avez pas finalisé les étapes ci-dessus.

#### Définir les responsabilités du revu

Bien que le relecteur soit le dernier maillon de la chaîne avant la fusion de votre PR, plus celle-ci est bien préparée par le revu, moins vous rencontrerez de risques à long terme. Voici quelques directives qui peuvent grandement aider :

1. **Communiquez avec votre relecteur** — Donnez à vos relecteurs le contexte de votre tâche. Puisque la plupart d'entre nous, auteurs de pull requests, avons probablement déjà été relecteurs, mettez-vous simplement à la place du relecteur et demandez-vous : « Comment cela pourrait-il être plus facile pour moi ? »
2. **Faites des pull requests plus petites** — Faire des pull requests plus petites est le meilleur moyen d'accélérer votre temps de revue. Gardez vos pull requests petites afin de pouvoir itérer plus rapidement et plus précisément. En général, les changements de code plus petits sont également plus faciles à tester et à vérifier comme stables. Lorsque une pull request est petite, il est plus facile pour les relecteurs de comprendre le contexte et de raisonner avec la logique.
3. **Évitez les changements pendant la revue de code** — Les changements majeurs au milieu de la revue de code réinitialisent essentiellement tout le processus de revue. Si vous devez apporter des changements majeurs après avoir soumis une revue, vous pouvez envoyer votre revue existante et suivre avec des changements supplémentaires. Si vous devez apporter des changements majeurs après avoir commencé le processus de revue de code, assurez-vous d'en informer le relecteur dès que possible.
4. **Répondez à tous les commentaires actionnables de la revue de code** — Même si vous n'implémentez pas leurs commentaires, répondez-y et expliquez votre raisonnement. Si quelque chose n'est pas clair, posez des questions à l'intérieur ou à l'extérieur de la revue de code.
5. **Les revues de code sont des discussions, pas des dictats** — Vous pouvez considérer la plupart des commentaires de revue de code comme une suggestion plutôt que comme un ordre. Il est acceptable de ne pas être d'accord avec les commentaires d'un relecteur, mais vous devez expliquer pourquoi et lui donner l'opportunité de répondre.

#### Définir les responsabilités du relecteur

Puisque le relecteur est le dernier maillon avant la fusion du code, une grande partie de la responsabilité lui incombe pour réduire les erreurs. Le relecteur doit :

1. Être conscient de la description de la tâche et des exigences.
2. S'assurer de bien comprendre le code.
3. Évaluer tous les compromis architecturaux.
4. Diviser vos commentaires en 3 catégories : Critiques, Optionnels et Positifs. Les premiers sont des commentaires que le développeur doit accepter de changer, et les derniers sont des commentaires qui permettent au développeur de connaître votre appréciation pour de beaux morceaux de code.

Également, évitez de nombreux commentaires et utilisez plutôt la revue GitHub (voir exemple ci-dessous).

![Image](https://cdn-media-1.freecodecamp.org/images/1*Dk9zXJdZRlzpapQ_ERyKwA.png)

Lorsque vous avez plusieurs commentaires, vous devez utiliser l'option de revue dans GitHub, au lieu de commenter chacun d'eux séparément, et notifier le développeur (propriétaire de la PR) lorsque vous avez terminé.

Enfin, j'ai trouvé que poser les questions suivantes est un excellent outil pour un processus de revue globalement meilleur et plus facile :

* Ai-je des difficultés à comprendre ce code ?
* Y a-t-il une complexité dans le code qui pourrait être réduite par un refactoring ?
* Le code est-il bien organisé dans une structure de package qui a du sens ?
* Les noms de classes sont-ils intuitifs et est-il évident de savoir ce qu'ils font ?
* Y a-t-il des classes qui sont particulièrement grandes ?
* Y a-t-il des méthodes particulièrement longues ?
* Tous les noms de méthodes semblent-ils clairs et intuitifs ?
* Le code est-il bien documenté ?
* Le code est-il bien testé ?
* Existe-t-il des moyens de rendre ce code plus efficace ?
* Le code respecte-t-il les normes de style de notre équipe ?

Il existe diverses pratiques efficaces et différentes de revue de code qui varient en fonction des besoins de l'équipe. Donc, supposez que ceci est mon opinion personnelle et qu'il existe d'autres moyens qui pourraient fonctionner pour votre équipe. En fin de compte, la construction d'un processus aussi sensible devrait être subjective aux objectifs de votre entreprise, à la culture de votre équipe et à la structure globale de R&D.

Si vous avez des questions ou des commentaires pour améliorer ces directives, n'hésitez pas à ajouter un commentaire ci-dessous !