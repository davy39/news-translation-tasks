---
title: Suivez ces principes pratiques pour obtenir des limites de microservices bien
  conçues
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-06T10:33:28.000Z'
originalURL: https://freecodecamp.org/news/follow-these-practical-principles-and-get-well-designed-microservices-boundaries-ef2deffd69e3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gKsnN4cbdRZfueyRWA6fjg.jpeg
tags:
- name: Design
  slug: design
- name: Microservices
  slug: microservices
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Suivez ces principes pratiques pour obtenir des limites de microservices
  bien conçues
seo_desc: 'By Jake Lumetta

  How to avoid making your microservices too small and tightly coupled


  _Photo by [Unsplash](https://unsplash.com/photos/aIYFR0vbADk?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" target="_blank" titl...'
---

Par Jake Lumetta

#### Comment éviter de rendre vos microservices trop petits et trop étroitement couplés

![Image](https://cdn-media-1.freecodecamp.org/images/HCYtimj7KjfKRnaZ1wl8f1qu03qPfosHMamw)
_Photo par [Unsplash](https://unsplash.com/photos/aIYFR0vbADk?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Erol Ahmed</a> sur <a href="https://unsplash.com/search/photos/complex?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

L'un des [avantages principaux du développement de nouveaux systèmes avec des microservices](https://buttercms.com/books/microservices-for-startups/should-you-always-start-with-a-monolith) est que l'architecture permet aux développeurs de construire et de modifier des composants individuels de manière indépendante. Mais des problèmes peuvent survenir lorsqu'il s'agit de minimiser le nombre de rappels entre chaque API.

Chris McFadden, VP de l'ingénierie chez SparkPost, a raconté une histoire de pièges de conception de microservices qui peut sembler familière à d'autres développeurs.

Dans les premiers jours de SparkPost, McFadden et son équipe devaient résoudre un problème que chaque entreprise SaaS rencontre : ils devaient fournir des services de base comme l'authentification, la gestion de compte et la facturation.

Le problème principal, bien sûr, n'était pas de savoir comment facturer leurs utilisateurs. Il s'agissait de concevoir leurs microservices de compte utilisateur pour supporter tout ce qui accompagne ce domaine de problème : comptes utilisateurs, clés API, authentification, comptes professionnels, facturation, et ainsi de suite.

Pour résoudre cela, ils ont créé deux microservices : une API Utilisateurs et une API Comptes. L'API Utilisateurs gérerait les comptes utilisateurs, les clés API et l'authentification, et l'API Comptes gérerait toute la logique liée à la facturation. Une séparation très logique, mais avant longtemps, ils ont repéré un problème.

« Nous avions un service appelé l'API Utilisateur, et un autre appelé l'API Compte. Mais le problème était qu'ils avaient en réalité plusieurs appels en va-et-vient entre eux. Donc vous faisiez quelque chose dans les comptes et aviez un appel et un point de terminaison dans les utilisateurs ou vice versa », a déclaré Chris.

Les deux services étaient trop étroitement couplés.

« Nous avons réalisé que dans la plupart des cas, vous ne voulez vraiment pas qu'un service appelle un autre service de manière parfois circulaire. Ce n'est généralement pas une bonne idée », a-t-il expliqué.

La solution, selon McFadden, est d'appliquer les limites de service appropriées.

Mais comment déterminer ces limites de service ? Contrairement au concept parfois difficile à saisir et abstrait de la conception pilotée par le domaine (DDD) — un cadre pour les microservices — la sagesse pratique des CTO expérimentés offre un meilleur cadre pour concevoir les limites des microservices. Cette sagesse, issue de heures d'entretiens, est distillée ci-dessous.

### Éviter les règles arbitraires

Lors de la conception et de la création d'un microservice, ne tombez pas dans le piège de l'utilisation de règles arbitraires. Si vous lisez suffisamment de conseils, vous rencontrerez certaines des règles ci-dessous. Bien qu'attrayantes, celles-ci ne sont **pas** des moyens appropriés pour déterminer les limites des microservices.

#### **Règle arbitraire #1 : Un microservice doit avoir X lignes de code**

Clarifions une chose : il n'y a pas de limitations sur le nombre de lignes de code dans un microservice. Un microservice ne devient pas soudainement un monolithe simplement parce que vous écrivez quelques lignes de code supplémentaires. La clé est de s'assurer qu'il y a une forte cohésion pour le code au sein d'un service (plus sur cela plus tard).

#### **Règle arbitraire #2 : Transformer chaque fonction en un microservice**

Si vous avez une fonction qui calcule quelque chose en fonction de trois valeurs d'entrée et retourne un résultat, est-ce un bon candidat pour un microservice ? Devrait-elle être une application déployable séparément ? Cela dépend vraiment de ce que fait la fonction et de la manière dont elle sert l'ensemble du système.

#### **Autres règles arbitraires**

D'autres règles arbitraires incluent celles qui ne prennent pas en compte votre contexte entier, comme l'expérience de l'équipe, la capacité DevOps, ce que fait le service et les besoins de disponibilité des données.

### Cinq caractéristiques d'un service bien conçu

Si vous avez lu sur les microservices, vous avez sans doute rencontré des conseils sur ce qui fait un service bien conçu. Une grande partie de cela se résume au principe de forte cohésion et de faible couplage. Bien que ce soient des conseils judicieux, ces concepts sont assez abstraits.

J'ai parlé avec des dizaines de CTO de ce sujet pour apprendre comment ils ont défini les limites de leurs microservices. J'ai distillé pour vous certaines des caractéristiques sous-jacentes ci-dessous.

#### **Caractéristique #1 : Un service bien conçu ne partage pas de tables de base de données avec un autre service**

Comme nous l'avons vu dans le cas de Chris McFadden mentionné ci-dessus, lorsqu'il s'agit de concevoir un microservice, si vous avez plusieurs services référençant la même table, c'est un signal d'alarme car cela signifie probablement que votre base de données est une source de couplage.

Il s'agit vraiment de la manière dont le service se rapporte aux données, ce que Oleksiy Kovrin, responsable du SRE Swiftype chez Elastic, m'a expliqué.

« L'un des principes fondateurs principaux que nous utilisons lors du développement de nouveaux services est qu'ils ne doivent pas franchir les limites des bases de données. Chaque service doit s'appuyer sur son propre ensemble de magasins de données sous-jacents. Cela nous permet de centraliser les contrôles d'accès, la journalisation d'audit, la logique de mise en cache, etc. », a-t-il déclaré.

Kovyrin a poursuivi en expliquant que si un sous-ensemble de vos tables de base de données « n'a pas ou très peu de connexions avec le reste de l'ensemble de données, c'est un fort signal que ce composant pourrait être isolé dans une API séparée ou un service séparé. »

Darby Frey, cofondateur de Lead Honestly, a écho à ce sentiment : « Chaque service doit avoir ses propres tables [et] ne doit jamais partager de tables de base de données. »

#### **Caractéristique #2 : Un service bien conçu a un nombre minimal de tables de base de données**

La taille idéale d'un microservice est suffisamment petite, mais pas plus. Et il en va de même pour le nombre de tables de base de données par service.

Steven Czerwinski, responsable de l'ingénierie chez Scaylr, m'a expliqué lors d'un entretien que le point idéal pour Scaylr est « une ou deux tables de base de données pour un service. »

Chris McFadden a élaboré dans le même sens : « Nous avons un microservice de suppression, et il gère, suit des millions et des milliards d'entrées concernant les suppressions, mais tout est très axé uniquement sur la suppression, donc il n'y a vraiment qu'une ou deux tables là. Il en va de même pour d'autres services comme les webhooks. »

#### **Caractéristique #3 : Un service bien conçu est judicieusement avec ou sans état**

Lors de la conception de votre microservice, vous devez vous demander s'il nécessite un accès à une base de données ou s'il s'agira d'un service sans état traitant des téraoctets de données comme des e-mails ou des journaux.

Soyez clair sur ce point dès le départ et cela conduira à un service mieux conçu.

Julien Lemoine d'Algolia explique : « Nous définissons les limites d'un service en définissant ses entrées et sorties. Parfois, un service est une API réseau, mais il peut également s'agir d'un processus consommant des fichiers et produisant des enregistrements dans une base de données (c'est le cas de notre service de traitement des journaux). »

#### **Caractéristique #4 : Les besoins de disponibilité des données d'un service bien conçu sont pris en compte**

Lors de la conception d'un microservice, vous devez garder à l'esprit quels services dépendront de ce nouveau service et quel est l'impact systémique si ces données deviennent indisponibles. En tenant compte de cela, vous pouvez concevoir correctement des systèmes de sauvegarde et de récupération des données pour ce service.

En parlant à Steven Czerwinski, il a mentionné que leurs données critiques de mappage d'espace de lignes de clients sont répliquées et séparées de différentes manières en raison de leur importance.

En revanche, « les informations par fragment, c'est dans leur propre petite partition. C'est ennuyeux si cela tombe en panne car cette partie de la population de clients n'aura pas leurs journaux disponibles, mais cela n'impacte que 5 pour cent des clients plutôt que 100 pour cent des clients », a expliqué Czerwinski.

#### **Caractéristique #5 : C'est une source unique de vérité**

La dernière caractéristique à garder à l'esprit est de concevoir un service pour qu'il soit la source unique de vérité pour quelque chose dans votre système.

Pour vous donner un exemple, lorsque vous commandez quelque chose sur un site de commerce électronique, un identifiant de commande est généré. Cet identifiant de commande peut être utilisé par d'autres services pour interroger un service de commande pour obtenir des informations complètes sur la commande. En utilisant le concept de pub/sub, les données qui sont échangées entre les services doivent être l'identifiant de commande, et non les attributs/informations de la commande elle-même. Seule la commande a des informations complètes et est la source unique de vérité pour une commande donnée.

### Considérations supplémentaires pour les grandes équipes

Ces directives devraient servir toutes les équipes, mais les CTO ont également mentionné des considérations pour les grandes équipes à prendre en compte lors de la conception des limites des microservices.

Pour les grandes organisations, où des équipes entières peuvent être dédiées à la possession d'un service, la considération organisationnelle entre en jeu lors de la détermination des limites des services. Et il y a deux considérations à garder à l'esprit : un calendrier de publication indépendant et une importance différente du temps de fonctionnement.

« La mise en œuvre la plus réussie des microservices que nous avons vue est soit basée sur un principe de conception logicielle comme la conception pilotée par le domaine, par exemple, et l'architecture orientée services, soit celles qui reflètent une approche organisationnelle », a déclaré Khash Sajadi, PDG de Cloud66.

« Donc [pour l']équipe des paiements », a poursuivi Sajadi, « ils ont le service de paiement ou le service de validation de carte de crédit et c'est le service qu'ils fournissent au monde extérieur. Donc ce n'est pas nécessairement quelque chose de logiciel. C'est surtout à propos de l'unité commerciale [qui] fournit un service de plus au monde extérieur. »

Amazon est un exemple parfait d'une grande organisation avec plusieurs équipes. Comme mentionné dans un article publié dans [API Evangelist](https://apievangelist.com/2012/01/12/the-secret-to-amazons-success-internal-apis/), Jeff Bezos a émis un mandat à tous les employés les informant que chaque équipe au sein de l'entreprise devait communiquer via une API. Quiconque ne le faisait pas serait licencié.

De cette manière, toutes les données et fonctionnalités étaient exposées via l'interface. Bezos a également réussi à faire en sorte que chaque équipe se découple, définisse quelles étaient ses ressources et les rende disponibles via l'API. Amazon construisait un système à partir de zéro. Cela permet à chaque équipe au sein de l'entreprise de devenir partenaire les unes des autres.

Travis Reeder, CTO d'Iron.io, a commenté l'initiative interne de Bezos.

« Jeff Bezos a ordonné que toutes les équipes devaient construire des API pour communiquer avec d'autres équipes. C'est aussi lui qui a inventé la règle des 'deux pizzas' ; une équipe ne devrait pas être plus grande que ce que deux pizzas peuvent nourrir », a-t-il déclaré.

« Je pense que la même chose pourrait s'appliquer ici : tout ce qu'une petite équipe peut développer, gérer et avec laquelle elle peut être productive. Si cela commence à devenir ingérable ou à ralentir, c'est probablement trop grand », m'a dit Reeder.

### Directives pendant les tests et la mise en œuvre

Les CTO ont également offert des informations sur les signaux d'alarme à surveiller pour déterminer si un service est trop petit ou non correctement défini.

**Surveillez la surdépendance entre deux services**

Si deux services s'appellent constamment l'un l'autre, c'est une forte indication de couplage et un signal qu'ils pourraient être mieux combinés en un seul service.

En revenant à l'exemple partagé par Chris McFadden au début de ce chapitre où il avait deux services API, comptes et utilisateurs qui communiquaient constamment entre eux, McFadden a eu l'idée de fusionner les services et a décidé de l'appeler l'API Accuser. Cela s'est avéré être une stratégie fructueuse :

« Ce que nous avons commencé à faire, c'était éliminer ces liens [qui étaient les] appels API internes entre eux. Cela a aidé à simplifier le code. » McFadden m'a informé.

**Les frais généraux de configuration du service l'emportent-ils sur l'avantage de l'avoir indépendant ?**

Darby Frey a expliqué : « Chaque application doit avoir ses journaux agrégés quelque part et doit être surveillée. Vous devez configurer des alertes pour cela. Vous devez avoir des procédures opérationnelles standard et des livres de bord pour quand les choses se cassent. Vous devez gérer l'accès SSH à cette chose. Il y a une énorme fondation de choses qui doivent exister pour qu'une application fonctionne simplement. »

### Considérez ces caractéristiques

La conception de microservices est une combinaison d'art et de science, mais les caractéristiques des mises en œuvre réussies de microservices fournissent une excellente liste de contrôle lors de la conception de votre prochain ensemble de limites de service.

Un service bien conçu :

1. Ne partage pas de tables de base de données avec un autre service
2. A un nombre minimal de tables de base de données
3. Est judicieusement avec ou sans état
4. A ses besoins de disponibilité des données pris en compte
5. Est une source unique de vérité

_Si vous avez apprécié cet article, aidez-le à se répandre en applaudissant ci-dessous ! Pour plus de contenu comme celui-ci, suivez-nous sur [Twitter](https://twitter.com/ButterCMS) et [abonnez-vous](https://buttercms.com/blog/) à notre blog._

_Jake Lumetta est le PDG de [ButterCMS](https://buttercms.com/), et publie [Microservices for Startups](https://buttercms.com/books/microservices-for-startups/)._

_Et si vous voulez ajouter un blog ou un CMS à votre site web sans vous embêter avec Wordpress, [vous devriez essayer Butter CMS](https://buttercms.com/).