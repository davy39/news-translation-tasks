---
title: Comment optimiser les coûts de votre architecture cloud AWS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-15T18:45:44.000Z'
originalURL: https://freecodecamp.org/news/cost-optimization-in-aws
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/bram-naus-n8Qb1ZAkK88-unsplash-1.jpg
tags:
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
- name: Cloud Services
  slug: cloud-services
- name: optimization
  slug: optimization
- name: software architecture
  slug: software-architecture
seo_title: Comment optimiser les coûts de votre architecture cloud AWS
seo_desc: 'By Sumeet Ninawe

  In this article, I''ll highlight what I mean by optimizing your costs in AWS cloud
  architecture. Then I''ll share how you can do it with respect to the AWS Well-Architected
  framework.

  The Problems of Maintaining IT Architecture

  The tra...'
---

Par Sumeet Ninawe

Dans cet article, je vais souligner ce que j'entends par optimisation des coûts dans l'architecture cloud AWS. Ensuite, je partagerai comment vous pouvez le faire en respectant le cadre AWS Well-Architected.

## Les problèmes de maintenance de l'architecture IT

La maintenance traditionnelle de l'infrastructure IT n'était pas très, hmm, efficace ? Je n'ai pas vraiment les mots pour décrire ce problème, surtout parce que je ne comprendrai jamais la douleur de gérer des centres de données sur site.

Mais cela implique la fourniture de l'infrastructure, l'installation du système d'exploitation et des applications, la configuration du réseau dans un enchevêtrement de câbles, la surveillance constante des performances, et bien plus encore.

Imaginez l'effort nécessaire juste pour garder ces centres de données en fonctionnement – l'approvisionnement, les opérations, la construction d'installations spéciales pour maintenir les serveurs en marche, la reprise après sinistre, et ainsi de suite. Cela peut prendre des semaines, voire des mois, pour mettre à l'échelle cette infrastructure traditionnelle.

Ce type de situation influence également le développement des applications. Les anciennes applications étaient souvent construites comme des monolithes et le risque global d'échec était élevé. Quel était votre entreprise à nouveau ?

## Comment le cloud computing aide

L'émergence de fournisseurs de cloud comme AWS a changé cette équation. Imaginez ne pas avoir à faire tout ce qui précède par vous-même. Au lieu de cela, une équipe d'experts le fait pour vous à un coût.

Le cloud computing fait exactement cela. Il a également introduit de nouvelles façons de construire des applications. Les applications développées en utilisant les capacités du cloud sont appelées applications cloud-native.

Comme je l'ai mentionné précédemment, tout cela a un coût. Mais si vous comparez ces coûts avec la manière dont l'infrastructure traditionnelle était gérée, c'est toujours moins cher.

Pourtant, ce n'est pas tout – cela pourrait être encore moins cher si vous gérez vos services cloud de manière judicieuse. L'optimisation des coûts est l'un des piliers du cadre AWS Well-Architected. Cela décrit des moyens d'optimiser les coûts, non seulement en construisant des applications cloud-native, mais aussi d'autres aspects organisationnels.

Les ressources cloud sont scalables, facilement gérées, avancées, fiables, sécurisées, rentables et hautement disponibles. Vous n'avez pas besoin de provisionner et de payer pour des machines virtuelles haute performance dès le début pour gérer quelques pics de trafic au début. Ce serait un scénario typique de lift and shift.

## Calculez vos coûts cloud

Si vous êtes nouveau dans le cloud ou prévoyez de migrer vos charges de travail existantes vers AWS, AWS propose un service utile pour calculer le coût total de possession (TCO). Il compare le déploiement sur site avec les coûts que vous devriez payer dans le cloud.

Le calculateur TCO prend en compte des aspects comme les coûts de stockage, les coûts réseau, les coûts des serveurs et les coûts opérationnels. Il vous fournit également une estimation pour un arrangement de lift and shift.

Les estimations fournies par les calculateurs TCO peuvent être encore réduites en mettant en œuvre les piliers d'optimisation des coûts dans les architectures cloud, comme :

