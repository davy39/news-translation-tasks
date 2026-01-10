---
title: 'Monolithe vs microservices : quelle architecture convient à votre équipe ?'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-17T12:39:12.000Z'
originalURL: https://freecodecamp.org/news/monolith-vs-microservices-which-architecture-is-right-for-your-team-bb840319d531
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KZM0T2Mg-Kog2AJ-mg6Jfg.jpeg
tags:
- name: business
  slug: business
- name: Design
  slug: design
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Monolithe vs microservices : quelle architecture convient à votre équipe
  ?'
seo_desc: 'By Jake Lumetta

  My good friend Darby Frey recently kicked off a greenfield project after assuming
  his new role as Sr. Platform Engineering Lead of Gamut. Despite starting out with
  monolith at his previous company Belly, he discovered that — in the ri...'
---

Par Jake Lumetta

Mon bon ami Darby Frey a récemment lancé un projet greenfield après avoir assumé son nouveau rôle de Sr. Platform Engineering Lead chez Gamut. Malgré avoir commencé avec un monolithe dans son ancienne entreprise Belly, il a découvert que — dans les bonnes circonstances — commencer avec un monolithe n'est pas toujours la meilleure solution.

Chez Belly, Darby et son équipe ont décomposé leur monolithe en une architecture de microservices assez large. Ils ont réussi à la stabiliser, mais seulement après des mois d'essais et de tribulations pour migrer vers les microservices.

Avec cette expérience fraîche dans son esprit, il a abordé son nouveau projet chez Gamut un peu plus méfiant envers les microservices.

« J'étais fermement membre de l'équipe Monolithe. [Je pensais] construisons une seule application et séparons les choses plus tard si nous commençons à ressentir des difficultés », a-t-il déclaré.

Bien que ce soit un projet greenfield, l'équipe de Darby était petite et il avait des délais agressifs, donc en surface, un monolithe semblait être le choix évident.

« [Mais avec ce nouveau projet], j'étais anxieux de ne pas répéter les erreurs du passé. »

Et avec cela, il s'est retrouvé face à une décision à laquelle nous sommes tous confrontés : devons-nous commencer avec un monolithe ou des microservices, et comment décider ?

### Sagesse conventionnelle sur les monolithes

De nombreuses startups commencent avec un monolithe, car sa structure se prête bien aux petites équipes et offre d'autres avantages comme une charge opérationnelle réduite. De plus, les monolithes ont souvent une seule base de code massive. La logique de l'application côté serveur, la logique côté client, les tâches en arrière-plan, etc., sont toutes définies dans la même base de code. Cela signifie que si les développeurs veulent apporter des modifications ou des mises à jour, ils doivent construire et déployer toute la pile en une seule fois.

Un monolithe n'est pas une architecture dépassée que nous devons laisser dans le passé. Dans certaines circonstances, un monolithe est idéal. J'ai parlé à Steven Czerwinski, Head of Engineering chez Scaylr et ancien employé de Google, pour mieux comprendre cela.

« Même si nous avions eu ces expériences positives d'utilisation de microservices chez Google, nous [chez Scaylr] avons choisi [la voie du monolithe] car avoir un seul serveur monolithique signifie moins de travail pour nous en tant que deux ingénieurs », a-t-il expliqué. C'était au tout début de Scalyr.

En d'autres termes, parce que son équipe était petite, une application unifiée était plus facile à gérer par rapport à tout diviser en microservices.

### L'alternative des microservices

Zachary Crockett, CTO de Particle, m'a dit cela lors d'un entretien :

> « Lorsque l'on parle de microservices, les gens ont tendance à se concentrer sur une extrémité de ce spectre : de nombreuses petites applications qui s'envoient trop de messages. À l'autre extrémité du spectre, vous avez un géant monolithe qui fait trop de choses. Pour tout système réel, il existe de nombreuses architectures orientées services possibles entre ces deux extrêmes. »

Le style architectural des microservices est une approche pour développer une seule application comme une suite de petits services. Chacun s'exécute dans son propre processus et communique avec des mécanismes légers, souvent une API de ressources HTTP.

Ces services sont construits autour de capacités métier et sont déployables indépendamment par une machinerie de déploiement entièrement automatisée. Il y a un minimum de gestion centralisée de ces services, qui peuvent être écrits dans différents langages de programmation et peuvent utiliser différentes technologies de stockage de données.

Les microservices ont des avantages distincts :

