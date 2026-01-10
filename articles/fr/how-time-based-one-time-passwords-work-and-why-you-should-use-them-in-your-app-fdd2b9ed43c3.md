---
title: Comment fonctionnent les mots de passe à usage unique basés sur le temps et
  pourquoi vous devriez les utiliser dans votre application.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-18T23:14:56.000Z'
originalURL: https://freecodecamp.org/news/how-time-based-one-time-passwords-work-and-why-you-should-use-them-in-your-app-fdd2b9ed43c3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NtO_nq3H7lfuDd9nL9pRWg.jpeg
tags:
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Two-factor authentication
  slug: two-factor-authentication
seo_title: Comment fonctionnent les mots de passe à usage unique basés sur le temps
  et pourquoi vous devriez les utiliser dans votre application.
seo_desc: 'By Prakash Sharma

  With the increase in cyber security threats, it has become more and more necessary
  to upgrade the security standards of your web applications. You need to make sure
  your users’ accounts are safe.

  Nowadays, a lot of online web applic...'
---

Par Prakash Sharma

Avec l'augmentation des menaces de cybersécurité, il est devenu de plus en plus nécessaire de mettre à niveau les normes de sécurité de vos applications web. Vous devez vous assurer que les comptes de vos utilisateurs sont sécurisés.

