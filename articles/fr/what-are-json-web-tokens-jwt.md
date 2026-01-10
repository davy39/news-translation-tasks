---
title: Qu'est-ce que les JSON Web Tokens (JWT) ?
subtitle: ''
author: Grant Riordan
co_authors: []
series: null
date: '2025-07-07T21:58:35.931Z'
originalURL: https://freecodecamp.org/news/what-are-json-web-tokens-jwt
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1751819356361/352ef68a-fa20-4a69-b666-393f7a17fa40.png
tags:
- name: JWT
  slug: jwt
- name: authentication
  slug: authentication
- name: authorization
  slug: authorization
- name: Tutorial
  slug: tutorial
seo_title: Qu'est-ce que les JSON Web Tokens (JWT) ?
seo_desc: When you’re working with any website, application, or API, you'll inevitably
  need to log in and authenticate your user base. One of the more commonly used methods
  of passing around authentication credentials from one system to another is using
  a JSON...
---

Lorsque vous travaillez avec un site web, une application ou une API, vous devrez inévitablement vous connecter et authentifier votre base d'utilisateurs. L'une des méthodes les plus couramment utilisées pour transmettre des informations d'authentification d'un système à un autre consiste à utiliser un JSON Web Token (JWT).

Dans cet article, vous apprendrez :

* Ce qu'est un JSON Web Token (JWT)

* Comment les JWT sont structurés et créés

* Différentes techniques de signature JWT et algorithmes (symétrique vs asymétrique)

* Comment les JWT sont utilisés dans les flux d'authentification réels

* Bonnes pratiques de sécurité importantes pour l'utilisation des JWT

## Table des matières

