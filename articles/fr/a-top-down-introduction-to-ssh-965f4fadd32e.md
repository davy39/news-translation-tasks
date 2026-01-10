---
title: Une introduction descendante à SSH et comment il permet le partage sécurisé
  de données
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-06T12:18:02.000Z'
originalURL: https://freecodecamp.org/news/a-top-down-introduction-to-ssh-965f4fadd32e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*TiltvM4ydji8sXcvbsEL_Q.jpeg
tags:
- name: encryption
  slug: encryption
- name: Security
  slug: security
- name: software development
  slug: software-development
- name: ssh
  slug: ssh
- name: Web Development
  slug: web-development
seo_title: Une introduction descendante à SSH et comment il permet le partage sécurisé
  de données
seo_desc: 'By Sam Ollason

  This article will take a high-level and top-down approach to explain how SSH works
  and how it is used for securely communicating with remote computers.

  We will look at how an SSH session is actually ‘secure’ and how computers establish...'
---

Par Sam Ollason

**Cet article adoptera une approche de haut niveau et descendante pour expliquer comment SSH fonctionne et comment il est utilisé pour communiquer de manière sécurisée avec des ordinateurs distants.**

Nous examinerons comment une session SSH est réellement "sécurisée" et comment les ordinateurs établissent et configurent une session SSH en premier lieu. Nous examinerons également les avantages de l'utilisation de SSH.

_Note :_ Cela est destiné à des notes futures pour moi-même, mais j'espère que vous en apprendrez quelque chose aussi !

