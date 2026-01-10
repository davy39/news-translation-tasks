---
title: Aide-mémoire des commandes OpenSSL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-10T20:15:02.000Z'
originalURL: https://freecodecamp.org/news/openssl-command-cheatsheet-b441be1e8c4a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3L4lzv7L5K6VcauwadO_7w.jpeg
tags:
- name: development
  slug: development
- name: Security
  slug: security
- name: SSL
  slug: ssl
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Aide-mémoire des commandes OpenSSL
seo_desc: 'By Alexey Samoshkin

  When it comes to security-related tasks, like generating keys, CSRs, certificates,
  calculating digests, debugging TLS connections and other tasks related to PKI and
  HTTPS, you’d most likely end up using the OpenSSL tool.

  OpenSSL i...'
---

Par Alexey Samoshkin

Lorsque vous devez effectuer des tâches liées à la sécurité, telles que la génération de clés, de CSR, de certificats, le calcul de digests, le débogage des connexions TLS et d'autres tâches liées à la PKI et au HTTPS, vous finirez probablement par utiliser l'outil OpenSSL.

OpenSSL inclut une multitude de fonctionnalités couvrant un large éventail de cas d'utilisation, et il est difficile de retenir sa syntaxe pour tous ces cas et assez facile de se perdre. Les pages `man` ne sont pas très utiles ici, donc souvent nous cherchons simplement sur Google "openssl comment [cas d'utilisation ici]" ou nous cherchons une sorte d'"aide-mémoire openssl" pour rappeler l'utilisation d'une commande et voir des exemples.

Cet article est ma collection personnelle de snippets et d'exemples de commandes `openssl`, regroupés par cas d'utilisation.

### Cas d'utilisation

Voici une liste de cas d'utilisation que je vais couvrir :