* **Meilleure Organisation** : Les architectures de microservices sont généralement mieux organisées. Chaque microservice a un travail très spécifique, et il ne se préoccupe pas des travaux des autres composants.
* **Découplés** : Les services découplés sont également plus faciles à recomposer et à reconfigurer pour servir les besoins de différentes applications (par exemple, servir à la fois les clients web et l'API publique). Ils permettent également une livraison rapide et indépendante de parties individuelles au sein d'un système plus large et intégré.
* **Performance** : Dans les bonnes circonstances, les microservices peuvent également avoir des avantages de performance selon la manière dont ils sont organisés. Il est possible d'isoler les services sollicités et de les mettre à l'échelle indépendamment du reste de l'application.
* **Moins d'erreurs** : Les microservices permettent un développement parallèle en établissant une frontière difficile à franchir entre différentes parties de votre système. En faisant cela, vous rendez difficile — ou au moins plus difficile — de faire la mauvaise chose : à savoir, connecter des parties qui ne devraient pas être connectées, et coupler trop étroitement celles qui doivent être connectées.

Mais ils créent également des défis uniques :

* **Préoccupations transversales dans chaque service** : En construisant une nouvelle architecture de microservices, vous risquez de découvrir de nombreuses préoccupations transversales que vous n'aviez pas anticipées au moment de la conception. Vous devrez soit supporter le surcoût de modules séparés pour chaque préoccupation transversale (c'est-à-dire les tests), soit encapsuler les préoccupations transversales dans une autre couche de service que tout le trafic traverse. Finalement, même les architectures monolithiques tendent à router le trafic à travers une couche de service externe pour les préoccupations transversales, mais avec une architecture monolithique, il est possible de retarder le coût de ce travail jusqu'à ce que le projet soit beaucoup plus mature.
* **Charge opérationnelle plus élevée** : Les microservices sont fréquemment déployés sur leurs propres machines virtuelles ou conteneurs, entraînant une prolifération de travail de gestion de VM. Ces tâches sont fréquemment automatisées avec des outils de gestion de flotte de conteneurs.

### Quel modèle vous convient ?

Des entretiens avec des dizaines de CTO nous ont appris qu'une seule approche ne convient pas à tous. Leurs expériences servent de rubrique utile pour vous aider à décider entre un monolithe et des microservices. Répondre à ces questions devrait vous guider dans la bonne direction :

#### Êtes-vous en terrain familier ?

Darby et son équipe chez Gamut ont pu se lancer directement dans les microservices parce qu'il avait de l'expérience avec les plateformes eCommerce, et son entreprise avait une richesse de connaissances concernant les besoins et les demandes de leurs clients. S'il avait emprunté une voie inconnue, un monolithe aurait peut-être été l'option la plus sûre.

De même, les startups naissent souvent des difficultés rencontrées dans les entreprises précédentes. Dans ces scénarios, il est parfois clair que la scalabilité sera une exigence primaire, surtout dans les services basés sur l'infrastructure comme la gestion des logs dans le cloud.

#### Votre équipe est-elle préparée ?

Votre équipe a-t-elle de l'expérience avec les microservices ? Que se passe-t-il si vous quadruplez la taille de votre équipe dans l'année à venir — les microservices sont-ils idéaux pour cette situation ? Évaluer ces dimensions de votre équipe est crucial pour le succès de votre projet.

Julien Lemoine, CTO chez Algolia, a commenté ce point :

> « Nous avons toujours commencé avec une approche de microservices. Le principal objectif était de pouvoir utiliser différentes technologies pour construire notre service, pour deux grandes raisons :

> 1) Nous voulons utiliser le meilleur outil pour chaque service. Notre API de recherche est hautement optimisée au niveau le plus bas et le C++ est le langage parfait pour cela. Cela dit, utiliser le C++ pour tout est une perte de productivité, surtout pour construire un tableau de bord !

> 2) Nous voulons les meilleurs talents et utiliser une seule technologie limiterait nos options. C'est pourquoi nous avons différents langages dans l'entreprise. Go est moins parfait que C++ lorsque vous voulez tout optimiser au niveau de la milliseconde, mais c'est le langage parfait lorsque la performance est encore clé (traitement des logs où nous traitons plusieurs téraoctets de logs par jour, utiliser Ruby ou Python serait une perte de CPU). »

Si votre équipe est préparée, commencer avec des microservices est judicieux car cela permet à votre équipe de s'habituer au rythme du développement dans un environnement de microservices, dès le départ.

#### Comment est votre infrastructure ?

En réalité, vous aurez besoin d'une infrastructure basée sur le cloud pour que les microservices fonctionnent pour votre projet. David Strauss, CTO de Pantheon, l'a expliqué ainsi :

