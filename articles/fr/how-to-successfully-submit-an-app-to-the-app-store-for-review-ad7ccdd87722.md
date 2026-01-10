---
title: Comment soumettre une application à l'App Store pour examen avec succès
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-19T21:53:59.000Z'
originalURL: https://freecodecamp.org/news/how-to-successfully-submit-an-app-to-the-app-store-for-review-ad7ccdd87722
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zfrYdaUXd2-v6f1KaepbnA.jpeg
tags:
- name: Apple
  slug: apple
- name: iOS
  slug: ios
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment soumettre une application à l'App Store pour examen avec succès
seo_desc: 'By Irina Bulygina

  The Apple team has a strict vision concerning the quality of mobile applications.
  This is really great for the users, because the Apple team works hard to make the
  App Store a trustworthy ecosystem. The App Store has a high threshol...'
---

Par Irina Bulygina

L'équipe Apple a une vision stricte concernant la qualité des applications mobiles. C'est vraiment génial pour les utilisateurs, car l'équipe Apple travaille dur pour faire de l'App Store un écosystème de confiance. L'App Store a un seuil élevé et des exigences strictes, non seulement pour les performances de l'application, mais aussi pour la mise en œuvre de mesures de sécurité appropriées. L'utilisateur peut être sûr que les applications iOS sont fiables.

