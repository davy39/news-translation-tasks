---
title: Comment protéger vos informations avec Local Sheriff
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-01T18:12:00.000Z'
originalURL: https://freecodecamp.org/news/local-sheriff-watching-them-watching-us-5eacf3eb00ca
coverImage: https://cdn-media-1.freecodecamp.org/images/1*S5zyXVDrpVR24gnN9Vs0Tg.jpeg
tags:
- name: big data
  slug: big-data
- name: JavaScript
  slug: javascript
- name: privacy
  slug: privacy
- name: Security
  slug: security
- name: 'tech '
  slug: tech
seo_title: Comment protéger vos informations avec Local Sheriff
seo_desc: 'By Konark Modi

  Watching them watching us


  What is a TellTale URL ?

  A URL is the most commonly tracked piece of information. The innocent choice to
  structure a URL based on page content can make it easier to learn a users’ browsing
  history, address, h...'
---

Par Konark Modi

#### Les observer nous observer

![Image](https://cdn-media-1.freecodecamp.org/images/bal86HLtSK3DaHmGSDs2koKIIaTAzzAp23wY)

### **Qu'est-ce qu'une URL TellTale ?**

Une URL est l'information la plus couramment suivie. Le choix innocent de structurer une URL basée sur le contenu de la page peut faciliter l'apprentissage de l'historique de navigation, de l'adresse, des informations de santé ou d'autres détails sensibles d'un utilisateur. Elles contiennent des informations sensibles ou peuvent mener à une page qui contient des informations sensibles.

Nous appelons ces URLs des TellTaleURLs.

Examinons quelques exemples de telles URLs.

### **EXEMPLE #1 :**

**Site web** : _donate.mozilla.org (Corrigé)_

Après avoir terminé le processus de paiement sur _donate.mozilla.org_, vous êtes redirigé vers une page de "merci". Si vous regardez attentivement l'URL montrée dans la capture d'écran ci-dessous, elle contient certaines informations privées comme _email, pays, montant, méthode de paiement_.

![Image](https://cdn-media-1.freecodecamp.org/images/yFTLh7ZBCOWDlqold7QyIGe9LCTe02pOzgsT)
_PII dans l'URL sur donate.mozilla.org_

Maintenant, parce que cette page charge certaines ressources depuis des tiers et que l'URL n'est pas assainie, les mêmes informations sont également partagées avec ces tiers via le référent et comme valeur à l'intérieur de la charge utile envoyée aux tiers.

![Image](https://cdn-media-1.freecodecamp.org/images/qQpzQGwGsPEJDchKDOrU8ZKXxM7ALe4QO5DI)
_URL avec PII partagée lors du chargement des polices depuis Google Apis._

Dans ce cas particulier, il y avait 7 tiers avec lesquels ces informations étaient partagées.

Mozilla a été prompt à corriger ces problèmes, plus de détails peuvent être trouvés ici : [_https://bugzilla.mozilla.org/show_bug.cgi?id=1516699_](https://bugzilla.mozilla.org/show_bug.cgi?id=1516699)

### EXEMPLE #2 :

**Site web** : trainline.eu, _JustFly.com (Dernière vérification : août 2018)_

Une fois que vous avez terminé un achat comme des billets de train ou des billets d'avion, vous recevez un email qui contient un lien pour gérer votre réservation. La plupart du temps, lorsque vous cliquez sur le lien, les détails de la réservation vous sont montrés - sans avoir à entrer d'autres détails comme le code de réservation, le nom d'utilisateur/mot de passe.

Cela signifie que l'URL elle-même contient un certain jeton qui est unique à l'utilisateur et fournit l'accès à la réservation de l'utilisateur.

Il se trouve que ces URLs sont également partagées avec des tiers, donnant à ces tiers [des données hautement sensibles](https://medium.freecodecamp.org/how-airlines-dont-care-about-your-privacy-case-study-emirates-com-6271b3b8474b) et [l'accès à vos réservations](https://cliqz.com/en/magazine/lufthansa-data-leak-what-a-single-url-can-reveal-about-you).

![Image](https://cdn-media-1.freecodecamp.org/images/B6qA9nsCDe3WcNG8MseCRhq0lnG7I2gSG08K)
_JustFly.com divulguant l'ID de réservation à 10 domaines tiers._

![Image](https://cdn-media-1.freecodecamp.org/images/Sgg5O7vWB-Bh4E5NuAW3wQkr0hkQiUbQN2qI)
_trainline.eu partageant le jeton de réservation avec 17 domaines tiers._

![Image](https://cdn-media-1.freecodecamp.org/images/dKN254bU1AgMCf21rWvWc0u6ge6iscwRKT5y)
_URL avec jeton partagée via Ref et à l'intérieur de la charge utile._

### EXEMPLE #3 :

**Site web** : _foodora.de, grubhub.com (Dernière vérification : août 2018)_

L'un des prérequis pour commander de la nourriture en ligne est d'entrer l'adresse où vous voulez que la nourriture soit livrée.

Certains sites populaires de livraison de nourriture convertissent l'adresse en valeurs précises de latitude-longitude et les ajoutent à l'URL.

L'URL est également partagée avec des tiers, divulguant potentiellement l'adresse de l'utilisateur.

![Image](https://cdn-media-1.freecodecamp.org/images/zh6XHBxE7ubGBB8l3of-fFhYuNhvQodJGRAf)
_Foodora divulguant les détails de l'adresse à 15 domaines tiers._

> Pour être clair, ce ne sont pas seulement ces sites web qui souffrent de telles fuites. Ce problème existe partout - c'est une situation par défaut, pas une rareté. Nous l'avons vu avec Lufthansa, Spotify, Flixbus, Emirates, et même avec des prestataires médicaux.

### Risques des URLs TellTale :

* Les sites web divulguent négligemment des informations sensibles à une pléthore de tiers.
* La plupart du temps sans le consentement des utilisateurs.
* Plus dangereusement : La plupart des sites web ne sont pas conscients de ces fuites lors de l'implémentation de services tiers.

### Ces problèmes sont-ils difficiles à résoudre ?

En tant qu'ingénieur logiciel ayant travaillé pour certaines des plus grandes entreprises de commerce électronique, je comprends le besoin d'utiliser des services tiers pour optimiser et améliorer non seulement le produit numérique mais aussi la manière dont les utilisateurs interagissent avec le produit.

Ce n'est pas l'utilisation de services tiers qui est préoccupante dans ce cas, mais l'implémentation de ces services. Les propriétaires doivent toujours avoir le contrôle de leur site web et de ce que le site web partage avec les services tiers.

C'est ce contrôle qui doit être exercé pour limiter la fuite d'informations utilisateur.

Ce n'est pas une tâche mammouth, c'est juste une question d'engagement à préserver le droit fondamental à la vie privée.

Par exemple :

1. Les pages privées doivent avoir des [balises meta noindex](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta).
2. Limiter la présence de services tiers sur les pages privées.
3. [Referrer-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy) sur les pages avec des données sensibles.
4. Implémenter CSP et SRI. Même avec une grande empreinte de services tiers, [CSP](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP), [SRI](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity) ne sont pas activés sur la majorité des sites web.

### Présentation de Local Sheriff :

Étant donné que de telles fuites d'informations sont dangereuses à la fois pour les utilisateurs et les organisations, pourquoi est-ce un problème si répandu ?

Une grande raison pour laquelle ces problèmes existent est le manque de sensibilisation.

Un bon point de départ pour les sites web est de voir quelles informations sont divulguées ou de détecter la présence de TellTaleURLs.

Mais afin de découvrir si cela se produit avec les sites web que vous maintenez ou visitez, vous devez apprendre à utiliser certains outils pour inspecter le trafic réseau, comprendre la relation premier tiers - tiers, puis vous assurer d'avoir ces outils ouverts pendant le processus de transaction.

Pour aider à combler cette lacune, nous voulions construire un outil avec les directives suivantes :

* Facile à installer.
* Surveille et stocke toutes les données échangées entre les sites web et les tiers - localement sur la machine de l'utilisateur.
* Aide à identifier les utilisateurs que les entreprises suivent sur Internet.
* Interface pour rechercher les informations divulguées aux tiers.

Étant donné les directives ci-dessus, une extension de navigateur semblait être un choix raisonnable. Après avoir installé Local-Sheriff, en arrière-plan :

1. En utilisant l'API WebRequest, elle surveille l'interaction entre le premier tiers et le tiers.
2. Classe ce qui est premier tiers et tiers dans l'URL.
3. Est livrée avec une copie de la base de données de [WhoTracksMe](https://whotracks.me/). Pour mapper quel domaine appartient à quelle entreprise.

4. Fournit une interface où vous pouvez rechercher des valeurs que vous pensez être privées et voir quels sites web les divulguent à quels tiers. Par exemple : nom, email, adresse, date de naissance, cookie, etc.

### Revisiter l'EXEMPLE #1

**Site web** : _donate.mozilla.org_

* L'utilisateur a installé Local-Sheriff et fait un don à mozilla.org.

![Image](https://cdn-media-1.freecodecamp.org/images/xrealtqpe6MuxuFVU6nqyaWR3Z6FZm-J4uwv)
_PII dans l'URL sur donate.mozilla.org_

* Clique sur l'icône pour ouvrir l'interface de recherche.

![Image](https://cdn-media-1.freecodecamp.org/images/oQTbZxMUMeO0l83pyyvQca-EWggpcB1tMn7Z)
_Icône Local Sheriff._

* Entre l'email utilisé sur le site donate.mozilla.org.

![Image](https://cdn-media-1.freecodecamp.org/images/XU1a1DfPQyJLtvGYM52swvVEyVD5Xj1FH91R)
_Interface de recherche Local-Sheriff_

Il peut être vu que l'adresse email utilisée au moment du don a été partagée avec **~7 domaines tiers.**

Vous pouvez l'essayer vous-mêmes en l'installant :

* **Firefox** : [https://addons.mozilla.org/de/firefox/addon/local-sheriff/](https://addons.mozilla.org/de/firefox/addon/local-sheriff/)
* **Chrome** : [https://chrome.google.com/webstore/detail/local-sheriff/ckmkiloofgfalfdhcfdllaaacpjjejeg](https://chrome.google.com/webstore/detail/local-sheriff/ckmkiloofgfalfdhcfdllaaacpjjejeg)

**Ressources** :

* **Plus de détails** : [_https://www.ghacks.net/2018/08/12/local-sheriff-reveals-if-sites-leak-personal-information-with-third-parties/_](https://www.ghacks.net/2018/08/12/local-sheriff-reveals-if-sites-leak-personal-information-with-third-parties/)
* **Code source** : [_https://github.com/cliqz-oss/local-sheriff_](https://github.com/cliqz-oss/local-sheriff)
* **Conférences** : [_Defcon 26 Demo Labs_](https://www.defcon.org/html/defcon-26/dc-26-demolabs.html) _, [FOSDEM 2019](https://fosdem.org/2019/schedule/event/web_extensions_exposing_privacy_leaks/)_
* **Code** : [https://github.com/cliqz-oss/local-sheriff](https://github.com/cliqz-oss/local-sheriff)
* **Chrome store** : [https://chrome.google.com/webstore/detail/local-sheriff/ckmkiloofgfalfdhcfdllaaacpjjejeg](https://chrome.google.com/webstore/detail/local-sheriff/ckmkiloofgfalfdhcfdllaaacpjjejeg)

Merci d'avoir lu et partagé ! :)

Si vous avez aimé cette histoire, n'hésitez pas à ??? quelques fois (Jusqu'à 50 fois. Sérieusement).

Bon piratage !

[- Konark Modi](https://twitter.com/konarkmodi)

**_Crédits_** :

* _Un merci spécial à [Remi](https://twitter.com/Pythux) , [Pallavi](https://twitter.com/Pi_Modi) pour avoir révisé cet article :)_
* _Le titre « Les observer nous observer » provient d'une conférence conjointe entre Local Sheriff et [Trackula](https://trackula.org/en/) à FOSDEM 2019._