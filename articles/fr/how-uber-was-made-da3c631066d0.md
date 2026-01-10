---
title: Comment Uber a été créé
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-31T23:30:59.000Z'
originalURL: https://freecodecamp.org/news/how-uber-was-made-da3c631066d0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*N8jLWFdC1v1ZBLdOHQlO3A.png
tags:
- name: mobile
  slug: mobile
- name: mobile app development
  slug: mobile-app-development
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: uber
  slug: uber
seo_title: Comment Uber a été créé
seo_desc: 'By Dmytro Brovkin

  Uber has transformed the world. Indeed, its inconceivable to think of a world without
  the convenience of the innovative ride sharing service. Tracing its origins in a
  market which is constantly being deregulated, Uber has emerged tr...'
---

Par Dmytro Brovkin

Uber a transformé le monde. En effet, il est inconcevable d'imaginer un monde sans le confort du service innovant de covoiturage. Retraçant ses origines dans un marché en constante déréglementation, Uber a émergé triomphant. Opérant dans plus de 58 pays et évalué à environ 66 milliards de dollars américains, Uber s'est rapidement étendu pour établir des branches dans plus de 581 villes dans plus de 82 pays, avec les États-Unis, le Brésil, la Chine, le Mexique et l'Inde étant les pays les plus actifs d'Uber.