De nos jours, de nombreuses applications web en ligne demandent aux utilisateurs d'ajouter une couche supplémentaire de sécurité pour leur compte. Ils le font en activant l'authentification à deux facteurs. Il existe diverses méthodes pour implémenter l'authentification à deux facteurs, et l'authentification TOTP (l'algorithme de mot de passe à usage unique basé sur le temps) en est une.

Cet article explique ce que c'est, et comment et pourquoi l'utiliser. Mais avant de comprendre cela, examinons d'abord brièvement ce que signifie l'authentification à deux facteurs.

### Qu'est-ce que l'authentification à deux facteurs ?

L'authentification à deux facteurs (ou authentification multifactorielle) est simplement une couche supplémentaire de sécurité pour le compte d'un utilisateur. Cela signifie que, après avoir activé l'authentification à deux facteurs, l'utilisateur doit passer par une étape supplémentaire pour se connecter avec succès. Par exemple, les étapes habituelles pour se connecter à un compte sont :

![Image](https://cdn-media-1.freecodecamp.org/images/ZqTllcloHTWpzWYDh-YsnOggoitxJSicGiVj)

Mais après avoir activé l'authentification à deux facteurs, les étapes ressemblent à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/inJY5oemUFqSO2g5G6HvPpNt0I74XF0hlRKV)

Ainsi, cela ajoute une étape supplémentaire au processus de connexion. Cette méthode est plus sécurisée, car un criminel ne peut pas accéder au compte de l'utilisateur à moins qu'il n'ait accès à la fois au mot de passe régulier de l'utilisateur et au mot de passe à usage unique.

Actuellement, il existe deux méthodes largement utilisées pour obtenir ce mot de passe à usage unique :

1. **Basé sur SMS** : Dans cette méthode, chaque fois que l'utilisateur se connecte, il reçoit un message texte sur son numéro de téléphone enregistré, qui contient un mot de passe à usage unique.
2. **Basé sur TOTP** : Dans cette méthode, lors de l'activation de l'authentification à deux facteurs, l'utilisateur est invité à scanner une image QR à l'aide d'une application spécifique pour smartphone. Cette application génère ensuite en continu le mot de passe à usage unique pour l'utilisateur.

La méthode basée sur SMS ne nécessite aucune explication. Elle est facile, mais elle a ses propres problèmes, comme l'attente du SMS à chaque tentative de connexion, les problèmes de sécurité, etc. La méthode basée sur TOTP devient populaire en raison de ses avantages par rapport à la méthode basée sur SMS. Alors, comprenons comment fonctionne la méthode basée sur TOTP.

### Comment fonctionne la méthode basée sur TOTP

Avant de comprendre cela, discutons d'abord des problèmes que cette méthode résoudra pour nous.

En utilisant la méthode TOTP, nous créons un mot de passe à usage unique du côté de l'utilisateur (au lieu du côté serveur) via une application pour smartphone.

Cela signifie que les utilisateurs ont toujours accès à leur mot de passe à usage unique. Ainsi, cela évite au serveur d'envoyer un message texte chaque fois que l'utilisateur tente de se connecter.

De plus, le mot de passe généré change après un certain intervalle de temps, il se comporte donc comme un mot de passe à usage unique.

Super ! Maintenant, comprenons le fonctionnement de la méthode TOTP et essayons d'implémenter la solution ci-dessus nous-mêmes. Notre exigence ici est de créer un mot de passe du côté de l'utilisateur, et ce mot de passe doit continuer à changer.

Voici une façon d'implémenter cette solution :

```
Lorsque l'utilisateur active l'authentification à deux facteurs :
```

```
1. Le serveur backend crée une clé secrète pour cet utilisateur particulier.2. Le serveur partage ensuite cette clé secrète avec l'application téléphone de l'utilisateur.3. L'application téléphone initialise un compteur.4. L'application téléphone génère un mot de passe à usage unique en utilisant cette clé secrète et le compteur.5. L'application téléphone change le compteur après un certain intervalle et régénère le mot de passe à usage unique le rendant dynamique.
```

Cela devrait fonctionner, mais il y a trois problèmes principaux avec cela :

1. Comment l'application générera-t-elle un mot de passe à usage unique en utilisant une clé secrète et un compteur ?
2. Comment le compteur sera-t-il mis à jour ? Comment le serveur web gardera-t-il une trace du compteur ?
3. Comment le serveur partagera-t-il la clé secrète avec l'application du téléphone ?

La solution au premier problème est définie dans l'algorithme HOTP.

### Comprendre HOTP :

HOTP signifie « HMAC-Based One-Time Password ». Cet algorithme a été publié en tant que [RFC4226](https://tools.ietf.org/html/rfc4226) par l'[Internet Engineering Task Force](https://en.wikipedia.org/wiki/Internet_Engineering_Task_Force) (IETF). HOTP définit un algorithme pour créer un mot de passe à usage unique à partir d'une clé secrète et d'un compteur.

Vous pouvez utiliser cet algorithme en deux étapes :

1. La première étape consiste à créer un hachage [HMAC](https://en.wikipedia.org/wiki/HMAC) à partir d'une clé secrète et d'un compteur.

```
// Obtenir le hachage HMAC (en utilisant l'algorithme de hachage SHA-1) par secretKey et counter
```

```
hmacHash = HMAC-SHA-1(secretKey, counter);
```

2. Dans ce code, la sortie serait une chaîne de 20 octets. Cette longue chaîne n'est pas adaptée comme mot de passe à usage unique. Nous avons donc besoin d'un moyen de tronquer cette chaîne. HOTP définit un moyen de tronquer cette chaîne à la longueur souhaitée.

```
// hmacHash[19] signifie le 19ème octet de la chaîne.offset = hmacHash[19] & 0xf;
```

```
truncatedHash = (hmacHash[offset++] & 0x7f) << 24 | (hmacHash[offset++] & 0xff) << 16 | (hmacHash[offset++] & 0xff) << 8 | (hmacHashh[offset++] & 0xff);
```

```
finalOTP = (truncatedHash % (10 ^ numberOfDigitsRequiredInOTP));
```

Cela peut sembler effrayant, mais ce n'est pas le cas. Dans cet algorithme, nous obtenons d'abord `offset` qui est les 4 derniers bits de `hmacHash[19]`. Après cela, nous concaténons les octets de `hmacHash[offset]` à `hmacHash[offset+3]` et stockons les 31 derniers bits dans `truncatedHash`. Enfin, en utilisant une simple opération modulo, nous obtenons le mot de passe à usage unique qui a une longueur raisonnable.

Cela définit assez bien l'algorithme HOTP. Le document [RFA4226](https://tools.ietf.org/html/rfc4226) explique pourquoi c'est la manière la plus sécurisée d'obtenir un mot de passe à usage unique à partir de ces deux valeurs.

Super ! Nous avons donc trouvé un moyen d'obtenir un mot de passe à usage unique en utilisant une clé secrète et un compteur. Mais qu'en est-il du deuxième problème ? Comment garder une trace du compteur ?

La solution au deuxième problème se trouve dans le TOTP.

### Comprendre TOTP :

TOTP signifie « Time-Based One-Time Password ». Cela a été publié en tant que [RFC6238](https://tools.ietf.org/html/rfc6238) par [IETF](https://en.wikipedia.org/wiki/Internet_Engineering_Task_Force).

Un TOTP utilise l'algorithme HOTP pour obtenir le mot de passe à usage unique. La seule différence est qu'il utilise le « Temps » à la place du « compteur », et cela donne la solution à notre deuxième problème.

Cela signifie qu'au lieu d'initialiser le compteur et de le suivre, nous pouvons utiliser le temps comme compteur dans l'algorithme HOTP pour obtenir l'OTP. Comme un serveur et un téléphone ont tous deux accès au temps, aucun d'eux n'a à garder une trace du compteur.

De plus, pour éviter le problème des différents fuseaux horaires du serveur et du téléphone, nous pouvons utiliser un [timestamp Unix](https://en.wikipedia.org/wiki/Unix_time), qui est indépendant des fuseaux horaires.

Cependant, le temps Unix est défini en secondes, donc il change chaque seconde. Cela signifie que le mot de passe généré changera chaque seconde, ce qui n'est pas bon. Au lieu de cela, nous devons ajouter un intervalle significatif avant de changer le mot de passe. Par exemple, l'application Google Authenticator change le code toutes les 30 secondes.

```
counter = currentUnixTime / 30
```

Nous avons donc résolu le problème du compteur. Maintenant, nous devons aborder notre troisième problème : partager la clé secrète avec l'application téléphone. Ici, un code QR peut nous aider.

### Utiliser un code QR

Bien que nous puissions demander aux utilisateurs de taper la clé secrète directement dans leur application téléphone, nous voulons rendre les clés secrètes assez longues pour des raisons de sécurité. Demander à l'utilisateur de taper une chaîne aussi longue ne serait pas une expérience conviviale.

Puisque la majorité des smartphones sont équipés d'une caméra, nous pouvons l'utiliser et demander à l'utilisateur de scanner un code QR pour obtenir la clé secrète. Nous devons donc convertir la clé secrète en code QR et la montrer à l'utilisateur.

Nous avons résolu les trois problèmes ! Et maintenant vous savez comment fonctionne TOTP. Voyons comment l'implémenter dans une application.

### Comment implémenter TOTP

Il existe certaines applications téléphoniques gratuites (comme Google Authenticator App, Authy, etc.) disponibles qui peuvent générer un OTP pour l'utilisateur. Par conséquent, dans la plupart des cas, créer votre propre application téléphone n'est pas nécessaire.

Les pseudo-codes suivants expliquent une façon d'implémenter l'authentification à deux facteurs basée sur TOTP dans une application web.

```
Lorsque l'utilisateur demande à activer l'authentification à deux facteurs
```

```
// Générer une clé secrète de longueur 20.secretKey = generateSecretKey(20);
```

```
// Sauvegarder cette clé secrète dans la base de données pour cet utilisateur particulier.saveUserSecretKey(userId, secretKey);
```

```
// convertir cette clé secrète en image qr.qrCode = convertToQrCode(secretKey);
```

```
// envoyer l'image qr en réponse response(qrCode);
```

L'utilisateur est invité à scanner ce code QR. Lorsque l'application téléphone scanne le code QR, elle obtient la clé secrète de l'utilisateur. En utilisant cette clé secrète, le temps Unix actuel et l'algorithme HOTP, l'application téléphone générera et affichera le mot de passe.

Nous demandons à l'utilisateur de taper le code généré après avoir scanné le code QR. Cela est nécessaire, car nous voulons nous assurer que l'utilisateur a scanné avec succès l'image et que l'application téléphone a généré avec succès le code.

```
L'utilisateur tape le code affiché dans l'application.
```

```
// Récupérer la clé secrète de la base de données.secretKey = getSecretKeyOfUser(userId);
```

```
if (codeTypedByUser == getHOTP(secretKey, currentUnixTime / 30)) {   enableTwoFactorAuthentication(userId);}
```

Ici, nous utilisons l'algorithme HOTP côté serveur pour obtenir l'authentification basée sur OTP à partir de la clé secrète et du temps Unix actuel. Si cet OTP est le même que celui tapé par l'utilisateur, alors nous pouvons activer l'authentification à deux facteurs pour cet utilisateur.

Maintenant, après chaque opération de connexion, nous devons vérifier si cet utilisateur particulier a activé l'authentification à deux facteurs. Si elle est activée, alors nous demandons le mot de passe à usage unique affiché dans l'application téléphone. Et si ce code tapé est correct, l'utilisateur est authentifié.

```
L'utilisateur tape le code affiché dans l'application téléphone pour se connecter
```

```
// Récupérer la clé secrète de la base de données.secretKey = getSecretKeyOfUser(userId);
```

```
if (codeTypedByUser == getHOTP(secretKey, currentUnixTime)) {   signIn(userId);}
```

### Que se passe-t-il si l'utilisateur perd le code ?

Il existe plusieurs façons d'aider l'utilisateur à récupérer le code. Habituellement, lorsqu'ils activent l'authentification à deux facteurs, nous pouvons leur montrer la clé secrète ainsi que le code QR et leur demander de sauvegarder ce code quelque part en sécurité.

Des applications comme Google Authenticator App vous permettent de générer le mot de passe en entrant directement la clé secrète. Si l'utilisateur perd le code, il peut entrer cette clé secrète sauvegardée en sécurité dans l'application téléphone pour générer à nouveau l'OTP.

Si nous avons le numéro de téléphone de l'utilisateur, nous pouvons également utiliser la méthode basée sur SMS pour envoyer un OTP à l'utilisateur afin de l'aider à récupérer le code.

### Conclusion

L'authentification à deux facteurs gagne en popularité. De nombreuses applications web l'implémentent pour une sécurité supplémentaire.

Contrairement à la méthode basée sur SMS, la méthode TOTP ne nécessite pas non plus beaucoup d'efforts supplémentaires. Cette fonctionnalité vaut donc la peine d'être implémentée pour toute application.