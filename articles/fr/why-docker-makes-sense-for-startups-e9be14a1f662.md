---
title: Pourquoi Docker a du sens pour les startups
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-18T18:58:26.000Z'
originalURL: https://freecodecamp.org/news/why-docker-makes-sense-for-startups-e9be14a1f662
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mUBw_A0ktP7ikp8MefvDXQ.jpeg
tags:
- name: AWS
  slug: aws
- name: Docker
  slug: docker
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: technology
  slug: technology
seo_title: Pourquoi Docker a du sens pour les startups
seo_desc: 'By Charly Vega

  Docker is becoming the standard to develop and run containerized applications.

  Long ago, this piece of technology might have made sense to system administrator
  and PaaS (Platform as a Service) providers. But we’ve been hearing rather l...'
---

Par Charly Vega

Docker devient la norme pour développer et exécuter des applications conteneurisées.

Il y a longtemps, cette technologie aurait pu avoir du sens pour les administrateurs système et les fournisseurs de PaaS (Platform as a Service). Mais nous avons entendu assez peu de choses de la part des startups sur leur adoption de Docker. Particulièrement celles comptant entre 1 et 10 employés. Cette impression corrobore quelque peu les [recherches récentes](https://www.datadoghq.com/docker-adoption/) de [Datadog HQ](https://medium.com/u/acdb626ac40c) :

![Image](https://cdn-media-1.freecodecamp.org/images/1*TNQdK1w297zNJKDauk4a4Q.png)
_... devinez que cette histoire aurait pu être écrite de manière plus opportune en 2015._

Au cas où vous ne seriez pas sûr que cela vaille la peine, nous avons pensé révéler à quel point l'adoption d'une architecture compatible avec les conteneurs a aidé [notre startup](https://blog.beta.uy/). Et pourquoi vous pourriez essayer Docker si vous ne l'avez pas encore fait.

### L'expérience de développement

Si vous travaillez dans une petite startup [de deux pizzas](http://www.businessinsider.com/amazon-jeff-bezos-two-pizza-rule-productive-meetings-2017-7), il y a de fortes chances que les membres de votre équipe soient multitâches. Une fois que les projets ne sont plus cloisonnés, vous recevrez un accueil chaleureux dans l'enfer des environnements de développement.

Considérez un scénario simple où un ingénieur front-end a besoin d'une API non encore en production d'un back-end. Vous pourriez surmonter cela en utilisant des données simulées ou en configurant des environnements de préproduction. Ce sont de grandes solutions. Mais rien ne vaut l'agilité d'exécuter des intégrations directement contre le code back-end lui-même.

Des outils comme docker-compose ont fait des merveilles pour nous. Tout ce qu'un nouveau venu doit faire est d'installer une seule [_chose_](https://www.docker.com/docker-mac). Une seule invocation de docker-compose et Docker configurera tout pour vous, afin que vous puissiez vous remettre à coder immédiatement.

La [nature déclarative](https://docs.docker.com/compose/compose-file/#dockerfile) de ces outils fournit une description simple de la manière dont les composants d'exécution communiquent entre eux. Cela facilite grandement la compréhension de votre architecture de haut niveau.

### Portabilité

En plus d'être utile en développement, Docker nous a également apporté de la simplicité lors de l'emballage de notre code pour la production. Cela est dû au fait qu'il rend les environnements de développement et de production plus symétriques. C'est un point soulevé par le [dev/prod parity](https://12factor.net/dev-prod-parity) de 12factor.

Nous avons de grands outils spécifiques aux langages comme [rbenv](https://github.com/rbenv/rbenv) (gestion des versions Ruby) et [nvm](https://github.com/creationix/nvm) (Node Version Manager). Ils nous protègent contre des problèmes comme les incompatibilités de versions d'exécution. Vous dépasseriez leurs capacités si votre code dépendait de certains binaires natifs obscurs ou d'une structure de système de fichiers particulière.

C'est là que les conteneurs font un effort supplémentaire. Ils nous permettent d'emballer notre application avec exactement le type d'environnement dont nous avons besoin.

Cette même portabilité brille dans les configurations hybrides de cloud. À ce sujet, je n'ai pas besoin de vous en dire beaucoup plus que notre histoire de migration de notre cloud.

Nous étions mécontents de la faible fiabilité et du support de notre fournisseur de cloud à l'époque. Nous avons décidé de passer au [roi](https://thenextweb.com/offers/2016/03/11/amazon-web-services-dominates-cloud-services-market/#.tnw_e8LvdkYN) de l'IaaS (Infrastructure as a Service), AWS (Amazon Web Services).

Nous avions prévu que cette migration aurait lieu plus tôt que tard. Nous avions donc migré nos applications pour qu'elles s'exécutent sur Docker depuis quelques mois. Lorsque le moment est venu de dire adieu à notre ancien cloud, le processus de transition entier n'a pris que quelques jours.

Une telle transition drastique pourrait être considérée comme un événement rare. Mais je n'ai jamais trouvé problématique de privilégier la flexibilité.

Il est worth de noter qu'il ne s'agit pas seulement des applications. Les [solutions clés en main hébergées](https://aws.amazon.com/cloudwatch/) peuvent résoudre des préoccupations transversales telles que la surveillance et la journalisation. Pourtant, celles-ci peuvent être remplacées par des solutions open-source conteneurisées qui sont [plus faciles](https://technologyconversations.com/2016/10/24/forwarding-logs-from-all-containers-running-anywhere-inside-a-docker-swarm-cluster/) à configurer et vous laissent dans une meilleure position pour éviter la [prison du cloud](http://firstround.com/review/the-three-infrastructure-mistakes-your-company-must-not-make/).

### Orchestration

La question n'est pas de savoir si vous **avez besoin** d'un système d'orchestration ou non. Il s'agit de savoir si vous voulez qu'il soit auto-géré ou si vous voulez être l'orchestrateur humain qui corrige un temps d'arrêt à 3 heures du matin.

L'analogie est de devoir prendre soin de nombreuses pièces mobiles. Les systèmes logiciels deviennent plus complexes et fragmentés à l'exécution. Ils deviennent fragiles face au partitionnement du réseau.

Maintenant, les conteneurs seuls ne résolvent pas ce problème — en fait, c'est plutôt le contraire. Leur nature éphémère rend votre système très dynamique. Cela rend difficile la définition des dépendances au moment du déploiement.

Passez à une infrastructure en cluster, et la situation s'aggrave. Cela atteint le point où vous n'êtes jamais certain de l'endroit où vos processus pourraient finir par s'exécuter. Cela rend leur localisation et leur traitement d'autant plus difficiles. Mais c'est le besoin d'embrasser cette nature qui donne lieu à une multitude de solutions.

Nous avons essayé plusieurs systèmes de clustering. Ceux-ci incluaient Kubernetes de Google, Marathon de Mesosphere et Nomad de Hashicorp.

Nous nous sommes installés sur [Docker Swarm](https://github.com/docker/swarm) de Docker pour la plupart de nos déploiements en utilisant le simple modèle Docker pour AWS CloudFormation [template](https://docs.docker.com/docker-for-aws/).

Exprimez d'abord de manière déclarative l'état souhaité de votre système concernant les services qu'il doit exécuter. Ensuite, Swarm surveillera constamment l'état réel de vos conteneurs. Il réconciliera l'état souhaité en reprogrammant la charge de travail sur d'autres nœuds en cas de défaillance d'un nœud. Il guérira également le cluster en réapprovisionnant de nouveaux serveurs si un nœud devient irréparable.

La provision de votre propre cluster de conteneurs peut échapper à vos besoins. Cependant, de nouvelles plateformes [Caas](http://searchitoperations.techtarget.com/definition/Containers-as-a-Service-CaaS) (Containers-as-a-Service) apparaissent souvent sans coût supplémentaire par rapport à l'utilisation de votre infrastructure sous-jacente.

![Image](https://cdn-media-1.freecodecamp.org/images/1*p2d6GDAtrpRQr2UzZX91zw.png)
_Qui a besoin de chatons quand on a des baleines cartoon._

Vous trouverez la découverte de services, l'équilibrage de charge, les réseaux définis par logiciel, le stockage persistant, la planification des tâches et le consensus RAFT. Cela garantit un voyage effrayant mais amusant à travers un tourbillon de jargon à la sonorité cool.

### Réduire votre facture d'infrastructure

Vous n'avez pas besoin d'un autre article sur "Comment nous avons réduit nos coûts de serveur de `{{ rand_amount }}` après être passés à `{{ rand_language }}`". Donc, je vais essayer de proposer quelque chose de différent.

Les microservices sont très en vogue ces jours-ci. Nous avons divisé nos applications en plusieurs services différents ici chez [Beta Labs](https://medium.com/@betalabs). Cette approche nous permet de mélanger et d'assortir différents langages et frameworks. Cela nous garde libres de travailler avec le meilleur outil pour le travail à chaque fois.

Veuillez me supporter. J'essaie de faire un plaidoyer pour les microservices en 10 mots ou moins.

Suivant le principe de 12factor "[Un codebase, plusieurs déploiements](https://12factor.net/codebase)", cela signifie que chaque service doit être déployé en tant que sa propre application en termes de PaaS. C'est ainsi que la plupart des modèles de tarification PaaS évoluent.

Lançons quelques chiffres. Exécuter une configuration disponible pour une application Ruby dans Heroku signifie exécuter au moins deux web Standard 1X [dynos](https://devcenter.heroku.com/articles/background-jobs-queueing). Cela vous coûtera 50 $ par mois pour un total de 1 application limitée à 512 Mo de mémoire.

Cela fait 50 $ par mois pour les services front-end. Ajoutez un worker dyno pour un simple traitement en arrière-plan, et cela fait 25 $ de plus par mois.

Vous pourriez également vouloir quelques services back-end légers, comme un middleware ou un broker avec une logique personnalisée, qui pourraient se contenter de 1 instance chacun. Vous pourriez facilement dépasser les 100 $ par mois.

Cela, avant même de parler des add-ons. Ajoutez 30 $ de plus par mois pour une instance Redis et PostgreSQL de base. Le Logplex de Heroku est uniquement pour le streaming. Donc, si vous voulez conserver vos logs un peu plus longtemps, vous voudrez également ajouter un service de journalisation qui peut être [partagé](https://devcenter.heroku.com/articles/managing-add-ons#using-the-command-line-interface-attaching-an-add-on-to-another-app) entre les applications.

Voyons comment nous pourrions faire mieux.

![Image](https://cdn-media-1.freecodecamp.org/images/1*S1kWdAuHYbxc7sUW7k-0hA.png)
_Une VM par service (monolithique) vs. plusieurs services (micro) par VM. Crédit : [Martin Fowler](http://martinfowler.com" rel="noopener" target="_blank" title=")_

Empruntons à la description de Martin Fowler des [microservices](https://martinfowler.com/articles/microservices.html). L'utilisation combinée de conteneurs avec un système de clustering fournit une plateforme belle et adaptée pour le scaling dynamique de vos services.

Nos conteneurs sont placés sur des nœuds avec les ressources les plus disponibles. Tous les nœuds partagent un [SDN](http://www.webopedia.com/TERM/S/software_defined_networking.html) (Software Defined Network) interne. Ainsi, vos services peuvent communiquer entre eux sans quitter le cluster.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ECJp2DdJnM5u0Hvv_EfGwQ.png)
_Un cluster Swarm de 3 nœuds exécutant l'exemple-voting-app_

Revenons à notre exemple précédent. Un tel système pourrait tenir sur un cluster Docker Swarm de 3 nœuds basé sur t2.micro, ce qui coûte environ [50 $ par mois](https://calculator.s3.amazonaws.com/index.html#r=IAD&s=EC2&key=calc-0351D66A-E96F-4871-B9C8-1F42BF37FDCC). Vous pourriez avoir un total de 3 Go de mémoire. Vous pourriez même avoir une marge supplémentaire pour exécuter vos propres instances Redis conteneurisées, si vous vous sentez audacieux.

Les dynos de Heroku sont beaucoup plus performants en termes de CPU avec 8 cœurs virtuels contre 1. Mais à moins que vous n'exécutiez un langage avec des threads natifs, une configuration multi-processus par dyno pourrait vous faire trouver 512 Mo de mémoire insuffisants rapidement. De plus, cela ne fera pas une grande différence si votre charge de travail est intensive en I/O.

Ne vous méprenez pas, en ce qui concerne la simplification de DevOps, cela ne devient pas beaucoup mieux que Heroku. Je ne suggère pas que vous ou quelqu'un dans votre équipe devriez vous lancer seul et passer des nuits à apprendre à configurer des setups de haute disponibilité dans PostgreSQL. Nous comparerions des pommes et des oranges.

Je pense néanmoins qu'il est important de souligner que vous **payez** un supplément pour toute cette fiabilité et cette facilité d'utilisation. Avec cela, vous pouvez juger par vous-même ce qui vaut vraiment le prix et ce que vous pouvez faire vous-même.

Oh, tant que nous y sommes, n'oubliez pas que vous pouvez [exécuter vos conteneurs Docker](https://devcenter.heroku.com/articles/container-registry-and-runtime) dans Heroku.

#### Sécurité inhérente

Cet argument ne tiendra pas beaucoup la route lors de la comparaison de la plateforme Docker à un PaaS. Pourtant, vous constaterez que vous réduisez le risque de certaines vulnérabilités par rapport à votre boîte Ubuntu exécutant plusieurs applications.

Pourquoi est-ce différent ? Entrez les conteneurs Linux. Un concept intrigant autrefois présenté par des entreprises comme Heroku lors de la lecture de leurs guides se trouve désormais au cœur même de Docker. Et avec eux vient une fonctionnalité de sécurité très appréciée : l'isolation.

Prenez le pire scénario où quelqu'un exécute du code à distance à l'intérieur de votre serveur. Cela semble trop tiré par les cheveux ? Consultez [ImageTragick](https://imagetragick.com/). Les applications tendent à avoir une relation un-à-un avec les conteneurs. Vous devriez pouvoir isoler les dommages au domaine de cette application, gardant tout ce que vous choisissez d'exécuter sur vos hôtes en sécurité.

C'est une caractéristique similaire à ce que les VMs ([Machines Virtuelles](https://en.wikipedia.org/wiki/Virtual_machine)) ont fourni depuis assez longtemps. Mais elles ont toujours eu une nature légèrement plus rigide avec des temps de démarrage et de provisionnement plus longs, plus l'overhead d'exécuter des systèmes d'exploitation complets.

On pourrait presque être pardonné de leur donner des cycles de vie plus longs et de les traiter davantage comme des [Animaux de compagnie que du Bétail](http://cloudscaling.com/blog/cloud-computing/the-history-of-pets-vs-cattle/), mais l'exécution de plus d'applications de cette manière conduit à la compromission potentielle de plus de secrets.

Bien que l'exécution d'applications conteneurisées réduise ce risque, cela ne signifie pas que vous serez immunisé contre les mauvaises pratiques des développeurs. Vous ne voudriez pas compromettre l'accès au [Docker daemon](https://github.com/dockersamples/docker-swarm-visualizer/blob/master/docker-compose.yml#L7) de l'hôte, par exemple. Mais dans l'ensemble, les environnements conteneurisés aident à réduire votre surface d'attaque en tant qu'organisation.

Soyez simplement prudent et [ne](https://avicoder.me/2016/07/22/Twitter-Vine-Source-code-dump/) gardez pas vos images publiques (coup bas, je sais).

### _Vous en avez envie_

D'accord, cela pourrait être complètement biaisé par ce que nos geeks intérieurs trouvent motivant, mais...

Nous ne pouvons pas dire que nous n'avons pas dû travailler autour de certains angles rugueux au début. Je dois admettre être attiré par les outils hipster plutôt facilement.

On devrait pouvoir ajouter de nouveaux outils à l'arsenal si on sent que cela contribuera à son bonheur en tant qu'ingénieur. N'était-ce pas une partie du point de vente pour les startups en premier lieu ?

Si vous décidez de ne pas utiliser Docker, vous constaterez presque certainement que le fait d'être un peu compétent en matière de conteneurs sera utile dans les [années à venir](https://www.linux.com/news/5-next-gen-cloud-technologies-you-should-know).

### Conclusion

Alors, était-ce une route lisse comme de la soie vers le paradis des conteneurs ? Pas du tout.

Aurions-nous pu nous contenter d'outils plus stables jusqu'à ce que les angles rugueux de Docker soient complètement polis ? Probablement.

Aurions-nous complètement échoué en tant que startup si nous n'avions pas adopté Docker ? Très certainement pas.

Investirions-nous à nouveau dans l'adoption de conteneurs ? Un **oui** retentissant s'impose.

Ces points sont loin d'être exclusifs aux startups. Je dirais même que la taille de l'entreprise est presque irrélevante. Soyez assuré, mon approbation ne compromettra pas la réputation de Docker parmi les types d'entreprises soit.

Nous ne préconisons pas que Docker est le **seul** moyen de résoudre ces problèmes intemporels. Et nous n'avons pas beaucoup parlé de ses inconvénients.

Mais pour l'instant, c'est **bien** la solution la plus proche de tout-en-un pour tous les problèmes courants que nous avons présentés ci-dessus.

Dans l'ensemble, il est assez sûr de dire que les conteneurs sont là pour rester — oh attendez, avez-vous entendu parler de ce truc **serverless** ? À y penser, les conteneurs sont si vieux jeu...

Merci d'avoir lu ! N'hésitez pas à laisser un commentaire si vous avez des pensées ou des questions. Si vous avez trouvé cet article utile, quelques applaudissements signifieraient beaucoup !