---
title: Comment sécuriser les applications mobiles – Une checklist de sécurité pour
  les applications mobiles
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-02T23:18:54.000Z'
originalURL: https://freecodecamp.org/news/how-to-secure-mobile-apps
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/mobile-app-security.jpg
tags:
- name: Application Security
  slug: application-security
- name: mobile app development
  slug: mobile-app-development
seo_title: Comment sécuriser les applications mobiles – Une checklist de sécurité
  pour les applications mobiles
seo_desc: "By Roger James\nSecurity has always been a major concern for businesses.\
  \ And this concern is even greater when it comes to mobile apps. \nToday every business\
  \ has a mobile app to connect more easily with their customers. And if that business\
  \ does not t..."
---

Par Roger James

La sécurité a toujours été une préoccupation majeure pour les entreprises. Et cette préoccupation est encore plus grande lorsqu'il s'agit d'applications mobiles.

Aujourd'hui, chaque entreprise dispose d'une application mobile pour se connecter plus facilement avec ses clients. Et si cette entreprise ne prend pas les protections de sécurité appropriées, cela peut mettre sa marque en danger.

Les appareils mobiles couvrent plusieurs systèmes d'exploitation et, étant donné la nature distribuée des composants, la sécurité des applications mobiles rencontre souvent des problèmes.

J'espère que votre entreprise est correctement sécurisée et que vous cherchez simplement une checklist de sécurité pour les applications mobiles pour l'avenir. Si c'est le cas, tant mieux pour vous – être propriétaire d'une entreprise signifie que vous devez prendre soin de la sécurité des applications mobiles.

