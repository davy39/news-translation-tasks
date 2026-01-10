---
title: Comprendre l'architecture VPC – Comment sécuriser les instances AWS EC2
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-05-02T13:33:22.000Z'
originalURL: https://freecodecamp.org/news/understanding-vpc-architecture-securing-aws-ec2-instances
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/pexels-sevenstorm-juhaszimrus-425160.jpg
tags:
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
- name: computer networking
  slug: computer-networking
seo_title: Comprendre l'architecture VPC – Comment sécuriser les instances AWS EC2
seo_desc: "AWS Virtual Private Clouds (VPCs) are the organizing structure of most\
  \ AWS network operations. Without a clear understanding of how they work, it'll\
  \ be hard to get security and efficiency quite right. \nBut before talking about\
  \ VPCs directly, I'm goin..."
---

Les VPC (Virtual Private Clouds) d'AWS sont la structure organisatrice de la plupart des opérations réseau AWS. Sans une compréhension claire de leur fonctionnement, il sera difficile d'obtenir une sécurité et une efficacité optimales. 

Mais avant de parler directement des VPC, je vais prendre une minute ou deux pour rafraîchir vos mémoires sur les bases de l'architecture de réseau TCP/IP et de l'adressage NAT. 

Mais n'hésitez pas à sauter la partie suivante si vous maîtrisez déjà tout cela. Une fois cela derrière nous, je vous montrerai à quoi ressemble la construction de VPC dans AWS. 

## Un rapide rappel sur TCP/IP

D'accord. Donc, TCP signifie Transmission Control Protocol et IP signifie Internet Protocol. Si cela semble un peu large – presque comme s'ils essayaient de décrire la totalité de l'internet – c'est parce que presque tout ce que nous faisons sur l'internet est effectivement contrôlé par ces protocoles TCP/IP vieilles de plus d'un demi-siècle.

Cet article provient de mon [cours sur la sécurisation de vos instances AWS EC2](https://www.udemy.com/course/securing-amazon-ec2-instances/?referralCode=E3ACB9DC5E3B77853E63). Si vous le souhaitez, vous pouvez suivre la version vidéo ici :

%[https://www.youtube.com/watch?v=iCal_Tzvg9g&list=PLSiZCpRYoTZ5dys7oy4ReI-ltW0jnGTMO&]

Pour nos besoins, rappelez-vous que chaque appareil connecté au réseau doit avoir une adresse IP unique. Étant donné que, mathématiquement, il ne peut y avoir que quatre milliards d'adresses IPv4 32 bits, et qu'il y a déjà bien plus de quatre milliards d'appareils connectés au réseau sur l'internet, quelque chose devait changer. 

```
Une adresse IPv4 typique :
192.168.2.45
```

Le protocole IPv6 128 bits a finalement été introduit pour permettre des _milliards_ d'adresses uniques. Nous n'en manquerons jamais. 

```
Une adresse IPv6 typique :
fd42:e265:3791:64f9:216:3eff:fe54:fcfe/64
```

Mais avant IPv6, une autre solution brillante a été introduite : le réseau NAT. 

## Qu'est-ce que la traduction d'adresses réseau (NAT) ?

Le protocole NAT réserve trois segments de réseau pour une utilisation dans les réseaux _privés_ uniquement. En utilisant NAT, votre domicile peut avoir 15 ou 20 appareils – y compris des ordinateurs portables, des smartphones sur WiFi, des imprimantes réseau, des routeurs, et peut-être un réfrigérateur intelligent ou deux – mais entre eux, ils n'utiliseront qu'une seule adresse IP publique. 

Comment cela fonctionne-t-il ? Eh bien, votre fournisseur de services internet attribuera cette adresse IP publique unique au modem qu'ils vous envoient. Mais ce modem agira comme un serveur DHCP et attribuera à chaque appareil _local_ une adresse IP _privée_ provenant de l'un de ces trois segments de réseau. 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/slide-31.png)
_Une architecture NAT typique_

Le serveur DHCP _traduira_ toutes les requêtes circulant entre vos appareils locaux et les services basés sur internet de manière à ce que ces services internet pensent que l'IP de votre appareil est en réalité l'adresse publique unique. 

Mais les paquets réseau entrants sont en réalité livrés directement à votre appareil en utilisant son adresse NAT locale. Le système est vraiment brillant. Et il a ajouté des décennies de vie au système IPv4.

Mais une fois que nous avons NAT en place, il peut en fait faire beaucoup plus que simplement traduire l'adressage local. Ce qui nous amène à la raison pour laquelle nous parlons de tout cela dans le contexte de la sécurité des instances EC2 en premier lieu. 

Vous voyez, NAT permet une segmentation réseau très sophistiquée. En configurant soigneusement les règles d'adressage et de routage, vous pouvez transformer un réseau local unique en un environnement multicouche et hautement sécurisé pour les déploiements critiques de l'entreprise. 

Voici une illustration d'un environnement répliqué utilisant des sous-réseaux publics et privés provenant de la documentation AWS.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/bastion_aws.png)
_Comment les hôtes bastion peuvent s'intégrer dans un VPC AWS_

La seule connexion avec le monde extérieur, un tel sous-réseau privé, aurait des flux traversant un hôte bastion et une passerelle NAT vivant dans un sous-réseau public adjacent. Forcer tout à passer par ces deux appareils vous permet de contrôler précisément le trafic. 

L'hôte bastion fournit une boîte de saut permettant aux administrateurs d'ouvrir en toute sécurité des sessions SSH à distance sur les instances s'exécutant dans vos sous-réseaux privés. Et la passerelle NAT permet aux services s'exécutant sur vos instances privées un accès sortant à, par exemple, tirer des mises à jour logicielles. Les hôtes bastion et les passerelles NAT entraîneront des coûts d'utilisation réguliers, d'ailleurs.

## Comment optimiser les réseaux VPC

Maintenant, je vais vous montrer comment tout cela fonctionne dans l'écosystème AWS. À partir du tableau de bord VPC, je peux cliquer sur Créer VPC. Tout de suite, j'ai une décision à prendre : est-ce que je veux construire un simple VPC où je peux héberger quelques ressources, ou quelque chose de plus compliqué ?

Si je choisis VPC uniquement, je devrai simplement donner un nom au VPC, sélectionner mes environnements d'adressage et je suis prêt à partir. 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/ec2_security8-f007434.png)
_Partie de l'interface de configuration VPC dans AWS_

Mais nous sommes ici pour tester l'option _VPC et plus_. Comme vous pouvez le voir, cela ouvrira un aperçu de l'infrastructure à droite qui nous montre exactement ce qui sera créé en fonction des sélections actuelles, et à quoi cela ressemblera. 

Actuellement, comme vous pouvez le voir, nous obtiendrons un sous-réseau public et un sous-réseau privé dans chacune des deux zones de disponibilité, et des tables de routage et des connexions réseau appropriées pour faire fonctionner tout cela. 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/ec2_security8-f007926.png)
_Remarquez comment AWS attribue automatiquement des noms logiques aux nouveaux sous-réseaux_

