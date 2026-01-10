---
title: Comment les chefs de projet et les développeurs peuvent tous deux (heureusement
  !) donner des dates de livraison réalistes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-14T15:40:50.000Z'
originalURL: https://freecodecamp.org/news/how-project-managers-and-developers-can-both-happily-give-realistic-ship-dates-2d5e4ec42df7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*I0MCeRgbNi2aHiuxUtD-cg.png
tags:
- name: Entrepreneurship
  slug: entrepreneurship
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Time management
  slug: time-management
- name: Web Development
  slug: web-development
seo_title: Comment les chefs de projet et les développeurs peuvent tous deux (heureusement
  !) donner des dates de livraison réalistes
seo_desc: 'By Roy Yuen

  Project managers (PMs) are deadline chasers. They think clients want the earliest
  possible ship date to reduce costs. But that’s a common misconception. What clients
  really want is the best possible product with the earliest possible ship...'
---

Par Roy Yuen

Les chefs de projet (PM) sont des chasseurs de délais. Ils pensent que les clients veulent la date de livraison la plus précoce possible pour réduire les coûts. Mais c'est une idée fausse courante. Ce que les clients veulent vraiment, c'est **le meilleur produit possible** avec la date de livraison la plus précoce possible.   
   
Les produits de qualité nécessitent un code bien écrit. Les développeurs devraient [utiliser les 12 approches de développement du Joel Test](https://www.joelonsoftware.com/2000/08/09/the-joel-test-12-steps-to-better-code/) pour assurer un bon contrôle de source, encourager les builds quotidiens et utiliser des testeurs QA.  
   
Les délais réalistes doivent être basés sur des estimations provenant des antécédents. Nos équipes de projet voulaient vérifier l'exactitude de nos estimations et créer une boucle de rétroaction pour nos PM et développeurs. Nous utilisons [l'ordonnancement basé sur les preuves](https://www.joelonsoftware.com/2007/10/26/evidence-based-scheduling/) (EBS) avec Fog Creek depuis deux mois, et j'aimerais partager ce que nous avons appris jusqu'à présent.

### Ordonnancement basé sur les preuves sans être OCD

Nous avons utilisé l'EBS de Fog Creek pour suivre les estimations des développeurs par rapport à leur temps réel passé sur un projet. Ces données nous ont aidés à établir de meilleurs plannings de projet et ont également fourni une boucle de rétroaction pour les PM et les développeurs afin d'améliorer leurs estimations pour les tâches individuelles.

Mais l'accent n'est pas mis sur les outils de suivi du temps OCD — nous faisons confiance à nos développeurs et PM pour saisir leurs temps dans la feuille de calcul du projet.  
   
En plus de ce que Fog Creek mentionne dans leur [article de blog sur l'EBS](https://www.joelonsoftware.com/2007/10/26/evidence-based-scheduling/), voici ce que nous avons appris dans notre mise en œuvre.

### Décomposer les projets en tâches de moins de 2 jours

![Image](https://cdn-media-1.freecodecamp.org/images/pynJTa8tOvPX88QjfGWMSgZjO6Aps7NqiJqI)
_Un modèle pour notre feuille de calcul Google pour l'EBS_

Comme je l'ai mentionné ci-dessus, notre EBS suit les estimations par rapport au temps passé pour les histoires utilisateur et les fonctionnalités. Les fonctionnalités individuelles sont décomposées en tâches (GitHub Issues) qui doivent être complétées en deux jours.

Les développeurs doivent encore cartographier exactement comment une fonctionnalité sera assemblée en créant des tâches suffisamment petites. Par exemple, plutôt que de simplement dire « Créer un panier d'achat », nous pouvons décomposer ces tâches en divers éléments, tels que « Disposer la liste des produits du panier ».  
   
Ce suivi bénéficie également à nos clients, car ils peuvent voir exactement sur quoi nous travaillons pour chaque sprint bihebdomadaire. Ils seront informés si les fonctionnalités sont complétées en avance ou en retard par rapport au planning, et il n'y aura pas de surprises.  
   
Nous suivons également les estimations de temps de nos PM, car ils ne sont pas seulement des gestionnaires de compte. Ils doivent avoir une certaine compréhension technique. Il est important pour les PM d'apprendre de leurs erreurs de calcul et d'améliorer leurs estimations futures.

En comparant leurs estimations avec celles du développeur pour la même fonctionnalité, ils peuvent poser des questions lorsqu'il y a un grand écart. Ils apprennent ce qui prend plus de temps, comment la dette technique affecte un projet et comment les choses fonctionnent mieux techniquement.  
   
Nos PM aident à trouver le juste milieu : ils donnent à leurs développeurs suffisamment de temps pour architecturer et coder correctement tout en fournissant un délai raisonnable (et un coût) aux clients.

### Suivi du temps écoulé

![Image](https://cdn-media-1.freecodecamp.org/images/XgRI8Yc9mxDrsE7n6b5JTVx5x-ftP4lUV6HO)
_Crédit : [Toggl](https://toggl.com/team-time-tracking/" rel="noopener" target="_blank" title=")_

Puisque notre entreprise a des horaires de travail flexibles, de nombreux collègues peuvent prendre des pauses café ou aller discuter. Pour l'EBS, ces pauses sont comptées dans le temps passé pour cette fonctionnalité. Certains développeurs peuvent prendre des pauses fréquentes et travailler en sprints rapides, tandis que d'autres peuvent travailler en continu pendant quatre heures.

En fin de compte, si le temps estimé et le temps réel passé sont les mêmes, alors les deux développeurs sont toujours précis. Vous pouvez vérifier vos propres estimations de travail avec l'application [Toggl](https://www.toggl.com), en laissant le minuteur allumé pendant les pauses (aussi fréquentes ou longues qu'elles soient) jusqu'à ce qu'une fonctionnalité soit terminée. Mais ce n'est pas vraiment nécessaire.  
   
Parce que de nombreuses tâches prennent au moins quelques heures, les développeurs peuvent rapidement enregistrer les problèmes qu'ils complètent quotidiennement. Des estimations telles que 0,25 jour sont suffisantes. C'est pourquoi nous n'exigeons pas de suiveurs de temps.  
   
Nous mesurons le temps estimé par rapport au temps réel passé en tant que « vélocité ». Si une estimation et le temps suivi sont les mêmes, nous lui donnons un 1. Si un développeur a terminé une tâche en 2 jours, mais a estimé qu'il faudrait 2,5 jours, sa vélocité était de 0,8, ce qui signifie qu'il a sous-estimé sa vitesse.  
   
Le but du suivi n'est pas de devenir plus rapide pour le simple plaisir. **Le but de l'EBS est la cohérence et la précision.** La cohérence signifie que les membres de l'équipe peuvent prédire les dates de livraison les uns des autres sur la base des performances passées. La précision signifie atteindre de manière cohérente une vélocité aussi proche de 1 que possible (faible plage).

### Intégration des estimations des développeurs dans les estimations de projet

![Image](https://cdn-media-1.freecodecamp.org/images/0TEIAmOyPHzBvlvWuZarxPLBee3tfPwfAQxZ)

Lorsque qu'un client vient à nous avec un projet, nos PM décomposent les fonctionnalités puis estiment combien de temps est nécessaire pour chaque fonctionnalité. En additionnant toutes les fonctionnalités, y compris les revues de code et la QA, nous pouvons donner une estimation de projet standard.   
   
L'EBS nous aide à voir comment les développeurs individuels peuvent affecter les projets. Depuis que nous avons commencé le suivi, nous avons appris des schémas intéressants. Par exemple, certains développeurs peuvent constamment surestimer leur vélocité et sont donc en retard par rapport à leurs estimations. Cependant, ils peuvent encore finir par terminer les fonctionnalités plus rapidement que la « moyenne » et être à l'heure.

Puisque ce comportement est encore prévisible, nos PM savent maintenant comment ajuster les estimations données aux clients. En revanche, si nous avions un développeur qui livrait constamment en avance, nos PM sauraient qu'ils pourraient peut-être donner aux clients une estimation plus serrée.

Cela montre simplement que les preuves sont encore meilleures que l'expérience.

### Autres observations et apprentissages de l'EBS

![Image](https://cdn-media-1.freecodecamp.org/images/NMSQ693m6Q9xxV3tWzxzLCKL4-muJwobbJYD)
_Photo par [NeONBRAND](https://unsplash.com/@neonbrand" rel="noopener" target="_blank" title=") via Unsplash_

Nous avons appris autre chose d'intéressant : les développeurs plus expérimentés n'estiment pas nécessairement mieux. Une raison possible est que nous leur déléguons des fonctionnalités complexes. Même avec une planification détaillée, il y a un haut niveau d'incertitude. Les problèmes doivent être abordés au fur et à mesure que le développement progresse.

Le but est de permettre aux développeurs et aux PM de donner un temps tampon pour les tâches qu'ils ne peuvent pas encore imaginer pleinement, et d'utiliser les estimations existantes pour les tâches courantes (comme les pages de connexion).  
   
Une autre observation est que même si chaque produit est différent, certaines tâches courantes resteront toujours aussi chronophages. Nous ne devrions pas essayer de nous précipiter pour « optimiser » juste pour réduire les coûts.  
   
L'EBS et le suivi des tâches sur une feuille de calcul nous ont également aidés à identifier rapidement les schémas de retard récurrents avec certains types de fonctionnalités.   
   
Avoir des preuves nous aide à suivre les schémas afin que nous puissions mieux comprendre nos styles de travail. Cependant, chaque projet est un nouveau projet.

Joel a montré comment les projets devraient [utiliser une simulation de Monte Carlo](https://www.joelonsoftware.com/2007/10/26/evidence-based-scheduling/), avec 100 scénarios possibles, chacun avec une probabilité de 1 %. Cela montre toute la gamme des futurs possibles pour un projet basé sur les données de vélocité historiques d'un développeur sélectionnées aléatoirement. Le but est de réduire cette plage de dates de livraison pour un client, et non de fixer une date et d'assumer une précision de 100 % à chaque fois.

L'EBS a confirmé que le développement logiciel est une probabilité.

### Réflexions finales

![Image](https://cdn-media-1.freecodecamp.org/images/nPwz4z8R0HokPPukDL7lCkclOnD5pmzE7KOO)
_Photo par [Felix Plakolb](https://unsplash.com/@felix_plakolb" rel="noopener" target="_blank" title=") via Unsplash_

Pour des raisons pratiques, nous donnons toujours aux clients une date de livraison estimée pour un projet. Nous invitons également nos clients dans des projets Basecamp afin qu'ils sachent sur quoi nous travaillons chaque semaine.   
   
Lorsque qu'une entreprise ou un développeur (y compris des collègues !) vous donne une estimation de projet, ne regardez pas seulement le nombre total de jours. Quelle que soit la durée du projet, demandez des estimations décomposées en fonctionnalités et des antécédents pour les dates de livraison des projets. Comprenez d'abord comment une équipe fait ses estimations de projet, puis intégrez cela dans la budgétisation à long terme de votre produit.

Avez-vous aimé cet article ? Si oui, cliquez sur le bouton d'applaudissements pour que plus de gens le voient. Merci !

? Chez O[ursky](https://oursky.com), nous sommes là pour aider les marques et les entrepreneurs à concrétiser leurs idées. Contactez-nous si vous cherchez un partenaire pour vous aider à construire votre prochain produit numérique.