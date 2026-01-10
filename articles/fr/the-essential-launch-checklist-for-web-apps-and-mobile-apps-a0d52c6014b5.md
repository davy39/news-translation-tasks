---
title: La Checklist Essentielle pour le Lancement d'Applications Web et Mobiles
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-21T03:40:25.000Z'
originalURL: https://freecodecamp.org/news/the-essential-launch-checklist-for-web-apps-and-mobile-apps-a0d52c6014b5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*e7O7A5rM79ng6b8Dc3EbEg.jpeg
tags:
- name: mobile app development
  slug: mobile-app-development
- name: SEO
  slug: seo
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: La Checklist Essentielle pour le Lancement d'Applications Web et Mobiles
seo_desc: 'By Ben Cheng

  This is a simple launch checklist for web and mobile apps that I’ve prepared for
  product and project managers to quickly test performance of their apps. It also
  includes a list of commonly overlooked simple mobile app tests to confirm th...'
---

Par Ben Cheng

Voici une checklist simple pour le lancement d'applications web et mobiles que j'ai préparée pour les chefs de produit et les chefs de projet afin de tester rapidement les performances de leurs applications. Elle inclut également une liste de tests simples souvent négligés pour confirmer que l'application se comporte comme prévu.

Les chefs de produit côté client peuvent utiliser les outils fournis pour voir les résultats de performance lorsqu'ils travaillent avec des agences digitales ou des sociétés de développement.

### Applications Web

Pour les applications web, la checklist de lancement doit couvrir les points suivants :

1. Performance : Réussir le test Google Page Speed Insights
2. Sécurité
3. Liens brisés
4. Compatibilité
5. SEO / Réseaux sociaux
6. Éléments souhaitables

### Performance : Réussir le test Google Page Speed Insights

