---
title: Quatre modèles d'architecture candidats pour les applications décentralisées
  basées sur la Blockchain
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-23T15:49:36.000Z'
originalURL: https://freecodecamp.org/news/https-medium-com-srinathperera-blockchain-patterns-6cf58fdc2d9b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*iCv3PnwJ3jvu2pDhEq3ZhQ.png
tags:
- name: Bitcoin
  slug: bitcoin
- name: Blockchain
  slug: blockchain
- name: Cryptocurrency
  slug: cryptocurrency
- name: software architecture
  slug: software-architecture
- name: 'tech '
  slug: tech
seo_title: Quatre modèles d'architecture candidats pour les applications décentralisées
  basées sur la Blockchain
seo_desc: 'By Srinath Perera

  Blockchain has a diverse set of use cases, ranging from finance to a decentralized
  Internet. However, most blockchain use cases can be implemented using relatively
  few patterns. For example, A Pattern Collection for Blockchain-based...'
---

Par Srinath Perera

La Blockchain a une diversité de cas d'utilisation, allant de la finance à un Internet décentralisé. Cependant, la plupart des cas d'utilisation de la blockchain peuvent être implémentés en utilisant relativement peu de modèles. Par exemple, [A Pattern Collection for Blockchain-based Applications](https://www.researchgate.net/publication/325439030_A_Pattern_Collection_for_Blockchain-based_Applications) fournit une liste de 15 modèles de Blockchain.

Les modèles à grain fin, tels que décrits ci-dessus, sont utiles. Cependant, la conception du système nécessite un niveau d'abstraction beaucoup plus élevé. Il est également utile d'avoir des macro-modèles plus grossiers, que nous appelons des modèles d'architecture. Cet article décrit quatre de ces modèles d'architecture.

Commençons. Pour décrire les modèles, j'utiliserai le modèle décrit par Aleksandra Tešanović dans [What is a Pattern](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.123.1162&rep=rep1&type=pdf).

### Modèle d'architecture pour l'IAM.

**Contexte :** Les environnements IAM incluent de nombreux utilisateurs et fournisseurs de services. Les systèmes IAM donnent à chaque utilisateur un compte et un ensemble de capacités permettant aux utilisateurs d'aller chez les fournisseurs de services, de démontrer leur propriété des comptes, puis de recevoir des services basés sur leurs capacités.

**Forces :** Besoin de mettre en œuvre un environnement IAM décentralisé où un seul utilisateur malveillant ou quelques utilisateurs ne peuvent pas affecter significativement le système.

**Solution :** Le modèle candidat proposé utilise la spécification DID du World Wide Web Consortium (W3C) et la spécification W3C Verifiable Claims de la manière suivante.

![Image](https://cdn-media-1.freecodecamp.org/images/lUMFQa8e5GZRqE9PVExbKKUBq43VTd0LCauy)
_Figure 1 : Modèle d'architecture IAM basé sur la Blockchain_

Supposons qu'Alice ait besoin d'une identité (DID, qui est un identifiant unique). Comme le montre la figure pour la création d'un nouveau DID, Alice crée une entrée dans la blockchain. Cette entrée inclut un identifiant généré aléatoirement, un lien vers le dépôt avec ses données de profil, et un hachage des données de profil. Le profil utilisateur contient une clé publique et un ensemble de revendications vérifiables. L'identifiant aléatoire généré devient maintenant le DID d'Alice car elle est la seule à posséder la clé privée correspondant à la clé publique.

Les revendications vérifiables sont des jetons de délégation signés par une autorité compétente. Le créateur les enregistre également dans une blockchain avec le hachage de la revendication de manière similaire au DID.

Alice obtient les revendications vérifiables en premier lieu en se rendant chez les autorités. Par exemple, le département d'enregistrement personnel ou équivalent est l'autorité compétente pour les revendications vérifiables de nom, d'adresse et de date de naissance. En supposant que les autorités émettent des revendications vérifiables, Alice démontre d'abord sa propriété du DID en utilisant un protocole de défi-réponse. Ensuite, elle soumet des demandes de revendications vérifiables pour ses attributs, qui peuvent, par exemple, inclure son nom, son adresse, son diplôme et sa date de naissance. Pour mettre à jour ses données de profil, Alice ajoutera une nouvelle entrée à la blockchain avec un nouveau hachage du profil.

Dans le protocole de défi-réponse, le validateur génère une graine aléatoire, la chiffrer en utilisant la clé publique d'Alice, puis défie Alice de démontrer qu'elle possède la clé privée en déchiffrant la graine chiffrée. Puisqu'Alice possède la clé privée, elle doit être la propriétaire du DID.

Un autre utilisateur ou une organisation (authentificateur), Bob, qui veut identifier Alice, reçoit d'abord le DID d'Alice, lit toutes les entrées liées à ce DID à partir de la blockchain, récupère les données de profil d'Alice et les vérifie. Bob peut vérifier l'identité d'Alice (identification) à nouveau en utilisant le protocole de défi-réponse. Ensuite, Bob peut confirmer les revendications vérifiables et être assuré que les revendications concernant Alice sont vraies.

Nous pouvons superposer la plupart des cas d'utilisation de l'IAM sur ce modèle d'architecture. Par exemple, nous pouvons réaliser le contrôle d'accès soit en émettant des revendications vérifiables pour les actions que nous voulons que les utilisateurs effectuent, soit en n'acceptant que les utilisateurs qui ont certaines propriétés (par exemple, âge, description de poste, appartenance à un groupe) dans leurs revendications vérifiables. Une implémentation peut choisir de mettre en cache des sous-ensembles pertinents des données de profil dans une base de données pour améliorer les performances.

### Modèle d'architecture pour l'historique ou l'espace de travail auditable

**Contexte :** Deux ou plusieurs parties effectuent des transactions ou des travaux ensemble, et leurs activités doivent être enregistrées de manière indéniable.

**Forces :** Besoin de mettre en œuvre un journal d'audit décentralisé ou un espace de travail où un seul utilisateur malveillant ou quelques utilisateurs ne peuvent pas affecter significativement le système.

**Solution :** Le système proposé enregistre les activités et crée des entrées dans la blockchain pour ces enregistrements. L'entrée contient le hachage des enregistrements d'activité, et donc, les enregistrements ne peuvent pas être contestés plus tard.

![Image](https://cdn-media-1.freecodecamp.org/images/iF-qjFAl8ERHYc8MkajFeVnIUK10RiWz2RVG)
_Figure 2 : Modèle d'architecture pour l'historique ou l'espace de travail auditable basé sur la Blockchain_

Par exemple, supposons qu'Alice veuille payer un impôt. Le serveur fiscal accepte la demande de paiement, crée un reçu numérique, enregistre son hachage dans la blockchain et envoie le reçu à Alice. Alice peut vérifier le reçu en calculant le hachage et en vérifiant par rapport à la valeur stockée dans la blockchain. Après cela, Bob ne peut pas nier le reçu car le hachage du reçu et l'heure sont enregistrés dans la blockchain.

Si les activités sont nombreuses, il peut être nécessaire de contourner les limitations de performance de la blockchain. Par conséquent, certaines implémentations peuvent enregistrer un hachage de plusieurs enregistrements d'activité sous forme de bloc au lieu d'un seul enregistrement d'activité.

### Modèle d'architecture pour le registre ou la place de marché

**Contexte :** Un registre est une collection d'entrées de données qui peuvent être recherchées et récupérées sur le réseau. Une place de marché est un registre qui permet aux utilisateurs d'acheter les services ou produits représentés par les entrées de données. Par exemple, un registre peut être un catalogue d'API disponibles.

**Forces :** Besoin de mettre en œuvre un environnement décentralisé où un seul utilisateur malveillant ou quelques utilisateurs ne peuvent pas affecter significativement le système.

**Solution :** Le modèle proposé fonctionne comme suit.

![Image](https://cdn-media-1.freecodecamp.org/images/PxrO0b03JFpQ-JuWXHXtzkfq56xJHND3gesV)
_Figure 3 : Modèle d'architecture de registre basé sur la Blockchain_

Considérons d'abord un registre. Avec l'architecture proposée, lorsqu'un utilisateur émet une mise à jour de registre (pour ajouter ou modifier une entrée), le client enregistre le changement dans la blockchain. Si les données de la mise à jour sont volumineuses, l'enregistrement de la blockchain peut contenir un lien vers les données et une valeur de hachage des données. Si les données stockées dans le registre doivent être modifiées, le client du registre ajoute un nouvel enregistrement à la blockchain avec les informations modifiées.

Dans le diagramme ci-dessus, chaque utilisateur a un client de registre en cours d'exécution sur la machine locale (par exemple, ordinateur portable ou téléphone). Chaque client de registre lit les enregistrements de mise à jour à partir de la blockchain, vérifie les données de mise à jour par rapport au hachage inclus dans les enregistrements et reconstitue la vue la plus récente des enregistrements à partir des mises à jour. Par exemple, en lisant les enregistrements de la blockchain sur les API, leurs ajouts, modifications et suppressions, le client de registre peut créer une vue qui montre les API actuelles incluses dans le registre. Pour éviter d'avoir à lire et vérifier tous les enregistrements à chaque fois que le registre est utilisé, les clients peuvent stocker les données dans une base de données et les indexer. Le client doit vérifier périodiquement la blockchain et mettre à jour le registre.

La blockchain fonctionne bien comme un "marché de services", puisque le même service peut être vendu plusieurs fois. Cependant, en raison des limitations de performance, les places de marché basées sur la blockchain ne sont pas adaptées aux articles qui ne peuvent être vendus qu'une seule fois.

Pour illustrer le fonctionnement d'un registre basé sur la blockchain, regardons lorsque Alice souhaite s'abonner au "service de nouvelles météo" sur la place de marché blockchain. Lorsqu'elle soumet sa demande, le registre crée des identifiants pour le service et les partage avec Alice. Le paiement peut se faire de plusieurs manières : en utilisant des Bitcoins, via un contrat intelligent où les paiements sont effectués en temps opportun, ou par certains moyens hors bande.

### Modèle d'architecture pour les contrats intelligents et les objets gérés

Dans ce modèle, nous considérons deux cas. Tout d'abord, nous considérons les contrats intelligents, et en second lieu, nous considérons un cas spécial commun des contrats intelligents : les "objets gérés".

#### Modèle de contrats intelligents

**Contexte :** Plusieurs utilisateurs souhaitent se conformer à un contrat, décrit comme un programme exécutable. Le contrat subit des transitions d'état selon les conditions définies dans le contrat, et à un moment donné, tout le monde peut convenir de l'état actuel du contrat.

**Forces :** besoin de mettre en œuvre un environnement où un seul utilisateur malveillant ou quelques utilisateurs ne peuvent pas affecter significativement le système.

**Solution :** Les contrats intelligents font partie des technologies de blockchain et sont pris en charge par les implémentations de blockchain, telles qu'Ethereum. Un contrat est décrit à l'aide d'un langage de contrat intelligent et distribué à tous les participants. À mesure que les conditions définies dans le contrat changent, chaque participant exécute le contrat et enregistre l'état actuel dans la blockchain à l'aide de l'algorithme de consensus.

#### Modèle d'objets gérés

**Contexte :** Nous devons suivre la propriété des objets intelligents du monde réel. Ici, les objets intelligents sont des objets du monde réel capables d'exécuter une logique informatique en leur sein. Le propriétaire est autorisé à contrôler et à effectuer des actions sur les objets du monde réel. De plus, le propriétaire peut transférer sa propriété à quelqu'un d'autre.

**Forces :** besoin de mettre en œuvre un environnement où un seul utilisateur malveillant ou quelques utilisateurs ne peuvent pas affecter significativement le système.

**Solution :** Ce qui suit décrit la mise en œuvre du modèle en utilisant la voiture comme exemple d'objet géré.

![Image](https://cdn-media-1.freecodecamp.org/images/8je7rRiQV0zVRuuvCXjnHJHMNlnNjOrv29r4)
_Figure 4 : Modèle d'architecture pour les objets gérés basé sur la Blockchain_

Nous pouvons implémenter une blockchain pour un objet géré, dans ce cas, une voiture, en deux étapes. Tout d'abord, le fabricant enregistre le DID et la clé publique du propriétaire de la voiture. Lorsque la propriété change, le propriétaire ajoute un nouvel enregistrement dans la blockchain spécifiant le nouveau propriétaire. Ensuite, lors de la vérification de la propriété, la voiture récupère d'abord tous les enregistrements dans la blockchain et vérifie que chaque enregistrement est ajouté par le propriétaire à ce moment-là. Cela est fait en vérifiant la clé publique de l'utilisateur qui a écrit l'enregistrement par rapport à la clé publique incluse dans l'enregistrement de propriété précédent. Le dernier propriétaire de cette chaîne valide est le propriétaire actuel.

Après avoir déterminé le propriétaire, la voiture se connecte au propriétaire actuel, Alice, en récupérant sa clé publique et en effectuant une connexion basée sur un protocole de défi-réponse avec le téléphone d'Alice, qui possède la clé privée d'Alice.

Un tel système réduit les risques associés aux artefacts contrôlés à distance. Par exemple, dans une implémentation non blockchain, quelqu'un ayant accès peut changer la propriété de votre voiture. Cependant, avec le modèle basé sur la blockchain, pour contrôler à distance la voiture, un éventuel attaquant doit changer l'enregistrement de propriété dans la blockchain, ce qui est très difficile à réaliser sans être le propriétaire.

Cependant, il est difficile d'empêcher quelqu'un qui a accès à l'"objet" de changer physiquement la logique en cours d'exécution (par exemple, en remplaçant le micrologiciel de la voiture). Une solution à ce problème est de construire une forme d'autodestruction qui se déclenche lorsque l'on détecte une manipulation de l'artefact.

Par exemple, Alice achète la voiture à Bob en utilisant un contrat intelligent qui paie Bob et met à jour la propriété du véhicule. Après la transaction, Alice se rend à la voiture, qui lit le DID d'Alice à partir du téléphone, récupère sa clé publique, l'authentifie en utilisant un protocole de défi-réponse en communiquant avec le téléphone qui possède la clé privée d'Alice, vérifie sa propriété et déverrouille la voiture.

### Conclusion

Nous avons discuté de quatre modèles d'architecture basés sur la blockchain. Le document GitHub, [Blockchain-based Integration Use Cases](https://github.com/wso2/ETAC/blob/master/blockchain/blockchain-usecases.md), montre ces modèles en action, décrivant comment plus de 30 cas d'utilisation de la blockchain peuvent être implémentés en utilisant ces quatre modèles.

Si vous avez des opinions sur les modèles ci-dessus ou si vous connaissez d'autres modèles, je serais vraiment ravi de les entendre.

J'espère que cela a été utile. Si vous aimez cela, vous pourriez également aimer une analyse détaillée de la blockchain dans notre article récemment publié, "[A use case centric survey of Blockchain: status quo and future directions](https://peerj.com/preprints/27529/)".