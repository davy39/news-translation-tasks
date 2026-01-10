---
title: Aujourd'hui, j'ai lancé ma première application mobile. Voici ce que j'ai appris
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-28T14:22:33.000Z'
originalURL: https://freecodecamp.org/news/today-i-launched-my-first-mobile-app-heres-what-i-learned-6fc25c14eee6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yUKmN6_dAlYalYjlsu57_w.png
tags:
- name: Cryptocurrency
  slug: cryptocurrency
- name: Design
  slug: design
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: startup
  slug: startup
seo_title: Aujourd'hui, j'ai lancé ma première application mobile. Voici ce que j'ai
  appris
seo_desc: 'By Harshita Arora

  I’ve been writing a fair bit on Medium recently, sharing valuable design and development
  knowledge I gained from working on my first app, Crypto Price Tracker that I just
  launched today, on 28th Jan.

  I wanted to share my story of wo...'
---

Par Harshita Arora

J'ai écrit pas mal d'articles sur Medium récemment, partageant des connaissances précieuses en design et développement que j'ai acquises en travaillant sur ma première application, [Crypto Price Tracker](https://itunes.apple.com/us/app/crypto-price-tracker/id1333696099?ls=1&mt=8), que je viens de lancer aujourd'hui, le 28 janvier.

Je voulais partager mon histoire de travail sur cette application, depuis le jour où j'ai commencé jusqu'à aujourd'hui. J'espère que cet article aidera et inspirera d'autres jeunes programmeurs (ou vraiment quiconque s'intéresse à la création de produits technologiques !) à acquérir des compétences techniques précieuses, à identifier les besoins du marché, à construire de grands produits avec leurs compétences qui répondent à ces besoins du marché.

Un peu de contexte sur moi : je suis une homeschooler de 16 ans. J'apprends le design numérique et la programmation depuis l'âge de 13 ans. J'ai été la plus jeune stagiaire chez Salesforce à Bangalore en hiver 2016.

J'ai participé au programme d'été MIT Launch en été 2017 où mon équipe et moi avons lancé [Universeaty](http://universeatyapp.com/). C'était la première fois que je m'essayais aux applications iOS et j'ai adoré la rapidité avec laquelle il était possible de construire des produits tangibles et de voir les résultats de mon travail en développant des applications mobiles. Transformer mes idées en logiciels était beaucoup plus facile et plus amusant !

J'ai commencé à apprendre Swift et le développement d'applications iOS grâce à des cours en ligne sur [Treehouse](https://teamtreehouse.com/tracks/beginner-ios-development), [Udemy](https://www.udemy.com/ios-11-app-development-bootcamp/), j'ai regardé des vidéos sur YouTube et j'ai pratiqué la construction d'applications basiques. Cela a posé les bases de ma programmation. J'ai commencé à construire des applications plus sérieuses et complexes après quelques semaines d'apprentissage et de pratique.

Vers le 20 novembre 2017, j'ai décidé que je voulais travailler sur une application de suivi des prix des cryptomonnaies, d'alertes et de gestion de portefeuille. J'ai partagé une partie de l'histoire de ma motivation [ici](https://blog.usejournal.com/a-sneak-peek-at-a-beautiful-new-cryptocurrency-price-tracking-portfolio-and-alerts-app-bd16c3985134). J'ai récemment réalisé que partager mon histoire et certaines des leçons que j'ai apprises tout au long de mon parcours est effectivement utile aux autres !

### Commencer

C'était difficile de commencer : incertitude, inconnues, choses à penser et décisions à prendre. Aucune idée de par où commencer. Mais je savais que ma première étape était de mener des recherches de marché pour savoir exactement ce que mon public cible voulait — les fonctionnalités, le design et tout ce que je devrais construire dans l'application.

J'ai posté sur Reddit, des groupes Facebook, Quora, et j'ai demandé à quelques amis qui étaient investis et intéressés par les cryptos. J'ai obtenu des retours solides sur l'idée et j'ai été beaucoup plus informée sur les besoins de mes utilisateurs cibles.

L'étape suivante était de concevoir l'application. J'ai commencé par dessiner les diagrammes de flux utilisateur et les wireframes. Je suis ensuite passée à l'utilisation de logiciels de design pour créer des maquettes et un prototype. J'ai écrit une autre [histoire](https://medium.freecodecamp.org/designing-beautiful-mobile-apps-from-scratch-1a3441ebd604) sur la conception d'applications mobiles à partir de zéro, et j'ai partagé des images de chaque étape de design de l'application Crypto Price Tracker.

Et le résultat final de ce processus était ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*yUKmN6_dAlYalYjlsu57_w.png)
_Un design délicieux :)_

### Développement de Crypto Price Tracker

J'avais assez peur d'atteindre cette étape, car j'étais (et je suis toujours) une débutante en programmation. Je ne connaissais pas beaucoup Swift et je n'avais aucune idée de comment configurer le serveur pour les notifications, parmi de nombreux autres défis techniques. J'avais tant de choses à faire pour l'application avec peu de compétences techniques. Mais j'étais confiante de pouvoir comprendre les choses et apprendre en cours de route en construisant chaque fonctionnalité. Et, avec le recul, je peux dire que je l'ai fait :)

