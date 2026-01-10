---
title: Comment appliquer le Framework Agile aux projets de Data Science
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-28T07:22:33.000Z'
originalURL: https://freecodecamp.org/news/applying-agile-methodology-to-data-science-projects
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/1_AZ_AWktR7nuirzHudbFimA.png
tags:
- name: agile
  slug: agile
- name: clients
  slug: clients
- name: customer
  slug: customer
- name: Data Science
  slug: data-science
- name: project management
  slug: project-management
seo_title: Comment appliquer le Framework Agile aux projets de Data Science
seo_desc: 'By Black Raven

  In this article, we''ll discuss how agile principles and values can be applied to
  the way you approach data science projects.

  Project management methodologies are commonly used to get projects done or get a
  product (often referred to as...'
---

Par Black Raven

Dans cet article, nous discuterons de la manière dont les principes et valeurs agiles peuvent être appliqués à la façon dont vous abordez les projets de data science.

Les méthodologies de gestion de projet sont couramment utilisées pour mener à bien des projets ou produire un produit (souvent appelé outil). Ce sont, en général, des processus et des frameworks qui décomposent l'objectif global en tâches individuelles organisées sur une timeline. Cela peut être adapté et utilisé pour aborder les projets de data science.

Par le passé, la méthodologie traditionnelle [**Waterfall**](https://en.wikipedia.org/wiki/Waterfall_model) (remontant à 1970) a été très populaire. Elle définit tous les besoins et paramètres du produit dès le début, afin que l'équipe de projet puisse travailler vers cet objectif en phases séquentielles.

Cette méthode a été couronnée de succès dans l'industrie manufacturière où les spécifications des produits varient rarement avec le temps. Elle nécessite une planification préalable très extensive, et idéalement, le produit final est exactement le même que celui spécifié au début.

Mais la méthodologie Waterfall a commencé à devenir inadaptée pour les projets logiciels. Pour cette raison, de nombreuses [méthodologies populaires de gestion de projet](https://thedigitalprojectmanager.com/project-management-methodologies-made-simple/) ont émergé au fil des ans, en particulier dans l'industrie du développement logiciel. Permettez-moi de partager la plus populaire.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/1_5QuiHM9Tp1RnKfVFiIk2fg.png)
_Waterfall vs Agile. Figure par l'Auteur._

## Framework Agile

[Agile](https://en.wikipedia.org/wiki/Agile_software_development) est une manière de travailler développée en 2001, et est largement utilisée pour gérer les projets de développement logiciel. Elle est adaptée aux cycles de développement rapides et prévoit des spécifications changeantes tout au long du processus de conception et de construction. Elle est flexible et vise une amélioration incrémentale itérative du produit grâce à la collaboration d'équipe. En bref, Agile consiste à planifier, construire, tester, apprendre et répéter.

Les équipes Agile sont réactives aux exigences imprévisibles à mesure que le projet se déroule, grâce à des processus de travail itératifs. Voici les [**principes Agile**](https://agilemanifesto.org/principles.html) qui servent de cadre (guide) à la manière de travailler :

* Satisfaction du client par une livraison précoce et continue de logiciels
* Accommodation des exigences changeantes tout au long du processus de développement
* Livraison fréquente de logiciels fonctionnels, car le logiciel fonctionnel est la principale mesure de progression
* Collaboration et interaction entre les parties prenantes commerciales (client) et les développeurs (fournisseur) tout au long du projet, y compris la communication en face à face au sein de l'équipe de développement
* Soutien, confiance et motivation des personnes impliquées
* Frameworks Agile pour soutenir un rythme de développement constant
* Attention aux détails techniques et à la conception améliore l'agilité
* Simplicité dans la recherche de solutions
* Réflexions régulières dans l'équipe auto-organisée sur la manière de devenir plus efficace

Les projets Agile sont caractérisés par une série de tâches qui sont conçues, exécutées et adaptées en fonction des exigences de la situation. Cependant, l'accent d'Agile n'est pas mis sur ce qu'il faut faire, mais sur **comment penser**. Agile valorise et place la [**priorité**](https://agilemanifesto.org/) sur :

* Les individus et les interactions (plutôt que les processus et les outils)
* Les logiciels fonctionnels (plutôt que la documentation exhaustive)
* La collaboration avec le client (plutôt que la négociation contractuelle)
* La réponse au changement (plutôt que le suivi d'un plan rigide prédéfini)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/1_aaIzYNWVd7LDnmzV6VBP5g.png)
_Méthode de travail Agile. Figure par l'Auteur._

## Pratiques Agile et Data Science

Bien que les principes et priorités Agile soient employés pour une plus grande productivité, la plupart d'entre eux peuvent être exploités pour les projets de data science (DS).

De plus, les data scientists ne savent pas comment planifier le projet car il est impossible de déterminer une timeline spécifique pour le type de "recherche" et de travail exploratoire. La plupart des projets DS nécessitent des essais et des erreurs en empruntant différents chemins et en essayant différentes techniques. Ils n'ont pas d'élément de certitude dans le résultat, donc Agile peut être utilisé pour diriger le flux de travail.

La plupart des autres projets traitent de ce que les clients veulent, de ce que les développeurs veulent et de ce que l'entreprise recherche. En travaillant avec la DS, une autre perspective est ajoutée : **ce que les données vous disent**.

Les data scientists ne peuvent rien comprendre aux données à moins de développer une compréhension de base. Il y a beaucoup d'investigation, d'exploration, de tests et de réglages. Agile utilise le concept d'itération et de feedback constant afin d'affiner un système en développement, afin de monter dans la **Pyramide de Valeur des Données**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/1_A1HnvWOiFiubgYJH1Wo3Gw.png)
_Pyramide de Valeur des Données. Figure par l'Auteur._

Lorsque l'on travaille sur des projets DS, les insights ne sont pas immédiatement réalisables. Plusieurs itérations sont nécessaires avant que des insights puissent être découverts.

### Comment les pratiques agiles peuvent être appliquées

Je vais expliquer les principales pratiques de travail Agile ([**Scrum framework**](https://en.wikipedia.org/wiki/Scrum_(software_development))), et comment elles peuvent être appliquées à la DS :

**Définir le besoin commercial et l'objectif du projet**. Cela est généralement piloté par le propriétaire du produit qui est responsable des fonctionnalités et de la qualité du produit. Il s'agit des grandes lignes, mais c'est la croyance centrale à laquelle vous vous référerez tout au long de la construction.

En DS, le propriétaire du produit pourrait être le client, l'entreprise ou le client final (par exemple, l'utilisateur final d'un outil de prédiction). Comprenez les problèmes auxquels le propriétaire du produit est confronté et adaptez la proposition de projet pour répondre à ses besoins.

**Construire le backlog**. En se concentrant sur les exigences des utilisateurs ("user stories" en Agile), une liste de tâches est dérivée que vous devez accomplir pour construire des fonctionnalités de produit ou améliorer les performances du produit.

L'équipe DS construit le backlog avec le propriétaire du produit pour déterminer les fonctionnalités du produit et les cibles de performance. Le backlog pourrait commencer par l'obtention des données de manière structurée avant qu'elles puissent être analysées. Ensuite, cela pourrait être une liste pour la sélection de fonctionnalités ou l'ingénierie de fonctionnalités, ou une liste de modèles à sélectionner, ajuster et optimiser.

**Prioriser le backlog**, identifier les tâches du backlog qui apporteront le plus de valeur avec le moins d'effort.

En DS, toutes les approches ne valent pas la peine d'être essayées, donc couvrez d'abord les plus prometteuses. Lorsque les principales sont réalisées, vous pourriez constater que les autres restantes ne sont pas aussi importantes qu'initialement pensé.

**Faire un sprint** (le travail de développement réel). Les sprints sont généralement des cycles de deux semaines où les tâches de haute priorité du backlog sont travaillées.

En DS, chaque sprint pourrait durer de deux à quatre semaines selon la taille de l'équipe. Pendant le sprint, terminez toujours la tâche de la plus haute priorité avant de passer à la suivante.

**Avoir des standups quotidiens**. Les réunions standup sont pour que les membres de l'équipe soient responsables les uns envers les autres de leur progression dans le sprint actuel. Chaque membre de l'équipe prend à tour de rôle pour rapporter son statut — ce qui a été fait la veille, ce qu'il faut faire aujourd'hui, tout obstacle potentiel. La communication la plus efficace se produit lorsque les membres de l'équipe DS se rencontrent en face à face pour partager leur travail.

**Revoir la sortie du sprint** (réunion rétrospective de sprint). À la fin des deux semaines, il devrait y avoir une sortie fonctionnelle pour que l'équipe de projet démontre, avec une amélioration incrémentale du produit.

Les data scientists devraient partager les sorties avant d'essayer de perfectionner les processus. Obtenez des feedbacks des parties prenantes du client et préparez-vous pour le prochain sprint. Le feedback régulier est un principe clé pour la méthode Agile d'amélioration incrémentale itérative.

**Préparer le prochain sprint**. Identifier les tâches qui se passent bien et continuer à les faire, et identifier celles qui sont des obstacles à éliminer.

Il est important de comprendre que, contrairement au développement logiciel, la DS est plus basée sur l'expérimentation que sur les tâches. La DS aide à explorer les données, elle doit donc être traitée comme plusieurs expériences de recherche. Une fois de plus, construisez et priorisez le backlog afin que le prochain sprint puisse être réalisé, pour travailler sur les prochaines zones d'amélioration.

**Déployer le produit final**. Lorsque toutes les parties prenantes conviennent qu'aucune amélioration supplémentaire n'est nécessaire dans le produit, il est prêt pour le déploiement final.

Les projets DS suivent la "loi de l'amélioration décroissante". Par exemple, si un modèle a atteint 70 % de précision, les 5 à 10 % d'amélioration suivants prendront beaucoup plus d'efforts qu'avant, et cela dépend également des limitations de l'ensemble de données. Décidez en équipe si les efforts valent l'amélioration incrémentale.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screenshot_1-2.jpg)
_Photo par [Unsplash](https://unsplash.com/@youxventures" rel="noopener">You X Ventures</a> sur <a href="https://unsplash.com/photos/Oalh2MojUuk" rel="noopener)_

## Défis avec le client

Outre une communication adéquate entre l'équipe DS et le client, les attentes du client doivent être gérées.

Tous les clients aiment généralement l'idée qu'Agile est flexible et qu'il leur offre plus d'opportunités de changer d'avis à mesure que le projet se développe. Cependant, ils ne réalisent peut-être pas que cette flexibilité est également coûteuse en temps et en argent. Voici quelques choses que vous devriez faire :

### Le coût de la flexibilité

Faites comprendre au client que **la flexibilité est inévitablement coûteuse**. C'est comme un billet d'avion en classe économique flexible qui permet des changements d'itinéraire coûtera beaucoup plus cher que le billet fixe. Faire des changements signifie également que le client paie pour le temps et les efforts gaspillés dans le passé.

### Définir les attentes

Définissez les attentes du client pour qu'il s'engage à consacrer du temps à des **réunions rétrospectives de sprint** fréquentes (par exemple, toutes les deux semaines) afin d'évaluer les sprints terminés.

En outre, le représentant du client dans chaque réunion doit être (**autonomisé** par la direction supérieure) capable de prendre des décisions sur les spécifications du produit. Pour qu'Agile fonctionne, le client doit fournir un feedback continu et définir des priorités pour maintenir le projet en mouvement.

### La confiance est importante

Gagnez la **confiance** du client et montrez-lui que chaque itération est réalisée avec les meilleurs efforts possibles pour livrer de la valeur et améliorer le produit.

Tout en détenant le pouvoir de décision, le client s'attend également à ce qu'une itération apporte une amélioration considérable.

Un tel déséquilibre de responsabilité dans la relation client-fournisseur doit être converti en une confiance mutuelle et une volonté d'expérimenter ensemble. Le principe d'Agile en matière de **collaboration** signifie qu'il s'agit d'un effort d'équipe à la fois pour prendre des décisions et livrer de la valeur.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screenshot_2.jpg)
_Photo par [Unsplash](https://unsplash.com/@youxventures" rel="noopener">You X Ventures</a> sur <a href="https://unsplash.com/photos/6awfTPLGaCE" rel="noopener)_

## Produit Minimum Viable

Une caractéristique clé de la méthode de travail Agile est le développement d'un produit minimum viable (**MVP**). Il s'agit de la **configuration la plus fondamentale du produit** (ou outil).

Après que les objectifs du projet ont été définis, l'équipe fait une proposition concernant l'approche du problème. Cela inclut la construction du MVP dans le laps de temps le plus court possible (comme un mois pour les projets DS). Le MVP n'a que les fonctionnalités les plus importantes, mais ses performances peuvent ne pas être les plus optimales.

Cela peut sembler très risqué — mettre une version moins que terminée à l'essai pour le client. Donc l'équipe (y compris le client) doit être préparée à cela. Le but est de faire fonctionner le MVP, de le tester et de voir s'il va vraiment dans la bonne direction pour résoudre le problème et aider le cas commercial.

Le MVP va s'améliorer, car l'équipe DS va utiliser ce qu'elle a appris des feedbacks du MVP pour construire une version améliorée. Agile consiste à déployer continuellement et à apprendre de ses erreurs, et à travailler avec le client pour améliorer le produit.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/0_Su_JCisEQJnWBB52.png)
_Nature itérative d'Agile. Figure prise de <a class="bw cu jf jg jh ji" target="_blank" rel="noopener" href="https://towardsdatascience.com/data-science-agile-cycles-my-method-for-managing-data-science-projects-in-the-hi-tech-industry-b289e8a72818" style="box-sizing: inherit; color: inherit; text-decoration: none; -webkit-tap-highlight-color: transparent; background-repeat: repeat-x; background-image: url(&quot;data:image/svg+xml;utf8,<svg preserveAspectRatio=\&quot;none\&quot; viewBox=\&quot;0 0 1 1\&quot; xmlns=\&quot;http://www.w3.org/2000/svg\&quot;><line x1=\&quot;0\&quot; y1=\&quot;0\&quot; x2=\&quot;1\&quot; y2=\&quot;1\&quot; stroke=\&quot;rgba(0, 0, 0, 0.84)\&quot; /></svg>&quot;); background-size: 1px 1px; background-position: 0px calc(1em + 1px);">TowardsDataScience</a>._

> Agile consiste à planifier, construire, tester, apprendre et répéter.

## Livrable du projet DS

La méthode de travail Agile permet aux data scientists de prioriser et de créer des feuilles de route basées sur les exigences et les objectifs. Avec chaque itération, les data scientists peuvent apprendre quelque chose de nouveau, obtenir des résultats plus affinés et les utiliser pour la prochaine amélioration incrémentale.

Voici quelques livrables de projet Agile pour façonner et guider le processus de projet :

* **Déclaration de vision du projet** : Un résumé qui articule les objectifs du projet.
* **Feuille de route du projet** : La vue d'ensemble des exigences nécessaires pour atteindre la vision du projet.
* **Backlog du projet** : Ordonné par priorité, il s'agit de la liste complète de ce qui est nécessaire pour soutenir votre projet.
* **Plan de release** : Un calendrier pour la sortie d'un produit fonctionnel (ou outil), mais pas de documentation. Les projets doivent être auto-documentés en cours de route.
* **Backlog du sprint** : Les user stories (exigences), objectifs et tâches liés au sprint actuel.
* **Incrément** : La fonctionnalité du produit en cours de travail qui est présentée aux parties prenantes à la fin du sprint et qui pourrait potentiellement être donnée au client. L'objectif n'est pas de livrer plus, mais d'obtenir une sortie de _valeur plus élevée_.

## Résumé

Agile va être adopté par de plus en plus d'équipes de projets DS dans un avenir proche. De nombreux data scientists ont rapporté que cela les rend plus productifs.

Ce n'est pas parce que les data scientists sont devenus plus qualifiés, mais parce qu'Agile peut les aider à optimiser leurs projets. Au lieu de passer du temps sur des modèles qui sont peu susceptibles de révéler des résultats productifs, il est préférable de consacrer ce temps à d'autres fins axées sur les résultats.

Être "agile" (flexible) signifie que vous devez adopter une approche dynamique dans la planification et être adaptable aux besoins changeants de la nouvelle situation lorsqu'elle se présente.

**L'environnement Agile prône l'action rapide, l'échec rapide, la discussion et l'évaluation, puis une nouvelle tentative en utilisant une approche différente ou une méthode améliorée.** Cela fonctionne très bien dans des environnements dynamiques où il y a un potentiel pour des exigences changeantes ou évolutives.

Bonne chance pour vos projets DS !

Référence :
[Data-science ? Agile ? Cycles ? Ma méthode pour gérer les projets de data-science dans l'industrie high-tech.](https://towardsdatascience.com/data-science-agile-cycles-my-method-for-managing-data-science-projects-in-the-hi-tech-industry-b289e8a72818)