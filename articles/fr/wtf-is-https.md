---
title: WTF est HTTPS ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-24T12:43:00.000Z'
originalURL: https://freecodecamp.org/news/wtf-is-https
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/dayne-topkin-78982-unsplash.jpg
tags:
- name: https
  slug: https
- name: Security
  slug: security
- name: technology
  slug: technology
seo_title: WTF est HTTPS ?
seo_desc: 'By Megan Kaczanowski

  Security has a lot of acronyms. What do they mean? Let’s break them down into manageable
  bits.

  First, HTTPS is actually HTTP running with TLS or SSL over it. First, we’ll cover
  HTTP, then TLS and SSL.

  What is HTTP?

  HTTP is what w...'
---

Par Megan Kaczanowski

La sécurité comporte de nombreux acronymes. Que signifient-ils ? Décomposons-les en parties gérables.

Tout d'abord, HTTPS est en fait HTTP fonctionnant avec TLS ou SSL par-dessus. Nous allons d'abord couvrir HTTP, puis TLS et SSL.

### Qu'est-ce que HTTP ?

HTTP est ce que les navigateurs web utilisent pour se connecter aux pages web, images, etc. C'est un protocole textuel sans connexion. La partie sans connexion signifie que chaque fois que le navigateur web doit charger un nouvel élément, une nouvelle connexion doit être établie (au lieu de garder la connexion ouverte tout le temps, comme le font la plupart des protocoles). Un protocole est simplement un ensemble de règles informatiques qui régissent la manière dont les appareils se connectent sur Internet.

Lorsque vous tapez une URL dans un navigateur, l'ordinateur récupère l'adresse IP (c'est le DNS). Ensuite, le navigateur se connecte au serveur et envoie une requête HTTP à la page web. Le serveur web vérifie la page et la charge. Ensuite, le navigateur reçoit la page et ferme la connexion. Le navigateur parcourt ensuite la page pour trouver d'autres parties à charger (comme des images, des applets, etc.). Pour chaque nouvelle partie à charger, le navigateur établit et ferme une autre connexion. Enfin, la page est complètement chargée.

Le problème avec HTTP est qu'il transmet les informations en clair, ce qui signifie que toute personne ayant les compétences techniques pour surveiller le trafic peut voir tout ce qui est transmis (y compris les noms d'utilisateur et les mots de passe). HTTPS offre un chiffrement et une authentification.

Le chiffrement est conçu pour masquer le contenu d'un message à toute personne autre que le destinataire prévu du message. L'idée est de transformer les données de sorte que seule une certaine personne, ou un groupe de personnes, puisse transformer les données en un message reconnaissable.

L'authentification vérifie l'identité. Elle est utilisée pour vérifier que le serveur qui est censé envoyer le message est bien le serveur qui a envoyé le message.

### Qu'est-ce que SSL/TLS ?

Tout d'abord, SSL et TLS font essentiellement la même chose. Mais TLS est une version plus récente du même protocole, avec des protocoles de chiffrement et d'authentification plus robustes.

En gros, TLS utilise le **chiffrement asymétrique** pour établir un lien entre les deux serveurs en utilisant des **clés privées/publiques**. Le chiffrement asymétrique est comme une serrure et une clé, où une personne a la 'serrure' qui chiffre les données, et une deuxième personne a la 'clé' qui déchiffre les données. Les clés publiques et privées sont comme un ensemble serrure et clé où l'une verrouille (chiffre) les données, et l'autre déverrouille (déchiffre) les données.

Après l'initialisation de la session, les serveurs peuvent calculer de manière sécurisée un secret partagé et commencer à communiquer en utilisant le chiffrement symétrique (car il est beaucoup plus rapide et peut transmettre des paquets de données plus grands). Le chiffrement symétrique n'a pas de paire serrure/clé. Au lieu de cela, c'est comme parler à quelqu'un dans un endroit sécurisé (secret partagé). Si l'endroit est sécurisé (c'est-à-dire que vous êtes les seuls à savoir où vous êtes/connaître le secret partagé), vous n'avez pas à vous soucier de protéger des morceaux spécifiques d'informations avec une serrure et une clé.

### Comment fonctionne SSL/TLS ?

SSL/TLS fonctionne via un protocole appelé SSL/TLS Handshake. Voici comment cela fonctionne :

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screen-Shot-2019-06-13-at-4.22.38-PM.png)

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screen-Shot-2019-06-13-at-4.22.47-PM.png)

Le handshake utilise le chiffrement asymétrique pour établir le processus et convenir d'un secret partagé. Ensuite, le handshake passe au chiffrement symétrique plus rapide. La partie 'accepted ciphers' aide simplement les serveurs à convenir d'un protocole commun à utiliser.

<iframe src="https://giphy.com/embed/cI45LEPRoFQhLVq7AB" width="480" height="360" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/skittles-yes-winning-heck-cI45LEPRoFQhLVq7AB">via GIPHY</a></p>

HTTPS est important car il protège l'intégrité du trafic d'un site web. Cela permet à un site web de protéger ses utilisateurs contre les attaquants malveillants qui cherchent à installer des logiciels malveillants ou à voler des données utilisateur, ainsi que contre des tiers comme les FAI qui pourraient être intéressés par l'injection de publicités ou la collecte de données.

HTTPS garantit que les utilisateurs ont une vie privée, et il devient omniprésent, en grande partie grâce à la poussée de Google pour HTTPS. C'est pourquoi sur les sites web avec HTTPS, lorsque vous utilisez un navigateur Chrome, vous verrez un symbole de 'cadenas' (voir ci-dessous).

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screen-Shot-2019-06-18-at-5.31.55-PM-1.png)

Les sites web qui n'ont pas HTTPS afficheront un avertissement rouge vif 'non sécurisé'. De plus, de nombreuses nouvelles fonctionnalités ne sont pas activées sans HTTPS (en particulier pour les applications web progressives). Étant donné à quel point HTTPS est essentiel à la sécurité du web, il est important pour toute personne travaillant dans la sécurité de comprendre pourquoi et comment il fonctionne. Afin de sécuriser les systèmes, vous devez les comprendre.