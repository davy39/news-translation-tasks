---
title: 'Une introduction à HTTP : tout ce que vous devez savoir'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-11T15:23:37.000Z'
originalURL: https://freecodecamp.org/news/http-and-everything-you-need-to-know-about-it
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/slik.jpeg
tags:
- name: http
  slug: http
- name: https
  slug: https
- name: internet
  slug: internet
- name: General Programming
  slug: programming
- name: SSL
  slug: ssl
seo_title: 'Une introduction à HTTP : tout ce que vous devez savoir'
seo_desc: 'By Goran Aviani

  In this article, I will walk you through how the world wide web works at a fundamental
  level.

  The core technology is HTTP - Hypertext Transfer Protocol. It''s the communication
  protocol you use when you browse the web.

  At a fundamental...'
---

Par Goran Aviani

Dans cet article, je vais vous expliquer comment le world wide web fonctionne à un niveau fondamental.

La technologie centrale est HTTP - Hypertext Transfer Protocol. C'est le protocole de communication que vous utilisez lorsque vous naviguez sur le web.

À un niveau fondamental, lorsque vous visitez un site web, votre navigateur envoie une requête HTTP à un serveur. Ensuite, ce serveur répond avec une ressource (une image, une vidéo, ou le HTML d'une page web) - que votre navigateur affiche ensuite pour vous.

C'est le modèle basé sur les messages de HTTP. Chaque interaction HTTP inclut une requête et une réponse.

Par nature, HTTP est sans état.

**Sans état** signifie que toutes les requêtes sont séparées les unes des autres. Ainsi, chaque requête de votre navigateur doit contenir suffisamment d'informations pour que le serveur puisse satisfaire la requête. Cela signifie également que chaque transaction du modèle basé sur les messages de HTTP est traitée séparément des autres.

## URLs

L'URL (Uniform Resource Locator) est probablement le concept le plus connu du Web. C'est aussi l'un des concepts les plus importants et utiles. Une URL est une adresse web utilisée pour identifier les ressources sur le Web.

L'idée du web est structurée autour des ressources. Depuis ses débuts, le Web était la plateforme pour partager des fichiers texte/HTML, des documents, des images, etc., et à ce titre, il peut être considéré comme une collection de ressources.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0-DTR8JpFZo31ht-Kd.jpg)
_Exemple d'une URL_

**Protocole**

Le plus souvent, ce sont HTTP (ou HTTPS pour une version sécurisée de HTTP).

D'autres protocoles notables sont :

* File Transfer Protocol (FTP)

est un protocole standard utilisé pour transférer des fichiers entre un client et un serveur sur un réseau.
* Simple Mail Transfer Protocol (SMTP) est un standard pour la transmission d'e-mails.

**Domaine**

Nom utilisé pour identifier une ou plusieurs adresses IP où la ressource est située.

**Chemin** Spécifie l'emplacement de la ressource sur le serveur. Il utilise la même logique qu'un emplacement de ressource utilisé sur l'appareil où vous lisez cet article (par exemple, /search/cars/VWBeetle.pdf ou C:/my cars/VWBeetle.pdf).

**Paramètres**

Données supplémentaires utilisées pour identifier ou filtrer la ressource sur le serveur.

**Note** : Lorsque vous recherchez des articles et plus d'informations sur HTTP, vous pouvez rencontrer le terme URI (ou uniform resource identifier). URI est parfois utilisé à la place de URL, mais principalement dans les spécifications formelles et par des personnes qui veulent frimer. :)

## Requêtes HTTP

Dans HTTP, chaque requête doit avoir une adresse URL. De plus, la requête a besoin d'une méthode. Les quatre principales méthodes HTTP sont :

* GET
* PUT
* POST
* DELETE

Je vais expliquer ces méthodes, et plus, dans la section Méthodes HTTP de cet article.

Et ces méthodes correspondent directement à des actions :

* lire
* mettre à jour
* créer
* supprimer

Tous les messages HTTP ont un ou plusieurs en-têtes, suivis d'un corps de message facultatif. Le corps contient les données qui seront envoyées avec la requête ou les données reçues avec la réponse.

La première partie de chaque requête HTTP contient trois éléments :

Exemple :

* GET /adds/search-result?item=vw+beetle HTTP/1.1

_Quand une URL contient un signe "?", cela signifie qu'elle contient une requête. Cela signifie qu'elle envoie des paramètres de la ressource demandée._

1. La première partie est une méthode qui indique quelle méthode HTTP est utilisée. La méthode la plus couramment utilisée est la méthode GET. La méthode GET récupère une ressource du serveur web et, comme GET n'a pas de corps de message, rien après l'en-tête n'est nécessaire.
2. La deuxième partie est une URL demandée.
3. La troisième partie est une version HTTP utilisée. La version 1.1 est la version la plus courante pour la plupart des navigateurs, cependant, la version 2.0 prend le relais.

Il y a aussi d'autres choses intéressantes dans une requête HTTP :

**En-tête Referer**

indique l'URL d'où provient la requête.

**En-tête User-Agent**

informations supplémentaires sur le navigateur utilisé pour générer la requête.

**En-tête Host**

identifie de manière unique un nom d'hôte ; il est nécessaire lorsque plusieurs pages web sont hébergées sur le même serveur.

**En-tête Cookie**

soumet des paramètres supplémentaires au client.

## Réponses HTTP

Tout comme dans les requêtes HTTP, les réponses HTTP se composent également de trois éléments :

Exemple :

HTTP/1.1 200 OK

1. La première partie est la version HTTP utilisée.
2. La deuxième partie est le code numérique du résultat de la requête.
3. La troisième partie est une description textuelle de la deuxième partie.

Il y a d'autres choses intéressantes dans une réponse HTTP :

**En-tête Server**

informations sur le logiciel du serveur web utilisé.

**En-tête Set-Cookie**

émet le cookie au navigateur.

**Corps du message**

il est courant pour une réponse HTTP de contenir un corps de message.

**En-tête Content-Length**

indique la taille du corps du message en octets.

## Méthodes HTTP

Les méthodes les plus courantes sont GET et POST. Mais il y en a quelques autres aussi.

**GET**

Vous utilisez cette méthode pour demander des données à une ressource spécifiée où les données ne sont pas modifiées de quelque manière que ce soit. Les requêtes GET ne changent pas l'état de la ressource.

**POST**

Vous utilisez cette méthode pour envoyer des données à un serveur afin de créer une ressource.

**PUT
** Vous utilisez cette méthode pour mettre à jour la ressource existante sur un serveur en utilisant le contenu dans le corps de la requête. Considérez cela comme un moyen d'"éditer" quelque chose.

**HEAD**

Vous utilisez cette méthode de la même manière que GET, mais avec la distinction que le retour d'une méthode HEAD ne doit pas contenir de corps dans la réponse. Mais le retour contiendra les mêmes en-têtes que si GET était utilisé. Vous utilisez la méthode HEAD pour vérifier si la ressource est présente avant de faire une requête GET.

**TRACE
**
Vous utilisez cette méthode à des fins de diagnostic. La réponse contiendra dans son corps le contenu exact du message de la requête.

**OPTIONS**

Vous utilisez cette méthode pour décrire les options de communication (méthodes HTTP) qui sont disponibles pour la ressource cible.

**PATCH
**
Vous utilisez cette méthode pour appliquer des modifications partielles à une ressource.

**DELETE
**Vous utilisez cette méthode pour supprimer la ressource spécifiée.

## REST

Le transfert d'état représentationnel (REST) est un style d'architecture où les requêtes et les réponses contiennent des représentations de l'état actuel de la ressource du système.

Méthode "régulière" :

* [http://carapp.com/search?make=wv&model=beetle](http://carapp.com/search?make=wv&model=beetle)

Style REST :

* [http://carapp.com/search/vw/beetle](http://carapp.com/search/vw/beetle)

Vous pouvez [en apprendre plus sur REST ici si vous êtes curieux](https://www.freecodecamp.org/news/how-the-web-works-part-iii-http-rest-e61bc50fa0a/).

## En-têtes HTTP

Il y a trois composants principaux qui constituent la structure de la requête/réponse. Ceux-ci incluent :

* Première ligne
* En-têtes
* Corps/Contenu

Nous avons déjà parlé de la première ligne dans les requêtes et réponses HTTP, et la fonction du corps a également été mentionnée. Maintenant, nous allons parler des en-têtes HTTP.

Les en-têtes HTTP sont ajoutés après la première ligne et sont définis comme des paires nom:valeur séparées par un deux-points. Les en-têtes HTTP sont utilisés pour envoyer des paramètres supplémentaires avec la requête ou la réponse.

Comme je l'ai déjà dit, le corps du message inclut les données à envoyer avec la requête ou les données reçues avec la réponse.

Il existe différents types d'en-têtes qui sont regroupés en fonction de leur utilisation en 4 grandes catégories :

* **En-tête général**

En-têtes qui peuvent être utilisés dans les messages de requête et de réponse et qui sont indépendants des données échangées.
* **En-tête de requête**

Ces en-têtes définissent des paramètres pour les données demandées ou des paramètres qui donnent des informations importantes sur le client faisant la requête.
* **En-tête de réponse**

Ces en-têtes contiennent des informations sur la réponse entrante.
* **En-tête d'entité**

Les en-têtes d'entité décrivent le contenu qui constitue le corps du message.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0-0BI1BEJpajUiJ_4R.jpg)
_Types d'en-têtes_

## Codes de statut HTTP

En naviguant sur le web, vous avez peut-être rencontré des pages "erreur 404 : non trouvé" ou des pages "erreur 500 : le serveur ne répond pas".

Ce sont des codes de statut HTTP.

Chaque message de réponse HTTP doit contenir un code de statut HTTP dans sa première ligne, nous indiquant le résultat de la requête.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Steve_Losh_on_Twitter___HTTP_status_ranges_in_a_nutshell__1xx__hold_on_2xx__here_you_go_3xx__go_away_4xx__you_fucked_up_5xx__I_fucked_up_.png)

Il y a cinq groupes de codes de statut qui sont regroupés par le premier chiffre :

* 1xx

Informatif.
* 2xx

La requête a réussi.
* 3xx

Le client est redirigé vers une ressource différente.
* 4xx

La requête contient une erreur de quelque sorte.
* 5xx

Le serveur a rencontré une erreur en satisfaisant la requête.

[Voici une liste complète des codes de réponse de statut HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) et leur explication.

## HTTPS (Hypertext Transfer Protocol Secure)

La version sécurisée du protocole HTTP est HyperText Transfer Protocol Secure (HTTPS). HTTPS fournit une communication chiffrée entre un navigateur (client) et le site web (serveur).

Dans HTTPS, le protocole de communication est chiffré en utilisant Transport Layer Security (TLS) ou Secure Sockets Layer (SSL).

Le protocole est donc souvent appelé HTTP sur TLS, ou HTTP sur SSL.

Les protocoles TLS et SSL utilisent un système de chiffrement asymétrique. Les systèmes de chiffrement asymétrique utilisent une clé publique (clé de chiffrement) et une clé privée (clé de déchiffrement) pour chiffrer un message.

N'importe qui peut utiliser la clé publique pour chiffrer un message. Cependant, les clés privées sont secrètes, et cela signifie que seul le destinataire prévu peut déchiffrer le message.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0-pB_y5GVIF_O_z4lw.gif)
_Exemple de système de chiffrement asymétrique_

#### Poignée de main SSL/TLS

Lorsque vous demandez une connexion HTTPS à un site web, le site web envoie son certificat SSL à votre navigateur. Ce processus où votre navigateur et le site web initient la communication est appelé la "poignée de main SSL/TLS".

La poignée de main SSL/TLS implique une série d'étapes où le navigateur et le site web se valident mutuellement et commencent la communication à travers le tunnel SSL/TLS.

Comme vous l'avez probablement remarqué, lorsqu'un tunnel sécurisé de confiance est utilisé pendant une connexion HTTPS, l'icône de cadenas vert est affichée dans la barre d'adresse du navigateur.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/0-g7q-rF8JTGp7fs19.png)
_Exemple de l'une de mes pages sécurisées_

#### **Avantages de HTTPS**

Les principaux avantages de HTTPS sont :

* Les informations des clients, comme les numéros de carte de crédit et autres informations sensibles, sont chiffrées et ne peuvent pas être interceptées.
* Les visiteurs peuvent vérifier que vous êtes une entreprise enregistrée et que vous possédez le domaine.
* Les clients savent qu'ils ne doivent pas visiter de sites sans HTTPS, et donc, ils sont plus susceptibles de faire confiance et de compléter des achats sur des sites qui utilisent HTTPS.

Merci d'avoir lu ! Consultez d'autres articles comme celui-ci [sur mon profil freeCodeCamp](https://www.freecodecamp.org/news/author/goran/). Et découvrez d'autres choses amusantes que je construis [sur ma page GitHub](https://github.com/GoranAviani).