> « [Auparavant], vous vouliez commencer avec un monolithe parce que vous vouliez déployer un seul serveur de base de données. L'idée de devoir configurer un serveur de base de données pour chaque microservice et ensuite le mettre à l'échelle était une tâche mammouth. Seule une organisation énorme et technologiquement avancée pouvait le faire.

> Alors qu'aujourd'hui, avec des services comme Google Cloud et Amazon AWS, vous avez de nombreuses options pour déployer de petites choses sans avoir besoin de posséder la couche de persistance pour chacune. »

#### Évaluez le risque commercial

Vous pourriez penser que les microservices sont la « bonne » voie à suivre en tant que startup technologiquement avancée avec de grandes ambitions. Mais les microservices posent un risque commercial. David Strauss a expliqué :

> « Beaucoup d'équipes surdimensionnent leur projet initialement ; tout le monde veut penser que sa startup sera la prochaine licorne et qu'elle devrait donc tout construire avec des microservices ou une autre infrastructure hyper-scalable. Mais c'est généralement faux, presque tout le temps. »

Un exemple de cela dans ses premiers jours chez Pantheon était un système limité à une seule VM. Ils pensaient qu'il faudrait un mois ou deux avant d'être forcés de le mettre à l'échelle. Cela a fini par prendre plus d'un an — et ils l'ont mis à l'échelle d'une manière complètement différente de ce qu'ils avaient anticipé.

Il a poursuivi en disant que, dans ces cas, les domaines que vous pensiez devoir mettre à l'échelle ne sont probablement pas les parties qui devront être mises à l'échelle en premier. Cela entraîne des efforts mal placés même pour les systèmes qui devront être mis à l'échelle.

### Le contexte est clé — Règles empiriques pour choisir une architecture

Nous avons passé des heures à interviewer des CTO réussis et nous les avons distillées en directives générales à suivre lors du choix de votre architecture de service.

#### Quand commencer avec un monolithe

Voici quelques scénarios qui indiquent que vous devriez commencer votre prochain projet en utilisant une architecture monolithique.

* **Votre équipe est au stade de fondation** : Votre équipe est petite, entre 2 et 5 membres, et est donc incapable de gérer une architecture de microservices plus large et à forte charge.
* **Vous construisez un produit non prouvé ou une preuve de concept** : Construisez-vous un produit non prouvé sur le marché ? Si c'est une nouvelle idée, il est probable qu'elle pivote et évolue au fil du temps, donc un monolithe est idéal pour permettre une itération rapide du produit. Même chose pour une preuve de concept où votre objectif est simplement d'apprendre le plus possible le plus rapidement possible, même si vous finissez par le jeter.
* **Vous n'avez aucune expérience avec les microservices** : Si votre équipe n'a aucune expérience préalable avec les microservices, sauf si vous pouvez justifier de prendre le risque d'apprendre « à la volée » à un stade aussi précoce, c'est probablement un autre signe que vous devriez vous en tenir à un monolithe pour commencer.

#### Quand commencer avec des microservices

Voici quelques scénarios qui indiquent que vous devriez commencer votre prochain projet en utilisant des microservices :

* **Vous avez besoin d'une livraison de service rapide et indépendante** : Les microservices permettent une livraison rapide et indépendante de parties individuelles au sein d'un système plus large et intégré. Notez que, selon la taille de votre équipe, cela peut prendre du temps pour voir les gains de livraison de service par rapport au fait de commencer avec un monolithe.
* **Une partie de votre plateforme doit être extrêmement efficace** : Si votre entreprise traite intensivement des pétabytes de volume de logs, vous voudrez probablement construire ce service dans un langage très efficace (par exemple, C++) tandis que votre tableau de bord utilisateur peut être construit en Ruby on Rails.
* **Vous prévoyez de développer votre équipe** : Commencer avec des microservices habitue votre équipe à développer dans des services séparés dès le début. Et avoir des équipes séparées par des frontières de service rend beaucoup plus facile la mise à l'échelle de votre équipe lorsque vous en avez besoin sans introduire une complexité exponentielle.

### Choisissez l'architecture avec laquelle vous pouvez vivre confortablement

Les microservices sont devenus une architecture de service de plus en plus populaire, mais il est essentiel de comprendre s'il s'agit de la meilleure solution pour votre projet. Votre propre contexte, évalué par rapport aux considérations ci-dessus, est la clé pour décider si vous devez commencer avec un monolithe ou des microservices.

Jake est le PDG de [ButterCMS](https://buttercms.com/). Pour plus de contenu comme celui-ci, suivez [@ButterCMS](https://twitter.com/ButterCMS) sur Twitter et abonnez-vous à [notre blog](https://buttercms.com/blog/).