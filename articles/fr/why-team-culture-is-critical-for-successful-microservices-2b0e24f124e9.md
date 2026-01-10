---
title: Pourquoi la culture d'équipe est cruciale pour des microservices réussis
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-20T17:21:15.000Z'
originalURL: https://freecodecamp.org/news/why-team-culture-is-critical-for-successful-microservices-2b0e24f124e9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xxKgPqB6Hkmx6y3gJS8LwA.jpeg
tags:
- name: Culture
  slug: culture
- name: Microservices
  slug: microservices
- name: Productivity
  slug: productivity
- name: teamwork
  slug: teamwork
- name: technology
  slug: technology
seo_title: Pourquoi la culture d'équipe est cruciale pour des microservices réussis
seo_desc: 'By Jake Lumetta

  Developers are increasingly turning to microservices to build and modify individual
  components independently. Microservices are clearly beneficial from a technical
  standpoint, but before teams decide to implement microservices, they s...'
---

Par Jake Lumetta

Les développeurs se tournent de plus en plus vers les microservices pour construire et modifier des composants individuels de manière indépendante. Les microservices sont clairement bénéfiques d'un point de vue technique, mais avant que les équipes ne décident de les implémenter, elles devraient considérer comment la création de microservices impactera la culture d'équipe.

Cet article offre des conseils et des perspectives de CTO qui ont connu les succès et enduré les difficultés de croissance de l'implémentation de microservices, ainsi que des orientations pour intégrer en douceur les microservices dans la culture de votre équipe.

### Règle n°1 : Vous ne pouvez pas construire des microservices réussis sans une culture d'équipe réussie.

À l'époque où je travaillais avec des développeurs Java, je me souviens d'une source de tension au sein de l'équipe concernant qui allait travailler sur les nouvelles fonctionnalités les plus importantes. Notre direction technique avait décidé que nous utiliserions exclusivement Java pour construire tous les nouveaux microservices.

Il y avait de bonnes raisons à cette décision, mais — comme je l'expliquerai plus tard — une telle décision restrictive avait des conséquences en termes de moral d'équipe. Nous avons appris une leçon importante là-bas : dans la mesure du possible, communiquer le « pourquoi » d'une décision technique à l'équipe peut grandement contribuer à créer une culture où les gens sont tenus informés.

En ce qui concerne l'organisation et la gestion d'une équipe autour des microservices, il est toujours difficile de trouver un équilibre entre l'humeur, le moral et la culture globale de votre équipe. Dans la plupart des cas, la direction doit équilibrer le risque que les membres de l'équipe utilisent de nouvelles technologies avec les besoins du client et de l'entreprise elle-même.

Ce dilemme, et bien d'autres similaires, a conduit les CTO à se poser des questions telles que : Quelle liberté devrais-je donner à mon équipe en matière d'adoption de nouvelles technologies ? Et peut-être plus important encore, comment puis-je gérer la culture globale au sein de mon équipe ?

#### Donnez à chaque membre de l'équipe une chance de s'épanouir

Lorsque les responsables techniques mentionnés ci-dessus ont décidé que Java était la meilleure technologie à utiliser pour construire des microservices, la décision était vraiment la meilleure pour l'entreprise. Java est performant, et beaucoup de personnes expérimentées de l'équipe le maîtrisaient bien. C'est pourquoi nous avons choisi Java. Cependant, tout le monde dans l'équipe n'avait pas d'expérience avec Java.

Le problème était que notre équipe était divisée en deux camps : les développeurs Java et les développeurs JavaScript. Avec le temps, de nouveaux projets passionnants sont apparus, et nous utilisions toujours Java pour les réaliser. Bientôt, une certaine frustration s'est installée au sein du camp JavaScript.

« Pourquoi les développeurs Java obtiennent-ils toujours les nouveaux projets passionnants, tandis que nous sommes laissés pour faire les tâches banales de front-end comme l'implémentation d'outils d'analyse tiers ? Nous voulons aussi un grand projet passionnant sur lequel travailler ! »