1. Dimensionnement approprié
2. Élasticité accrue
3. Choix du bon modèle de tarification
4. Adaptation à la demande
5. Mesure et surveillance

## Liste de contrôle pour l'optimisation des coûts

### Dimensionnement approprié

Il est très important de comprendre les exigences de capacité de votre application et de ses fonctions. Deviner la capacité entraîne généralement un déséquilibre – nous finissons par provisionner moins, ce qui pourrait nous faire perdre des clients, ou nous finissons par provisionner plus, ce qui nous fait payer plus que nécessaire.

En règle générale, vous devriez commencer petit et surveiller votre utilisation pendant un certain temps pour établir une tendance. Sur la base de cette tendance, vous pouvez augmenter l'échelle et acheter des instances réservées ou de la capacité, ce qui peut aider à économiser jusqu'à 75 % des coûts de calcul.

### Élasticité accrue

Pour accommoder automatiquement les pics de trafic occasionnels, il est important de mettre en œuvre une architecture cloud élastique. Cela permet aux groupes d'auto-scaling de s'adapter en fonction de vos besoins. C'est là que vous adaptez la capacité à la demande.

Bien sûr, cela n'est pas possible sans surveiller votre utilisation actuelle. La surveillance vous aide à comprendre les exigences de calcul au fil du temps et vous permet de définir des seuils. Vous pouvez utiliser les événements générés de cette manière pour prendre des mesures d'échelle.

### Choix du bon modèle de tarification

Chaque service offert par AWS est accompagné d'un modèle de tarification. Dans le cas du calcul et du stockage, AWS propose divers types de modèles de tarification qui, en essence, définissent les termes des services gérés.

Dans le cas des instances EC2, le modèle de tarification définit la disponibilité et l'accès à divers niveaux. Par exemple, les instances à la demande peuvent être créées et détruites à tout moment. D'autre part, les instances réservées sont des instances fixes à long terme qui entraînent des dépenses moins élevées.

Il existe d'autres modèles de tarification, comme les instances Spot, les instances dédiées, les hôtes dédiés, et plus encore.

### Adaptation à la demande

AWS Auto Scaling peut être utilisé pour adapter la demande afin que vous payiez moins pour les périodes où vous n'êtes pas actif et ne payez que pour les périodes où la demande augmente. Pendant cette période, vous pouvez également utiliser des instances réservées pour réduire davantage vos coûts en vous engageant à long terme. C'est un exemple d'optimisation des coûts.

Le passage au cloud appelle également à un changement culturel dans les organisations, surtout lorsqu'il s'agit d'optimisation des coûts. Les équipes doivent être sensibilisées au fonctionnement du cloud et aux ressources gérées à utiliser dans divers scénarios.

Vous pouvez former un Cloud Centre of Excellence (CCoE) pour travailler à travers les verticales afin de surveiller et de suggérer de meilleures façons de mettre en œuvre les principes d'optimisation des coûts ci-dessous.

1. Définir et appliquer le marquage
2. Structures de compte efficaces
3. Concevoir et utiliser des métriques
4. Concevoir des architectures basées sur les coûts

## L'importance du marquage

Pour gérer les coûts et répondre aux questions liées aux dépenses, vous devez effectuer le marquage comme une meilleure pratique. Le marquage des ressources nous permet d'avoir une meilleure visibilité et un contrôle plus granulaire sur nos dépenses cloud.

Des formats de marquage standard doivent être définis et appliqués pour chaque organisation lors de la création de ressources cloud. Le format peut définir des aspects comme le projet, les unités de portefeuille, les équipes, et ainsi de suite au niveau organisationnel.

En allant plus loin, des conventions basées sur les projets peuvent également être définies pour représenter les services soutenus par diverses ressources cloud. Cependant, soyez conscient du nombre de balises que vous choisissez – il ne devrait pas y avoir trop ou trop peu de balises définies. En général, les balises peuvent être catégorisées en deux groupes :

1. **Technique** – représentant les détails techniques comme l'automatisation, la sécurité, et ainsi de suite.
2. **Stratégique** – représentant les détails organisationnels comme un centre de coût, le contrôle d'accès, la gouvernance, et ainsi de suite.

