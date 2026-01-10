---
title: Comment mettre en place une boucle de rétroaction courte en tant que développeur
  solo
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2018-07-13T21:30:46.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-a-short-feedback-loop-as-a-solo-coder-67709cba21e0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*pmBhfr3r0VgXfvG_9Uu1pQ.png
tags:
- name: goal-setting
  slug: goal-setting
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment mettre en place une boucle de rétroaction courte en tant que développeur
  solo
seo_desc: I’ve spent the last couple years as a solo freelance developer. Comparing
  this experience to previously working in companies, I’ve noticed that those of us
  who work alone can have fewer iterative opportunities for improvement than developers
  who work...
---

J'ai passé les dernières années en tant que développeur freelance solo. En comparant cette expérience à mon travail précédent en entreprise, j'ai remarqué que ceux d'entre nous qui travaillent seuls peuvent avoir moins d'opportunités itératives d'amélioration que les développeurs qui travaillent en équipe.

Pour avoir l'opportunité de s'améliorer, nous devons adopter le concept de boucle de rétroaction courte. Il s'agit d'un processus d'incorporation continue de nouveaux apprentissages issus de l'observation et de l'expérience précédente sur une courte période. Ce processus doit être **créé** par les personnes travaillant principalement seules, au lieu d'être **adopté**, comme c'est souvent le cas, lorsque l'on rejoint une équipe.

Dans cet article, j'espère partager ce que j'ai appris sur la mise en place pour s'améliorer rapidement et continuellement en tant que développeur solo.

### À propos des boucles de rétroaction

Le colonel John Boyd de l'US Air Force a développé le concept de la [boucle OODA](https://en.wikipedia.org/wiki/OODA_loop), OODA étant l'acronyme de **observer, s'orienter, décider, agir**. Dans les opérations militaires, cela illustre un processus de prise de décision basé sur l'ingestion constante de nouvelles informations :

**Observer** : Obtenir des informations brutes sur les circonstances en évolution et l'environnement actuel.

**S'orienter** : Mettre les observations brutes en contexte. Tenir compte de la pertinence par rapport à la situation actuelle et des connaissances et de l'expertise précédemment acquises.

**Décider** : Élaborer un plan pour atteindre son objectif.

**Agir** : Exécuter le plan.

Puisqu'il s'agit d'une boucle, l'étape **agir** mène directement à l'étape **observer**. C'est le concept critique de "rétroaction" qui permet des itérations de plus en plus réussies. Il est largement applicable au-delà des opérations militaires — vous pouvez le reconnaître comme l'origine de la méthode [PDCA](https://en.wikipedia.org/wiki/PDCA) (plan-do-check-act).

J'aime la boucle OODA, car c'est une illustration succincte d'une boucle de rétroaction générale. De nombreux concepts et méthodes de travail s'appuient sur l'idée de boucles de rétroaction, y compris les méthodes [DevOps](https://en.wikipedia.org/wiki/DevOps) et de [développement agile](https://en.wikipedia.org/wiki/Agile_software_development).

### Boucle de rétroaction de l'équipe de développement

Examinons à quoi pourraient ressembler certains composants d'une boucle de rétroaction pour un développeur au sein d'une équipe :

1. Directives des propriétaires de produits ou retours des utilisateurs
2. Daily scrum/standup avec toute l'équipe
3. Priorisation avec l'équipe de développeurs
4. Codage et tests individuels
5. Revue de code par les pairs
6. Déploiement et surveillance des performances

Implicitement, ces étapes supposent le soutien des collègues et de la direction — en d'autres termes, quelqu'un à qui rendre des comptes. Comment un développeur freelance solo peut-il créer un environnement similaire de responsabilité ?

### Boucle de rétroaction du développeur solo

Voici quelques étapes possibles qu'un développeur freelance individuel peut mettre en œuvre pour créer une boucle de rétroaction courte :

1. Construire la discipline
2. Clarifier les objectifs concrets de haut niveau
3. Prioriser et planifier les objectifs de niveau intermédiaire et bas
4. Automatiser votre travail
5. Bloquer du temps pour la revue de code
6. Bloquer du temps pour la revue de processus
7. Mettre à jour vos objectifs et processus avec les résultats de vos revues

Je vais détailler chacune de ces étapes ci-dessous.

#### Construire la discipline

