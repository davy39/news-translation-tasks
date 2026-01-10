---
title: 'AWS et l''élasticité : rester en avance sur la demande des utilisateurs'
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2019-07-11T10:32:00.000Z'
originalURL: https://freecodecamp.org/news/aws-and-elasticity-keeping-ahead-of-user-demand
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/DB.png
tags:
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
seo_title: 'AWS et l''élasticité : rester en avance sur la demande des utilisateurs'
seo_desc: 'I’ll assume that, one way or another, you’re already familiar with many
  of AWS’s core deployment services. That means you now know about:

  • EC2 instances and AMIs (Amazon Machine Images), and the “peripheral” tools that
  support their deployment like ...'
---

Je suppose que, d'une manière ou d'une autre, vous êtes déjà familier avec de nombreux services de déploiement principaux d'AWS. Cela signifie que vous connaissez maintenant :

• Les instances EC2 et les AMIs (Amazon Machine Images), ainsi que les outils "périphériques" qui soutiennent leur déploiement comme les groupes de sécurité et les volumes EBS

• L'incorporation de bases de données dans nos applications, à la fois sur instance et via le service géré RDS

• L'utilisation de buckets S3 pour livrer des fichiers média via nos applications EC2 et pour le stockage de sauvegarde du serveur

• Le contrôle de l'accès à nos ressources AWS avec IAM (Identity and Access Management)

• La gestion de ensembles de ressources croissants en appliquant intelligemment des tags, et

• L'accès à nos ressources en utilisant soit l'interface navigateur soit l'AWS CLI (Command Line Interface)

Tout cela peut être représenté par le schéma de la figure 1.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6dMDZX1tCuM2iQTkmkNwJw.png)
_Figure 1. Il s'agit du type d'infrastructure d'application que vous devriez être capable de construire en utilisant les services principaux d'AWS._

Maintenant, je vais changer un peu de focus et explorer quelques bonnes pratiques pour l'optimisation des applications. La figure 2 peut vous aider à visualiser comment toute cette infrastructure peut être rendue hautement disponible grâce à la magie de la segmentation réseau, de l'auto-scaling et de l'équilibrage de charge.

![Image](https://cdn-media-1.freecodecamp.org/images/1*DXQZ8lIjFXIcgL-f8DGRTA.png)
_Figure 2. Une illustration de la manière dont les services de données et de sécurité d'AWS fonctionnent ensemble pour permettre à une instance EC2 de livrer son application aux clients._

Bien que vous ne soyez probablement pas encore familier avec de nombreux outils et relations représentés dans le diagramme, vous devriez passer une minute à noter mentalement au moins quelques points clés, y compris :

• Le Virtual Private Cloud (VPC) qui englobe toutes les ressources AWS dans notre déploiement d'application

• Les deux types de zones de disponibilité : privées et publiques — utilisées pour gérer et, si nécessaire, isoler les ressources

• Les groupes de sécurité dont les règles contrôlent le mouvement des données entre les ressources

• L'AMI EC2 (Amazon Machine Image) qui sert de modèle pour répliquer des environnements de système d'exploitation précis

• Le bucket S3 (Simple Storage Service) qui peut stocker et livrer des données — à la fois pour la sauvegarde et la livraison aux utilisateurs

• Les volumes EBS qui agissent comme des volumes de données (comme des disques durs) pour une instance

• L'auto scaler qui permet l'approvisionnement automatique de plus (ou moins) d'instances pour répondre aux demandes changeantes d'une application, et

• L'équilibreur de charge qui achemine le trafic entre plusieurs serveurs pour garantir la meilleure expérience utilisateur possible

Je suis assez sûr que vous avez déjà compris cela : le "e" dans de nombreux noms de services AWS (EC2, ECS, EFS, EMR...) ne signifie pas "électronique" comme dans les noms de certaines technologies plus anciennes comme l'email, mais "élastique". Vous pouvez, néanmoins, être excusé de vous demander ce qu'il y a dans la vision AWS du cloud computing qui est si élastique.

Mais avant de répondre à cette question, il pourrait être utile de parler un peu du cloud computing en général. Comprendre ce qui rend le cloud unique est probablement essentiel pour tirer pleinement parti de tout ce qu'il a à offrir.

### Cloud Computing

Le National Institute of Standards and Technology (NIST) des États-Unis définit le cloud computing comme des services qui offrent à leurs utilisateurs ces cinq qualités :

• Auto-service à la demande : Les clients peuvent accéder aux ressources du cloud public chaque fois que nécessaire et sans avoir à les commander via un représentant humain.

• Accès réseau large : Les ressources du cloud sont accessibles depuis n'importe quel emplacement connecté au réseau (c'est-à-dire, Internet).

