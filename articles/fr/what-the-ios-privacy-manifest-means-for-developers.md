---
title: Ce que le manifeste de confidentialité iOS signifie pour les développeurs
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2024-03-15T16:56:05.000Z'
originalURL: https://freecodecamp.org/news/what-the-ios-privacy-manifest-means-for-developers
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/pawel-czerwinski-jj4LC7iKA6Q-unsplash.jpg
tags:
- name: privacy
  slug: privacy
seo_title: Ce que le manifeste de confidentialité iOS signifie pour les développeurs
seo_desc: 'At WWDC 2023, Apple introduced us to a new bundle resource that is going
  to be added to every application and library: the privacy manifest. A lot has been
  written since then about this subject but without that much clarity.

  When first announced, App...'
---

[Lors de la WWDC 2023](https://developer.apple.com/videos/play/wwdc2023/10060), Apple nous a présenté une nouvelle ressource de bundle qui sera ajoutée à chaque application et bibliothèque : le manifeste de confidentialité. Beaucoup de choses ont été écrites depuis sur ce sujet, mais sans beaucoup de clarté.

Lors de son annonce initiale, Apple a déclaré qu'au printemps 2024 (comprenez – le printemps est déjà là), la présence d'un manifeste de confidentialité est attendue et fera partie du [processus de révision des applications](https://developer.apple.com/distribute/app-review/). Apple demande également aux développeurs d'applications, ainsi qu'aux développeurs de SDK, d'adopter le manifeste de confidentialité.

En avance rapide jusqu'au 7 décembre 2023, [Apple a annoncé](https://developer.apple.com/news/?id=r1henawx#:~:text=Third%2Dparty%20SDK%20privacy%20manifest%20and%20signatures.&text=Starting%20in%20spring%202024%2C%20if,used%20as%20a%20binary%20dependency.) une liste de "SDK tiers couramment utilisés" qui, si ils sont inclus par votre application, nécessitent un manifeste de confidentialité. Aucune explication réelle n'a été donnée quant à la raison pour laquelle les SDK tiers listés sont ceux qui ont été sélectionnés, mais il y a eu beaucoup de spéculations à ce sujet.

Et nous voici après le 29 février 2024 (un jour bissextile !), lorsque [Apple a annoncé](https://developer.apple.com/news/?id=3d8a9yyh) un calendrier pour l'application de la section des API de raison requise du manifeste de confidentialité.

Tout cela a conduit à une certaine confusion parmi les développeurs qui s'efforcent de comprendre si leur application ou SDK relève d'une catégorie de manifeste de confidentialité.

Les développeurs ne sont pas sûrs d'ajouter un manifeste de confidentialité à leur SDK, même s'il n'est pas listé. La [documentation](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files) elle-même, bien qu'elle donne un bon aperçu de tout, manque des distinctions et détails nécessaires que les développeurs recherchent.

Une partie de moi veut dire qu'Apple garde les choses vagues car l'avenir proche apportera des changements que les manifestes de confidentialité apporteront. Une autre partie de moi dit qu'Apple a toujours été aussi vague, et que c'est simplement leur modus operandi.

Dans tous les cas, vous lisez cet article parce que vous voulez comprendre comment tout cela vous affecte. Alors, décomposons les choses.

> _⚠️ Avertissement : Cet article ne traitera pas de l'explication de ce qu'est le manifeste de confidentialité ou de la manière de l'ajouter à votre application/bibliothèque, car cela a été bien couvert par la documentation d'Apple._

## Les Quatre Cavaliers

Le manifeste de confidentialité est divisé en quatre sujets :

* NSPrivacyTracking.
* NSPrivacyTrackingDomains.
* NSPrivacyCollectedDataTypes (étiquettes nutritionnelles).
* NSPrivacyAccessedAPITypes (API de raison requise).

Les deux premiers sont liés ensemble et peuvent poser les changements les plus substantiels à votre application/bibliothèque, alors nous commencerons par le numéro trois.

### Qu'est-ce que NSPrivacyCollectedDataTypes ?

Cette section contient diverses catégories de collecte de données. Si votre application ou SDK fait quelque chose avec, vous devez les déclarer.

Chaque type de données collectées doit être fourni avec la raison de leur collecte.

Les catégories vont des informations de contact sur l'utilisateur (telles que l'email/numéro de téléphone), à la localisation et aux achats.

Dans votre fichier de manifeste de confidentialité, vous aurez un tableau de NSPrivacyCollectedDataTypes, où chaque élément contiendra :

* Le type de données collectées.
* Si ces données sont liées à l'utilisateur ou non.
* Si ces données sont utilisées pour suivre l'utilisateur ou non.
* La ou les raisons de la collecte de ces données.

Faisons un exemple. Imaginez que votre application collecte la localisation précise d'un utilisateur afin de suivre les mouvements de l'utilisateur pour voir si l'utilisateur est à proximité de magasins spécifiques.

Si l'utilisateur est à proximité d'un tel magasin, vous lui présentez une publicité pertinente. En tenant compte de tout cela, vous devrez créer une entrée où :

* Le type de données sera NSPrivacyCollectedDataTypePreciseLocation.
* Marquez vrai car nous lions les données à l'utilisateur.
* Marquez vrai car nous suivons l'utilisateur avec ces données.
* Puisque nous allons afficher des publicités à l'utilisateur, nous choisirons NSPrivacyCollectedDataTypePurposeThirdPartyAdvertising, NSPrivacyCollectedDataTypePurposeProductPersonalization, et NSPrivacyCollectedDataTypePurposeAppFunctionality car toutes ces raisons correspondent aux données que nous collectons.

### Qu'est-ce que NSPrivacyAccessedAPITypes ?

Comme mentionné, cette section est un peu plus obscure et un peu plus exigeante.

Ici, Apple liste des API très spécifiques de différentes catégories que, si vous utilisez, vous devez les déclarer.

Pour chaque API listée, il y a des raisons spécifiques pour lesquelles vous devez les déclarer. Certaines raisons indiquent clairement que même si vous utilisez l'API, vous ne pouvez pas envoyer les données reçues par cette API à un serveur (hors appareil).

Si vous trouvez que votre application ou SDK utilise l'une des API listées, alors vous devez la lister avec une raison appropriée. Par exemple, si nous utilisons l'exemple de la section précédente, notre application lit et écrit des données dans les préférences utilisateur qui concernent la localisation de l'utilisateur. Donc, nous devrons :

* Lister NSPrivacyAccessedAPICategoryUserDefaults comme le NSPrivacyAccessedAPIType.
* Utiliser CA92.1 dans les NSPrivacyAccessedAPITypeReasons.

Si vous pensez ne pas voir la raison pour laquelle vous utilisez une API, [vous pouvez en informer Apple](https://idmsa.apple.com/IDMSWebAuth/signin.html?path=%2Fcontact%2Frequest%2Fprivacy-manifest-reason%2F&appIdKey=891bd3417a7776362562d2197f89480a8547b108fd934911bcbea0110d07f757&rv=0).

> 🏳️ Aucune des API listées ne peut être utilisée pour suivre l'utilisateur.

Enfin, nous arrivons aux deux catégories les plus problématiques.

### Qu'est-ce que NSPrivacyTracking et NSPrivacyTrackingDomains ?

Qu'est-ce que le suivi ? Le savez-vous ? Quelqu'un le sait-il ? Cela n'a vraiment pas d'importance, car [Apple a une définition pour cela](https://developer.apple.com/app-store/app-privacy-details/#user-tracking) :

> "Le suivi" fait référence à la liaison des données collectées à partir de votre application concernant un utilisateur final ou un appareil particulier, telles qu'un identifiant utilisateur, un identifiant d'appareil ou un profil, avec des données tierces à des fins de publicité ciblée ou de mesure publicitaire, ou au partage des données collectées à partir de votre application concernant un utilisateur final ou un appareil particulier avec un courtier de données.

Donc, si votre application ou SDK ne relève pas de cette définition, vous devez marquer faux comme valeur pour NSPrivacyTracking et vous pouvez respirer.

Car si vous devez marquer vrai comme NSPrivacyTracking, alors vous devez fournir tous les domaines que votre application ou SDK utilise à des fins de suivi dans le cadre de NSPrivacyTrackingDomains.

À ce stade, vous devez vous demander pourquoi je fais tout un plat de cela. Eh bien, cela a à voir avec le fait qu'Apple bloquera toutes les requêtes vers tout domaine listé sous NSPrivacyTrackingDomains si l'utilisateur n'autorise pas l'application à le suivre.

Relisez le paragraphe ci-dessus.

Vous comprenez ? Vous devrez maintenant rediriger les requêtes réseau différemment en fonction de si l'utilisateur a donné son consentement pour être suivi ou non.

Côté client (application/bibliothèque), cela peut être un petit changement à gérer. Mais côté serveur/infrastructure, cela peut nécessiter un travail important car de nouveaux domaines (ou sous-domaines) doivent être créés.

Les données qui ont été agrégées d'une certaine manière doivent maintenant être agrégées à partir d'une autre source. Vous devez également vous assurer qu'aucune donnée liée au suivi n'est envoyée à vos nouveaux domaines. Vous ne voudriez pas vous retrouver dans un scénario où votre application/bibliothèque cesse complètement de fonctionner.

Pour vous aider à comprendre quels domaines relèvent de la catégorie de suivi, vous pouvez utiliser [Instruments](https://developer.apple.com/documentation/xcode/detecting-when-your-app-contacts-domains-that-may-be-profiling-users). Soyez conscient que si vos domaines ne relèvent pas de cette catégorie maintenant, cela ne signifie pas qu'ils n'en relèveront pas plus tard.

## Conclusion

Comme pour toute nouvelle réglementation ou politique, de nombreuses questions restent sans réponse :

* Si mon application a une webview, où certaines requêtes réseau sont faites, dois-je inclure celles-ci comme domaines pour NSPrivacyTrackingDomains ?
* Les sous-domaines sont-ils suffisants ou les développeurs doivent-ils créer des domaines complètement différents ?
* Si ma bibliothèque n'est pas listée comme faisant partie des SDK couramment utilisés, y a-t-il une chance qu'elle le soit à l'avenir ? Quels sont les critères utilisés pour lister de tels SDK ?
* Dois-je inclure une signature à mon SDK même s'il n'est pas listé parmi les SDK couramment utilisés ?

De plus, en regardant l'état actuel des choses dans la communauté des développeurs, la réponse est assez la même. Au moment de la rédaction de cet article, de nombreux SDK qui sont listés dans la liste d'Apple n'ont toujours pas publié de version avec un manifeste de confidentialité.

À mesure que nous nous approcherons de la date à laquelle il sera obligatoire d'avoir un manifeste de confidentialité, espérons que plus de détails émergeront et que la clarté s'améliorera. En attendant, préparez-vous.