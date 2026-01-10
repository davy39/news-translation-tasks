---
title: Comment organiser une excellente Revue de Sprint – Conseils pratiques pour
  les développeurs et les équipes
subtitle: ''
author: Ben
co_authors: []
series: null
date: '2025-01-29T17:02:01.052Z'
originalURL: https://freecodecamp.org/news/how-to-run-a-great-sprint-review-actionable-insights
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1738170100236/fcc7407a-3b08-493f-a704-661eed12f369.png
tags:
- name: agile
  slug: agile
- name: Scrum
  slug: scrum
- name: planning
  slug: planning
seo_title: Comment organiser une excellente Revue de Sprint – Conseils pratiques pour
  les développeurs et les équipes
seo_desc: 'In my twenty years of being in the Software Engineer game, I’ve been through
  lots of Sprint Reviews. I’ve seen them done well, and I’ve seen them used as no
  more than a few hours every sprint for people to take a nice break in a meeting
  room.

  When do...'
---

En vingt ans de carrière dans le domaine de l'ingénierie logicielle, j'ai participé à de nombreuses Revues de Sprint. J'en ai vu des bien menées, et d'autres utilisées simplement comme une pause de quelques heures dans une salle de réunion.

Lorsque bien menée, la Revue de Sprint peut être essentielle pour maintenir votre projet sur la bonne voie. Mais une Revue de Sprint mal menée est pire que le simple temps perdu – elle réduit également la confiance des gens dans Scrum dans son ensemble.

Dans cet article, je vais vous guider à travers des idées claires et étape par étape pour rendre votre Revue de Sprint plus précieuse.

## **Qu'est-ce qu'une Revue de Sprint ?**

Une **Revue de Sprint** est une courte session organisée à la fin de chaque sprint, généralement toutes les deux semaines.

Elle permet à l'équipe de montrer ce qu'elle a accompli via des démonstrations, de recueillir des retours et de décider des prochaines étapes.

Lorsque bien menée, la Revue de Sprint montre les progrès et renforce la confiance des parties prenantes dans le produit et le projet.

Bien sûr, vous pouvez dire aux parties prenantes que vous êtes sur la bonne voie, mais si elles peuvent le voir de leurs propres yeux lors de la Revue de Sprint, elles seront beaucoup plus satisfaites.

## Qui doit participer à la Revue ?

En bref, toute personne qui le souhaite. Toute personne ayant un intérêt dans le projet, à quelque titre que ce soit, peut et doit assister aux réunions.

L'équipe Scrum elle-même est au cœur de la réunion, mais il peut également y avoir des membres des ventes, de la direction, d'autres équipes Scrum et des chefs de projet.

En résumé, si quelqu'un peut apporter une contribution utile à un projet ou tirer profit de l'apprentissage de quelque chose sur un projet, il doit assister à la réunion.

## Que faire avant la Revue

Pour que la réunion se déroule aussi facilement que possible, vous devez vous assurer que toutes les personnes présentant sont prêtes et ont une démonstration prête à montrer.

D'après mon expérience, les démonstrations en direct ne fonctionnent pas. Enfin, parfois elles fonctionnent, mais la plupart du temps, non.

Demandez aux personnes qui ont une démonstration d'enregistrer au moins leur workflow avant la réunion. Ainsi, si elles insistent pour faire une démonstration en direct, elles auront une vidéo enregistrée en secours si quelque chose ne va pas.

Vous devriez également avoir un ordre de passage. Sachez qui présente, dans quel ordre, et regroupez-les par similitude de sujet. L'ordre de passage et les présentateurs n'ont pas vraiment d'importance tant que les présentations sont regroupées par sujet.

Par exemple, si vous avez six ingénieurs – deux travaillant sur une page de connexion, deux sur un nouveau service back-end et deux sur la performance de la base de données – assurez-vous que votre ordre de passage regroupe ces trois domaines distincts.

