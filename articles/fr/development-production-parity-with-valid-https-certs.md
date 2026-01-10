---
title: Comment combler l'écart entre le développement et la production avec des certificats
  HTTPS valides
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-07-31T17:30:52.000Z'
originalURL: https://freecodecamp.org/news/development-production-parity-with-valid-https-certs
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/pexels-martin-damboldt-814499--1-.jpg
tags:
- name: https
  slug: https
- name: software development
  slug: software-development
seo_title: Comment combler l'écart entre le développement et la production avec des
  certificats HTTPS valides
seo_desc: 'By Linda Ikechukwu

  One of the core principles of software development involves maintaining development/production
  parity. But this is not always the case for developers working on localhost.

  To review, dev/prod parity refers to keeping development, s...'
---

Par Linda Ikechukwu

L'un des principes fondamentaux du développement logiciel consiste à maintenir la parité entre les environnements de développement et de production. Mais ce n'est pas toujours le cas pour les développeurs travaillant sur `localhost`.

Pour rappel, la parité dev/prod fait référence au fait de garder les environnements de développement, de staging et de production aussi similaires que possible afin d'éviter de rencontrer des bugs non détectés. Un manque de parité dev/prod peut entraîner des bugs qui se produisent dans un environnement mais qui ne peuvent pas être reproduits et débogués dans d'autres.

Ainsi, par exemple, si votre site web en production fonctionne en HTTPS, vous voudrez que votre site de développement local fonctionne également en HTTPS.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-183.png)
_"Ça marche sur mon ordinateur..." comic. [Source de l'image](https://twitter.com/gerardsans/status/1413936148846727179?s=20)_

## Pourquoi vous devriez activer HTTPS sur votre localhost

Vous pourriez penser, "est-ce que `localhost` ne se comporte pas comme `https` ? N'est-ce pas pour cela que certaines API qui ne fonctionnent pas sur un site HTTP déployé fonctionnent sur `http://localhost` ?"

Eh bien, oui. Pour un grand nombre de cas d'utilisation, `http://localhost/<votreport>` est tout à fait correct et se comporte comme un site HTTPS. Mais il existe des cas où ce n'est pas le cas. Voici quelques exemples de tels cas :

**Débogage des erreurs de contenu mixte** : Les erreurs de contenu mixte se produisent lorsque tout le contenu d'une page n'est pas récupéré via HTTPS.

Par exemple, si vous utilisez une bibliothèque JavaScript à partir d'un CDN basé sur HTTP, tout peut fonctionner comme prévu lorsque vous travaillez sur localhost. Mais dans votre environnement de production basé sur HTTPS, les choses peuvent être différentes.

Sur une page HTTPS, toute tentative de chargement de JavaScript à partir d'une URL HTTP sera bloquée par les navigateurs. Parce que votre environnement local fonctionne sur localhost, vous pourriez ne pas être en mesure de repérer ce bug.

**Test de bibliothèques ou API tierces** qui nécessitent HTTPS (par exemple OAuth ou l'API d'Instagram) en local.

Ou **configuration et test de cookies sécurisés sur différents navigateurs pendant le développement local** : Les cookies `Secure` sont définis uniquement sur HTTPS, mais pas sur `http://localhost` pour tous les navigateurs.

Il existe d'autres cas, car cette liste n'est pas exhaustive. Mais pour éviter les cas où les choses ne fonctionneront pas sur `http://localhost`, ou où il ne se comportera pas tout à fait comme votre site de production, utilisez simplement **HTTPS pour le développement local**.

Maintenant, pour activer HTTPS pour votre environnement local, vous devez obtenir un certificat TLS pour celui-ci. Parlons-en.

## La relation entre HTTPS et les certificats TLS

Si vous connaissez déjà les certificats TLS et comment ils permettent HTTPS, ou si vous êtes axé sur les solutions et souhaitez passer à l'action, vous pouvez sauter cette section et passer à la suivante.

Mais si vous souhaitez obtenir des informations de base sur pourquoi les certificats TLS sont la clé, continuez votre lecture.

### Qu'est-ce que HTTPS ?

HTTPS est une extension sécurisée de HTTP, le protocole de communication utilisé pour livrer des pages web sur Internet.

HTTPS est essentiellement HTTP avec une couche de sécurité ajoutée fournie par le protocole Transport Layer Security (TLS). Alors que HTTP gère le transport des données sur Internet, TLS chiffre ces données pour garantir leur sécurité, donnant naissance à HTTPS.

### Qu'est-ce que TLS ?

Le chiffrement TLS des transferts de données est basé sur la transmission d'un certificat TLS du serveur web à un client, généralement le navigateur.

Voici comment cela fonctionne : lorsque vous entrez une URL HTTPS que vous souhaitez visiter, votre navigateur tente d'établir une connexion HTTPS avec le serveur web hébergeant le fichier nécessaire pour servir la page web. Pour ce faire, une poignée de main TLS est effectuée.

Le but de la poignée de main TLS est que le navigateur et le serveur web s'accordent sur une clé cryptographique symétrique partagée à utiliser pour chiffrer et déchiffrer les messages échangés entre eux. Mais cette clé symétrique doit être échangée de manière sécurisée.

Les clés symétriques sont un type de clé cryptographique préféré pour le chiffrement car elles sont plus rapides à exécuter (sur le web, la vitesse est tout). Mais elles sont plus risquées car il n'y a aucun moyen de garantir ou de vérifier qu'un acteur malveillant n'intercepte pas une clé symétrique en transit et ne la revendique pas. De plus, il n'y a aucun moyen de vérifier que seul le destinataire prévu reçoit la clé.

C'est là que les clés asymétriques entrent en jeu pour résoudre ce problème. Les clés asymétriques sont utilisées pour transmettre de manière sécurisée une clé symétrique entre le client et le serveur.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Talk-Using-Certificates-on-local-web-servers--1-.png)
_Illustration représentant la communication sécurisée entre le navigateur et le serveur web_

### Comment fonctionnent les clés asymétriques ?

Les clés asymétriques utilisent une paire de clés : une clé publique et une clé privée. Lors de l'échange de données, l'expéditeur utilise la clé publique pour chiffrer les messages, et le destinataire utilise sa clé privée (qui est gardée privée et jamais partagée) pour déchiffrer le message. Puisque la clé privée est gardée secrète, cela garantit que seul le destinataire prévu peut déchiffrer le message.

Par exemple, si un serveur souhaite recevoir de manière sécurisée une clé symétrique d'un navigateur, il crée une paire de clés asymétriques et partage la clé publique avec le navigateur. Le navigateur utilise la clé publique pour chiffrer la clé symétrique et envoie le message chiffré au serveur. Le serveur utilise ensuite sa clé privée (qui n'est connue que du serveur) pour déchiffrer le message.