## Comment suivre vos coûts de cloud computing

Il existe plusieurs façons de suivre ce que vous dépensez en cloud computing. Examinons les principales maintenant.

### Cost Explorer

AWS propose quelques services très utiles comme **Cost Explorer** qui vous donne un aperçu de vos dépenses cloud au fil du temps. Il offre une interface visuelle agréable représentant les coûts mensuels ou quotidiens. Il vous donne également un tableau de bord par défaut représentant les coûts mensuels encourus par service.

AWS Cost Explorer vous aide à générer et exporter des rapports de coûts à un niveau élevé ainsi que des rapports granulaires et spécifiques. Vous pouvez construire vos rapports et tableau de bord en fonction de vos intérêts et de votre focus.

Cost Explorer vous aide à définir des budgets qui aident à surveiller vos coûts. Les budgets sont un excellent moyen de garder vos coûts sous contrôle. En utilisant les budgets, vous pouvez définir une ligne de base de dépenses dans AWS et configurer des notifications de dépassement de seuil.

Par exemple, si les coûts dépassent plus de 80 % du budget de base, vous pouvez choisir de recevoir une notification qui vous aidera ensuite à prendre des mesures.

Cost Explorer vous donne également des recommandations de dimensionnement approprié qui vous aident à identifier où vous pourriez provisionner plus que l'infrastructure requise en termes de type d'instance, de modèle de tarification, et ainsi de suite.

### QuickSight

Si vous avez besoin d'un outil de reporting plus détaillé, AWS propose son service **QuickSight**. Il s'agit d'une solution d'analyse commerciale pour le reporting des coûts. Il est rapide et hautement scalable et inclut des capacités de ML.

Vous pouvez explorer, analyser et collaborer sur des sujets de dépenses de coûts de manière beaucoup plus efficace. Cependant, ce n'est pas un service gratuit comme Cost Explorer et il fonctionne sur une base de paiement par session.

### AWS Trusted Advisor

**AWS Trusted Advisor** est un service qui incarne un service virtuel d'AWS qui vous conseille sur le cadre. Il effectue une série de vérifications avec les meilleures pratiques AWS et les met en évidence dans le format ci-dessous si des actions sont requises.

1. aucun problème détecté – signifiant que la mise en œuvre est conforme aux normes requises.
2. investigation recommandée – pour les avertissements.
3. action recommandée – pour tout aspect qui est totalement hors de propos.

AWS Trusted Advisor surveille en continu combien de vos ressources provisionnées vous avez utilisées et génère des recommandations. Dans le cas de l'optimisation des coûts, il met en évidence si des ressources sont sous-utilisées, si des instances sont inactives, si des instances réservées vont expirer, et plus encore.

### AWS CloudFront

Vous n'avez pas toujours à attendre qu'AWS Trusted Advisor conseille sur les optimisations avant de prendre des mesures. **AWS CloudFront** est un service qui fournit des métriques de ressources que nous pouvons utiliser pour surveiller les performances nous-mêmes et identifier les ressources sous-utilisées.

AWS CloudWatch est le moyen le plus simple de collecter des métriques puisqu'il s'intègre directement avec plusieurs services AWS. En obtenant une visibilité opérationnelle et des insights, vous pouvez agir sur les améliorations et optimiser les coûts.

### Tenancy des instances EC2

AWS offre diverses options pour provisionner une machine virtuelle sur leur infrastructure. Ces options sont créées pour répondre à vos besoins en fonction de la criticité de votre service.

Dans toute implémentation donnée, tous les services ne nécessitent pas de nœuds dédiés haute performance. De même, tout ne peut pas fonctionner sur des nœuds à faible calcul et moins disponibles.

Cela nous offre une opportunité d'explorer et de définir notre infrastructure de calcul la plus adaptée à l'entreprise et la plus rentable. Examinons certains des types de calcul (EC2) fournis par AWS.

