---
title: Qu'est-ce que le TLS ? Explication en français simple du chiffrement de la
  sécurité de la couche de transport
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2020-09-08T16:39:48.000Z'
originalURL: https://freecodecamp.org/news/what-is-tls-transport-layer-security-encryption-explained-in-plain-english
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/13466286-1BED-4E1F-A3BE-92A971BBF635.jpeg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: Security
  slug: security
- name: TLS
  slug: tls
seo_title: Qu'est-ce que le TLS ? Explication en français simple du chiffrement de
  la sécurité de la couche de transport
seo_desc: "If you want to have a confidential conversation with someone you know,\
  \ you might meet up in person and find a private place to talk. \nBut if you want\
  \ to send data confidentially over the Internet, you might have a few more considerations\
  \ to cover.\nTL..."
---

Si vous souhaitez avoir une conversation confidentielle avec quelqu'un que vous connaissez, vous pourriez vous rencontrer en personne et trouver un endroit privé pour parler. 

Mais si vous souhaitez envoyer des données de manière confidentielle sur Internet, vous pourriez avoir quelques considérations supplémentaires à couvrir.

Le TLS, ou Transport Layer Security, fait référence à un protocole. "Protocole" est un mot qui signifie, "la manière dont nous avons convenu de faire les choses ici", plus ou moins. 

La partie "couche de transport" du TLS fait simplement référence à la communication hôte à hôte, telle que la manière dont un client et un serveur interagissent, dans le [modèle de suite de protocoles Internet](https://en.wikipedia.org/wiki/Internet_protocol_suite).

Le protocole TLS tente de résoudre ces problèmes fondamentaux :

* Comment puis-je savoir que vous êtes bien celui que vous prétendez être ?
* Comment puis-je savoir que ce message de votre part n'a pas été falsifié ?
* Comment pouvons-nous communiquer de manière sécurisée ?

Voici comment fonctionne le TLS, expliqué en français simple. Comme pour de nombreuses interactions réussies, cela commence par une poignée de main.

## Faire connaissance

Le processus de base d'une [poignée de main TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security#TLS_handshake) implique un client, tel que votre navigateur web, et un serveur, tel que celui hébergeant un site web, établissant certaines règles de base pour la communication. 

Cela commence par le client disant bonjour. Littéralement. C'est ce qu'on appelle un message _ClientHello_.

Le message _ClientHello_ indique au serveur quelle version du protocole TLS et quelles _suites de chiffrement_ il prend en charge. 

Bien que "suite de chiffrement" semble être une mise à niveau d'hôtel sophistiquée, cela fait simplement référence à un ensemble d'algorithmes qui peuvent être utilisés pour sécuriser les communications. 

Le serveur, dans un message similaire appelé _ServerHello_, choisit la version du protocole et la suite de chiffrement à utiliser parmi les choix offerts. D'autres données peuvent également être envoyées, par exemple, un _identifiant de session_, si le serveur prend en charge la reprise d'une poignée de main précédente.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/hello-hello.png)
_Dessin animé d'une fenêtre de navigateur et d'un serveur se disant bonjour, par l'auteur._

Selon la suite de chiffrement choisie, le client et le serveur échangent des informations supplémentaires afin d'établir un secret partagé. 

