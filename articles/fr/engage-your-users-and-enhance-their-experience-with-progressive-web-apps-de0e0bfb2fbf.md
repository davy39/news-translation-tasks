---
title: Engagez vos utilisateurs et améliorez leur expérience avec les Progressive
  Web Apps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-16T09:44:05.000Z'
originalURL: https://freecodecamp.org/news/engage-your-users-and-enhance-their-experience-with-progressive-web-apps-de0e0bfb2fbf
coverImage: https://cdn-media-1.freecodecamp.org/images/1*h2X9ckg3FJr4FGSfwh0F2w.jpeg
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Engagez vos utilisateurs et améliorez leur expérience avec les Progressive
  Web Apps
seo_desc: 'By Dave Gray

  What is a Progressive Web App?

  A Progressive Web App (aka PWA) is a duality. It is both a website and a web app.
  A PWA provides progressive enhancements to new and existing websites. These mobile-focused
  enhancements are easy to justify....'
---

Par Dave Gray

### **Qu'est-ce qu'une Progressive Web App ?**

Une **Progressive Web App** (ou PWA) est une dualité. C'est à la fois un site web et une application web. Une PWA offre des [améliorations progressives](https://developers.google.com/web/updates/2015/12/getting-started-pwa) aux sites web nouveaux et existants. Ces améliorations axées sur le mobile sont faciles à justifier. [L'utilisation d'Internet sur mobile a dépassé celle sur desktop à l'automne 2016.](https://techcrunch.com/2016/11/01/mobile-internet-use-passes-desktop-for-the-first-time-study-finds/) Nous vivons véritablement dans un monde mobile d'abord.

L'une de ces améliorations est l'option « Ajouter à l'écran d'accueil ». Les sites web activent cette fonctionnalité dans certains navigateurs en [répondant à des critères de conception spécifiques pour les PWA](https://developers.google.com/web/fundamentals/app-install-banners/#what_are_the_criteria). Cette fonctionnalité vous permet d'enregistrer l'icône de la PWA sur votre écran d'accueil à côté de vos autres icônes d'applications. Vous pouvez ensuite lancer la PWA avec l'apparence et la convivialité d'une application.

![Image](https://cdn-media-1.freecodecamp.org/images/hfv56qaFb28RtMwcPtMmlxU5xC3tizX4HPTQ)
_Le message par défaut de Firefox Beta lors de la visite d'une Progressive Web App._

Les développeurs web peuvent désormais concevoir une expérience « similaire à une application » en plein écran pour les utilisateurs. HTML, CSS et JavaScript sont les seuls langages de programmation nécessaires. Les fonctionnalités natives des appareils mobiles, y compris les notifications push, la caméra, la géolocalisation et [beaucoup plus](https://whatwebcando.today/), sont désormais disponibles pour une utilisation. De plus, une PWA doit toujours fournir des fonctionnalités même si vous perdez votre connexion de données. Elle doit fonctionner hors ligne !

[Google a défini trois domaines](https://developers.google.com/web/progressive-web-apps/) qui sont des « incontournables » pour les Progressive Web Apps : elles doivent être **fiables**, **rapides** et **engageantes**. Google indique que les Progressive Web Apps doivent « se charger instantanément, indépendamment de l'état du réseau », « répondre rapidement aux interactions de l'utilisateur », « vivre sur l'écran d'accueil de l'utilisateur » et « offrir une expérience immersive en plein écran ».

### **Pourquoi ai-je besoin (ou pourquoi mon entreprise a-t-elle besoin) d'une Progressive Web App ?**

Vous pouvez **éliminer le besoin de développer des solutions séparées** (iOS, Android, Web) lorsqu'une Progressive Web App suffit.

Les PWA ne sont pas des remplacements pour toutes les applications mobiles, loin de là. Il existe de nombreuses applications mobiles avec des fonctionnalités que les PWA ne peuvent pas reproduire. Cependant, si votre application se concentre sur le partage d'informations (publications, photos, produits, support, interaction sociale), une PWA est un excellent choix.

Une autre réponse à la question « Pourquoi ? » est la **portée**.

En référence au rapport comScore 2017 sur les applications mobiles aux États-Unis ([demandez votre accès ici](https://www.comscore.com/Insights/Presentations-and-Whitepapers/2017/The-2017-US-Mobile-App-Report)), 87 % du temps d'utilisation est consacré aux applications mobiles contre 13 % au web mobile. Pourtant, en comparant la portée des 500 meilleures applications web mobiles et des 500 meilleures propriétés web mobiles, le web mobile a plus du double de la portée — 15,7 millions de visiteurs uniques mensuels en moyenne contre 7 millions pour les applications mobiles.

De plus, comScore note que 80 % des utilisateurs ont intentionnellement déplacé des applications vers leur écran d'accueil en 2017, soit une augmentation de 5 % par rapport à 2016.

![Image](https://cdn-media-1.freecodecamp.org/images/AW2wV7m8DAOiyp7gyPyTPwyZ3oK3rT07hi92)
_La PWA Pmount installée sur l'écran d'accueil et prête à envoyer des notifications push pour les offres spéciales quotidiennes._

Les Progressive Web Apps combinent les capacités des fonctionnalités natives des applications qui entraînent des **temps d'utilisation élevés** avec la **portée des propriétés web** et la possibilité de **s'installer sur l'écran d'accueil**. Cette combinaison hybride rend les Progressive Web Apps dignes d'intérêt.

Plusieurs sites web **passent déjà à l'étape** des Progressive Web Apps pleinement fonctionnelles.

![Image](https://cdn-media-1.freecodecamp.org/images/1aj7EZIQJsVV120dVqijEx5ykn4frLp04V01)
_Twitter Lite PWA demandant des autorisations pour les notifications push et une icône sur l'écran d'accueil_

[Twitter Lite](https://mobile.twitter.com/) est un excellent exemple utilisant les notifications push et la fonctionnalité hors ligne. La PWA de Twitter « [augmente considérablement l'engagement et réduit l'utilisation des données](https://developers.google.com/web/showcase/2017/twitter) ».

![Image](https://cdn-media-1.freecodecamp.org/images/b7AfNLZRm9FWG8COOXRqKV0VdpzxbP9Tjv3k)
_La PWA Pinterest a entraîné une augmentation de 40 % du temps passé dans l'expérience mobile_

Cette [étude de cas sur la PWA Pinterest](https://medium.com/dev-channel/a-pinterest-progressive-web-app-performance-case-study-3bd6ed2e6154) révèle des statistiques impressionnantes et des informations précieuses. Par rapport à leur expérience mobile web précédente, Pinterest a réalisé une augmentation de 60 % des engagements principaux. Leurs revenus publicitaires générés par les utilisateurs ont augmenté de 44 %. De plus, le temps passé a augmenté de 40 %.

![Image](https://cdn-media-1.freecodecamp.org/images/gfROMdw0E8X1UM9sVT5gNTbGTq7HphHr3F-y)
_Plus de la moitié des utilisateurs de Trivago ont déjà décidé d'« ajouter à l'écran d'accueil »_

La PWA de Trivago obtient des résultats impressionnants. [Plus de la moitié des utilisateurs](https://www.thinkwithgoogle.com/intl/en-gb/consumer-insights/trivago-embrace-progressive-web-apps-as-the-future-of-mobile/) ont utilisé leur fonctionnalité « ajouter à l'écran d'accueil ». L'engagement de ces utilisateurs a augmenté de 150 %. [Trivago](https://www.trivago.com/) discute de leur décision concernant la PWA [dans cette vidéo](https://youtu.be/pFE3LRRxqlo).

De nombreux autres exemples de PWA existent. Commencez votre recherche sur [pwa.rocks](https://pwa.rocks/) et cette [liste de 5 PWA impressionnantes](https://deanhume.com/home/blogpost/5-awesome-progressive-web-apps-worth-exploring/10153).

### **Comment commencer ?**

Si vous êtes un développeur web, un bon point de départ est la [page Google Developers sur les Progressive Web Apps](https://developers.google.com/web/progressive-web-apps/). Vous devrez apprendre les [Service Workers](https://developers.google.com/web/fundamentals/primers/service-workers/) et les [Web App Manifests](https://developers.google.com/web/fundamentals/web-app-manifest/).

Google fournit un outil d'audit de site web automatisé appelé Lighthouse. Lighthouse audite [cinq catégories](https://developers.google.com/web/tools/lighthouse/scoring) pour votre application : Progressive Web App, Performance, Accessibilité, Bonnes pratiques et Optimisation pour les moteurs de recherche. Le rapport d'audit détaillé de Lighthouse vous donnera 15 pages de détails avec plus de 50 résultats d'audit individuels.

![Image](https://cdn-media-1.freecodecamp.org/images/6Sqon96qx2nVOJugWsfb2ApTSZsxEEkruXto)
_Les cinq catégories de résultats d'audit fournies par Lighthouse._

Si vous n'êtes pas un développeur web, vous devrez en trouver un pour créer ou mettre à jour votre site web actuel en une application web progressive. Les PWA sont actuellement intensives en développement. Je ne connais aucun service qui élimine la nécessité de coder dans la solution. Si vous possédez le pub local ou le café du coin, vous pourriez trouver un client régulier qui est aussi un développeur ayant besoin d'un projet de test PWA. (Voir [thepmount.com](http://thepmount.com)) Dans les mois à venir, je prévois de publier des articles sur chaque étape du processus de création d'une PWA.

### **Conclusion**

Les **Progressive Web Apps** offrent des [améliorations progressives](https://developers.google.com/web/updates/2015/12/getting-started-pwa) aux sites web existants et établissent de [nouveaux critères](https://developers.google.com/web/fundamentals/app-install-banners/#what_are_the_criteria) pour les applications web préexistantes et nouvelles à atteindre. Répondre aux exigences des PWA et réussir les [audits Lighthouse](https://developers.google.com/web/tools/lighthouse/) aidera à fournir des expériences utilisateur [fiables, rapides et engageantes](https://developers.google.com/web/progressive-web-apps/) sur les appareils mobiles... et c'est quelque chose dont nous devrions tous bénéficier.

![Image](https://cdn-media-1.freecodecamp.org/images/jElxr0WSiaE1TRYpVhvO2nrl9HZ1zdgjvEEr)
_L'Americano d'aujourd'hui du café local_

N'hésitez pas à me contacter à tout moment sur [LinkedIn](https://www.linkedin.com/in/davidagray/) ou [Twitter](https://twitter.com/yesdavidgray). Et si vous avez aimé cet article, donnez-lui quelques applaudissements. Je vous en serai sincèrement reconnaissant.

[**Dave Gray | Profil professionnel | LinkedIn**](https://www.linkedin.com/in/davidagray/)  
[_Consultez le profil professionnel de Dave Gray sur LinkedIn. LinkedIn est le plus grand réseau professionnel au monde, aidant..._www.linkedin.com](https://www.linkedin.com/in/davidagray/)[**Dave Gray (@yesdavidgray) | Twitter**](https://twitter.com/yesdavidgray)  
[_Les derniers Tweets de Dave Gray (@yesdavidgray). Enseignant @FHSUInformatics * Développeur * Musicien * Entrepreneur..._twitter.com](https://twitter.com/yesdavidgray)