1. **Instances réservées** – engagement à long terme, faible coût.
2. **Instances Spot** – très faible coût, utilise la capacité EC2 excédentaire, libérée lorsque la capacité n'est pas disponible, bonne pour les applications tolérantes aux pannes.
3. **Instances à la demande** – aucun engagement, coûts réguliers.
4. **Instances dédiées** – instances créées à partir de ressources non partagées.
5. **Hôtes dédiés** – instance dédiée avec accès aux options matérielles comme les ports.
6. **Capacité réservée** – La capacité réservée peut être achetée et utilisée dans une famille d'instances. Les instances peuvent être redimensionnées, en fonction du facteur de normalisation. Aide à réduire les coûts avec flexibilité.

En fonction de vos exigences, vous pouvez sélectionner les options appropriées ci-dessus pour héberger votre charge de travail. Par exemple, lorsque vous êtes sûr qu'un certain nœud existera à long terme, vous pouvez profiter des instances réservées au lieu des instances à la demande et économiser jusqu'à 75 % des coûts.

Il n'y a aucun intérêt à provisionner une instance à la demande pour des charges éphémères et non critiques. Les instances Spot peuvent être utilisées dans ce cas pour aider à réduire les coûts jusqu'à 90 %.

### Dimensionnement approprié du stockage AWS

AWS propose divers types de stockage et vous pouvez utiliser le stockage approprié en fonction de la fréquence à laquelle vous souhaitez que vos données soient stockées. Divers types de stockage proposés par AWS sont Objet, Bloc, Fichier, Hybride, Edge et Sauvegarde.

Prenons un exemple de stockage d'objets. Voici les classes de stockage proposées par AWS S3. La classe de stockage d'objets que vous choisissez dépendra de la fréquence à laquelle les données sont accédées et de la période de conservation requise.

1. **Stockage standard** – stockage standard, coûts réguliers, accès immédiat.
2. **Accès peu fréquent standard** – disponibilité réduite, coûts réduits.
3. **Accès peu fréquent à une zone** – redondance réduite, coûts réduits.
4. **Hiérarchisation intelligente** – pour les modèles d'accès inconnus, les données sont déplacées dans et hors de diverses classes en fonction de la fréquence d'utilisation des fichiers.
5. **Glacier** – Stockage à long terme, bon marché, minutes ou heures pour récupérer.
6. **Glacier Deep Archive** – Stockage à plus long terme, moins cher, heures pour récupérer.

Les politiques de cycle de vie peuvent être utilisées pour transférer les anciennes données vers un stockage à long terme moins cher.

Chaque type de stockage est accompagné de divers leviers que vous pouvez régler de manière appropriée pour optimiser vos coûts de stockage sur AWS. Je recommande d'utiliser le **Gestionnaire de cycle de vie des données AWS** lors du provisionnement de vos capacités de stockage.

## Une note finale

Il existe de nombreuses optimisations de coûts que vous pouvez appliquer aux ressources dans AWS, mais la manière dont vous appliquez ces optimisations dépend de vos priorités commerciales.

Principalement, vous devez décider si votre focus est sur les coûts ou sur le temps de mise sur le marché. Les principales bases de l'optimisation des coûts sont :

1. **Basé sur le temps** – pour optimiser au fil du temps.
2. **Basé sur la demande** – pour optimiser en fonction de la demande/trafic.
3. **Basé sur le tampon** – pour optimiser en fonction des charges de travail secondaires.

Le pilier d'optimisation des coûts d'un cadre bien architecturé suggère que lors de la conception, du développement et du déploiement d'applications sur AWS, il est une bonne pratique de garder l'optimisation des coûts en perspective.

Vous devriez surveiller en continu vos coûts pour tirer le meilleur parti de votre investissement cloud.

Dans cet article, nous avons discuté de divers aspects de l'optimisation des coûts cloud en relation avec le cadre AWS Well-Architected. Si vous êtes resté avec moi jusqu'à maintenant, santé à vous !

Hey, si vous aimez ce contenu, envisagez de vous abonner, de suivre et de partager cet article de blog ! [Let'sDoTech](https://letsdotech.dev), [Instagram](https://www.instagram.com/letsdotech/), [Twitter](https://twitter.com/letsdotech_dev), [LinkedIn](https://www.linkedin.com/company/letsdotech).