---
title: Comment protéger les données en transit à l'aide de HMAC et Diffie-Hellman
  dans Node.js [Guide complet]
subtitle: ''
author: Hamdaan Ali
co_authors: []
series: null
date: '2024-03-18T23:00:22.000Z'
originalURL: https://freecodecamp.org/news/hmac-diffie-hellman-in-node
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/Protect-Data-in-Transit-Handbook-v2--1-.png
tags:
- name: data
  slug: data
- name: handbook
  slug: handbook
- name: MathJax
  slug: mathjax
- name: Security
  slug: security
seo_title: Comment protéger les données en transit à l'aide de HMAC et Diffie-Hellman
  dans Node.js [Guide complet]
seo_desc: Data integrity refers to the assurance that data will remain accurate, unaltered,
  and consistent throughout its lifecycle. In communication, data integrity is important
  in safeguarding against unintended alterations and malicious interventions during...
---

L'intégrité des données fait référence à l'assurance que les données resteront exactes, inchangées et cohérentes tout au long de leur cycle de vie. Dans la communication, l'intégrité des données est importante pour se prémunir contre les altérations involontaires et les interventions malveillantes lors de la transmission des données.

L'intégrité des données numériques est assurée à l'aide d'algorithmes de hachage. Le module `crypto` dans Node fournit diverses fonctions de bibliothèque intégrées et vérifiées pour fournir des moyens non seulement de vérifier l'intégrité des données, mais aussi l'authenticité de leur origine.

Ce guide vise à mettre en lumière le fonctionnement interne des fonctions de la bibliothèque `crypto` et à vous donner un aperçu du fonctionnement interne de HMAC et de l'échange de clés Diffie-Hellman. Cela vous aidera à prendre des décisions éclairées sur les algorithmes de hachage et les longueurs de clés en fonction des exigences de votre entreprise.

L'objectif principal de ce guide est de souligner l'aspect crucial de l'intégrité des données plutôt que de discuter des divers algorithmes de chiffrement disponibles.

Le chiffrement est utilisé pour protéger les informations en les convertissant dans un format sécurisé, ce qui garantit leur confidentialité. Mais l'intégrité des données concerne le fait de s'assurer que les données restent exactes et inchangées.

Vous pouvez également regarder la vidéo associée ici :