Si cela n'était pas assez impressionnant, en 2016, l'entreprise a complété un total de [2 milliards de trajets](http://www.reuters.com/article/us-uber-rides-idUSKCN0ZY1T8) en une semaine. Lorsque vous considérez le fait que le premier milliard de trajets a pris 6 ans à Uber, et que le deuxième milliard a été obtenu en seulement 6 mois, il n'est pas surprenant de voir Uber émerger comme un leader mondial des affaires. Ce phénomène mondial est construit sur une idée simple, séduisante dans son principe - la capacité de héler une voiture avec rien d'autre que votre smartphone.

Il a pris le problème de héler un taxi et a donné à tout le monde une solution équitable tout en capitalisant davantage sur le marché émergent. Et les gens intelligents posent la bonne question : *Comment puis-je créer une application comme Uber pour mes besoins commerciaux ?*

### Débuts modestes

Tout a commencé en 2008, avec les fondateurs d'Uber discutant de l'avenir de la technologie lors d'une conférence. En 2010, Uber a officiellement lancé à San Francisco. En 6 mois, ils avaient 6 000 utilisateurs et fournissaient environ 20 000 trajets. Quelle était la clé de leur succès ? Pour commencer, les fondateurs d'Uber se sont concentrés sur l'attraction des conducteurs et des passagers *simultanément*. San Francisco était le cœur de la communauté technologique aux États-Unis et était ainsi le terrain d'essai parfait pour que cette forme d'innovation technologique prospère.

Au début, Uber a diffusé son application par le bouche-à-oreille, en organisant et en sponsorisant des événements technologiques, et en offrant des trajets gratuits avec leur application aux participants de leurs événements. Cette forme de stratégie de mise sur le marché persiste aujourd'hui - en offrant des réductions de 50 % aux nouveaux passagers pour leur premier trajet Uber. Cette réduction initiale a incité les utilisateurs à devenir des passagers à long terme, et le reste est de l'histoire. Alors que de plus en plus de personnes se tournaient vers les médias sociaux pour parler au monde de cette nouvelle application innovante - le pur génie de leur stratégie marketing a porté ses fruits.

### Cohésion de la technologie produit : Comment fonctionne Uber

Qu'est-ce qui fait d'Uber, Uber ? Pour commencer, c'est l'appel universel, ou la manière dont ils ont rationalisé leur produit, leur logiciel et leur technologie. C'était, au début, frais, innovant, et n'avait jamais été vu auparavant. Donc, si quelqu'un voulait répliquer le modèle, il devrait regarder la stratégie de marque d'Uber.

Pour utiliser Uber, vous devez télécharger l'application, qui a été lancée d'abord sur iPhone, puis étendue à Android et Blackberry.

![Image](https://cdn-media-1.freecodecamp.org/images/yDIB85tHWIguxTk-5yISquZxfjDP8L4mzUUc)

Les cofondateurs d'Uber, Garret Camp et Travis Kalanick, se sont largement appuyés sur 6 technologies clés basées sur la géolocalisation iOS et Android. Ce qui l'a vraiment vendu, cependant, c'était sa valeur centrale claire - la capacité de cartographier et de suivre tous les taxis disponibles dans votre zone donnée. Toutes les autres interactions sont basées sur cette valeur centrale - et c'est ce qui distingue Uber (et distinguera *votre* application) de la foule. Pour créer une application comme Uber, vous devrez avoir :

**1. Fonctionnalités d'enregistrement/connexion :** Uber vous permet de vous enregistrer avec votre prénom, nom, numéro de téléphone et langue préférée. Une fois inscrit, ils vous enverront un SMS pour vérifier votre numéro, ce qui vous permettra ensuite de définir vos préférences de paiement. Les frais de trajet sont facturés après chaque trajet via ce système sans argent liquide.

**2. Fonctionnalités de réservation :** Cela permet aux conducteurs d'accepter ou de refuser les demandes de trajet entrantes et d'obtenir des informations sur l'emplacement actuel et la destination du client.

**3. La capacité d'identifier l'emplacement d'un appareil :** Uber, via le [Framework CoreLocation](https://developer.apple.com/library/ios/documentation/CoreLocation/Reference/CoreLocation_Framework/_index.html) (pour les plateformes iOS) obtient l'emplacement géographique et l'orientation d'un appareil pour planifier l'emplacement et la livraison. La compréhension des fonctionnalités de géolocalisation iOS et Android est cruciale pour cette étape, car c'est ce sur quoi votre application fonctionne.

**4. Directions de point à point :** L'application Uber fournit des directions à la fois au conducteur et à l'utilisateur. Les développeurs de l'application Uber utilisent [MapKit](https://developer.apple.com/library/ios/documentation/MapKit/Reference/MapKit_Framework_Reference/_index.html) pour iOS et [Google Maps Android API](https://developers.google.com/maps/documentation/android/?hl=uk) pour Android pour calculer l'itinéraire et rendre les directions disponibles. Ils ont également mis en œuvre Google Maps pour iPhone et Android, mais ont habilement adapté la technologie d'autres entreprises de cartographie pour résoudre tout problème logistique qui pourrait survenir.

**5. Notifications push et SMS :** Vous recevez jusqu'à 3 notifications instantanément d'Uber lorsque vous réservez un trajet.

* Une notification vous indiquant lorsque le conducteur accepte votre demande
* Une lorsque le conducteur est proche de votre emplacement
* Une dans le cas peu probable où votre trajet a été annulé

Vous recevez également la mise à jour complète sur le statut de votre conducteur, jusqu'à la marque du véhicule et le numéro de plaque d'immatriculation, ainsi qu'une estimation du temps d'arrivée du taxi.

**6. Calculateur de prix :** Uber propose un système de paiement sans argent liquide, payant les conducteurs automatiquement après chaque trajet, traité via la carte de crédit de l'utilisateur. Uber prend 25 % du tarif du conducteur, ce qui permet des profits faciles. Ils se sont associés à Braintree, un leader mondial dans l'industrie des paiements mobiles, mais d'autres bonnes options disponibles sont Stripe, ou Paypal, via [Card.io](https://www.card.io/).

![Image](https://cdn-media-1.freecodecamp.org/images/jSK4uzHjvAgF9B-HZppjCqhtzposxcaTs4ck)

Voici quelques fonctionnalités très recherchées pour le côté utilisateur de l'application :

* **La capacité de voir le profil et le statut du conducteur :** Vos clients se sentiront plus en sécurité en pouvant voir la vérification de votre conducteur, et il est judicieux en matière de sécurité de s'assurer que vous savez qui utilise votre application à des fins lucratives.
* **La capacité de recevoir des alertes :** Recevez des notifications immédiates sur le statut de votre trajet et toute annulation.
* **La capacité de voir l'itinéraire depuis leurs téléphones (Un système de navigation intégré) :** Cela est intrinsèquement lié à vos fonctionnalités de géolocalisation, vous voulez pouvoir diriger vos taxis vers les itinéraires les plus rapides et les plus disponibles.
* **Calcul de prix :** Calculer un prix à la demande et mettre en œuvre un système de paiement sans argent liquide.
* **Une option de "partage de frais" :** Uber a introduit cette option avec un grand succès. Elle permet aux amis de partager le prix du trajet.
* **Demander des conducteurs précédents :** C'est un peu comme avoir votre chauffeur de taxi préféré en composition rapide, et c'est un bon moyen de garantir des clients réguliers.
* **Liste d'attente au lieu de la tarification dynamique :** Évitez le tracas médiatique de l'emploi de la tarification dynamique en utilisant une fonctionnalité de liste d'attente, afin que vos utilisateurs puissent être ajoutés à une liste d'attente plutôt que d'être facturés plus que nécessaire, et pour les empêcher de rafraîchir l'application pendant les heures de pointe, réduisant ainsi les ressources requises par votre infrastructure backend.

Une autre clé du succès d'Uber, qui devrait être notée par les développeurs potentiels d'applications similaires, est la manière dont Uber fonctionne. Ils exploitent plus d'un marché, ce qui équivaut à plus de passagers, plus de conducteurs et plus d'affaires pour l'entreprise. Uber a maîtrisé l'art de la localisation - la capacité de battre les marchés et les concurrents préexistants, ce qui retient davantage leur base de clients en améliorant leur propre stratégie commerciale.

Ils ont pris en compte le contexte et les circonstances locales. Par exemple, ils se sont associés à Paypal en novembre 2013 pour fournir autant de personnes en Allemagne n'utilisent pas de cartes de crédit, et sont passés à des services basés sur des messages SMS en Asie car il y a plus de personnes mais moins de smartphones par habitant. Cela les aide à répondre à divers marchés et à optimiser les profits.

La stratégie marketing d'Uber n'est pas statique - elle est *dynamique*. L'expansion était nécessaire, et le modèle économique tire profit de la saturation du marché des taxis avec leurs clients et conducteurs, stimulant leur croissance exponentielle. Ce que les développeurs d'applications en herbe peuvent retenir de cela, c'est que vous devez concevoir votre application pour la *flexibilité*.

![Image](https://cdn-media-1.freecodecamp.org/images/xjyzI3-4GQNC6sGtfj5nFecOrXfmeIJPAKNK)

Concevez votre application de manière à ce qu'elle puisse encaisser les coups et s'adapter. Avoir un système en place qui vous permet de construire et d'intégrer des changements efficacement au sein de l'application et permet aux membres de l'équipe de communiquer efficacement est d'une importance primordiale.

Ce qui a rendu Uber si réussi, c'est sa capacité à redéfinir notre façon de penser la technologie et son fonctionnement. En effet, il a rendu le marché meilleur et plus efficace grâce au service innovant à la demande.

### Quelle technologie est utilisée pour construire Uber ?

Le côté technologique de l'application est principalement écrit en JavaScript, qui est également utilisé pour calculer l'offre et prédire la demande. Avec les systèmes de dispatch en temps réel construits sur Node.js et Redis. Java, ainsi que Objective-C, est utilisé pour les applications iPhone et Android. [Twilio](http://www.twilio.com/customers/stories/hulu) est la force derrière les messages texte d'Uber, et les notifications push sont mises en œuvre via le [Service de Notifications Push d'Apple](https://developer.apple.com/library/ios/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/Chapters/ApplePushService.html) sur la plateforme iOS et [Google Cloud Messaging](http://developer.android.com/google/gcm/index.html) (GCM) pour l'application Android.

### Combien Uber gagne-t-il ?

En réalité, c'est beaucoup moins que vous ne le pensez. L'évaluation de 66 milliards de dollars, après la commission de 25 % (ce qui représente environ 0,19 $ par trajet) va principalement vers le traitement des cartes de crédit, les intérêts, les taxes, la compensation des employés, le support client, le marketing et divers efforts anti-fraude.

### Combien coûte la création d'Uber ?

Uber n'est pas seulement une application, c'en sont deux - une pour le passager et une pour le conducteur. Le coût de développement d'une application comme Uber dépend de plusieurs facteurs

* le coût de construction d'un MVP
* le développement et l'acquisition de produits
* la résolution des économies de marketing
* le coût constant de construction et d'amélioration des capacités analytiques de votre application

Lorsque vous créez une application comme Uber, vous investirez une somme importante dans les services de conception, le développement backend et web, la gestion de projet, sans parler du développement d'applications natives Android et iOS. Le nombre total d'heures de travail s'élève à environ 5000 heures pour des applications de taxi à la demande similaires, ce qui porte le coût de développement d'une telle application à environ 50 000 $ (en supposant que votre équipe travaille pour 50 dollars de l'heure). Cependant, comme les tarifs horaires varient environ de 20 à 150 dollars, les coûts médians pourraient être plus élevés ou plus bas.

### Conclusion

Pour conclure, le succès d'Uber est dû à plusieurs facteurs, notamment un modèle économique clair et des fonctionnalités basées sur l'interaction, et non l'inverse, combiné à une stratégie marketing axée sur l'attraction des utilisateurs.

La question que tout le monde se pose, bien sûr, est de savoir comment réduire le risque global d'échec en s'assurant que votre idée et votre produit sont viables lorsque vous développez une application ?

Une façon est d'utiliser un partenaire de développement d'applications mobiles (comme [Octodev](https://octodev.net/)) qui a travaillé sur de nombreuses applications de ce type et comprend les processus impliqués. Un avantage d'utiliser un tel partenaire est qu'ils ont travaillé sur de nombreux projets de développement d'applications et ont l'expérience pratique en développement de produits pour éviter les pièges et tirer le meilleur parti de votre vision.

![Image](https://cdn-media-1.freecodecamp.org/images/xBVVhGnGnGEq75DCyMztISQhiCRXGmkrh1nF)
_Processus de développement d'applications Octodev_

Une autre partie importante pour garantir que votre projet de développement d'applications est exécuté rapidement et en douceur est d'avoir une feuille de route claire et une communication régulière pendant le projet. Il existe de nombreuses approches pour y parvenir et nous, chez Octodev, utilisons une approche consultative pour le développement d'applications. Nous nous inspirons de nos implémentations d'applications réussies. [Contactez-nous](https://octodev.net/contact-us/) maintenant si vous souhaitez un coût précis pour votre propre idée d'application comme Uber.

Cet article a été initialement publié sur le [Blog Octodev](https://octodev.net/how-uber-was-made/).