• Mise en commun des ressources : Les fournisseurs de cloud offrent un modèle multi-locataire, par lequel les clients individuels peuvent partager des ressources en toute sécurité les uns avec les autres, et une allocation dynamique des ressources, par laquelle les ressources peuvent être allouées et désallouées selon la demande des clients.

• Élasticité rapide : La disponibilité et la performance des ressources peuvent être automatiquement augmentées ou diminuées pour répondre à la demande changeante des clients.

• Service mesuré : Les clients peuvent consommer des services à différents niveaux sur une seule période de facturation et ne sont facturés que pour les ressources qu'ils utilisent réellement.

Ces cinq qualités décrivent un système profondément flexible et hautement automatisé dont les éléments peuvent être librement mélangés et assortis pour fournir le service le plus efficace et le plus rentable possible. Mais, une grande partie de ce qui rend cela possible est l'existence de systèmes intégrés qui peuvent s'ajuster dynamiquement en fonction de ce qui se passe autour d'eux. Ces ajustements sont des exemples de comportement élastique.

### Élasticité vs Scalabilité

Ainsi, l'élasticité, comme nous l'avons établi, est la capacité d'un système à surveiller la demande des utilisateurs et à augmenter et diminuer automatiquement les ressources déployées en conséquence. La scalabilité, en revanche, est la capacité d'un système à surveiller la demande des utilisateurs et à augmenter et diminuer automatiquement... attendez : n'ai-je pas dit cela à propos de l'élasticité ?

C'est un peu compliqué. En fait, les deux termes sont parfois utilisés de manière interchangeable. Cependant, je pense qu'il est utile de les distinguer. Maintenant, gardez à l'esprit que la manière dont j'explique la relation entre ces deux idées n'est en aucun cas le dernier mot sur le sujet — regardez un peu autour de vous et vous trouverez d'autres approches. Mais, je pense, dans le contexte de la compréhension du fonctionnement d'AWS, mon interprétation devrait être utile.

Ce qui rend un élastique élastique, c'est en partie sa capacité à s'étirer sous pression, mais aussi la manière dont il revient rapidement à sa taille originale lorsque la pression est relâchée. En termes AWS, cela signifierait la manière dont, par exemple, EC2 met des instances à votre disposition lorsque vous en avez besoin, mais vous permet de les abandonner lorsqu'elles ne sont pas utilisées ; ne vous facturant que pour le temps d'utilisation. Voir figure 3.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HldsGHvKzHoyiJwqiDbl1A.png)
_Figure 3. L'élasticité permet aux systèmes d'ajouter ou de supprimer dynamiquement des ressources pour répondre à la demande changeante._

La scalabilité décrit la manière dont un système est conçu pour répondre à la demande changeante. Cela peut inclure le fait que vous avez un accès 24 heures sur 24 à toutes les ressources dont vous pourriez avoir besoin (ce qui, bien sûr, est une caractéristique élastique), mais cela signifie également que la conception sous-jacente elle-même supporte des changements rapides et imprévisibles.

Par exemple, un logiciel qui est scalable peut être facilement pris et déposé sur un nouveau serveur — éventuellement dans un nouvel environnement réseau — et simplement fonctionner sans aucune configuration manuelle. De même, comme illustré dans la figure 4, la composition d'une infrastructure scalable peut être rapidement modifiée de manière à ce que tous les anciens éléments sachent immédiatement comment travailler ensemble avec les nouveaux.

