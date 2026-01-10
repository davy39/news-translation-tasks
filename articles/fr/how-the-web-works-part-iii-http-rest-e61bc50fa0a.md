---
title: 'Comment le Web fonctionne Partie III : HTTP & REST'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-12-30T16:12:13.000Z'
originalURL: https://freecodecamp.org/news/how-the-web-works-part-iii-http-rest-e61bc50fa0a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*akH3uy2vSLQ0ba4odSKI_w.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 'Comment le Web fonctionne Partie III : HTTP & REST'
seo_desc: 'By Preethi Kasireddy

  We went over basic web architecture in part I, and we talked about web application
  structure in part II. Now it’s time to roll up our sleeves and tackle part III:
  a closer look at HTTP and REST.

  Understanding HTTP is crucial for ...'
---

Par Preethi Kasireddy

Nous avons passé en revue l'architecture web de base dans la [partie I](https://medium.freecodecamp.com/how-the-web-works-a-primer-for-newcomers-to-web-development-or-anyone-really-b4584e63585c), et nous avons parlé de la structure des applications web dans la [partie II](https://medium.freecodecamp.com/how-the-web-works-part-ii-client-server-model-the-structure-of-a-web-application-735b4b6d76e3). Il est maintenant temps de retrousser nos manches et de nous attaquer à la partie III : un regard plus approfondi sur HTTP et REST.

Comprendre HTTP est crucial pour les développeurs web car il facilite le flux d'informations dans les applications web, permettant de meilleures interactions utilisateur et une performance améliorée du site.

### Qu'est-ce que HTTP ?

Dans le modèle Client-Serveur, les clients et les serveurs échangent des messages selon un modèle de messagerie "requête-réponse" : le client envoie une requête et le serveur retourne une réponse.

Suivre ces messages est plus compliqué qu'il n'y paraît, donc le client et le serveur adhèrent à un langage commun et à un ensemble de règles pour savoir à quoi s'attendre. Ce langage, ou "protocole", est appelé HTTP.

