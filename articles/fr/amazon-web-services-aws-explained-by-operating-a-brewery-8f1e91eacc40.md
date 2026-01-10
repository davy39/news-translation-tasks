---
title: Amazon Web Services (AWS) expliqué par le fonctionnement d'une brasserie
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-31T00:09:02.000Z'
originalURL: https://freecodecamp.org/news/amazon-web-services-aws-explained-by-operating-a-brewery-8f1e91eacc40
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QGoJbSOAuIoW-bkOxyY8iQ.jpeg
tags:
- name: AWS
  slug: aws
- name: education
  slug: education
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Amazon Web Services (AWS) expliqué par le fonctionnement d'une brasserie
seo_desc: 'By Kevin Kononenko

  If you understand how a brewery works, then you can understand Amazon Web Services
  (AWS).


  _Photo by [Unsplash](https://unsplash.com/photos/5sAzXev5-jA?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopen...'
---

Par Kevin Kononenko

#### **Si vous comprenez comment fonctionne une brasserie, alors vous pouvez comprendre Amazon Web Services (AWS).**

![Image](https://cdn-media-1.freecodecamp.org/images/1*QGoJbSOAuIoW-bkOxyY8iQ.jpeg)
_Photo par [Unsplash](https://unsplash.com/photos/5sAzXev5-jA?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Elevate</a> sur <a href="https://unsplash.com/search/photos/brewery?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Lorsque vous travaillez sur la construction de votre première application web, vous entendez TOUJOURS parler de la facilité de lancer un nouveau produit par rapport aux années passées.

Les gens diront des choses comme, _"De mon temps, il fallait acheter son propre serveur et le configurer soi-même !"_

Ou encore, _"Nous passions des nuits blanches à déboguer le dernier problème avec notre infrastructure serveur."_

Heureusement, ces jours sont révolus. Vous pouvez déployer votre nouvelle application web pour 10 $ par mois en moins d'une heure, si vous savez ce que vous faites.

Mais il y a un petit problème. Des outils standard comme Amazon Web Services (AWS) peuvent être assez compliqués, du moins pour un débutant. Bien qu'ils offrent la capacité incroyable de passer de vos premiers utilisateurs à des centaines de millions d'utilisateurs... ils nécessitent également une certaine configuration.

Je voulais en savoir plus sur toutes les principales options qu'offre AWS. Après y avoir réfléchi pendant quelques heures, j'ai réalisé que l'écosystème AWS est similaire à toutes les différentes parties d'une brasserie à grande échelle.

Voici un rapide aperçu :

![Image](https://cdn-media-1.freecodecamp.org/images/0*vdBGfOwhkhaQ2lTd)

Alors, voici comment 5 outils populaires d'AWS fonctionnent en coulisses d'une application web. J'expliquerai également [Heroku](http://heroku.com/), un outil populaire pour déployer des applications web qui offre moins de flexibilité mais qui est plus facile à prendre en main.

La vidéo officielle d'AWS donne un peu de contexte sur les outils que nous allons discuter :

Pour comprendre ce tutoriel, vous devez simplement comprendre le concept du [modèle client-serveur](https://blog.codeanalogies.com/2018/02/02/localhost-explained-by-trying-to-start-a-microbrewery/), que vous pouvez [apprendre ici](https://blog.codeanalogies.com/2018/02/02/localhost-explained-by-trying-to-start-a-microbrewery/).

#### Le Contexte d'Amazon Web Services

Imaginons que vous êtes passionné par la fabrication de bière. Vous commencez dans votre cuisine en brassant pour vous-même et vos amis. Bientôt, la nouvelle de votre délicieux travail se répand. Afin de répondre à la demande croissante, vous décidez de louer du matériel et un espace dans un entrepôt pour voir si vous pouvez créer une entreprise à part entière. Vous prendrez des commandes de la part de distributeurs, de restaurants et d'entreprises indépendantes.

![Image](https://cdn-media-1.freecodecamp.org/images/0*2zJ-RgXq4mX3eN-t)

Dans l'exemple ci-dessus, une commande arrive d'un **client** — l'un des restaurants ou distributeurs. Cela s'appelle une **requête**. Votre brasserie fournira la commande et collectera le paiement via une facture. Cela s'appelle la **réponse**.

De même, les navigateurs web envoient des requêtes aux serveurs en fonction des actions des utilisateurs. Le serveur retourne les informations requises via une réponse.

![Image](https://cdn-media-1.freecodecamp.org/images/0*MsF4PEVc5qVit5Xc)

Ce n'est bien sûr qu'une vue d'ensemble. Nous allons approfondir tous les différents processus qui se produisent côté **serveur** dans notre exploration d'AWS. Dans notre analogie de la brasserie, nous supposons que les commandes arrivent déjà de tous côtés. Il est maintenant de notre responsabilité d'organiser toute une brasserie afin de pouvoir livrer ces commandes de manière fiable.

### Heroku Expliqué — Une Alternative Bien Plus Simple à AWS

Avant d'aborder les 5 parties d'AWS, vous devriez probablement connaître l'alternative plus simple. Heroku gère beaucoup de ces systèmes pour vous. En fait, il est construit sur l'infrastructure AWS.

Heroku vous permet de déployer de nouvelles versions de votre application directement depuis votre ligne de commande en utilisant _git push heroku master_. Il dispose également d'une [bibliothèque riche d'add-ons](https://elements.heroku.com/addons) qui vous permettent d'ajouter de nouvelles fonctionnalités à vos _dynos_, ou serveurs virtuels.

Heroku est un peu comme engager un entrepreneur tiers pour gérer votre brasserie. Tout ce que vous avez à faire est de fournir les recettes, et cet entrepreneur utilisera son expertise en exploitation de brasserie pour produire la bière. Ils fournissent l'équipe, l'équipement et les relations avec les fournisseurs.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ho0-aZixv74gV3-v0RbTyA.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*dosvXrcjnrJ9UetnJVZTyw.jpeg)

Cela peut sembler miraculeux. Maintenant, vous pouvez sauter tout ce temps et cette énergie douloureux que vous auriez dû consacrer à apprendre à gérer une brasserie ! Mais il y a deux raisons d'être prudent.

1. Cette approche sera plus coûteuse. Vous payez l'entreprise pour son expertise en plus du coût des salaires, des matières premières, etc.
2. Ils peuvent ne pas s'adapter comme vous le souhaiteriez. Imaginons que vous commencez à recevoir des millions de dollars de commandes et que vous devez développer votre activité. Ils peuvent ne pas être prêts à s'adapter aussi rapidement que vous.

Heroku présente les mêmes avantages/inconvénients. Il est un peu plus cher mais permet de commencer immédiatement. Si vous vous développez, vous devrez peut-être migrer vos services vers AWS, ce qui signifie que vous devrez apprendre le système AWS de toute façon.

Avec cela, explorons les différents outils au sein d'AWS.

### Outils de Stockage AWS

Ceci est la première de trois catégories qui vont sembler similaires, alors accrochez-vous ! Dans notre brasserie, il y a beaucoup d'**actifs statiques** qui ne changent pas mais qui sont nécessaires pour tout type de brassage. Pensez aux machines, à la chaîne de montage ou aux outils électriques que les travailleurs utilisent. Vous ne pouvez pas démonter et recombiner ces éléments. Mais ils peuvent être utilisés encore et encore et rester utiles.

C'est un peu comme [Amazon S3](https://en.wikipedia.org/wiki/Amazon_S3). S3 est le service cloud qui vous permet de stocker des actifs statiques comme des images. Il signifie Simple Storage Service.

![Image](https://cdn-media-1.freecodecamp.org/images/1*e9abmVhUIIGeLSkYlbHb6Q.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*n053ea_uJrzL4Wb0kBmp8A.jpeg)

Le concept de "stockage d'actifs statiques", dans ce cas, est un peu différent de ce que vous pourriez penser dans la vie réelle. Dans la vie réelle, stocker des objets statiques pourrait signifier mettre quelque chose dans un grenier et l'oublier. Mais en ce qui concerne les services cloud, cela signifie préparer un objet ou une image à être utilisé en quelques millisecondes.

C'est différent du stockage de base de données, car les données dans une base de données peuvent être **interrogées**. Les actifs statiques ne peuvent être que **demandés**.

### Services de Base de Données AWS

Amazon Relational Database Service (RDS) vous permet de configurer et d'exploiter votre base de données relationnelle au sein d'AWS. Certains exemples courants incluent MySQL, PostGreSQL et Microsoft SQL Server.

Dans notre exemple de brasserie, cela ressemble un peu aux parties de la brasserie qui stockent les bouteilles, les étiquettes, le houblon, le malt et tout autre ingrédient dont vous aurez besoin pour fabriquer la bière. Et je suppose que cela inclurait également le compte bancaire de votre entreprise, puisque c'est une forme de stockage dynamique.

Vous vous demandez peut-être pourquoi nous parlons à nouveau de stockage après la section précédente. C'est parce que tous ces éléments sont beaucoup plus dynamiques — ils sont constamment combinés ou modifiés pour traiter les requêtes des utilisateurs/clients.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ci_kNJOcrUCpn0mcW6VHqg.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*wWmbObMp__nfxL14zzW3cQ.jpeg)

C'est le type de données que vous allez **interroger**, plutôt que de les demander, comme dans l'exemple précédent. Si vous gériez les bases de données pour Facebook, par exemple, cela inclurait les données utilisateur et les publications qui seraient ensuite incluses dans le Fil d'Actualité.

Une dernière remarque : ces données (ou houblon/malt/bouteilles) ne sont utiles que pour livrer une réponse à l'utilisateur. Si vous vouliez mesurer la performance de votre brasserie, vous devriez mettre en place un nouveau processus pour votre équipe d'exploitation.

Imaginez si votre équipe d'exploitation courait frénétiquement dans votre brasserie, essayant de suivre vos performances tandis que les travailleurs normaux essayaient de produire et de mettre en bouteille autant de bière que possible. Ces deux équipes ont des intérêts séparés.

C'est là que l'entrepôt de données entre en jeu.

### Outils d'Entrepôt de Données AWS

Clarifions une chose ici : "entrepôt de données" est un nom terrible pour un service cloud. D'accord, cela peut avoir du sens pour un développeur avec des années d'expérience, mais pour un débutant... combien de choses dans le développement web ressemblent à un entrepôt ? BEAUCOUP.

Un exemple courant de [produit d'entrepôt de données](https://en.wikipedia.org/wiki/Data_warehouse) est [Redshift](https://en.wikipedia.org/wiki/Amazon_Redshift). Ces types d'outils facilitent l'analyse des données par les développeurs. Ils incluent des données de bases de données relationnelles, ainsi que des données ERP, CRM et d'automatisation marketing.

Revenons à notre analogie de la brasserie. Jusqu'à présent, dans notre brasserie, toutes nos "données" ne sont pas dans un format très accessible. Elles sont sous forme de bouteilles, de sacs de houblon et de toutes les autres matières premières qui traînent dans l'installation. Un analyste devrait compter manuellement tous ces objets physiques s'il voulait analyser l'efficacité de l'usine.

Vous avez besoin d'un moyen de convertir ces données physiques en données lisibles par machine, que votre équipe d'exploitation peut utiliser pour rendre la brasserie plus efficace. Pensez à cela comme à un système de capteurs autour de l'installation. Les capteurs convertissent le mouvement physique des matières premières en données lisibles par machine, qui peuvent ensuite être analysées.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EySamZAufAFciP0g2y3U8g.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*AtoYuA5nKYjrwlOEBNL0gQ.jpeg)

Ainsi, maintenant, alors que notre usine fonctionne, les données sont automatiquement collectées et partagées avec l'équipe d'exploitation de l'usine afin qu'ils puissent analyser l'efficacité.

Voyez-vous comment cela réduit le stress à la fois pour l'usine et l'équipe de production ? L'équipe de production peut se concentrer sur la fabrication de la bière sur le terrain tandis que l'équipe d'exploitation peut analyser depuis leur bureau. C'est une bonne raison d'utiliser également un outil d'entrepôt de données. Il réduit le nombre de requêtes sur votre base de données, ce qui peut ralentir les performances.

Espérons que vous voyez pourquoi l'outil "entrepôt de données" est légèrement trompeur. Oui, cela crée un nouvel ensemble de données strictement pour l'analyse. Mais il est difficile de dire pourquoi il est plus "semblable à un entrepôt" que toute autre partie du système.

### Outils de Calcul AWS

Dans tous les diagrammes jusqu'à présent, avez-vous remarqué que "brasserie" est au milieu, que le diagramme montre une brasserie réelle ou un environnement de cloud computing ?

C'est parce que nous n'avons pas encore couvert le service qui relie tout cela : [EC2, ou Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html). EC2 vous permet de lancer des instances virtuelles, qui sont un peu comme la brasserie dans cette analogie.

Les instances sont des **serveurs virtuels**. Contrairement aux technologies précédentes, où votre code était lié à un serveur physique, les serveurs virtuels vous permettent de lancer votre propre environnement dans le cloud, qui est composé de nombreux serveurs connectés. C'est la partie qui relie tous les autres services AWS ensemble.

C'est un peu comme pouvoir démarrer ou arrêter une nouvelle brasserie à tout moment dans n'importe quelle partie du monde en copiant votre brasserie existante. Cela peut ne pas être possible dans la vie réelle, mais c'est possible dans l'écosystème AWS. EC2 fournit une fonctionnalité similaire à la fois à l'espace physique et aux travailleurs de la brasserie.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TbPj10B8QH10Dx_tiIC-Iw.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*l0y3g0gR4MUX7O8t5HhVvA.jpeg)

Le diagramme peut être légèrement trompeur, car un serveur virtuel n'occupe pas un serveur entier. Il existe au sein d'un réseau de serveurs. Mais c'était trop compliqué à montrer dans un petit diagramme. Alors je l'ai gardé.

### Outils de Gestion AWS

La dernière catégorie d'outils est celle des outils de gestion, comme Elastic Beanstalk ou CloudWatch. Ces outils peuvent :

1. Surveiller les autres outils listés ci-dessus
2. Mettre en place des processus pour aider les outils de plusieurs catégories à travailler ensemble

![Image](https://cdn-media-1.freecodecamp.org/images/0*V5AvyPtgGhHLXZF2)
_Crédit Image : FreeCodeCamp_

Dans le graphique ci-dessus, vous pouvez voir comment de nombreux outils peuvent aider à déployer et maintenir votre application. C'est pourquoi ces outils sont similaires à l'équipe de gestion de l'entreprise. Ils ne produisent pas personnellement de la bière pour votre entreprise, mais ils aident plutôt toutes les divisions à travailler ensemble.

Il existe une grande variété d'outils dans la catégorie de gestion, donc je ne vais pas couvrir un outil individuel en profondeur. Ils se situent à un niveau au-dessus des autres outils discutés.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8hrWANJasTDpQaERaaF-aQ.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*d_Kx52WUCIS0tYPVGHm18Q.jpeg)

### Obtenez les Derniers Tutoriels Visuels

Avez-vous aimé ce tutoriel ? Donnez-lui un "clap", ou inscrivez-vous ici pour recevoir mes dernières explications sur le développement web.