**Mais selon une [enquête](https://www.pixelcrayons.com/blog/mobile-app-stats/?utm_source=freecodecamp&utm_medium=mobile%2Bapp%2Bdevelopment_sk&utm_campaign=website), plus de 75 % des applications mobiles échoueront aux tests de sécurité de base.**

De nombreux employés téléchargent des applications depuis les magasins d'applications et utilisent des applications mobiles qui peuvent accéder aux actifs de l'entreprise ou effectuer des fonctions commerciales. Et malheureusement, ces applications offrent peu ou pas de garanties de sécurité. Elles sont exposées à des attaques et à des violations des politiques de sécurité de l'entreprise en permanence.

Je sais que personne ne veut faire partie de cet échec. C'est pourquoi vous devez suivre une checklist de sécurité pour les applications mobiles.

## Renforcer l'authentification

Pour prévenir les accès non autorisés et les attaques par devinettes de mots de passe, vous devez mettre en place une authentification multifactorielle. Les trois principaux facteurs d'authentification sont :

* quelque chose que l'utilisateur connaît, comme un mot de passe ou un code PIN
* quelque chose que l'utilisateur possède, comme un appareil mobile
* ou quelque chose que l'utilisateur est, comme une empreinte digitale.

Combiner l'authentification basée sur un mot de passe avec un certificat client, un identifiant d'appareil ou un mot de passe à usage unique réduit considérablement le risque d'accès non autorisé. Vous pouvez également mettre en place des restrictions basées sur l'heure de la journée et la localisation pour prévenir la fraude.

## Chiffrer les communications mobiles

Avec des menaces comme l'espionnage et les attaques de type "man-in-the-middle" sur les réseaux WiFi et cellulaires, les services informatiques doivent s'assurer que toutes les communications entre les applications mobiles et les serveurs d'applications sont chiffrées.

Un chiffrement robuste qui utilise des clés SSL de 4096 bits et des échanges de clés basés sur des sessions peut empêcher même les pirates les plus déterminés de déchiffrer les communications.

En plus de chiffrer le trafic, les services informatiques doivent confirmer que les données au repos – les données sensibles stockées sur les téléphones des utilisateurs – sont également chiffrées. Pour les données ultra-sensibles, les services informatiques peuvent vouloir empêcher les données d'être jamais téléchargées sur l'appareil de l'utilisateur final.

## Corriger les vulnérabilités des applications et des systèmes d'exploitation

Les vulnérabilités récentes d'Android et d'iOS, telles que [Stagefright](https://play.google.com/store/apps/details?id=com.zimperium.stagefrightdetector&hl=en_IN) et [XcodeGhost](https://www.macrumors.com/2015/09/20/xcodeghost-chinese-malware-faq/), ont exposé les utilisateurs mobiles à des attaques.

En plus des failles des systèmes d'exploitation mobiles, les services informatiques doivent faire face à une succession sans fin de mises à jour et de correctifs d'applications.

Pour protéger les utilisateurs mobiles des attaques, les services informatiques doivent vérifier les appareils mobiles et s'assurer que les derniers correctifs et mises à jour ont été appliqués.

## Protéger contre le vol d'appareils

Chaque année, des millions d'appareils mobiles sont perdus ou volés. Pour s'assurer que les données sensibles ne tombent pas entre de mauvaises mains, les services informatiques doivent fournir un moyen d'effacer à distance les données sensibles ou – mieux encore – s'assurer que les données ne sont jamais stockées sur les appareils mobiles en premier lieu.

Pour les appareils appartenant aux employés, les services informatiques doivent verrouiller ou effacer les informations de l'entreprise tout en laissant les applications et fichiers personnels intacts. Lorsque l'appareil est retrouvé ou remplacé, les services informatiques doivent pouvoir restaurer rapidement les applications et les données des utilisateurs.

## Analyser les applications mobiles pour détecter les logiciels malveillants

Éliminez les logiciels malveillants et les publiciels en testant les applications pour détecter les comportements malveillants. Les logiciels malveillants peuvent être détectés à l'aide d'outils de sandboxing virtuel ou de scanning basé sur les signatures. Pour les solutions de workspace mobile ou de mobile virtuel, effectuez des analyses de logiciels malveillants sur le serveur.

## Protéger les données de l'application sur votre appareil

Assurez-vous que les développeurs ne stockent aucune donnée sensible sur leurs appareils. Si vous devez stocker des données sur l'appareil pour une raison quelconque, assurez-vous d'abord qu'elles sont chiffrées/protégées. Et ensuite, ne les stockez que dans des fichiers, des magasins de données et des bases de données.

Si vous utilisez les dernières technologies de chiffrement, vous pouvez obtenir un niveau de sécurité plus élevé.

## Sécuriser la plateforme

Votre plateforme doit être correctement sécurisée et contrôlée. Ce processus consiste à détecter les [téléphones jailbreakés](https://www.scribd.com/document/226019655/IOS-Application-Security-Part-24-Jailbreak-Detection-and-Evasion) et à empêcher l'accès à d'autres services lorsque cela est nécessaire.

## Prévenir les fuites de données

Pour éviter les fuites de données tout en permettant aux utilisateurs d'installer des applications personnelles sur leurs appareils mobiles, les services informatiques doivent séparer les applications professionnelles des applications personnelles.

Créer des espaces de travail mobiles sécurisés aide à prévenir l'accès des logiciels malveillants aux applications de l'entreprise et empêche les utilisateurs de copier, sauvegarder ou distribuer des données sensibles.

### Pour une prévention des fuites de données ultra-sensibles :

* Contrôler l'accès au presse-papiers pour prévenir les fonctions de copier-coller
* Bloquer les captures d'écran
* Empêcher les utilisateurs de télécharger des fichiers confidentiels sur leur téléphone ou de sauvegarder des fichiers sur des sites de partage de fichiers ou des appareils ou lecteurs connectés.
* Filigraner les fichiers sensibles avec les noms d'utilisateur et les horodatages des utilisateurs

## Optimiser la mise en cache des données

Saviez-vous que les appareils mobiles stockent généralement des données en cache afin d'améliorer les performances d'une application ? Cela constitue une cause majeure de problèmes de sécurité, car ces applications et appareils deviennent plus vulnérables et il est relativement facile pour les attaquants de violer et de déchiffrer les données en cache. Cela entraîne souvent le vol de données utilisateur.

Vous pouvez exiger un mot de passe pour accéder à l'application si la nature de vos données est extrêmement sensible. Cela aidera à réduire les vulnérabilités associées aux données en cache.

Ensuite, mettez en place un processus automatique qui efface les données en cache chaque fois que l'appareil est redémarré. Cela aide à réduire le cache et à atténuer les préoccupations de sécurité.

## Isoler les informations de l'application

Vous devez séparer toutes les informations accessibles via un appareil mobile des données d'un utilisateur. Et ce processus d'isolement des informations nécessite quelques niveaux de protection autour des applications déployées par l'entreprise. Ainsi, les données de l'entreprise seront séparées des données privées de l'employé ainsi que de l'application destinée aux consommateurs.

Ce processus d'isolement des données devrait augmenter la satisfaction et la productivité de vos clients, tout en s'assurant qu'ils sont conformes à vos règles de sécurité.

L'utilisation d'un modèle basé sur des conteneurs peut vous aider dans ce cas. La sécurité est souvent plus stricte et ne fera aucun compromis à aucun niveau de transmission. Cela aide finalement à éliminer le risque de perte de données de l'entreprise.

## Mots de la fin

Avant de lancer votre entreprise – ou même si vous en dirigez déjà une – essayez de mettre en œuvre cette checklist de sécurité pour les applications mobiles. Cela vous aidera à protéger votre entreprise contre toute fraude ou perte.

Je sais que la sécurité est une préoccupation majeure et ne peut pas simplement être résolue en suivant quelques étapes. Si vous avez besoin d'aide, contactez une [entreprise de développement d'applications mobiles](https://www.pixelcrayons.com/mobile-app-development/?utm_source=freecodecamp&utm_medium=mobile%2Bapp%2Bdevelopment_sk&utm_campaign=website) qui peut vous guider tout au long du processus.