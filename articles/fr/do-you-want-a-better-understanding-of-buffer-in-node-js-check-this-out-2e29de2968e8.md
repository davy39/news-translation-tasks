---
title: Vous voulez une meilleure compréhension de Buffer dans Node.js ? Découvrez
  cela.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-13T16:12:13.000Z'
originalURL: https://freecodecamp.org/news/do-you-want-a-better-understanding-of-buffer-in-node-js-check-this-out-2e29de2968e8
coverImage: https://cdn-media-1.freecodecamp.org/images/0*5WRoozR6-foMoED1.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Vous voulez une meilleure compréhension de Buffer dans Node.js ? Découvrez
  cela.
seo_desc: 'By Justice Mba

  Are you always mystified, like me, whenever you come across words like Buffer, Stream,
  and binary data in Node.js? Does that feeling make you shrink from understanding
  them, thinking they are not meant for you but only for Node.js guru...'
---

Par Justice Mba

Êtes-vous toujours mystifié, comme moi, chaque fois que vous rencontrez des mots comme **Buffer, Stream** et **données binaires** dans Node.js ? Ce sentiment vous donne-t-il envie de reculer pour les comprendre, en pensant qu'ils ne sont pas faits pour vous mais seulement pour les gourous de Node.js et les développeurs de packages ?

En effet, ces mots peuvent être très intimidants, surtout lorsque vous entrez dans le développement web avec Node.js sans aucun diplôme en informatique.

Malheureusement, de nombreux tutoriels et livres sauteront directement à l'enseignement du développement d'applications web avec des packages Node.js sans vous laisser comprendre les fonctionnalités principales de Node.js et pourquoi elles existent. Et certains vous diront effrontément que vous n'avez pas besoin de les comprendre parce que vous **ne travaillerez peut-être jamais** directement avec eux.

Eh bien, c'est vrai, vous ne travaillerez peut-être jamais directement avec eux si vous choisissez de rester un développeur Node.js moyen.

Cependant, si les mystères vous rendent vraiment curieux, et que vous ne reculez devant rien pour satisfaire votre curiosité, et si vous voulez porter votre compréhension de Node.js à un niveau supérieur, alors vous voulez vraiment creuser plus profondément pour comprendre les nombreuses fonctionnalités principales de Node.js, comme **Buffer**, par exemple. Et c'est exactement pourquoi j'écris cet article — pour nous aider à démystifier certaines de ces fonctionnalités et à porter notre apprentissage de Node.js à un niveau supérieur.

Lors de l'introduction de **Buffer**, [la documentation officielle de Node.js](https://nodejs.org/dist/latest-v8.x/docs/api/buffer.html#buffer_buffer) indique en partie...

> ... mécanisme pour lire ou manipuler des flux de données binaires. La classe `Buffer` a été introduite dans le cadre de l'API Node.js pour permettre d'interagir avec des flux d'octets dans le contexte de choses comme les flux TCP et les opérations du système de fichiers.

Hmmm, à moins que vous n'ayez eu des connaissances préalables sur tous les mots des phrases ci-dessus, ils sont probablement juste un tas de jargon. Essayons de simplifier cela un peu en le reformulant, afin que nous puissions avoir un objectif clair et ne pas être distraits par les nombreuses clochettes et sifflets qui s'y trouvent. En extrayant de cette introduction, nous pourrions dire en toute sécurité :

La classe `Buffer` a été introduite dans le cadre de l'API Node.js pour permettre de manipuler ou d'interagir avec des flux de données binaires.

Maintenant, c'est plus simple, n'est-ce pas ? Mais... Buffer, flux, données binaires... toujours beaucoup de grands mots. Eh bien, essayons de nous attaquer à ces grands mots du dernier au premier.

### Données binaires, qu'est-ce que c'est ?

Vous savez probablement déjà que les ordinateurs stockent et représentent les données en binaires. Le binaire est simplement un ensemble ou une collection de 1 et de 0. Par exemple, les éléments suivants sont cinq binaires différents, cinq ensembles différents de 1 et de 0 :