J'ai commencé par importer tous les designs dans Xcode et configurer une version brute pour chaque écran. J'ai divisé mon travail de codage en fonction des fonctionnalités dont j'aurais besoin dans l'application. Plusieurs fois, j'ai dû supprimer des choses de mes spécifications (et modifier les designs) car elles semblaient prendre trop de temps à développer (surtout si elles semblaient offrir peu de fonctionnalités).

J'ai écrit le code de réseau pour afficher les données des API que j'utilisais et j'ai construit l'interface principale de mon application. Je suis ensuite passée à la fonctionnalité "Liste de souhaits" de l'application. Maintenant, pour sauvegarder des données localement sur le téléphone d'un utilisateur, vous devez créer des modèles Core Data — quelque chose avec lequel je n'avais jamais travaillé auparavant. Et d'autres lacunes et défis techniques sont apparus.

Mais j'ai continué à apprendre. Quand j'avais besoin de quelque chose, je le cherchais sur Google. Habituellement, il y avait des réponses utiles, des extraits de code ou des tutoriels vidéo pour presque tout. Chaque fois que je bloquais, je posais des questions sur StackOverflow ou j'envoyais des emails à mes mentors pour obtenir de l'aide. Petit à petit, je me suis sentie beaucoup plus à l'aise pour me lancer dans des choses inconnues.

À la fin des trois semaines que j'ai passées à coder l'application, je me suis beaucoup améliorée en tant que programmeuse. J'ai appris des concepts et j'ai pu les pratiquer en construisant une vraie application. J'ai pu travailler avec un certain nombre de technologies, bibliothèques et frameworks iOS intéressants.

J'ai encore besoin de beaucoup m'améliorer en tant que développeuse. Mon application charge parfois lentement. Ce n'est pas l'application la plus optimisée ou la plus rapide qui existe. Mais je suis toujours assez contente d'avoir pu construire quelque chose d'utile et de précieux.

L'étape suivante que j'avais prévue était de localiser mon application en 10 langues. Je pensais que ce serait facile puisque mon application n'est pas très textuelle. Oh, je me trompais ! La localisation est un processus très chronophage pour les applications. J'écris une autre histoire pour expliquer comment localiser techniquement.

