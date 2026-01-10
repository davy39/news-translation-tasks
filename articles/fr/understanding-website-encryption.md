---
title: Comment fonctionne le chiffrement des sites web
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-03-28T17:35:27.000Z'
originalURL: https://freecodecamp.org/news/understanding-website-encryption
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/pexels-markus-spiske-225769.jpg
tags:
- name: encryption
  slug: encryption
- name: Security
  slug: security
seo_title: Comment fonctionne le chiffrement des sites web
seo_desc: It's one thing to protect your data when it's sitting quietly on your own
  local machine and not bothering anyone. But moving data between locations – as you
  do whenever you open a website on a remote server or send an email attachment across
  the inte...
---

C'est une chose de protéger vos données lorsqu'elles sont stockées tranquillement sur votre propre machine locale sans déranger personne. Mais le transfert de données entre différents emplacements – comme vous le faites chaque fois que vous ouvrez un site web sur un serveur distant ou que vous envoyez une pièce jointe par e-mail sur Internet – introduit un tout nouvel ensemble de vulnérabilités.

Les protocoles en texte clair transmettent les données sous leur forme non chiffrée, ce qui les rend vulnérables à l'écoute clandestine et à l'altération par des tiers. Les données transmises via des protocoles en texte clair peuvent être facilement interceptées et lues par quiconque ayant accès au réseau.

Si vous envisagez de transmettre, par exemple, des informations de carte de crédit ou de saisir des mots de passe de banque en ligne de cette manière, je vous supplie d'arrêter immédiatement. Vous voulez absolument ajouter une dose de chiffrement à l'ensemble.