Si deux démonstrations sont assez similaires, vous pouvez expliquer le contexte une fois, puis enchaîner les deux démonstrations. Soyez efficace, car il y a beaucoup de monde dans cette réunion et tout le monde sait que [les réunions sont coûteuses](https://calculatorlord.com/meeting-cost-calculator/).

## Pendant la Revue

Les ingénieurs logiciels qui ont terminé un travail présenteront leur travail aux autres membres de l'équipe Scrum (Product, QA, etc.) ainsi qu'à toutes les parties prenantes présentes.

Après chaque présentation d'un ingénieur, toute personne dans la salle est libre de poser des questions ou de faire des commentaires sur le travail/la présentation.

Ces questions peuvent simplement servir à combler des lacunes de connaissances pour les personnes moins informées sur le projet, ou elles peuvent porter sur les raisons pour lesquelles une solution particulière a été choisie.

Les membres de l'audience plus orientés vers les aspects métiers ou produits peuvent maintenant donner leur avis sur le fait que ce qui a été démontré correspond à l'intention métier de ce qui avait été demandé.

Une fois toutes les questions et commentaires traités, l'ingénieur suivant présentera son travail.

Lors d'une Revue de Sprint, tout le monde est encouragé à parler, mais généralement, seuls les ingénieurs présentent. Ainsi, l'ingénieur présentera ce sur quoi il a travaillé, puis les membres Product, QA, BA, etc., pourront donner leur avis et poser des questions spécifiquement sur ce que l'ingénieur a présenté.

## Exemple de Revue

Examinons un exemple de revue et ce à quoi cela pourrait ressembler.

Nous utiliserons l'exemple précédent de six ingénieurs : deux travaillant sur une page de connexion, deux sur un service back-end et deux sur la performance de la base de données. Dans ce cas, vous pourriez avoir un ordre de passage comme suit :

Présentations :

1. Larry : *L'utilisateur dépasse le nombre maximal de tentatives de connexion et le compte utilisateur est verrouillé après le cinquième mot de passe incorrect. L'utilisateur doit réinitialiser son mot de passe avant de pouvoir se connecter à nouveau.*

2. David : *L'utilisateur clique sur le lien "mot de passe oublié" et un lien est envoyé à son adresse e-mail. L'utilisateur suit ce lien et peut réinitialiser son mot de passe.*

3. Premilla : *Le service de reporting consomme l'événement "L'utilisateur a dépassé le nombre maximal de tentatives de connexion" et le publie sur le tableau de bord de reporting.*

4. Akshat : *Le service de reporting consomme l'événement "L'utilisateur a cliqué sur le lien mot de passe oublié" et le publie sur le tableau de bord de reporting.*

5. Olga : *Un utilisateur administrateur peut consulter le tableau de bord de reporting pour un mois et charger le rapport en moins de 3 secondes.*

6. Trevor : *Un utilisateur administrateur peut consulter les événements de plusieurs utilisateurs combinés dans un seul tableau de bord et charger le rapport en moins de 2 secondes.*

Comme vous pouvez le voir ici, les deux histoires utilisateur de la page de connexion sont démontrées en premier, puis les deux histoires du service de reporting, et enfin les deux histoires sur la vitesse de la base de données. Cela nécessite moins de changements de contexte pour les membres de l'audience et signifie que le contexte ne doit être donné qu'au début de la première des deux histoires regroupées (c'est-à-dire les présentations 1, 3 et 5).

Après la présentation 1 (par Larry), le Product peut demander pourquoi il a choisi 5 tentatives comme nombre maximal de tentatives avant de verrouiller le compte. Larry peut avoir une réponse, ou non. Le Product peut soit demander un suivi ultérieur pour découvrir quelle est la norme de l'industrie et l'appliquer à la logique de Larry, soit simplement la laisser telle quelle.

Après chacune des six présentations, il peut y avoir des questions, des commentaires et des demandes de changement de la part de toute personne dans l'audience. Cela déclenche généralement une conversation parmi l'audience sur la meilleure approche.

Par exemple, dans le cas de Larry, certains peuvent soutenir qu'ils ne devraient même pas utiliser un nom d'utilisateur et un mot de passe, mais plutôt une adresse e-mail et un [lien magique](https://www.pingidentity.com/en/resources/blog/post/what-is-magic-link-login.html). C'est là toute la beauté de la revue. Vous avez beaucoup de personnes intelligentes dans une salle qui apportent leur propre expérience et expertise.

## **Conseils pratiques**

Voici quelques conseils sur ce qu'il faut montrer, comment le montrer et ce qui compte vraiment pendant la réunion elle-même.

### 1. Présenter des livrables réels

Tout d'abord, présentez toujours un logiciel fonctionnel ou un travail terminé plutôt que des diapositives statiques. Par exemple, si vous avez développé une nouvelle fonctionnalité de connexion, faites une démonstration en direct. Cela rend la revue plus authentique et montre des progrès tangibles.

### 2. Encourager les retours ouverts

Ensuite, invitez les questions de tout le monde. Rappelez aux parties prenantes que leurs idées peuvent aider à façonner le travail futur. Notez leurs suggestions et confirmez si des changements doivent être directement intégrés à votre backlog.

### 3. Garder un format clair et structuré

Troisièmement, maintenez un format simple. Par exemple, commencez par un bref aperçu de l'objectif du sprint, passez aux démonstrations et terminez par une courte discussion sur les prochaines étapes.

Évitez d'entrer trop dans les détails techniques. Si un sujet nécessite plus de temps, organisez une discussion de suivi.

### 4. S'aligner sur les prochaines étapes

Ensuite, mettez à jour votre backlog en fonction de ce que vous avez appris. Si une fonctionnalité nécessite un ajustement supplémentaire, ajoutez cette tâche immédiatement.

Cela aide l'ensemble du groupe à rester informé du plan pour le sprint à venir.

### 5. Garder la réunion courte et terminer à l'heure

Vous devriez passer en revue le travail d'une équipe Scrum pour un sprint (deux ou trois semaines).

Si vos réunions s'éternisent, cela signifie soit que votre équipe Scrum est trop grande (auquel cas, vous devriez penser à diviser votre équipe Scrum en [équipes plus petites](https://namegenerators.online/scrum-team-name-generator/)), soit que vous n'êtes pas assez efficace avec vos démonstrations.

Le temps et l'attention des gens sont précieux et limités. Limitez les réunions à pas plus d'un [cycle ultradien](https://en.wikipedia.org/wiki/Basic_rest%E2%80%93activity_cycle). Personnellement, j'essaie de limiter toutes les réunions que je dirige à un maximum de 90 minutes.

Enfin, fixez une limite ferme pour la réunion afin que les participants se sentent en confiance pour apporter leurs retours sans prolonger la discussion.

Terminer à l'heure respecte l'emploi du temps de chacun et maintient l'équipe en forme pour le prochain sprint.

## **En résumé**

Une Revue de Sprint donne aux parties prenantes un aperçu en temps réel du travail accompli, assure l'alignement sur les prochaines étapes et recueille les retours nécessaires pour développer efficacement votre produit.

Si vous vous concentrez sur la présentation de réels progrès, en invitant à un dialogue ouvert et en gardant les choses concises, vous verrez une amélioration constante dans la manière dont votre équipe livre.

*Dans son temps libre, Ben écrit son blog tech* [*Just Another Tech Lead*](https://justanothertechlead.com/) *et gère un site créant des calculateurs en ligne gratuits à vie sur* [*CalculatorLord.com*](https://calculatorlord.com/)*.*