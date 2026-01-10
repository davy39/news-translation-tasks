---
title: HTTP Networking en JavaScript – Guide pour Débutants
subtitle: ''
author: Lane Wagner
co_authors: []
series: null
date: '2023-02-14T00:42:39.000Z'
originalURL: https://freecodecamp.org/news/http-full-course
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1738338854008/9272a213-f1ed-40d0-8d33-f57a11b3756c.png
tags:
- name: computer networking
  slug: computer-networking
- name: http
  slug: http
seo_title: HTTP Networking en JavaScript – Guide pour Débutants
seo_desc: 'HTTP is the backbone of the modern internet. In this text-based course,
  you''ll learn how the HTTP protocol works and how it''s used in real-world web development.

  All the code samples for this course are in JavaScript, but the networking concepts
  you''...'
---

HTTP est l'épine dorsale de l'internet moderne. Dans ce cours basé sur du texte, vous apprendrez comment le protocole HTTP fonctionne et comment il est utilisé dans le développement web réel.

Tous les exemples de code pour ce cours sont en JavaScript, mais les concepts de mise en réseau que vous apprendrez ici s'appliquent généralement à tous les langages de programmation. *Si vous n'êtes pas encore familier avec JavaScript, vous pouvez consulter* [*mon cours JS ici*](https://boot.dev/learn/learn-javascript)*.*

J'ai inclus tout le matériel d'apprentissage dont vous aurez besoin ici dans cet article, mais si vous souhaitez une expérience plus pratique, vous pouvez suivre la [version interactive de ce cours avec des défis de codage sur Boot.dev ici.](https://boot.dev/learn/learn-http)

J'ai également publié une version vidéo gratuite de ce cours sur la chaîne YouTube freeCodeCamp :

%[https://www.youtube.com/watch?v=2JYT5f2isg4] 

Si vous aimez cette vidéo, vous pouvez consulter mes autres tutoriels sur ma [chaîne YouTube Boot.dev ici](https://youtube.com/@bootdotdev).

Tout cela dit, plongeons dans l'apprentissage de HTTP !

## **Table des Matières**

1. [Pourquoi HTTP ?](#heading-pourquoi-http)
    
2. [Qu'est-ce que le DNS ?](#quest-ce-que-le-dns)
    
3. [Que sont les URIs ?](#heading-que-sont-les-uris)
    
4. [Async/Await](#chapter-4-async-await)
    
5. [Gestion des Erreurs](#heading-gestion-des-erreurs)
    
6. [En-têtes HTTP](#heading-en-tetes-http)
    
7. [Qu'est-ce que JSON ?](#heading-quest-ce-que-json)
    
8. [Méthodes HTTP](#chapter-8-methodes-http)
    
9. [Chemins et Paramètres d'URL](#heading-chemins-et-parametres-durl)
    
10. [Qu'est-ce que HTTPS ?](#heading-quest-ce-que-https)
    

## Pourquoi HTTP ?

### Communiquer sur le web

Instagram serait assez terrible si vous deviez copier manuellement vos photos sur le téléphone de votre ami lorsque vous souhaitez les partager. Les applications modernes doivent pouvoir communiquer des informations *entre appareils* via l'internet.

* Gmail ne stocke pas simplement vos e-mails dans des variables sur votre ordinateur, il les stocke sur des ordinateurs dans leurs centres de données.
    
* Vous ne perdez pas vos messages Slack si vous faites tomber votre ordinateur dans un lac – ces messages existent sur les [serveurs](https://en.wikipedia.org/wiki/Web_server) de Slack.
    

### Comment fonctionne la communication web ?

Lorsque deux ordinateurs communiquent entre eux, ils doivent utiliser les mêmes règles. Un anglophone ne peut pas communiquer verbalement avec un japonais, et de même, deux ordinateurs doivent parler la même langue pour communiquer.

Ce "langage" que les ordinateurs utilisent est appelé un [protocole](https://en.wikipedia.org/wiki/Communication_protocol). Le protocole le plus populaire pour la communication web est [HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview), qui signifie Hypertext Transfer Protocol.

### Interagir avec un serveur

Dans ce cours, beaucoup des exemples de code interagiront avec le [PokeAPI](https://pokeapi.co/). Il fournit des données sur les Pokémon.

Voici un code qui récupère une liste de Pokémon depuis le PokeAPI :

```javascript
const pokemonResp = await getItemData()

logPokemons(pokemonResp.results)

async function getItemData() {
  const response = await fetch('https://pokeapi.co/api/v2/pokemon/', {
    method: 'GET',
    mode: 'cors',
    headers: {
      'Content-Type': 'application/json'
    }
  })
  return response.json()
}

function logPokemons(pokemons) {
  for (const pokemon of pokemons) {
    console.log(pokemon.name)
  } 
}
```

Lorsque vous exécutez ce code, vous remarquerez que aucune des données enregistrées dans la console n'a été générée dans notre code ! C'est parce que les données que nous avons récupérées sont envoyées via l'internet depuis nos serveurs via HTTP. Ne vous inquiétez pas, nous expliquerons plus en détail cela plus tard.

### Requêtes et Réponses HTTP

Au cœur de HTTP se trouve un simple système de requête-réponse. L'ordinateur "demandeur", également connu sous le nom de "[client](https://en.wikipedia.org/wiki/Client_\(computing\))", demande à un autre ordinateur certaines informations. Cet ordinateur, le "[serveur](https://en.wikipedia.org/wiki/Server_\(computing\))", envoie une réponse avec les informations demandées.

![Image](https://i.imgur.com/ReFw6nN.png align="left")

Nous parlerons des spécificités de la manière dont les "requêtes" et les "réponses" sont formatées plus tard. Pour l'instant, pensez simplement à cela comme un simple système de questions-réponses.

* Requête : "Quels sont les objets dans le jeu Fantasy Quest ?"
    
* Réponse : Une liste des objets dans le jeu Fantasy Quest
    

### HTTP alimente les sites web

Comme nous l'avons discuté, [HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview), ou Hypertext Transfer Protocol, est un [protocole](https://developer.mozilla.org/en-US/docs/Glossary/Protocol) conçu pour transférer des informations entre ordinateurs.

Il existe d'autres protocoles pour communiquer via l'internet, mais HTTP est le plus populaire et est *particulièrement adapté aux sites web et aux applications web*.

Chaque fois que vous visitez un site web, votre navigateur envoie une requête HTTP au serveur de ce site web. Le serveur répond avec tout le texte, les images et les informations de style dont votre navigateur a besoin pour rendre son joli site web.

![Image](https://i.imgur.com/EflKJzq.jpg align="left")

### URL HTTP

Une URL, ou [Uniform Resource Locator](https://www.freecodecamp.org/news/url-definition/), est essentiellement l'adresse d'un autre ordinateur, ou "serveur" sur l'internet. Une partie de l'URL spécifie comment atteindre le serveur, et une autre partie indique au serveur quelles informations nous voulons - mais nous en parlerons plus tard.

Pour l'instant, il est important de comprendre qu'une URL représente une pièce d'information sur un autre ordinateur à laquelle nous voulons accéder. Nous pouvons y accéder en faisant une *requête*, et en lisant la *réponse* que le serveur renvoie.

### Comment utiliser les URL en HTTP

Le `http://` au début d'une [URL de site web](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_URL) spécifie que le protocole `http` sera utilisé pour la communication.

![Image](https://i.imgur.com/6jiaXBn.png align="left")

D'autres protocoles de communication utilisent également des URL (d'où "Uniform Resource Locator"). C'est pourquoi nous devons être spécifiques lorsque nous faisons des requêtes HTTP en préférant l'URL avec `http://`

### Révision des Requêtes et Réponses

* Un "client" est un ordinateur faisant une requête HTTP
    
* Un "serveur" est un ordinateur répondant à une requête HTTP
    
* Un ordinateur peut être un client, un serveur, les deux, ou aucun des deux. "Client" et "serveur" sont simplement des mots que nous utilisons pour décrire ce que font les ordinateurs dans un système de communication.
    
* Les clients envoient des requêtes et reçoivent des réponses
    
* Les serveurs reçoivent des requêtes et envoient des réponses
    

## L'API Fetch de JavaScript

Dans ce cours, nous utiliserons l'API [fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) intégrée de JavaScript pour faire des requêtes HTTP.

La fonction `fetch()` est mise à notre disposition par le langage JavaScript s'exécutant dans le navigateur. Tout ce que nous avons à faire est de lui fournir les paramètres dont elle a besoin.

### **Comment Utiliser Fetch**

```javascript
const response = await fetch(url, settings)
const responseData = await response.json()
```

Nous approfondirons les différentes choses qui se passent dans cet appel `fetch` standard plus tard, mais couvrons quelques bases pour l'instant.

* `response` est la donnée qui revient du serveur
    
* `url` est l'URL à laquelle nous faisons une requête
    
* `settings` est un objet contenant certains paramètres spécifiques à la requête
    
* Le mot-clé `await` indique à JavaScript d'attendre que la requête revienne du serveur avant de continuer
    
* `response.json()` convertit les données de réponse du serveur en un objet JavaScript
    

Voyez si vous pouvez repérer le problème avec cet extrait de code :

```javascript
const pokemonResp = getItemData()

logPokemons(pokemonResp.results)

// le bug est au-dessus de cette ligne

async function getItemData() {
  const response = await fetch('https://pokeapi.co/api/v2/pokemon/', {
    method: 'GET',
    mode: 'cors',
    headers: {
      'Content-Type': 'application/json'
    }
  })
  return response.json()
}

function logPokemons(pokemons) {
  for (const pokemon of pokemons) {
    console.log(pokemon.name)
  } 
}
```

Indice : Nous n'attendons pas que les données soient renvoyées à travers le réseau.

### Clients Web

Un client web est un appareil faisant des requêtes à un serveur web. Un client peut être n'importe quel type d'appareil mais est souvent quelque chose avec lequel les utilisateurs interagissent physiquement. Par exemple :

* Un ordinateur de bureau
    
* Un téléphone mobile
    
* Une tablette
    

Dans un site web ou une application web, nous appelons l'appareil de l'utilisateur le "front-end".  
Un client front-end fait des requêtes à un serveur back-end.

![Image](https://i.imgur.com/zldXGet.jpg align="left")

### Serveurs Web

Jusqu'à présent, la plupart des données avec lesquelles vous avez travaillé dans votre code ont simplement été générées et stockées localement dans des variables.

Bien que vous utilisiez toujours des variables pour stocker et manipuler des données pendant l'exécution de votre programme, la plupart des sites web et applications utilisent un serveur web pour stocker, trier et servir ces données afin qu'elles persistent plus longtemps qu'une seule session et puissent être accessibles par plusieurs appareils.

### **Écouter et servir des données**

De manière similaire à un serveur dans un restaurant qui apporte votre nourriture à la table, un [serveur web](https://en.wikipedia.org/wiki/Web_server)) sert des ressources web, telles que des pages web, des images et d'autres données. Le serveur est allumé et "écoute" constamment les requêtes entrantes afin que, dès qu'il reçoit une nouvelle requête, il puisse envoyer une réponse appropriée.

### Le serveur est le back-end

Alors que le "front-end" d'un site web ou d'une application web est l'appareil avec lequel l'utilisateur interagit, le "back-end" est le serveur qui conserve toutes les données dans un emplacement central. Si vous êtes encore confus, [consultez cet article comparant le développement front-end et back-end](https://blog.boot.dev/backend/frontend-vs-backend-meaning/).

### Un serveur est juste un ordinateur

"Serveur" est simplement le nom que nous donnons à un ordinateur qui joue le rôle de servir des données à travers une connexion réseau.

Un bon serveur est allumé et disponible 24 heures sur 24, 7 jours sur 7. Bien que votre ordinateur portable *puisse* être utilisé comme serveur, il est plus logique d'utiliser un ordinateur dans un centre de données conçu pour être opérationnel en permanence.

## Qu'est-ce que le DNS ?

### Adresses Web

Dans le monde réel, nous utilisons des adresses pour nous aider à trouver où vit un ami, où se trouve une entreprise, ou où une fête est organisée.

En informatique, les clients web trouvent d'autres ordinateurs sur l'internet en utilisant des adresses de [Protocole Internet ou IP](https://en.wikipedia.org/wiki/Internet_Protocol).

Une adresse IP est une étiquette numérique qui sert deux fonctions principales :

1. Adressage de localisation
    
2. Identification du réseau
    

### Noms de domaine et adresses IP

Chaque appareil connecté à l'internet possède une adresse IP unique. Lorsque nous naviguons sur l'internet, les domaines que nous visitons sont tous associés à une adresse IP particulière.

Par exemple, cette URL Wikipedia pointe vers une page sur les mini-pigs : `https://en.wikipedia.org/wiki/Miniature_pig`  
La partie [domaine](https://en.wikipedia.org/wiki/Domain_Name_System) de l'URL est `en.wikipedia.org`. `en.wikipedia.org` se convertit en une adresse IP spécifique, et cette adresse IP indique à votre ordinateur exactement où communiquer avec cette page Wikipedia.

Cloudflare est une entreprise technologique qui fournit un serveur HTTP public que nous pouvons utiliser pour rechercher l'adresse IP de n'importe quel domaine. Jetez un coup d'œil à ce code exemple :

```javascript
async function fetchIPAddress(domain) {
  const resp = await fetch(`https://cloudflare-dns.com/dns-query?name=${domain}&type=A`, {
    headers: {
      'accept': 'application/dns-json'
    }
  })
  const respObject = await resp.json()
  for (const record of respObject.Answer) {
    return record.data
  }
  return null
}

const domain = 'api.boot.dev'
const ipAddress = await fetchIPAddress(domain)
if (!ipAddress) {
  console.log('quelque chose a mal tourné dans fetchIPAddress')
} else {
  console.log(`adresse IP trouvée pour le domaine ${domain}: ${ipAddress}`)
}
```

Pour résumer, un "nom de domaine" fait partie d'une URL. C'est la partie qui indique à l'ordinateur *où se trouve le serveur sur l'internet* en étant converti en une adresse IP numérique.

Nous verrons exactement comment une adresse IP est utilisée par votre ordinateur pour trouver un chemin vers le serveur dans un cours de mise en réseau ultérieur. Pour l'instant, il est simplement important de comprendre qu'une adresse IP est ce que votre ordinateur utilise à un niveau inférieur pour communiquer sur un réseau.

Déployer un vrai site web sur l'internet est en réalité assez simple. Cela implique seulement quelques étapes :

1. Créer un serveur qui héberge les fichiers de votre site web et le connecter à l'internet
    
2. Acquérir un nom de domaine
    
3. Connecter le nom de domaine à l'adresse IP de votre serveur
    
4. Votre serveur est accessible via l'internet !
    

![Image](https://i.imgur.com/vjjPt2a.png align="left")

Comme nous l'avons discuté, le "nom de domaine" ou "nom d'hôte" fait partie d'une URL. Nous aborderons les autres parties d'une URL plus tard.

Par exemple, l'URL `https://example.com/path` a un nom d'hôte de `example.com`. Les parties `https://` et `/path` ne font pas partie de la correspondance `nom de domaine -> adresse IP` que nous avons apprise.

### Utilisation de l'API URL en JavaScript

L'API `URL` est intégrée à JavaScript. Vous pouvez créer un [nouvel objet URL](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) comme ceci :

```js
const urlObj = new URL('https://example.com/example-path')
```

Et ensuite vous pouvez [extraire simplement le nom d'hôte](https://developer.mozilla.org/en-US/docs/Web/API/URL) :

```js
const urlObj.hostname
```

### Révision du DNS

Nous avons donc parlé des noms de domaine et de leur utilité, mais nous n'avons pas parlé du système utilisé pour effectuer cette conversion.

Le [DNS](https://www.freecodecamp.org/news/what-is-dns/), ou "Système de Noms de Domaine", est l'annuaire téléphonique de l'internet. Les humains se connectent aux sites web via des [noms de domaine](https://en.wikipedia.org/wiki/Domain_name), comme [Boot.dev](https://boot.dev).

Le DNS "résout" ces noms de domaine pour trouver les [adresses IP](https://en.wikipedia.org/wiki/Internet_Protocol) associées afin que les clients web puissent charger les ressources pour l'adresse spécifique.

![Image](https://i.imgur.com/yvfSbVL.png align="left")

### Comment fonctionne le DNS ?

Nous entrerons dans plus de détails sur le DNS dans un cours futur, mais pour vous donner une idée simplifiée de son fonctionnement, introduisons l'ICANN. [ICANN](https://www.icann.org/) est une organisation à but non lucratif qui gère le DNS pour l'ensemble de l'internet.

Chaque fois que votre ordinateur tente de résoudre un nom de domaine, il contacte l'un des "[serveurs de noms racine](https://en.wikipedia.org/wiki/Root_name_server)" de l'ICANN dont l'adresse est incluse dans la configuration réseau de votre ordinateur.

À partir de là, ce serveur de noms peut recueillir les enregistrements de domaine pour un nom de domaine spécifique à partir de leur base de données DNS distribuée.

Si vous considérez le DNS comme un annuaire téléphonique, l'ICANN est l'éditeur qui maintient l'annuaire imprimé et disponible.

### Sous-domaines

Nous avons appris comment un nom de domaine se résout en une adresse IP, qui n'est qu'un ordinateur sur un réseau - souvent l'internet.

Un sous-domaine préfixe un nom de domaine, permettant à un domaine de router le trafic réseau vers de nombreux serveurs et ressources différents.

Par exemple, le site web [Boot.dev](https://boot.dev) est hébergé sur un ordinateur différent de notre blog. Notre blog, trouvé à [blog.boot.dev](https://blog.boot.dev) est hébergé sur notre sous-domaine "blog".

## Que sont les URIs ?

Nous avons brièvement abordé les URL plus tôt, mais maintenant plongeons un peu plus profondément dans le sujet.

Un [URI](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier), ou Uniform Resource *Identifier*, est une séquence de caractères unique qui identifie une ressource qui est (presque toujours) accessible via l'internet.

Tout comme JavaScript a des règles de syntaxe, les URIs en ont aussi. Ces règles aident à assurer l'uniformité afin que tout programme puisse interpréter le sens de l'URI de la même manière.

Les URIs se présentent en deux types principaux :

* [URLs](https://en.wikipedia.org/wiki/URL)
    
* [URNs](https://en.wikipedia.org/wiki/Uniform_Resource_Name)
    

Nous nous concentrerons spécifiquement sur les URLs dans ce cours, mais il est important de savoir que les URLs ne sont qu'un type d'URI.

![Image](https://i.imgur.com/VzqzckC.png align="left")

Les URLs ont plusieurs sections, certaines étant obligatoires, d'autres non.  
Utilisons l'[API URL](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) pour analyser une URL et imprimer toutes les différentes parties. Nous en apprendrons plus sur chaque partie plus tard, pour l'instant, divisons et imprimons une URL.

```js
function printURLParts(urlString) {
  const urlObj = new URL(urlString)
  console.log(`protocol: ${urlObj.protocol}`)
  console.log(`username: ${urlObj.username}`)
  console.log(`password: ${urlObj.password}`)
  console.log(`hostname: ${urlObj.hostname}`)
  console.log(`port: ${urlObj.port}`)
  console.log(`pathname: ${urlObj.pathname}`)
  console.log(`search: ${urlObj.search}`)
  console.log(`hash: ${urlObj.hash}`)
}

const fantasyQuestURL = 'http://dragonslayer:pwn3d@fantasyquest.com:8080/maps?sort=rank#id'
printURLParts(fantasyQuestURL)
```

### Dissection d'une URL

Il y a 8 parties principales à une URL, bien que toutes les sections ne soient pas toujours présentes. Chaque partie joue un rôle spécifique pour aider les clients à localiser la ressource spécifiée.  
Les 8 sections sont :

![Image](https://i.imgur.com/iI3sUVh.png align="left")

* Le protocole est obligatoire
    
* Les noms d'utilisateur et mots de passe sont optionnels
    
* Un domaine est obligatoire
    
* Le port par défaut pour un protocole donné est utilisé si aucun n'est fourni
    
* Le chemin par défaut ( `/` ) est utilisé si aucun n'est fourni
    
* Une requête est optionnelle
    
* Un fragment est optionnel
    

### Ne vous attardez pas trop sur la mémorisation de ces choses

Parce que les noms des différentes sections sont souvent utilisés de manière interchangeable, et parce que toutes les parties de l'URL ne sont pas toujours présentes, il peut être difficile de garder les choses claires.

Ne vous inquiétez pas de mémoriser ces choses ! Essayez simplement de vous familiariser avec ces concepts d'URL à un niveau élevé. Comme tout bon développeur, vous pouvez simplement chercher à nouveau la prochaine fois que vous aurez besoin d'en savoir plus.

### Le Protocole

Le "protocole", également appelé "schéma", est le premier composant d'une URL. Son but est de définir les règles selon lesquelles les données communiquées sont affichées, encodées ou formatées.

Quelques exemples de différents protocoles d'URL :

* http
    
* ftp
    
* mailto
    
* https
    

Par exemple :

* `http://example.com`
    
* `mailto:noreply@fantasyquest.app`
    

### Tous les schémas ne nécessitent pas "//"

Le "http" dans une URL est toujours suivi de `://`. Toutes les URL ont le deux-points, mais la partie `//` n'est incluse que pour les schémas qui ont un [composant d'autorité](https://www.rfc-editor.org/rfc/rfc3986#section-3.2).

Comme vous pouvez le voir ci-dessus, le schéma `mailto` n'utilise pas de composant d'autorité, donc il n'a pas besoin des barres obliques.

### Ports d'URL

Le port dans une URL est un point virtuel où les connexions réseau sont établies. Les ports sont gérés par le système d'exploitation d'un ordinateur et sont numérotés de `0` à `65,535`.

Chaque fois que vous vous connectez à un autre ordinateur via un réseau, vous vous connectez à un port spécifique sur cet ordinateur, qui est écouté par un logiciel spécifique sur cet ordinateur. Un port ne peut être utilisé que par un seul programme à la fois, c'est pourquoi il existe tant de ports possibles.

Le composant port d'une URL n'est souvent pas visible lors de la navigation sur des sites normaux sur l'internet, car 99 % du temps vous utilisez les ports par défaut pour les schémas HTTP et HTTPS : `80` et `443`, respectivement.

Chaque fois que vous n'utilisez pas un port par défaut, vous devez le spécifier dans l'URL. Par exemple, le port `8080` est souvent utilisé par les développeurs web lorsqu'ils exécutent leur serveur en "mode test" afin qu'ils n'utilisent pas le port "production" "80".

![Image](https://i.imgur.com/h3kBsRC.png align="left")

### Chemins d'URL

Dans les premiers jours de l'internet, le chemin d'une URL était souvent un reflet du chemin de fichier sur le serveur vers la ressource que le client demandait.

Par exemple, si le site web `https://exampleblog.com` avait un serveur web s'exécutant dans son répertoire `/home`, alors une requête à l'URL `https://exampleblog.com/site/index.html` pourrait s'attendre à ce que le fichier `index.html` du répertoire `/home/site` soit retourné.

Les sites web étaient très simples. Ils n'étaient qu'une collection de documents texte stockés sur un serveur. Un simple logiciel de serveur pouvait gérer les requêtes HTTP entrantes et répondre avec les documents selon le composant de chemin des URL.

### De nos jours, ce n'est pas toujours une question de système de fichiers

Sur de nombreux serveurs web modernes, le chemin d'une URL n'est pas un reflet de la hiérarchie du système de fichiers du serveur. Les chemins dans les URL sont essentiellement juste un autre type de paramètre qui peut être passé au serveur lors de l'envoi d'une requête.

Conventionnellement, deux chemins d'URL différents devraient désigner des ressources différentes. Par exemple, différentes pages sur un site web, ou peut-être différents types de données d'un serveur de jeu.

### Paramètres de requête

Les paramètres de requête dans une URL ne sont *pas* toujours présents. Dans le contexte des sites web, les paramètres de requête sont souvent utilisés pour l'analyse marketing ou pour changer une variable sur la page web. Avec les URL de sites web, les paramètres de requête *changent rarement* *laquelle* page vous consultez, bien qu'ils changent souvent le *contenu* de la page.

Cela dit, les paramètres de requête peuvent être utilisés pour tout ce que le serveur choisit de les utiliser, tout comme le chemin de l'URL.

### Comment Google utilise les paramètres de requête

1. Ouvrez un nouvel onglet et allez sur [google.com](https://google.com)
    
2. Recherchez "hello world"
    
3. Jetez un coup d'œil à votre URL actuelle. Elle devrait commencer par `https://www.google.com/search?q=hello+world`
    
4. Changez l'URL pour dire `https://www.google.com/search?q=hello+universe`
    
5. Appuyez sur "entrée"
    

Vous devriez voir de nouveaux résultats de recherche pour la requête "hello universe". Google a choisi d'utiliser des paramètres de requête pour représenter la valeur de votre requête de recherche. Cela a du sens - chaque page de résultats de recherche est *essentiellement* la même page en ce qui concerne la structure et la mise en forme - elle vous montre simplement différents résultats en fonction de la requête de recherche.

## Async/Await

Vous êtes probablement déjà familier avec le code [synchrone](https://developer.mozilla.org/en-US/docs/Glossary/Synchronous), ce qui signifie un code qui *s'exécute en séquence*. Chaque ligne de code s'exécute dans l'ordre, l'une après l'autre.

![Image](https://i.imgur.com/03FFGu0.png align="left")

Exemple de code synchrone :

```js
console.log("Je m'imprime en premier");
console.log("Je m'imprime en second");
console.log("Je m'imprime en troisième");
```

Le code asynchrone ou [async](https://developer.mozilla.org/en-US/docs/Glossary/Asynchronous) s'exécute en *parallèle*. Cela signifie que le code plus bas s'exécute *en même temps qu'*une ligne de code précédente est encore en cours d'exécution. Une bonne façon de visualiser cela est avec la fonction JavaScript [setTimeout()](https://developer.mozilla.org/en-US/docs/Web/API/setTimeout).

`setTimeout` accepte une fonction et un nombre de millisecondes en entrée. Il attend que le nombre de millisecondes se soit écoulé, puis il exécute la fonction qui lui a été donnée.

Exemple de code asynchrone :

```js
jsconsole.log("Je m'imprime en premier");
setTimeout(() => console.log("Je m'imprime en troisième car j'attends 100 millisecondes"), 100);
console.log("Je m'imprime en second");
```

Essayez de modifier les temps d'attente dans le code asynchrone ci-dessous pour obtenir les messages dans le bon ordre :

```js
const craftingCompleteWait = 0
const combiningMaterialsWait = 0
const smeltingIronBarsWait = 0
const shapingIronWait = 0

// Ne touchez pas en dessous de cette ligne

setTimeout(() => console.log('Épée longue en fer complète !'), craftingCompleteWait)
setTimeout(() => console.log('Combinaison des matériaux...'), combiningMaterialsWait)
setTimeout(() => console.log('Fonte des barres de fer...'), smeltingIronBarsWait)
setTimeout(() => console.log('Façonnage du fer...'), shapingIronWait)

console.log('Allumage de la forge...')

await sleep(2500)
function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms))
}
```

Ordre attendu :

1. Allumage de la forge...
    
2. Fonte des barres de fer...
    
3. Combinaison des matériaux...
    
4. Façonnage du fer...
    
5. Épée longue en fer complète !
    

### Pourquoi voulons-nous du code asynchrone ?

Nous essayons de garder la plupart de notre code synchrone car il est plus facile à comprendre, et donc souvent moins sujet aux bugs. Mais parfois nous *avons besoin* que notre code soit asynchrone.

Par exemple, chaque fois que vous mettez à jour vos paramètres utilisateur sur un site web, votre navigateur devra communiquer ces nouveaux paramètres au serveur. Le temps nécessaire à votre requête HTTP pour voyager physiquement à travers tout le câblage de l'internet est généralement d'environ 100 millisecondes. Ce serait une très mauvaise expérience si votre page web devait geler en attendant que la requête réseau se termine. Vous ne pourriez même pas bouger la souris en attendant !

En rendant les requêtes réseau *asynchrones*, nous permettons à la page web d'exécuter d'autres codes tout en attendant que la réponse HTTP revienne. Cela maintient l'expérience utilisateur réactive et conviviale.

En règle générale, nous ne devrions utiliser le code asynchrone que lorsque nous en avons besoin pour des raisons de performance. Le code synchrone est plus simple.

![Image](https://i.imgur.com/03FFGu0.png align="left")

### Promesses en JavaScript

Une Promesse en JavaScript est très similaire à faire une promesse dans le monde réel. Lorsque nous faisons une promesse, nous prenons un engagement envers quelque chose.

Par exemple, *je promets de vous expliquer les promesses JavaScript*. Ma promesse à vous a 2 issues potentielles : elle est soit tenue, ce qui signifie que je vous ai finalement expliqué les promesses, soit elle est rompue, ce qui signifie que j'ai échoué à tenir ma promesse et ne vous ai pas expliqué les promesses.

L'[objet Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) représente l'accomplissement ou le rejet éventuel de notre promesse et contient les valeurs résultantes. En attendant, pendant que nous attendons que la promesse soit tenue, notre code continue de s'exécuter.

Les promesses sont la méthode moderne la plus populaire pour écrire du code asynchrone en JavaScript.

### Comment déclarer une promesse

Voici un exemple de promesse qui se résoudra et retournera la chaîne "résolue !" ou sera rejetée et retournera la chaîne "rejetée !" après 1 seconde.

```plaintext
const promise = new Promise((resolve, reject) => {
  setTimeout(() => {
    if (getRandomBool()) {
      resolve("résolue !")
    } else {
      reject("rejetée !")
    }
  }, 1000)
})

function getRandomBool(){
  return Math.random() < .5
}
```

### Comment utiliser une promesse

Maintenant que nous avons créé une promesse, comment l'utiliser ?

L'objet `Promise` dispose de [.then](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then) et [.catch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/catch) qui facilitent son utilisation. Pensez à `.then` comme à la *suite attendue* d'une promesse, et à `.catch` comme à la suite "quelque chose a mal tourné".

Si une promesse *se résout*, sa fonction `.then` s'exécutera. Si la promesse est rejetée, sa méthode `.catch` s'exécutera.

Voici un exemple d'utilisation de `.then` et `.catch` avec la promesse que nous avons créée ci-dessus :

```js
promise.then((message) => {
    console.log(`La promesse est enfin ${message}`)
}).catch((message) => {
    console.log(`La promesse est enfin ${message}`)
})

// imprime :
// La promesse est enfin résolue !
// ou
// la promesse est enfin rejetée !
```

### Pourquoi les promesses sont-elles utiles ?

Les promesses sont le moyen le plus propre (mais pas le seul) de gérer le scénario courant où nous devons faire des requêtes à un serveur, ce qui est généralement fait via une requête HTTP. En fait, la fonction [fetch()](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) que nous utilisions plus tôt dans le cours retourne une promesse !

### E/S, ou "entrée/sortie"

Presque chaque fois que vous utilisez une promesse en JavaScript, ce sera pour gérer une forme d'E/S. E/S, ou entrée/sortie, fait référence au moment où notre code doit interagir avec des systèmes en dehors du monde (relativement) simple des variables locales et des fonctions.  
Exemples courants d'E/S :

* Requêtes HTTP
    
* Lecture de fichiers depuis le disque dur
    
* Interaction avec un appareil Bluetooth
    

Les promesses nous aident à effectuer des E/S sans forcer l'ensemble de notre programme à geler en attendant une réponse.

### Promesses et le mot-clé "await"

Nous avons utilisé le mot-clé [await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await) à quelques reprises dans ce cours, il est donc temps de comprendre enfin ce qui se passe sous le capot.

Le mot-clé `await` est utilisé pour *attendre* qu'une promesse se résolve. Une fois qu'elle a été résolue, l'expression `await` retourne la valeur de la promesse `Promise` résolue.

### Exemple avec le rappel .then

```js
promise.then((message) => {
  console.log(`Résolue avec ${message}`)
}).
```

### Exemple d'attente d'une promesse

```js
const message = await promise
console.log(`Résolue avec ${message}`)
```

### Le mot-clé async

Alors que le mot-clé `await` peut être utilisé à la place de `.then()` pour *résoudre* une promesse, le mot-clé [async](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function) peut être utilisé à la place de [new promise()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise) pour *créer* une nouvelle promesse.

Lorsque une fonction est précédée du mot-clé `async`, elle *renverra automatiquement* une promesse. Cette promesse se résout avec la valeur que votre code renvoie depuis la fonction. Vous pouvez penser à `async` comme "enveloppant" votre fonction dans une promesse.

Ces exemples sont équivalents :

### New Promise()

```js
function getPromiseForUserData(){
  return new Promise((resolve) => {
    fetchDataFromServerAsync().then(function(user){
      resolve(user)
    })
  })
}

const promise = getPromiseForUserData()
```

### Async

```js
async function getPromiseForUserData(){
  const user = await fetchDataFromServer()
  return user
}

const promise = getPromiseForUserData()
```

### .then() vs await

Dans les premiers jours des navigateurs web, les promesses et le mot-clé `await` n'existaient pas, donc la seule façon de faire quelque chose de manière asynchrone était d'utiliser des rappels.

Une "fonction de rappel" est une fonction que vous passez à une autre fonction. Cette fonction appelle ensuite votre rappel plus tard. La fonction [setTimeout](https://developer.mozilla.org/en-US/docs/Web/API/setTimeout) que nous avons utilisée par le passé est un bon exemple.

```js
function callbackFunction(){
  console.log("appel en retour maintenant !")
}
const milliseconds = 1000
setTimeout(callbackFunction, milliseconds)
```

Bien que même la syntaxe `.then()` soit généralement plus facile à utiliser que les rappels sans l'API `Promise`, la syntaxe `await` les rend encore plus faciles à utiliser. Vous devriez utiliser `async` et `await` plutôt que `.then` et [new Promise()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise) comme règle générale.

Pour démontrer, lequel de ceux-ci est le plus facile à comprendre ?

```js
fetchUser.then(function(user){
  return fetchLocationForUser(user)
}).then(function(location){
  return fetchServerForLocation(location)
}).then(function(server){
  console.log(`Le serveur est ${server}`)
});
```

```js
const user = await fetchUser()
const location = await fetchLocationForUser(user)
const server = await fetchServerForLocation(location)
console.log(`Le serveur est ${server}`)
```

Ils font tous les deux la même chose, mais le deuxième exemple est tellement plus facile à comprendre ! Les mots-clés `async` et `await` n'ont été publiés que *après* l'API `.then`, ce qui explique pourquoi il reste encore beaucoup de code `.then()` hérité.

## Gestion des Erreurs

Lorsque quelque chose ne va pas pendant l'exécution d'un programme, JavaScript utilise le paradigme `try/catch` pour gérer ces erreurs. Try/catch est assez courant, et [Python](https://boot.dev/learn/learn-python) utilise un mécanisme similaire.

### D'abord, une erreur est levée

Par exemple, supposons que nous essayons d'accéder à une propriété sur une variable non définie. JavaScript lèvera automatiquement une erreur.

```js
const speed = car.speed
// Le code plante avec l'erreur suivante :
// "ReferenceError: car is not defined"
```

### Essayer et attraper les erreurs

En enveloppant ce code dans un bloc try/catch, nous pouvons gérer le cas où `car` n'est pas encore défini.

```js
try {
  const speed = car.speed
} catch (err) {
  console.log(`Une erreur a été levée : ${err}`)
  // le code enregistre proprement :
  // "Une erreur a été levée : ReferenceError: car is not defined"
}
```

### Bugs vs Erreurs

La gestion des erreurs via try/catch n'est pas la même chose que le débogage. De même, les erreurs ne sont pas les mêmes que les bugs.

* Un bon code sans bugs peut encore produire des erreurs qui sont gérées avec élégance
    
* Les bugs sont, par définition, des morceaux de code qui ne fonctionnent pas comme prévu
    

### Qu'est-ce que le Débogage ?

"Déboguer" un programme est le processus de parcourir votre code pour trouver où il ne se comporte pas comme prévu. Le débogage est un processus manuel effectué par le développeur.

Exemples de débogage :

* Ajouter un paramètre manquant à un appel de fonction
    
* Mettre à jour une URL cassée qu'une requête HTTP essayait d'atteindre
    
* Corriger un composant de sélection de date dans une application qui ne s'affichait pas correctement
    

### Qu'est-ce que la Gestion des Erreurs ?

La "gestion des erreurs" est un code qui peut gérer les *cas limites attendus* dans votre programme. La gestion des erreurs est un processus automatisé que nous concevons dans notre code de production pour le protéger contre des choses comme les connexions internet faibles, les mauvaises entrées utilisateur, ou les bugs dans le code des autres avec lesquels nous devons interagir.

Exemples de gestion des erreurs :

* Utiliser un bloc try/catch pour détecter un problème avec l'entrée utilisateur
    
* Utiliser un bloc try/catch pour échouer proprement lorsqu'aucune connexion internet n'est disponible
    

### En bref, n'utilisez pas try/catch pour essayer de gérer les bugs

Si votre code contient un [bug](https://en.wikipedia.org/wiki/Software_bug), try/catch ne vous aidera pas. Vous devez simplement trouver le bug et le corriger.

Si quelque chose hors de votre contrôle peut produire des problèmes dans votre code, vous devriez utiliser try/catch ou une autre logique de gestion des erreurs pour le gérer.

Par exemple, il pourrait y avoir une invite dans un jeu pour que les utilisateurs tapent un nouveau nom de personnage, mais nous ne voulons pas qu'ils utilisent de ponctuation. Valider leur entrée et afficher un message d'erreur si quelque chose ne va pas serait une forme de "gestion des erreurs".

### async/await facilite la gestion des erreurs

`try` et `catch` sont les moyens standard de gérer les erreurs en JavaScript, le problème est que l'API Promise originale avec `.then` ne nous permettait pas d'utiliser les blocs `try` et `catch`.

Heureusement, les mots-clés `async` et `await` *le permettent* - une raison de plus de préférer la nouvelle syntaxe.

### Rappel .catch() sur les promesses

La méthode [.catch()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/catch) fonctionne de manière similaire à la méthode .then(), mais elle se déclenche lorsqu'une promesse est *rejetée* au lieu d'être résolue.

### Exemple avec les rappels .then et .catch

```js
fetchUser().then(function(user){
  console.log(`utilisateur récupéré : ${user}`)
}).catch(function(err){
  console.log(`une erreur a été levée : ${err}`)
});
```

### Exemple d'attente d'une promesse

```js
try {
  const user = await fetchUser()
  console.log(`utilisateur récupéré : ${user}`)
} catch (err) {
  console.log(`une erreur a été levée : ${err}`)
}
```

Comme vous pouvez le voir, la version `async/await` ressemble exactement au `try/catch` JavaScript normal.

## En-têtes HTTP

Un [en-tête HTTP](https://developer.mozilla.org/en-US/docs/Glossary/HTTP_header) permet aux clients et aux serveurs de transmettre des informations *supplémentaires* avec chaque requête ou réponse. Les en-têtes sont simplement des paires [clé-valeur](https://en.wikipedia.org/wiki/Name%E2%80%93value_pair) insensibles à la casse qui transmettent des [métadonnées](https://en.wikipedia.org/wiki/Metadata) supplémentaires sur la requête ou la réponse.

Les requêtes HTTP d'un navigateur web transportent avec elles de nombreux en-têtes, notamment mais pas uniquement :

* Le type de client (par exemple Google Chrome)
    
* Le système d'exploitation (par exemple Windows)
    
* La langue préférée (par exemple l'anglais américain)
    

En tant que développeurs, nous pouvons également définir des en-têtes personnalisés dans chaque requête.

### API des En-têtes

L'API [Headers](https://developer.mozilla.org/en-US/docs/Web/API/Headers) nous permet d'effectuer diverses actions sur nos en-têtes de requête et de réponse, telles que la récupération, la définition et la suppression. Nous pouvons accéder à l'objet headers via les propriétés `Request.headers` et `Response.headers`.

### Comment Utiliser les Outils de Développement du Navigateur

Les navigateurs web modernes offrent aux développeurs un ensemble puissant d'*outils de développement*. Les [Outils de Développement](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools) sont le meilleur ami d'un développeur front-end. Par exemple, en utilisant les outils de développement, vous pouvez :

* Voir la sortie de la console JavaScript de la page web
    
* Inspecter le code HTML, CSS et JavaScript de la page
    
* Voir les requêtes et réponses réseau, ainsi que leurs en-têtes
    

La méthode pour accéder aux outils de développement varie d'un navigateur à l'autre. Si vous êtes sur Chrome, vous pouvez simplement faire un clic droit n'importe où dans une page web et cliquer sur l'option "inspecter". Suivez ce lien pour plus d'informations sur [comment accéder aux outils de développement](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools#:~:text=How%20do%20you%20pull%20it%20up%3F%20Three%20ways%3A).

### L'onglet réseau

Bien que tous les onglets des outils de développement soient très utiles, nous nous concentrerons spécifiquement sur l'*onglet Réseau* dans ce chapitre afin que nous puissions jouer avec les en-têtes HTTP.

L'onglet Réseau surveille l'activité réseau de votre navigateur et enregistre toutes les requêtes et réponses que le navigateur effectue, y compris le temps que prennent chacune de ces requêtes et réponses pour être entièrement traitées.

Si vous naviguez vers l'onglet Réseau et ne voyez aucune requête apparaître, essayez de rafraîchir la page.

![Image](https://i.imgur.com/STKdceG.png align="left")

### Pourquoi les en-têtes sont-ils utiles ?

Les en-têtes sont utiles pour plusieurs raisons, allant de la conception à la sécurité. Mais le plus souvent, les en-têtes sont utilisés comme [métadonnées](https://en.wikipedia.org/wiki/Metadata) ou données *sur* la requête.

Ainsi, par exemple, supposons que nous voulions demander le niveau d'un joueur depuis le serveur d'un jeu. Nous devons envoyer l'ID de ce joueur au serveur afin qu'il sache pour quel joueur renvoyer les informations. Cet ID *est ma requête*, ce n'est pas une information *sur ma requête*.

Un bon exemple d'un cas d'utilisation pour les en-têtes est l'[authentification](https://auth0.com/intro-to-iam/what-is-authentication/). Souvent, les identifiants d'un utilisateur sont inclus dans les en-têtes de requête. Les identifiants n'ont pas grand-chose à voir avec la requête *elle-même*, mais autorisent simplement le demandeur à être autorisé à faire la requête en question.

## Qu'est-ce que JSON ?

La notation d'objet JavaScript, ou [JSON](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON), est un standard pour représenter des données *structurées* basé sur la syntaxe des objets JavaScript.

JSON est couramment utilisé pour transmettre des données dans les applications web en utilisant HTTP. Les requêtes HTTP `fetch()` que nous avons utilisées dans ce cours ont retourné des données sous forme de données JSON.

### Syntaxe JSON

Puisque nous comprenons déjà à quoi ressemblent les objets JavaScript, comprendre JSON est facile. JSON est simplement un objet JavaScript converti en chaîne de caractères. Ce qui suit est une donnée JSON valide :

```json
{
    "films": [
        {
            "id": 1,
            "genre": "Action",
            "titre": "Iron Man",
            "réalisateur": "Jon Favreau"
        },
        {
            "id": 2,
            "genre": "Action",
            "titre": "The Avengers",
            "réalisateur": "Joss Whedon"
        }
    ]
}
```

### Comment analyser les réponses HTTP en JSON

JavaScript nous fournit des outils faciles pour nous aider à travailler avec JSON. Après avoir fait une requête HTTP avec l'[API fetch()](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API), nous obtenons un [objet Response](https://developer.mozilla.org/en-US/docs/Web/API/Response). Cet objet response nous offre des méthodes qui nous aident à interagir avec la réponse.

Une telle méthode est la méthode [.json()](https://developer.mozilla.org/en-US/docs/Web/API/Response/json). La méthode `.json()` prend le flux de réponse retourné par une requête fetch et retourne une [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) qui se résout en un objet JavaScript analysé à partir du corps JSON de la réponse HTTP.

```js
const resp = await fetch(...)
const javascriptObjectResponse = await resp.json()
```

Il est important de noter que le résultat de la méthode `.json()` *N'EST PAS* du JSON. Il s'agit du résultat de la prise de données JSON à partir du corps de la réponse HTTP et de l'analyse de cette entrée en un objet JavaScript.

### Révision JSON

JSON est une *représentation sous forme de chaîne* d'un objet JavaScript, ce qui le rend parfait pour l'enregistrer dans un fichier ou l'envoyer dans une requête HTTP.

Rappelez-vous, un objet JavaScript réel est quelque chose qui n'existe que dans les variables de votre programme. Si nous voulons envoyer un objet en dehors de notre programme, par exemple, à travers l'internet dans une requête HTTP, nous devons d'abord le convertir en JSON.

### Ce n'est pas seulement utilisé en JavaScript

Le fait que JSON s'appelle *JavaScript* Object Notation ne signifie pas qu'il n'est utilisé que par JavaScript ! JSON est un standard commun qui est reconnu et pris en charge par tous les principaux langages de programmation.

Par exemple, même si l'API backend de Boot.dev est écrite en [Go](https://boot.dev/learn/learn-golang), nous utilisons toujours [JSON](https://blog.boot.dev/golang/json-golang/) comme format de communication entre le front-end et le backend.

Au fait, ce cours a porté sur l'interaction avec des serveurs backend depuis une perspective front-end. Mais si vous êtes curieux de savoir comment vous pouvez devenir un ingénieur backend, [consultez ce guide](https://blog.boot.dev/backend/become-backend-developer/) que j'ai préparé. Pour référence, il faut généralement aux gens [entre 6 et 18 mois](https://blog.boot.dev/backend/how-long-to-become-backend-dev/) pour apprendre suffisamment pour obtenir leur premier [emploi backend](https://blog.boot.dev/backend/backend-job-description/).

### Cas d'utilisation courants de JSON

* Dans les corps de requêtes et de réponses HTTP
    
* En tant que formats pour les fichiers texte. Les fichiers `.json` sont souvent utilisés comme fichiers de configuration.
    
* Dans les bases de données NoSQL comme MongoDB, ElasticSearch et Firestore
    

### Comment prononcer JSON

Je le prononce "Jay-sawn", mais j'ai aussi entendu des gens le prononcer "Jason", comme le prénom.

### Comment envoyer du JSON

JSON n'est pas seulement quelque chose que nous recevons du serveur, nous pouvons aussi *envoyer* des données JSON.  
En JavaScript, deux des principales méthodes auxquelles nous avons accès sont [JSON.parse()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse), et [JSON.stringify()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify).

#### `JSON.stringify()`

`JSON.stringify()` est particulièrement utile pour *envoyer* du JSON.

Comme vous pouvez vous y attendre, la méthode JSON `stringify()` fait l'inverse de parse. Elle prend un objet ou une valeur JavaScript en entrée et le convertit en une chaîne. Cela est utile lorsque nous devons séquentialiser les objets en chaînes pour les envoyer à notre serveur ou les stocker dans une base de données.

Voici un extrait de code qui envoie une charge utile JSON à un serveur distant :

```plaintext
async function sendPayload(data, headers) {
  const response = await fetch(url, {
    method: 'POST',
    mode: 'cors',
    headers: headers,
    body: JSON.stringify(data)
  })
  return response.json()
}
```

### Comment analyser JSON

La méthode [JSON.parse()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse) prend une chaîne JSON en entrée et construit la valeur/objet JavaScript décrit par la chaîne. Cela nous permet de travailler avec le JSON comme un objet JavaScript normal.

Étant donné que les objets JSON ont une structure arborescente, il peut être utile de savoir comment les [parcourir de manière récursive](https://blog.boot.dev/javascript/how-to-recursively-traverse-objects/) si nécessaire.

```js
const json = '{"title": "Avengers Endgame", "Rating":4.7, "inTheaters":false}';
const obj = JSON.parse(json)

console.log(obj.title)
// Avengers Endgame
```

### XML

Nous ne pouvons pas parler de JSON sans mentionner [XML](https://en.wikipedia.org/wiki/XML#:~:text=Extensible%20Markup%20Language%20\(XML\)%20is,%2Dreadable%20and%20machine%2Dreadable.). Extensible Markup Language, ou `XML`, est un format basé sur du texte pour représenter des informations structurées, tout comme JSON - il a juste une apparence un peu différente.

XML est un langage de balisage comme [HTML](https://en.wikipedia.org/wiki/HTML), mais il est plus généralisé en ce sens qu'il n'utilise *pas* de balises prédéfinies. Tout comme dans un objet JSON, les clés peuvent être appelées n'importe quoi, les balises XML peuvent également avoir n'importe quel nom.

```xml
<root>
  <id>1</id>
  <genre>Action</genre>
  <title>Iron Man</title>
  <director>Jon Favreau</director>
</root>
```

Les mêmes données au format JSON :

```json
{
  "id": "1",
  "genre": "Action",
  "title": "Iron Man",
  "director": "Jon Favreau"
}
```

### Pourquoi utiliser XML ?

XML et JSON accomplissent des tâches similaires, alors lequel devriez-vous utiliser ?

XML était utilisé pour les mêmes choses que JSON est utilisé aujourd'hui. Les fichiers de configuration, les corps HTTP et autres cas d'utilisation de transfert de données peuvent fonctionner aussi bien avec JSON qu'avec XML. Voici mon conseil : en général, si JSON fonctionne, vous devriez le préférer à XML de nos jours. JSON est plus léger, plus facile à lire et a un meilleur support dans la plupart des langages de programmation modernes.

Il existe certains cas où XML pourrait encore être le meilleur choix, voire même le choix nécessaire, mais ces cas seront rares.

## Méthodes HTTP

HTTP définit un ensemble de [méthodes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) que nous utilisons chaque fois que nous faisons une requête. Nous avons utilisé certaines de ces méthodes dans les exercices précédents, mais il est temps de les approfondir et de comprendre les différences et les cas d'utilisation derrière les différentes méthodes.

### La méthode GET

La [méthode GET](https://www.freecodecamp.org/news/javascript-get-request-tutorial/) est utilisée pour "obtenir" une représentation d'une ressource spécifiée. Vous ne prenez pas les données du serveur, mais plutôt obtenez une représentation, ou copie, de la ressource dans son état actuel.

Une requête get est considérée comme une [méthode](https://developer.mozilla.org/en-US/docs/Glossary/Safe/HTTP) sûre à appeler plusieurs fois car elle ne modifie pas l'état du serveur.

### Comment faire une requête GET en utilisant l'API Fetch

La méthode fetch() accepte un objet `init` optionnel en tant que deuxième argument que nous pouvons utiliser pour définir des choses comme :

* `method` : La méthode HTTP de la requête, comme `GET`.
    
* `headers` : Les en-têtes à envoyer.
    
* `mode` : Utilisé pour la sécurité, nous en parlerons dans les cours futurs
    
* `body` : Le corps de la requête. Souvent encodé en JSON.
    

Exemple de requête `GET` utilisant fetch :

```js
await fetch(url, {
  method: 'GET',
  mode: 'cors',
  headers: {
    'sec-ch-ua-platform': 'macOS'
  }
})
```

### Pourquoi utilisons-nous les méthodes HTTP ?

Comme nous l'avons mentionné précédemment, le but principal des méthodes HTTP est d'indiquer au serveur ce que nous voulons faire avec la ressource avec laquelle nous essayons d'interagir.

À la fin de la journée, une méthode HTTP n'est qu'une chaîne de caractères, comme `GET`, `POST`, `PUT`, ou `DELETE`. Mais par *convention*, les développeurs backend écrivent presque toujours leur code serveur de sorte que les méthodes correspondent à différentes actions "CRUD".

Les actions "CRUD" sont :

* Créer
    
* Lire
    
* Mettre à jour
    
* Supprimer
    

La majeure partie de la logique dans la plupart des applications web est la logique "CRUD". L'interface web permet aux utilisateurs de créer, lire, mettre à jour et supprimer diverses ressources.

Pensez à un site de réseau social - les utilisateurs créent, lisent, mettent à jour et suppriment essentiellement leurs publications sociales. Ils créent, lisent, mettent à jour et suppriment également leurs comptes utilisateur. C'est du CRUD tout du long !

Il se trouve que les 4 méthodes HTTP les plus courantes correspondent bien aux actions CRUD :

* `POST` = créer
    
* `GET` = lire
    
* `PUT` = mettre à jour
    
* `DELETE` = supprimer
    

### Requêtes POST

Une [requête HTTP POST](https://www.freecodecamp.org/news/javascript-post-request-how-to-send-an-http-post-request-in-js/) envoie des données à un serveur, généralement pour créer une nouvelle ressource. Le `body` de la requête est la *charge utile* qui est envoyée au serveur avec la requête. Son type est indiqué par l'en-tête `Content-Type`.

### Comment ajouter un `body`

Le `body` de la requête est la *charge utile* qui est envoyée au serveur avec la requête. Son type est indiqué par l'en-tête `Content-Type` - pour nous, ce sera du JSON.

Les requêtes `POST` ne sont généralement *pas* des méthodes sûres à appeler plusieurs fois, car elles modifient l'état du serveur. Vous ne voudriez pas créer accidentellement 2 comptes pour le même utilisateur, par exemple.

```js
await fetch(url, {
  method: 'POST',
  mode: 'cors',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(data)
})
```

### Codes de Statut HTTP

Maintenant que nous comprenons comment écrire des requêtes HTTP à partir de zéro, nous devons apprendre comment nous assurer que le serveur fait ce que nous voulons.

Plus tôt dans le cours, nous avons appris comment accéder aux *outils de développement* du navigateur et utiliser ces outils pour inspecter les requêtes HTTP. Nous pouvons utiliser ce même processus pour vérifier les requêtes que nous faisons et vérifier ce qu'elles font afin de pouvoir résoudre les problèmes potentiels.

Lors de l'examen des requêtes, nous pouvons vérifier le `Code de Statut` de la requête pour obtenir des informations si la requête a réussi ou non.

* `100-199` : Réponses d'information. Elles sont très rares.
    
* `200-299` : Réponses réussies. Espérons que la plupart des réponses sont des 200 !
    
* `300-399` : Messages de redirection. Ceux-ci sont généralement invisibles car le navigateur ou le client HTTP effectuera automatiquement la redirection.
    
* `400-499` : Erreurs client. Vous verrez souvent celles-ci, surtout lorsque vous essayez de déboguer une application client
    
* `500-599` : Erreurs serveur. Vous verrez parfois celles-ci, généralement seulement s'il y a un bug sur le serveur.
    

Voici quelques-uns des codes de statut les plus courants, mais vous pouvez voir une [liste complète ici](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) si vous êtes intéressé.

* `200` - OK. C'est de loin le code le plus courant, il signifie simplement que tout a fonctionné comme prévu.
    
* `201` - Créé. Cela signifie qu'une ressource a été créée avec succès. Typiquement en réponse à une requête `POST`.
    
* `301` - Déplacé de manière permanente. Cela signifie que la ressource a été déplacée vers un nouvel emplacement, et la réponse inclura où se trouve cet nouvel emplacement. Les sites web utilisent souvent des redirections `301` lorsqu'ils changent leur nom de domaine, par exemple.
    
* `400` - Mauvaise requête. Une erreur générale indiquant que le client a fait une erreur dans sa requête.
    
* `403` - Non autorisé. Cela signifie que le client n'a pas les permissions correctes. Peut-être qu'il n'a pas inclus un en-tête d'autorisation requis, par exemple.
    
* `404` - Non trouvé. Vous verrez cela sur les sites web assez souvent. Cela signifie simplement que la ressource n'existe pas.
    
* `500` - Erreur interne du serveur. Cela signifie que quelque chose a mal tourné sur le serveur, probablement un bug de leur côté.
    

### Vous n'avez pas besoin de les mémoriser

Vous devez connaître les bases, comme "2XX est bon", "4XX est une erreur client", et "5XX est une erreur serveur". Cela dit, vous n'avez pas besoin de mémoriser tous les codes, ils sont faciles à rechercher.

![Image](https://i.imgur.com/FJl2z9O.jpg align="left")

Vérifions quelques codes de statut !

La propriété `.status` sur un objet Response vous donnera le code. Voici un exemple :

```js
async function getStatusCode(url, headers) {
  const response = await fetch(url, {
    method: 'GET',
    mode: 'cors',
    headers: headers
  })
  return response.status
}
```

### Méthode PUT

La [méthode HTTP PUT](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PUT) crée une nouvelle ressource ou remplace une représentation de la ressource cible par le contenu du `body` de la requête. En bref, elle met à jour les propriétés d'une ressource.

```js
await fetch(url, {
   method: 'PUT',
   mode: 'cors',
   headers: {
   'Content-Type': 'application/json'
   },
   body: JSON.stringify(data)
})
```

### POST vs PUT

Vous pensez peut-être que `PUT` est similaire à `POST` ou `PATCH`, et franchement, vous auriez raison. La principale différence est que PUT est censé être [idempotent](https://developer.mozilla.org/en-US/docs/Glossary/Idempotent), ce qui signifie que plusieurs requêtes PUT identiques devraient avoir le même effet sur le serveur.

En revanche, plusieurs requêtes `POST` identiques auraient des effets secondaires supplémentaires, comme la création de plusieurs copies de la ressource.

### HTTP Patch vs PUT

Vous pouvez rencontrer des méthodes [PATCH](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PATCH) de temps en temps. Bien qu'elle ne soit pas aussi courante que les autres méthodes, comme `PUT`, il est important de la connaître et de savoir ce qu'elle fait. La méthode `PATCH` est destinée à modifier *partiellement* une ressource.

En bref, `PATCH` n'est pas aussi populaire que `PUT`, et de nombreux serveurs, même s'ils permettent des mises à jour partielles, utiliseront toujours la méthode `PUT` pour cela.

### HTTP Delete

La méthode `DELETE` fait exactement ce à quoi vous vous attendez : elle est conventionnellement utilisée pour supprimer une ressource spécifiée.

```js
// Cela supprime l'emplacement avec l'ID : 52fdfc07-2182-454f-963f-5f0f9a621d72
const url = 'https://example-api.com/locations/52fdfc07-2182-454f-963f-5f0f9a621d72'

await fetch(url, {
  method: 'DELETE',
  mode: 'cors'
})
```

## Chemins et Paramètres d'URL

Le chemin d'URL vient juste après le domaine (ou le port si un est fourni) dans une chaîne d'URL.

Dans cette URL, le chemin est `/root/next` : `http://testdomain.com/root/next`.

### Ce que les chemins signifiaient au début de l'internet

Dans les premiers jours de l'internet, et parfois encore aujourd'hui, de nombreux serveurs web servaient simplement des fichiers bruts à partir du système de fichiers du serveur.

Par exemple, si je voulais que vous puissiez accéder à certains documents texte, je pourrais démarrer un serveur web dans mon répertoire `documents`. Si vous faisiez une requête à mon serveur, vous pourriez accéder à différents documents en utilisant le chemin qui correspondait à ma structure de fichiers locale.

Si j'avais un fichier dans mon répertoire local `/documents/hello.txt`, vous pourriez y accéder en faisant une requête `GET` à `http://example.com/documents/hello.txt`.

### Comment les chemins sont utilisés aujourd'hui

La plupart des serveurs web modernes n'utilisent pas cette simple correspondance de `chemin d'URL` -> `chemin de fichier`. Techniquement, un chemin d'URL est simplement une chaîne de caractères que le serveur web peut utiliser comme il le souhaite, et les sites web modernes tirent parti de cette flexibilité.

Quelques exemples courants de ce à quoi servent les chemins :

* La hiérarchie des pages sur un site web, que cela reflète ou non la structure de fichiers d'un serveur
    
* Les paramètres passés dans une requête HTTP, comme un ID de ressource
    
* La version de l'API
    
* Le type de ressource demandé
    

### APIs RESTful

[Representational State Transfer, ou REST](https://developer.mozilla.org/en-US/docs/Glossary/REST), est une convention populaire que les serveurs HTTP suivent. Toutes les APIs HTTP ne sont pas des "APIs REST", ou "RESTful", mais c'est *très* courant.

Les serveurs RESTful suivent un ensemble de règles qui facilitent la création d'APIs web fiables et prévisibles. REST est plus ou moins un ensemble de conventions sur la manière dont HTTP *devrait* être utilisé.

### Séparé et agnostique

La grande idée derrière REST est que les ressources sont transférées via des interactions client/serveur bien reconnues et indépendantes du langage.

Un style RESTful signifie que l'implémentation du client et du serveur peut être faite indépendamment l'une de l'autre, tant que certaines normes simples, comme les noms des ressources disponibles, ont été établies.

### Sans état

Une architecture RESTful est sans état. Cela signifie que le serveur n'a pas besoin de connaître l'état dans lequel se trouve le client, ni le client n'a besoin de connaître l'état dans lequel se trouve le serveur.

L'absence d'état dans REST est renforcée en interagissant avec des ressources plutôt qu'avec des commandes. Gardez à l'esprit que cela ne signifie pas que les applications sont sans état - au contraire, que signifierait "mettre à jour une ressource" si le serveur ne suivait pas son état ?

### Chemins dans REST

Dans une API RESTful, la dernière section du `path` d'une URL doit spécifier quelle ressource est accessible. Ensuite, comme nous en avons parlé dans la section "méthodes", selon que la requête est un `GET`, `POST`, `PUT` ou `DELETE`, la ressource est lue, créée, mise à jour ou supprimée.

Par exemple, dans le [PokeAPI](https://pokeapi.co/) :

* [`https://pokeapi.co/api/v2/pokemon/`](https://pokeapi.co/api/v2/pokemon/)
    
* [`https://pokeapi.co/api/v2/location/`](https://pokeapi.co/api/v2/pokemon/)
    

La première partie du chemin spécifie que nous interagissons avec une API plutôt qu'avec un site web. La partie suivante spécifie la version, dans ce cas, la version 2, ou `v2`.

Enfin, la dernière partie indique quelle ressource est accessible, qu'il s'agisse d'un `location` ou `pokemon`.

### Paramètres de Requête d'URL

Les paramètres de requête d'une URL apparaissent ensuite dans la structure de l'URL mais ne sont *pas* toujours présents - ils sont optionnels. Par exemple :

[https://www.google.com/search?q=boot.dev](https://www.google.com/search?q=boot.dev)

`q=boot.dev` est un paramètre de requête. Comme les en-têtes, les paramètres de requête sont des paires `clé / valeur`. Dans ce cas, `q` est la clé et `boot.dev` est la valeur.

### La Documentation d'un Serveur HTTP

Vous vous demandez peut-être :

> Comment suis-je censé mémoriser comment tous ces différents serveurs fonctionnent ???

La bonne nouvelle est que *vous n'avez pas besoin de le faire*. Lorsque vous travaillez avec un serveur backend, c'est la responsabilité des développeurs de ce serveur de vous fournir des instructions, ou une *documentation* qui explique comment interagir avec lui.

Par exemple, la documentation devrait vous dire :

* Le domaine du serveur
    
* Les ressources avec lesquelles vous pouvez interagir (chemins HTTP)
    
* Les paramètres de requête pris en charge
    
* Les méthodes HTTP prises en charge
    
* Tout ce dont vous aurez besoin pour travailler avec le serveur
    

![Image](https://i.imgur.com/GIlWhYF.jpg align="left")

Le serveur a le contrôle

Comme nous l'avons mentionné précédemment, le serveur a un contrôle total sur la manière dont le chemin dans une URL est interprété et utilisé dans une requête. Il en va de même pour les paramètres de requête.

Tous les serveurs ne prennent pas en charge les paramètres de requête pour chaque type de requête, cela dépend simplement, donc vous devrez consulter la documentation.

### Paramètres de Requête Multiples

Nous avons mentionné que les paramètres de requête sont des paires `clé/valeur` - cela signifie que nous pouvons avoir plusieurs paires.

`http://example.com?firstName=lane&lastName=wagner`

Dans l'exemple ci-dessus :

* `firstName` = `lane`
    
* `lastName` = `wagner`
    

Le `?` sépare les paramètres de requête du reste de l'URL. Le `&` est ensuite utilisé pour séparer *chaque paire* de paramètres de requête après cela.

Par exemple, faites cette requête pour limiter le nombre de Pokémon retournés par le PokeAPI à `2` :

```plaintext
https://pokeapi.co/api/v2/location/?limit=2
```

## Qu'est-ce que HTTPS ?

Hypertext Transfer Protocol *Secure* ou [HTTPS](https://www.freecodecamp.org/news/what-is-https-http-vs-https-meaning-and-how-it-works/) est une extension du protocole HTTP. HTTPS sécurise le transfert de données entre le client et le serveur en [chiffrant](https://developer.mozilla.org/en-US/docs/Glossary/Encryption) toute la communication.

HTTPS permet à un client de partager en toute sécurité des informations sensibles avec le serveur via une requête HTTP, telles que des informations de carte de crédit, des mots de passe ou des numéros de compte bancaire.

HTTPS nécessite que le client utilise [SSL](https://developer.mozilla.org/en-US/docs/Glossary/SSL) ou [TLS](https://www.freecodecamp.org/news/what-is-tls-transport-layer-security-encryption-explained-in-plain-english/) pour protéger les requêtes et le trafic en chiffrant les informations dans la requête. HTTPS est simplement HTTP avec une sécurité supplémentaire.

![Image](https://i.imgur.com/iOkQUdG.png align="left")

*HTTP vs HTTPS*

### HTTPS garde vos messages privés, mais pas votre identité

Nous n'aborderons pas *comment* fonctionne le chiffrement dans ce cours, mais nous le ferons dans les cours ultérieurs. Pour l'instant, il est important de noter que bien que HTTPS chiffre *ce que vous dites*, il ne protège pas nécessairement *qui vous êtes*. Des outils comme les [VPN](https://nordvpn.com/what-is-a-vpn/) sont nécessaires pour rester anonyme en ligne.

### HTTPS garantit que vous parlez à la bonne personne (ou serveur)

En plus de chiffrer les informations dans une requête, HTTPS utilise des [signatures numériques](https://en.wikipedia.org/wiki/Digital_signature) pour prouver que vous communiquez avec le serveur que vous pensez être.

Si un pirate informatique interceptait une requête HTTPS en se branchant sur un câble réseau, il ne pourrait pas prétendre avec succès être le serveur web de votre banque.

En supposant qu'un serveur supporte HTTPS, vous l'utilisez simplement en changeant le protocole de votre URL de requête : `https://boot.dev`

### Vous voulez mettre en pratique ce que vous avez appris avec un projet ?

Consultez ce [guide de projet où vous construirez un crawler web en JavaScript](https://boot.dev/build/link-analyzer) à partir de zéro. Il vous fera utiliser l'API Fetch et analyser des données JSON comme un pro ! Vous n'avez pas besoin de construire le projet, mais c'est un excellent moyen de pratiquer ce que vous avez appris.

## Félicitations pour être arrivé à la fin !

Si vous êtes intéressé par les devoirs de codage interactifs et les quiz de ce cours, vous pouvez consulter le [cours Apprendre HTTP](https://boot.dev/learn/learn-object-oriented-programming) sur [Boot.dev](https://boot.dev/).

Ce cours fait partie de mon [parcours complet de carrière de développeur backend](https://boot.dev/tracks/backend), composé d'autres cours et projets si vous êtes intéressé à les consulter.

Si vous voulez voir les autres contenus que je crée liés au développement web, consultez quelques-uns de mes liens ci-dessous :

* [Lane sur Twitter](https://twitter.com/wagslane)
    
* [Lane sur YouTube](https://youtube.com/@bootdotdev)
    
* [Site Personnel de Lane](https://wagslane.dev)