---
title: Comment l'auto-scaling et l'équilibrage de charge fonctionnent dans l'architecture
  logicielle
subtitle: ''
author: Daniel Adetunji
co_authors: []
series: null
date: '2024-06-17T18:52:13.000Z'
originalURL: https://freecodecamp.org/news/auto-scaling-and-load-balancing
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/image--13-.png
tags:
- name: software architecture
  slug: software-architecture
seo_title: Comment l'auto-scaling et l'équilibrage de charge fonctionnent dans l'architecture
  logicielle
seo_desc: While auto scaling and load balancing are two separate techniques in software
  architecture management, they are often implemented simultaneously. In the software
  architecture wild, one rarely exists without the other, as they complement each
  other to...
---

Bien que l'auto-scaling et l'équilibrage de charge soient deux techniques distinctes dans la gestion de l'architecture logicielle, elles sont souvent mises en œuvre simultanément. Dans le monde de l'architecture logicielle, l'une existe rarement sans l'autre, car elles se complètent pour gérer les changements imprévisibles de la demande.

Cet article expliquera comment fonctionnent l'auto-scaling et l'équilibrage de charge et pourquoi il est important de les prendre en compte dans vos conceptions. Il passera également en revue des exemples d'architectures montrant l'auto-scaling et l'équilibrage de charge en action.

## Table des matières