C'est ainsi que les clés asymétriques garantissent que seul le destinataire prévu avec la clé privée correspondante reçoit la clé symétrique.

Mais comment le serveur web obtient-il sa clé publique dans les mains du navigateur, et comment le navigateur peut-il être sûr que la clé publique qu'il a reçue appartient réellement au serveur web ? Ils peuvent la placer dans un fichier ou un document, et c'est à cela que servent les certificats TLS.

Un certificat TLS est un fichier de données hébergé sur le [serveur d'origine](https://www.cloudflare.com/learning/cdn/glossary/origin-server/) d'un site web et contient la [clé publique](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/) du serveur, ainsi que des informations connexes qui identifient le serveur web.

Maintenant, qu'en est-il du problème de confiance ? C'est là que le deuxième composant du jeu, les autorités de certification, entrent en jeu.

### Qu'est-ce qu'une autorité de certification ?

Une autorité de certification (CA) est une entité qui est approuvée à la fois par un client et un serveur. Son rôle principal est d'émettre de manière responsable des certificats TLS.

Les CA servent de garants ou d'arbitres. Par exemple, si M. A souhaite effectuer une transaction avec M. B, mais qu'ils n'ont aucune relation préalable, M. C, en qui M. B a confiance, peut se porter garant pour M. B.

Dans ce scénario, M. C joue le rôle de la CA, aidant à établir la confiance entre le client et le serveur. Les certificats TLS doivent être signés par des autorités de certification pour résoudre le problème de confiance.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Talk-Using-Certificates-on-local-web-servers--2-.png)
_Illustration montrant comment fonctionne une autorité de certification_

Ainsi, un certificat TLS est un fichier contenant la clé publique d'un serveur web, signé par une autorité de certification pour attester que la clé publique contenue dans le certificat est bien la clé publique du serveur web.

Lors de la poignée de main TLS, le client et le serveur utilisent les clés publique et privée pour échanger des données générées aléatoirement. Ces données aléatoires sont utilisées pour créer de nouvelles clés symétriques partagées pour le chiffrement, appelées clés de session. Et c'est ainsi que HTTPS voit le jour.

D'accord, assez de cryptographie pour aujourd'hui. Maintenant que vous comprenez les bases des certificats, examinons comment obtenir un certificat TLS pour votre serveur `[localhost](<http://localhost>)`.

