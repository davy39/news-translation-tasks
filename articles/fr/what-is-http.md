---
title: Qu'est-ce que HTTP ? Aperçu du protocole pour débutants
subtitle: ''
author: Rufai Mustapha
co_authors: []
series: null
date: '2023-04-06T16:53:26.000Z'
originalURL: https://freecodecamp.org/news/what-is-http
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/http--5-.jpg
tags:
- name: http
  slug: http
- name: web
  slug: web
seo_title: Qu'est-ce que HTTP ? Aperçu du protocole pour débutants
seo_desc: "Without HTTP (Hypertext Transfer Protocol), the World Wide Web as we know\
  \ it today would not exist. HTTP is the protocol that enables the transfer of data\
  \ over the internet, allowing users to access websites and other online resources.\
  \  \nThere are va..."
---

Sans HTTP (Hypertext Transfer Protocol), le World Wide Web tel que nous le connaissons aujourd'hui n'existerait pas. HTTP est le protocole qui permet le transfert de données sur Internet, permettant aux utilisateurs d'accéder à des sites web et à d'autres ressources en ligne.  
  
Il existe diverses façons de concevoir des applications web, notamment GraphQL, SOAP, Falcor, gRPC, WebSockets et Serverless Functions, avec REST étant le plus populaire (selon l'enquête [2021 State-of-API](https://www.postman.com/state-of-api/2021/) de Postman). Et au cœur de toutes ces architectures se trouve HTTP.

## Qu'apprendre avec HTTP

Pour comprendre HTTP, il est utile d'avoir une compréhension de base des concepts suivants :

1. Réseautage : La connaissance de la manière dont les ordinateurs communiquent entre eux via des réseaux est essentielle pour comprendre HTTP. Cela inclut des concepts tels que les adresses IP, le DNS et le routage.
2. Architecture web : HTTP est une partie clé de l'architecture web, donc comprendre comment les applications et les sites web sont construits peut vous aider à mieux comprendre HTTP. Cela inclut des concepts tels que HTML, CSS et JavaScript.
3. Programmation côté serveur : HTTP est utilisé pour communiquer entre les navigateurs web et les serveurs, donc comprendre comment les serveurs fonctionnent et comment construire des applications côté serveur peut vous aider à comprendre comment HTTP fonctionne.
4. Programmation côté client : HTTP est également utilisé pour communiquer entre les navigateurs web et les applications côté client, donc comprendre comment construire des applications côté client en utilisant JavaScript peut également être utile.

### À quoi s'attendre dans cet article

* Comment fonctionne le protocole HTTP.
* Comment faire des requêtes réseau avec Chrome et Postman.
* Comment téléverser des données avec la méthode HTTP POST dans Postman.

À la fin de l'article, les lecteurs devraient avoir une compréhension de base de HTTP, ainsi que des outils et ressources disponibles pour tester et dépanner les applications.

## Table des matières

* [Introduction à HTTP](#heading-introduction-a-http)
* [Qu'est-ce que le cycle requête-réponse HTTP ?](#heading-quest-ce-que-le-cycle-requete-reponse-http)
* [Comment créer des requêtes HTTP](#heading-comment-creer-des-requetes-http)
* [Qu'est-ce qu'une URL de requête HTTP ?](#heading-quest-ce-quune-url-de-requete-http)
* [Quelles sont les méthodes de requête HTTP ?](#heading-quelles-sont-les-methodes-de-requete-http)
* [Quels sont les en-têtes de requête HTTP ?](#heading-quels-sont-les-en-tetes-de-requete-http)
* [Qu'est-ce qu'un corps de requête HTTP ?](#heading-quest-ce-quun-corps-de-requete-http)
* [Qu'est-ce qu'une réponse HTTP ?](#heading-quest-ce-quune-reponse-http)

## Introduction à HTTP

HTTP (Hypertext Transfer Protocol) est un protocole utilisé pour échanger des informations sur Internet. HTTP est comme le système de livraison pour les informations sur Internet. Il s'assure que les informations vont d'un endroit à un autre, comme les navires transportent des marchandises à travers l'océan. C'est la base du World Wide Web.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/http-client-server.jpg)

HTTP est ce qui fait fonctionner Internet. C'est un moyen pour les navigateurs web et les serveurs de communiquer entre eux et d'envoyer des choses comme des pages web d'avant en arrière. Il est important pour les personnes qui construisent des sites web et des applications web de savoir comment cela fonctionne.  
  
Sans HTTP, il serait difficile d'imaginer comment Internet fonctionnerait. Il n'y aurait pas de pages web, pas d'URLs, et pas d'hyperliens. Au lieu de cela, les utilisateurs devraient connaître l'adresse IP exacte du serveur hébergeant les informationsqu'ils souhaitent accéder, et ils devraient utiliser un protocole de bas niveau comme TCP/IP pour transférer des données.

## Qu'est-ce que le cycle requête-réponse HTTP ?

La communication en HTTP repose sur un concept appelé le cycle requête-réponse. 

![Image](https://www.freecodecamp.org/news/content/images/2023/04/http-client-server-RR.jpg)

  
Le cycle requête-réponse est le processus par lequel un client (tel qu'un navigateur web ou une application mobile) communique avec un serveur pour récupérer des ressources ou effectuer des actions. Le cycle implique plusieurs étapes :

1. Le client initie une requête au serveur en envoyant un message de requête HTTP, qui contient des informations telles que la ressource demandée et tout paramètre supplémentaire.
2. Le serveur reçoit le message de requête et le traite, utilisant ses ressources pour générer un message de réponse.
3. Le serveur envoie le message de réponse au client, qui contient généralement la ressource demandée (comme une page web) et toute information ou métadonnée supplémentaire.
4. Le client reçoit le message de réponse et le traite, généralement en rendant le contenu dans un navigateur web ou en l'affichant dans une application.
5. Le client peut initier des requêtes supplémentaires au serveur, répétant le cycle si nécessaire.

## Comment créer des requêtes HTTP

Pour créer une requête HTTP valide, vous avez besoin des éléments suivants :

* Une URL.
* La méthode HTTP.
* Une liste d'en-têtes (en-têtes de requête).
* Le corps de la requête.

Voici un exemple d'en-tête de requête HTTP, avec trois lignes :

```http
GET /watch?v=8PoQpnlBXD0 HTTP/1.1
Host: www.youtube.com
Cookie: GPS=1; VISITOR_INFO1_LIVE=kOe2UTUyPmw; YSC=Jt6s9YVWMd4
```

1. La première ligne spécifie la méthode HTTP, le chemin et la version du protocole. Dans ce cas, il s'agit d'une requête `GET` pour la vidéo située à l'adresse `/watch?v=8PoQpnlBXD0` en utilisant le protocole HTTP/1.1.
2. La deuxième ligne spécifie l'hôte du site web, qui est [`www.youtube.com`](http://www.youtube.com/).
3. La troisième ligne contient un en-tête de cookie, qui est utilisé pour envoyer et stocker de petites quantités de données côté client. Dans ce cas, l'en-tête de cookie contient trois valeurs : `GPS=1, VISITOR_INFO1_LIVE=kOe2UTUyPmw`, et `YSC=Jt6s9YVWMd4`. Ces valeurs peuvent être utilisées par YouTube pour suivre et personnaliser l'expérience de l'utilisateur.

## Qu'est-ce qu'une URL de requête HTTP ?

![Image](https://www.freecodecamp.org/news/content/images/2023/04/url.jpg)

Lorsque qu'un navigateur web tente d'accéder à une image sur Internet, il envoie une requête au serveur en utilisant une URL. Cette URL est _unique_ et pointe vers une _ressource_ spécifique sur le serveur.  

Une ressource peut être n'importe quoi qui a un nom et peut être accédée avec un identifiant unique comme un utilisateur, un produit, un article, un document ou une image. Vous pouvez penser aux ressources comme des _noms_.

## Quelles sont les méthodes de requête HTTP ?

La méthode de requête indique au serveur quel type d'action le client souhaite que le serveur entreprenne. Les méthodes les plus courantes sont :

<table>
<thead>
<tr>
<th>Méthodes HTTP</th>
<th>Définition</th>
</tr>
</thead>
<tbody>
<tr>
<td>HEAD</td>
<td>Demande au serveur l'état (taille, disponibilité) d'une ressource.</td>
</tr>
<tr>
<td>GET</td>
<td>Demande au serveur de récupérer une ressource.</td>
</tr>
<tr>
<td>POST</td>
<td>Demande au serveur de créer une nouvelle ressource.</td>
</tr>
<tr>
<td>PUT</td>
<td>Demande au serveur de modifier/mettre à jour une ressource existante.</td>
</tr>
<tr>
<td>DELETE</td>
<td>Demande au serveur de supprimer une ressource.</td>
</tr>
</tbody>
</table>

## Quels sont les en-têtes de requête HTTP ?

Les en-têtes de requête HTTP sont des informations supplémentaires envoyées par le client dans le cadre d'une requête HTTP. Ils ont un format nom/valeur. C'est-à-dire :

```txt
Nom: Valeur
```

Ces en-têtes fournissent un contexte et des instructions supplémentaires au serveur, qui peuvent être utilisés pour traiter la requête ou personnaliser la réponse.

%[https://youtu.be/hqQR1O2H_ck]

Voici un exemple d'en-tête de requête HTTP :

```http
GET /api/data HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36
Accept: application/json
Accept-Language: en-US,en;q=0.5
Authorization: Token abc123
Cache-Control: no-cache
Connection: keep-alive
Referer: https://www.google.com/
Pragma: no-cache
```

Dans cet exemple, la méthode `GET` est utilisée pour envoyer une requête à l'endpoint `/api/data` sur le serveur `example.com` en utilisant le protocole HTTP/1.1. La requête inclut dix en-têtes :

| En-têtes | Définition |
| ------- | ---------- |
| Host | Cet en-tête spécifie le nom d'hôte du serveur auquel le client tente de se connecter. |
| User-Agent | Cet en-tête fournit des informations sur le client qui effectue la requête (dans ce cas, une version du navigateur Chrome). |
| Accept | Cet en-tête spécifie les types MIME de données que le client est prêt à accepter dans la réponse. |
| Accept-Language | Cet en-tête spécifie la ou les langues préférées pour la réponse. |
| Authorization | Cet en-tête fournit un jeton d'accès (dans ce cas, Token abc123) à des fins d'authentification. |
| Cache-Control | Cet en-tête spécifie les directives de mise en cache pour les requêtes et les réponses. |
| Connection | Cet en-tête spécifie les options de gestion de la connexion entre le client et le serveur. |
| Referer | Cet en-tête spécifie l'URL de la page qui a lié à la page actuelle. |
| Pragma | Cet en-tête spécifie des directives spécifiques à l'implémentation qui peuvent s'appliquer à tout agent le long de la chaîne requête-réponse. |
| Content-Type | Cet en-tête spécifie le type MIME des données envoyées dans le corps de la requête, mais il n'est pas utilisé dans cet exemple car il s'agit d'une requête GET sans corps de requête. |

%[https://youtu.be/Pjok-1Q6MOs]

## Qu'est-ce qu'un corps de requête HTTP ?

Dans HTTP, le corps de la requête est les données envoyées du client au serveur dans le cadre d'une requête HTTP. L'exemple ci-dessous montre comment téléverser une image sur le [Serveur API Cat](https://documenter.getpostman.com/view/5578104/RWgqUxxh#5a07d324-155b-487e-80a5-b1b9c1775339) :

%[https://youtu.be/zAVCD0nLnjg]

Et voici à quoi ressemble la requête :

```http
POST /v1/images/upload HTTP/1.1
Host: api.thecatapi.com
x-api-key: API_KEY
Content-Length: 232
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW

------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="file"; filename="/C:/Users/USER/Downloads/cat1.jpg"
Content-Type: image/jpeg

(data)
------WebKitFormBoundary7MA4YWxkTrZu0gW--
```

La requête inclut ces en-têtes :

1. `Host` : Cet en-tête spécifie le nom d'hôte du serveur auquel le client tente de se connecter.
2. `Content-Type` : La requête téléverse un fichier image nommé `cat1.jpg` en utilisant un type de données appelé `multipart/form-data`. L'image est au format JPEG et son contenu est inclus dans le corps de la requête.
3. `x-api-key` : Cet en-tête fournit une clé API à des fins d'authentification.
4. `Content-Length` : Cet en-tête spécifie la longueur du corps de la requête en octets. La valeur de ce champ est 232.

Lorsque le serveur reçoit cette requête, il analysera le corps de la requête et l'utilisera pour créer une nouvelle entrée dans la base de données de l'API Cat. Le serveur renverra ensuite une réponse contenant des informations sur la nouvelle entrée, telles que l'URL de l'image et l'ID de la base de données.

## Qu'est-ce qu'une réponse HTTP ?

Une réponse HTTP est le message qu'un serveur envoie à un client en réponse à une requête HTTP. Elle se compose généralement d'une ligne d'état, d'en-têtes et d'un corps de message :

```http
HTTP/1.1 200 OK
Date: Sun, 28 Mar 2023 10:15:00 GMT
Content-Type: application/json
Server: Apache/2.4.39 (Unix) OpenSSL/1.1.1c PHP/7.3.6
Content-Length: 1024

{
    "name": "John Doe",
    "email": "johndoe@example.com",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "zip": "12345"
    }
}
```

La ligne d'état contient la version HTTP, un code d'état indiquant le résultat de la requête, et un message correspondant.

Les en-têtes fournissent des informations supplémentaires sur la réponse, telles que le type de contenu du corps du message ou la date et l'heure auxquelles la réponse a été envoyée.

Le corps du message contient les données de réponse réelles, telles que le contenu HTML, JSON ou XML.

Voici quelques codes d'état HTTP courants :


| Code | Signification |
| ------ | ----------- |
| 100 | Continuer |
| 101 | Changement de protocole |
| 200 | OK |
| 201 | Créé |
| 202 | Accepté |
| 203 | Information non autorisée |
| 404  | Non trouvé : La ressource demandée n'a pas été trouvée sur le serveur. |
| 500 | Erreur interne du serveur : Le serveur a rencontré une erreur lors du traitement de la requête. |
| 301  | Déplacé de manière permanente : La ressource demandée a été déplacée de manière permanente vers une nouvelle URL. |

Voici un exemple de réponse JSON de l'API Cat :

```json
{
    "id": "ErDd1JRRT",
    "url": "https://cdn2.thecatapi.com/images/ErDd1JRRT.jpg",
    "width": 4282,
    "height": 6424,
    "original_filename": "cat1.jpg",
    "pending": 0,
    "approved": 1
}
```

Il s'agit d'une réponse JSON à une requête de l'API Cat qui semble fournir des métadonnées sur une image qui a été téléversée ou récupérée depuis l'API. Voici ce que signifie chaque champ :

* `id` : Un identifiant unique pour l'image.
* `url` : L'URL où l'image peut être accessible.
* `width` : La largeur de l'image en pixels.
* `height` : La hauteur de l'image en pixels.
* `original_filename` : Le nom original du fichier qui a été téléversé.
* `pending` : Un indicateur montrant si l'image est encore en cours de traitement par l'API.
* `approved` : Un indicateur montrant si l'image a été approuvée pour une utilisation publique par l'API.

## Conclusion

HTTP (Hypertext Transfer Protocol) est un protocole utilisé pour échanger des informations sur Internet. Il constitue la base du World Wide Web et permet la communication entre les navigateurs web et les serveurs.   
  
Cet article est une courte introduction à HTTP. Si vous êtes intéressé à en apprendre davantage, consultez ces recommandations de livres :

* "HTTP: The Definitive Guide" par David Gourley et Brian Totty - Ce livre est largement considéré comme le guide de référence sur HTTP. Il couvre le protocole en profondeur et fournit des informations détaillées sur ses fonctionnalités et son implémentation.
* "HTTP Pocket Reference" par Clinton Wong - Ce livre fournit une référence concise et portable au protocole HTTP. Il couvre l'essentiel du protocole et est une excellente ressource pour les développeurs qui ont besoin d'un accès rapide aux informations HTTP.
* "Web Performance Daybook Volume 2: Techniques and Tips for Optimizing Web Site Performance" édité par Stoyan Stefanov - Ce livre est une collection d'essais et d'articles sur la performance web, incluant une section sur l'optimisation HTTP. Il fournit des conseils pratiques sur la manière d'optimiser HTTP pour une performance web plus rapide et plus efficace.