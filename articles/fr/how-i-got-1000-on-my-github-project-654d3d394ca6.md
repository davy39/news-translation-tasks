---
title: Comment j'ai obtenu 1 000 étoiles sur mon projet GitHub, et les leçons apprises
  en cours de route
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-10-24T07:12:01.000Z'
originalURL: https://freecodecamp.org/news/how-i-got-1000-on-my-github-project-654d3d394ca6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*GKW7LslZMfOLVbqC4ok1Ow.png
tags: []
seo_title: Comment j'ai obtenu 1 000 étoiles sur mon projet GitHub, et les leçons
  apprises en cours de route
seo_desc: 'By Andrea Bizzotto

  I’ve been an iOS developer since 2012. I started writing open source code, to stop
  re-inventing the wheel and carry over my best code across projects.

  While some of my early projects had gathered some interest from the community, n...'
---

Par Andrea Bizzotto

Je suis développeur iOS depuis 2012. J'ai commencé à écrire du code open source, pour **arrêter de réinventer la roue** et **réutiliser mon meilleur code** dans différents projets.

Alors que certains de mes premiers projets avaient suscité _un certain_ intérêt de la communauté, aucun d'entre eux n'a décollé comme [**SwiftyStoreKit**](https://github.com/bizz84/SwiftyStoreKit).

Avant de partager la recette secrète qui a rendu cela possible, laissez-moi dire une chose :

> Je veux que mon code ait un **impact** dans le monde.

> Je veux que mon code donne du pouvoir aux développeurs, afin qu'ils puissent se concentrer sur la création de grandes applications.

> Si je réussis, toutes les corrections de bugs, les questions répondues et le temps non rémunéré que j'ai investi en vaudront la peine.

Les logiciels open source **ont un effet de levier**. Mon code atteint les utilisateurs finaux via plusieurs applications et permet à d'autres développeurs d'être plus productifs.

**Quel est cet effet de levier ?**

Selon l'API [Cocoapods Metrics](http://blog.cocoapods.org/metrics-api/), **SwiftyStoreKit** [a été téléchargé](http://metrics.cocoapods.org/api/v1/pods/SwiftyStoreKit.json) **42 302 fois** et installé dans **1 194 applications** au 20 octobre 2016.

![Image](https://cdn-media-1.freecodecamp.org/images/1*aRR-MUwscyB2oEp8imuKgg.png)
_Page du trafic GitHub pour SwiftyStoreKit (20 octobre 2016)_

_Pour contexte, [AFNetworking](https://github.com/AFNetworking/AFNetworking) (l'un des principaux projets iOS) [a été téléchargé](http://metrics.cocoapods.org/api/v1/pods/AFNetworking.json) 21 659 973 fois et installé dans 413 742 applications._

Mais assez de vantardise maintenant. ?

Mon propos est que **vous** pouvez le faire aussi.

* [**Restez au top de votre jeu**](https://medium.com/@ajithrnayak/stayin-on-top-of-your-game-ios-newsletters-blogs-developers-companies-to-follow-527b859b3bb5#.mml1nu6jc).
* Écrivez votre propre code et rendez-le open source, ou contribuez [à des projets existants](https://github.com/vsouza/awesome-ios).
* **Vous grandirez en tant que développeur** et vous pourrez vraiment aider et bénéficier aux autres.
* Faire cela est excellent pour votre CV. Cela vous fera **sortir du lot** et **obtenir de meilleurs emplois et clients**.

Alors, comment ai-je obtenu toutes ces ⭐⭐⭐⭐⭐ ?

### Ma recette

1. Choisissez le bon projet
2. Rendez-le facile à utiliser
3. **Écrivez le meilleur README possible**
4. Partagez **aux bons endroits**
5. **GitHub Trending**
6. **Recherche Google**
7. Continuez à grandir

Examinons ces points en détail.

### 1. Choisissez le bon projet

Comment choisir ? Une bonne façon de commencer est de **résoudre un problème que vous avez**. Dans mon cas, j'avais besoin d'un framework pour les achats intégrés (IAP) pour [l'une de mes applications](https://itunes.apple.com/app/id930804327).

Les IAP sont un moyen très populaire de monétiser vos applications dans l'App Store.

Malheureusement, le framework [StoreKit](https://developer.apple.com/documentation/storekit) d'Apple n'est pas exactement la chose la plus facile à utiliser :

* De nombreuses API natives à apprendre, principalement conçues à l'ère de l'Objective-C.
* Divers types d'achats intégrés.
* Les considérations de sécurité sont très importantes.
* Tester que vos flux d'achat sont corrects est difficile.

Un framework IAP léger pour faciliter les choses était vraiment nécessaire, donc **SwiftyStoreKit** était le bon projet.

### 2. Rendez-le facile à utiliser

Alors que j'ai essayé quelques autres bibliothèques tierces pour les IAP auparavant, aucune n'était aussi simple que je l'espérais.

J'ai commencé à construire **SwiftyStoreKit** lorsque Apple a sorti Swift 2. J'ai utilisé les **closures**, les **énumérations** et les nouvelles **fonctionnalités de gestion des erreurs** du langage pour écrire une API propre et facile à utiliser.

Avec **SwiftyStoreKit**, vous n'avez plus besoin de **registrer explicitement** un observateur pour la file d'attente des opérations de paiement. Vous appelez simplement une méthode asynchrone pour votre IAP, et mettez à jour l'état de votre application et l'interface utilisateur à la fin.

J'ai emprunté des idées et des modèles de code à d'autres projets open source populaires. Et j'étais satisfait des résultats.

### 3. Écrivez le meilleur README possible

Votre README est la **page d'accueil** de votre projet. Vous devriez y consacrer beaucoup de temps.

Il doit **avoir l'air** bien ! Si vous construisez un contrôle d'interface utilisateur, incluez un gif animé, des captures d'écran, ou même un lien vers un prototype. [Swift Messages](https://github.com/SwiftKickMobile/SwiftMessages) fait cela très bien.

Il doit inclure des badges pour que vous puissiez rapidement voir l'état du projet. Beaucoup de projets utilisent [shields.io](http://shields.io/). Vous devriez en faire de même.

Le README doit mettre en avant :

* Quelles sont les **fonctionnalités** et comment utiliser le projet en **documentant clairement l'API**.
* **Comment l'installer**. Note : Supportez autant d'outils de gestion de dépendances que possible, _pas seulement [Cocoapods](https://cocoapods.org/)._
* **Les plateformes supportées**. Vous l'aurez deviné, autant que vous le pouvez.
* **Les langues supportées**, avec des liens vers les branches ou tags appropriés pour les différentes versions linguistiques.
* Liste des **problèmes connus** (optionnel). Cela peut servir de résumé des problèmes actuels du projet.

De plus, vous pouvez ajouter une section FAQ, des références à des projets et ressources connexes, une liste de crédits, et la [**licence**](http://choosealicense.com/licenses/).

**Très important** : si vos utilisateurs ouvrent beaucoup de problèmes demandant des clarifications, votre README n'est pas assez bon. Répondez aux questions et améliorez-le en conséquence.

**Incluez un exemple de démonstration.** Cela aide les autres à utiliser votre projet. Cela sert de référence d'implémentation et montre comment intégrer votre code dans une application réelle.

### 4. Partagez aux bons endroits

Certains utilisateurs de GitHub maintiennent des listes de projets open source populaires par plateforme ou langage. J'ai soumis des **Pull Requests** pour inclure **SwiftyStoreKit** sur [Awesome iOS](https://github.com/vsouza/awesome-ios) et [Awesome Swift](https://github.com/matteocrippa/awesome-swift).

Ne vous limitez pas à GitHub :

* Trouvez des sites web qui agrègent des projets open source et soumettez le vôtre.
* Faites figurer votre projet dans des newsletters populaires pour votre langage ou plateforme.
* Partagez sur les réseaux sociaux avec des développeurs et comptes pertinents. Certains bons canaux sont **Product Hunt**, **Hacker News**, **Twitter**, **Reddit**.

### 5. GitHub Trending = Beaucoup de ⭐⭐⭐⭐⭐

Si vous apparaissez dans la liste **GitHub Trending**, votre projet peut vraiment décoller !

Pour moi, ce fut une surprise. Un collègue au travail m'a dit que **SwiftyStoreKit** était dans la liste des [tendances hebdomadaires](https://github.com/trending/swift?since=weekly) Swift sur GitHub. À partir de là, j'ai commencé à recevoir jusqu'à 50 étoiles par jour !

Comment apparaître dans la liste **GitHub Trending** ? [Lisez ceci](https://blog.cwrichardkim.com/how-to-get-hundreds-of-stars-on-your-github-project-345b065e20a2#.ndsxn9v7g)).

**Note** : Bon projet + grande visibilité = beaucoup d'intérêt. **Soyez prêt à suivre.**

### 6. Recherche Google

La recherche Google a été une grande source de trafic organique :

![Image](https://cdn-media-1.freecodecamp.org/images/1*5UnDJgk2HK8kv0ufQQkWkQ.png)
_Sites référents principaux pour SwiftyStoreKit_

En fait, la recherche de « Swift StoreKit » et « Swift In App Purchase » montre **SwiftyStoreKit** comme le **deuxième** et **quatrième** résultat respectivement :

![Image](https://cdn-media-1.freecodecamp.org/images/1*-uUd9yN2IK4hDYtQzPTfeg.png)
_Recherche Google pour Swift StoreKit_

Je n'ai pas fait de recherche de mots-clés pour améliorer le classement SEO de mon projet. Il est simplement arrivé en tête une fois qu'il est devenu populaire.

Néanmoins, si vous planifiez une bonne stratégie SEO, les résultats peuvent être excellents !

### 7. Continuez à grandir

Une fois que votre projet est populaire, les gens poseront beaucoup de questions et ouvriront des pull requests.

À un moment donné, un [contributeur](https://github.com/phimage) a porté **SwiftyStoreKit** sur macOS et a ajouté la prise en charge de la vérification des reçus. Je n'avais aucune expérience dans ces domaines, et c'était génial que quelqu'un aide à améliorer le projet !

D'autres contributions précieuses ont suivi, et je me suis retrouvé avec deux casquettes : **développeur principal** et **mainteneur**.

Être un bon mainteneur nécessite un **bon jugement** :

* Évaluez soigneusement les demandes de fonctionnalités. Visez à garder votre API propre et évitez le gonflement du code. Cela est particulièrement vrai pour **SwiftyStoreKit** car c'est un framework _léger_.
* Pour toute pull request ajoutant une fonctionnalité utile, n'ayez pas peur de demander des modifications pour garder le code propre et cohérent.
* Vous pouvez refuser les pull requests qui sont hors de portée ou si le code existant les couvre déjà.
* Soyez toujours courtois avec les contributeurs. Si vous rejetez leurs modifications, expliquez poliment pourquoi. Ne soyez pas comme [Linus Torvalds](http://www.theregister.co.uk/2016/07/11/linus_torvalds_in_sweary_rant_about_punctuation_in_kernel_comments/). ?

### Ce que j'ai appris

**SwiftyStoreKit** a été un excellent projet et m'a poussé dans le rôle de mainteneur pour la première fois.

Cela m'a forcé à augmenter mes connaissances sur les achats intégrés, surtout lorsque d'autres personnes ont fait des contributions.

Cette citation sur la gestion semble appropriée ici :

> En réalité, le plus grand défi pour une entreprise open sourçant un projet est l'obligation de gestion. Cette responsabilité est principalement une question de travail avec les gens et doit être gérée correctement — surtout si un projet gagne suffisamment en popularité. La plupart des projets ne deviennent pas assez grands pour que leur gestion devienne un fardeau. — [Artsy Blog](https://www.objc.io/issues/22-scale/artsy/)

Je n'ai pas toujours été en mesure de répondre aux questions à temps. J'espère faire mieux à l'avenir et améliorer mon processus de diverses manières :

* Ajouter un fichier CONTRIBUTING décrivant la manière recommandée d'ouvrir des problèmes et des pull requests, comme le font les projets open source populaires.
* Ajouter un Code de Conduite.
* Ajouter un [linting de code](https://github.com/realm/SwiftLint).
* Ajouter une couverture de **tests unitaires**, car j'ai besoin de **confiance** pour faire des modifications. Vraiment, _j'aurais dû faire cela depuis longtemps_.

Je suis à un stade où **SwiftyStoreKit** n'est pas assez grand pour devenir un fardeau à gérer. Je veux que ce projet s'épanouisse et j'accueille favorablement les contributions de la communauté.

### Crédits

Divulgation : Il y a quelque temps, j'ai découvert cette excellente histoire de [Richard Kim](https://blog.cwrichardkim.com/@cwRichardKim) sur Medium :

> [Comment obtenir des centaines d'étoiles sur votre projet GitHub](https://blog.cwrichardkim.com/how-to-get-hundreds-of-stars-on-your-github-project-345b065e20a2#.g8e2vl8hi)

Cela m'a ouvert les yeux sur ce qui fait qu'un projet open source se distingue. J'ai suivi ses conseils depuis. Cela a vraiment porté ses fruits et je tiens à le remercier pour ces informations.

### Conclusion

L'open source peut être une expérience très enrichissante, vous faisant grandir avec vos projets.

J'ai aidé des équipes dans diverses entreprises pendant plus de 10 ans, utilisant beaucoup de logiciels open source en cours de route.

Écrire du code open source est un excellent moyen de rendre à notre grande communauté, et j'apprécie profondément ce processus.

#### À rendre le monde meilleur, une ligne de code à la fois !

#### Mise à jour 2017-02-25 : Lisez ma suite à cet article sur [Maintenir un projet open source en croissance](https://medium.com/@biz84/maintaining-a-growing-open-source-project-1d385ca84c5#.legbfq8jl).

_À propos de moi : Je suis un développeur iOS freelance, jonglant entre le travail contractuel, l'open source, les projets parallèles et le blogging._

_Je suis [@biz84](https://twitter.com/biz84) sur Twitter. Vous pouvez également voir ma page [GitHub](https://github.com/bizz84). Retours, tweets, gifs amusants, tout est bienvenu ! Mon préféré ? Beaucoup de ???. Oh, et du pain aux bananes._