* [Qu'est-ce qu'un JWT ?](#heading-qu-est-ce-qu-un-jwt)

  * [Les JSON Web Tokens sont composés de trois éléments](#heading-les-json-web-tokens-sont-composés-de-trois-éléments)

  * [Signature asymétrique (RS256) expliquée](#heading-signature-asymétrique-rs256-expliquée)

  * [Analogie : Le cadenas et la clé pour les signatures asymétriques](#heading-analogie-le-cadenas-et-la-clé-pour-les-signatures-asymétriques)

* [Signature symétrique : HS256 (HMAC avec SHA-256)](#heading-signature-symétrique-hs256-hmac-avec-sha-256)

  * [Comment fonctionne la vérification HS256](#heading-comment-fonctionne-la-vérification-hs256)

* [JWT en action : Un flux d'authentification typique](#heading-jwt-en-action-un-flux-d-authentification-typique)

* [Bonnes pratiques de sécurité JWT et considérations](#heading-bonnes-pratiques-de-sécurité-jwt-et-considérations)

## Qu'est-ce qu'un JWT ?

> JSON Web Token (JWT) est une norme ouverte (RFC 7519) qui définit une manière compacte et autonome de transmettre en toute sécurité des informations entre les parties sous forme d'objet JSON. Ces informations peuvent être vérifiées et considérées comme fiables car elles sont signées numériquement. Les JWT peuvent être signés à l'aide d'un secret (avec l'algorithme HMAC) ou d'une paire de clés publique/privée utilisant RSA ou ECDSA. 
> 
— Introduction aux JWT par jwt.io

Bien que cette définition soit exacte, elle peut sembler un peu dense au premier abord. Imaginez que vous souhaitez envoyer un message scellé et inviolable à quelqu'un. C'est essentiellement ce qu'est un JSON Web Token (JWT). Il s'agit d'un message sécurisé, un type spécial de message conçu pour être envoyé entre deux parties qui peuvent être assurées qu'il provient d'un expéditeur attendu.

Chaque JWT est signé numériquement à l'aide soit d'un **code secret** (pour les algorithmes symétriques comme HMAC), soit d'une **clé privée** (pour les algorithmes asymétriques comme RSA ou ECDSA).

Ce code secret ou cette clé privée est connu uniquement du système qui émet le JWT (souvent appelé un *fournisseur d'authentification*, comme Auth0, AWS Cognito ou Firebase Auth, qui gère les connexions et l'identité des utilisateurs).

Cette signature prouve deux choses :

1. **Authenticité** : Elle prouve que le message provient bien de l'expéditeur qu'il prétend être.

2. **Intégrité** : Elle prouve que le message n'a pas été modifié ou falsifié depuis qu'il a été signé. Si même un seul caractère est modifié, la signature ne correspondra pas, et vous saurez que quelque chose ne va pas, ce qui signifie que le contenu du JWT ne peut pas être considéré comme fiable.

### Les JSON Web Tokens sont composés de trois éléments

Les JWT sont composés de 3 parties clés :

1. En-tête

2. Charge utile

3. Signature

#### En-tête

L'en-tête contient des métadonnées sur le token. Pensez-y comme à une étiquette sur un colis – il vous indique ce qu'il y a à l'intérieur et comment il a été préparé.

Typiquement, l'en-tête contient :

`alg` : Cela spécifie l'**algorithme** utilisé pour signer le JWT. Les algorithmes courants sont `HS256` (HMAC avec SHA-256) ou `RS256` (RSA avec SHA-256).

`typ` : Cela spécifie le **type** de token, qui est presque toujours `JWT` pour les JSON Web Tokens standard.

**Exemple (décodé) :**

```json
{ 
  "alg": "RS256",
  "typ": "JWT" 
} 
```

#### Charge utile

Il s'agit de la deuxième partie du JWT, et c'est là que les vraies données ou "revendications" sont stockées. Les revendications sont des déclarations sur une entité (généralement un utilisateur) et toute autre donnée supplémentaire. En utilisant l'analogie précédente d'un colis, pensez-y comme au "contenu" du colis.

Il existe trois types de revendications :

**1. Revendications enregistrées :** Il s'agit de revendications prédéfinies recommandées pour des cas d'utilisation courants. Elles ne sont pas obligatoires mais sont très utiles pour l'interopérabilité. Elles incluent :

* `iss` – émetteur, qui a émis le token (par exemple, le domaine de votre application)

* `sub` – sujet, le sujet du token (par exemple, l'ID d'un utilisateur)

* `aud` – audience, l'audience du token (c'est-à-dire à qui le token est destiné – par exemple, une API spécifique)

* `exp` – **expiration**, la date d'expiration sous forme de timestamp

* `iat` – émis à, quand le token a été émis sous forme de timestamp

* `nbf` – non avant, quand le token devient valide (c'est-à-dire que le token ne peut pas être utilisé ou considéré comme valide avant ce timestamp)

* `jti` – ID JWT, un identifiant unique pour le token, utile pour prévenir les attaques par relecture ou la liste noire

**2. Revendications publiques :** Elles peuvent être définies par quiconque utilisant des JWT. Pour éviter les conflits de noms, il est bon de les enregistrer ou de les définir en utilisant un identifiant unique comme un URI.

**3. Revendications privées :** Il s'agit de revendications personnalisées créées pour partager des informations spécifiques entre des parties qui conviennent de les utiliser. Elles dépendent entièrement de vous et des besoins de votre application.

**Exemple de charge utile :**

```json
{
  "sub": "1234567890", // sujet
  "name": "John Doe", // revendication privée
  "admin": true, // revendication privée / rôle
  "iat": 1678886400, // Émis à un timestamp spécifique
  "exp": 1678890000  // Expire à un timestamp spécifique
}
```

Comme l'en-tête, cet objet JSON est également **encodé en Base64Url** (une variante sécurisée pour les URL de l'encodage Base64) pour former la deuxième partie de la chaîne JWT.

**Note importante :** *La charge utile est* ***encodée****, pas chiffrée.* Cela signifie que n'importe qui peut facilement décoder le JWT et lire son contenu. Ne mettez jamais d'informations sensibles (comme des mots de passe) directement dans la charge utile, sauf si le JWT lui-même est chiffré (ce qui est un processus séparé appelé JWE - JSON Web Encryption). La sécurité d'un JWT standard provient entièrement de la signature, qui empêche la falsification.

#### Signature

La signature, comme nous l'avons déjà discuté, est la partie la plus importante du JWT. Sans elle, il n'y a aucune protection appliquée au JWT, ce qui signifie qu'il n'y a aucun moyen de valider l'origine du token ou son intégrité.

La signature est créée en prenant l'**en-tête encodé**, la **charge utile encodée**, et une **clé secrète** (ou une clé privée si des algorithmes asymétriques comme RSA sont utilisés). Ceux-ci sont ensuite passés par l'algorithme cryptographique spécifié dans l'en-tête (champ `alg`). Pour HS256, une clé secrète partagée est utilisée. Pour RS256, une clé privée est utilisée pour signer, et une clé publique correspondante est utilisée pour vérifier. Nous aborderons la vérification bientôt.

Pensez-y comme à un sceau inviolable sur votre colis, ou mieux encore, à un sceau de cire sur une lettre. Si vous recevez votre lettre et que le sceau de cire a été brisé, vous croiriez naturellement que le contenu de la lettre peut ne pas être original et donc ne peut pas être considéré comme fiable.

En pseudo-code, cela ressemblerait à ceci :

`Signature = Algorithme( Base64Url(En-tête) + "." + Base64Url(Charge utile), CléSecrète )`

Le résultat de ce processus de signature est la signature, qui est également encodée en Base64Url pour former la troisième partie de la chaîne JWT.

À la fin de tout le processus, votre JWT ressemblerait à ceci :

`base64EncodedHeader.base64EncodedPayload.base64EncodedSignature`

### Signature asymétrique (RS256) expliquée

Lorsque qu'un JWT utilise un algorithme comme RS256 (Signature RSA avec SHA-256), il emploie un processus cryptographique **asymétrique** impliquant une paire de clés **publique** et **privée**. C'est là que la magie principale de la preuve d'authenticité et d'intégrité se produit sans avoir besoin de partager un secret.

#### Le processus de signature (par l'émetteur)

L'**expéditeur** (le serveur qui émet le JWT, comme Auth0) possède la **clé privée**. Cette clé est gardée absolument secrète et sécurisée. Voici les étapes :

1. **Préparer les données :** Le serveur prend l'en-tête (qui inclut l'algorithme) et la charge utile. Il les encode en Base64Url, puis les concatène avec un point : `Base64Url(En-tête) + "." + Base64Url(Charge utile)`.

   Par exemple, avec cet en-tête :

   ```json
   {
     "typ": "JWT",
     "alg": "RS256"
   }
   ```

   Et cette charge utile :

   ```json
   {
     "sub": "1234567890",
     "name": "John Doe",
     "admin": true,
     "iat": 1751494086,
     "exp": 1751497686
   }
   ```

   Cela créerait une chaîne `header.payload` encodée en Base64Url comme l'exemple animé ci-dessous :

   ![Gif animé du processus convertissant l'en-tête et la charge utile en chaîne encodée en base64](https://cdn.hashnode.com/res/hashnode/image/upload/v1751810671075/128fa652-fe2a-4413-a238-71531bfe67ae.gif align="center")

2. **Calculer le hachage :** Il calcule ensuite un **hachage** (en utilisant SHA-256 dans ce cas) de cette chaîne combinée d'en-tête et de charge utile.

3. **Signer le hachage :** Enfin, il signe ce hachage en utilisant sa clé privée. Ce hachage cryptographiquement transformé est la partie signature du JWT.

Le JWT est ensuite formé en concaténant l'en-tête encodé en Base64Url, la charge utile encodée en Base64Url et la signature encodée en Base64Url, séparés par des points : `header.payload.signature`.

Le segment supérieur ci-dessous montre le JWT complet (header.payload.signature) :

![Image affichant le JWT entièrement formé ainsi que l'en-tête et la charge utile d'origine](https://cdn.hashnode.com/res/hashnode/image/upload/v1751830473890/31da21a0-50db-4a48-b4c3-378c2ac1616a.png align="center")

### Le processus de vérification

C'est là que la magie opère, et c'est souvent un point de confusion. La clé publique ne "déchiffre" pas les données originales comme le fait une clé symétrique. Au lieu de cela, elle effectue un processus de **vérification** unique.

Le destinataire (le client ou un autre serveur qui doit vérifier le JWT) possède la **clé publique**. Cette clé n'a **pas** besoin d'être gardée secrète – elle peut être librement distribuée.

Voici une explication étape par étape :

1. **Séparer les parties :** La première chose que fait le destinataire est de diviser la chaîne JWT entrante en ses trois composants encodés en Base64Url : l'En-tête, la Charge utile et la Signature.

2. **Obtenir la clé publique :** Le vérificateur a besoin de la **clé publique** qui correspond à la clé privée utilisée par l'émetteur. Les clés publiques sont souvent disponibles via un **point de terminaison JWKS (JSON Web Key Set)** (par exemple, `votre-domaine.com/.well-known/jwks.json`).

3. **Recréer les données à hacher :** Le destinataire prend l'En-tête encodé en Base64Url reçu et la Charge utile encodée en Base64Url reçue. Il les combine exactement comme l'a fait l'émetteur : `EncodedHeader.EncodedPayload`.

4. **Calculer un hachage local (Hachage A) :** Cette chaîne combinée est ensuite soumise au même algorithme de hachage (par exemple, SHA-256) qui a été spécifié dans l'en-tête du JWT. Cela produit un nouveau hachage calculé localement (appelons cela **"Hachage A"**). Ce hachage local représente à quoi le contenu *devrait* ressembler s'il n'a pas été falsifié.

5. **"Désigner" la signature reçue avec la clé publique pour obtenir le hachage signé original (Hachage B) :** Il s'agit de l'étape cryptographique principale. Le vérificateur utilise la clé publique (obtenue à l'étape 2) pour effectuer une opération mathématique sur la signature reçue. Cette opération ne crée *pas* une nouvelle signature pour comparaison. Au lieu de cela, elle "désigne" ou "déchiffre" effectivement la signature pour révéler le **hachage original ("Hachage B")** qui a été produit par la clé privée de l'émetteur.

   * **Point crucial :** Ce processus est destiné à la **vérification de l'authenticité**, et non au déchiffrement de données confidentielles. La clé publique confirme que la signature a bien été créée par la clé privée correspondante, et dans le cadre de cette confirmation, elle retourne le hachage original qui *a été signé*.

6. **Comparer les hachages :** Le vérificateur a maintenant deux hachages :

   * **Hachage A :** Le hachage qu'il **a calculé localement** à partir de l'en-tête et de la charge utile reçus (de l'étape 4).

   * **Hachage B :** Le hachage original qui a été extrait de la Signature reçue en utilisant la clé publique (de l'étape 5)

7. **Si le Hachage A correspond au Hachage B :** Cela prouve deux choses critiques :

   1. **Authenticité :** Le token a bien été signé par le détenteur légitime de la clé privée correspondante (par exemple, Auth0).

   2. **Intégrité :** Le contenu de l'en-tête et de la charge utile n'a **pas été falsifié** depuis qu'il a été signé à l'origine. Si même un seul caractère dans l'en-tête ou la charge utile était changé, le Hachage A serait différent et ne correspondrait pas au Hachage B. Dans ce cas, le JWT est considéré comme valide et son contenu peut être considéré comme fiable.

8. **Si les hachages ne correspondent PAS :** Le token est considéré comme invalide et **doit être rejeté**. Cela indique soit que le JWT a été signé par une partie non autorisée (un token falsifié), soit que son en-tête ou sa charge utile a été modifié après sa signature.

![Diagramme de flux du processus de vérification asymétrique](https://cdn.hashnode.com/res/hashnode/image/upload/v1751813812291/de32c7b0-1f3c-4f26-995e-b5c618b104b3.png align="center")

### Analogie : Le cadenas et la clé pour les signatures asymétriques

**Clé privée :** Une clé spéciale et unique qui peut **verrouiller** une boîte (créer une signature). Seul le propriétaire possède cette clé.

**Clé publique :** Une clé largement distribuée qui peut **tester** si une boîte a été verrouillée par la clé privée correspondante. Elle ne peut pas verrouiller une nouvelle boîte, mais elle peut confirmer si un verrou existant est authentique.

Vous ne reverrouillez pas la boîte avec la clé publique. Vous utilisez la clé publique pour vérifier si le verrou existant (la signature) est authentique et correspond au contenu de la boîte.

## Signature symétrique : HS256 (HMAC avec SHA-256)

Alors que RS256 utilise une paire de clés (privée pour la signature, publique pour la vérification), de nombreux JWT que vous rencontrerez sont signés de manière symétrique, le plus souvent avec l'algorithme HS256. HS256 signifie **HMAC (Hash-based Message Authentication Code) avec SHA-256**.

La différence fondamentale ici est l'utilisation d'une seule clé secrète partagée pour *à la fois* la signature et la vérification.

### Comment fonctionne la signature HS256

1. **Clé secrète partagée :** L'émetteur (par exemple, votre fournisseur d'authentification) possède une seule clé secrète confidentielle. Cette clé est connue *uniquement* de l'émetteur et de toutes les parties (comme votre API) qui doivent vérifier le token.

2. **Combiner l'en-tête et la charge utile :** Tout comme avec la signature asymétrique, l'émetteur prend l'En-tête encodé en Base64Url (qui spécifie `"alg": "HS256"`) et la Charge utile encodée en Base64Url, et les **assemble** avec un point.

3. **Appliquer HMAC-SHA256 :** Cette chaîne combinée est ensuite alimentée dans l'algorithme HMAC-SHA256 avec la clé secrète. L'algorithme HMAC utilise la clé secrète pour créer un hachage unique (la signature) des données. En pseudo-code, cela ressemble à ceci :

   `Signature = HMAC-SHA256( Base64Url(En-tête) + "." + Base64Url(Charge utile), CléSecrète )`

4. **Former le JWT :** La signature résultante (qui est également encodée en Base64Url) est ajoutée à l'en-tête et à la charge utile avec un point, formant le JWT complet : `base64EncodedHeader.base64EncodedPayload.base64EncodedSignature`.

### Comment fonctionne la vérification HS256

Lorsque qu'un destinataire reçoit un JWT signé avec HS256, il passe par un processus de vérification.

Tout d'abord, il sépare les parties. Le JWT est divisé en ses trois composants encodés en Base64Url : En-tête, Charge utile et Signature, comme nous l'avons fait avec les JWT asymétriques.

Ensuite, il obtient la clé secrète partagée. Le destinataire doit également posséder la **même clé secrète exacte** que celle utilisée par l'émetteur pour signer le token. Cette clé n'est *pas* distribuée publiquement comme une clé publique – elle doit être provisionnée de manière sécurisée à toute entité qui doit vérifier les tokens.

Ensuite, il recalcule la signature. Le destinataire le fait en prenant l'En-tête encodé en Base64Url reçu et la Charge utile encodée en Base64Url, en les combinant, puis en réappliquant l'algorithme HMAC-SHA256 en utilisant la *même clé secrète*. Cela produit une nouvelle signature calculée localement.

Enfin, le destinataire compare la signature qu'il vient de calculer localement avec la signature qu'il a reçue dans le cadre du JWT.

* **Si les deux signatures correspondent :** Le token est considéré comme valide. Cela confirme son authenticité (il provient de quelqu'un qui connaît le secret) et son intégrité (il n'a pas été falsifié).

* **Si les signatures ne correspondent PAS :** Le token est invalide et doit être rejeté. Cela indique soit une falsification, soit qu'il a été signé avec une clé secrète différente et inconnue.

![Diagramme de flux du processus de vérification symétrique](https://cdn.hashnode.com/res/hashnode/image/upload/v1751814851136/a73b7af6-e92d-40f3-b1e3-c4bd2406ede9.png align="center")

### Différences et considérations clés :

* **Gestion des clés :** Avec HS256, la clé secrète doit être partagée et gardée confidentielle par *toutes* les parties impliquées dans la signature et la vérification. Cela peut être plus difficile à gérer de manière sécurisée à grande échelle par rapport au modèle de clé publique/privée, où seule la clé privée nécessite une stricte confidentialité.

* **Performance :** HS256 est généralement plus rapide à calculer que les algorithmes asymétriques comme RS256, ce qui le rend adapté aux scénarios à haut volume où la clé secrète peut être distribuée de manière sécurisée.

## JWT en action : Un flux d'authentification typique

Maintenant que vous comprenez comment les JWT sont structurés et signés, examinons comment ils sont typiquement utilisés dans une application web réelle. Ce flux d'authentification est un modèle courant que vous pourriez rencontrer.

### **Étape 1 : L'utilisateur se connecte :**

Un utilisateur ouvre une application cliente (par exemple, un navigateur web, une application mobile) et entre ses identifiants de connexion (nom d'utilisateur et mot de passe).

Le client envoie ces identifiants de manière sécurisée (toujours via HTTPS !) à un **serveur d'authentification** (comme Auth0, AWS Cognito ou votre propre point de terminaison d'authentification backend).

### **Étape 2 : Le serveur d'authentification émet un JWT :**

Le serveur d'authentification vérifie ensuite les identifiants de l'utilisateur. S'ils sont valides, il génère un nouveau JWT. Ce JWT contient des revendications (comme l'ID de l'utilisateur, les rôles, la date d'expiration) dans sa charge utile et est signé numériquement par la **clé privée** du serveur (pour les algorithmes asymétriques comme RS256) ou la **clé secrète** (pour les algorithmes symétriques comme HS256).

Le serveur envoie ensuite ce JWT signé au client.

### **Étape 3 : Le client stocke le JWT :**

Le client reçoit le JWT et le stocke généralement dans un endroit sécurisé, comme la mémoire du navigateur, le stockage de session ou un cookie HTTP-only. La méthode de stockage dépend du type de client et des considérations de sécurité.

### **Étape 4 : Le client effectue des appels API :**

Lorsque l'utilisateur souhaite accéder à une ressource protégée sur une API backend (par exemple, ses données de profil, un flux privé), le client inclut le JWT dans la demande.

La manière standard de le faire est d'envoyer le token dans l'en-tête `Authorization` de la requête HTTP, précédé du mot `Bearer` :

`Authorization: Bearer <votre_jwt_ici>`

### **Étape 5 : L'API vérifie le JWT et autorise la demande :**

Maintenant, l'API backend reçoit la demande et extrait le JWT de l'en-tête `Authorization`. L'API effectue ensuite le processus de vérification du JWT en fonction de l'algorithme :

* Elle vérifie les revendications du token, en particulier la revendication `exp` (expiration), pour s'assurer qu'il est toujours valide.

* Si le token est valide, l'API fait confiance aux revendications dans la charge utile (par exemple, l'ID de l'utilisateur) et procède à l'exécution de la demande, utilisant potentiellement les rôles de l'utilisateur pour déterminer s'il a la permission d'accéder à la ressource demandée.

* Si le token est invalide (mauvaise signature, expiré, etc.), l'API rejette la demande, généralement avec un statut HTTP 401 Non autorisé.

Ce flux est puissant car les JWT sont **sans état** : une fois émis, le serveur d'authentification n'a pas besoin de conserver un enregistrement des sessions actives. L'API peut vérifier le token de manière indépendante, ce qui simplifie la mise à l'échelle et réduit la charge du serveur.

## Bonnes pratiques de sécurité JWT et considérations

Bien que les JWT offrent des capacités d'authentification puissantes, leur utilisation sécurisée nécessite une attention particulière aux bonnes pratiques. Les mauvaises configurations ou les négligences peuvent entraîner des vulnérabilités significatives.

### **Utilisez toujours HTTPS/TLS :**

**Crucial :** Les JWT sont **encodés, pas chiffrés, par défaut**. Cela signifie que quiconque intercepte le token pendant la transmission peut facilement lire sa charge utile. Par conséquent, les JWT (et tout le trafic d'authentification) **doivent toujours être transmis via HTTPS (TLS)** pour chiffrer le canal de communication lui-même et empêcher l'écoute clandestine.

### **Protégez vos clés de signature :**

Qu'il s'agisse d'une clé privée (pour RS256) ou d'une clé secrète partagée (pour HS256), ces clés sont primordiales. Si un attaquant obtient accès à votre clé de signature, il peut forger des JWT valides, usurper l'identité des utilisateurs et compromettre votre système. Stockez ces clés de manière sécurisée, de préférence dans des services de gestion de clés dédiés.

### **Gardez les tokens d'accès de courte durée (revendication `exp`) :**

Vous devez toujours définir des temps d'expiration courts (par exemple, 5-15 minutes) pour vos JWT utilisés comme tokens d'accès. Cela minimise la fenêtre d'opportunité pour un attaquant si un token est compromis.

Étant donné que les JWT sont sans état, ils sont difficiles à révoquer immédiatement une fois émis. Une courte durée de vie est votre principale défense contre les tokens compromis.

### **Implémentez les tokens de rafraîchissement (pour des sessions plus longues) :**

Pour maintenir l'expérience utilisateur avec des tokens d'accès de courte durée, utilisez des **tokens de rafraîchissement**. Un token de rafraîchissement est un token séparé, de plus longue durée (généralement stocké de manière plus sécurisée) qui peut être échangé contre un nouveau token d'accès de courte durée lorsque le token actuel expire, sans nécessiter que l'utilisateur se réauthentifie. Les tokens de rafraîchissement *peuvent* être révoqués par le serveur, offrant un meilleur contrôle.

### **Ne mettez jamais de données sensibles dans la charge utile :**

Répétons ce point crucial : la charge utile du JWT est encodée en Base64Url, ce qui est facilement réversible. Ne mettez pas de mots de passe, d'informations personnelles identifiables (PII) hautement sensibles ou de données commerciales confidentielles directement dans la charge utile du JWT. N'incluez que des informations non sensibles ou publiques, ou des données déjà chiffrées par d'autres moyens.

### **Validez TOUTES les revendications lors de la vérification :**

Lors de la vérification d'un JWT, ne vérifiez pas seulement la signature. Validez toujours toutes les revendications pertinentes, y compris :

* `exp` (Expiration) : Assurez-vous que le token n'a pas expiré.

* `iss` (Émetteur) : Vérifiez que le token provient du serveur d'authentification attendu.

* `aud` (Audience) : Assurez-vous que le token est destiné à votre API/application spécifique.

* `nbf` (Non avant) : Vérifiez si le token est déjà actif.

### **Envisagez la révocation des tokens (pour les cas critiques) :**

Pour les situations nécessitant une révocation immédiate (par exemple, changement de mot de passe de l'utilisateur, désactivation de compte), les JWT sans état typiques sont difficiles à gérer. Les stratégies incluent :

* Des temps d'expiration courts (comme ci-dessus).

* Une liste noire/liste de révocation : Stockez le `jti` (ID JWT) des tokens révoqués dans une base de données, en vérifiant cette liste à chaque demande. Cela ajoute une recherche avec état mais offre une révocation immédiate.

## Merci d'avoir lu !

J'espère que vous avez trouvé ce tutoriel utile, et comme toujours, si vous souhaitez poser des questions ou entendre parler des articles à venir, vous pouvez toujours me suivre sur 'X', mon identifiant est @grantdotdev et me suivre en cliquant [ici](https://x.com/grantdotdev).