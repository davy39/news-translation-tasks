---
title: Comment construire une évaluation précise des risques en cybersécurité
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-05-10T19:39:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-accurate-cybersecurity-risk-assessment
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/pexels-jonathan-petersson-965879.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: Security
  slug: security
seo_title: Comment construire une évaluation précise des risques en cybersécurité
seo_desc: "Are you responsible for the safety and reliability of IT infrastructure\
  \ and applications? You'll absolutely need regular and accurate assessments. \n\
  Effective risk assessments are about establishing how far your organization's IT\
  \ stack can be stretche..."
---

Êtes-vous responsable de la sécurité et de la fiabilité des infrastructures et applications IT ? Vous aurez absolument besoin d'évaluations régulières et précises. 

Les évaluations de risques efficaces consistent à déterminer jusqu'où votre pile IT peut être sollicitée avant de céder. 

D'un point de vue global, vous devrez réfléchir à la probabilité d'être touché par, par exemple, une attaque par ransomware qui pourrait rendre vos serveurs métiers inutilisables pendant quelques semaines – et à quel point cela vous coûterait en termes de pertes de revenus et de coûts de mitigation. 

Cet article provient de mon [cours d'introduction à la cybersécurité](https://www.udemy.com/course/intro-cyber-security-framework-planning/?referralCode=23853458BE14AFFAEFF2). Si vous le souhaitez, vous pouvez suivre la version vidéo ici :

%[https://www.youtube.com/watch?v=7JfuMdevhu4&list=PLSiZCpRYoTZ5dys7oy4ReI-ltW0jnGTMO&]

En face de cela, vous pourriez mesurer les coûts initiaux et continus associés aux sauvegardes et aux efforts de durcissement du système. Cela vous indiquera combien vous pouvez réellement vous permettre, et aussi à quel point vous devriez travailler de manière urgente pour développer un plan de défense global.

Vous voudrez également avoir une idée de l'interdépendance de vos systèmes : si, par exemple, vos applications web accessibles au public tombaient en panne, cela affecterait-il également vos systèmes de paie et d'inventaire en back-end ? 

Avez-vous suffisamment d'ingénieurs disponibles dans votre organisation qui pourraient être retirés de leur travail habituel pour couvrir une urgence ? Pourriez-vous être soumis à des responsabilités légales et à des poursuites judiciaires coûteuses à la suite d'une panne ? 

À quel moment les dommages causés par une panne majeure seraient-ils si graves qu'ils menaceraient la viabilité continue de vos opérations ?

Ce dernier point mérite d'être approfondi. Il s'avère que le monde de l'administration IT a développé des métriques particulièrement utiles pour mesurer les besoins de base de votre organisation et anticiper les étapes que vous devrez franchir pour garantir que ces besoins sont satisfaits. 

Je sais que cette liste ressemble à une soupe d'alphabet, mais il sera utile de consacrer un peu de temps à discuter brièvement de chacun de ces concepts.

* RPO : Objectif de Point de Récupération
* RTO : Objectif de Temps de Récupération
* MTTR : Temps Moyen de Récupération
* MTBF : Temps Moyen Avant Défaillance
* MTTF : Temps Moyen Jusqu'à la Défaillance

### Objectif de Point de Récupération (RPO)

L'**objectif de point de récupération** mesure la quantité de perte de données que vous pourriez subir avant que la récupération complète ne devienne impossible. Nous regardons ici en arrière à partir du moment où vous restaurez les opérations. 

Le point est que le monde a continué de tourner pendant que vos serveurs dormaient. Les clients ont essayé d'accéder à votre site, mais n'ont pas pu compléter les transactions. 

Cela représente une perte financière. Mais il pourrait également y avoir eu des clients existants qui utilisaient activement des versions locales de votre application sans réaliser que les données qu'ils généraient n'étaient pas correctement capturées par votre back-end.

Donc, _vous_ voulez savoir approximativement combien de données et de revenus vous traitez normalement en une heure, et combien d'heures de données et de revenus vous pouvez vous permettre de perdre. Avec ce chiffre, vous serez en mesure de déterminer à quelle vitesse votre plan de réponse et de récupération devra fonctionner pour être utile.

### Objectif de Temps de Récupération (RTO)

Cela nous amène à l'**objectif de temps de récupération** : combien de temps il vous faudra pour passer d'un état défaillant à des opérations entièrement restaurées. 

Si vos estimations de RTO pour un type de panne particulier sont, par exemple, de 12 heures, mais que votre objectif de _point_ de récupération n'est que de six heures, alors vous avez un problème. À quoi sert un plan de récupération coûteux si vous savez déjà que votre entreprise sera morte et enterrée au moment où il se terminera ? 

Si c'est ce que vos chiffres vous disent à propos de votre plan de récupération coûteux actuel, alors vous feriez mieux de commencer à travailler sur un plan de récupération _plus_ coûteux – ou plus efficace.

### Temps Moyen de Récupération (MTTR)

Si le RTO est un moyen de quantifier votre temps de réponse **cible** pour un seul événement de catastrophe hypothétique, le **temps moyen de récupération** nous donne une idée de la manière dont votre technologie se comportera réellement dans le monde réel. 

Votre MTTR pourrait être au moins partiellement basé sur les garanties de performance fournies par les fournisseurs qui fournissent les divers composants matériels et logiciels qui constituent votre pile. Mais je suppose qu'il dépendra principalement de l'historique de performance de vos équipes d'urgence. 

Encore une fois : un MTTR plus long que votre RPO est un signal que vous devez accorder une attention particulière à cela.

Outre ces métriques, il peut également être utile de réfléchir à la défaillance. Bien sûr, je ne veux pas dire à quel point les choses pourraient devenir désagréables si vous êtes celui qui laisse l'authentification de l'attaque par ransomware passer. Il n'est peut-être pas sain de passer trop de temps à obséder sur ce point. Plutôt, je veux dire réfléchir à la fréquence à laquelle vos systèmes sont susceptibles de tomber en panne.

Certains événements de défaillance ne sont pas difficiles à prédire. Vous savez, par exemple, que vous devrez remplacer complètement vos serveurs exécutant Ubuntu 20.04 d'ici la fin de sa [durée de vie des mises à jour matérielles et de maintenance en avril 2025](https://ubuntu.com/about/release-cycle). 

Sauf si, bien sûr, vous optez pour une option de maintenance de sécurité prolongée, auquel cas vous aurez jusqu'en avril 2030. De même, vous pouvez être raisonnablement certain que les disques de données fortement utilisés commenceront à tomber en panne après quelques années de service.

Mais les événements de logiciels malveillants ne se produisent pas selon un calendrier. Et, perversement, ils tendent à éclater lors des longs week-ends ou au milieu de la nuit. 

Ici, vous devrez travailler avec des données d'incidents disponibles publiquement provenant de gouvernements et d'entreprises de sécurité. Étant donné le nombre de violations non signalées, même ces chiffres ne vous rapprocheront probablement pas trop de la réalité.

L'objectif sera d'estimer combien de temps vos organisations _paires_ passent entre les événements majeurs. Une "organisation paire" est une organisation qui est largement similaire à la vôtre en termes de taille et de type d'industrie. Dans ce contexte, le temps moyen _avant_ la défaillance est généralement utilisé pour mesurer les temps de récupération des défaillances _réparables_. Cela peut vous aider à comprendre votre pile technologique – et particulièrement comment chaque couche fonctionnera sous stress dans l'ensemble.

### Temps Moyen Jusqu'à la Défaillance (MTTF)

En revanche, le **temps moyen _jusqu'à_ la défaillance** se concentre sur les défaillances _ir_réparables qui nécessitent le remplacement complet d'un composant ou d'un système. Dans l'ensemble, le MTTF sera la métrique la plus intéressante dans le contexte des menaces d'attaque.

Il y aura évidemment quelques conjectures avec tout cela, mais il est crucial de développer au moins un sens informé de la manière dont vous êtes susceptible de performer lorsque les choses deviennent folles et de la préparation réelle que vous avez pour les défis de continuité des activités.

## Conclusion

Avoir même une compréhension de base des processus et des métriques derrière les acronymes RPO, RTO, MTTR, MTBF et MTTF que nous avons discutés ici devrait vous donner une bonne chance de lutter avec succès contre le chaos.

Cet article et la vidéo qui l'accompagne sont extraits de [mon](https://www.udemy.com/course/intro-cyber-security-framework-planning/?referralCode=23853458BE14AFFAEFF2) **[cours d'introduction à la cybersécurité](https://www.udemy.com/course/intro-cyber-security-framework-planning/?referralCode=23853458BE14AFFAEFF2).** Et il y a beaucoup plus de bonnes choses technologiques disponibles sur [bootstrap-it.com](https://bootstrap-it.com)