Comme la plupart des conflits, cela a commencé petit mais s'est aggravé avec le temps.

La leçon que j'ai tirée de cette expérience est de prendre en compte l'expertise et les technologies préférées de votre équipe lors du choix d'une pile technologique de facto pour vos microservices, ainsi que lors de l'ajustement du niveau de liberté que vous donnez à votre équipe pour choisir leurs outils.

Bien sûr, vous devez avoir une certaine structure, mais si vous êtes trop restrictif — ou pire encore, aveugle au désir des membres de votre équipe d'innover avec différentes technologies — vous pourriez avoir un conflit à gérer.

Alors, évaluez de près votre équipe et élaborez un plan qui donne à chacun les moyens de s'épanouir. Ainsi, chaque section de votre équipe peut participer à des projets majeurs, sans que personne ne se sente exclu.

### Choix technologiques : stabilité vs flexibilité

L'un des plus grands défis auxquels sont confrontés les CTO et les développeurs est de déterminer quelle liberté technologique accorder aux développeurs.

Supposons que vous embauchiez un nouveau développeur junior. Il pourrait être enthousiaste à propos d'un tout nouveau framework JavaScript fraîchement sorti. Presque trop nouveau.

Ce framework, bien qu'il présente certaines avancées techniques, n'a peut-être pas fait ses preuves dans des environnements de production et ne dispose probablement pas d'un bon support. Les CTO doivent faire un choix difficile entre approuver cette décision pour le bien du moral et de l'enthousiasme au sein de l'équipe — ou la refuser pour protéger les besoins de l'entreprise, préserver la rentabilité de l'entreprise et maintenir la stabilité du projet à l'approche de la date limite.

La bonne réponse dépend de nombreux facteurs différents, ce qui signifie qu'il n'y a pas de réponse unique.

#### Liberté technologique

Certains CTO et fondateurs adoptent pleinement la liberté technologique, puis laissent les choses se stabiliser naturellement sur quelques technologies qui fonctionnent bien lors du déploiement.

