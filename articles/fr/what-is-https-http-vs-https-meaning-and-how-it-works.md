---
title: 'Qu''est-ce que HTTPS ? HTTP vs HTTPS : signification et fonctionnement'
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-08-16T13:57:44.000Z'
originalURL: https://freecodecamp.org/news/what-is-https-http-vs-https-meaning-and-how-it-works
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/john-salvino-bqGBbLq_yfc-unsplash.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: http
  slug: http
- name: https
  slug: https
- name: Security
  slug: security
seo_title: 'Qu''est-ce que HTTPS ? HTTP vs HTTPS : signification et fonctionnement'
seo_desc: 'Have you ever noticed the "HTTP" or "HTTPS" at the beginning of a URL in
  your browser? Well, what is HTTP and what is HTTPS? How are they different?

  In order to understand the differences, it helps to demistify to meaning of these
  two terms and under...'
---

Avez-vous déjà remarqué le "HTTP" ou "HTTPS" au début d'une URL dans votre navigateur ? Eh bien, qu'est-ce que HTTP et qu'est-ce que HTTPS ? En quoi sont-ils différents ?

Pour comprendre les différences, il est utile de démystifier la signification de ces deux termes et de comprendre comment chacun fonctionne.

## Qu'est-ce que HTTP ?

HTTP signifie **H**yper**T**ext **T**ransfer **P**rotocol et est le fondement du World Wide Web. Sans lui, le Web ne serait pas ce qu'il est aujourd'hui.

Une URL HTTP commence par `http://` et utilise par défaut le port 80.

La partie *HyperText* du nom signifie qu'il y a des documents ou des fichiers impliqués. Ceux-ci peuvent contenir du texte, des images, des graphiques, des vidéos ou tout autre média.

De plus, ils contiennent probablement des liens vers d'autres documents ou fichiers pour des références croisées, auxquels vous pouvez facilement accéder après avoir cliqué sur le lien avec une souris ou un pavé tactile, ou après l'avoir touché sur l'écran de votre téléphone.

La partie *Transfer* du nom signifie que les fichiers peuvent se déplacer sur le World Wide Web d'un appareil réseau à un autre.

La partie *Protocol* signifie qu'il consiste en un ensemble de règles informatiques qui régissent la manière dont les appareils peuvent utiliser Internet. Il leur indique également comment ils peuvent utiliser Internet comme moyen de communication lorsqu'ils sont connectés à de nombreux autres appareils à distance.

HTTP est construit sur le dessus de la suite de protocoles réseau TCP/IP et sur le dessus d'autres couches dans la pile de protocoles.

Le TCP/IP est un ensemble standardisé de règles pour la manière dont les navigateurs et les serveurs sont autorisés à communiquer sur Internet. Après tout, le World Wide Web est tout au sujet de la communication entre les navigateurs et les serveurs.

Plus précisément, HTTP est un protocole de couche application et est le protocole principal utilisé pour la communication et le transfert de données entre un client web et un serveur web.

En résumé, HTTP est un ensemble de règles et de normes pour la manière dont les fichiers hypertexte et toutes sortes d'informations sont transférés sur le web. C'est ainsi que les navigateurs et les serveurs communiquent.


## Un flux typique de requête et de réponse HTTP

HTTP est utilisé lorsque les navigateurs veulent se connecter à des sites web.

Ils communiquent en envoyant des requêtes HTTP et en recevant des réponses HTTP. Cela est connu sous le nom de *Cycle Requête - Réponse* dans un modèle de calcul client - serveur web.

![Screenshot-2021-08-11-at-3.17.23-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-11-at-3.17.23-PM.png)

Le client, qui est généralement un navigateur web comme Google Chrome, Mozilla Firefox ou Apple Safari, fait la requête. Il le fait en entrant une URL conviviale comme `freecodecamp.org` dans la barre d'adresse en haut du navigateur.