Le protocole HTTP définit la syntaxe (le format des données et l'encodage), la sémantique (la signification associée à la syntaxe) et le timing (la vitesse et la séquence). Chaque requête et réponse HTTP échangées entre un client et un serveur est considérée comme une seule **transaction HTTP**.

### HTTP : Les grandes lignes

Il y a quelques points à noter sur HTTP avant de plonger dans les détails.

Tout d'abord, HTTP est basé sur du texte, ce qui signifie que les messages échangés entre le client et le serveur sont des morceaux de texte. Chaque message contient deux parties : un en-tête et un corps.

Deuxièmement, HTTP est un protocole de couche application, ce qui signifie qu'il s'agit simplement d'une couche d'abstraction qui standardise la manière dont les hôtes communiquent. HTTP lui-même ne transmet pas les données. Il dépend toujours du protocole TCP/IP sous-jacent pour obtenir la requête et la réponse d'une machine à une autre.

(Rappel : TCP/IP est un système en deux parties qui fonctionne comme le système de "contrôle fondamental" de l'Internet. Pour plus d'informations sur TCP/IP, consultez la [Partie I](https://medium.freecodecamp.com/how-the-web-works-a-primer-for-newcomers-to-web-development-or-anyone-really-b4584e63585c))

Enfin, vous avez peut-être vu le protocole "HTTPS" dans la barre d'adresse de votre navigateur et vous êtes demandé si HTTP est la même chose que HTTP + "S". La réponse courte est oui, avec une légère différence.

Une requête ou réponse HTTP simple n'est pas cryptée et est vulnérable à divers types d'attaques de sécurité. HTTPS, en revanche, est une communication plus sécurisée qui utilise le cryptage pour garder les choses en sécurité. Il signifie HTTP sur TLS/SSL.

SSL est un protocole de sécurité qui permet au client et au serveur de communiquer sur un réseau de manière sécurisée — pour prévenir l'écoute clandestine et la falsification — tandis que le message traverse le réseau.

Le client indique généralement s'il a besoin d'une connexion TLS/SSL en utilisant un numéro de port spécial : 443. Une fois que le client et le serveur conviennent d'utiliser TLS/SSL pour communiquer, ils négocient une connexion stateful en effectuant ce qu'on appelle une "poignée de main TLS". Le client et le serveur établissent ensuite des clés de session secrètes qu'ils peuvent utiliser pour crypter et décrypter les messages lorsqu'ils communiquent entre eux.

De nombreux sites web majeurs comme Google et Facebook utilisent HTTPS — après tout, c'est ce qui garde vos mots de passe, vos informations personnelles et les détails de votre carte de crédit en sécurité sur le réseau.

### HTTP : Les détails

Avec ces bases en place, plongeons un peu plus profondément dans la structure de HTTP.

Nous pouvons commencer par visiter [https://www.github.com](https://www.github.com) pour communiquer avec un serveur GitHub. Si vous utilisez Chrome ou Firefox avec l'extension Firebug installée, vous pouvez examiner les détails des requêtes HTTP en allant dans l'onglet "Réseau". Si vous avez cela ouvert, puis visitez [www.github.com](http://www.github.com) en le tapant dans votre barre d'adresse et vous devriez voir quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/0*iIfVK98DBgJSL1bP.png)

Ensuite, dans le panneau de gauche, cliquez sur le premier chemin, "github.com." Vous devriez maintenant voir ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/0*7lnbizzpM7tRIws2.png)

### En-tête de requête HTTP

Les en-têtes HTTP contiennent généralement des métadonnées (des données sur les données). Les métadonnées incluent le type de requête (GET vs. POST vs. PUT vs. DELETE), le chemin, le code de statut, le type de contenu, l'agent utilisateur, le cookie, le corps de la publication (parfois), et plus encore.

Examinons de plus près les parties les plus importantes de l'en-tête en utilisant l'exemple de Github, en commençant par la section "en-têtes de réponse" :

* **URL de la requête : https://github.com/**
* L'URL que nous avons demandée
* **Méthode de requête : GET**
* Le type de méthode HTTP utilisé. Dans notre cas, notre navigateur a dit : "Hey, serveur de Github, GET me to your homepage."
* **Code de statut : 200 OK**
* Une manière standardisée pour le serveur d'informer le client du résultat de sa requête. Le code de statut 200 signifie que le serveur a trouvé avec succès la ressource et l'envoie.
* **Adresse distante : 192.30.252.129:443**
* L'adresse IP et le numéro de port du site web GitHub que nous avons visité. Notez qu'il s'agit du port # 443 (ce qui signifie que nous utilisons HTTPS au lieu de HTTP).
* **Encodage du contenu : gzip**
* L'encodage de la ressource que nous avons reçue. Dans notre cas, le serveur de Github nous informe que le contenu qu'il envoie est compressé. Github compresse probablement le fichier pour que vous puissiez avoir un temps de téléchargement plus rapide.
* **Type de contenu : text/HTML ; charset=utf-8**
* Spécifie la représentation des données dans le corps de la réponse, y compris le type et le sous-type. Le type décrit le type de données, tandis que le sous-type spécifie un format spécifique pour ce type de données. Dans notre cas, nous avons du texte envoyé sous forme de HTML
* La deuxième partie spécifie l'encodage des caractères pour le document HTML. Cela sera le plus souvent UTF-8, comme c'est le cas ci-dessus.

Il y a aussi beaucoup d'informations d'en-tête, que le client a dû envoyer pour que le serveur sache comment répondre. Jetez un coup d'œil sous la partie "en-têtes de requête" :

* **User-Agent : Mozilla/5.0 (Macintosh ; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36**
* Le logiciel qui agit au nom d'un utilisateur. Parfois, un site web a besoin de savoir comment il est visualisé. Donc le navigateur envoie cette chaîne User-Agent que le serveur peut utiliser pour déterminer ce qui est utilisé pour accéder à un site web
* **Accept-Encoding : gzip, deflate, sdch**
* Spécifie quel encodage de contenu le navigateur est prêt à accepter. Nous pouvons voir que gzip est listé, et c'est pourquoi le serveur de Github a pu nous envoyer le contenu au format gzip.
* **Accept-Language : en-US,en;q=0.8**
* Décrit la langue dans laquelle nous voulons que la page web soit. Dans notre cas, "en" signifie anglais.
* **Host : github.com**
* Auto-explicatif :)
* **Cookie : _octo=GH1.1.491617779.1446477115; logged_in=yes; dotcom_user=iam-peekay;** **_gh_sess=somethingFakesomething FakesomethingFakesomethingFakesomethingFakesomethingFakesomethingFakesomethingFake; user_session=FakesomethingFake somethingFakesomethingFakesomethingFake; _ga=9389479283749823749; tz=America%2FLos_Angeles_**
* Un morceau de texte qu'un serveur web peut stocker sur la machine d'un utilisateur et récupérer plus tard. Les informations sont stockées sous forme de paires nom-valeur. L'une des paires nom-valeur que Github a stockées pour ma requête, par exemple, est "dotcom_user=iam-peekay", ce qui informe Github que mon identifiant utilisateur est iam-peekay.

#### tl;dr : que se passe-t-il avec toutes ces paires nom-valeur ?

En bref, nous nous retrouvons avec beaucoup de paires nom-valeur. Mais comment ces paires nom-valeur sont-elles créées ?

Chaque fois que votre navigateur visite un site web, il recherchera sur votre ordinateur un fichier cookie défini par le site web plus tôt.

Donc, si je visite [www.github.com,](http://www.github.com,) mon navigateur recherchera un fichier cookie que GitHub a enregistré sur mon disque dur. S'il trouve un fichier cookie, il enverra toutes les paires nom-valeur dans l'en-tête de la requête.

Le serveur web de GitHub peut maintenant utiliser les données de cookie de nombreuses manières différentes, telles que le rendu de contenu basé sur mes préférences utilisateur stockées, le comptage du nombre de fois où j'ai visité leur site.

Si le navigateur ne trouve pas de fichier cookie — soit parce que le site n'a jamais été visité auparavant, soit parce que l'utilisateur l'a bloqué ou supprimé — le navigateur n'envoie aucune donnée de cookie.

Dans ce cas, le serveur de GitHub crée un nouvel ID sous forme de paire nom-valeur, ainsi que toute autre paire nom-valeur qu'il souhaite, et l'envoie à mon ordinateur via l'en-tête HTTP — que mon ordinateur stocke ensuite sur son disque dur.

### Corps HTTP

Comme vous l'avez vu ci-dessus, le serveur contient la plupart des "métadonnées" (données sur les données) importantes dont il a besoin pour communiquer avec le client.

Passons maintenant au corps.

Le corps, comme vous pouvez le deviner, est le corps du message. Selon le type de requête, il peut être vide.

Dans notre cas, vous pouvez voir le corps dans l'onglet "Réponse". Puisque nous avons fait une requête GET à [www.github.com,](http://www.github.com,) le corps contient le contenu de la page HTML pour [www.github.com.](http://www.github.com.)

![Image](https://cdn-media-1.freecodecamp.org/images/0*jobE31EJyQT2-UlD.png)

...Ce qui est, bien sûr, important pour afficher cette page.

#### Exercices supplémentaires

J'espère que cela vous laisse une meilleure compréhension de la structure de HTTP. Pour vous entraîner, vous pouvez jeter un coup d'œil à tous les autres actifs qui sont demandés par votre navigateur (images, fichiers JavaScript, etc.) lorsque vous visitez [www.github.com](http://www.github.com).

![Image](https://cdn-media-1.freecodecamp.org/images/0*GKPupdqLWV3KzxYN.png)

Cela étant dit, examinons les différents types de méthodes HTTP qu'un client peut initier.

### Méthodes HTTP

Les verbes HTTP, ou méthodes, indiquent au serveur quoi faire avec les données identifiées par l'URL. Les URL identifient toujours une ressource spécifique. Lorsqu'un client utilise une URL en combinaison avec un verbe HTTP, cela indique au serveur quelle action doit se produire sur quelle ressource.

Exemples d'URL incluent :

* **GET** [http://www.example.com/users](http://www.example.com/users) (obtenir tous les utilisateurs)
* **POST** [http://www.example.com/users/a-unique-id](http://www.example.com/users/a-unique-id) (créer un nouvel utilisateur)
* **PUT** [http://www.example.com/comments/a-unique-id](http://www.example.com/comments/a-unique-id) (mettre à jour un commentaire)
* **DELETE** [http://www.example.com/comments/a-unique-id](http://www.example.com/comments/a-unique-id) (supprimer un commentaire)

Lorsqu'un client fait une requête, il indiquera le type de requête en utilisant l'un de ces verbes. Les plus importants sont GET, POST, PUT et DELETE. Il existe d'autres méthodes, telles que HEAD et OPTIONS, mais elles sont plus rares, donc nous les sauterons pour cet article.

#### **GET**

GET est la méthode la plus couramment utilisée. Elle est utilisée pour lire les informations d'une URL donnée à partir d'un serveur.

Les requêtes GET sont en lecture seule, ce qui signifie que les données ne doivent jamais être modifiées sur le serveur — le serveur doit simplement récupérer les données inchangées. De cette manière, les requêtes GET sont considérées comme des opérations sûres, car les appeler une fois, ou les appeler 20 fois, aura le même effet.

De plus, les requêtes GET sont **idempotentes**. Cela signifie que l'envoi de plusieurs requêtes GET à la même URL devrait avoir exactement le même effet qu'une seule requête GET, puisque une requête GET demande simplement au serveur des données sans réellement changer de données sur le serveur.

Les requêtes GET répondent avec un code de statut 200 (OK) si la ressource a été trouvée avec succès, et 404 (NOT FOUND) si la ressource n'a pas été trouvée. (D'où le terme "page 404" pour les messages d'erreur lors de la visite d'URL retirées ou mal tapées.)

![Image](https://cdn-media-1.freecodecamp.org/images/1*l6TROCXMdqdCa5ZdD2D_sQ.png)
_La célèbre page 404 de GitHub sur le thème de Star Wars._

#### **POST**

POST est utilisé pour créer une nouvelle ressource, telle qu'un formulaire d'inscription. Vous utilisez POST lorsque vous souhaitez créer une ressource subordonnée (par exemple, un nouvel utilisateur) à une autre ressource parente (http://example.com/users). Votre publication à cette ressource parente est identifiée par l'URL, et le serveur traite la nouvelle ressource et l'associe à la ressource parente.

POST n'est ni sûr ni idempotent. Cela est dû au fait que l'envoi de deux ou plusieurs requêtes POST identiques entraînera probablement la création de deux nouvelles ressources identiques.

Les requêtes POST répondent avec un code de statut 201 (CREATED) ainsi qu'un en-tête de localisation avec le lien vers la ressource nouvellement créée.

#### **PUT**

PUT est utilisé pour mettre à jour la ressource identifiée par l'URL en utilisant les informations dans le corps de la requête. PUT peut également être utilisé pour créer une nouvelle ressource. Les requêtes PUT ne sont pas considérées comme des opérations sûres car elles modifient l'état sur le serveur. Cependant, elles sont idempotentes car plusieurs requêtes PUT identiques pour mettre à jour une ressource devraient avoir le même effet que la première.

Les requêtes PUT répondent avec un code de statut 200 (OK) si la ressource a été mise à jour avec succès, et 404 (NOT FOUND) si la ressource n'a pas été trouvée.

#### **DELETE**

DELETE est utilisé pour supprimer la ressource identifiée par l'URL. Les requêtes DELETE sont idempotentes car si vous supprimez une ressource, elle est supprimée et même si vous envoyez plusieurs requêtes DELETE identiques, le résultat est le même : une ressource supprimée.

Vous obtiendrez probablement simplement un message d'erreur 404 si vous envoyez une requête DELETE plus d'une fois pour la même ressource, car le serveur ne pourra pas la trouver une fois qu'elle a été supprimée.

Les requêtes DELETE répondent avec un code de statut 200 (OK) si la suppression a réussi ou 404 (NOT FOUND) si la ressource à supprimer n'a pas pu être trouvée.

Toutes les requêtes ci-dessus retournent un code 500 (INTERNAL SERVER ERROR) si le traitement échoue et que le serveur rencontre une erreur.

### Qu'est-ce que REST après tout ?

J'ai un dernier terme à couvrir avant de conclure : REST.

Vous avez peut-être entendu le terme "application RESTful" auparavant. Il est important de comprendre ce que cela signifie car si vous utilisez HTTP pour communiquer entre le client et le serveur, il est bénéfique de suivre les directives REST. (En fait, les verbes HTTP que nous avons définis ci-dessus représentent une grande partie de ce qu'est REST.)

REST signifie "Representational State Transfer". C'est un style d'architecture pour concevoir des applications.

L'idée de base est que vous utilisez un protocole "sans état", "client-serveur", "cacheable" pour effectuer des appels entre machines — et le plus souvent, ce protocole est HTTP. Ce n'est qu'une manière sophistiquée de dire que REST vous donne un ensemble de contraintes pour concevoir une application. Ces contraintes aident à rendre le système plus performant, évolutif, simple, modifiable, visible, portable et fiable.

La liste complète des contraintes est longue et vous pouvez en lire plus à ce sujet [ici](https://en.wikipedia.org/wiki/Representational_state_transfer). Pour les besoins de cet article, je voudrais m'attarder sur les deux plus importantes :

1. **Interface uniforme** : Cette contrainte vous indique comment définir l'interface entre le client et le serveur de manière à simplifier et à découpler l'architecture. Elle dit que :

* Les ressources doivent être identifiables dans une requête (par exemple, en utilisant des identifiants de ressource dans l'URI). Une ressource (par exemple, des données dans une base de données) est la donnée qui définit la représentation de la ressource (par exemple, JSON, HTML). Les ressources et les représentations de ressources sont des choses distinctes — le client n'interagit qu'avec la représentation de la ressource.
* Le client doit avoir suffisamment d'informations pour manipuler les ressources sur le serveur en utilisant la représentation de la ressource.
* Chaque message échangé entre le client et le serveur doit être auto-descriptif, avec des informations sur la manière de traiter le message.
* Les clients doivent envoyer des données d'état en utilisant le contenu du corps HTTP, les en-têtes de requête HTTP, les paramètres de requête et l'URL. Les serveurs doivent envoyer des données d'état en utilisant le contenu du corps HTTP, les codes de réponse et les en-têtes de réponse.
* NOTE : Les verbes HTTP que nous avons décrits ci-dessus constituent une grande partie de cette contrainte d'"interface uniforme", car ils représentent les actions uniformes qui se produisent sur les ressources.

**2. Sans état** : Cette contrainte dit que toutes les données d'état nécessaires pour traiter une requête client doivent être contenues dans la requête elle-même (URL, paramètres de requête, corps HTTP ou en-têtes HTTP) et le serveur doit envoyer toutes les données d'état nécessaires au client via la réponse elle-même (en-têtes HTTP, code de statut et corps de réponse HTTP).

**Note de bas de page** : L'état — ou l'état de l'application — est la donnée nécessaire à un serveur pour satisfaire une requête.

Ce que cela signifie, c'est que pour chaque requête, nous renvoyons les informations d'état d'avant en arrière, de sorte que le serveur n'ait pas à maintenir, mettre à jour et envoyer l'état.

Avoir un tel système sans état rend les applications beaucoup plus évolutives, car aucun serveur n'a à se soucier de maintenir le même état de session sur plusieurs requêtes. Tout ce qui est nécessaire pour obtenir les données d'état est disponible dans la requête et la réponse elles-mêmes.

### Remarques de clôture

Ouf ! HTTP est loin d'être simple. Mais comme vous pouvez le voir, c'est un composant critique de la relation client-serveur.

La création d'applications RESTful nécessite au moins une compréhension de base de HTTP. Avec ce contenu sous votre ceinture, vous êtes bien parti pour décrypter les mystères de la communication client-serveur dans votre prochain projet de codage.