« Nous donnons à notre équipe et à nous-mêmes une liberté à 100 % dans le choix des technologies. Nous avons finalement identifié deux ou trois technologies à ne pas utiliser, principalement pour ne pas compliquer notre histoire de déploiement », a déclaré [Benjamin Curtis](https://twitter.com/stympy?lang=en), cofondateur de [Honeybadger](https://www.honeybadger.io/).

« En d'autres termes, nous avons envisagé d'introduire de nouveaux langages et de nouvelles approches dans notre pile technologique lors de la création de nos microservices, et nous avons effectivement déployé un microservice de production sur une pile différente à un moment donné. [Bien que nous utilisions généralement] des technologies que nous connaissons pour simplifier notre pile d'opérations, nous réévaluons périodiquement cette décision pour voir si des avantages potentiels en termes de performance ou de fiabilité pourraient être obtenus en adoptant une nouvelle technologie, mais jusqu'à présent nous n'avons pas fait de changement », a poursuivi Curtis.

Lorsque j'ai parlé avec [Stephen Blum](https://twitter.com/stephenlb), CTO chez [PubNub](https://www.pubnub.com/), il a également exprimé une opinion similaire en faveur de l'accueil de presque toutes les technologies qui font leurs preuves :

« Nous sommes totalement ouverts à cela. Nous voulons continuer à avancer avec les nouvelles technologies open source disponibles et nous n'avons que quelques contraintes avec l'équipe qui sont très justes : doit fonctionner dans un environnement de conteneur et doit être rentable », a déclaré Blum.

#### Haute liberté, haute responsabilité

La liberté s'accompagne cependant d'une mise en garde : si les développeurs profitent des fruits de la liberté de choix technologique, ils doivent également prendre la responsabilité de s'assurer que la construction fonctionne.

Lors de mon entretien avec le CTO de [Sumo Logic](http://sumologic.com), [Christian Beedgen](https://twitter.com/raychaser), et l'architecte en chef [Stefan Zier](https://twitter.com/stefanzier), ils ont développé ce sujet. Ils ont ajouté du poids à la position selon laquelle, si vous allez donner aux développeurs la liberté de choisir leur technologie, cela doit s'accompagner d'un haut niveau de responsabilité.

« Il est vraiment important que [celui qui construit] le logiciel en prenne la pleine responsabilité. En d'autres termes, ils ne construisent pas seulement le logiciel, mais ils l'exécutent également et restent responsables de l'ensemble du cycle de vie », ont-ils déclaré.

Ils ont poursuivi en expliquant qu'un système ressemblant à un système de gouvernement fédéral devrait être mis en place pour aider à maintenir ces libertés sous contrôle en augmentant la responsabilité.

« [Vous avez besoin] d'une culture fédérale, vraiment. Vous devez avoir un système où plusieurs équipes indépendantes peuvent se réunir vers un objectif commun. Cela limite l'indépendance des unités dans une certaine mesure, car elles doivent accepter qu'il existe potentiellement un gouvernement fédéral de quelque sorte. Mais au sein de ces petits groupes, ils peuvent prendre autant de décisions par eux-mêmes qu'ils le souhaitent dans le cadre des directives établies à un niveau supérieur », a-t-il déclaré.

Décentralisé, fédéral, ou comme vous souhaitez le formuler, semble certainement être une approche attrayante pour structurer les équipes de microservices. C'est une approche qui donne à chaque équipe et à chaque membre de l'équipe la liberté qu'ils souhaitent — sans donner à quiconque le champ libre pour déconstruire l'ensemble du projet.

Mais tout le monde n'est pas d'accord.

#### Restreindre la technologie pour simplifier les choses

D'un autre côté, [Darby Frey](https://twitter.com/darbyfrey), cofondateur de Lead Honestly, adopte une approche plus restrictive en matière de sélection technologique.

« Dans mon ancienne entreprise, nous avions beaucoup de services et une équipe assez petite, et l'une des principales choses qui a fait que cela fonctionnait, surtout pour la taille de l'équipe que nous avions, était que chaque application était la même. Chaque service backend était une application Ruby », a-t-il expliqué.

Frey m'a expliqué comment cela a simplifié la vie de son équipe, car chaque service a « le même framework de test, le même backend de base de données, le même outil de traitement des tâches en arrière-plan, etc. Tout était identique. »

En même temps, Frey est sensible au concept des développeurs souhaitant introduire un nouveau langage, admettant qu'il « adore l'idée d'essayer de nouvelles choses ». Cependant, il estime que les inconvénients l'emportent sur les avantages.

« Avoir une architecture polyglotte peut augmenter les coûts de développement et de maintenance. Si tout est identique, vous pouvez vous concentrer sur la valeur métier et les fonctionnalités métier et ne pas avoir à être super cloisonné dans le fonctionnement de vos services. Je ne pense pas que tout le monde aime cette décision, mais à la fin de la journée, lorsqu'ils doivent corriger quelque chose le week-end ou en pleine nuit, ils l'apprécient », a déclaré Frey.

### Organisation centralisée ou décentralisée

La manière dont votre équipe est structurée aura également un impact sur votre culture d'ingénierie des microservices — en bien ou en mal.

Par exemple, il est courant que les ingénieurs logiciels écrivent le code avant de l'envoyer à l'équipe des opérations, qui à son tour le déploie sur les serveurs. Mais lorsque les choses se cassent (et elles se cassent toujours !), un conflit interne se produit.

Parce que les ingénieurs d'exploitation n'écrivent pas eux-mêmes le code, ils comprennent rarement les problèmes lorsqu'ils surviennent. Par conséquent, ils doivent contacter ceux qui l'ont codé — les ingénieurs logiciels. Ainsi, dès le départ, vous avez un intermédiaire qui relaie un message entre le problème et l'équipe qui peut le résoudre.

Pour ajouter un niveau de complexité supplémentaire, parce que les ingénieurs logiciels ne sont pas impliqués dans les opérations, ils ne peuvent souvent pas pleinement apprécier comment leur code affecte le fonctionnement global de la plateforme. Ils ne prennent connaissance d'un problème que lorsque les ingénieurs d'exploitation s'en plaignent. Comme vous pouvez le voir, c'est une relation vouée à un conflit constant.

#### Décentralisé = haute responsabilité

Une façon d'aborder ce problème est de suivre l'exemple de Netflix et Amazon, qui privilégient tous deux une gouvernance décentralisée. James Lewis et Martin Fowler, deux leaders de la pensée en matière de développement logiciel, ont exposé leurs réflexions via un [long article de blog](https://martinfowler.com/articles/microservices.html#ProductsNotProjects). Selon eux, la gouvernance décentralisée est la voie à suivre en matière d'organisation d'équipes de microservices.

« L'une des conséquences de la gouvernance centralisée est la tendance à standardiser sur des plateformes technologiques uniques. L'expérience montre que cette approche est restrictive — tous les problèmes ne sont pas des clous et toutes les solutions ne sont pas des marteaux », lit-on dans l'article.

« Peut-être l'apogée de la gouvernance décentralisée est l'éthique du 'construisez-le, exécutez-le' popularisée par Amazon. Les équipes sont responsables de tous les aspects du logiciel qu'elles construisent, y compris l'exploitation du logiciel 24h/24 et 7j/7 », poursuit-il.

Netflix, écrivent Lewis et Fowler, est une autre entreprise qui pousse à des niveaux de responsabilité plus élevés pour les équipes de développement. Ils émettent l'hypothèse que, parce qu'elles seront responsables et appelées en cas de problème plus tard, plus de soin sera pris lors des phases de développement et de test pour s'assurer que chaque microservice est en parfait état.

« Ces idées sont aussi éloignées que possible du modèle traditionnel de gouvernance centralisée », concluent-ils.

#### Qui est appelé en cas de problème le week-end ?

Lorsque vous envisagez une culture centralisée ou décentralisée, vous devriez réfléchir à l'impact que cela a sur vos membres d'équipe lorsque des problèmes surviennent inévitablement à des moments inopportuns. Vous voyez, un système décentralisé implique que chaque équipe décentralisée prend la responsabilité d'un service, ou d'un ensemble de services. Mais cela crée aussi un problème : les silos.

C'est l'une des raisons pour lesquelles [Darby Frey](https://twitter.com/darbyfrey), cofondateur de Lead Honestly, n'est pas un partisan du concept de gouvernance décentralisée.

« Le modèle selon lequel 'une seule équipe est responsable d'un service particulier' est quelque chose que l'on voit beaucoup dans les architectures de microservices. Nous ne faisons pas cela, pour plusieurs raisons. La principale raison commerciale est que nous voulons des équipes responsables non pas de codes spécifiques, mais de fonctionnalités orientées client. Une équipe peut être responsable du traitement des commandes, ce qui touchera plusieurs bases de code, mais le résultat final pour l'entreprise est qu'il y a une équipe qui possède l'ensemble du processus de bout en bout, de sorte qu'il y a moins de failles par lesquelles les choses peuvent passer », a expliqué Frey.

L'autre raison principale, a-t-il poursuivi, est que les développeurs peuvent prendre plus de responsabilité sur le projet global :

« Ils peuvent réellement penser au [projet] de manière holistique », a déclaré Frey.

Nathan Peck, Developer Advocate pour les services de conteneurs chez Amazon Web Services, [a expliqué ce problème plus en profondeur ici](https://medium.com/@nathankpeck/microservice-principles-decentralized-governance-4cdbde2ff6ca). En essence, lorsque vous séparez les ingénieurs logiciels et les ingénieurs d'exploitation, vous rendez la vie plus difficile à votre équipe chaque fois qu'un problème survient avec le code — ce qui est également une mauvaise nouvelle pour les utilisateurs finaux.

#### La décentralisation doit-elle conduire à la séparation et à la création de silos ?

Peck poursuit en expliquant que sa solution réside dans [DevOps](https://opensource.com/resources/devops), un modèle visant à resserrer la boucle de rétroaction en rapprochant ces deux équipes. Cela renforce la culture d'équipe et la communication dans le processus. Peck décrit cela comme l'approche « vous le construisez, vous l'exécutez ».

Cependant, cela ne signifie pas que les équipes doivent être cloisonnées ou éloignées de la participation à certaines tâches, comme Frey suggère que cela pourrait arriver.

« L'une des approches les plus puissantes de la gouvernance décentralisée est de construire un état d'esprit de 'DevOps' », a écrit Peck. « [Avec cette approche], les ingénieurs sont impliqués dans toutes les parties du pipeline logiciel : écriture de code, construction, déploiement du produit résultant, et exploitation et surveillance en production. La méthode DevOps contraste avec l'ancien modèle de séparation des équipes de développement des équipes d'exploitation en ayant des équipes de développement livrer du code 'par-dessus le mur' aux équipes d'exploitation qui étaient alors responsables de l'exécuter et de le maintenir. »

DevOps, comme l'a expliqué le CTO d'[Armory](http://armory.io), [Isaac Mosquera](https://twitter.com/imosquera), est un cadre et une culture de développement logiciel agile qui gagne en traction grâce à — eh bien, presque tout ce que Peck a dit.

Intéressamment, Mosquera estime que cette approche va à l'encontre de la [loi de Conway](https://en.wikipedia.org/wiki/Conway%27s_law) :

> « Les organisations qui conçoivent des systèmes… sont contraintes de produire des designs qui sont des copies des structures de communication de ces organisations. » — M. Conway

« Au lieu que la communication guide la conception logicielle, maintenant l'architecture logicielle guide la communication. Non seulement les équipes fonctionnent et s'organisent différemment, mais cela nécessite un nouvel ensemble d'outils et de processus pour soutenir ce type d'architecture, c'est-à-dire DevOps », a expliqué Mosquera.

[Chris McFadden](https://twitter.com/cristoirmac), VP de l'ingénierie chez [SparkPost](https://www.sparkpost.com/), a un exemple intéressant qui pourrait valoir la peine d'être suivi. Chez SparkPost, vous trouverez une gouvernance décentralisée — mais vous ne trouverez pas une culture d'une équipe par service.

« L'équipe qui développe ces microservices a commencé comme une seule équipe, mais elle est maintenant divisée en trois équipes sous le même groupe plus large. Chaque équipe a un certain niveau de responsabilité autour de certains domaines et certaines expertises, mais la propriété de ces services n'est pas restreinte à l'une de ces équipes », a déclaré McFadden.

Cette approche, a expliqué McFadden, permet à n'importe quelle équipe de travailler sur n'importe quoi, des nouvelles fonctionnalités aux corrections de bugs en passant par les problèmes de production liés à l'un de ces services. Il y a une flexibilité totale, et pas de silo en vue.

« Cela permet [aux équipes] d'être un peu plus flexibles, tant en termes de développement de nouveaux produits, simplement parce que vous n'êtes pas trop restreint et cela est basé sur notre taille en tant qu'entreprise et en tant qu'équipe d'ingénierie. Nous devons vraiment conserver une certaine flexibilité », a-t-il poursuivi.

Cependant, la taille pourrait jouer un rôle ici, car McFadden a admis que si SparkPost était beaucoup plus grand, « alors il serait plus logique d'avoir une seule équipe plus grande posséder l'un de ces microservices. »

« [C'est] mieux, je pense, d'avoir une responsabilité un peu plus large pour ces services et cela vous donne un peu plus de flexibilité. Au moins, cela fonctionne pour nous à ce stade, où nous en sommes en tant qu'organisation », a-t-il déclaré.

### Une culture d'ingénierie de microservices réussie est un exercice d'équilibre

En matière de technologie, la liberté — avec responsabilité — semble être le chemin le plus gratifiant. Les membres de l'équipe avec des préférences technologiques différentes viendront et partiront, tandis que de nouveaux défis pourraient vous obliger à abandonner les technologies qui vous ont bien servi jusqu'à présent. Le développement logiciel est en constante évolution, et vous devrez donc continuellement équilibrer les besoins de votre équipe à mesure que de nouveaux appareils, technologies et clients émergent.

En ce qui concerne la structuration de vos équipes, une approche décentralisée, mais non cloisonnée, qui tire parti de DevOps et instaure une mentalité de « vous le construisez, vous l'exécutez » semble être populaire, bien que d'autres écoles de pensée existent. Comme d'habitude, vous devrez expérimenter pour voir ce qui convient le mieux à votre équipe.

Voici un rapide récapitulatif sur la manière de garantir que votre culture d'équipe s'harmonise bien avec une architecture de microservices :

* **Soyez durable, mais flexible** : Équilibrez la durabilité sans oublier la flexibilité et le besoin pour votre équipe d'être innovante lorsque la bonne opportunité se présente. Cependant, il existe une différence d'opinion distincte sur la manière dont vous devriez atteindre cet équilibre.
* **Donnez des opportunités égales** : Ne favorisez pas une section de votre équipe par rapport à une autre. Si vous allez imposer des restrictions, assurez-vous qu'elles ne vont pas fondamentalement aliéner les membres de l'équipe dès le départ. Réfléchissez à la manière dont votre feuille de route produit se dessine et prévoyez comment elle sera construite et qui fera le travail.
* **Structurez votre équipe pour qu'elle soit agile, mais responsable** : La gouvernance décentralisée et le développement agile sont à la mode pour une bonne raison, mais n'oubliez pas d'installer un sens de la responsabilité au sein de chaque équipe.

*Si vous avez apprécié cet article, aidez-le à se diffuser en applaudissant ci-dessous ! Pour plus de contenu comme celui-ci, suivez-nous sur [Twitter](https://twitter.com/ButterCMS) et [abonnez-vous](https://buttercms.com/blog/) à notre blog.*

*Et si vous souhaitez ajouter un blog ou un CMS à votre site web sans vous embêter avec Wordpress, [vous devriez essayer Butter CMS](https://buttercms.com/).* [ButterCMS](https://buttercms.com/) est un CMS headless qui vous permet de créer des applications alimentées par un CMS en utilisant n'importe quel langage de programmation, y compris [Ruby](https://buttercms.com/ruby-cms/), [Rails](https://buttercms.com/rails-cms/), [Node.js](https://buttercms.com/nodejs-cms/), [Python](https://buttercms.com/python-cms/), [ASP.NET](https://buttercms.com/asp-net-cms/), [Flask](https://buttercms.com/flask-cms/), [Django](https://buttercms.com/django-cms/), [Go](https://buttercms.com/golang-cms/), [PHP](https://buttercms.com/php-cms/), [Laravel](https://buttercms.com/laravel-cms/), [Angular](https://buttercms.com/angular-cms/), [React](https://buttercms.com/react-cms/), [Elixir](https://buttercms.com/elixir-cms/), [Phoenix](https://buttercms.com/phoenix-cms/), [Meteor](https://buttercms.com/meteor-cms/), [Vue.js](https://buttercms.com/vuejs-cms/), et [Gatsby.js](https://buttercms.com/gatsbyjs-cms/)