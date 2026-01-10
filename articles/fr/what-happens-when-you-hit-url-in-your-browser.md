---
title: Que se passe-t-il lorsque vous cliquez sur une URL dans votre navigateur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-30T08:06:27.000Z'
originalURL: https://freecodecamp.org/news/what-happens-when-you-hit-url-in-your-browser
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/browser.png
tags:
- name: Browsers
  slug: browsers
- name: dns
  slug: dns
- name: internet
  slug: internet
- name: url
  slug: url
- name: Web Development
  slug: web-development
seo_title: Que se passe-t-il lorsque vous cliquez sur une URL dans votre navigateur
seo_desc: 'By Anchal Nigam

  In this article, I want my readers to get a picture of a very basic concept of the
  web world. Previously, I''ve written articles on the fancy stuff of today’s market,
  i.e. Angular journey, basics of react, etc. But, today, I want my re...'
---

Par Anchal Nigam

Dans cet article, je souhaite que mes lecteurs comprennent un concept très basique du monde du web. Précédemment, j'ai écrit des articles sur les sujets à la mode du marché actuel, c'est-à-dire [Le voyage Angular](https://www.freecodecamp.org/news/angular-a-journey-into-one-of-the-most-popular-front-end-tools-in-todays-job-market/), [les bases de React](https://www.freecodecamp.org/news/start-your-journey-into-the-world-of-react-by-learning-these-basics-d6e05d3655e3/), etc. Mais aujourd'hui, je veux que mes lecteurs découvrent le voyage qu'ils rencontrent en premier lorsqu'ils saisissent une URL.

Comme le sujet est auto-explicatif - **que se passe-t-il lorsque nous saisissons une URL ?** - commençons !

Avant de discuter de **ce qui se passe après avoir saisi l'URL**, nous devons comprendre ce qu'est réellement une URL et ce que signifient les différentes parties de l'URL - n'est-ce pas ? Sans perdre de temps, comprenons mieux les URL.

## URL - Localisateur Uniforme de Ressources

Si vous regardez sa forme complète, alors c'est auto-explicatif : il contient l'emplacement des ressources que nous voulons accéder. C'est une **adresse du lieu** où nous voulons aller pour interagir ou trouver des informations.

Regardons votre vie quotidienne. Si vous voulez visiter la maison de votre ami pour du travail ou pour obtenir des informations, vous avez besoin de son adresse. La même chose s'applique ici dans ce grand monde du web : nous devons donner une adresse du site web que nous voulons accéder. Le **site web est comme la maison et l'URL est l'adresse.**

### Anatomie d'une URL

Maintenant, nous savons ce qu'est une URL mais nous ne connaissons toujours pas les parties d'une URL. Allons-y !

Prenons un exemple :

[https://www.example.com/page1](https://www.example.com/page1)

Ici, la première partie est **'https'**. Cela indique essentiellement au navigateur quel protocole il doit utiliser. Il peut s'agir de **http, https, ftp**, etc. Un **protocole** est un **ensemble de règles** que le navigateur utilise pour la communication sur le réseau. **'https'** est essentiellement une **version sécurisée**, c'est-à-dire que les informations sont échangées de manière sécurisée.

La deuxième partie **www.example.com** est un **nom de domaine**. Vous pouvez le relier à la maison de votre ami. C'est une adresse de site web. Nous l'utilisons pour atteindre le serveur (ordinateur formé) qui est responsable de servir les informations pour ce site web. Attendez ! Vous pourriez penser, il y a quelques secondes, j'ai mentionné que l'URL est l'adresse alors que j'ai également mentionné que le nom de domaine est aussi une adresse. Vous avez peut-être été confus. Ne soyez pas confus !

### Différence entre URL et Nom de Domaine

La différence majeure entre les deux est que **l'URL est une adresse complète**. L'URL indique la méthode par laquelle les informations doivent être échangées, le chemin après avoir atteint ce site web. Alors que le **nom de domaine fait partie d'une URL**.

Prenons notre exemple précédent pour mieux comprendre. Vous pouvez dire que l'adresse de la maison de votre ami est un nom de domaine, alors que l'URL ne donne pas seulement l'adresse de la maison de votre ami (nom de domaine) mais aussi comment vous allez communiquer, comme parler dans une pièce séparée (sécurisée) ou devant tout le monde (les informations peuvent fuir). Elle indique également le chemin, c'est-à-dire à quelle partie de la maison vous irez après être entré dans la maison. Par conséquent, le nom de domaine fait partie de l'URL. Un nom de domaine avec plus d'informations est une URL.

J'espère que maintenant vous êtes clair avec l'URL. Passons à la partie suivante.

## Nom de Domaine

Dans la partie précédente, j'ai expliqué les noms de domaine, mais pas en profondeur. Je veux que vous approfondissiez le sujet. Comme je vous l'ai dit, le nom de domaine est l'adresse du site web. Il donne une **identité unique** à votre **site web** dans ce grand monde du web. Aucun deux noms de domaine ne peuvent être identiques, MAIS - Oui ! Il y a un 'mais'. Ce n'est pas la seule définition d'un nom de domaine. Il y a une autre histoire derrière cela. Entrons dans cette histoire.

Comme nous le savons, lorsque nous saisissons une URL ou vous pouvez dire un nom de domaine, alors ce site web s'ouvre avec son contenu. Un serveur (un ordinateur formé) le sert. Nous savons également que chaque ordinateur a une adresse IP qui est utilisée pour la communication sur Internet. C'est une adresse comme son nom l'indique 'adresse IP'. Lorsque nous **saisissons** une **URL**, alors nous **saisissons** en réalité l'**adresse IP** de l'ordinateur qui est responsable de servir le contenu du site web (hébergement).

Mais maintenant, vous pourriez penser, qu'est-ce que... tout est une adresse ? Pourquoi ce nom de domaine existe-t-il si l'adresse IP est là ? Pourquoi ne pouvons-nous pas utiliser l'adresse IP pour obtenir le contenu du site web ?

Oui ! Vous pouvez **utiliser les adresses IP** pour **obtenir le contenu** du site web, mais vraiment !.. Pourriez-vous vous souvenir de l'adresse IP associée à chaque site web ? Évidemment non ! C'est **difficile** de **se souvenir de l'adresse IP** de chaque site web. C'est pourquoi les noms de domaine sont apparus sur le marché.

Vous pouvez le relier à votre liste de contacts. Vous ne pouvez pas vous souvenir du numéro de chaque personne, mais vous pouvez vous souvenir de leur nom. Le même concept s'applique ici également. Vous **ne pouvez pas vous souvenir** de ces **adresses IP effrayantes**, mais vous pouvez facilement **vous souvenir** des **noms de domaine**.

Cette énorme quantité de données est maintenue dans une base de données où le nom de domaine avec son adresse IP est stocké. Un système qui stocke les noms de domaine avec leur adresse IP correspondante est connu sous le nom de **DNS (Système de noms de domaine)** (je crois que vous devez en avoir entendu parler).

Je pense avoir discuté suffisamment des bases. Maintenant, plongeons profondément dans le processus lorsque nous saisissons une URL.

## Recherche DNS pour trouver l'adresse IP

Après avoir saisi l'URL, la première chose qui doit se produire est de résoudre l'adresse IP associée au nom de domaine. Le DNS aide à résoudre cela. **Le DNS est comme un annuaire téléphonique** et **nous aide à fournir l'adresse IP** qui est associée au nom de domaine, tout comme notre annuaire téléphonique donne un numéro de mobile qui est associé au nom de la personne.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/dns.png)

Ceci est un aperçu, mais il y a **quatre couches** par lesquelles cette requête de nom de domaine passe. Comprenons les étapes :

1. Après avoir saisi l'URL, le **cache du navigateur** est vérifié. Comme le navigateur maintient ses enregistrements DNS pendant un certain temps pour les sites web que vous avez visités précédemment. Par conséquent, tout d'abord, la requête DNS s'exécute ici pour trouver l'adresse IP associée au nom de domaine.

2. Le deuxième endroit où la requête DNS s'exécute est le **cache du système d'exploitation**, suivi du **cache du routeur**.

3. Si dans les étapes ci-dessus, une requête DNS n'est pas résolue, alors elle fait appel au serveur de résolution. Le serveur de résolution n'est rien d'autre que votre FAI (Fournisseur d'accès à Internet). La requête est envoyée au FAI où la requête DNS s'exécute dans le **cache du FAI**.

4. Si dans la 3ème étape, aucun résultat n'est trouvé, alors la requête est envoyée au **serveur racine ou supérieur** de la hiérarchie DNS. Il ne se produit jamais qu'il dise aucun résultat trouvé, mais en réalité, il indique d'où vous pouvez obtenir cette information. Si vous recherchez l'adresse IP du domaine de premier niveau (.com, .net, .Gov, .org). Il indique au serveur de résolution de rechercher le **serveur TLD** (Domaine de premier niveau).

5. Maintenant, le serveur de résolution demande au serveur TLD de donner l'adresse IP de notre nom de domaine. Le TLD stocke les informations d'adresse du nom de domaine. Il indique au serveur de résolution de demander au **serveur de noms faisant autorité**.

6. Le serveur de noms faisant autorité est responsable de tout savoir sur le nom de domaine. Enfin, le serveur de résolution (FAI) obtient l'adresse IP associée au nom de domaine et la renvoie au navigateur.

Après avoir obtenu une adresse IP, le serveur de résolution la stocke dans son cache afin que la prochaine fois, si la même requête arrive, il n'ait pas à passer par toutes ces étapes à nouveau. Il peut maintenant fournir l'adresse IP à partir de leur cache.

C'est tout sur les étapes qui sont suivies pour résoudre l'adresse IP qui est associée au nom de domaine. Jetez un coup d'œil ci-dessous pour mieux comprendre :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/dns_resolve.png)

## Le navigateur initie une connexion TCP avec le serveur

Une fois l'**adresse IP** de l'ordinateur (où se trouvent les informations de votre site web) **trouvée**, il **initie la connexion** avec celui-ci. Pour communiquer sur le réseau, le **protocole Internet** est suivi. **TCP/IP** est le protocole le plus courant. Une connexion est établie entre les deux en utilisant un processus appelé **'poignée de main TCP en 3 étapes'**. Comprenons le processus brièvement :

1. Un ordinateur client envoie un **message SYN**, ce qui signifie que le deuxième ordinateur est ouvert pour une nouvelle connexion ou non.

2. Ensuite, **un autre ordinateur**, s'il est ouvert pour une nouvelle connexion, envoie un **message d'accusé de réception** avec un message SYN également.

3. Après cela, le **premier ordinateur** reçoit son message et accuse réception en **envoyant** un **message ACK**.

Pour mieux comprendre, regardez le diagramme ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/process.png)

## La communication commence (Processus de requête-réponse)

Enfin, la connexion est établie entre le client et le serveur. Maintenant, ils peuvent tous deux communiquer entre eux et partager des informations. Après une connexion réussie, le **navigateur (client)** envoie une **requête** à un **serveur** pour obtenir ce contenu. Le serveur sait tout ce qu'il doit envoyer comme réponse pour chaque requête. Par conséquent, le **serveur répond**. Cette réponse contient toutes les informations que vous avez demandées, comme une page web, un code d'état, un contrôle de cache, etc. Maintenant, le navigateur rend le contenu qui a été demandé.

C'est tout ! Tout le processus ci-dessus se produit lorsque nous saisissons une URL. Bien que ce long processus prenne moins de secondes pour se compléter. C'est la réponse à votre question **'que se passe-t-il lorsque nous saisissons une URL dans un navigateur ?'**

Merci d'avoir lu !