À la fin de 8 semaines (à partir du jour où j'ai commencé les recherches de marché), j'avais entièrement conçu et développé une application qui affichait les prix en temps réel de plus de 1000 cryptomonnaies provenant de 18 échanges en 32 devises fiduciaires. Il y avait des graphiques de prix (affichant les prix historiques sur 1 jour, 1 semaine, 1 mois, 3 mois et 1 an), une gestion de portefeuille, des alertes basées sur le temps et des alertes basées sur des seuils. Elle était localisée en 10 langues. J'ai également optimisé mon application pour l'iPhone X.

Une fois ma version prête, l'étape suivante était d'inviter des utilisateurs à tester et à donner leur avis sur l'application.

### Test et soumission de l'application

J'étais assez fière de mon application et j'étais super excitée de la mettre sur TestFlight et d'inviter tous mes amis et utilisateurs à la tester ! Après une longue attente de deux jours, la revue de l'application bêta a enfin été approuvée. J'ai invité mes amis à la tester et ils ont adoré l'application. Tous ont partagé des retours, des idées pour des fonctionnalités à avoir dans les futures mises à jour, et bien plus encore. L'application n'avait aucun plantage !

La version 1.0 était prête pour la soumission. Mes 100 captures d'écran (5 captures d'écran pour l'iPhone 5.5 pouces et 5 pour l'iPhone 5.8 pouces pour chaque langue) étaient prêtes, mes métadonnées étaient localisées aussi, et ma vidéo de prévisualisation était terminée.

Il y a eu quelques défis inattendus lors du téléchargement de la vidéo de prévisualisation car le nombre d'images par seconde (fps) était trop élevé. À ce stade, j'avais appris à accepter les défis inattendus et à les gérer efficacement. J'ai pu tout terminer et soumettre l'application pour revue à temps.

Deux jours plus tard, à 4h du matin, j'ai reçu l'email de rejet.

Cela m'a rendue extrêmement anxieuse. Tant de pensées me traversaient l'esprit avant de lire les raisons du rejet. Apple a rejeté l'application car le design ne semblait pas bon lorsqu'il était visualisé sur iPad. Je n'avais aucune idée que les applications iPhone uniquement devaient également être compatibles avec les iPads. Dans les heures qui ont suivi, j'ai lu quelques guides et corrigé toutes les contraintes et les problèmes de Auto Layout, testé l'application sur le simulateur iPad et cela a fonctionné. J'ai soumis la version pour revue à nouveau.

Un jour plus tard, j'ai enfin obtenu l'approbation ! C'était un soulagement, et maintenant je pouvais me concentrer à nouveau sur le produit. J'avais reçu une tonne de retours et de rapports de bugs de la part des testeurs. J'ai fait ces petites corrections de bugs et quelques modifications de traductions, et j'ai téléchargé la version finale. Elle a été approuvée en seulement 12 heures ! Mon application était maintenant bien meilleure et je suis contente que tant de personnes l'aient testée et rapporté des bugs qui auraient autrement été signalés dans les avis de l'application par des clients mécontents.

Dans les jours précédant le lancement, j'ai rassemblé cette histoire à partir des notes que j'ai prises et de mon journal quotidien afin de pouvoir partager les leçons avec tout le monde.

### Quelques leçons que j'ai apprises