%[https://youtu.be/FAfzQo_eJHI?feature=shared]

## Table des matières

* [Prérequis](#heading-prerequisites)
* [Le paradigme Alice-Bob](#heading-the-alice-bob-paradigm)
* [Code de détection de message (MDC)](#heading-message-detection-code-mdc)
* [Code d'authentification de message (MAC)](#heading-message-authentication-code-mac)
* [MAC basés sur le hachage (HMAC)](#heading-hash-based-macs-hmac)
* [Le protocole Diffie-Hellman-Merkle](#heading-the-diffie-hellman-merkle-protocol)
* [Relier les points](#heading-connecting-the-dots)
* [Appel des API](#heading-invoking-the-apis)
* [Conclusion](#heading-wrapping-up)
* [Références](#heading-references)

## **Prérequis**

1. **Node et Express :** Nous allons créer une application TypeScript utilisant le framework Express. Une compréhension de base du framework serait utile. Vous aurez besoin de l'[environnement d'exécution Node](https://nodejs.org/en/download/) pour exécuter les scripts.
2. **Client Postman :** Pour faire une requête API et tester l'application exemple, vous aurez besoin d'un outil pour faire des requêtes HTTP. Vous pouvez utiliser la fonction "Edit and Send" de votre navigateur web sous l'onglet Networks, mais comme tous les navigateurs ne permettent pas cela, il est préférable d'utiliser un outil comme [Postman](https://www.postman.com/downloads/) qui offre une meilleure interface pour observer les réponses.

## Le paradigme Alice-Bob

Tout au long de ce guide, vous rencontrerez de nombreux diagrammes de séquence et preuves mathématiques utilisant le paradigme Alice-Bob.

Le paradigme Alice-Bob est une convention courante en cryptographie où deux entités génériques, souvent nommées Alice et Bob, sont utilisées pour illustrer divers scénarios, protocoles ou principes cryptographiques.

![Le paradigme Alice-Bob](https://www.freecodecamp.org/news/content/images/2024/03/alice-bob-1.svg)
_Le paradigme Alice-Bob_

Ces personnages représentent deux parties engagées dans une communication, Alice représentant généralement l'expéditeur ou l'initiateur, et Bob représentant le destinataire ou le répondant.

Nous introduisons souvent Eve comme une troisième partie, symbolisant un écouteur ou un attaquant potentiel, ajoutant un élément de risque de sécurité et illustrant des scénarios où des entités externes pourraient tenter d'intercepter ou de manipuler la communication.

L'application exemple montrée dans les sections suivantes modélise ce paradigme Alice-Bob pour utiliser Boost Inc. et Account Aggregator (AA) comme les parties engagées dans la communication.

## Code de détection de message (MDC)

Lorsque Alice doit envoyer des données critiques à Bob via Internet, les données changent de mains, passant entre des routeurs et des serveurs, chaque étape portant le risque potentiel d'altérations involontaires.

Si Eve parvient à mettre la main sur les données d'Alice, ils pourraient les modifier. Ainsi, l'intégrité des données devient douteuse, soulignant que leur état original pourrait avoir été compromis lors de la transmission.

Notez que nous parlons de l'intégrité et non de la confidentialité des données. Même après qu'Alice ait chiffré les données, cela ne garantit pas intrinsèquement que les données n'ont pas été altérées pendant le transit.

Considérez ce scénario : même si Eve ne peut pas déchiffrer le message chiffré, ils pourraient tenter de modifier le texte chiffré en transit. Cela pourrait impliquer la modification de bits, la réorganisation de paquets ou l'injection de code malveillant, pouvant entraîner des conséquences involontaires lors du déchiffrement.

C'est là qu'intervient un code de détection de message (MDC) ou un hachage. Un code de détection de modification (MDC) est un digest de message ou une somme de contrôle qui peut prouver l'intégrité d'un message : que le message n'a pas été changé [1].

La figure ci-dessous explique comment le MDC est utilisé pour vérifier l'intégrité d'un message :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/MDC.png)
_Code de détection de modification [1]_

Une fonction de hachage est utilisée pour générer le digest pour un message donné. Cette fonction de hachage traite l'ensemble du contenu du message, produisant une chaîne de caractères de taille fixe qui représente de manière unique le contenu du message. Cela s'appelle le digest du message ou MDC.

Notez que toute fonction de hachage, telle que SHA-256, SHA-3 ou MD5, peut être utilisée en fonction de vos exigences de sécurité spécifiques et de vos préférences.

Une fois le digest généré, il sert d'empreinte digitale unique pour le message original. Lorsque Alice envoie à la fois le message et son digest correspondant à Bob, ils peuvent appliquer indépendamment la même fonction de hachage au message reçu. Si le digest calculé correspond à celui reçu d'Alice, cela sert de preuve irréfutable que le message n'a subi aucune modification pendant la transmission.

## Code d'authentification de message (MAC)

Bien que le MDC ou la somme de contrôle soit généralement transféré via un canal sécurisé, il peut arriver que la sécurité du canal ou de la partie de confiance elle-même soit compromise. Dans un tel cas, Eve peut facilement modifier à la fois le message et le digest et Bob ne saura jamais si le message provient réellement d'Alice comme prévu.

Ce que le MDC manque, c'est une garantie définitive de l'origine du message, laissant une vulnérabilité potentielle dans la confirmation de l'expéditeur réel.

C'est là qu'intervient le code d'authentification de message (MAC). Les MAC non seulement garantissent l'intégrité du message, détectant toute altération non autorisée, mais ils fournissent également un mécanisme pour authentifier l'origine des données. En d'autres termes, les MAC offrent l'assurance que le message provient effectivement d'Alice et non de quelqu'un d'autre.

La figure ci-dessous explique comment le MAC peut aider à authentifier l'origine d'un message en plus de fournir une vérification d'intégrité :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/MAC.png)
_Code d'authentification de message [1]_

Remarquez que la différence entre un MDC et un MAC est que le MAC inclut également une clé secrète \(K\) entre Alice et Bob. La fonction de hachage prend également une clé \(K\) ainsi que le message \(M\) pour générer un MAC.

                                                          $$ h (K | M) = MAC $$

Maintenant, le message et le MAC peuvent être envoyés sur le même canal non sécurisé. Lorsque Bob reçoit ce \( M + MAC \), il peut séparer le message M et calculer le MAC pour celui-ci en utilisant la même fonction de hachage et la clé secrète \(K\).

Bob comparera ensuite le MAC nouvellement calculé avec celui qu'il a reçu. Si les deux MAC correspondent, le message est authentique et n'a pas été modifié par un adversaire.

$$ Alice: S(K,M) = MAC \\ Bob: V(M, K, MAC) = Accept/ Reject $$

Puisque Eve ne possède pas cette clé secrète \(K\), ils ne peuvent pas modifier le message et générer un MAC valide. Par conséquent, le MAC résultant devient une empreinte digitale unique, signifiant non seulement l'intégrité du message mais aussi l'authentification de son origine.

## MAC basés sur le hachage (HMAC)

Bien que les MAC fournissent une garantie d'authentification de l'origine d'un message, ils ne garantissent pas encore l'infalsifiabilité. Il est facile pour Eve d'effectuer une attaque de l'homme du milieu (MiTM), d'intercepter la paire MAC + Message puis d'effectuer une attaque par extension de longueur.

Étant donné \( S = h( K || M) \) et le message \(M\), Eve peut étendre \(M\) à \(M' = M || Pad || w\) et créer \(MAC(M')\); où \(MAC(M')\) est évalué comme
\( S = h( K || M || Pad || w) \).

Eve n'a pas besoin de connaître la clé secrète \(K\) pour étendre le message \(M\) à \(M'\). Lorsque Alice reçoit ce \(M'\) modifié et \(MAC(M')\), ils sont incapables de déterminer la modification.

HMAC ou un MAC basé sur le hachage est une méthode spécifique pour construire un algorithme MAC à partir d'une fonction de hachage résistante aux collisions. HMAC utilise deux passes de calcul de hachage et offre une meilleure immunité contre les attaques par extension de longueur. La figure ci-dessous explique la construction des HMAC.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/HMAC-1.png)
_Code d'authentification de message basé sur le hachage [1]_

Il y a plusieurs étapes impliquées dans la mise en œuvre des HMAC [1] :

1. Diviser le message en N blocs, chacun de b bits
2. Sélectionner une clé secrète et la remplir à gauche avec des 0 pour créer une clé de b bits et effectuer un XOR exclusif avec une constante appelée \(ipad\) (remplissage d'entrée).
3. Utiliser la même clé secrète et effectuer un XOR avec une autre constante appelée \(opad\).
Les valeurs de \(ipad\) et \(opad\) sont des constantes fixes telles que définies dans les normes HMAC [3]. La valeur de \(ipad\) est prise comme une répétition de b/8 de la séquence
00110110 (hex : 36) et la valeur de \(opad\) est prise comme une répétition de b/8 de la séquence 01011100 (hex : 5C).
Ces valeurs sont définies de manière à avoir la distance de Hamming la plus "non régulière" [Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance) l'une de l'autre.
La distance de Hamming entre \(ipad\) et \(opad\) est de 4, ce qui signifie que exactement la moitié des bits sont inversés.
4. Préfixer le résultat produit à l'étape 2 au bloc de message. Utiliser la fonction de hachage sur ce bloc \(N+1\) pour créer un digest de message de n bits appelé HMAC intermédiaire.
5. Le HMAC intermédiaire est préfixé avec des \(0\) pour faire un bloc de b bits, puis le résultat de l'étape 3 est préfixé à ce bloc.
6. Utiliser à nouveau la fonction de hachage sur le résultat de l'étape 5 pour obtenir un HMAC final de n bits.

Mathématiquement, cela peut être représenté comme :

$$ S(k, m) = H(k \oplus \text{opad}  ||  H(k \oplus \text{ipad}  || m)) $$

Maintenant, si Eve essaie d'étendre \(M\) à \(M' = M || Pad || w\), la construction HMAC résultante serait :

$$ HMAC(K, M')=H(K||opad, H(K||ipad, M || Pad || w)) $$

En raison de l'application unique de \(opad\) dans le hachage externe, l'attaquant ne peut pas construire \(H(K||opad, <...> )\) sans connaître la clé \(K\). Le remplissage externe perturbe l'état interne pour toute entrée supplémentaire, contrariant la tentative de l'attaquant.

## Le protocole Diffie-Hellman-Merkle

L'un des principaux défis des chiffres à clé symétrique est la distribution des clés. Une question fondamentale se pose naturellement : comment Bob saura-t-il quelles clés Alice a utilisées ?

Une réponse très intuitive à ce problème pourrait être d'utiliser un échange de clés ou un centre de distribution de clés (KDC). Cependant, l'utilisation d'un KDC ou d'un échange de clés introduit une mise en garde notable : la nécessité d'un canal sécurisé pour transmettre les clés.

La sécurité d'un système utilisant un centre de distribution de clés (KDC), comme dans le cas du protocole d'authentification Kerberos, dépend fortement de la sécurité du KDC lui-même. Si le KDC est compromis, les clés cryptographiques qu'il gère et distribue peuvent être exposées, entraînant des vulnérabilités de sécurité potentielles dans l'ensemble du système, comme on l'a vu dans une attaque Golden Ticket.

En l'an 1979, [Ralph Merkle](https://en.wikipedia.org/wiki/Ralph_Merkle), [Whitfield Diffie](https://en.wikipedia.org/wiki/Whitfield_Diffie) et [Martin Hellman](https://en.wikipedia.org/wiki/Martin_Hellman) ont trouvé un moyen d'échanger des clés cryptographiques de manière sécurisée sur des canaux publics non sécurisés.

Le protocole Diffie-Hellman-Merkle fournit un moyen pour deux parties de convenir d'une clé secrète partagée sur un canal non sécurisé sans échanger directement cette clé. Le module `crypto` dans Node.js contient la classe `DiffieHellman`, qui est un utilitaire pour créer des échanges de clés Diffie-Hellman.

Avant d'examiner toutes les fonctions définies dans cette classe, il est important de comprendre les mathématiques qui entourent le protocole Diffie-Hellman-Merkle. Le diagramme de séquence UML ci-dessous explique les étapes impliquées dans le protocole Diffie-Hellman-Merkle :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/dh-1.svg)
_Le protocole Diffie-Hellman-Merkle_

Le processus commence avec l'une des parties qui souhaite établir une communication sécurisée avec l'autre. Dans ce cas, Alice souhaite démarrer la communication.

Alice choisira d'abord un générateur `g` choisi aléatoirement et un grand nombre premier `p`. Augmenter la longueur du nombre premier entraîne une sécurité accrue, car cela amplifie la difficulté pour les adversaires d'exécuter certaines attaques cryptographiques.

Cependant, l'augmentation du nombre premier entraîne également des coûts de calcul. Des nombres premiers plus longs nécessitent plus de ressources de calcul pour effectuer la génération de clés.

Maintenant, Alice doit sélectionner une clé privée `a` et calculer une exponentiation modulaire :

$$ A = g^a  (\text{mod} , p) $$

Alice enverra le générateur `g`, le grand nombre premier `p` et la clé publique d'Alice `A` à Bob. À ce stade, Bob a toutes les valeurs dont il a besoin pour évaluer sa propre exponentiation modulaire de :

$$ A = g^b  (\text{mod} , p) $$

Il renverra cette clé publique `B` à Alice.

Notez qu'à ce stade, toutes les communications se font sur un canal non sécurisé. Les valeurs `g`, `p`, `A` et `B` "peuvent" également être envoyées en texte clair. La clé secrète réelle est évaluée lorsque Alice et Bob utilisent ces données pour calculer ce que l'on appelle un "Secret Partagé".

Secret partagé calculé par A :

$$ S = A^b  (\text{mod} , p) \\  S = g^{\left(ab\right)}  (\text{mod} , p) $$

Secret partagé calculé par B :

$$ S = B^a  (\text{mod} , p) \\  S = g^{\left(ab\right)}  (\text{mod} , p) $$

Remarquez comment le secret partagé calculé par les deux parties à leur extrémité est le même.

Ce résultat symétrique est l'essence de l'échange de clés Diffie-Hellman, où chaque partie calcule indépendamment le secret partagé en utilisant sa clé privée et la clé publique reçue de l'autre partie. Cela garantit que Alice et Bob arrivent à un secret partagé identique, établissant une base sécurisée pour une communication chiffrée ultérieure.

### Pourquoi le secret partagé est-il sécurisé ?

L'échange de clés Diffie-Hellman repose sur les principes mathématiques du logarithme discret, des racines primitives et de l'exponentiation modulaire.

L'exponentiation modulaire est le problème de calculer \(a^b  mod n\), où \(a\), \(b\), et \(n\) sont des entiers connus. Le logarithme discret est le problème de trouver \(x\) tel que \(a^x  mod n = b\), où \(a\), \(b\), et \(n\) sont des entiers connus et \(a\) est une racine primitive modulo \(n\).

La sécurité de Diffie-Hellman est enracinée dans la complexité computationnelle du calcul des logarithmes discrets.

Par exemple, étant donné `g`, `p` et `a`, il est facile de calculer `A` car l'exponentiation modulaire est dans P, ce qui signifie qu'il existe un algorithme en temps polynomial pour le résoudre.

Mais l'inverse ne peut pas être dit vrai. Étant donné `g`, `p` et `A`, le calcul de `a` nécessite la résolution du problème du logarithme discret, qui est largement considéré comme une tâche computationnellement irréalisable [2].

Rappelez-vous que les deux parties calculeront le secret partagé à leur extrémité et qu'il n'est pas nécessaire d'envoyer ce secret à l'autre partie. Cela élimine le risque que le secret partagé soit intercepté par Eve et la seule option qui leur reste est de résoudre le problème du logarithme discret.

## Relier les points

La clé \(K\) que nous fournissons dans un HMAC doit être la même pour Alice et Bob. Maintenant que nous savons comment fonctionne un échange de clés Diffie-Hellman-Merkle, il devient intuitif que nous pouvons utiliser le secret partagé comme clé pour un HMAC.

Alice peut utiliser la clé partagée \(S\) dans la fonction HMAC comme paramètre et Bob peut utiliser le même secret partagé \(S\), calculé à leur extrémité, dans l'algorithme de vérification.

Le module `crypto` dans Node.js fournit diverses fonctions intégrées pour implémenter des constructions cryptographiques telles que les HMAC et l'échange de clés Diffie-Hellman. Il est toujours recommandé d'utiliser des bibliothèques cryptographiques vérifiées et d'éviter d'implémenter des algorithmes cryptographiques vous-même en raison des préoccupations concernant les [attaques par canaux auxiliaires](https://en.wikipedia.org/wiki/Side-channel_attack) ou un [Heartbleed](https://en.wikipedia.org/wiki/Heartbleed).

Créons une application TypeScript/Node.js pour comprendre l'implémentation et les prototypes de ces fonctions. Les deux entités impliquées dans la communication dans cette application seront Boost Inc. et Account Aggregator. Boost doit envoyer des données critiques à Account Aggregator.

Nous utiliserons d'abord la classe `DiffieHellman` pour créer des clés secrètes pour les deux entités. Boost utilisera ensuite la clé secrète pour créer un HMAC en utilisant la classe `Hmac` dans Node. Account Aggregator recevra ce HMAC avec le message. Ils vérifieront ce HMAC par rapport au HMAC nouvellement généré à partir du message qu'ils ont reçu.

Notez que le code à l'extrémité d'Account Aggregator sera simulé et nous créerons des points de terminaison d'API pour chaque opération afin de montrer la séparation des préoccupations dans cette application exemple.

Le diagramme de séquence suivant explique ce que fait l'application :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Sample-Application-1.svg)
_Diagramme de séquence UML pour l'application exemple_

### Configuration du projet

À la racine de votre espace de travail, installez Express, Axios, les définitions de type de Node et les définitions de type d'Express en utilisant la commande suivante :

```bash
npm init -y | npm install axios express
npm install -D nodemon ts-node @types/express @types/node typescript
```

Configurez `tsconfig` selon vos préférences et créez un fichier appelé `cryto.utils.ts` sous `src/utils`. Créons une interface et importons tous les modules nécessaires de la bibliothèque `crypto` :

```ts
import { createHmac, createDiffieHellman, DiffieHellman, KeyObject, BinaryLike } from 'crypto';

export interface KeyPair {
  publicKey: Buffer;
  privateKey: Buffer;
  generator: Buffer;
  prime: Buffer;
  diffieHellman: DiffieHellman;
}
```

Cette interface fonctionnera comme un plan pour gérer les paires de clés cryptographiques dans cette application. Elle encapsule les clés publiques et privées, le générateur, le nombre premier et un objet Diffie-Hellman.

En utilisant cette interface, nous assurerons une approche structurée et standardisée pour gérer les informations de paires de clés cryptographiques, promouvant ainsi la clarté et la cohérence dans les opérations cryptographiques au sein d'un environnement Node.js.

### La fonction createDiffieHellman

Ensuite, nous définirons la fonction `generateKeyPair` qui nous permettra de générer les clés privées et publiques, \(A\) et \(B\) ainsi que le grand nombre premier \(p\) et le générateur \(g\) en utilisant les fonctions `createDiffieHellman` et `generateKeys`.

```ts
export function generateKeyPair(prime?: any, generator?: any): KeyPair {
  const diffieHellman = prime && generator ? createDiffieHellman(prime, 'hex', generator, 'hex') : createDiffieHellman(2048);
  diffieHellman.generateKeys();

  return {
    publicKey: diffieHellman.getPublicKey(),
    privateKey: diffieHellman.getPrivateKey(),
    generator: diffieHellman.getGenerator(),
    prime: diffieHellman.getPrime(),
    diffieHellman,
  };
}
```

Remarquez que les paramètres de cette fonction – `prime` et `generator` – sont optionnels. Cela est dû au fait que le `createDiffieHellman` sous-jacent a cinq surcharges définies :

```ts
function createDiffieHellman(primeLength: number, generator?: number): DiffieHellman;
    
function createDiffieHellman(
	prime: ArrayBuffer | NodeJS.ArrayBufferView,
	generator?: number | ArrayBuffer | NodeJS.ArrayBufferView,
): DiffieHellman;

function createDiffieHellman(
    prime: ArrayBuffer | NodeJS.ArrayBufferView,
    generator: string,
    generatorEncoding: BinaryToTextEncoding,
): DiffieHellman;

function createDiffieHellman(
    prime: string,
    primeEncoding: BinaryToTextEncoding,
    generator?: number | ArrayBuffer | NodeJS.ArrayBufferView,
): DiffieHellman;

function createDiffieHellman(
    prime: string,
    primeEncoding: BinaryToTextEncoding,
    generator: string,
    generatorEncoding: BinaryToTextEncoding,
): DiffieHellman;
```

La première fonction crée un objet Diffie-Hellman avec un nombre premier généré aléatoirement de la longueur spécifiée. Le `createDiffieHellman(2048);` crée un objet Diffie-Hellman où la longueur du nombre premier généré aléatoirement est de 2048 bits.

Lorsque aucune valeur de générateur n'est fournie à cette fonction, elle prend la valeur par défaut de 2. La longueur du nombre premier doit nécessairement être grande et si vous sélectionnez une valeur petite, Node lancera une erreur signifiant que cette longueur ne permettra pas de créer une clé sécurisée.

Au lieu de passer la longueur du nombre premier, nous pouvons passer le nombre premier sous forme de tampon. C'est ce que fera Account Aggregator à leur extrémité lorsque Boost enverra les détails nécessaires.

De même, vous pouvez utiliser les autres déclarations de fonction selon votre cas d'utilisation pour passer le nombre premier et le générateur en tant que types `ArrayBuffer` ou `ArrayBufferView` ou en tant que `string` avec un encodage spécifié.

### La fonction computeSecret

Maintenant, définissons une méthode `generateSharedSecret` qui prend une paire de clés et une clé publique comme paramètre et calcule le secret partagé \(S\) :

```ts
export function generateSharedSecret(keyPair: KeyPair, publicKey: Buffer): Buffer {
  return keyPair.diffieHellman.computeSecret(publicKey);
}
```

La fonction `computeSecret` a également quatre surcharges, qui vous permettent de fournir le paramètre de clé publique sous forme de `string` ou de `ArrayBufferView` ainsi que des options pour spécifier l'`inputEncoding` et l'`outputEncoding`.

### La fonction createHmac

Maintenant que nous avons calculé notre secret partagé, créons une fonction `generateHMAC` qui consomme ce secret partagé et génère un digest contre celui-ci.

```ts
export function generateHMAC(data: any, secretKey: KeyObject | BinaryLike): any {
  data = JSON.stringify(data);
  const hmac = createHmac('sha256', secretKey);
  hmac.update(data);
  return hmac.digest('hex');
}

```

Le premier paramètre de la fonction `createHmac` prend un algorithme. C'est là que vous devez spécifier quelle fonction de hachage sous-jacente vous souhaitez utiliser.

Rappelez-vous que la sécurité de HMAC repose sur divers facteurs, y compris la force cryptographique de la fonction de hachage sous-jacente, la taille de sa sortie de hachage, et la qualité et la taille de la clé.

Les options qui vous sont données sous ce paramètre d'algorithmes dépendent des algorithmes disponibles pris en charge par la version OpenSSL sur la plateforme. Pour vérifier quels algorithmes sont disponibles pour vous, exécutez la commande suivante dans le terminal :

```bash
openssl list -digest-algorithms
```

Cela vous donnera une liste à partir de laquelle vous pouvez sélectionner votre algorithme souhaité pour la fonction de hachage sous-jacente :

```bash
RSA-MD4 => MD4
RSA-MD5 => MD5
RSA-MDC2 => MDC2
RSA-RIPEMD160 => RIPEMD160
RSA-SHA1 => SHA1
RSA-SHA1-2 => RSA-SHA1
RSA-SHA224 => SHA224
RSA-SHA256 => SHA256
...
```

La clé secrète que la fonction `createHmac` prend pourrait être de type `KeyObject` ou de type `BinaryLike`. Notez que le type `BinaryLike` est un type d'union dans TypeScript. C'est un type qui peut être soit une `string` soit un `NodeJS.ArrayBufferView`.

Le paramètre `data` de la fonction `createHmac` est conçu pour accepter des `strings`, des `Buffer`, des `TypedArray` et des `DataView`. Pour simplifier l'expérience du développeur et minimiser la complexité, nous définissons intentionnellement le type de paramètre `data` dans la fonction generateHMAC comme `any`. En interne, nous gérons la conversion en une chaîne en utilisant `JSON.stringify`.

### Initialisation de la communication

Maintenant, du côté de Boost, créez un fichier `verification.controller.ts` sous `src/controllers` :

```ts
import { generateKeyPair, generateSharedSecret, generateHMAC, KeyPair } from '@boost/v1/utils/crypto.utils';
import { KeyObject, BinaryLike } from 'crypto';

const boostKeyPair: KeyPair = generateKeyPair();

export function shareKeys() {
    const boostPublicKey: Buffer = boostKeyPair.publicKey;
    const boostPrivateKey: Buffer = boostKeyPair.privateKey;
    const boostGenerator: Buffer = boostKeyPair.generator;
    const boostPrime: Buffer = boostKeyPair.prime;
    const boostDiffieHellman = boostKeyPair.diffieHellman;

    return {
        boostPublicKey,
        boostPrivateKey,
        boostGenerator,
        boostPrime,
        boostDiffieHellman,
    };
}

export function hmacDigest(data: any, secretKey: KeyObject | BinaryLike): any {
    return generateHMAC(JSON.stringify(data), secretKey);
}

```

Ce fichier importe l'interface et tous les modules nécessaires de `cryto.utils.ts` et définit deux fonctions d'enveloppement – `shareKeys` et `hmacDigest`. `shareKeys` ne servira que d'enveloppe autour de `generateKeyPair` qui permettra aux développeurs de Boost d'envoyer uniquement les clés requises à Account Aggregator.

### Configuration de l'Account Aggregator

À l'extrémité de l'Account Aggregator, nous devons configurer une fonction qui calcule la clé publique de l'AA et l'envoie à Boost Inc. Nous aurons également besoin d'une fonction pour vérifier le HMAC reçu d'une donnée en le comparant à celui que l'AA génère :

```ts
import { generateKeyPair, generateSharedSecret, generateHMAC, KeyPair } from '../utils/crypto.utils';  
import axios from 'axios';

let sharedSecret: Buffer;

export async function sendAAPublicKey(): Promise<Buffer> {
  try {
    const response = await axios.get('http://localhost:3000/init');

    const boostPublicKey: Buffer = Buffer.from(response.data.boostPublicKey, 'hex');
    const boostGenerator: Buffer = Buffer.from(response.data.boostGenerator, 'hex');
    const boostPrime: Buffer = Buffer.from(response.data.boostPrime, 'hex');

    const AA: KeyPair = generateKeyPair(boostPrime, boostGenerator);
    sharedSecret = generateSharedSecret(AA, boostPublicKey);

    return AA.publicKey;
  } catch (error) {
    console.error('Error sending AA public key:', (error as Error).message);
    throw error;
  }
}

export async function verifyData(data: any, hmac: string): Promise<string> {
  try {
    const calculatedHMAC = generateHMAC(JSON.stringify(data), sharedSecret);
    return calculatedHMAC === hmac ? "Integrity and authenticity verified" : "Integrity or authenticity compromised";
  } catch (error) {
    console.error('Error verifying data:', (error as Error).message);
    throw error;
  }
}

```

Nous faisons une requête Axios à l'endpoint `/init` défini chez Boost et récupérons \(p\), \(g\) et \(A\). Une fois que nous avons calculé la clé publique, nous la renvoyons à Boost. Nous calculerons également notre secret partagé ici, que nous utiliserons lors de la vérification du HMAC dans la méthode `verifyData`.

### Configuration des API Express

Maintenant que tous les contrôleurs et fonctions utilitaires sont en place, nous allons créer quelques endpoints pour faciliter la communication entre Boost Inc. et Account Aggregator.

#### Boost :

```ts
import express, { Request, Response } from 'express';
import { hmacDigest, shareKeys } from '@boost/v1/controllers/verification.controller';
import { KeyPair, generateSharedSecret } from '@boost/v1/utils/crypto.utils';
import { DiffieHellman } from 'crypto';
import axios from 'axios';

const appBoost = express();
const PORT_BOOST = 3000;

let boostPublicKey: Buffer, boostPrivateKey: Buffer;
let boostGenerator: Buffer, boostPrime: Buffer;
let sharedSecret: Buffer;
let boostKeyPair: KeyPair, boostDiffieHellman: DiffieHellman;

appBoost.get('/init', async (req: Request, res: Response) => {
    ({ boostPublicKey, boostPrivateKey, boostGenerator, boostPrime, boostDiffieHellman } = shareKeys());
    res.send({ boostPublicKey, boostGenerator, boostPrime });
});

// Simulated Data
const data = {
    name: 'Boost User 1',
    phone: '1234567890',
};

appBoost.get('/fetchData', async (req: Request, res: Response) => {
    const hmac = hmacDigest(data, sharedSecret);
    res.send({ data, hmac });
});

appBoost.listen(PORT_BOOST, () => {
  console.log(`Boost server is running on http://localhost:${PORT_BOOST}`);
});

```

L'endpoint `/init`, hébergé par Boost, est invoqué par AA dans sa fonction `sendAAPublicKey`. Lorsque le secret partagé est calculé, AA invoquera l'endpoint `/fetchData` pour récupérer les informations critiques.

#### Account Aggregator (AA) :

```ts
import express, { Request, Response } from 'express';
import { sendAAPublicKey, verifyData } from '@AA/v1/controllers/aa.controller';
import { KeyPair, generateSharedSecret } from '@boost/v1/utils/crypto.utils';
import { DiffieHellman } from 'crypto';
import axios from 'axios';

const appAA = express();
const PORT_AA = 3001;

let boostPublicKey: Buffer, boostPrivateKey: Buffer;
let boostGenerator: Buffer, boostPrime: Buffer;
let AAPublicKey: Buffer;
let sharedSecret: Buffer;
let boostKeyPair: KeyPair, boostDiffieHellman: DiffieHellman;

appAA.get('/fetchAAPublicKey', async (req: Request, res: Response) => {
    AAPublicKey = await sendAAPublicKey();
    res.send({ AAPublicKey: AAPublicKey.toString('hex') });

    boostKeyPair = {
        publicKey: boostPublicKey,
        privateKey: boostPrivateKey,
        generator: boostGenerator,
        prime: boostPrime,
        diffieHellman: boostDiffieHellman,
    }

    sharedSecret = generateSharedSecret(boostKeyPair, AAPublicKey);
});

appAA.get('/verifyData', async (req: Request, res: Response) => {
    const response = await axios.get('http://localhost:3000/fetchData');
    const { data, hmac } = response.data;
    const verified = await verifyData(data, hmac);
    res.send({ verified });
});

appAA.listen(PORT_AA, () => {
  console.log(`AA server is running on http://localhost:${PORT_AA}`);
});

```

L'endpoint `fetchAAPublicKey`, hébergé à l'extrémité de l'AA, sera invoqué par Boost lorsqu'il souhaite évaluer le secret partagé. La méthode `verifyData` est encapsulée dans une requête `GET`, permettant à l'une ou l'autre des parties de confirmer l'intégrité des données transmises.

## Appel des API

Rendez-vous sur votre client Postman pour tester ces API. Puisque la méthode `sendAAPublicKey` prend en charge l'initiation, nous devons démarrer notre communication en utilisant l'endpoint `/fetchAAPublicKey` :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/image-35.png)
_Client Postman : endpoint fetchAAPublicKey_

Vous observerez la clé publique de l'AA en réponse. Maintenant, Boost Inc. utilisera cette clé publique et évaluera le secret partagé.

Une fois cela fait, il utilisera le secret partagé pour calculer le digest du message dans l'endpoint `/fetchData`. Puisque `/verifyData` invoque l'endpoint précédent, nous vérifierons cela en action sur notre client Postman :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/image-36.png)
_Client Postman : endpoint verifyData_

Vous remarquerez que la réponse de `/verifyData` déclare la vérification réussie de l'intégrité et de l'authenticité. Cette reconnaissance garantit que les données transmises restent non altérées et proviennent de la source authentifiée, offrant une couche de sécurité pour la communication entre les deux entités.

## Conclusion

Et voilà : en utilisant les HMAC et l'échange de clés Diffie-Hellman-Merkle, vous pouvez vérifier l'intégrité et l'authenticité de vos données transmises, améliorant ainsi la sécurité de vos applications et assurant un cadre de communication API fiable pour les développeurs.

En comprenant les subtilités et les fondements mathématiques de ces pratiques, vous pouvez maintenant prendre des décisions éclairées, renforçant votre système contre les menaces de falsification.

Retrouvez les extraits de code complets ici — [GitHub Gist | HamdaanAliQuatil](https://gist.github.com/HamdaanAliQuatil/8e0942eddfe708aafd4f95b739802c0c).

Vous pouvez me trouver sur X (anciennement Twitter) — [Hamdaan Ali Quatil](https://twitter.com/violinblackeye).

### Références

[1] Behrouz A. Forouzan — Introduction à la cryptographie et à la sécurité des réseaux

[2] New Directions in Cryptography, Whitfield Diffie et Martin E. Hellman [diffie.hellman.pdf (jhu.edu)](https://www.cs.jhu.edu/~rubin/courses/sp03/papers/diffie.hellman.pdf)

[3] Keying Hash Functions for Message Authentication, Mihir Bellare, Ran Canetti, Hugo Krawczyk [https://cseweb.ucsd.edu/~mihir/papers/kmd5.pdf](https://cseweb.ucsd.edu/~mihir/papers/kmd5.pdf)