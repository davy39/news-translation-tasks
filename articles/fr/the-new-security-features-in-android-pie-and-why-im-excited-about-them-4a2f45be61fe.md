---
title: Les nouvelles fonctionnalités de sécurité dans Android Pie et pourquoi je suis
  enthousiaste à leur sujet
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-27T17:29:15.000Z'
originalURL: https://freecodecamp.org/news/the-new-security-features-in-android-pie-and-why-im-excited-about-them-4a2f45be61fe
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UL2cOeH9M7dVfIe1k5qlrw.jpeg
tags:
- name: Android
  slug: android
- name: mobile app development
  slug: mobile-app-development
- name: Security
  slug: security
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: Les nouvelles fonctionnalités de sécurité dans Android Pie et pourquoi
  je suis enthousiaste à leur sujet
seo_desc: 'By Onur Tuna

  I gave a talk at the Google Developer Group Devfest 18 in Ankara about Android as
  I do every year. Quite likely this was the last talk I will give on Android. I talked
  about one of the big improvements in the latest version of Android. T...'
---

Par Onur Tuna

J'ai donné une conférence au Google Developer Group Devfest 18 à Ankara sur Android, comme je le fais chaque année. Il est fort probable que ce soit la dernière conférence que je donnerai sur Android. J'ai parlé de l'une des grandes améliorations de la dernière version d'Android. Pour moi, cela a été l'amélioration Android la plus passionnante à ce jour. Il y a beaucoup de nouvelles mises à jour de sécurité et de fonctionnalités dans Android Pie, et je veux les présenter brièvement ici.

> Vous pouvez obtenir ma présentation [ici](https://drive.google.com/file/d/1OzDPj-8urX5tRpBUJiSVM2MOUUao45-K/view?usp=sharing).

#### Restriction sur l'utilisation du micro ou de la caméra en arrière-plan

Les applications ne pourront pas utiliser votre micro ou votre caméra en arrière-plan avec Android Pie. Il s'agit de l'une des fonctionnalités de sécurité les plus importantes de ce nouveau système Android.

![Image](https://cdn-media-1.freecodecamp.org/images/XZOMpqVe7lZvCv-5Wsm06tNACR1hgPE5bDwu)

Les applications ne pourront utiliser votre micro ou votre caméra que si elles sont activement utilisées à l'écran. Si vous avez des craintes que certaines applications vous écoutent, vous pouvez être sûr qu'aucune application ne peut vous écouter secrètement avec Android Pie.

Bien que cette mesure empêche les applications d'écouter vos conversations, Google pourra toujours vous écouter. « OK Google. » ?

Au fait, aucune application ne pourra utiliser d'autres capteurs que le micro et la caméra.

#### Nouveau mode de verrouillage

![Image](https://cdn-media-1.freecodecamp.org/images/yUjuzkTOaouvv5YQ8CoA7ag7-bZeucj4qGGP)

Lorsque l'authentification par empreinte digitale a été introduite pour la première fois, elle a aidé tout le monde. Savez-vous combien de fois un humain moyen authentifie son téléphone mobile dans une journée ? Oui. Trop souvent.

Voici le problème : il existe de nombreuses histoires sur la façon dont la police ou des personnes mal intentionnées pourraient vous forcer à déverrouiller votre téléphone avec votre empreinte digitale pour le fouiller. N'importe qui pourrait vous forcer à déverrouiller votre téléphone avec votre identifiant facial pour accéder à votre vie numérique (de nos jours, c'est votre vie réelle).

Vous pouvez désactiver l'authentification par empreinte digitale et par reconnaissance faciale dans Android Pie en activant le mode de verrouillage. Seuls votre code PIN, votre motif ou votre mot de passe fonctionneront lorsqu'il est activé. Cependant, cette fonctionnalité ne sera pas nécessaire dans votre vie quotidienne. Il est simplement bon de l'avoir pour les situations à haut risque.

#### **HTTPS est le protocole par défaut pour les applications**

Aujourd'hui, la plupart des gens savent que les sites web qui ont une clé verte verrouillée sont suffisamment sécurisés pour y entrer. Vous pouvez rechercher cette clé dans votre navigateur. Cependant, vous ne pouvez pas savoir si l'application que vous utilisez effectue des appels vers des services HTTPS.

Toute application régulière envoie des données sur Internet. Toute personne mal intentionnée peut lire ces données que vous envoyez, sauf si elles sont chiffrées. HTTPS garantit que la transaction est chiffrée. Android obligera les développeurs à envoyer des données via HTTPS pour s'assurer que les données envoyées depuis votre téléphone seront chiffrées.

#### **La restauration de votre appareil nécessitera un code d'accès**

![Image](https://cdn-media-1.freecodecamp.org/images/Aw96iyrmcpvoSVchcozPV159UoIdANOD7H-1)

Avec Android Pie, vous restaurerez votre appareil en utilisant votre code PIN, votre motif ou votre mot de passe. L'empreinte digitale ou l'identifiant facial a suffi pour restaurer l'appareil jusqu'à présent. Cependant, cette simplicité est venue avec une certaine vulnérabilité. Une deuxième couche d'authentification a été introduite pour restaurer votre appareil de manière plus sécurisée. Soyez conscient que si vous oubliez le code PIN, vous ne pourrez pas restaurer votre appareil.

#### **Le ton d'alerte lorsque votre appel est enregistré**

Il existe de nombreuses applications qui peuvent enregistrer des appels. Cela a été une grande vulnérabilité jusqu'à présent. Il y a deux cas : toute application peut enregistrer votre appel, ou quelqu'un avec qui vous parlez peut enregistrer l'appel.

Maintenant, si vous enregistrez un appel, un ton d'alerte sera envoyé périodiquement à vous et à la personne avec qui vous parlez. Android Pie met fin à cette paranoïa de manière permanente.

J'ai essayé de présenter les améliorations significatives d'Android Pie avec ce post. Bien qu'il y ait beaucoup d'autres améliorations, ce sont celles que j'ai trouvées les plus importantes. Android Pie sera la version d'Android la plus sécurisée à ce jour.