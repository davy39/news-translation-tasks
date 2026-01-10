---
title: Comment gérer le chiffrement à grande échelle avec le chiffrement par enveloppe
  et les systèmes de gestion des clés
subtitle: ''
author: Rohit Jacob Mathew
co_authors: []
series: null
date: '2021-10-27T22:52:59.000Z'
originalURL: https://freecodecamp.org/news/envelope-encryption
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/1400-x-600.jpg
tags:
- name: Application Security
  slug: application-security
- name: encryption
  slug: encryption
seo_title: Comment gérer le chiffrement à grande échelle avec le chiffrement par enveloppe
  et les systèmes de gestion des clés
seo_desc: "Recently at work, I came across an interesting method to handle encryption\
  \ at scale called envelope encryption. \nFirst of all, it increases security and\
  \ helps you ease out the management of encryption keys. But it's also a highly recommended\
  \ pattern ..."
---

Récemment au travail, je suis tombé sur une méthode intéressante pour gérer le chiffrement à grande échelle appelée chiffrement par enveloppe. 

Tout d'abord, cela augmente la sécurité et vous aide à faciliter la gestion des clés de chiffrement. Mais c'est aussi un modèle fortement recommandé par PCI-DSS (Norme de sécurité pour le traitement des cartes de crédit) et entraîne une meilleure confidentialité des données et une meilleure protection des informations personnellement identifiables (PII). 

Lorsque nous pensons aux données, il y a 3 endroits où nous pouvons penser à les chiffrer :

* Au repos – sur des dispositifs de stockage matériels comme un disque ou dans vos appareils
* En transit – lors du déplacement de données entre différents emplacements comme serveur à serveur via des appels API
* En utilisation – pendant qu'elles sont utilisées par un serveur (c'est un nouveau concept et il est encore en cours de recherche)

Nous allons principalement traiter du chiffrement au repos, et le chiffrement par enveloppe est un modèle populaire pour ce cas d'utilisation.

## Qu'est-ce que le chiffrement par enveloppe ? 💡

Le chiffrement par enveloppe implique de chiffrer vos données avec une clé de chiffrement des données, puis de chiffrer la clé de chiffrement des données (DEK) avec une clé maître client (CMK). 

Vous stockez ensuite à la fois les données chiffrées et la DEK chiffrée côte à côte dans la base de données. Cette pratique d'utilisation d'une clé d'enveloppement pour chiffrer les clés de données est connue sous le nom de chiffrement par enveloppe.

Vous devez comprendre ces deux clés avant de voir comment le processus de chiffrement se déroule :

1. Clé maître client (CMK)
2. Clé de chiffrement des données (DEK)

### Clés maîtresses client/Clés racines/Clés de chiffrement des clés (CMK)

Ce sont des clés symétriques utilisées pour chiffrer, déchiffrer et rechiffrer des données. Elles peuvent également générer des clés de chiffrement des données que vous pouvez utiliser en dehors du système KMS. Elles suivent les règles suivantes :