## Comment obtenir un certificat TLS pour votre serveur localhost

Maintenant que vous comprenez le rôle que jouent les certificats dans l'activation de HTTPS, il est clair ce que nous devons faire pour activer HTTPS pour notre serveur web local : nous devons obtenir un certificat TLS d'une autorité de certification approuvée par les navigateurs et les clients sur notre appareil.

Les systèmes d'exploitation et les navigateurs sont livrés avec une liste prédéfinie de CA de confiance publiques telles que Let's Encrypt. Pour voir la liste des autorités de certification de confiance sur votre magasin de confiance racine du système, si vous êtes sur un Mac, recherchez 'accès aux trousseau'.

Mais ces CA sont interdites d'émettre des certificats pour des domaines sur des TLD privés comme localhost [pour diverses raisons](https://smallstep.com/blog/reasons-not-to-use-public-certificate-authorities/).

Il est possible de créer un certificat TLS auto-signé sans CA. Dans ce cas, vous signerez vous-même votre certificat et attesterez du fait que votre clé publique est bien votre clé publique.

Avec les certificats auto-signés, il n'y a pas d'autorité extérieure pour vérifier que le serveur d'origine est bien celui qu'il prétend être.

Les navigateurs ne considèrent pas les certificats auto-signés comme dignes de confiance et peuvent toujours marquer les sites qui les utilisent comme "non sécurisés", malgré l'URL https://. C'est ce qui se passe avec le [drapeau https de Gatsby](https://www.gatsbyjs.com/docs/local-https/).

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image--1-.png)
_Erreur de certificat auto-signé sur le navigateur Firefox._

Ce que vous devez faire est :

1. Créer votre propre autorité de certification locale
2. Faire en sorte que votre système/environnement lui fasse confiance
3. Utiliser la CA pour émettre un certificat TLS pour votre serveur web local
4. Installer le certificat sur votre serveur web

Cela peut sembler beaucoup, n'est-ce pas ? La bonne nouvelle est que c'est en fait super facile et rapide à faire en utilisant un projet open-source connu sous le nom de `step-ca`.

## Comment utiliser `step-ca` pour obtenir un certificat TLS pour votre serveur Node.js local

[`step-ca` est une autorité de certification open-source](https://github.com/smallstep/certificates) pour les réseaux privés et internes.

Pour commencer, suivez ces étapes :

Tout d'abord, ouvrez votre terminal. Exécutez `brew install step` si vous êtes sur un Mac pour installer `step-ca` et l'outil CLI accompagnant, `step-cli`.

`step-cli` est un outil CLI utile pour interagir et communiquer avec `step-ca`. Si vous êtes sur Windows ou Linux, vous pouvez trouver des instructions d'installation dans la documentation.

Ensuite, exécutez `step-init`. Cette commande crée et initialise un serveur d'autorité de certification `step-ca` sur votre machine locale.

Ensuite, vous serez invité à sélectionner quelques options comme montré dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Talk-Using-Certificates-on-local-web-servers--3-.png)
_Capture d'écran des options de configuration de `step-ca`_

Passons-les en revue une par une :

* **Type de déploiement** : Comme sur l'image ci-dessus, choisissez 'Standalone' car vous exécutez vous-même l'option `step-ca`.
* **Comment souhaitez-vous nommer votre PKI** : Changez 'Linda-PKI' en ce que vous voulez.
* **Quelles adresses DNS ou IP souhaitez-vous ajouter à votre nouvelle CA** : Cela vous demande de spécifier les noms de domaine ou adresses IP pour lesquels vous souhaitez que votre CA émette des certificats. Puisque c'est pour localhost, entrez 'localhost'.
* **Quelle IP et quel port souhaitez-vous lier à votre CA** : Cela vous demande de spécifier un port sur lequel le serveur CA s'exécutera.
* **Comment souhaitez-vous nommer votre provisionneur** : Dans l'écosystème `step-ca`, un provisionneur est une personne ou une entité autorisée à initier des opérations d'émission de certificats avec une CA. Pensez à cela comme à l'utilisation de votre email comme nom d'utilisateur pour vous inscrire sur une plateforme.
* **Choisissez un mot de passe pour les clés de votre CA et votre premier provisionneur** : C'est le mot de passe qui sera utilisé pour autoriser les demandes d'émission de certificats. Notez votre mot de passe car il sera utile dans les prochaines étapes.

Après avoir rempli toutes les options, vous obtiendrez un écran comme ci-dessous, indiquant que votre CA et autres éléments nécessaires ont été créés et sont prêts à être utilisés.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-2022-10-21-at-17.58.57.png)
_Capture d'écran de l'écran de succès de `step-ca`_

