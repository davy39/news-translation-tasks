---
title: Comment mener un processus de développement réussi (même si vous n'êtes pas
  technique)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-12T14:54:04.000Z'
originalURL: https://freecodecamp.org/news/how-to-run-a-successful-development-process-even-if-youre-not-technical-185d0558c89a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*SbbrnjE8bpHcyPXXx-9iKw.png
tags:
- name: agile
  slug: agile
- name: business
  slug: business
- name: management
  slug: management
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment mener un processus de développement réussi (même si vous n'êtes
  pas technique)
seo_desc: 'By Jonathan Solórzano-Hamilton

  Laurence Peter formulated the principle that “managers rise to the level of their
  incompetence” in 1969. In particular, non-technical leaders have earned a poor reputation
  with software developers.

  Office Space depicts ...'
---

Par Jonathan Solórzano-Hamilton

Laurence Peter a formulé le principe selon lequel « [les managers montent jusqu'au niveau de leur incompétence](https://en.wikipedia.org/wiki/Peter_principle) » en 1969. En particulier, les dirigeants non techniques ont acquis une mauvaise réputation auprès des développeurs de logiciels.

Le film Office Space dépeint le manager non technique en la personne de Bill Lumbergh, représenté ci-dessus. Dilbert fournit le classique « Pointy-Haired Boss ».

Cet article s'adresse à toute personne qui souhaite orchestrer efficacement un processus de développement sans devenir la cible des blagues de son équipe autour de la fontaine à eau. Je vais partager ce que j'ai appris au fil des années en gérant des processus de développement et de mise en production en tant que manager et architecte logiciel à l'UCLA et à l'Université de Stanford.

La plus grande leçon que j'ai apprise est que la clé pour maintenir des mises en production de logiciels réussies est **totalement non technique**.

Il s'agit de **processus**.

Certains aspects d'un processus de développement bénéficient de connaissances techniques, mais ce n'est pas obligatoire. La mise en production réussie d'un logiciel est bien plus une question d'architecture de processus robuste que de design ou de code seul.

Pour les besoins de cet article, nous supposerons que vous avez déjà convenu de commencer à construire quelque chose. Le pipeline d'approbation du produit est un processus différent. Aujourd'hui, nous nous concentrons sur la mise en production du produit convenu, du concept à la production.

#### Quoi construire

Votre équipe doit établir une feuille de route claire pour leur code. Les architectes et les fabricants utilisent des plans. Vous devriez faire de même.

![Image](https://cdn-media-1.freecodecamp.org/images/AkCcR1pOy96AhiGcLiOvYb7vxjrbhjP7qTMJ)
_Dois-je utiliser ces plans ou simplement improviser ? Hmm… ([source](http://www.energepic.com/manager-processing-his-new-project/" rel="noopener" target="_blank" title="))_

Votre feuille de route doit inclure un ensemble de schémas qui remplissent chacun un objectif différent. Ces schémas diffèrent pour les applications individuelles. Une maquette d'interface utilisateur, un diagramme d'architecture d'application et un modèle de processus métier sont courants. Des diagrammes de composants plus détaillés tels que les [diagrammes UML (Unified Modeling Language)](https://en.wikipedia.org/wiki/Unified_Modeling_Language) et les modèles de flux sont souvent utiles également.

L'expertise technique vous permet d'utiliser ces schémas pour critiquer l'architecture de votre équipe et vous assurer qu'elle est sur la bonne voie. Même sans compétence technique, ces schémas seront cruciaux.

Vous pouvez les utiliser pour mener des conversations productives sur l'achèvement du produit. Vous n'aurez plus à tirer un « % terminé » de nulle part ou à deviner à partir de l'équipe de développement. Vous pouvez suivre l'état de chaque élément du diagramme pour déterminer à quel point l'application est proche de l'achèvement. Vous pouvez également projeter la vitesse future en fonction de la rapidité avec laquelle l'équipe a terminé les composants précédents.

Il n'y a pas de quantité « correcte » de documentation pré-développement, mais il y a une quantité incorrecte : aucune. Travaillez avec votre équipe pour déterminer ce qui constitue une feuille de route acceptable avant qu'ils ne commencent à coder. Le **premier point de contrôle** de votre processus de développement sera de passer en revue cette documentation et de vous assurer qu'ils ont respecté cet accord.

#### Quoi ne pas construire

Votre équipe ne peut pas tout construire. Ni ne devrait-elle. Vous devez vous assurer que vos développeurs se concentrent uniquement sur ce qu'ils doivent réellement construire.

Pourquoi construisez-vous cette application en premier lieu ? Définissez la différenciation clé par rapport aux produits existants. 80 % du temps de votre équipe devrait être consacré à soutenir cette différenciation.

Les schémas que vous devriez maintenant avoir seront utiles ici. Votre application inclut-elle un composant de journalisation ? Un processus d'inscription et de connexion ? Il existe déjà d'excellents frameworks logiciels libres et open source (FOSS) dans la plupart des langages pour ces composants. Certains sont disponibles sous des licences extrêmement permissives.

Tesla fournit une excellente illustration de ce concept. Leur premier différenciateur clé était d'utiliser une batterie lithium-ion pour rendre les voitures électriques compétitives avec l'essence. Le lithium-ion a atteint cet objectif en réduisant le poids de la batterie et en augmentant l'autonomie.

![Image](https://cdn-media-1.freecodecamp.org/images/QdKRq-oWIu4tJWTg2tWzznCngx8rOJ5X9fkE)
_Eventuellement, Tesla est passé à la construction d'infrastructures entières pour soutenir leurs voitures, comme cette station « Supercharger »… mais pas avant d'avoir perfectionné leur produit initial différenciant ([source](https://pixabay.com/en/tesla-supercharger-battery-eco-1724773/" rel="noopener" target="_blank" title="))_

Le premier prototype de Tesla a simplement converti une voiture de sport électrique préexistante de l'acide-plomb aux batteries lithium. Leur première série de production était principalement une Lotus Elise roadster (une voiture de sport préexistante) qui avait une batterie et un moteur Tesla.

La leçon pour votre équipe est d'**utiliser ce qui existe déjà** autant que possible. Si vous pouvez utiliser ou adapter un package FOSS, faites-le. Même si vous devez licencier du code payant d'ailleurs, cela en vaut presque toujours la peine.

Mettez en place rapidement toute l'échafaudage afin de pouvoir tester **votre** « batterie lithium-ion ». Ensuite, vous pouvez itérer et remplacer ce qui aidera à différencier davantage votre produit sans stresser sur le retard de la préparation à la production.

Le **deuxième point de contrôle** de votre processus de développement est de passer en revue l'architecture prévue avec votre équipe et d'identifier la partie très limitée qu'ils prévoient de construire à partir de zéro.

Si cela ressemble à quelque chose qui existe déjà, et que ce n'est pas le cœur de votre produit, défiez votre équipe de voir pourquoi ils pensent devoir le refaire.

#### Ne jetez pas simplement par-dessus le mur

![Image](https://cdn-media-1.freecodecamp.org/images/9HqmCSAF1sZNlirB8SOVGHDY5mNU8gtqv5IK)
_Trop souvent, les équipes de développement « jettent la version par-dessus le mur » lorsque leur travail est terminé et s'en vont. Les bugs post-version sont pour l'équipe de support à gérer. ([source](https://pixabay.com/en/brick-wall-clinker-bricks-1747314/" rel="noopener" target="_blank" title="))_

Une fois que vous avez identifié les technologies pré-construites que vous allez utiliser, assurez-vous de les passer en revue avec votre groupe de support de production.

Les administrateurs de bases de données et de serveurs devront planifier l'installation et le support de toute nouvelle technologie. C'est le **troisième point de contrôle** de votre processus de développement : la préparation opérationnelle.

Garder l'équipe de support de production dans la boucle dès le début représente 90 % de la sauce secrète connue sous le nom de « [DevOps](https://en.wikipedia.org/wiki/DevOps) ». Si vous n'en avez pas entendu parler, DevOps est l'idée que les équipes de développement logiciel et d'exploitation de production devraient s'unir sous des objectifs communs.

Les avantages proposés incluent des versions beaucoup plus rapides, un code plus fiable et plus de temps passé à développer grâce à l'automatisation. Ce sont tous de grands avantages, mais ils découlent d'un processus de communication solide. L'automatisation suit, ne remplace pas, la collaboration.

#### Implémentation et Test

Maintenant, votre équipe écrit le code. Collaborez avec votre équipe d'implémentation pour concevoir un processus de division du travail entre eux. Il n'y a pas d'approche universelle, et c'est là que les « compétences douces » de leadership l'emportent largement sur toute compétence technique.

Certains développeurs voudront accaparer tout le travail « intéressant » et ignorer tout travail ingrat. Ils peuvent croire qu'ils sont la personne la plus intelligente de la pièce et qu'ils devraient avoir leur choix d'affectations. D'autres peuvent résister au changement et ne vouloir faire que le même type de travail qu'ils ont fait auparavant.

Guidez votre équipe vers une distribution équitable du travail. Défiez tout le monde à grandir de manière appropriée et à partager et collaborer.

Un autre aspect technique de l'implémentation est que le code doit inclure des tests automatisés suffisants. Ce sont des tests définis par le code qu'un système de test peut exécuter.

![Image](https://cdn-media-1.freecodecamp.org/images/ICxFDWBeo5Blw4ttUNwfMxqVch58WdgE054c)
_Si le code va planter, ne voulez-vous pas que les CV de ces gars soient en jeu plutôt que le vôtre ? (domaine public : photo du gouvernement américain)_

Les scripts de test « manuels » où un humain interagit avec le code pour voir s'il fonctionne sont insuffisants et reflètent une [dette technique](https://guide.freecodecamp.org/agile/technical-debt). Votre équipe technique devrait au moins inclure des [tests unitaires](https://guide.freecodecamp.org/software-engineering/unit-tests/). Le [développement piloté par les tests](https://guide.freecodecamp.org/agile/test-driven-development/) est une approche populaire pour s'assurer que le code critique est toujours testé.

Vous pouvez mener une conversation non technique avec votre équipe sur leur « couverture de test » (la portion du code qui est testée). C'est assez simple : demandez-leur de lister leurs hypothèses. Ensuite, demandez-leur où et comment ils testent ces hypothèses.

Le **point de contrôle** auquel le code est considéré comme complet par les développeurs est appelé dans mon équipe **dev-complete**. Cela signifie que le processus de développement principal (dev) est terminé, mais que du code supplémentaire peut être écrit pour traiter les problèmes qui surviennent lors du processus de révision.

Dans un processus de développement [agile](https://guide.freecodecamp.org/agile), vous diviserez généralement le processus d'implémentation en plusieurs points de contrôle au lieu d'une seule date limite tout ou rien. Ceux-ci sont généralement appelés itérations.

Référez-vous à la feuille de route que vous avez définie dans la première étape. Avant de commencer de nouveaux composants, assurez-vous que ce que vous avez déjà commencé est au moins dev-complete. Cela vous donne une vue précise de la vitesse de développement et réduit les risques.

Au fur et à mesure que vous terminez les itérations, vous pouvez pousser le code vers un environnement pour les « tests d'acceptation ». Cela implique des utilisateurs pilotes ou de test (ou une équipe interne jouant ce rôle) qui interagissent avec le produit partiel. Ils testent pour s'assurer qu'il répond aux attentes de conception et fournissent des commentaires sur la manière dont il pourrait être amélioré.

Les tests d'acceptation ne sont pas un substitut aux tests unitaires mentionnés précédemment. Ils servent un objectif différent. Laisser votre équipe de développement s'appuyer sur les tests d'acceptation pour attraper les bugs fonctionnels de base est une recette pour le désastre.

Les commentaires des testeurs d'acceptation peuvent être incorporés dans l'itération suivante. C'est une autre bonne raison de ne pas mordre un gros morceau du produit en une seule fois. Vous voulez laisser de la place pour changer de cap une fois que les gens commencent à utiliser le produit.

Une fois que vous avez accumulé suffisamment de code testé pour constituer une version de produit suffisante, vous êtes prêt à commencer le processus de gestion de version.

#### Chercher des bugs dans tous les bons endroits

![Image](https://cdn-media-1.freecodecamp.org/images/oAPMfSCILwWnEPtFSiiZIYKpmLDdAQUmVfgV)
_Le bug doit être quelque part ici… ([source](https://pixabay.com/en/manuscript-magnify-glass-glass-1614234/" rel="noopener" target="_blank" title="))_

Votre développeur ou votre équipe est arrivé à un point où ils pensent que le code est terminé. Les testeurs d'acceptation sont satisfaits du fonctionnement du produit. Le **prochain point de contrôle** du processus est de valider la croyance que vous avez un code prêt à devenir un produit. Commençons à passer en revue le code !

Vous n'êtes peut-être pas à l'aise ou n'avez pas suffisamment de connaissances techniques pour passer en revue le code de l'équipe vous-même. Ce n'est pas grave ! Vous n'avez pas à le faire. Votre processus doit le faire.

Travaillez avec votre équipe pour identifier un processus de révision de code qui fonctionne pour eux. Si vous avez plus d'un développeur, la révision de code par les pairs fonctionne très bien. Si vous n'en avez pas, y a-t-il d'autres développeurs dans votre organisation en dehors de votre équipe ? Travaillez au-delà des limites de l'équipe pour établir un programme de révision de code par les pairs.

S'il n'y a vraiment qu'un seul développeur, asseyez-vous avec lui et faites-lui parcourir le code. Utilisez vos schémas comme point de référence, et demandez-lui de vous expliquer comment le code atteint les objectifs du schéma.

À la conclusion du processus de révision de code, le développeur et le ou les réviseurs devraient se sentir à l'aise d'être tenus responsables du code.

La révision de code est également un bon moment pour passer en revue deux autres points critiques : la documentation et la sécurité.

J'ai [déjà écrit sur une architecture de documentation durable](https://medium.freecodecamp.org/our-team-broke-up-with-instant-legacy-releases-and-you-can-too-d129d7ae96bb) — consultez-le si vous êtes intéressé !

La révision de sécurité doit faire partie de toute révision de code. En général, cela implique de jeter un second regard sur le code pour repérer les faiblesses où un attaquant pourrait l'exploiter pour révéler des données privées ou prendre le contrôle du serveur. Cela doit être fait par une personne technique.

Le projet Open Web Application Security Project (OWASP) publie un [guide complet gratuit](https://www.owasp.org/images/2/2e/OWASP_Code_Review_Guide-V1_1.pdf) pour la révision de sécurité.

Votre développeur peut le faire s'il est le seul dans l'équipe, même s'il utilise simplement un outil d'analyse de code de sécurité automatisé. Il existe des outils gratuits pour aider à ce processus qui sont [liés via le wiki OWASP](https://www.owasp.org/index.php/Static_Code_Analysis).

#### Éjectez, éjectez, éjectez !

Le code a passé le processus de révision. Il est prêt à devenir un produit. Mais cela ne signifie pas qu'il est prêt pour la production.

Le **dernier point de contrôle** à franchir est la préparation au déploiement. Votre code est-il dans un état où il est facile à déployer en production ? Cela devrait impliquer le moins d'étapes manuelles possible.

Cela signifie également que vous devez avoir un plan pour revenir en arrière en cas de problème avec le code. Cela s'appelle un « plan de retour arrière ».

![Image](https://cdn-media-1.freecodecamp.org/images/IGMiN5fE7LDRncFW484II9F4dlHTjbDYCsNR)
_Tout le code de production ne reste pas en production… ([source](https://en.wikipedia.org/wiki/Lockheed_S-3_Viking#/media/File:S-3A_escape_sys_China_Lake_NAN1-72jpg.jpg" rel="noopener" target="_blank" title="))_

Si vous avez une équipe distincte pour les opérations logicielles, c'est là qu'ils réintègrent le tableau. Ils devraient passer en revue la documentation de déploiement et de retour arrière et vous faire savoir si elle est suffisante.

Si vous n'avez pas ce personnel, vous pouvez effectuer cette étape vous-même. Assurez-vous qu'il y a des instructions claires et simples pour déployer le produit. Il devrait y avoir très peu d'étapes manuelles, car chaque étape manuelle introduit une chance d'erreur humaine.

Il devrait y avoir un plan clair et suffisant pour revenir à l'état précédent si le déploiement ne réussit pas. Cela peut être aussi simple que de restaurer une sauvegarde, ou cela peut impliquer une communication avec les clients ou une conversion de données.

Le fait que le plan soit suffisant dépend de la rigueur avec laquelle votre équipe a testé le code, et de la portée de la mise en production du produit. Pensez également aux risques associés au produit ou à cette version particulière.

Une fois que vous avez franchi ce point de contrôle, poussez ce code en production !

#### Post-version

Réussite ou échec, il est important de faire un retour en arrière et de passer en revue le déroulement du processus.

Votre équipe a-t-elle estimé avec précision l'effort nécessaire pour mettre en production un produit ? Les tests ont-ils modélisé de manière adéquate le scénario de production ? Revisitez les points de contrôle d'implémentation et de test, et passez en revue la performance de l'équipe.

Comment le produit fonctionne-t-il en production ? Il est bon de rendre visite au personnel des opérations et d'obtenir leurs commentaires. Cela crée davantage de confiance entre les équipes de développement et d'exploitation, et conduira à davantage d'avantages DevOps à l'avenir.

Quels sont les écarts restants dans votre produit ? S'ils se trouvent dans du code tiers, c'est le moment de considérer si vous devez personnaliser vos packages ou tout réimplémenter à partir de zéro. Sinon, vous avez maintenant des informations sur ce qu'il faut construire pour la prochaine version.

Par-dessus tout, tenez-vous et votre équipe responsables des résultats de vos efforts.

La responsabilité facilite l'indépendance et favorise la croissance individuelle. À mesure que votre équipe s'habitue à être tenue responsable de chaque étape de ce processus, elle ajustera ses performances en conséquence.

#### Conclusion

Vous n'avez pas besoin d'être le moins du monde technique pour mener un processus de mise en production de logiciels réussi. La compétence technique peut aider, mais elle peut aussi devenir une béquille.

La clé d'une mise en production de logiciels réussie est un processus bien documenté et bien compris pour faire passer le logiciel du pipeline de l'idée au produit. Vous avez maintenant un point de départ pour rédiger votre propre processus de mise en production de logiciels.

Ce qui est le plus important, c'est que vous participiez avec votre équipe à combler les lacunes et à créer un processus reproductible qui fonctionne pour vous tous.

Il n'a pas besoin d'être parfait pour qui que ce soit, mais il doit être compris par tout le monde.

Vous devez également vous assurer que la vitesse de votre produit à travers ces points de contrôle correspond à la demande pour le produit. Aucun de ces éléments ne doit être un obstacle de plusieurs jours. Cela pourrait être une simple liste de contrôle d'une page. Vous devez définir un processus qui convient à votre environnement.

Comme pour tout processus, vous devez également itérer. Tout comme avec le code, votre premier brouillon non testé n'est probablement pas parfait. Ajustez le processus à chaque passage et vous obtiendrez un chemin de mise en production de logiciels fluide et prévisible.

Et n'oubliez pas de vous coiffer. Vous ne voulez pas qu'il ait l'air… pointu.

Si vous avez aimé cet article et que vous souhaitez en lire d'autres similaires, veuillez ? pour me le faire savoir ! Si vous souhaitez en savoir plus sur les processus de développement d'applications d'entreprise, veuillez répondre ci-dessous. Je suis heureux de partager ce que j'ai appris lors du parcours de mon équipe !

Vous pourriez également apprécier mes autres articles sur le processus métier du développement logiciel :

* [Ce que vous manquez en sautant la liste de contrôle](https://medium.freecodecamp.org/what-you-missed-because-you-were-too-cocky-to-use-a-checklist-c30c3ad663c2)
* [Comment nous nous sommes réorganisés en une équipe de développement plus professionnelle lorsque nous avons perdu notre gourou solitaire](https://medium.com/@peachpie/life-after-rick-our-team-reborn-after-the-fiery-departure-of-our-misanthropic-guru-b1fbaf3b8621)

Jonathan est le directeur adjoint de l'architecture et des opérations au département des systèmes d'information de recherche de l'UCLA. Il a obtenu un diplôme de physique de l'Université de Stanford et a depuis passé plus de 10 ans à travailler dans l'architecture des systèmes d'information, l'amélioration des processus commerciaux basés sur les données et la gestion organisationnelle.