![Image](https://cdn-media-1.freecodecamp.org/images/1*H2rBMFyp1oMI4RZYHrYjPw.png)
_Figure 4. Un logiciel scalable peut être facilement copié pour une utilisation sur plusieurs serveurs déployés dans plusieurs environnements réseau._

Avec cela à l'esprit, nous pouvons dire que l'EC2 d'Amazon n'est pas seulement élastique mais, puisque ses éléments (instances, volumes de stockage, groupes de sécurité, etc.) peuvent être facilement intégrés et retirés des infrastructures en cours d'exécution, il est également très scalable. Ah, mais quel type de scalable ? Il y en a deux, vous savez :

• Le scaling horizontal est le "scaling out" — où vous ajoutez plus de nœuds de serveur légers (ou "instances") pour répondre à la demande croissante.

• Le scaling vertical est le "scaling up" — où vous déplacez votre application d'un serveur léger unique vers un serveur avec une capacité de calcul plus grande.

Il est certainement possible de transférer des applications basées sur AWS de serveurs légers à des serveurs plus lourds, et pour certaines charges — comme de nombreuses bases de données de transactions à haute charge, c'est préféré. Mais dans un contexte AWS, si vous entendez une conjugaison du mot "scale", les chances sont qu'il s'agit de scaling horizontal.

### Applications pratiques

D'accord. Mais qui s'en soucie ? Eh bien, à mesure que la demande des clients sur notre site WordPress continue de croître, nous le ferons, et de manière significative. Vous voyez, pour une raison quelconque — peut-être liée au fait que nous réduisons le prix de notre produit de 75 % pendant seulement une demi-heure chaque soir — les clients arrivent en plus grand nombre en début de soirée, heure locale. Ainsi, tandis que le serveur unique que nous avons été en train d'exécuter reste largement inutilisé pendant la majeure partie de la journée, il fond simplement sous la pression de milliers de visites concentrées sur une si courte période de temps.

Et puis il y a cette question que l'un des gars du bureau a posée l'autre jour : "Notre entreprise entière fonctionne sur un seul serveur web ; que se passe-t-il s'il tombe en panne ?" En effet.

Nous pourrions provisionner quatre ou cinq serveurs supplémentaires et les faire fonctionner à plein temps. De cette façon, nous serions couverts pour les périodes de fort trafic et pour la défaillance de n'importe quel serveur. Mais cela impliquerait encore un gaspillage colossal, puisque pendant la majeure partie de chaque journée, nous paierions pour que la plupart des instances restent inactives. Cela ne serait pas non plus nécessairement d'une grande aide en cas de défaillance du réseau, ce qui couperait probablement la connectivité à tous les serveurs en même temps.

Nous pourrions toujours traiter au moins le problème de la demande des clients en arrangeant pour que quelqu'un soit au bureau chaque soir pour démarrer manuellement autant de serveurs supplémentaires que nous aurons besoin. Mais nous avons demandé autour de nous, et personne ne s'est porté volontaire. Et de plus, la meilleure façon de s'assurer qu'un travail quotidien ne sera pas fait est de supposer qu'un administrateur se souviendra de le faire.

### Automatisation de la haute disponibilité

Alternativement, nous pourrions passer un peu de temps à incorporer une capacité de haute disponibilité dans notre configuration et laisser le tout être géré discrètement et efficacement par un logiciel. Ce sera le sujet des prochains chapitres de mon livre, où nous apprendrons à tirer parti des zones de disponibilité géographiquement distantes d'AWS pour rendre la défaillance totale de l'application beaucoup moins probable, utiliser l'équilibrage de charge pour coordonner entre les serveurs parallèles et surveiller leur santé, et l'auto-scaling pour laisser AWS répondre automatiquement aux pics et aux creux de la demande changeante en lançant et en arrêtant des instances selon les besoins.

Pour plus d'informations sur Amazon Web Services, téléchargez le premier chapitre gratuit de [Learn Amazon Web Service in a Month of Lunches](https://www.manning.com/books/learn-amazon-web-services-in-a-month-of-lunches) et consultez cette [présentation Slideshare](http://www.slideshare.net/ManningBooks/learn-amazon-web-services-in-a-month-of-lunches). N'oubliez pas d'utiliser le code **ssclinton** pour économiser 42 % sur votre achat.