Maintenant, exécutez `step certificate install <chemin-vers-root_ca.crt>` pour installer le fichier de certificat racine de la CA dans votre magasin de confiance système. Remplacez `<chemin-vers-root_ca.crt>` par votre propre chemin de fichier de l'étape précédente. Dans mon exemple, ce serait `</Users/linda/.step/certs/root_ca.crt>`.

Souvenez-vous comment j'ai mentionné que votre autorité de certification doit être approuvée par vos navigateurs, et que tous les systèmes d'exploitation et navigateurs sont préinstallés avec des autorités de certification approuvées ? Cette étape ajoute votre autorité de certification nouvellement créée à cette liste.

Après avoir exécuté cette commande, vous obtiendrez un écran comme ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-2022-10-22-at-08.41.43.png)
_Capture d'écran de l'écran de succès de l'installation du certificat racine `step-ca`_

Ensuite, exécutez `step-ca <chemin-vers-ca.json>` pour démarrer le serveur CA. Dans mon exemple, `<chemin-vers-ca.json>` serait `/Users/linda/.step/config/ca.json` de la troisième étape. Vous obtiendrez un écran vous informant que votre CA est maintenant en cours d'exécution sur le port que vous avez spécifié dans la troisième étape.

Utilisez votre CA pour créer un nouveau certificat et une nouvelle clé privée pour votre serveur/projet [localhost](http://localhost). Exécutez `step ca certificate <sujet> <fichier-crt> <fichier-clé>` sur votre serveur de projet où :

* `sujet` est le nom de domaine ou l'adresse IP du serveur pour lequel vous obtenez un certificat,
* `fichier-crt` est le nom du fichier pour écrire le certificat, et
* `fichier-clé` est le fichier pour écrire la clé privée.

Pour mon exemple, ma commande était `step ca certificate localhost server.crt server.key`

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-2022-10-22-at-09.01.23.png)
_Capture d'écran de l'écran de succès pour la création du certificat et de la clé privée step-ca_

Vous remarquerez que des fichiers server.crt et server.key seront créés dans votre projet.

Enfin, référencez les fichiers `server.crt` et `server.key` dans la méthode Node.js `https.createServer()` pour les propriétés cert et key, respectivement, dans votre fichier `index.js`. Cela indique au serveur Node.js résultant d'utiliser le certificat et la clé privée lors d'une poignée de main TLS pour activer HTTPS.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-2022-10-22-at-11.27.41.png)
_Capture d'écran des fichiers server.crt et server.key référencés dans la fonction https.createServer dans mon projet de démonstration node.js_

Arrêtez et redémarrez votre serveur Node.js, puis naviguez vers votre URL localhost. Votre localhost devrait maintenant fonctionner en HTTPS, comme ci-dessous (remarquez le signe de cadenas) :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-2022-10-21-at-17.32.21.png)
_Capture d'écran de mon serveur localhost node.js fonctionnant maintenant en HTTPS !_

Super !

## Derniers mots et points bonus

Si vous avez suivi ce tutoriel, vous avez réussi à émettre un certificat pour votre projet Node.js local. Vous pouvez utiliser la même autorité de certification (CA) pour émettre des certificats pour d'autres projets fonctionnant sur différents ports en suivant le même processus.

Il est important de noter que par défaut, ces certificats ne sont valides que pour un jour. Vous avez deux options pour prolonger leur durée de vie : soit l'étendre lors de la création du certificat, en utilisant les drapeaux `--not-before` et `--not-after` ([voir la documentation](https://smallstep.com/docs/step-cli/reference/certificate/create/#positional-arguments)), soit exécuter un démon pour renouveler périodiquement le certificat.

Si votre certificat a déjà expiré, vous pouvez le renouveler manuellement en suivant les étapes ci-dessous :

1. Redémarrez votre instance `step-ca` au cas où le processus aurait été fermé (c'est-à-dire que vous avez fermé le terminal d'une manière ou d'une autre). Exécutez `step-ca <chemin-fichier-vers-ca.json>`.
2. Exécutez `step ca provisioner update linda.ikechukwu@smallstep.com --allow-renewal-after-expiry` où [linda.ikechukwu@smallstep.com](mailto:linda.ikechukwu@smallstep.com) doit être le nom de votre provisionneur.
3. Tuez le processus du serveur CA et redémarrez-le.
4. Ensuite, exécutez la commande de renouvellement `step ca renew server.crt server.key`

Bonne construction !