* L'accès à ces clés doit être restreint aux points de terminaison les moins nombreux
* L'accès à ces clés doit être sécurisé par ACL
* Ces clés doivent être stockées dans un endroit sécurisé comme un KMS ou un module de sécurité matériel (pour se conformer à [FIPS 140-2](https://en.wikipedia.org/wiki/FIPS_140-2))

Dans des systèmes comme Google Cloud Key Management Service, vous avez une hiérarchie de clés comme illustré ci-dessous (vous pouvez trouver plus d'informations [ici](https://cloud.google.com/security/encryption/default-encryption#encryption_key_hierarchy_and_root_of_trust)) :

![Hiérarchie des clés de chiffrement chez Google](https://cdn.hashnode.com/res/hashnode/image/upload/v1635198625726/DgTfDZpGk.png)

### Clés de chiffrement des données (DEK)

Les clés de données sont des clés de chiffrement que vous pouvez utiliser pour chiffrer des données, y compris de grandes quantités de données et d'autres clés de chiffrement des données. 

Contrairement aux CMK, qui ne peuvent pas être téléchargées, les clés de données vous sont retournées pour une utilisation en dehors du KMS. Certaines des meilleures pratiques pour les DEK sont les suivantes :

* Vous devez générer les DEK localement
* Lorsque vous les stockez, assurez-vous toujours que les DEK sont chiffrées au repos
* Pour un accès facile, stockez la DEK près des données qu'elle chiffre
* Générez une nouvelle DEK chaque fois que vous écrivez les données. Cela signifie que vous n'avez pas besoin de faire tourner les DEK.
* N'utilisez pas la même DEK pour chiffrer les données de deux utilisateurs différents
* Utilisez un algorithme robuste tel que l'AES 256 bits

## Processus de chiffrement par enveloppe

Tout d'abord, une requête API est envoyée au KMS pour générer une clé de données en utilisant la CMK.

Ensuite, le KMS retourne une réponse avec la clé de données en clair et la clé de données chiffrée (en utilisant la CMK).

![Générer des clés de données](https://cdn.hashnode.com/res/hashnode/image/upload/v1635198711784/Bm05yko4g.png)

Les données sont chiffrées en utilisant la clé de données en clair, puis la clé de données en clair est supprimée de la mémoire.

![Processus de chiffrement](https://cdn.hashnode.com/res/hashnode/image/upload/v1635198735343/vjqUrCTa1.png)

Les données chiffrées et la clé de données chiffrée sont regroupées dans une enveloppe et stockées.

![Processus de chiffrement avec données stockées au repos](https://cdn.hashnode.com/res/hashnode/image/upload/v1635198756845/mXf8rwGhU.png)

## Processus de déchiffrement

Tout d'abord, la clé de données chiffrée est extraite de l'enveloppe.

Ensuite, une requête API est envoyée au KMS en utilisant la clé de données chiffrée qui contient des informations sur la CMK à utiliser dans le KMS pour le déchiffrement.

Le KMS retourne une réponse avec la clé de données en clair.

![Obtention de la clé de données en clair](https://cdn.hashnode.com/res/hashnode/image/upload/v1635198816460/dl8Q5RoPKew.png)

Ensuite, les données chiffrées sont déchiffrées en utilisant la clé de données en clair, et la clé de données en clair est supprimée de la mémoire.

## **En quoi le chiffrement par enveloppe est-il différent des autres modèles de chiffrement** ? 💡

Chaque service que vous construisez nécessite un chiffrement à un moment donné. Cela pourrait être des mots de passe ou des PII dans une base de données, des identifiants pour un service externe, ou même des fichiers dans un système de fichiers.

### Fichiers de configuration

Vous pouvez facilement gérer certaines de ces situations avec un fichier de configuration, mais ils posent leurs propres risques de sécurité comme :

* Une planification appropriée est nécessaire pour garder les données sécurisées
* Plusieurs formats sont présents, comme YAML, JSON et XML pour n'en nommer que quelques-uns
* Les emplacements de stockage exacts peuvent être codés en dur dans l'application, rendant le déploiement potentiellement problématique
* L'analyse des fichiers de configuration peut être problématique.

### Chiffrement symétrique

Vous pouvez chiffrer des données en utilisant une clé symétrique, mais elles souffrent d'un problème majeur qui est la gestion des clés.

Vous devez trouver un moyen d'obtenir la clé pour la partie avec laquelle vous partagez des données. Mais si quelqu'un met la main sur une clé symétrique, il peut déchiffrer tout ce qui est chiffré avec cette clé.

### Chiffrement asymétrique

Vous pouvez chiffrer des données en utilisant le chiffrement asymétrique, qui est considéré comme une norme de nos jours. Cependant, certains de ses inconvénients sont :

* C'est un processus lent, ce qui le rend inadapté au déchiffrement de messages en masse
* Lorsque vous perdez votre clé privée, vos messages reçus ne seront pas déchiffrés
* Si votre clé privée est identifiée par un attaquant, il peut lire tous vos messages

### Chiffrement par enveloppe

Certains des avantages offerts par le chiffrement par enveloppe sont :

* **Une combinaison des avantages du chiffrement symétrique et asymétrique** – Les données sont chiffrées en utilisant une DEK qui suit le chiffrement symétrique. La DEK est chiffrée par une CMK qui suit le chiffrement asymétrique. En utilisant le chiffrement asymétrique, les DEK chiffrées peuvent être partagées et déchiffrées uniquement par ceux qui ont accès à la CMK, atténuant le problème d'échange de clés des algorithmes symétriques.
* **Gestion des clés plus facile** – Plusieurs DEK peuvent être chiffrées sous une seule clé racine et faciliter la gestion des clés dans un KMS. Vous pouvez également effectuer une maintenance des clés plus sécurisée en faisant tourner vos clés racines, au lieu de faire tourner et de rechiffrer toutes vos DEK.
* **Protection des clés de données** – Parce que nous chiffrons la clé de données avec la CMK, nous n'avons pas à nous soucier de stocker la clé de données chiffrée. Ainsi, nous pouvons stocker en toute sécurité la clé de données chiffrée à côté des données chiffrées.

## Pourquoi les systèmes de gestion des clés fonctionnent bien à grande échelle

Le chiffrement par enveloppe et les KMS fonctionnent si bien à grande échelle grâce aux **performances**. Comme nous l'avons mentionné précédemment, les chiffrements asymétriques sont généralement lents et les chiffrements symétriques sont très rapides, mais la gestion des clés peut être un problème. 

Ainsi, dans le chiffrement par enveloppe, pour une grande quantité de données, vous les chiffrez rapidement en utilisant un chiffrement symétrique avec une clé aléatoire. Ensuite, seule la clé est chiffrée en utilisant un chiffrement asymétrique. Cela offre les avantages du chiffrement asymétrique, avec les performances du chiffrement symétrique.

![KMS utilisé à grande échelle dans Google](https://cdn.hashnode.com/res/hashnode/image/upload/v1635198563732/1E9VcEqZ-.png)

Les systèmes de gestion des clés comme AWS KMS, Azure Key Vault et Google Cloud Key Management Service vous offrent un service entièrement géré pour stocker et gérer les clés de chiffrement. Ceux-ci utilisent le chiffrement par enveloppe en interne, et ils sont utilisés par défaut dans de nombreux services qui supportent le chiffrement chez les fournisseurs d'infrastructure cloud comme AWS, GCP, Azure et autres.

Un système de gestion des clés idéal doit être hautement disponible, il doit contrôler l'accès à la ou aux clés maîtresses, il doit auditer l'utilisation des clés, et enfin, il doit gérer le cycle de vie des clés.

Ainsi, en ayant les caractéristiques ci-dessus et en utilisant le chiffrement par enveloppe en interne, les systèmes de gestion des clés sont idéaux pour gérer le chiffrement à grande échelle.

## Résumé

Le chiffrement par enveloppe est l'un des modèles de conception de sécurité des applications les plus fiables utilisés à grande échelle. C'est la méthode de chiffrement par défaut utilisée dans des services comme AWS S3, GCP et autres. 

Espérons que cela vous aide à comprendre comment vous pouvez chiffrer/déchiffrer une grande quantité de données en utilisant la méthode de chiffrement par enveloppe à grande échelle dans une configuration plus fiable.

Merci d'avoir lu ! J'espère vraiment que vous trouverez cet article utile. Je suis toujours intéressé à connaître vos pensées et je suis heureux de répondre à toutes les questions que vous pourriez avoir. Si vous pensez que cet article était utile, veuillez le partager afin que d'autres puissent le lire également.

P.S. – N'hésitez pas à me contacter sur [LinkedIn](https://www.linkedin.com/in/rohitjmathew) ou [Twitter](https://twitter.com/iamrohitjmathew).

## Ressources

Cet article s'appuie fortement sur les matériaux suivants :

* [Google Cloud Data Encryption - Jayendra's Cloud Certification Blog -](https://jayendrapatil.com/tag/envelope-encryption/)
* [AWS KMS concepts - AWS](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html)
* [AWS KMS and Envelope Encryption - Manish Pandit](https://lobster1234.github.io/2017/09/29/aws-kms-envelope-encryption/)
* [Cloud Architecture Pattern: Envelope Encryption (or Digital Envelope) with Public Cloud Providers Part 1 - Nilay Parikh](https://blog.nilayparikh.com/security/application/cloud-architecture-patterns-envelope-encryption-or-digital-envelope-with-public-cloud-providers-part-1/)
* [AWS KMS Envelope Encryption - Chirag Modi](https://dev.to/chiragdm/aws-kms-envelope-encryption-3689)
* [Protecting data with envelope encryption - IBM](https://cloud.ibm.com/docs/key-protect?topic=key-protect-envelope-encryption)
* [Envelope encryption - GCP](https://cloud.google.com/kms/docs/envelope-encryption)
* [Encryption at rest in Google Cloud - GCP](https://cloud.google.com/security/encryption/default-encryption)

%[https://youtu.be/StJ1NOQjAjo]