![Image](https://cdn-media-1.freecodecamp.org/images/F0xSx0bm1cKylEjl0uyrNv0IUDmaXv2DE3mb)
_Photo par [Unsplash](https://unsplash.com/photos/pY_AZJfdbHQ?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Matt Artz</a> sur <a href="https://unsplash.com/search/photos/key?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### Qu'est-ce que SSH ?

SSH est l'abréviation de "secure shell". C'est un protocole pour partager des données entre deux ordinateurs via Internet.

Un protocole est essentiellement un ensemble de règles qui définissent le langage que les ordinateurs peuvent utiliser pour communiquer.

Typiquement, les deux ordinateurs impliqués sont votre ordinateur (le "client") et un serveur distant (l'"hôte").

### Pourquoi s'en soucier ?

#### Communications sécurisées entre ordinateurs

Chaque fois que deux ordinateurs communiquent via Internet, nous voulons être sûrs que nos messages ne peuvent pas être interceptés et compris par quiconque écoute les messages.

Imaginez envoyer vos coordonnées bancaires via Internet pour acheter quelque chose en ligne. Si vos messages n'étaient pas chiffrés, alors tout ordinateur qui écoute ou tout ordinateur qui reçoit les messages pour les transmettre pourrait être en mesure de voir votre numéro de compte et votre mot de passe. Ce n'est pas bon !

Je crois que c'est un concept important à comprendre pour quiconque aspire à travailler avec les technologies web.

#### Accès sécurisé aux ordinateurs distants

Utiliser SSH pour vérifier l'authentification est une méthode d'authentification plus sécurisée que l'utilisation d'un mot de passe. Nous explorerons comment cela fonctionne ci-dessous.

### Comment SSH est-il sécurisé ?

SSH est une méthode sécurisée d'envoi de communications entre deux ordinateurs.

Par "sécurisé", je veux dire une méthode de codage des messages sur un ordinateur client de sorte que le seul autre ordinateur qui peut décoder les messages et les comprendre est l'hôte. Ce codage/décodage est appelé **chiffrement**, donc ce que nous voulons vraiment dire ici, c'est que SSH est sécurisé parce qu'il utilise un **canal de communication chiffré**.

### Comment une session SSH est-elle établie ?

Plusieurs processus doivent avoir lieu entre deux ordinateurs pour qu'une session SSH commence.

1. Tout d'abord, nous avons besoin d'une méthode pour établir un moyen sécurisé d'échanger des messages entre les ordinateurs. Nous devons établir un **canal chiffré**.
2. Nous avons besoin d'un moyen de vérifier que les données reçues par l'hôte n'ont pas été altérées. Cela s'appelle la **vérification** et ici nous vérifions l'intégrité des données envoyées par le client.
3. Vérification (à nouveau). Nous avons besoin d'un moyen de vérifier que l'ordinateur avec lequel nous communiquons n'est pas un imposteur. Il s'agit d'une autre forme de vérification mais ici nous vérifions l'identité de l'ordinateur.

Après ces trois étapes, nous pouvons maintenant communiquer de manière sécurisée avec un ordinateur distant.

Après ces étapes, nous pouvons partager des données "secrètes" de manière sécurisée et nous pouvons également vérifier si un client a la permission d'accéder à un hôte de manière plus sécurisée qu'en utilisant un mot de passe. Ce processus est appelé **authentification utilisant le chiffrement asymétrique**.

Chacune de ces sections ci-dessous entrera dans plus de détails sur ces étapes.

### **Configuration d'un canal chiffré**

Une partie centrale du protocole SSH est qu'il est sécurisé (c'est même dans le nom !), ce qui signifie que toutes les informations envoyées en utilisant SSH sont chiffrées.

#### Comment ces informations sont-elles chiffrées ?

Le chiffrement signifie essentiellement "mélanger les lettres" en utilisant des mathématiques astucieuses. Les deux ordinateurs doivent avoir un moyen de chiffrer les informations de sorte que seul l'autre ordinateur puisse déchiffrer les informations et les comprendre.

#### Comment cela fonctionne-t-il ?

Les deux ordinateurs ont une version identique d'une **clé symétrique**. La clé symétrique est simplement une chaîne de lettres stockée quelque part sur les ordinateurs. Les ordinateurs peuvent utiliser les clés symétriques pour chiffrer et également déchiffrer les messages qui leur sont envoyés.

L'utilisation de cette approche de clé symétrique est appelée **chiffrement symétrique**. La partie "symétrique" vient du fait que la clé symétrique sur chaque ordinateur est identique. Cette approche fonctionne vraiment bien... mais elle ne fonctionne que tant que aucun autre ordinateur n'a accès à la clé symétrique.

#### Un problème

Comment les deux ordinateurs savent-ils quelle est la clé symétrique ?

Un ordinateur pourrait la créer et l'envoyer dans un message via Internet. Mais les messages ne seraient pas encore chiffrés, donc quiconque intercepte les messages aurait instantanément la clé symétrique... et pourrait déchiffrer toutes les communications futures. Ce n'est pas bon !

Cela s'appelle parfois le problème de "l'échange de clés". Il est clair que nous devons ajouter une autre étape au processus avant de pouvoir utiliser les clés symétriques.

#### Une solution

Une solution au problème de "l'échange de clés" ci-dessus est que les deux ordinateurs partagent certaines informations publiques entre eux (elles sont "publiques" ce qui signifie qu'ils ne se soucient pas si quelqu'un les intercepte) et combinent cela avec certaines informations sur leur propre ordinateur pour **créer de manière indépendante** des **clés symétriques identiques**.

Ces clés symétriques peuvent ensuite être utilisées dans le chiffrement symétrique de la manière décrite ci-dessus.

#### Comment cela fonctionne

Les deux ordinateurs ont chacun leur propre clé privée et clé publique. Ensemble, elles forment une **paire de clés**. Les ordinateurs **partagent leurs clés publiques** entre eux via Internet. Donc, à ce stade du processus, chaque ordinateur connaît

* sa propre clé privée,
* sa propre clé publique,
* et la clé publique de l'autre ordinateur.

#### Génération de clés symétriques

Les deux ordinateurs utilisent ensuite ces trois éléments d'information pour générer de manière indépendante une **clé symétrique identique**.

Chaque ordinateur utilise un algorithme mathématique qui utilise les trois entrées mentionnées ci-dessus. Cet algorithme fait partie de l'algorithme d'échange de clés Diffie-Hellman. L'algorithme qui sera exécuté sur chaque ordinateur est quelque chose comme ceci :

```
Hôte
pub_2 = clé publique de l'autre ordinateur
pub_1 = ma clé publique
pri_1 = ma clé privée

f(pub_2, pub_1, pri_1) = abcdefg // Clé Symétrique

Client :
f(pub_1, pub_2, pri_2) = abcdefg // Clé Symétrique
```

L'important à retenir ici est que les ordinateurs ont **partagé uniquement des informations publiques** via Internet **mais ont tout de même pu créer des clés symétriques !**

L'approche consistant à utiliser des paires de clés et à partager des informations publiques pour générer des clés symétriques identiques est appelée **chiffrement asymétrique**. Il est appelé "asymétrique" parce que les deux ordinateurs commencent avec leurs propres paires de clés différentes.

**Jusqu'à présent :** nous avons vu comment utiliser le chiffrement asymétrique pour générer de manière indépendante des clés symétriques identiques sur les deux ordinateurs _de manière sécurisée_ (résolvant le problème de l'échange de clés) et ensuite échanger des informations de manière sécurisée entre les ordinateurs en utilisant des clés symétriques pour le chiffrement et le déchiffrement.

### Vérification

Donc, nous pouvons communiquer de manière sécurisée. Mais la partie suivante du processus d'établissement d'une session SSH est de vérifier que les données n'ont pas été altérées lors de leur transmission **et** que l'autre ordinateur est bien celui qu'il prétend être.

#### Pourquoi en avons-nous besoin ?

Un autre ordinateur pourrait usurper l'identité de l'un des ordinateurs et initier l'échange de clés ci-dessus. Donc, comment pouvons-nous **sécuriser** la vérification que le message provient bien de l'autre ordinateur et non d'un imposteur ?

#### Hachage

Nous devons utiliser une fonction de **hachage**. Il s'agit simplement d'une fonction mathématique qui prend des entrées et produit une chaîne de taille fixe.

La caractéristique importante de cette fonction est qu'il est virtuellement impossible de déterminer quelles étaient les entrées en utilisant uniquement les sorties.

Après qu'un client et un hôte ont généré leurs clés symétriques, le client utilisera une fonction de hachage pour générer un HMAC. Cela signifie simplement "code d'authentification de message basé sur le hachage". Il s'agit simplement d'une autre chaîne de caractères/nombres. Le client enverra ce HMAC au serveur pour vérification.

Les ingrédients de la fonction de hachage sont

* La clé symétrique sur le client
* Le numéro de séquence du paquet (chaque message envoyé est contenu dans un "paquet" d'informations)
* Le contenu du message (chiffré !!!)

Un exemple avec des données fictives :

```
symm_key       = abcdefg
pkge_no        = 13
encr_message   = mot_de_passe_chiffré

Hash(symm_key, pkge_no, encr_message) = *HMAC* // Valeur hachée
```

#### Comment l'hôte utilise-t-il ces informations ?

Lorsque l'hôte reçoit le HMAC, il peut utiliser **la même** fonction de hachage avec ces trois ingrédients :

* sa propre copie de la clé symétrique (identique !),
* le numéro de séquence du paquet,
* et le message chiffré.

Si la valeur hachée qu'il calcule est la même que le HMAC qu'il a reçu du client, alors nous avons vérifié que l'ordinateur connecté est le même que l'ordinateur qui possède la clé symétrique.

Rappelez-vous que seul l'hôte et le client savent quelle est la clé symétrique et aucun autre ordinateur ne le sait !

Ici, il n'a donc pas d'importance que l'hôte ne connaisse pas le contenu décodé du message chiffré — l'hôte a tout de même vérifié l'identité de l'ordinateur connecté !

La beauté de cette approche est que nous n'avons pas seulement vérifié l'identité du client et nous sommes assurés que les données n'ont pas été altérées, mais nous l'avons fait de manière sécurisée (sans **partager aucune information privée**).

**Résumé :** nous avons utilisé une fonction de hachage sur le client puis sur l'hôte pour vérifier l'intégrité des données et vérifier l'identité du client.

![Image](https://cdn-media-1.freecodecamp.org/images/ej0rVm5QFV0xIuBr4f2Dm8CIAqxZTjkfl5jP)

### Authentification

La dernière partie de la communication sécurisée avec des ordinateurs distants est :

_même si_ nous avons généré des clés symétriques avec l'ordinateur connecté et

_même si_ nous utilisons les clés symétriques pour communiquer de manière sécurisée et

_même si_ l'ordinateur connecté est réellement le client que nous attendons et non un imposteur,

alors nous avons établi une session SSH... mais l'ordinateur connecté a-t-il **l'autorisation** d'accéder au contenu de l'hôte ?

Cela s'appelle "l'authentification" : l'acte de vérifier les permissions et les droits d'accès.

#### Il existe deux façons de vérifier l'authentification :

**1—Utilisation d'un mot de passe**

Le client peut envoyer à l'hôte un message (chiffré) contenant un mot de passe. L'hôte peut déchiffrer le message et vérifier le mot de passe dans une base de données pour vérifier si le client a la permission d'accéder à l'utilisateur spécifié (zone de l'ordinateur). Mission accomplie.

**2 — Utilisation de paires de clés et de chiffrement asymétrique**

Plus tôt, nous avons vu comment le chiffrement asymétrique peut utiliser deux paires de clés pour générer de manière sécurisée des clés symétriques identiques sur le client et l'hôte. En utilisant des idées similaires, le client peut **se connecter sans mot de passe**.

Voici une approche très haut niveau de la façon dont le processus fonctionne :

_Configuration :_

Sur le client, allez dans le terminal et utilisez une commande pour générer une clé publique et une clé privée (en surface, il utilise "RSA", un algorithme mathématique) sur le client. Copiez la clé **publique** (PAS la clé privée !) dans le presse-papiers.

_Je répète :_ Copiez la clé **PUBLIQUE** (**PAS LA CLÉ PRIVÉE !**) dans le presse-papiers.

Ensuite, dans le terminal sur le client, utilisez un mot de passe pour vous connecter à distance à l'hôte. Collez la clé publique du client dans le dossier approprié sur l'hôte aux côtés des autres clés publiques.

Maintenant, l'hôte a

* Sa propre paire de clés publique/privée
* La clé publique du client

En regardant la section ci-dessus sur l'algorithme d'échange de clés, vous pouvez voir comment l'hôte a tous les ingrédients nécessaires pour générer une clé symétrique !

_Défier :_

Lorsque le client veut se connecter, l'hôte peut émettre un "défi" en envoyant un message qui a été chiffré (avec la clé symétrique de l'hôte) et dire : _"Je ne vous autoriserai l'accès que si vous pouvez déchiffrer ce message !"_.

Le client a alors

* sa propre clé publique et privée
* la clé publique de l'hôte
* le message chiffré

Donc maintenant le client a tout ce dont il a besoin pour générer une clé symétrique (identique)... et déchiffrer le message ! Il peut déchiffrer le message et envoyer une confirmation qu'il a "réussi" le défi à l'hôte.

L'hôte est satisfait que le client connecté est autorisé et accorde la permission d'accès.

**Pourquoi se donner la peine d'utiliser la deuxième approche ?**

Cela est considéré comme plus sécurisé que l'utilisation d'un simple mot de passe car un bot peut utiliser une approche "brute force" pour continuer à utiliser de nombreuses combinaisons pour deviner votre mot de passe, mais ils n'auront pas les bonnes paires de clés pour que la deuxième approche fonctionne.

Pour aller plus loin :

[**Tutoriel SSH pour débutants - Comment fonctionne SSH**](https://www.hostinger.com/tutorials/ssh-tutorial-how-does-ssh-work)

[SSH, ou Secure Shell, est un protocole d'administration à distance qui permet aux utilisateurs de contrôler et de modifier leurs serveurs distants...www.hostinger.com](https://www.hostinger.com/tutorials/ssh-tutorial-how-does-ssh-work)

[https://www.udemy.com/the-complete-junior-to-senior-web-developer-roadmap/](https://www.udemy.com/the-complete-junior-to-senior-web-developer-roadmap/)

### Conclusion

SSH est un outil important utilisé pour contrôler à distance d'autres ordinateurs.

SSH est sécurisé car les deux ordinateurs peuvent chiffrer et déchiffrer les messages en utilisant des clés symétriques identiques (appelé "chiffrement symétrique").

Les principales étapes pour initier une session SSH sont :

1. **Configuration d'un canal chiffré.** Utilisation du chiffrement asymétrique pour résoudre le problème de l'échange de clés qui génère de manière indépendante des clés symétriques identiques sur les deux ordinateurs sans partager aucune information privée.
2. **Vérification :** Utilisation du hachage sur les deux ordinateurs pour vérifier l'identité de l'ordinateur connecté
3. Vérification (à nouveau). Utilisation du hachage sur les deux ordinateurs pour vérifier que l'intégrité des données n'a pas été compromise lors de la transmission.

Nous pouvons ensuite utiliser SSH pour envoyer des données de manière sécurisée entre les ordinateurs. Un cas d'utilisation important de cela est pour **l'authentification**. Bien que vous puissiez utiliser un mot de passe, l'utilisation du chiffrement asymétrique pour vérifier que le "client" connecté a la permission d'accéder à l'"hôte" est considérée comme plus sécurisée.

Si vous êtes intéressé par l'amélioration de vos compétences SSH, je vous recommande sérieusement [ce](https://www.udemy.com/the-complete-junior-to-senior-web-developer-roadmap/) cours. Je l'ai trouvé vraiment utile pour améliorer certaines de mes compétences ! (_disclaimer :_ Je n'ai aucun lien ou attache avec l'auteur ou la plateforme. J'ai suivi le cours il y a un moment et je l'ai trouvé vraiment bon !)

Merci d'avoir lu !