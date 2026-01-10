---
title: Comment faire fonctionner HTTPS sur votre environnement de développement local
  en 5 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-19T23:09:37.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-https-working-on-your-local-development-environment-in-5-minutes-7af615770eec
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9cb0e5740569d1a4cab759.jpg
tags:
- name: development
  slug: development
- name: https
  slug: https
- name: Security
  slug: security
- name: SSL
  slug: ssl
- name: 'tech '
  slug: tech
seo_title: Comment faire fonctionner HTTPS sur votre environnement de développement
  local en 5 minutes
seo_desc: 'By Daksh Shah


  Almost any website you visit today is protected by HTTPS. If yours isn’t yet, it
  should be. Securing your server with HTTPS also means that you can’t send requests
  to this server from one that isn’t protected by HTTPS. This poses a pro...'
---

Par Daksh Shah

![Image](https://cdn-media-1.freecodecamp.org/images/1*8XwjYNPlrj0paEvIjn0Dcw.png)

Presque tous les sites web que vous visitez aujourd'hui sont protégés par HTTPS. Si le vôtre ne l'est pas encore, [il devrait l'être](https://developers.google.com/web/fundamentals/security/encrypt-in-transit/why-https). Sécuriser votre serveur avec HTTPS signifie également que vous ne pouvez pas envoyer de requêtes à ce serveur à partir d'un serveur non protégé par HTTPS. Cela pose un problème pour les développeurs qui utilisent un environnement de développement local, car tous fonctionnent sur `http://localhost` par défaut.

Dans la startup dont je fais partie, nous avons décidé de sécuriser nos endpoints AWS Elastic Load Balancer avec HTTPS dans le cadre d'une initiative pour renforcer la sécurité. Je me suis retrouvé dans une situation où les requêtes de mon environnement de développement local vers le serveur ont commencé à être rejetées.

Après une rapide recherche sur Google, j'ai trouvé plusieurs articles comme [celui-ci](https://devcenter.heroku.com/articles/ssl-certificate-self), [celui-là](https://www.kevinleary.net/self-signed-trusted-certificates-node-js-express-js/) ou [celui-ci](https://blog.praveen.science/securing-your-localhost/) avec des instructions détaillées sur la manière d'implémenter HTTPS sur `localhost`. Aucune de ces instructions ne semblait fonctionner, même après les avoir suivies religieusement. Chrome me renvoyait toujours une erreur `NET::ERR_CERT_COMMON_NAME_INVALID`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cQyGAORXHxsrhs5KRRBOgQ.png)

### Le problème

Toutes les instructions détaillées que j'avais trouvées étaient correctes à l'époque où elles avaient été écrites. Plus maintenant.

Après une tonne de recherches sur Google, j'ai découvert que la raison pour laquelle mon certificat local était rejeté était que [Chrome avait abandonné le support de la correspondance commonName dans les certificats](https://groups.google.com/a/chromium.org/forum/m/#!topic/security-dev/IGT2fLJrAeo), exigeant ainsi un subjectAltName depuis janvier 2017.

### La solution

Nous allons utiliser [OpenSSL](https://www.openssl.org/) pour générer tous nos certificats.

#### Étape 1 : Certificat SSL racine

La première étape consiste à créer un certificat racine Secure Sockets Layer (SSL). Ce certificat racine peut ensuite être utilisé pour signer n'importe quel nombre de certificats que vous pourriez générer pour des domaines individuels. Si vous n'êtes pas familier avec l'écosystème SSL, cet [article de DNSimple](https://support.dnsimple.com/articles/what-is-ssl-root-certificate/) fait un bon travail d'introduction aux certificats SSL racine.

Générez une clé RSA-2048 et enregistrez-la dans un fichier `rootCA.key`. Ce fichier sera utilisé comme clé pour générer le certificat SSL racine. Vous serez invité à entrer une phrase de passe que vous devrez saisir chaque fois que vous utiliserez cette clé particulière pour générer un certificat.

```bash
openssl genrsa -des3 -out rootCA.key 2048
```

Vous pouvez utiliser la clé que vous avez générée pour créer un nouveau certificat SSL racine. Enregistrez-le dans un fichier nommé `rootCA.pem`. Ce certificat aura une validité de 1 024 jours. N'hésitez pas à le modifier pour le nombre de jours que vous souhaitez. Vous serez également invité à fournir d'autres informations facultatives.

```bash
openssl req -x509 -new -nodes -key rootCA.key -sha256 -days 1024 -out rootCA.pem
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*76xehIse7mPGF094ojiBBw.png)

#### Étape 2 : Faire confiance au certificat SSL racine

Avant de pouvoir utiliser le certificat SSL racine nouvellement créé pour commencer à émettre des certificats de domaine, il y a une étape supplémentaire. Vous devez indiquer à votre Mac de faire confiance à votre certificat racine afin que tous les certificats individuels émis par celui-ci soient également dignes de confiance.

Ouvrez l'accès au trousseau sur votre Mac et allez dans la catégorie Certificats de votre trousseau système. Une fois là, importez le `rootCA.pem` en utilisant Fichier > Importer des éléments. Double-cliquez sur le certificat importé et changez le menu déroulant "Lorsque vous utilisez ce certificat :" **pour Toujours faire confiance** dans la section Confiance.

Votre certificat devrait ressembler à ceci dans l'accès au trousseau si vous avez correctement suivi les instructions jusqu'à présent.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NWwMb0yV9ClHDj87Kug9Ng.png)

#### Étape 3 : Certificat SSL de domaine

Le certificat SSL racine peut maintenant être utilisé pour émettre un certificat spécifiquement pour votre environnement de développement local situé à `localhost`.

Créez un nouveau fichier de configuration OpenSSL `server.csr.cnf` afin de pouvoir importer ces paramètres lors de la création d'un certificat au lieu de les saisir sur la ligne de commande.

```bash
[req]
default_bits = 2048
prompt = no
default_md = sha256
distinguished_name = dn

[dn]
C=US
ST=RandomState
L=RandomCity
O=RandomOrganization
OU=RandomOrganizationUnit
emailAddress=hello@example.com
CN = localhost
```

Créez un fichier `v3.ext` afin de créer un [certificat X509 v3](https://en.wikipedia.org/wiki/X.509). Remarquez comment nous spécifions `subjectAltName` ici.

```bash
authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:FALSE
keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
subjectAltName = @alt_names

[alt_names]
DNS.1 = localhost
```

Créez une clé de certificat pour `localhost` en utilisant les paramètres de configuration stockés dans `server.csr.cnf`. Cette clé est stockée dans `server.key`.

```bash
openssl req -new -sha256 -nodes -out server.csr -newkey rsa:2048 -keyout server.key -config <( cat server.csr.cnf )
```

Une demande de signature de certificat est émise via le certificat SSL racine que nous avons créé précédemment pour créer un certificat de domaine pour `localhost`. Le résultat est un fichier de certificat appelé `server.crt`.

```bash
openssl x509 -req -in server.csr -CA rootCA.pem -CAkey rootCA.key -CAcreateserial -out server.crt -days 500 -sha256 -extfile v3.ext
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*kulsSyc0-ylsevP5eIlktA.png)

#### Utilisez votre nouveau certificat SSL

Vous êtes maintenant prêt à sécuriser votre `localhost` avec HTTPS. Déplacez les fichiers `server.key` et `server.crt` vers un emplacement accessible sur votre serveur et incluez-les lors du démarrage de votre serveur.

Dans une application Express écrite en Node.js, voici comment vous procéderiez. Assurez-vous de le faire uniquement pour votre environnement local. **Ne l'utilisez pas en production**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*89r7TnYG49V3zMoUnfOP7Q.png)

J'espère que vous avez trouvé ce tutoriel utile. Si vous n'êtes pas à l'aise avec l'exécution des commandes données ici par vous-même, j'ai créé un ensemble de scripts pratiques que vous pouvez exécuter rapidement pour générer les certificats pour vous. Plus de détails peuvent être trouvés sur le [dépôt GitHub](https://github.com/dakshshah96/local-cert-generator/).

_J'adore aider les autres développeurs web. Suivez-moi sur [Twitter](https://twitter.com/dakshshah96) et faites-moi savoir si vous avez des suggestions ou des commentaires. Si vous souhaitez montrer votre appréciation pour l'un des travaux que j'ai réalisés, qu'il s'agisse d'un article de blog, d'un projet open source ou simplement d'un tweet amusant, vous pouvez [m'offrir une tasse de café](https://www.buymeacoffee.com/dakshshah96)._