Cet article est extrait de [The Complete LPI Security Essentials Exam Study Guide](https://www.udemy.com/course/complete-lpi-security-essentials-exam-study-guide/?referralCode=C2B6802EDB99578238B5). Vous pouvez également suivre le contenu à l'aide de cette vidéo :

%[https://www.youtube.com/watch?v=v3Z0IRzTEcY&list=PLSiZCpRYoTZ7wEwmKRsRjaQF3qSi4bbdl&index=1]

## Quelques protocoles de chiffrement clés

Les protocoles de chiffrement de transport, comme on peut le constater, utilisent des techniques de chiffrement pour protéger les données pendant le transit. Les données sont chiffrées avant d'être transmises et déchiffrées après avoir été reçues. Cela offre une protection contre l'écoute clandestine et l'altération par des tiers.

Les protocoles de chiffrement de transport les plus courants sont le Secure Sockets Layer (SSL) et son successeur, le Transport Layer Security (TLS).

Au-delà du chiffrement de transport, le chiffrement de bout en bout (E2EE) désigne une méthode de chiffrement des données de l'appareil de l'expéditeur vers l'appareil du destinataire, de telle sorte que seuls l'expéditeur et le destinataire ont accès aux données.

L'E2EE assure la protection de l'intégralité de la transmission, y compris contre les intermédiaires tels que les administrateurs réseau, les fournisseurs de services et les pirates. L'E2EE est généralement utilisé dans des applications telles que la messagerie instantanée, le courrier électronique et le partage de fichiers.

[HTTPS (Hypertext Transfer Protocol Secure)](https://www.freecodecamp.org/news/what-is-https-http-vs-https-meaning-and-how-it-works/) est un protocole couramment utilisé pour sécuriser les pages web. Il utilise le chiffrement SSL ou TLS pour sécuriser la connexion entre un navigateur web et un serveur, garantissant que les informations sensibles, telles que les identifiants de connexion et les numéros de carte de crédit, ne puissent pas être interceptées par des tiers.

[TLS (Transport Layer Security)](https://www.freecodecamp.org/news/what-is-tls-transport-layer-security-encryption-explained-in-plain-english/) est un protocole de sécurité qui assure le chiffrement et l'intégrité de la transmission des données sur Internet. C'est le successeur de SSL et il est actuellement largement utilisé pour sécuriser les connexions web, les e-mails et d'autres protocoles Internet. TLS utilise la cryptographie à clé publique pour négocier une clé secrète partagée, qui est ensuite utilisée pour chiffrer les données.

## Comment identifier le chiffrement d'un site web

Vous pouvez identifier si un site web est chiffré en cherchant l'icône du cadenas et le préfixe « https » dans l'URL du site. L'icône du cadenas est généralement située dans la barre d'adresse de votre navigateur web et indique que la connexion entre votre navigateur et le site web est sécurisée.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-28-at-10.11.06-AM.png)
_Le cadenas montrant que freecodecamp.org/news est sécurisé_

L'icône du cadenas peut également indiquer le niveau de sécurité, comme le type de chiffrement utilisé, l'identité du site web et la validité du certificat SSL/TLS.

Le préfixe « https » dans l'URL du site web indique que la connexion est chiffrée et sécurisée. Le « s » dans « https » signifie « secure » (sécurisé). En revanche, les sites web non chiffrés utilisent le préfixe « http » dans leur URL.

Il est important de noter que bien que l'icône du cadenas et le préfixe « https » indiquent qu'un site web est chiffré, ils ne garantissent pas l'authenticité ou la sécurité du site. Soyez toujours prudent lorsque vous saisissez des informations sensibles, telles que des identifiants de connexion ou des numéros de carte de crédit, sur n'importe quel site web, et assurez-vous de vérifier l'identité du site avant de saisir toute information sensible.

Les sites web chiffrés par TLS peuvent obtenir des cadenas et le préfixe « HTTPS » en demandant un certificat à une autorité de certification. Autrefois, les AC facturaient des sommes importantes pour l'émission de certificats, et elles prenaient également leur temps. Cependant, c'était avant Let's Encrypt.

[Let's Encrypt](https://letsencrypt.org/) est une autorité de certification à but non lucratif qui fournit des certificats SSL/TLS gratuits, automatisés et open source. Ces certificats sont utilisés pour chiffrer et sécuriser les communications web, offrant confidentialité et intégrité des données aux utilisateurs d'Internet.

La principale valeur de Let's Encrypt est sa capacité à rendre le chiffrement plus accessible et abordable. En proposant des certificats SSL/TLS gratuits, Let's Encrypt permet aux propriétaires de sites web de sécuriser plus facilement et à moindre coût leurs sites et de protéger la vie privée de leurs utilisateurs.

En plus d'être gratuits, les certificats Let's Encrypt sont également faciles à obtenir et à installer. Les certificats sont émis via [un processus automatisé](https://certbot.eff.org/), ce qui permet aux propriétaires de sites web d'obtenir un certificat en quelques minutes, plutôt que d'attendre des jours ou des semaines pour un traitement manuel.

## Comprendre les certificats X.509

Comprenons un peu mieux ces certificats. X.509 est une norme pour les certificats numériques largement utilisée sur Internet pour établir la confiance entre les parties.

Un certificat X.509 est un document numérique qui contient des informations sur l'identité d'une entité et qui est signé par un tiers de confiance appelé autorité de certification (AC).

![Image](https://www.freecodecamp.org/news/content/images/2023/03/slide-31-1.png)
_Schéma du fonctionnement des certificats X.509_

Le processus d'obtention d'un certificat X.509 implique de passer par plusieurs étapes :

* L'entité demandant le certificat (un propriétaire de site web, par exemple) génère une demande de signature de certificat (CSR) qui comprend des informations sur son identité et sa clé publique.
* L'AC vérifie l'identité de l'entité et délivre le certificat X.509. Le certificat contient la clé publique de l'entité, des informations sur son identité et la signature de l'AC.
* L'entité installe le certificat sur son serveur web et configure son site pour utiliser le protocole HTTPS, ce qui permet une communication chiffrée entre le serveur et le client.

Le processus de révocation d'un certificat X.509 comprend les étapes suivantes :

* L'entité ou l'AC détecte que le certificat doit être révoqué. Par exemple, l'entité peut avoir perdu le contrôle de sa clé privée, ou les informations d'identité dans le certificat peuvent avoir changé.
* L'entité ou l'AC demande la révocation du certificat.
* L'AC met à jour sa liste de révocation de certificats (CRL) pour indiquer que le certificat a été révoqué. La CRL est une liste de tous les certificats révoqués émis par l'AC.
* Lorsqu'un client se connecte à un site web, il vérifie le certificat par rapport à la CRL pour s'assurer qu'il n'a pas été révoqué. Si le certificat a été révoqué, le client ne fera pas confiance au site web et n'établira pas de connexion sécurisée.

Un certificat X.509 contient plusieurs champs clés qui fournissent des informations sur l'identité de l'entité et sur le certificat lui-même. Certains de ces champs clés sont :

* Le numéro de version du format de certificat X.509.
* Un identifiant unique attribué au certificat par l'autorité de certification (AC).
* Des informations sur l'entité que le certificat représente, telles que son nom, son adresse et sa clé publique.
* Des informations sur l'AC qui a délivré le certificat, telles que son nom et son adresse.
* Les dates de début et de fin de la période de validité du certificat, pendant laquelle le certificat peut être considéré comme fiable.
* La clé publique de l'entité que le certificat représente.
* L'algorithme utilisé par l'AC pour signer le certificat et vérifier son authenticité.
* La signature de l'AC, qui est utilisée pour vérifier l'authenticité du certificat.

## Confidentialité persistante (PFS)

Il reste une chose que nous devrions aborder avant de quitter le monde des sessions web chiffrées. La confidentialité persistante (Perfect Forward Secrecy - PFS) est une propriété de sécurité en cryptographie qui garantit que la confidentialité des sessions passées ne peut pas être compromise, même si les clés de chiffrement utilisées dans ces sessions sont divulguées ultérieurement.

Ceci est réalisé en utilisant des clés éphémères, qui sont générées pour chaque session et supprimées une fois la session terminée. Les clés éphémères sont utilisées pour établir un échange de clés sécurisé et ne sont jamais stockées, de sorte qu'elles ne peuvent pas être utilisées pour déchiffrer des sessions passées même si elles sont divulguées plus tard.

La PFS est une propriété importante dans les protocoles de communication sécurisés, car elle garantit que même si un attaquant parvient à obtenir les clés de chiffrement pour une seule session, il ne pourra pas utiliser ces clés pour compromettre les sessions passées ou futures.

## Conclusion

Grâce à cette connaissance du fonctionnement interne du chiffrement, vous serez mieux à même d'évaluer la sécurité de vos activités de navigation sur Internet. Vous saurez également ce que vous devez faire pour chiffrer les sites web que vous pourriez gérer vous-même.

Cet article et la vidéo qui l'accompagne sont extraits de mon cours [Complete LPI Security Essentials Exam Study Guide](https://www.udemy.com/course/complete-lpi-security-essentials-exam-study-guide/?referralCode=C2B6802EDB99578238B5). Et bien d'autres ressources technologiques sont disponibles sur [bootstrap-it.com](https://bootstrap-it.com/)