`10`, `01`, `001`, `1110`, `00101011`

Chaque nombre dans un binaire, chaque `1` et `0` dans un ensemble sont appelés un **Bit**, qui est une forme courte de **Binary digIT**.

Pour stocker ou représenter un morceau de données, un ordinateur doit convertir ces données en leur représentation binaire. Par exemple, pour stocker le nombre 12, un ordinateur doit convertir 12 en sa représentation binaire qui est `1100`.

Comment un ordinateur sait-il comment faire cette conversion ? Eh bien, c'est des mathématiques pures. C'est le simple système de numération binaire que nous avons appris en mathématiques de base — exprimer un nombre dans le système de numération en base-2. Les ordinateurs comprennent ces mathématiques.

Mais les nombres ne sont pas le seul type de données avec lequel nous travaillons. Nous avons aussi des chaînes de caractères, des images, et même des vidéos. Les ordinateurs savent comment représenter tous les types de données en binaires. Prenons les chaînes de caractères, par exemple. Comment un ordinateur représentera-t-il la chaîne "L" en binaires ? Pour stocker un caractère en binaires, les ordinateurs convertiront d'abord ce caractère en un nombre, puis convertiront ce nombre en sa représentation binaire. Donc pour la chaîne "L", les ordinateurs convertiront d'abord **L** en un nombre qui représente **L**. Voyons comment.

Ouvrez la console de votre navigateur et collez le code suivant, puis appuyez sur Entrée : `"L".charCodeAt(0)`. Qu'avez-vous vu ? Le nombre 76 ? C'est la représentation numérique ou **Code de Caractère** ou **Point de Code** du caractère **L**. Mais comment un ordinateur sait-il quel nombre exact représentera chaque caractère ? Comment sait-il utiliser le nombre 76 pour représenter **L** ?

#### **Jeux de Caractères**

Les jeux de caractères sont des règles déjà définies de quel nombre exact représente chaque caractère. Nous avons différentes définitions de ces règles. Les plus populaires incluent **Unicode** et **ASCII**. JavaScript fonctionne très bien avec les jeux de caractères Unicode. En fait, c'est l'Unicode dans votre navigateur qui indique que 76 devrait représenter **L**.

Nous avons donc vu comment les ordinateurs représentent les caractères en nombres. Maintenant, l'ordinateur représentera à son tour le nombre 76 en sa représentation binaire. Vous pourriez penser, eh bien, il suffit de convertir 76 en système de numération en base-2. Pas si vite !

#### **Encodage de Caractères**

Tout comme il existe des règles qui définissent quel nombre devrait représenter un caractère, il existe également des règles qui définissent **comment** ce nombre devrait être représenté en binaires. Plus précisément, **combien de bits** utiliser pour représenter le nombre. Cela s'appelle **Encodage de Caractères**.

L'une des définitions pour l'encodage de caractères est **UTF-8**. UTF-8 indique que les caractères doivent être encodés en **octets**. Un octet est un ensemble de huit bits — huit 1 et 0. Donc huit 1 et 0 doivent être utilisés pour représenter le Point de Code de n'importe quel caractère en binaire.

Pour comprendre cela, comme nous l'avons mentionné précédemment, la représentation binaire du nombre 12 est `1100`. Donc lorsque UTF-8 indique que 12 devrait être en huit bits, UTF-8 dit qu'un ordinateur doit ajouter plus de bits du côté gauche de la représentation réelle en base-2 du nombre 12 pour en faire un octet. Donc 12 devrait être stocké comme `00001100`. Cela a du sens ?

Par conséquent, 76 devrait être stocké comme `01001100`.

Cela, mes amis, est comment les ordinateurs stockent les chaînes de caractères ou les caractères en binaires. De même, les ordinateurs ont également des règles spécifiées sur la manière dont les images et les vidéos doivent être converties ou encodées et stockées en binaires. Le point ici est que les ordinateurs stockent tous les types de données en binaires, et cela est connu sous le nom de données binaires.