1. La localisation est une excellente idée. Jusqu'à présent, je regrettais ma décision de localiser mon application en 10 langues. J'avais écrit quelques [réponses Quora](https://www.quora.com/How-do-you-localize-your-metadata-in-the-iOS-and-Mac-App-Store/answer/Harshita-Arora-16?share=9cb57341&srid=ud5cQ) sur la façon dont c'était la chose la plus chronophage que j'ai faite pour mon application et je ne conseillerais à aucun développeur indépendant sans le budget pour externaliser de localiser. Mais maintenant mon opinion a changé. Localiser votre application dans 10 à 12 langues en utilisant Google Translate et en faisant relire par des amis est un excellent moyen d'atteindre un public plus large pour votre application. Apple aime aussi davantage les applications localisées. Vous ne pouvez pas toujours tout faire correctement et chaque chaîne possible localisée. Mais vous pouvez obtenir 80 % des résultats (c'est-à-dire, le texte traduit) avec 20 % du travail.
2. Les gens sont beaucoup plus disposés à vous aider que vous ne le pensez. Je suis très reconnaissante d'avoir un certain nombre d'amis et de mentors qui m'ont beaucoup aidée dans ce parcours. Mais j'ai été simplement stupéfaite de voir combien d'inconnus m'ont répondu lorsque je les ai contactés et m'ont aidée. Très tôt dans mon parcours, lorsque je n'avais qu'un petit prototype de l'interface principale de mon application, j'ai contacté [Carla White](http://carla.is/) après avoir lu son livre incroyable. Elle m'a mentorée et m'a aidée avec ses conseils pour l'application. Alors que je localisais mon application, j'avais besoin de relecteurs pour chaque langue afin de m'assurer que les traductions (effectuées à l'aide de Google Translate) étaient bonnes et spécifiques au contexte. [Pascal](https://twitter.com/DJCalled) a commenté mon histoire sur Medium en offrant son aide pour les traductions allemandes. Je l'ai contacté et, avec un préavis très court, il a vraiment édité mes traductions allemandes ! Et beaucoup d'autres inconnus ont offert leur aide.

Un point clé important à retenir de cela serait : Les gens sont prêts à vous aider. Contactez-les, soyez sincère, et ils vous aideront de toutes les manières possibles ! :D
3. Les retours des utilisateurs dès le début sont super critiques. Non seulement les mots gentils de vos fans ou croyants vous motivent, mais beaucoup de vos premiers utilisateurs vous donneront des idées pour des fonctionnalités, des améliorations de design, et bien plus de retours précieux. Une des erreurs que j'ai faites a été de tester très tard. J'ai téléchargé ma version pour les tests TestFlight seulement ~1 semaine avant le lancement prévu lorsque l'application était presque prête et je ne pouvais pas faire de changements majeurs. Si j'avais demandé à mes utilisateurs de commencer à tester il y a des semaines lorsque je n'avais que l'interface principale, j'aurais obtenu beaucoup de retours et je l'aurais améliorée. Et itéré cela pour chaque fonctionnalité majeure, mon application aurait été bien meilleure. Plusieurs testeurs ont mentionné des choses qui auraient pu être corrigées en 2-3 jours si j'avais envoyé la version pour les tests plus tôt. Donc mon conseil à tout le monde serait : Mettez votre application entre les mains de vos utilisateurs et faites-les la tester dès que possible et obtenez des retours !

### Quelques outils utiles que j'ai utilisés

1. [AppLaunchPad](https://theapplaunchpad.com/) pour créer plusieurs ensembles de captures d'écran (pour de nombreuses localisations) plus rapidement.
2. [Cocoapods](https://cocoapods.org/). [SwiftyJSON](https://cocoapods.org/pods/SwiftyJSON) et [Alamofire](https://cocoapods.org/?q=alamofire) pour écrire un meilleur code de réseau, [Charts](https://cocoapods.org/pods/Charts) pour créer des graphiques de prix. Il y a un cocoapod pour presque tout !
3. [Firebase](https://firebase.google.com/) pour le serveur de notifications push et pour le serveur de cache pour stocker les prix toutes les 5 minutes afin de mettre à jour les graphiques de prix.
4. Deux API pour les prix : [cryptowatch](https://cryptowat.ch/docs/api) et [CoinCap](https://github.com/CoinCapDev/CoinCap.io). Cette [API](http://fixer.io/) pour les taux de change pour la conversion.

C'est génial de pouvoir partager les leçons que j'ai apprises et mon parcours avec un large public. J'espère que cela servira d'inspiration à d'autres personnes pour essayer d'apprendre la programmation et de construire des applications ou vraiment tout ce qui les intéresse. Personnellement, je vais commencer par apprendre le ML et la science des données après mon application — alors n'ayez pas peur d'expérimenter avec différents domaines ! Essayez quelque chose de difficile et quelque chose qui vous met mal à l'aise. Les choses les plus difficiles à faire sont généralement les plus intéressantes et gratifiantes à la fin. :)

Si vous avez aimé lire ceci et avez des retours ou des pensées à partager, n'hésitez pas à m'envoyer un email à harshita@harshitaapps.com. Et si vous aimez mon application, vous pouvez la télécharger depuis l'App Store [ici](https://itunes.apple.com/us/app/crypto-price-tracker/id1333696099?ls=1&mt=8). :)