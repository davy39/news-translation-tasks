---
title: Comment protéger votre PWA – Bonnes pratiques de sécurité pour les applications
  web
subtitle: ''
author: Rahul
co_authors: []
series: null
date: '2023-04-17T21:28:20.000Z'
originalURL: https://freecodecamp.org/news/how-to-protect-your-pwa
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/pwa.png
tags:
- name: progressive web app
  slug: progressive-web-app
- name: PWA
  slug: pwa
- name: Security
  slug: security
seo_title: Comment protéger votre PWA – Bonnes pratiques de sécurité pour les applications
  web
seo_desc: Hey, everybody! I'm Rahul. In today's world, web apps have become more prevalent
  because they work seamlessly on multiple devices. But as with any application, PWAs
  can be vulnerable to security threats, which can compromise user data and damage
  the ...
---

Hey tout le monde ! Je suis [Rahul](https://fueler.io/rahoool). Dans le monde d'aujourd'hui, les applications web sont devenues plus répandues car elles fonctionnent de manière transparente sur plusieurs appareils. Mais comme pour toute application, les PWA peuvent être vulnérables aux menaces de sécurité, ce qui peut compromettre les données des utilisateurs et nuire à la réputation.

Il est naturel de s'enthousiasmer pour le lancement de quelque chose de nouveau, mais il est également important de se rappeler les bases de la sécurité des sites web. En tant que développeur, vous savez qu'il est important de protéger votre application web des utilisateurs malveillants, des attaquants, des pirates et d'autres cybermenaces.

Vous avez travaillé dur pour créer l'expérience utilisateur parfaite et il est maintenant temps de la sécuriser.

Dans ce tutoriel, nous allons passer en revue quelques stratégies simples mais puissantes qui vous aident à protéger votre PWA. Commençons !

# Qu'est-ce qu'une PWA ?

![Illustration PWA par undraw.co](https://www.freecodecamp.org/news/content/images/2023/04/undraw_progressive_app_m-9-ms.svg)
_Illustration PWA par undraw.co_

Êtes-vous intéressé à offrir une expérience d'application mobile native à vos utilisateurs sans les tracas du développement d'applications ? Les applications web progressives (PWA) sont la solution.

Les PWA sont un type d'application web qui utilise les dernières technologies web pour offrir une expérience utilisateur similaire à celle d'une application mobile native.

Elles sont conçues pour tirer parti des fonctionnalités des appareils mobiles natifs et fonctionnent pour les applications, indépendamment du fait que l'utilisateur ait une connexion Internet mauvaise ou inexistante.

De plus, les PWA sont fiables, rapides et engageantes — et elles sont plus faciles à développer et à maintenir que les applications traditionnelles.

Le meilleur aspect des PWA est qu'elles offrent la même expérience sur tous les principaux navigateurs comme Chrome, Firefox, Edge et Safari — vous n'avez donc pas à vous soucier des problèmes de compatibilité.

De plus, comme les PWA ne nécessitent pas d'installation depuis un magasin d'applications, les utilisateurs n'ont pas à attendre que leur fabricant d'appareils les approuve ou les met à jour.

Tous ces facteurs font des PWA une solution idéale pour les entreprises à la recherche de solutions mobiles rentables.

# Comment sécuriser une PWA

## Authentification et autorisation dans les PWA

![Image](https://www.freecodecamp.org/news/content/images/2023/04/undraw_authentication_re_svpt.svg)
_Illustration d'authentification par undraw.co_

Si vous développez une application web progressive (PWA), vous devez vous assurer qu'elle est correctement sécurisée. Pour ce faire, vous devez comprendre les bases de l'authentification et de l'autorisation.

L'authentification est le processus par lequel les utilisateurs prouvent leur identité et vérifient qu'ils ont l'autorisation appropriée pour accéder à l'application.

L'autorisation, en revanche, garantit que ces utilisateurs ont accès uniquement aux zones et au contenu qu'ils sont autorisés à voir, tout en appliquant des restrictions sur ce qu'ils peuvent faire.

Pour mettre en œuvre une authentification et une autorisation efficaces au sein de votre PWA, voici quelques bonnes pratiques à suivre.

1. Tout d'abord, utilisez des mots de passe sécurisés qui sont difficiles à deviner ou à craquer pour les pirates ou les bots, ainsi que l'authentification à deux facteurs (2FA) pour une sécurité supplémentaire.
2. Ensuite, utilisez un contrôle d'accès basé sur les rôles (RBAC) pour l'autorisation. Cela établit les permissions des utilisateurs en fonction des rôles, qui peuvent être rapidement ajustées si nécessaire.
3. Enfin, utilisez HTTPS avec un chiffrement SSL/TLS pour tout le trafic web de votre PWA. Cela garantira que toutes les données envoyées entre les clients et les serveurs sont chiffrées, protégeant les informations des utilisateurs contre les acteurs malveillants.

Il est important de garder à l'esprit que l'authentification et l'autorisation peuvent également être vulnérables aux attaques de la part d'utilisateurs malveillants si elles ne sont pas mises en œuvre correctement. Il est donc essentiel de rester conscient des vecteurs d'attaque courants comme les menaces d'injection SQL et les attaques par scripts inter-sites (XSS).

En mettant en œuvre des mesures de sécurité appropriées telles que la validation des entrées et les tests de pénétration, vous pouvez protéger votre PWA contre ces menaces.

## Comment utiliser HTTPS et SSL/TLS pour sécuriser vos PWA

HTTPS et SSL/TLS sont deux des outils les plus importants lorsqu'il s'agit de sécuriser les PWA.

Voyons ce qu'ils sont exactement :

### Qu'est-ce que HTTPS ?

HTTPS signifie Hyper Text Transfer Protocol Secure. C'est un protocole utilisé pour une communication sécurisée entre un serveur web et un navigateur web, et il est vital pour protéger les données contre l'interception par des tiers.

En termes simples, HTTPS aide à garantir que les données que vous envoyez et recevez de votre PWA sont toujours sécurisées.

### Qu'est-ce que SSL/TLS ?

SSL (Secure Sockets Layer) et [TLS (Transport Layer Security)](https://www.freecodecamp.org/news/what-is-tls-transport-layer-security-encryption-explained-in-plain-english/) sont des protocoles cryptographiques qui fournissent une authentification, un chiffrement et une intégrité des données.

Ces protocoles permettent des connexions sécurisées entre les navigateurs web, les applications et les serveurs via Internet via un processus de poignée de main chiffré.

Ainsi, ils jouent un rôle important dans la garantie que les données de votre application web restent sûres et sécurisées.

### Bonnes pratiques pour la mise en œuvre de HTTPS et SSL/TLS dans les PWA

Pour protéger efficacement votre PWA, vous devez vous assurer que vous suivez certaines bonnes pratiques pour la mise en œuvre de HTTPS et SSL/TLS dans les PWA :

1. Utilisez HTTPS partout : Assurez-vous que toutes vos pages sont servies via HTTPS, plutôt que via des connexions HTTP non sécurisées. Cela aidera à garantir que les données de vos utilisateurs sont protégées lorsqu'ils sont sur votre site web ou votre application.
2. Installez un certificat SSL : Cela permettra les connexions HTTPS sur votre site et fournira une authentification entre le serveur hébergeant votre PWA et les utilisateurs qui le visitent.
3. Testez régulièrement les connexions : Assurez-vous que toutes vos connexions sont toujours sécurisées en les testant régulièrement pour détecter toute vulnérabilité ou risque pour la sécurité.
4. Mettez en œuvre l'épinglage de certificat : L'épinglage de certificat est une mesure de sécurité importante qui consiste à lier un domaine hôte à un certificat SSL spécifique. Cela empêche les attaques de type **man-in-the-middle** et aidera à protéger votre PWA contre les acteurs malveillants.
5. Mettez à jour vos protocoles de sécurité : Mettez régulièrement à jour les protocoles de sécurité de votre serveur web pour vous assurer que vous utilisez toujours la version la plus sécurisée.
6. Configurez des règles de pare-feu appropriées : Configurez les règles de votre pare-feu pour permettre uniquement les connexions sécurisées et bloquer tout trafic suspect. Cela aidera à protéger votre PWA contre les attaques malveillantes.

Une fois que vous avez mis en œuvre ces bonnes pratiques, vous pouvez être assez confiant que votre PWA est aussi sécurisée que possible.

Mais, [la sécurité ne consiste pas seulement à prévenir les attaques malveillantes](https://www.freecodecamp.org/news/attacks-on-ssl-tls-and-how-to-protect-your-system/). Il s'agit de garantir que les données de vos utilisateurs sont toujours gardées sûres et sécurisées.

En suivant les étapes ci-dessus, vous pouvez vous assurer que votre PWA est toujours conforme aux dernières normes et directives de sécurité. Cela aidera à protéger les données de vos utilisateurs contre les accès non autorisés et les potentielles menaces de sécurité.

## Comment se protéger contre les attaques par scripts inter-sites (XSS) et la falsification de requêtes inter-sites (CSRF)

[Les scripts inter-sites](https://www.freecodecamp.org/news/how-to-protect-against-dom-xss-attacks/) et [la falsification de requêtes inter-sites](https://www.freecodecamp.org/news/what-is-cross-site-request-forgery/) sont deux menaces de sécurité qui peuvent causer des dommages sérieux aux PWA.

Le XSS fonctionne en injectant du code malveillant dans le navigateur via une application web vulnérable.

Ce code peut être utilisé pour exfiltrer des données de la PWA, comme des mots de passe ou des numéros de carte de crédit, ou pour exécuter tout autre code malveillant.

Le CSRF, en revanche, est une forme d'attaque qui manipule le navigateur d'un utilisateur pour envoyer des requêtes falsifiées sans qu'il le sache.

Cela peut être utilisé pour exécuter des actions au sein d'une application, comme transférer de l'argent ou supprimer des données.

Heureusement, il existe des mesures que vous pouvez prendre pour protéger votre PWA contre les attaques XSS et CSRF :

* **Assainissez toutes les entrées utilisateur** : L'assainissement des entrées utilisateur est l'une des meilleures façons de se protéger contre les attaques XSS et CSRF. Assurez-vous de toujours valider et filtrer tout contenu potentiellement dangereux avant qu'il ne soit ajouté à votre base de données.
* **Utilisez une protection CAPTCHA** : L'ajout d'une protection CAPTCHA aux formulaires web aidera à garantir que toute requête provenant des utilisateurs provient de vraies personnes plutôt que de bots ou de scripts malveillants.
* **Utilisez des cookies sécurisés** : Les cookies sécurisés vous permettent de stocker des données sur vos utilisateurs dans un format chiffré et de limiter l'accès uniquement aux utilisateurs autorisés. Cela peut aider à s'assurer que les données ne sont pas exposées en cas de compromission.

En prenant ces mesures, vous pouvez aider à protéger votre PWA contre les attaques XSS et CSRF.

## Comment développer une politique de sécurité de contenu (CSP)

La politique de sécurité de contenu (CSP) est un mécanisme de sécurité web important conçu pour prévenir les attaques malveillantes.

En termes simples, une CSP est un ensemble de règles qui spécifient quelles sources sont autorisées lors du chargement de ressources telles que des scripts, des images et des feuilles de style. En définissant les sources de ces types de contenu, la CSP aide à protéger vos applications contre les attaques par scripts inter-sites (XSS) et les attaques par injection de données.

En mettant en œuvre une CSP sur votre PWA, vous pouvez ajouter une couche supplémentaire de protection contre les attaques malveillantes.

Quelques bonnes pratiques pour la mise en œuvre de la CSP incluent :

* **Définir les origines autorisées** : Cela garantit que seules les sources autorisées peuvent accéder au contenu de votre application.
* **Mettre en liste blanche les styles en ligne** : Lorsque cela est possible, utilisez l'attribut nonce pour mettre en liste blanche des scripts et styles en ligne spécifiques afin que le code ne soit exécuté que si le nonce correspond à ce qui est spécifié dans la politique.
* **Interdire les méthodes non sécurisées** : Incluez une directive qui bloque les méthodes dangereuses telles que eval() afin de vous protéger contre les attaques par injection de code.
* **Configurer la journalisation/le reporting** : Configurez la journalisation/le reporting afin de pouvoir suivre les requêtes entrantes et signaler toute activité suspecte.

En suivant ces bonnes pratiques et en configurant correctement la CSP, vous pouvez protéger efficacement vos PWA contre les attaques malveillantes tout en garantissant qu'elles restent sécurisées et performantes.

## Conclusion

En bref, si vous souhaitez garder votre application web sécurisée, il est important de suivre les protocoles de sécurité des meilleures pratiques tels que l'authentification robuste et le chiffrement, les mises à jour régulières des correctifs de sécurité et les API sécurisées. Il est également essentiel d'avoir un processus de développement sécurisé en place pour garantir que seul le code le plus sécurisé est déployé.

Enfin, l'éducation des utilisateurs est essentielle lorsqu'il s'agit des applications web. Fournir aux utilisateurs une plateforme sécurisée n'est que la moitié de la bataille, car en fin de compte, c'est à l'utilisateur de rester vigilant quant à sa sécurité en ligne.

Lisez plus sur les PWA :

* [Qu'est-ce qu'une PWA ? Les applications web progressives pour les débutants](https://www.freecodecamp.org/news/what-are-progressive-web-apps/)
* [Comment créer une PWA à partir de zéro avec HTML, CSS et JavaScript](https://www.freecodecamp.org/news/build-a-pwa-from-scratch-with-html-css-and-javascript/)