1. [Auto Scaling Expliqué](#heading-mise-a-lechelle-automatique-expliquee)
    
2. [Mise à l'échelle dynamique](#heading-mise-a-lechelle-dynamique)
    
3. [Mise à l'échelle planifiée](#heading-mise-a-lechelle-planifiee)
    
4. [Pourquoi utiliser l'auto-scaling](#heading-pourquoi-utiliser-lauto-scaling)
    
5. [Équilibrage de charge expliqué](#heading-equilibrage-de-charge-explique)
    
6. [Pourquoi utiliser l'équilibrage de charge](#heading-pourquoi-utiliser-lequilibrage-de-charge)
    
7. [Mettre tout ensemble – Équilibrage de charge et auto-scaling en action](#heading-mettre-tout-ensemble-equilibrage-de-charge-et-auto-scaling-en-action)
    

## Auto Scaling Expliqué

L'auto-scaling, comme son nom l'indique, est simplement un moyen de mettre à l'échelle automatiquement vos instances de calcul. Avec la plupart des fournisseurs de cloud comme AWS, GCP et Azure, vous sélectionnez des politiques de mise à l'échelle qui définissent comment il ajoutera ou supprimera des instances.

Les politiques de mise à l'échelle sont simplement des règles qui indiquent combien vous devez augmenter ou diminuer le nombre d'instances en fonction d'une métrique prédéfinie.

Les politiques de mise à l'échelle peuvent être dynamiques, par exemple, en ajoutant de nouvelles instances en fonction de l'utilisation du CPU des instances existantes. Les politiques de mise à l'échelle peuvent également être basées sur un calendrier, c'est-à-dire sur des heures spécifiques de la journée ou de la semaine où vous anticipez une demande plus élevée ou plus faible.

### Mise à l'échelle dynamique

La mise à l'échelle dynamique est idéale lorsque la demande fluctue fortement à des moments inconnus et imprévisibles. Vous savez qu'il peut y avoir une augmentation ou une diminution soudaine de la demande sur vos instances, vous ne savez simplement pas quand.

En utilisant une analogie de restaurant, imaginez une instance comme un chef qui transforme les commandes en repas. Si vous n'avez que trois chefs et que vous n'avez pas de grandes fluctuations de la demande tout au long de la journée ou de la semaine, vous n'avez rien à craindre.

Mais si votre restaurant avait une vente plus populaire que prévu, ou qu'un grand groupe de touristes descendait soudainement sur le restaurant, comment feriez-vous face ? Et si vous pouviez ajouter plus de chefs à la volée immédiatement lorsque cela est nécessaire ?

C'est ainsi que fonctionne la mise à l'échelle dynamique automatique. La mise à l'échelle dynamique fera apparaître spontanément des chefs dans la cuisine, prêts à transformer les commandes en délicieux repas, en fonction d'une métrique prédéfinie que vous pouvez choisir pour mesurer à quel point les chefs sont surchargés, c'est-à-dire à quel point ils ont du mal à remplir les commandes actuelles.

N'oubliez pas que ces politiques de mise à l'échelle sont simplement des règles. Ces règles peuvent être très simples, comme :

> *si l'utilisation du CPU est > 50 %, ajoutez une instance supplémentaire. Si l'utilisation du CPU est <50 %, supprimez une instance.*

Ces règles peuvent également être plus complexes.

Avec AWS et GCP, par exemple, vous pouvez définir une métrique de suivi cible qui surveillera les performances du CPU de votre groupe de mise à l'échelle et ajoutera ou supprimera des instances de sorte que l'utilisation moyenne du CPU corresponde approximativement à votre paramètre souhaité.

Par exemple, si vous spécifiez que vous souhaitez que l'utilisation moyenne du CPU de votre groupe de mise à l'échelle soit de 60 %, des instances seront ajoutées ou supprimées selon les besoins pour atteindre approximativement cet objectif.

L'utilisation de l'utilisation du CPU pour déclencher une action de mise à l'échelle est l'un des modèles les plus populaires. Mais l'utilisation du CPU n'est pas la seule métrique que vous pouvez utiliser pour la mise à l'échelle. À certains égards, il peut en fait être sous-optimal d'utiliser l'utilisation du CPU, surtout si vous voulez une mise à l'échelle encore plus réactive.

Et si vous pouviez suivre une autre métrique qui anticipe l'augmentation de l'utilisation du CPU afin de ne pas avoir à attendre l'inévitable augmentation de l'utilisation du CPU de vos instances avant qu'une action de mise à l'échelle ne soit déclenchée ?

Avec GCP, par exemple, si vous avez un équilibreur de charge HTTP devant vos instances, vous pouvez configurer votre mise à l'échelle pour qu'elle soit déclenchée en fonction du nombre de requêtes atteignant votre équilibreur de charge. De même avec AWS, si vous avez une [file d'attente SQS](https://lightcloud.substack.com/i/70277437/messaging-queues) devant vos instances, vous pouvez mettre à l'échelle en fonction du nombre de messages dans la file d'attente.

Dans ces deux exemples, quelque chose d'autre anticipe une augmentation probable de l'utilisation future du CPU, donc la définition d'une action de mise à l'échelle pour qu'elle soit déclenchée en fonction de cela est un moyen de créer une mise à l'échelle plus réactive.

En revenant à notre analogie de restaurant, cela reviendrait à appeler plus de chefs dans la cuisine une fois que vous voyez une longue file d'attente à l'extérieur du restaurant. C'est une manière plus réactive de faire face à une augmentation soudaine de la demande par rapport à attendre que vos chefs soient submergés de commandes.

### Mise à l'échelle planifiée

La mise à l'échelle planifiée est idéale lorsque la demande fluctue fortement à des moments connus.

En utilisant à nouveau l'analogie du restaurant, votre politique de mise à l'échelle peut être basée sur un calendrier. Par exemple, si vous savez que les soirs et les week-ends sont plus chargés que les matins et les jours de semaine, votre politique de mise à l'échelle garantira qu'il y a plus de chefs pendant les périodes de demande attendue plus élevée.

Avec AWS et GCP, vous pouvez définir une politique de mise à l'échelle planifiée pour ajouter ou supprimer des instances à des heures spécifiques.

### Pourquoi utiliser l'auto-scaling ?

L'auto-scaling résout le problème ancien de la planification de la capacité. Essayer de prévoir avec précision la quantité de calcul nécessaire à l'avenir est semé d'erreurs. Trop peu de capacité, et votre site web est hors ligne pendant les périodes de forte demande, vous coûtant de l'argent et de la réputation. Trop de capacité, et vous payez pour des instances inutilisées.

La planification de la capacité est fondamentalement un problème de prévision. Et les humains ne sont pas très doués pour prévoir avec précision l'avenir. Avant l'existence de fournisseurs de cloud comme AWS, GCP et Azure, les entreprises devaient planifier la capacité en fonction de la demande future attendue. Ce processus de planification était souvent simplement du travail de devinette déguisé. Vous deviez payer à l'avance pour des serveurs et espérer ne pas avoir significativement sous-estimé ou surestimé le nombre de serveurs dont vous aviez besoin.

Le problème avec la prévision survient parce que nous avons une foi mal placée dans la mesure précise de l'avenir inconnaissable. Les humains font des prévisions inexactes depuis longtemps. Dès 600 av. J.-C., le philosophe grec Thalès était si occupé à compter les étoiles qu'il tombait constamment dans des nids-de-poule sur la route.

Certaines choses sont fondamentalement inconnaissables, et c'est très bien. L'auto-scaling élimine le besoin de prévoir avec précision la demande future puisque vous pouvez automatiquement augmenter ou diminuer le nombre d'instances que vous avez en fonction de votre politique de mise à l'échelle.

En utilisant l'auto-scaling, vous améliorez la résilience de votre architecture et réduisez les coûts. Ce sont les deux principales raisons d'utiliser l'auto-scaling dans vos conceptions.

#### Améliorer la résilience

Pouvoir augmenter automatiquement et immédiatement le nombre d'instances en réponse à une demande croissante réduit les risques que vos instances soient sous une charge excessive et à risque de mauvaise performance. Cela améliore la résilience de votre architecture.

L'auto-scaling n'est cependant pas seulement une question de mise à l'échelle. Il peut également être utilisé pour maintenir un nombre défini d'instances. C'est un excellent moyen de créer des architectures auto-réparatrices.

Avec AWS, vous pouvez définir le nombre minimum, maximum et souhaité d'instances de calcul, sans aucune politique de mise à l'échelle. AWS tentera simplement de maintenir le nombre souhaité d'instances spécifié par vous. Donc, si vous définissez le minimum, le maximum et le souhaité tous égaux à un, AWS maintiendra une instance pour vous. Si cette instance tombe en panne, une autre sera automatiquement créée pour remplacer l'instance défaillante afin de restaurer votre capacité souhaitée.

C'est un moyen peu coûteux et facile de garantir une [haute disponibilité](https://lightcloud.substack.com/i/59017006/high-availability) sans avoir plusieurs instances dans différentes zones de disponibilité.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F263f0886-2617-480a-af2b-232e97270a24_1559x914.png align="left")

*Auto-réparation en action, au sens figuré*

La capacité à créer des architectures auto-réparatrices est un argument vraiment solide pour presque toujours placer vos instances dans un groupe d'auto-scaling. AWS et GCP ne facturent pas, à l'heure actuelle, l'utilisation de l'auto-scaling. Vous ne payez que pour l'infrastructure sous-jacente créée pour supporter vos instances.

Ainsi, même s'il n'y a pas de besoin de pouvoir mettre à l'échelle les instances en fonction de la demande qui leur est soumise, avoir des instances dans un groupe d'auto-scaling est un moyen peu coûteux et facile de créer une architecture auto-réparatrice.

#### Réduire les coûts

Les exemples précédents concernaient l'augmentation du nombre d'instances pour répondre à une demande plus élevée. Mais il est tout aussi important de pouvoir réduire l'échelle pendant les périodes de demande plus faible.

L'auto-scaling vous permet de le faire en utilisant des politiques de mise à l'échelle planifiées ou dynamiques. C'est un excellent moyen de vous assurer que vous ne payez pas plus que nécessaire.

## Équilibrage de charge expliqué

Les équilibreurs de charge acceptent les connexions des clients et distribuent les requêtes sur les instances cibles. La distribution des requêtes est généralement effectuée sur la couche 7 (couche application) ou la couche 4 (couche transport). Ces couches sont un modèle théorique qui organise les réseaux informatiques en 7 couches et est [connu sous le nom de modèle OSI](https://www.freecodecamp.org/news/osi-model-networking-layers-explained-in-plain-english/).

Je ne vais pas entrer dans trop de détails sur le modèle OSI ici, mais pour l'instant, ce qui est important à savoir est que la plupart des équilibreurs de charge peuvent fonctionner sur la couche application ou la couche transport. Cela signifie qu'ils fonctionnent avec des protocoles de couche 7 comme HTTP(S) ou des protocoles de couche 4 comme TCP, UDP, SMTP, SSH.

L'exemple de cette section ne couvrira que les équilibreurs de charge d'application de couche 7 plus populaires qui fonctionnent avec HTTP/HTTPS.

Bien que les détails de mise en œuvre de bas niveau et les cas d'utilisation entre les équilibreurs de charge de couche 7 et de couche 4 soient différents, les principes restent les mêmes. Les équilibreurs de charge sont utilisés pour distribuer le trafic entrant sur un certain nombre d'instances cibles.

La distribution des requêtes parmi les instances cibles utilise généralement un algorithme de round robin où les requêtes sont envoyées à chaque instance séquentiellement. Ainsi, la requête #1 va à l'instance #1, la requête #2 à l'instance #2, la requête #3 à l'instance #3, la requête #4 revient à l'instance #1, et ainsi de suite.

Bien que d'autres algorithmes d'équilibrage existent, l'algorithme de round robin est le plus populaire utilisé par la plupart des fournisseurs de cloud pour l'équilibrage de charge.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4c5a66a2-31da-471e-a753-44b75dd78708_1898x1490.png align="left")

*Une vue simple de la manière dont les équilibreurs de charge distribuent les requêtes*

Le diagramme ci-dessus est une représentation logique du fonctionnement des équilibreurs de charge. Il ne montre qu'un seul équilibreur de charge, ce qui n'est pas une conception très résiliente. Cette abstraction logique est facile à illustrer, mais n'est pas précise.

En coulisses, plusieurs nœuds d'équilibreur de charge sont déployés dans chaque sous-réseau au sein d'une zone de disponibilité. L'équilibreur de charge est créé avec un seul enregistrement DNS qui pointe vers tous les nœuds d'équilibreur de charge élastique créés, c'est-à-dire que cet enregistrement DNS unique pointe vers toutes les adresses IP des nœuds réels déployés. Toutes les requêtes entrantes sont distribuées équitablement entre tous les nœuds de l'équilibreur de charge et les nœuds de l'équilibreur de charge distribuent à leur tour équitablement les requêtes aux instances cibles. De cette manière, vous n'avez pas de point de défaillance unique.

Une représentation plus réaliste, bien que plus complexe, du fonctionnement des équilibreurs de charge est montrée ci-dessous. Dans cet exemple, les requêtes arriveront à l'un des nœuds de l'équilibreur de charge déployés dans les trois sous-réseaux, puis elles seront distribuées équitablement entre les instances cibles.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F14072032-eb00-4b67-b253-1e293331b732_1938x1665.png align="left")

*Une vue plus précise de la manière dont les équilibreurs de charge distribuent les requêtes*

### Pourquoi utiliser l'équilibrage de charge ?

Les équilibreurs de charge garantissent que le trafic est distribué parmi les instances cibles. Cela répartit la charge et empêche une seule instance d'être surchargée par un nombre excessif de requêtes.

Les équilibreurs de charge créent également une architecture faiblement couplée. Le couplage lâche est généralement recherché car il signifie que les utilisateurs n'ont pas besoin d'être conscients des instances, ou que les instances n'ont pas besoin d'être conscientes des autres instances.

Que signifie exactement être "conscient" ? Puisque les requêtes des utilisateurs sont d'abord envoyées à l'équilibreur de charge, les utilisateurs ne sont pas conscients des instances répondant réellement à leur requête. Toute la communication est effectuée via l'équilibreur de charge, il devient donc facile de changer le type et le nombre d'instances sans que l'utilisateur en soit conscient. L'équilibreur de charge est conscient des instances dans sa cible afin qu'il puisse envoyer la requête à toutes les instances pertinentes.

## Mettre tout ensemble – Équilibrage de charge et auto-scaling en action

Le diagramme ci-dessous montre l'équilibrage de charge et l'auto-scaling utilisés pour une application web à trois niveaux composée de niveaux web, application et base de données. Chacun de ces niveaux dispose d'instances/infrastructures séparées.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F27dcd71d-6672-4f40-9dd4-1389a42869d7_1405x1923.png align="left")

*Équilibrage de charge et auto-scaling utilisés pour une application web à trois niveaux composée de niveaux web, application et base de données.*

Les instances des niveaux web et application sont dans des groupes d'auto-scaling séparés. Il y a également un équilibreur de charge entre l'utilisateur et le niveau web, et entre le niveau web et le niveau application.

En ayant un équilibreur de charge entre l'utilisateur et le niveau web, le niveau web peut être mis à l'échelle indépendamment, en utilisant la fonction d'auto-scaling pour ajouter ou supprimer des instances selon les besoins.

L'utilisateur n'a pas besoin de savoir à quelle instance se connecter car la connexion passe par un équilibreur de charge. C'est le couplage lâche en action. La même logique s'applique entre le niveau web et le niveau application. Sans l'équilibreur de charge, les instances des deux niveaux seraient fortement couplées, rendant la mise à l'échelle difficile.

Le niveau de base de données dans ce cas est une base de données RDS avec un nœud maître et deux nœuds de secours. Toutes les lectures et écritures vont au nœud maître et si ce nœud tombe en panne, il y a un basculement automatique vers l'une des instances de secours.

L'auto-scaling garantit :

1. **Résilience**, car il peut automatiquement et immédiatement augmenter le nombre d'instances en réponse à une demande croissante. Il peut également s'auto-réparer, donc même si vous n'anticipez pas le besoin de mise à l'échelle immédiate et automatique basée sur les changements de demande, l'auto-réparation est presque toujours souhaitée car elle augmente la disponibilité de votre architecture.
    
2. **Contrôle des coûts**, car il a la capacité de réduire l'échelle et de diminuer le nombre d'instances utilisées pendant les périodes de demande plus faible, ce qui peut vous faire économiser de l'argent.
    

L'équilibrage de charge garantit :

1. **Distribution de la charge**, car il empêche un seul nœud d'être surchargé par des requêtes.
    
2. **Couplage lâche**, car il élimine le besoin de conscience entre les utilisateurs et les instances, et entre les instances elles-mêmes. Cela permet aux instances de mettre à l'échelle indépendamment.
    

Merci d'avoir lu !