---
title: Il est facile de tromper le scanner d'empreintes digitales de votre téléphone.
  Voici comment nous devrions le corriger.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-24T15:36:53.000Z'
originalURL: https://freecodecamp.org/news/it-is-easy-to-trick-the-mobile-phones-fingerprint-scanner-d8d7f509d128
coverImage: https://cdn-media-1.freecodecamp.org/images/1*fPDbcBXDvkEgZ5mp9xfF8A.jpeg
tags:
- name: Android
  slug: android
- name: Apple
  slug: apple
- name: Security
  slug: security
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: Il est facile de tromper le scanner d'empreintes digitales de votre téléphone.
  Voici comment nous devrions le corriger.
seo_desc: 'By Nikhil Dwivedi

  Early last week, I was setting up fingerprint sensors on my new iPhone. That’s when
  my brother, @Prateek , came up with an idea to test these mobile fingerprint sensors.

  The test was to scan his finger along with mine at the time of...'
---

Par Nikhil Dwivedi

Au début de la semaine dernière, je configurais les capteurs d'empreintes digitales sur mon nouvel iPhone. C'est alors que mon frère, [_@Prateek_](https://twitter.com/prateekdwv), a eu l'idée de tester ces capteurs d'empreintes digitales mobiles.

Le test consistait à scanner son doigt en même temps que le mien au moment de la configuration de l'empreinte digitale. Vous savez comment ces appareils vous demandent de soulever puis de reposer votre doigt plusieurs fois pour capturer tous les angles possibles. Nous l'avons fait — son doigt a été scanné plusieurs fois lorsque le téléphone s'attendait à ce que je soulève et repose uniquement mon doigt.

![Image](https://cdn-media-1.freecodecamp.org/images/ihb6oUoreF0lZP3x6FOX26g5xcBIp7uwywOt)
_Image montrant la configuration du scan d'empreinte digitale sur iPhone_

À ma grande surprise, nous avons réussi à tromper le téléphone. La configuration était terminée, et maintenant nous pouvions tous les deux utiliser notre doigt pour déverrouiller le téléphone. Voici à quoi ressemblaient les paramètres — un seul doigt configuré, et nous pouvions tous les deux déverrouiller le téléphone.

![Image](https://cdn-media-1.freecodecamp.org/images/ZntDoKdtDzZSxQuK1MKHICDLsmt6ieOiDvuZ)
_Page des paramètres de l'iPhone montrant un seul doigt configuré_

La pensée nous est venue : est-ce une sorte de bug, ou quoi ? Pour l'instant, c'était le moment d'un exercice amusant — essayer avec tous les autres téléphones qui supportent la reconnaissance d'empreintes digitales.

Nous avons donc commencé avec divers téléphones Android, certains avec ROM stock et d'autres avec des systèmes d'exploitation personnalisés de tiers comme Micromax, Lenovo et Xiaomi. Le résultat était le même pour tous. Nous pouvions chacun utiliser notre doigt pour déverrouiller le même téléphone alors qu'un seul doigt était configuré.

### Commençons par comprendre comment fonctionnent ces scanners d'empreintes digitales mobiles

En restant sur le sujet, il existe deux technologies populaires et fondamentales derrière la reconnaissance d'empreintes digitales dans les téléphones mobiles.

**Scanner optique** — cette technique utilise une image optique pour capturer diverses images de votre doigt. Une sorte de caméra de haute précision et quelques LED font le travail ici. Le logiciel compare ensuite ces images bidimensionnelles avec l'image prise à partir du doigt scanné.

Puisque ce n'est essentiellement qu'une image qui est comparée, ces scanners sont faciles à tromper. Une image d'un doigt imprimée à l'aide d'une imprimante haute résolution suffit pour tromper ces types de scanners.

**Scanner capacitif** — ici, un réseau de condensateurs capture le motif à partir de l'image scannée. Un circuit électrique complexe en dessous capture les données et celles-ci sont utilisées pour comparer le doigt scanné.

Cette technique est beaucoup plus sécurisée et est difficile à tromper. Une image haute définition d'un doigt ne peut pas être utilisée pour déverrouiller le téléphone. Le téléphone Samsung Galaxy S8 affirme utiliser cette technique.

### _Maintenant, place au débat : est-ce correct ou non ?_

Au début, lorsque vous voyez cela se produire, vous pouvez dire que quelque chose d'inhabituel se passe. Pour garder votre scanner d'empreintes digitales sécurisé, les composants suivants sont importants :

* _Technique de numérisation_ — matériel utilisé pour scanner le doigt et extraire les données/motifs.
* _Stockage_ — Base de données où les données/le motif de l'empreinte digitale sont stockés.
* _Algorithme_ — utilisé pour stocker et comparer le motif scanné.

![Image](https://cdn-media-1.freecodecamp.org/images/ucfJ-wZD8S9EGf7ptKgFV6bY8FvogXEamMby)
_Architecture générale du scanner d'empreintes digitales mobiles_

Pour la sécurité globale, l'enregistrement de l'empreinte digitale est aussi important que la référence à la base de données pour la vérification. Il semble y avoir un défaut et une inefficacité dans la manière dont les empreintes digitales sont stockées.

En examinant le cas ci-dessus, il apparaît que diverses impressions d'empreintes digitales recueillies au moment de la configuration sont stockées comme un ensemble indépendant de données. Lorsque vous scannez un doigt pour déverrouiller l'appareil, le scan est comparé à un tableau de la représentation binaire des doigts qui ont été scannés au moment de la configuration. _Possiblement, c'est ainsi que nous avons pu tromper le téléphone en scannant le doigt d'une autre personne au moment de la configuration._

![Image](https://cdn-media-1.freecodecamp.org/images/pJFbTm37qw0toUb4pfJO2v7FuYAGXuYSozuz)
_Représentation — Un tableau d'empreintes digitales, stocké au moment de la configuration. [source](http://www.mdpi.com/1424-8220/10/5/4206/htm" rel="noopener" target="_blank" title=")_

Il semble y avoir un problème conceptuel et fondamental dans le fonctionnement actuel du système.

Je ne peux pas revendiquer de cas d'utilisation où cela pourrait entraîner une faille de sécurité. Mais puisque l'adoption de l'authentification basée sur les empreintes digitales augmente rapidement, et que son utilisation va au-delà du simple déverrouillage de votre appareil, il est logique d'améliorer la technologie pour combler cette lacune.

### Alors, que faire ensuite ?

Au moment de la configuration, les scans successifs du doigt pourraient être comparés les uns aux autres pour s'assurer que tous les scans enregistrés étaient du même doigt. Il est évident d'avoir un certain pourcentage de chevauchement entre les différents scans. Une telle chose aurait empêché [Prateek Dwivedi](https://www.freecodecamp.org/news/it-is-easy-to-trick-the-mobile-phones-fingerprint-scanner-d8d7f509d128/undefined) de scanner son doigt lorsque j'essayais de configurer le téléphone. _Cela aurait sécurisé la manière dont les empreintes digitales sont capturées au moment de la configuration._

![Image](https://cdn-media-1.freecodecamp.org/images/hLsbzoXZyPNqGAclK5EVK1qwl87iZmL2XJJL)
_Un certain chevauchement entre deux scans successifs_

La récupération pourrait être rendue plus sécurisée en ne comparant pas le scan pour déverrouiller l'appareil avec un seul des scans pré-stockés. Idéalement, le scan sera comparé à un degré élevé avec l'une des représentations stockées, et il sera également comparé à tous les autres scans dans une certaine mesure. Au lieu de se fier à une seule correspondance optimale, nous devrions noter la correspondance en fonction d'une comparaison de toutes les représentations. Le pourcentage cumulatif de comparaison devrait être pris en compte pour l'authentification.

### Conclusion

Pour conclure, comme je l'ai souligné dans mon [précédent blog](https://medium.com/@niks.dwivedi/biometric-identification-usage-in-finance-mobile-applications-11b15c8d0b88) — « [Identification biométrique et utilisation dans les applications mobiles bancaires](https://medium.com/@niks.dwivedi/biometric-identification-usage-in-finance-mobile-applications-11b15c8d0b88) : »

L'authentification biométrique n'est pas encore suffisamment sécurisée. Récemmement, nous avons vu une inclination et un changement vers l'utilisation de ces techniques pour les paiements et les transactions financières également. La montée en puissance des téléphones mobiles et des appareils IoT a contribué à l'adoption des techniques d'authentification biométrique. Il est temps de réfléchir davantage à la manière de rendre la technologie d'authentification biométrique plus sécurisée et plus difficile à compromettre.

_Suivez-moi sur medium — [Nikhil Dwivedi](https://www.freecodecamp.org/news/it-is-easy-to-trick-the-mobile-phones-fingerprint-scanner-d8d7f509d128/undefined)._

_Mon compte twitter est — [@Niks_Dwivedi](https://twitter.com/Niks_Dwivedi)_