![Image](https://cdn-media-1.freecodecamp.org/images/e3ZdwpSpZ51SExdgGqJKFgq72yV6jRHMm653)
_Notez que Google fera de la [vitesse de page un facteur de classement dans les recherches mobiles](https://techcrunch.com/2018/01/17/google-will-make-page-speed-a-factor-in-mobile-search-ranking-starting-in-july/" rel="noopener" target="_blank" title=") à partir de juillet 2018_

1. Entrez le site dans Google [PageSpeed Insights](https://developers.google.com/speed/pagespeed/insights/) pour voir vos résultats
2. Si le site nécessite une connexion / des identifiants, connectez-vous d'abord au site et vérifiez les performances avec [l'extension Chrome Page Speed Insights](https://chrome.google.com/webstore/detail/pagespeed-insights-with-p/lanlbpjbalfkflkhegagflkgcfklnbnh)
3. Un autre outil utile est [Pass GTMetrix Analysis](https://gtmetrix.com/)

**Pourquoi :** Les statistiques montrent constamment que quelques secondes de temps de chargement font une énorme différence en termes de rétention. [53 % des visites de sites sont abandonnées si un site met plus de 3 secondes à charger](https://www.thinkwithgoogle.com/data-gallery/detail/mobile-site-abandonment-three-second-load/). Avoir un site plus rapide aide à retenir les visiteurs et augmente l'engagement avec votre site. Cela réduit également votre taux de rebond et aide votre SEO.

### Sécurité

![Image](https://cdn-media-1.freecodecamp.org/images/TafLFoWB04CtnkMX1U3Xy7QtP0IAVnsOHmI-)
_Assurez-vous que votre site web / application web a au moins un score A pour SSL. Source : Qualsys_

1. Utilisez uniquement HTTPS. HTTP doit toujours rediriger vers HTTPS.
2. [Test SSL de Qualys](https://www.ssllabs.com/ssltest/index.html) - Visez un score de A ou plus
3. Considérez ces outils de scan gratuits / open source (entre autres) : [Qualys](https://www.qualys.com/forms/freescan/), [OpenVAS](http://www.openvas.org/), [Nmap](http://nmap.org/), [OSSEC](https://ossec.github.io/), [Security Onion](http://securityonion.blogspot.com/), [OpenSSH](http://www.openssh.org/)

**Pourquoi :** Il est facile d'oublier s'il n'y a pas de checklist, car ces fonctionnalités ne font généralement pas partie de l'UI et peuvent ne pas être détectées dans les [tests exploratoires](https://blog.oursky.com/2018/05/08/software-qa-exploratory-testing/).

### Liens brisés

![Image](https://cdn-media-1.freecodecamp.org/images/LjTSSPVLill9Ok3wxQkbw7Af7m7ON0dcgpwU)
_Source : Screaming Frog_

1. Vérifiez que toutes les pages n'ont pas de liens brisés sur [Monkeytest](https://monkeytest.it/)
2. Vérifiez que toutes les pages n'ont pas de liens invalides sur [Screaming Frog](https://www.screamingfrog.co.uk/)

**Pourquoi :** c'est mieux pour l'UX, et les liens brisés peuvent nuire à votre SEO.

### Compatibilité

1. Vérifiez la compatibilité avec les principaux navigateurs de bureau et leurs versions (Chrome, Firefox, Safari, Opera, Internet Explorer)
2. Vérifiez également les navigateurs mobiles !
3. Vérifiez également comment Safari (iOS) et Chrome (Android) se comportent sur différentes tailles d'écran.

Les navigateurs intégrés aux applications peuvent également se comporter différemment. Comme ils sont très courants, vous pouvez essayer d'ouvrir un lien depuis Facebook, Reddit, Twitter, ou même votre application de boîte de réception.

**Pourquoi :** Tous les navigateurs de bureau ne rendent pas de la même manière, et vous voulez garantir une expérience utilisateur cohérente et de haute qualité. De plus, les sites web ou applications web réactifs doivent s'adapter à différentes tailles d'écran (mais parfois la version rendue ne se comporte pas comme prévu pour une taille spécifique).

Par exemple, consultez un cas que nous avons trouvé avec [l'en-tête collant de YouTube pour Internet Explorer](https://code.oursky.com/should-you-use-sticky-header/).

### SEO / Réseaux sociaux

![Image](https://cdn-media-1.freecodecamp.org/images/LQAdZBeDCyantwVkP3DoMJm1HaesAEEFKNse)

1. Est-il correctement indexé par Google ? (Vérifiez avec [Google Webmaster Tools](https://www.google.com/webmasters/))
2. Est-il dans la première page des résultats de recherche Google (SERPs) ?
3. Contient-il les balises OpenGraph correctes pour le partage social ? Testez en déposant le lien dans Facebook / Twitter / Pinterest pour voir quelle image, quel titre et quelle description sont générés
4. Le site ou l'application a-t-il la balise Title / Meta Description correcte ?
5. A-t-il une Favicon ?

**Pourquoi :** Assurez-vous que votre application, service ou site web est découvrable en complétant le côté technique du SEO et des réseaux sociaux. Le SEO aide les utilisateurs potentiels à vous trouver en utilisant des termes de recherche clés. L'optimisation sociale formate le contenu de votre site afin que vos utilisateurs et votre communauté puissent facilement le partager pour référer plus d'utilisateurs.

Selon les [statistiques 2017 de Hubspot](https://www.hubspot.com/marketing-statistics), 61 % des marketeurs disent que l'amélioration du SEO et la croissance d'une présence organique en ligne sont leur priorité absolue pour le marketing entrant.

### Éléments souhaitables

![Image](https://cdn-media-1.freecodecamp.org/images/qe5zm-k6pJhpf2wjBJJx8DRT6W2CtLvrHvp6)
_Source de l'image : [Paper CSS](https://github.com/cognitom/paper-css" rel="noopener" target="_blank" title=") par cognitom sur GitHub_

1. Validez le HTML/CSS avec [https://validator.w3.org](https://validator.w3.org/)
2. Vérifiez l'accessibilité web de base avec [WAVE](https://wave.webaim.org/) ou avec des outils à [https://www.w3.org/WAI/ER/tools/](https://www.w3.org/WAI/ER/tools/)
3. Les pages 404 sont-elles informatives ?
4. Votre site a-t-il besoin d'une [feuille de style d'impression](https://github.com/cognitom/paper-css) ?
5. Assurez-vous que votre JavaScript est exempt d'erreurs lorsque votre page se charge (vérifiez depuis les outils de développement de Google Chrome)
6. Les URLs sont-elles raisonnables/descriptives ? Des URLs raisonnables aident les visiteurs et les moteurs de recherche à comprendre votre contenu.
7. Le domaine canonique fonctionne-t-il ? ([www.abc.com](http://www.abc.com/) vs abc.com, etc.)

### Pour les Applications Mobiles

![Image](https://cdn-media-1.freecodecamp.org/images/Wnq0bIwnGYiM8uQVSugh-ZsPX05gNAMujyWn)
_Les petits écrans comme l'iPhone 4SE posent des défis d'UI._

Voici une checklist simple pour tester les applications mobiles. Voici quelques problèmes souvent négligés avec les applications mobiles :

1. L'entrée utilise-t-elle le bon type de clavier (par exemple, les entrées d'email ou de numéro doivent utiliser le type de clavier correspondant) et CTA ? (par exemple, dans un formulaire, le CTA du clavier en bas à droite dans iOS doit montrer "suivant", et lorsqu'on appuie dessus, il doit passer à l'entrée suivante du formulaire).
2. L'application a-t-elle un indicateur de chargement approprié lorsqu'elle effectue un travail nécessitant que les utilisateurs attendent ?
3. Testez l'application dans des [conditions de réseau médiocres](https://code.oursky.com/offline-first-network-connection-error/), pour vérifier si elle se comporte comme prévu.
4. Testez l'application en mode avion (si elle est censée fonctionner hors ligne).
5. Testez la compatibilité des applications dans différentes dimensions d'écran (surtout les petits écrans).
6. Testez si l'application demande des permissions avec une explication appropriée.
7. Testez si l'application affiche des messages d'erreur faciles à comprendre.
8. Testez si l'application fonctionne correctement pendant les interruptions sous Android (comme un appel, ou un stockage faible).
9. Testez l'application avec différentes localisations / fuseaux horaires.
10. Testez l'application avec différentes tailles de police (surtout dans iOS).

C'est à peu près tout. Merci de partager si vous avez trouvé cet article utile !

**Oursky est une agence digitale dirigée par des ingénieurs basée à Hong Kong qui a travaillé avec des marques mondiales et des entreprises cotées. Si vous avez une application ou souhaitez développer une solution digitale pour votre produit, [contactez-nous](https://oursky.com/contact) !**

_Ces notes sont adaptées d'un atelier que j'ai animé pour des chefs de projet dans une entreprise à Hong Kong et publié [sur notre blog](https://blog.oursky.com/2018/05/21/launch-checklist-websites-web-apps/) le 21 mai 2018._