Ce nom de domaine, `freecodecamp.org`, est mappé à une adresse IP [avec l'aide du Domain Name System (DNS)](https://www.freecodecamp.org/news/what-is-dns/).

Le navigateur web se connecte ensuite au serveur et fait une requête HTTP, demandant les informations dont il a besoin pour recevoir afin de charger une page web.

Une requête HTTP peut ressembler à ceci :

```
GET / HTTP/1.1
Host: www.freecodecamp.org
```

Elle se compose de :

- Une méthode HTTP, souvent appelée verbe HTTP, comme `GET`. Ce verbe spécifique est utilisé pour *obtenir* des informations en retour. Un autre verbe courant est `POST`, qui est utilisé lorsque le client soumet des données dans un formulaire. Les verbes spécifient l'action que les navigateurs attendent du serveur.
- Le chemin, qui dans notre exemple est `/`, le chemin *racine*. Le serveur stocke tous les fichiers qui composent un site web, donc une requête doit spécifier quelle partie le navigateur demande à charger.
- Le type HTTP et sa version.
- Le nom de domaine de l'URL.

Le serveur web reçoit ensuite la requête et la traite en recherchant les données demandées.

Un serveur est un ordinateur différent de ceux que nous utilisons au quotidien. Son seul but est de stocker des données et des fichiers et de les récupérer et de les distribuer lorsqu'ils sont demandés.

Le serveur retourne un message, ou une *Réponse* HTTP, au navigateur.

Un exemple de réponse est : `HTTP/1.1 200 OK`

- Il commence d'abord par le protocole et la version `HTTP/1.1`
- Ensuite, le *code de statut* HTTP, un nombre à 3 chiffres, qui dans ce cas est `200`. Il indique si la requête HTTP a été complétée ou non. Les codes de statut commençant par `2` indiquent un succès et que la requête a été complétée avec succès. Les codes de statut commençant par `4`, comme `404`, indiquent une erreur côté client (par exemple, une faute de frappe dans l'URL) donc la page n'est pas affichée dans le navigateur. Un code de statut commençant par `5` signifie une erreur côté serveur et à nouveau la page n'est pas affichée dans le navigateur.
- Ensuite, le *texte de statut*, un texte lisible par l'homme, qui résume la signification du code de statut. Dans ce cas, c'est "OK", ce qui signifie une récupération réussie du document demandé.

Une réponse HTTP comprend également des en-têtes qui peuvent ressembler à ceci :

```
date: Thu, 12 Aug 2021 12:07:16 GMT
server: cloudflare
content-type: text/html; charset=utf-8
```

Les en-têtes incluent des informations importantes sur le type de contenu renvoyé, telles que la langue, le format et le moment où la réponse a été envoyée.

Enfin, une réponse à une requête 'GET' comprend le *corps HTTP* facultatif. Cela contient les informations demandées, comme les fichiers HTML/CSS/JavaScript qui composent le site web.

Ensuite, le navigateur reçoit la réponse, rend la page et ferme la connexion.

Chaque fois qu'il doit charger un nouvel élément sur une page (comme différents styles, images ou vidéos), il démarrera une nouvelle connexion et le processus entier se répète.

## Limites de HTTP

HTTP est rapide grâce à sa simplicité, mais il ne fournit pas de sécurité lors de l'échange de données. Cela est dû au fait que toutes les données sont transmises en **texte brut** et rien n'est crypté.

Lors du transfert, les données hypertexte sont décomposées en 'paquets', et toute personne disposant des bons outils, compétences et connaissances entre le navigateur et le serveur peut facilement visualiser et voler les informations transmises.

Cela signifie que les noms d'utilisateur, les mots de passe et les informations sensibles risquent d'être accessibles aux attaquants, tandis que le risque d'injection de virus est élevé.

Cela signifie que HTTP n'est pas un support sécurisé ou privé, ce qui rend les utilisateurs peu sûrs.

HTTP est sûr pour certains sites, comme les blogs, mais vous ne devez pas soumettre d'informations de carte de crédit ou d'autres informations personnelles via une connexion HTTP.


## Qu'est-ce que HTTPS ?

HTTPS signifie **H**yper**T**ext **T**ransfer **P**rotocol **S**ecure.

Une URL HTTPS commence par `https://` et utilise le port 443 par défaut.

Ce n'est pas un protocole séparé de HTTP, mais c'est la version plus *sécurisée* et confidentielle de celui-ci. C'est le moyen le plus sûr de transférer des données entre un navigateur et un serveur.

La plupart des sites web utilisent aujourd'hui HTTPS plutôt que HTTP. Donc, avant de soumettre des informations sensibles comme se connecter à votre compte bancaire et effectuer des transactions financières, assurez-vous toujours que le site utilise HTTPS.

Vous pouvez savoir si un site est sécurisé et dispose d'une connexion HTTPS grâce à l'icône de cadenas sur le côté gauche de la barre d'adresse :

![Screenshot-2021-08-11-at-6.41.08-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-11-at-6.41.08-PM.png)

![Screenshot-2021-08-12-at-7.38.33-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-12-at-7.38.33-PM.png)

Contrairement à HTTP qui fonctionne sur la couche Application, HTTPS fonctionne sur la couche Transport.

## Comment fonctionne HTTPS ?

Chaque paquet de données envoyé via une connexion HTTPS est *crypté* et sécurisé, en utilisant des protocoles cryptographiques tels que TLS ou SSL, par-dessus HTTP.

Transport Layer Security (TLS), anciennement connu sous le nom de Secure Sockets Layer (SSL), est le protocole utilisé pour crypter les communications. Il s'agit de la version plus récente et plus sécurisée de SSL.

TLS offre une sécurité contre les attaques, et ses trois principaux objectifs sont l'authentification, la confidentialité et la sécurité globale.

TLS sécurise les communications en utilisant un algorithme de clé asymétrique, Public Key Infrastructure (PKI). Ce système utilise deux clés uniques pour crypter et décrypter les informations sensibles, permettant une communication sécurisée sur Internet.

Les deux clés sont utilisées conjointement, et de cette manière, TLS crée un lien entre l'expéditeur et le destinataire. Il s'assure que les deux parties sont identifiées et sont vraiment celles qu'elles prétendent être.

Tout d'abord, vous avez la clé **publique**. Elle est disponible pour être vue publiquement et peut être partagée avec tout le monde et quiconque souhaite interagir avec le site.

Cette clé est utilisée pour transformer le texte brut en texte chiffré, pour crypter les données, et agit comme un cadenas pour crypter les données. Elle confirme également le propriétaire d'une clé privée. La distribution des clés publiques aux navigateurs est effectuée avec des certificats.

Ensuite, chaque clé publique a une clé **privée** unique et elles fonctionnent par paire. Vous utilisez cette clé pour décrypter les informations. Les données cryptées avec une clé publique ne peuvent être décryptées que par la clé privée unique correspondante.

C'est cette clé privée unique qui déverrouille le cadenas et décrypte les données. Une clé privée confirme également que les informations vous appartiennent. Cette clé est gardée privée, stockée et disponible uniquement pour son propriétaire.

Une connexion sécurisée est établie et les certificats sont échangés avant tout transfert de données réel.

Le client tape l'URL de la page web qu'il souhaite accéder. Le serveur de la page web envoie le certificat TLS ou SSL contenant la clé publique pour démarrer la connexion. Le client et le serveur échangent beaucoup d'informations (appelé une poignée de main TLS/SSL) jusqu'à ce qu'ils établissent une session sécurisée.


## Conclusion

Dans cet article, nous avons appris ce qu'est HTTPS, comment il fonctionne et en quoi il est différent (et plus sécurisé) que HTTP.

Pour résumer, HTTPS est la version sécurisée de HTTP, le protocole réseau de base pour envoyer de l'hypertexte sur le web.

Dans HTTPS, il y a des étapes supplémentaires pour la sécurité, telles que les certificats TLS/SSL et la poignée de main TLS/SSL.

Il fournit une authentification pour les utilisateurs et les données, s'assurant que les transactions restent privées (avec l'intégrité des données comme priorité) sans craindre une violation de données lors de la communication client-serveur.

Le contenu des messages et des transactions ne peut être vu que par l'expéditeur et le destinataire prévu.

Merci d'avoir lu !