1. [Travailler avec les clés RSA et ECDSA](#travailler-avec-les-cles-rsa-et-ecdsa)
2. [Créer des demandes de signature de certificat (CSR)](#creer-des-demandes-de-signature-de-certificat-csr)
3. [Créer des certificats X.509](#creer-des-certificats-x509)
4. [Vérifier les CSR ou les certificats](#verifier-les-csr-ou-les-certificats)
5. [Calculer les digests de messages et l'encodage base64](#calculer-les-digests-de-messages-et-lencodage-base64)
6. [Client TLS pour se connecter à un serveur distant](#client-tls-pour-se-connecter-a-un-serveur-distant)
7. [Mesurer le temps de connexion et de handshake TLS](#mesurer-le-temps-de-connexion-et-de-handshake-tls)
8. [Convertir entre les formats d'encodage (PEM, DER) et les formats de conteneur (PKCS12, PKCS7)](#convertir-entre-les-formats-dencodage-pem-der-et-les-formats-de-conteneur-pkcs12-pkcs7)
9. [Lister les suites de chiffrement](#lister-les-suites-de-chiffrement)
10. [Vérifier manuellement le statut de révocation d'un certificat à partir d'un répondeur OCSP](#verifier-manuellement-le-statut-de-revocation-dun-certificat-a-partir-dun-repondeur-ocsp)

Bien sûr, ce n'est pas une liste complète, mais elle couvre les cas d'utilisation les plus courants et inclut ceux avec lesquels j'ai travaillé. Par exemple, je saute le chiffrement et le déchiffrement, ou l'utilisation d'OpenSSL pour la gestion des CA. `openssl` est comme un univers. On ne sait jamais où il se termine. ?

### Travailler avec les clés RSA et ECDSA

Dans les commandes ci-dessous, remplacez `[bits]` par la taille de la clé (par exemple, 2048, 4096, 8192).

Générer une clé RSA :  
`openssl genrsa -out example.key [bits]`

Afficher la clé publique ou le modulus uniquement :  
`openssl rsa -in example.key -pubout`  
`openssl rsa -in example.key -noout -modulus`

Afficher la représentation textuelle de la clé RSA :  
`openssl rsa -in example.key -text -noout`

Générer une nouvelle clé RSA et la chiffrer avec une phrase de passe basée sur le chiffrement AES CBC 256 :  
`openssl genrsa -aes256 -out example.key [bits]`

Vérifier votre clé privée. Si la clé a une phrase de passe, vous serez invité à la saisir :  
`openssl rsa -check -in example.key`

Supprimer la phrase de passe de la clé :  
`openssl rsa -in example.key -out example.key`

Chiffrer une clé privée existante avec une phrase de passe :  
`openssl rsa -des3 -in example.key -out example_with_pass.key`

Générer une clé ECDSA. `curve` doit être remplacé par : `prime256v1`, `secp384r1`, `secp521r1`, ou toute autre courbe elliptique supportée :  
`openssl ecparam -genkey -name [curve] | openssl ec -out example.ec.key`

Afficher la représentation textuelle de la clé ECDSA :  
`openssl ec -in example.ec.key -text -noout`

Lister les courbes EC disponibles, que la bibliothèque OpenSSL supporte :  
`openssl ecparam -list_curves`

Générer des paramètres DH avec une longueur donnée :  
`openssl dhparam -out dhparams.pem [bits]`

### Créer des demandes de signature de certificat (CSR)

Dans les commandes ci-dessous, remplacez `[digest]` par le nom de la fonction de hachage supportée : `md5`, `sha1`, `sha224`, `sha256`, `sha384` ou `sha512`, etc. Il est préférable d'éviter les fonctions faibles comme `md5` et `sha1`, et de rester sur `sha256` et au-dessus.

Créer une CSR à partir d'une clé privée existante.  
`openssl req -new -key example.key -out example.csr -[digest]`

Créer une CSR et une clé privée sans phrase de passe en une seule commande :  
`openssl req -nodes -newkey rsa:[bits] -keyout example.key -out example.csr`

Fournir les informations du sujet de la CSR sur la ligne de commande, plutôt que via une invite interactive.  
`openssl req -nodes -newkey rsa:[bits] -keyout example.key -out example.csr -subj "/C=UA/ST=Kharkov/L=Kharkov/O=Super Secure Company/OU=IT Department/CN=example.com"`

Créer une CSR à partir d'un certificat et d'une clé privée existants :  
`openssl x509 -x509toreq -in cert.pem -out example.csr -signkey example.key`

Générer une CSR pour un certificat SAN multi-domaines en fournissant un fichier de configuration openssl :  
`openssl req -new -key example.key -out example.csr -config req.conf`

où `req.conf` :

```
[req]prompt=nodefault_md = sha256distinguished_name = dnreq_extensions = req_ext
```

```
[dn]CN=example.com
```

```
[req_ext]subjectAltName=@alt_names
```

```
[alt_names]DNS.1=example.comDNS.2=www.example.comDNS.3=ftp.example.com
```

### Créer des certificats X.509

Créer un certificat auto-signé et une nouvelle clé privée à partir de zéro :  
`openssl req -nodes -newkey rsa:2048 -keyout example.key -out example.crt -x509 -days 365`

Créer un certificat auto-signé en utilisant une CSR et une clé privée existantes :  
`openssl x509 -req -in example.csr -signkey example.key -out example.crt -days 365`

Signer un certificat enfant en utilisant votre propre certificat "CA" et sa clé privée. Si vous étiez une entreprise CA, cela montre un exemple très naïf de la façon dont vous pourriez émettre de nouveaux certificats.  
`openssl x509 -req -in child.csr -days 365 -CA ca.crt -CAkey ca.key -set_serial 01 -out child.crt`

Afficher la représentation textuelle du certificat  
`openssl x509 -in example.crt -text -noout`

Afficher l'empreinte du certificat en tant que digest md5, sha1, sha256 :  
`openssl x509 -in cert.pem -fingerprint -sha256 -noout`

### Vérifier les CSR ou les certificats

Vérifier une signature de CSR :  
`openssl req -in example.csr -verify`

Vérifier qu'une clé privée correspond à un certificat et à une CSR :  
`openssl rsa -noout -modulus -in example.key | openssl sha256`  
`openssl x509 -noout -modulus -in example.crt | openssl sha256`  
`openssl req -noout -modulus -in example.csr | openssl sha256`

Vérifier le certificat, à condition que vous ayez les certificats racine et intermédiaires configurés comme de confiance sur votre machine :  
`openssl verify example.crt`

Vérifier le certificat, lorsque vous avez une chaîne de certificats intermédiaires. Le certificat racine ne fait pas partie du bundle et doit être configuré comme de confiance sur votre machine.  
`openssl verify -untrusted intermediate-ca-chain.pem example.crt`

Vérifier le certificat, lorsque vous avez une chaîne de certificats intermédiaires et un certificat racine, qui n'est pas configuré comme de confiance.  
`openssl verify -CAFile root.crt -untrusted intermediate-ca-chain.pem child.crt`

Vérifier que le certificat servi par un serveur distant couvre un nom d'hôte donné. Utile pour vérifier que votre certificat multi-domaines couvre correctement tous les noms d'hôte.  
`openssl s_client -verify_hostname [www.example.com](http://www.example.com) -connect example.com:443`

### Calculer les digests de messages et l'encodage base64

Calculer les digests `md5`, `sha1`, `sha256`, `sha384`, `sha512` :  
`openssl dgst -[hash_function] <input.f`i`le`  
`cat input.file | openssl [hash_functi`on]

Encodage et décodage base64 :  
`cat /dev/urandom | head -c 50 | openssl base64 | openssl base64 -d`

### Client TLS pour se connecter à un serveur distant

Se connecter à un serveur supportant TLS :  
`openssl s_client -connect [example.com:443](http://www.google.com:443)`  
`openssl s_client -host example.com -port 443`

Se connecter à un serveur et afficher la chaîne de certificats complète :  
`openssl s_client -showcerts -host example.com -port 443 </dev/n`ull

Extraire le certificat :  
`openssl s_client -connect example.com:443 2>&1 < /dev/null | sed -n '/-----BEGIN/,/-----END/p' > certif`icate.pem

Remplacer l'extension SNI (Server Name Indication) par un autre nom de serveur. Utile pour les tests lorsque plusieurs sites sécurisés sont hébergés sur la même adresse IP :  
`openssl s_client -servername [www.](http://www.foobbz.site)example.com -host example.com -port 443`

Tester la connexion TLS en forçant l'utilisation d'une suite de chiffrement spécifique, par exemple `ECDHE-RSA-AES128-GCM-SHA256`. Utile pour vérifier si un serveur peut communiquer correctement via différentes suites de chiffrement configurées, et non celle qu'il préfère.  
`openssl s_client -host example.com -port 443 -cipher ECDHE-RSA-AES128-GCM-SHA256 2>&1 </de`v/null

### Mesurer le temps de connexion et de handshake TLS

Mesurer le temps de connexion SSL sans/avec réutilisation de session :  
`openssl s_time -connect example.com:443 -new`  
`openssl s_time -connect example.com:443 -reuse`

Examiner approximativement les temps de handshake TCP et SSL en utilisant `curl` :  
`curl -kso /dev/null -w "tcp:%{time_connect}, ssldone:%{time_appconnect}\n" https://example.com`

Mesurer la vitesse de divers algorithmes de sécurité :  
`openssl speed rsa2048`  
`openssl speed ecdsap256`

### Convertir entre les formats d'encodage et de conteneur

Convertir un certificat entre les formats DER et PEM :  
`openssl x509 -in example.pem -outform der -out example.der`  
`openssl x509 -in example.der -inform der -out example.pem`

Combiner plusieurs certificats dans un fichier PKCS7 (P7B) :  
`openssl crl2pkcs7 -nocrl -certfile child.crt -certfile ca.crt -out example.p7b`

Convertir d'un PKCS7 vers un PEM. Si le fichier PKCS7 contient plusieurs certificats, le fichier PEM contiendra tous les éléments.  
`openssl pkcs7 -in example.p7b -print_certs -out example.crt`

Combiner un fichier de certificat PEM et une clé privée en PKCS#12 (.pfx .p12). Vous pouvez également ajouter une chaîne de certificats au fichier PKCS12.  
`openssl pkcs12 -export -out certificate.pfx -inkey privkey.pem -in certificate.pem -certfile ca-chain.pem`

Convertir un fichier PKCS#12 (.pfx .p12) contenant une clé privée et des certificats en PEM :  
`openssl pkcs12 -in keystore.pfx -out keystore.pem -nodes`

### Lister les suites de chiffrement

Lister les suites de chiffrement TLS disponibles, que le client openssl est capable de gérer :  
`openssl ciphers -v`

Énumérer toutes les suites de chiffrement individuelles, qui sont décrites par une chaîne de liste de chiffrement OpenSSL. Cela est utile lorsque vous configurez un serveur (comme Nginx), et que vous devez tester votre chaîne `ssl_ciphers`.  
`openssl ciphers -v 'EECDH+ECDSA+AESGCM:EECDH+aRSA+SHA256:EECDH:DHE+AESGCM:DHE:!RSA!aNULL:!eNULL:!LOW:!RC4'`

### Vérifier manuellement le statut de révocation d'un certificat à partir d'un répondeur OCSP

Ceci est un processus en plusieurs étapes :

1. Récupérer le certificat d'un serveur distant
2. Obtenir la chaîne de certificats de l'autorité de certification intermédiaire
3. Lire l'URI du point de terminaison OCSP à partir du certificat
4. Demander à un répondeur OCSP distant le statut de révocation du certificat

Tout d'abord, récupérez le certificat d'un serveur distant :  
`openssl s_client -connect example.com:443 2>&1 < /dev/null | sed -n '/-----BEGIN/,/-----END/p' >` cert.pem

Vous devrez également obtenir la chaîne de certificats de l'autorité de certification intermédiaire. Utilisez le drapeau `-showcerts` pour afficher la chaîne de certificats complète, et enregistrez manuellement tous les certificats intermédiaires dans le fichier `chain.pem` :  
`openssl s_client -showcerts -host example.com -port 443 </dev/n`ull

Lire l'URI du point de terminaison OCSP à partir du certificat :  
`openssl x509 -in cert.pem -noout -ocsp_uri`

Demander à un répondeur OCSP distant le statut de révocation du certificat en utilisant l'URI de l'étape précédente (par exemple, http://ocsp.stg-int-x1.letsencrypt.org).   
`openssl ocsp -header "Host" "ocsp.stg-int-x1.letsencrypt.org" -issuer chain.pem -VAfile chain.pem -cert cert.pem -text -url [http://ocsp.stg-int-x1.letsencrypt.org](http://ocsp.stg-int-x1.letsencrypt.org)`

### Ressources

J'ai rassemblé quelques ressources sur OpenSSL que vous pourriez trouver utiles.

OpenSSL Essentials: Working with SSL Certificates, Private Keys and CSRs | DigitalOcean — [https://www.digitalocean.com/community/tutorials/openssl-essentials-working-with-ssl-certificates-private-keys-and-csrs](https://www.digitalocean.com/community/tutorials/openssl-essentials-working-with-ssl-certificates-private-keys-and-csrs)

The Most Common OpenSSL Commands — [https://www.sslshopper.com/article-most-common-openssl-commands.html](https://www.sslshopper.com/article-most-common-openssl-commands.html)

OpenSSL: Working with SSL Certificates, Private Keys and CSRs — [https://www.dynacont.net/documentation/linux/openssl/](https://www.dynacont.net/documentation/linux/openssl/)