Si vous êtes super intéressé par les détails de l'encodage de caractères, vous pourriez aimer [cette introduction douce et détaillée](https://www.w3.org/International/questions/qa-what-is-encoding).

Maintenant que nous comprenons ce que sont les données binaires, mais qu'est-ce que les **flux de données binaires** de notre introduction au buffer ?

### Stream

Stream dans Node.js signifie simplement une séquence de données étant déplacée d'un point à un autre au fil du temps. Le concept entier est que vous avez une énorme quantité de données à traiter, mais vous n'avez pas besoin d'attendre que toutes les données soient disponibles avant de commencer à les traiter.

En gros, ces grandes données sont décomposées et envoyées par morceaux. Donc, à partir de la définition originale d'un buffer (« flux de données binaires... dans le contexte de... le système de fichiers »), cela signifie simplement des données binaires étant déplacées dans le système de fichiers. Par exemple, déplacer les textes stockés dans file1.txt vers file2.txt.

Mais comment exactement le buffer nous aide-t-il à interagir avec ou à manipuler les données binaires pendant le streaming ? Qu'est-ce que ce buffer au fait ?

### Buffer

Nous avons vu qu'un flux de données est le mouvement des données d'un point à un autre, mais comment **exactement** sont-elles déplacées ?

Typiquement, le mouvement des données se fait généralement avec l'intention de les traiter, ou de les lire, et de prendre des décisions basées sur celles-ci. Mais il y a un minimum et un maximum de données qu'un processus peut prendre au fil du temps. Donc si le taux auquel les données arrivent est plus rapide que le taux auquel le processus consomme les données, les données excédentaires doivent attendre quelque part pour leur tour d'être traitées.

D'autre part, si le processus consomme les données plus rapidement qu'elles n'arrivent, les quelques données qui arrivent plus tôt doivent attendre qu'une certaine quantité de données arrive avant d'être envoyées pour traitement.

Cette « zone d'attente » est le buffer ! C'est un petit emplacement physique dans votre ordinateur, généralement dans la RAM, où les données sont temporairement rassemblées, attendent, et sont finalement envoyées pour traitement pendant le streaming.

Nous pouvons penser à l'ensemble du processus de flux et de buffer comme à une station de bus. Dans certaines stations de bus, un bus n'est pas autorisé à partir avant qu'un certain nombre de passagers n'arrive ou avant une heure de départ spécifique. De plus, les passagers peuvent arriver à différents moments avec différentes vitesses. Ni les passagers ni la station de bus n'ont le contrôle sur l'arrivée des passagers à la station.

Dans tous les cas, les passagers qui arrivent plus tôt devront **attendre** jusqu'à ce que la station de bus décide d'envoyer le bus sur son chemin. Pendant ce temps, les passagers qui arrivent lorsque le bus est déjà en chargement ou lorsque le bus est déjà parti devront **attendre** le prochain bus.

Dans tous les cas, il y a toujours un lieu d'attente. C'est le **Buffer** pour Node.js ! Node.js ne peut pas contrôler la vitesse ou le temps d'arrivée des données, la vitesse du flux. Il ne peut décider que lorsque c'est le moment d'envoyer les données. Si ce n'est pas encore le moment, Node.js les mettra dans le buffer — la « zone d'attente » — un petit emplacement dans la RAM, jusqu'à ce que ce soit le moment de les envoyer pour traitement.

Un exemple typique où vous pourriez voir le buffer en action est lorsque vous diffusez une vidéo en ligne. Si votre connexion Internet est suffisamment rapide, la vitesse du flux sera suffisamment rapide pour remplir instantanément le buffer et l'envoyer pour traitement, puis en remplir un autre, et l'envoyer, puis un autre, et encore un autre... jusqu'à ce que le flux soit terminé.