Plus un prérequis qu'une étape en soi, construire la discipline est ce qui permet à notre boucle de rétroaction courte de fonctionner. Rien d'autre dans cet article ne sera utile si nous n'avons pas la capacité de faire quelque chose que nous ne voulons pas faire. La discipline est certainement une compétence. Elle peut être apprise, entraînée et améliorée comme toute autre.

Pourquoi la discipline est-elle si importante ? Parce que lorsque nous sommes en train de finaliser un projet ce vendredi soir, nous n'aurons pas envie d'écrire un bon message de commit. Nous n'aurons pas envie de nettoyer les commentaires du code. Nous voulons juste voir le projet partir, _Bonjour, git push -f_.

C'est dans ces moments que la discipline nous permet de ne pas manquer une opportunité de pratiquer, d'apprendre et d'améliorer notre processus de travail. La discipline nous aide à éviter les commits de vendredi soir qui se transforment en `git reset --hard` de lundi matin.

#### Clarifier les objectifs concrets de haut niveau

![Image](https://cdn-media-1.freecodecamp.org/images/FSBRpf7OG7Jq2t0heAlZu4PLkFgpWIk3sW6p)

Que nous travaillions pour un client ou que nous développions notre propre meilleure application, nous ne pourrons pas mesurer nos progrès ou nos améliorations sans quelque chose à quoi les mesurer.

Lorsque je discute d'un nouveau projet avec un client, je parle toujours en termes de réalisations concrètes. Cela peut prendre la forme de la réalisation d'une fonctionnalité spécifique à une certaine date, ou de la décision de ce à quoi ressemble le MVP pour un utilisateur. Cela est autant pour mon bénéfice que pour celui de mon client. En convenant, par écrit, **ce qui** sera réalisé et **quand**, mon client et moi avons clairement défini des objectifs de haut niveau et pouvons tous deux évaluer comment le projet progresse.

Lorsque je travaille pour moi-même, je me traite comme je traiterais un client. Je prends un engagement, par écrit, décrivant ce qui sera réalisé, et quand. Cela peut être quelque chose d'aussi simple qu'une liste d'objectifs pour la semaine, ou aussi détaillé qu'un tableau kanban.

Le but d'avoir un objectif concret, cependant, n'est pas de s'y tenir à tout prix. Il est important de fixer une attente, avec nous-mêmes et avec nos clients, que les objectifs seront réexaminés à des dates mutuellement convenues au cours du projet. Cela permet la partie si importante de "rétroaction" de la boucle.

#### Prioriser et planifier les objectifs de niveau intermédiaire et bas

![Image](https://cdn-media-1.freecodecamp.org/images/ne08OzeVcFueWzqHi5iS5spqEzuVgL6Vzhhc)

Peu d'objectifs sont atteints en une seule étape. Même le simple processus de préparation d'un sandwich au beurre de cacahuète et à la gelée (un exemple d'enseignement favori en [programmation informatique](https://www.youtube.com/watch?v=y62zj9ozPOM&t=1016s)) peut être décomposé en instructions successivement plus petites et plus précises. Bien que nous, humains, n'ayons peut-être pas besoin de la granularité qu'un programme informatique exige, les objectifs qui sont divisés en étapes réalisables et limitées dans le temps sont beaucoup plus faciles à assimiler. 💡

Commencez par les objectifs de niveau intermédiaire, et rendez chaque étape concrète. Si l'objectif est de lancer une nouvelle application web open source, par exemple, les étapes pourraient ressembler à ceci :

1. Compléter le JavaScript de l'application
2. Créer le front end et la feuille de style
3. Effectuer des tests locaux
4. Configurer le serveur cloud
5. Déployer l'application sur le cloud
6. Effectuer des tests
7. Ajouter le dépôt à GitHub
8. Publier sur Hacker News
9. Profit !!!

Chacun des exemples ci-dessus encapsule de nombreux objectifs plus petits, de bas niveau — nous pouvons penser à ceux-ci comme à nos éléments de liste de tâches. Par exemple, "Configurer le serveur cloud" pourrait impliquer :

1. Rechercher les fournisseurs de cloud
2. Décider du service et s'inscrire
3. Configurer le serveur/instance
4. Ajouter des intégrations
5. Tester le déploiement

Nos paramètres pour les tailles de morceaux et ce qui constitue une "étape" peuvent être différents les uns des autres, et changeront probablement de projet en projet. Si vos étapes de niveau intermédiaire et bas définissent clairement un chemin concret pour atteindre les objectifs de haut niveau que vous avez fixés, alors vous êtes en bonne voie. Plus tard, en évaluant le processus de décision qui nous a conduits à ces objectifs de niveau intermédiaire et bas, nous pouvons boucler notre boucle de rétroaction.

#### Automatiser votre travail

![Image](https://cdn-media-1.freecodecamp.org/images/YQiux-ArUTRIoqGGcNSAY7W1cyjyG1SiHTJG)

J'ai récemment lu un excellent article intitulé [Le travail manuel est un bug](https://queue.acm.org/detail.cfm?id=3197520). Il discute d'un processus par lequel les développeurs réussis documentent et finissent par automatiser leur travail. La beauté de cette idée réside dans sa simplicité. En écrivant les choses que nous faisons manuellement, nous sommes en mesure de corriger et d'affiner nos processus. En affinant nos processus, nous pouvons plus facilement les traduire en extraits de code et en scripts. Avec une collection de scripts que nous pouvons enchaîner, nous pouvons automatiser notre travail.

Automatiser le travail ne consiste pas seulement à gagner du temps. Cela réduit les erreurs de type "je n'ai pas encore bu mon café", minimise la charge cognitive en laissant plus de place à la créativité, et permet à nos processus d'être reproductibles entre collaborateurs et projets. Cela aide à raccourcir notre boucle de rétroaction en garantissant que nous ne faisons pas la même chose trois fois de trois manières différentes.

Nous pouvons commencer à automatiser en créant notre propre wiki personnel. Si nous prenons l'habitude d'écrire chaque chose manuelle que nous faisons, peu importe à quel point elle peut sembler basique à ce moment-là, nous nous donnons plus d'opportunités de repérer des motifs, et ainsi des intégrations et améliorations possibles.

La première fois que nous faisons quelque chose manuellement, nous écrivons les étapes. La deuxième fois, nous suivons les étapes. Cela nous donne l'opportunité de les corriger et de les affiner en fonction de ce que nous avons appris depuis la première fois.

Au fil des itérations successives, nous pourrions remplacer des parties de commandes manuelles par des variables. Nous pourrions trouver des extraits pratiques de scripts bash qui automatisent juste une partie de notre tâche. Tant que nous continuons à réviser et à améliorer notre wiki personnel, nous progressons vers l'automatisation.

#### Bloquer du temps pour la revue de code

![Image](https://cdn-media-1.freecodecamp.org/images/j0xWdQE2By2JGa9VFfRjL88NWz7ERedqY21F)

Il est trop facile de commiter du code désordonné lorsque nous travaillons seuls. Nous pensons, _qui va le voir ? Je le corrigerai plus tard._ Chaque fois que cela se produit, cependant, nous construisons une habitude. C'est une mauvaise habitude.

Travailler seul signifie qu'il n'y a personne pour donner des retours sur nos commits lorsque nous faisons quelque chose qui n'a pas de sens, ou qui pourrait être amélioré. Au lieu de cela, nous devons activement chercher des opportunités de nous améliorer. Les communautés open source sont incroyables pour cela. Il y a une richesse d'informations disponibles pour nous en termes de styles de codage, d'exemples de code refactorisé, et un smorgasbord d'extraits qui réalisent cette-chose-que-nous-essayions-de-faire mais en moins de lignes. Nous pouvons apprendre tout ce que nous voulons, si nous bloquons simplement le temps pour le faire.

Planifiez votre propre revue de code à un moment qui a du sens pour vous et le projet sur lequel vous travaillez. Cela pourrait être chaque fois que vous terminez une correction ou une fonctionnalité, ou à des intervalles réguliers quotidiens ou hebdomadaires. Si vous avez quelqu'un qui peut vous aider, réservez-le. Il y a aussi [des salons de discussion remplis de personnes](https://victoria.dev/verbose/top-free-resources-for-developing-coding-superpowers/) heureuses de prêter main forte.

Faites quelques recherches sur les meilleures pratiques de base pour ce sur quoi vous travaillez. Fixez-vous une limite de temps, cependant, et prenez ce que vous lisez avec un grain de sel. Il y a beaucoup de terriers de lapin dans ce domaine. En tant que point de départ, je recommanderais d'apprendre sur le code DRY, et de regarder [Uncle Bob exiger du professionnalisme dans le développement logiciel](https://www.youtube.com/watch?v=p0O1VVqRSK0&feature=youtu.be&t=330).

#### Liste de contrôle pour la revue de code

Voici ma liste de contrôle personnelle pour la revue de code, basée sur quelques bonnes pratiques générales. N'hésitez pas à l'utiliser comme point de départ pour la vôtre !

> **_L'Extravaganza de la Revue de Code de Victoria !_**

>  _- [ ] Cela résout un élément de haute priorité._  
>  _- [ ] Il s'agit d'une implémentation complète qui suit la spécification._  
>  _- [ ] Les modifications hors sujet n'ont pas été incluses et ont été ajoutées au backlog._  
>  _- [ ] Les noms de variables sont significatifs et il n'y a pas de nombres magiques._  
>  _- [ ] Des messages d'erreur corrects et utiles sont retournés à chaque opportunité._  
>  _- [ ] Aucune instruction d'impression de débogage n'a été laissée._  
>  _- [ ] Ce code est DRY et modulaire._  
>  _- [ ] Ce code est sécurisé. Le code privé et public sont bien séparés._  
>  _- [ ] Ce code est sa propre documentation, ou la documentation est à jour._  
>  _- [ ] Un enfant de cinq ans pourrait suivre cela, sérieusement c'est si lisible._  
>  _- [ ] Les tests unitaires passent avec succès._  
>  _- [ ] Master a été fusionné dans la branche et testé._  
>  _- [ ] La mise en forme suit les directives de style._  
>  _- [ ] Je ne peux pas trouver d'autres cas limites ou défauts connus._  
>  _- [ ] Je serais heureux si ce code m'était publiquement attribué._  
>  _- [ ] Je comprends pleinement ce que le code fait et l'impact des modifications que j'ai apportées._  
> -  _[ ] J'ai réellement vérifié qu'il fait réellement ce que j'ai dit qu'il faisait._

[Voici un excellent exemple](https://dev.to/gonedark/writing-clean-code) de nettoyage de code en gardant à l'esprit certains des points ci-dessus.

#### Bloquer du temps pour la revue de processus

![Image](https://cdn-media-1.freecodecamp.org/images/Nvgdg9nCzq5Rrtlq29-FF564MtsGginnwJnU)

Tout comme nous apprenons en révisant notre code, nous affinons nos processus en les révisant également. La revue de processus est la plus bénéfique lorsqu'elle est effectuée à intervalles réguliers tout au long du projet, et pas seulement après l'achèvement du projet.

Pour les projets à court terme, un bon point de départ pour la planification des revues de processus est à chaque mi-parcours — une fois à mi-chemin, et à nouveau après l'achèvement. Les projets à long terme peuvent avoir des revues à chaque quart de parcours.

#### Questions pour la revue de processus

La revue de processus peut être aussi simple qu'une courte liste de questions :

1. Quels étaient mes objectifs de haut niveau pour cette période ? Les ai-je atteints ?
2. Quels étaient mes objectifs de niveau intermédiaire et bas pour cette période ? Les ai-je atteints ?
3. Aurais-je été mieux servi avec des objectifs différents ou plus spécifiques ? Pourquoi ?
4. Ai-je réussi à supprimer ou à automatiser les obstacles ?
5. Ai-je respecté mon calendrier de revue de code ? Pourquoi ou pourquoi pas ?
6. Comment pourrais-je supprimer les obstacles la prochaine fois ?

Mettre de côté du temps dédié pour notre revue de processus peut nous aider à répondre à des questions comme celles-ci de manière réfléchie et honnête. Cela nous permet de tirer le meilleur parti de notre revue, aidant à raccourcir notre boucle de rétroaction.

#### Mettre à jour vos objectifs et processus avec les résultats de vos revues

![Image](https://cdn-media-1.freecodecamp.org/images/RCd2DfPOTP3j7UoMT1M9-UCuLeNO7SQRkKDo)

Toutes les données de performance du monde ne nous sont d'aucune utilité si nous ne les mettons pas en pratique. Avec chaque revue de code successive, nous pouvons affiner et ajouter à notre liste de contrôle. Avec ce que nous apprenons de chaque revue de processus, nous pouvons affiner et améliorer nos processus. Plus nous pouvons inventer des moyens concrets et observables de mettre en œuvre notre apprentissage, plus nous aurons de succès.

Faire un effort conscient pour utiliser et pratiquer les choses que nous avons apprises est le dernier composant vital de notre boucle de rétroaction. Plus nous incorporons souvent de nouveaux apprentissages, plus notre boucle devient courte, nous permettant de nous améliorer encore plus rapidement.