Cependant, répondre à toutes les exigences peut devenir un vrai cauchemar pour les développeurs. Juste pour comparer, le développement de l'application peut prendre seulement quelques semaines, tandis que le temps passé à passer l'examen de l'App Store peut être jusqu'à un mois (ou même des mois si le développeur ignore les [directives pour les développeurs d'Apple](https://developer.apple.com/app-store/review/guidelines)).

Je travaille chez [Dashdevs](http://www.dashdevs.com) en tant que Client Engager. Mon principal devoir est de créer des applications à partir de zéro pour qu'elles passent l'examen. Je travaille avec les exigences des clients. Nous avons plus de 9 ans d'expertise dans le développement d'applications iOS. Nous avons travaillé avec divers marchés, industries et différentes entreprises.

La complexité des applications varie également. Nous avons soumis 250+ applications pour examen en 2018. Toutes n'ont pas passé l'examen du premier coup. Mais parfois, nous avons ressenti une joie débridée suite à un bon examen.

Dans cet article, je souhaite partager notre expérience afin que vous puissiez éviter les erreurs courantes et passer facilement l'étape de l'examen.

### **Comment postuler à l'App Store**

Une toute nouvelle application iOS brillante a été développée, testée et est prête à voir le monde. Un fichier binaire est déjà téléchargé sur le panneau iTunes Connect. Mais que faut-il d'autre ?

* Vous devez ajouter des informations de base (description, tags, contacts) sur votre application, ajouter des captures d'écran et les identifiants d'un compte utilisateur de démonstration (si votre application nécessite une autorisation).
* Vous devez inclure des explications détaillées des fonctionnalités non évidentes (comme l'utilisation de gestes natifs) et des achats intégrés dans les notes de révision de l'application.
* Ensuite, vous devez appuyer sur le bouton « Soumettre pour examen » pour informer Apple que votre application est prête pour l'App Store.

Vous serez averti si quelque chose d'important dans la description est manquant. Ensuite, le statut de l'examen de l'application sera changé en « En attente d'examen ». Cela peut prendre quelques jours avant que la vérification réelle ne commence. Lorsque l'équipe de vérification commence réellement l'examen, le statut de l'application sera changé en « En cours d'examen ».

**_Astuce:_** _Vous économiserez des efforts en installant l'application iTunes Connect sur votre iPhone pour recevoir des notifications immédiates sur tous les changements de statut._

L'examen de l'App Store est une étape obligatoire pour toutes les applications. Le processus de vérification de l'application suit les directives Apple, garantissant la meilleure et la plus sûre expérience utilisateur.

Ils examinent également les informations principales sur l'application. Une partie de la vérification est effectuée automatiquement à l'aide de scripts, et l'autre partie est effectuée par des personnes. Si votre application présente un problème, vous recevrez une notification avec une description précise de ce qui doit être corrigé. Le délai pour la première étape de l'examen est de 3 à 7 jours. L'inspection des mises à jour de l'application est plus rapide, de 1 à 3 jours.

![Image](https://cdn-media-1.freecodecamp.org/images/9WES-31NeFCei5gylQdCdN0Jno1fRnw1HoVp)

Au cours des dernières années, j'ai eu quelques problèmes avec des applications soumises pour examen. Certains étaient faciles à corriger, et d'autres ont pris de nombreuses heures.

### Alors, pourquoi vos applications n'ont-elles pas passé du premier coup ?

Voici ce que vous devez prendre en compte.

#### **Utilisez les directives de l'interface humaine (HIG) pour le design**

Vos designers doivent suivre les [HIG](https://developer.apple.com/design/human-interface-guidelines) dès le début. Les tailles et positions des boutons, l'utilisation correcte des éléments de base de l'UI et la navigation doivent être conformes aux directives Apple. La correction des problèmes avec les HIG peut vous coûter cher si vous trouvez ces problèmes à la fin du développement.

**_Astuce:_** _Ne créez pas une application qui semble de manière confuse similaire à un produit Apple existant ou à une autre application (pas de copies). L'équipe Apple est très stricte à ce sujet._

#### **Vérifiez la liste des fonctionnalités**

Votre application doit inclure des fonctionnalités, du contenu et une interface utilisateur qui l'élèvent au-delà d'un site web repackagé. L'équipe Apple se soucie de l'utilité et des avantages pour l'utilisateur.

Il y a eu un cas où l'une de nos applications a été rejetée parce que l'équipe de révision d'Apple a supposé que notre application n'avait pas besoin d'avoir la fonctionnalité d'inscription/connexion. Nous avons donc envoyé un avis de recours avec les preuves de la pertinence de cette fonctionnalité.

Un autre cas était un peu différent : l'application était trop simple pour l'AppStore (juste un calendrier amusant). L'application avait besoin de fonctionnalités supplémentaires. Nous l'avons améliorée en ajoutant une fonction de partage, et elle a passé l'examen.

Une autre règle significative à respecter est que votre application ne doit pas nécessiter l'installation d'autres applications.

#### **Fournissez un compte de démonstration avec toutes les fonctionnalités à l'équipe Apple**

L'équipe de révision de l'App Store essaiera définitivement de s'inscrire à votre application, mais ils devront également vérifier le reste des fonctionnalités. Par exemple, pour examiner les fonctionnalités d'une application bancaire, ils doivent avoir un compte avec une carte activée et quelques transactions dessus. Vous devez être sûr que le compte accède à toutes les fonctionnalités et que toutes les fonctionnalités back-end sont activées.

**_Astuce:_** _ne fournissez pas ce compte à votre équipe QA pour les tests habituels, surtout pendant la période de révision. Une fois, nous avons envoyé une application pour révision, et en même temps, notre ingénieur en assurance qualité testait la fonctionnalité de blocage et a accidentellement banni un nouvel utilisateur._

#### **Pas de "test", "bientôt disponible", "bêta", "essai", "Testflight" dans l'application.**

Toutes vos fonctionnalités futures, inachevées ou de démonstration ne doivent pas être utilisées dans l'application. N'utilisez pas ces mots pour le contenu de votre application, même pour les captures d'écran et les descriptions dans l'application. Si vous devez tester votre application, vous pouvez rejoindre les [services Testflight](https://developer.apple.com/testflight/).

Nous avons fait une erreur ridicule avec une autre de nos applications. Comme vous le savez peut-être, pour préparer une soumission à l'examen, les développeurs prennent parfois des captures d'écran de l'application directement depuis TestFlight. Ces images sont publiées comme captures d'écran de l'application réelle pour l'App Store. Si vous faites cela, vérifiez deux fois, car il peut y avoir l'étiquette "Testflight" dans la barre d'état. Lorsque cela se produit, votre application est rejetée. Cette petite chose peut bloquer la soumission de votre application.

#### **Performance**

Aucun plantage, aucune performance lente, aucune fuite de mémoire ne sont autorisés pour les applications de l'App Store. Les bundles d'applications incomplets et les binaires qui plantent ou présentent des problèmes techniques évidents dans les applications sont rejetés immédiatement.

#### **Décrivez uniquement les fonctionnalités existantes**

Aucune publicité pour les fonctionnalités futures ne doit figurer dans la description de l'application.

#### **Conditions générales / Politiques de confidentialité**.

Ces documents ou les liens vers eux doivent être ajoutés à l'application. Vous devez expliquer à l'utilisateur comment ses données sensibles sont traitées et quelles données sont partagées par l'application avec des tiers et à quelles fins (par exemple, outils d'analyse, réseaux publicitaires et SDK tiers, etc.). Un utilisateur doit connaître les politiques de suppression et de conservation de votre application.

#### **Propriété intellectuelle**

Vous devez avoir les autorisations pour utiliser tous les matériaux dans l'application (problème de droit d'auteur). N'utilisez pas de marques commerciales tierces, d'œuvres protégées par des droits d'auteur ou d'idées brevetées dans votre application si vous n'avez pas obtenu la licence nécessaire. Souvenez-vous des restrictions contre l'utilisation de contenu sexuel ou pornographique, de marijuana, de tabac, de substances contrôlées, de citations trompeuses de textes religieux et de violence dans les applications mobiles.

#### **Licences**

Si certaines réglementations dans votre domaine d'activité exigent une licence pour fournir vos services, comme la FinTech, la Médecine, les Soins de santé, etc., vous devez joindre une copie de ces documents à l'examen de l'application. Si une application nécessite un matériel spécifique, vous devez fournir un certificat ou une licence correspondant pour ce matériel.

Un autre cas de notre expérience : une application utilisait une imprimante à autocollants spéciale. Au début, l'application a été rejetée, et nous avons dû obtenir un certificat pour utiliser ces imprimantes. Il nous a fallu un mois pour obtenir l'approbation officielle du fabricant du matériel.

Un autre exemple était une application de banque numérique. Nous avons dû fournir à l'équipe de révision de l'App Store la licence de monnaie électronique. Cela s'applique également à l'industrie des cryptomonnaies.

> « Les applications facilitant les offres initiales de pièces (ICO), le trading de contrats à terme sur cryptomonnaies et d'autres cryptosécurités ou quasi-sécurités doivent provenir de banques établies, de sociétés de valeurs mobilières, de négociants en contrats à terme (FCM) ou d'autres institutions financières approuvées et doivent se conformer à toutes les lois applicables. »

#### **Demandez les permissions à l'utilisateur**

Votre application doit demander les permissions pour utiliser la caméra, le microphone, la localisation, l'accès aux contacts, au rouleau de la caméra et aux emplacements de l'utilisateur. Les permissions doivent être pertinentes pour les fonctionnalités de l'application. L'équipe de l'App Store veille à ce que les informations collectées dans l'application soient stockées de la bonne manière et empêche leur utilisation, divulgation ou accès non autorisé par des tiers.

**_Astuce:_** _n'oubliez pas d'ajouter une description de ces permissions au fichier .plist. C'est une autre raison courante de rejet._

#### **Pas de données fictives dans l'application**

Si votre application n'a pas de contenu pour certains formulaires dont vous avez besoin, masquez cet élément ou ajoutez un espace réservé avec une explication sur la manière dont l'utilisateur peut obtenir les données nécessaires.

Parfois, les développeurs codent en dur pour montrer la fonctionnalité maximale de l'utilisateur. Par exemple, votre application a une section avec des graphiques affichant les statistiques d'activité de l'utilisateur dans l'application. Dans ce cas, il doit y avoir un espace réservé avec un texte d'invite indiquant que le graphique sera disponible lorsque l'utilisateur commencera à utiliser l'application au quotidien.

Avec les publicités, c'est la même chose : vous ne pouvez pas soumettre l'application avec des bannières publicitaires vides ou des publicités de test.

#### **Capacité à modérer le contenu de l'utilisateur**

« Bloquer un utilisateur/contenu », « signaler un utilisateur/contenu », « liste noire pour les utilisateurs » sont des fonctionnalités requises pour l'application si elle fournit une communication multi-utilisateurs (par exemple, flux, chats, groupes). En tant que propriétaire de produit, vous devez être conscient que différentes personnes utiliseront votre application et que certaines d'entre elles peuvent déranger les autres. Vous devez fournir à vos utilisateurs la capacité de gérer le contenu et la communauté avec lesquels ils interagissent.

### Options de publication

Avec chaque soumission pour examen, mon équipe gagne une nouvelle expérience. Mon principal conseil est de soumettre votre application à l'examen de l'App Store dès que vous avez développé le MVP de votre application. Gardez à l'esprit que même si vous passez l'examen, cela ne signifie pas que l'application sera publiée.

Il y a trois actions différentes que vous pouvez entreprendre après un examen réussi :

* **Publier manuellement cette version** : en tant que développeur ou gestionnaire d'application, vous devez aller dans le panneau iTunes Connect et appuyer sur le bouton pour publier l'application.
* **Publier automatiquement cette version** : cela signifie que l'application sera publiée dès qu'elle passera l'examen.
* **Publier automatiquement cette version après l'examen de l'App, pas avant le...** : vous pouvez sélectionner l'heure/date de la publication. Si votre application passe l'examen, elle sera publiée à ce moment-là.

Ces options peuvent aider les développeurs et les propriétaires/gestionnaires de produits à passer l'examen et à attendre le début de la campagne marketing. Vous devez savoir que le premier examen de l'application est le plus critique, et donc l'équipe de l'App Store vérifie l'application pendant une période beaucoup plus longue et plus minutieusement. Chaque mise à jour ultérieure est également examinée, mais cela prend moins de temps pour la vérification. Parfois, cela peut prendre seulement quelques heures.

L'App Store peut rejeter votre application. Ce n'est pas grave. Ne paniquez pas. Si vous comprenez la raison, vous corrigez simplement le problème et soumettez à nouveau l'application pour examen. Si vous avez des questions ou souhaitez fournir des informations supplémentaires, vous pouvez utiliser le Centre de résolution pour communiquer avec l'équipe de révision de l'App. Ils sont prêts à vous aider avec votre application. Nous avons corrigé de nombreux problèmes avec leur aide.

J'espère que les exemples mentionnés dans cet article vous seront utiles et que toutes vos applications iOS passeront la vérification de l'App Store dès la première tentative.

P.S. Liens utiles :

* [Guide de programmation des applications](https://developer.apple.com/library/content/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007072)
* [Guide de programmation des extensions d'applications](https://developer.apple.com/library/content/documentation/General/Conceptual/ExtensibilityPG/)
* [Directives de stockage des données iOS](https://developer.apple.com/icloud/documentation/data-storage/index.html)
* [Directives de l'interface humaine](https://developer.apple.com/design/human-interface-guidelines/)
* [Ressources marketing et directives d'identité](https://developer.apple.com/app-store/marketing/guidelines/)
* [Directives pour l'utilisation des marques commerciales et des droits d'auteur d'Apple](http://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html)