Souvent, ce processus passe de la [cryptographie asymétrique](https://en.wikipedia.org/wiki/Public-key_cryptography) à la [cryptographie symétrique](https://en.wikipedia.org/wiki/Symmetric-key_algorithm) avec différents niveaux de complexité. Explorons ces concepts à un niveau général et voyons pourquoi ils sont importants pour le TLS.

## Débuts asymétriques

Voici l'asymétrie :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image.jpeg)
_Petit œuf, gros œuf._

La cryptographie asymétrique est une méthode par laquelle vous pouvez effectuer une _authentification_. Lorsque vous vous authentifiez, vous répondez à la question fondamentale, "Comment puis-je savoir que vous êtes bien celui que vous prétendez être ?"

Dans un système cryptographique asymétrique, vous utilisez une paire de clés afin de réaliser l'authentification. Ces clés sont asymétriques. Une clé est votre clé publique, qui, comme vous pourriez le deviner, est publique. L'autre est votre clé privée, qui – eh bien, vous savez.

Typiquement, lors de la poignée de main TLS, le serveur fournira sa clé publique via son certificat numérique, parfois encore appelé son _certificat SSL_, bien que le TLS remplace le protocole Secure Sockets Layer (SSL) obsolète. 

Les certificats numériques sont fournis et vérifiés par des tiers de confiance connus sous le nom de [Autorités de Certification (CA)](https://en.wikipedia.org/wiki/Certificate_authority), qui sont un tout autre sujet en eux-mêmes.

Bien que quiconque puisse chiffrer un message en utilisant votre clé publique, seule votre clé privée peut ensuite déchiffrer ce message. 

La sécurité de la cryptographie asymétrique repose uniquement sur le fait que votre clé privée reste privée, d'où l'asymétrie. 

Elle est également asymétrique dans le sens où c'est un voyage à sens unique. Alice peut envoyer des messages chiffrés avec votre clé publique, mais aucune de vos clés ne vous aidera à envoyer un message chiffré à Alice.

## Secrets symétriques

La cryptographie asymétrique nécessite également plus de ressources computationnelles que la cryptographie symétrique. 

Ainsi, lorsqu'une poignée de main TLS commence par un échange asymétrique, le client et le serveur utiliseront cette communication initiale pour établir un secret partagé, parfois appelé _clé de session_. Cette clé est symétrique, ce qui signifie que les deux parties utilisent le même secret partagé et doivent maintenir ce secret pour que le chiffrement soit sécurisé.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-11.png)
_Une personne sage dit : partagez votre clé publique, mais gardez vos clés partagées privées._

En utilisant la communication asymétrique initiale pour établir une clé de session, le client et le serveur peuvent s'assurer que la clé de session est connue d'eux seuls. Pour le reste de la session, ils utiliseront tous les deux cette même clé partagée pour chiffrer et déchiffrer les messages, ce qui accélère la communication.

## Sessions sécurisées

Une poignée de main TLS peut utiliser la cryptographie asymétrique ou d'autres suites de chiffrement pour établir la clé de session partagée. Une fois la clé de session établie, la partie poignée de main est terminée et la session commence.

La _session_ est la durée de la communication chiffrée entre le client et le serveur. Pendant cette période, les messages sont chiffrés et déchiffrés en utilisant la clé de session que seul le client et le serveur possèdent. Cela garantit que la communication est sécurisée.

L'intégrité des informations échangées est maintenue en utilisant une somme de contrôle. Les messages échangés en utilisant les clés de session ont un [code d'authentification de message (MAC)](https://en.wikipedia.org/wiki/Message_authentication_code) attaché. Ce n'est pas la même chose que l'[adresse MAC](https://en.wikipedia.org/wiki/MAC_address) de votre appareil. Le MAC est généré et vérifié en utilisant la clé de session. 

Grâce à cela, l'une ou l'autre des parties peut détecter si un message a été modifié avant d'être reçu. Cela résout la question fondamentale, "Comment puis-je savoir que ce message de votre part n'a pas été falsifié ?"

Les sessions peuvent se terminer délibérément, en raison d'une déconnexion du réseau, ou parce que le client est resté inactif trop longtemps. Une fois une session terminée, elle doit être rétablie via une nouvelle poignée de main ou par le biais de secrets précédemment établis appelés _identifiants de session_ qui permettent de reprendre une session.

## TLS et vous

Faisons un récapitulatif :

* Le TLS est un protocole cryptographique pour fournir une communication sécurisée.
* Le processus de création d'une connexion sécurisée commence par une poignée de main.
* La poignée de main établit une clé de session partagée qui est ensuite utilisée pour sécuriser les messages et fournir l'intégrité des messages.
* Les sessions sont temporaires et, une fois terminées, doivent être rétablies ou reprises.

Ce n'est qu'un aperçu de surface des systèmes cryptographiques très complexes qui aident à garder vos communications sécurisées. Pour plus de détails sur le sujet, je recommande d'explorer les suites de chiffrement et les divers [algorithmes pris en charge](https://en.wikipedia.org/wiki/Cipher_suite#Supported_algorithms).

Le protocole TLS joue un rôle très important dans votre vie quotidienne. Il aide à sécuriser vos e-mails à votre famille, vos activités bancaires en ligne et la connexion par laquelle vous lisez cet article. 

Le [protocole de communication HTTPS](https://en.wikipedia.org/wiki/HTTPS) est chiffré en utilisant le TLS. Chaque fois que vous voyez cette petite icône de cadenas dans votre barre d'URL, vous faites l'expérience en direct de tous les concepts que vous venez de lire dans cet article. 

Vous connaissez donc maintenant la réponse à la dernière question : "Comment pouvons-nous communiquer de manière sécurisée ?"

## Heading Installation

Pour installer TLS, suivez ces étapes :

1. **Générez une clé privée** : Utilisez OpenSSL pour générer une clé privée.
   ```bash
   openssl genpkey -algorithm RSA -out private_key.pem
   ```

2. **Générez un certificat** : Créez un certificat auto-signé pour les tests.
   ```bash
   openssl req -new -x509 -key private_key.pem -out certificate.pem -days 365
   ```

3. **Configurez votre serveur** : Intégrez le certificat et la clé dans votre serveur web.

   Pour Apache, ajoutez ces lignes à votre fichier de configuration :
   ```apache
   SSLEngine on
   SSLCertificateFile /chemin/vers/certificate.pem
   SSLCertificateKeyFile /chemin/vers/private_key.pem
   ```

   Pour Nginx, utilisez ce bloc de configuration :
   ```nginx
   server {
       listen 443 ssl;
       server_name votre-domaine.com;
       ssl_certificate /chemin/vers/certificate.pem;
       ssl_certificate_key /chemin/vers/private_key.pem;
   }
   ```

4. **Redémarrez votre serveur** : Appliquez les modifications en redémarrant votre serveur.

   Pour Apache :
   ```bash
   sudo systemctl restart apache2
   ```

   Pour Nginx :
   ```bash
   sudo systemctl restart nginx
   ```

5. **Testez votre configuration** : Vérifiez que TLS est correctement configuré en visitant votre site avec `https://`.

   Vous pouvez également utiliser des outils comme [SSL Labs](https://www.ssllabs.com/ssltest/) pour analyser votre configuration.

💡 **Conseil** : Pour une sécurité optimale, utilisez des certificats signés par une autorité de certification (CA) reconnue plutôt que des certificats auto-signés.

✨ **Félicitations** ! Vous avez maintenant une connexion sécurisée avec TLS.

Pour plus d'informations, consultez la [documentation officielle](https://en.wikipedia.org/wiki/Transport_Layer_Security).