Remarquez comment chaque objet est automatiquement nommé de manière à refléter correctement la structure de nommage que j'ai spécifiée. Tout cela est automatiquement conforme aux meilleures pratiques de sécurité et de disponibilité.

Je peux choisir de spécifier une location dédiée pour les nouvelles instances lancées dans ce VPC – bien que, comme je l'ai mentionné précédemment, cela ne sera probablement pas pertinent pour tous les cas.

Le nombre de zones de disponibilité que vous configurez reflétera la profondeur de tolérance aux pannes dont votre application a besoin. Plus il y a de zones, moins votre application a de chances de tomber en panne. 

Bien sûr, de la même manière, plus il y a de zones, plus vous aurez besoin de faire fonctionner d'instances et plus vous dépenserez. Vous pouvez voir que la modification de cette valeur aura un impact sur les paramètres de sous-réseau à droite.

Vous pouvez également contrôler le nombre de sous-réseaux publics et privés. Les options disponibles refléteront le nombre de zones de disponibilité que vous avez sélectionnées ci-dessus. En gros, l'interface utilisateur rend presque impossible de faire quelque chose de stupide – ce que j'apprécie.

L'ajustement des sous-réseaux dans l'interface utilisateur mettra automatiquement à jour la configuration à droite. La sélection d'une passerelle NAT générera un nouvel objet avec toutes les connectivités appropriées intégrées. 

Un dernier outil vraiment pratique est les champs qui nous permettent d'affiner l'allocation d'adresses pour nos sous-réseaux. Cela pourrait être important si vous prévoyez de déployer, par exemple, un grand nombre de conteneurs virtuels dans quelques sous-réseaux publics mais rien de plus qu'une poignée de serveurs de base de données dans vos sous-réseaux privés. Vous aurez probablement besoin de beaucoup plus d'adresses dans les premiers et de moins dans les seconds.

Une fois que vous avez démarré votre VPC, il ne faudra que quelques secondes pour que toutes les parties se mettent en place. Une fois cela fait, vous pourrez naviguer vers le tableau de bord Vos VPC pour confirmer ce qui est maintenant disponible. 

## Conclusion

Nous avons couvert beaucoup de terrain dans cet article. Vous avez appris comment les VPC peuvent être conçus pour employer des topologies de routage sophistiquées qui exposent et bloquent les ressources pour répondre efficacement à vos besoins opérationnels et de sécurité.

Merci d'avoir lu !