Mais si votre connexion est lente, après avoir traité le premier ensemble de données arrivé, le lecteur vidéo affichera une icône de chargement, ou affichera le texte « buffering », ce qui signifie rassembler plus de données, ou attendre que plus de données arrivent. Et lorsque le buffer est rempli et traité, le lecteur montre les données, la vidéo. Pendant la lecture de celle-ci, plus de données continueront à arriver et à attendre dans le buffer.

Si le lecteur a terminé le traitement ou la lecture des données précédentes, et que le buffer n'est pas encore rempli, le texte « buffering » sera affiché à nouveau, en attendant de rassembler plus de données à traiter.

C'est ça **Buffer !**

À partir de la définition originale d'un buffer, il montre que pendant que les données sont dans le buffer, nous pouvons manipuler ou interagir avec les données binaires en cours de streaming. Quel type d'interaction pourrions-nous avoir avec ces données binaires brutes ? L'implémentation de Buffer dans Node.js nous fournit une liste complète de ce qui est réalisable. Voyons quelques-unes de ces interactions.

#### Interagir avec un Buffer

Il est même possible de créer votre propre buffer ! En plus de celui que Node.js créera automatiquement pendant un flux, il est possible de créer et de manipuler votre propre buffer. Intéressant, n'est-ce pas ? Créons-en un !

Selon ce que vous voulez réaliser, il existe différentes façons de créer un buffer. Voyons quelques-unes.

```
// Créer un buffer vide de taille 10. // Un buffer qui ne peut contenir que 10 octets.
```

```
const buf1 = Buffer.alloc(10);
```

```
// Créer un buffer avec du contenu
```

```
const buf2 = Buffer.from("hello buffer");
```

Une fois votre buffer créé, vous pouvez commencer à interagir avec lui

```
// Examiner la structure d'un buffer
```

```
buf1.toJSON()// { type: 'Buffer', data: [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] }// un buffer vide
```

```
buf2.toJSON()// { type: 'Buffer',     data: [        104, 101, 108, 108, 111, 32, 98, 117, 102, 102, 101, 114      ]    }
```

```
// la méthode toJSON() présente les données comme les Points de Code Unicode des caractères
```

```
// Examiner la taille d'un buffer
```

```
buf1.length // 10
```

```
buf2.length // 12. Assigné automatiquement en fonction du contenu initial lors de la création.
```

```
// Écrire dans un bufferbuf1.write("Buffer really rocks!") 
```

```
// Décoder un buffer
```

```
buf1.toString() // 'Buffer rea'
```

```
// oops, parce que buf1 est créé pour contenir seulement 10 octets, il n'a pas pu contenir le reste des caractères
```

```
// Comparer deux buffers
```

Il y a beaucoup d'interactions que nous pouvons avoir avec un buffer. Rendez-vous sur [la documentation officielle](https://nodejs.org/dist/latest-v8.x/docs/api/buffer.html) pour jouer avec ces méthodes.

Enfin, je vous laisse avec ce petit défi : Allez lire [la source de **zlib.js**](https://github.com/nodejs/node/blob/master/lib/zlib.js), l'une des bibliothèques principales de Node.js, pour voir comment elle utilise la puissance du buffer pour manipuler des flux de données binaires. Cela se révèle être des fichiers gzip. Pendant que vous lisez, documentez ce que vous apprenez et partagez-le avec nous ici dans les commentaires.

J'espère que cette introduction vous a aidé à mieux comprendre le Buffer de Node.js.

Si vous pensez que j'ai fait un bon travail, et que d'autres méritent une chance de voir cela, applaudissez pour l'article afin d'aider à répandre une meilleure compréhension du Buffer dans notre communauté Node.js.

Si vous avez une question qui n'a pas été répondue ou si vous avez une compréhension différente de certains des points ici, n'hésitez pas à laisser un commentaire ici ou via [Twitter](https://twitter.com/Daajust).