---
title: Comment construire un système de design avec une petite équipe
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-24T15:47:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-design-system-with-a-small-team-53a3276d44ac
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bPOUHDfQzUG7hVlz_CLLpA.jpeg
tags:
- name: Design
  slug: design
- name: Sketch
  slug: sketch
- name: Style Guide
  slug: style-guide
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
seo_title: Comment construire un système de design avec une petite équipe
seo_desc: 'By Naema Baskanderi

  Last night my small team and I headed out to do a little networking and learn about
  Design Systems. Being that is was the buzzword of 2017, we were eager to learn how
  we could create our own.

  We had heard all the wonderful benefit...'
---

Par Naema Baskanderi

La nuit dernière, mon petite équipe et moi sommes sortis pour faire un peu de réseautage et en apprendre davantage sur les systèmes de design. Étant donné que c'était le mot à la mode de 2017, nous étions impatients d'apprendre comment nous pourrions créer le nôtre.

Nous avions entendu tous les avantages merveilleux de la création d'un système de design : gagner du temps, réduire les débats, favoriser la collaboration, l'adoption, et plus encore. J'étais excitée !

Toutes les présentations parlaient de la manière de créer un système de design. Cependant, celles-ci concernaient des **grandes** équipes ou des équipes disposant de ressources dédiées, voire une équipe DesignOps _(2ème mot à la mode de 2017)_ pour construire et maintenir le système de design.

À la fin de la soirée, nous sommes repartis un peu découragés. Mais nous n'étions pas seuls. Pendant la séance de questions-réponses, beaucoup demandaient :

_Comment puis-je construire un système de design en tant que designer unique ?_

_Je suis le seul designer, quel conseil avez-vous pour moi ?_

Mais mon équipe et moi avons décidé de ne pas laisser cela nous arrêter. Nous allons tout de même créer notre propre système de design. Avant de plonger dans le sujet, voici un peu de contexte.

![Image](https://cdn-media-1.freecodecamp.org/images/w7MV47tWonjOTDKdvUFgLR76rTke2MdUeQEx)

#### Qu'est-ce qu'un système de design ?

> Un système de design offre une bibliothèque de style visuel, de composants et d'autres éléments documentés et publiés par un individu, une équipe ou une communauté sous forme de code et d'outils de design afin que les produits adoptants puissent être plus efficaces et cohérents. — [Nathan Curtis](https://medium.com/eightshapes-llc/defining-design-systems-6dd4b03e0ff6)

En termes simples, un système de design est une collection de composants réutilisables pour unifier des produits entiers.

De nombreuses personnes ont écrit des articles approfondis et des livres sur les systèmes de design. En voici quelques-uns que vous pourriez trouver utiles :

[**Un guide complet des systèmes de design - Blog InVision**](https://www.invisionapp.com/blog/guide-to-design-systems/)  
[_Des entreprises comme Airbnb, Uber et IBM ont changé leur façon de concevoir des produits numériques en intégrant leurs propreswww.invisionapp.com](https://www.invisionapp.com/blog/guide-to-design-systems/)[**Systèmes de design, guides de style et bibliothèques de motifs : Oh là là ! - UXcellence**](https://uxcellence.com/2017/design-systems-style-guides-pattern-libraries)  
[_De nombreux designers utilisent les termes système de design, bibliothèque de motifs et guide de style de manière interchangeable. Mais ils ne veulent pas dire la même choseuxcellence.com](https://uxcellence.com/2017/design-systems-style-guides-pattern-libraries)[**Manuel des systèmes de design**](https://www.designbetter.co/design-systems-handbook)  
[_Un système de design unit les équipes produit autour d'un langage visuel commun. Dans ce livre, apprenez comment vous pouvez créer un designwww.designbetter.co](https://www.designbetter.co/design-systems-handbook)[**Créer un système de design : la checklist du processus en 100 points**](https://www.uxpin.com/studio/ebooks/create-design-system-guide-checklist/)  
[_Sachez comment construire un système de design étape par étape. Basé sur des projets réels. Créez un inventaire UI, obtenez l'adhésion, créez des couleurswww.uxpin.com](https://www.uxpin.com/studio/ebooks/create-design-system-guide-checklist/)

#### Guide de style vs. Système de design

Vous pourriez penser, c'est bien mais **_n'est-ce pas simplement un guide de style ?_**

> Un guide de style est un artefact du processus de design. Un système de design est un produit vivant, financé, avec une feuille de route et un backlog, servant un écosystème. — [Nathan Curtis](https://twitter.com/nathanacurtis/status/656829204235972608?lang=en)

De plus, un système de design est un ensemble de composants de différentes tailles (ou molécules) qui peuvent être assemblés de manière infinie pour créer une série de composants plus grands. Le [Atomic Design](http://atomicdesign.bradfrost.com/) de Brad Frost est l'inspiration pour la conception des composants.

#### Avantages d'un système de design

> Le défi auquel nous sommes confrontés aujourd'hui est que les outils ne communiquent pas très bien entre eux, des détails passent à travers les mailles du filet, il y a un énorme fossé entre le design et l'ingénierie, et nous devons faire beaucoup de travail manuel pour nous assurer que nous sommes toujours au top de tout. — [UX Bootcamp](https://blog.prototypr.io/pattern-library-style-guides-design-systems-do-you-need-one-b7857af0f255)

En tant que petite équipe travaillant sur des logiciels d'entreprise B2B, nous nous sommes lancés dans la création d'un système de design avec un temps, un budget et des ressources limités. Je voulais rappeler à notre équipe les avantages.

Globalement, notre équipe gagnerait du temps grâce à :

* Réduction des débats — Pas besoin de perdre du temps à revisiter les décisions de design pour le même composant
* Composants réutilisables rendant l'échelle possible
* Collaboration accrue — améliorer le travail à distance et dans différents bureaux

J'avais une raison égoïste de vouloir construire un système de design. J'ai rapidement réalisé que, si nous réussissions, nous pourrions automatiser de nombreuses tâches, nous laissant du temps pour faire ce que j'aime, **résoudre les problèmes des utilisateurs** ! C'est le cœur de l'UX.

#### Structure du système de design

Pour créer un système de design, nous devons le décomposer et comprendre ses parties :

![Image](https://cdn-media-1.freecodecamp.org/images/FISXXSaT45PI0BAQjM37CySskxm5WT-7aZXt)
_[UX Pin — Système de design](https://www.slideshare.net/uxpin/building-a-design-system-a-practitioners-case-study" rel="noopener" target="_blank" title=")_

Un peu d'introspection est également nécessaire. Voici quelques questions à se poser lors de la création d'un système de design :

* Comment le système fonctionne-t-il aujourd'hui et dans le futur ?
* Quelle est notre vision ?
* Quels problèmes essayons-nous de résoudre ?
* Qui est le plus impacté par ce problème ?
* Quel impact voulons-nous qu'un système de design ait sur notre façon de travailler ?

Voici comment d'autres abordent ce sujet :

[**Comment nous utilisons le design basé sur les composants**](https://medium.com/@lewisplushumphreys/how-were-using-component-based-design-5f9e3176babb)  
[_Le design basé sur les composants est souvent évoqué dans le contexte de grands projets complexes. Dans cet article, nous faisons valoir quemedium.com](https://medium.com/@lewisplushumphreys/how-were-using-component-based-design-5f9e3176babb)[**Configurer un système de design**](https://blog.prototypr.io/design-system-ac88c6740f53)  
[_Construire un système qui fournit un ensemble unifié d'UX, de règles de design et de motifs._blog.prototypr.io](https://blog.prototypr.io/design-system-ac88c6740f53)

![Image](https://cdn-media-1.freecodecamp.org/images/ss415zgUFpiKE8X4Vw7gtdx04Il-BimlF0sr)

### Comment notre petite équipe peut-elle créer un système de design ?

Par où commencer lorsque vous n'avez pas assez de ressources, de temps ou de budget ?

#### 1. Ne pas partir de zéro

> _Si vous souhaitez faire une tarte aux pommes à partir de zéro, vous devez d'abord inventer l'univers._ — Carl Sagan

Notre équipe examine les systèmes de design existants pour pouvoir — comme le dit Austin Kleon :

![Image](https://cdn-media-1.freecodecamp.org/images/sYXNsuwQhjfgXgcC7KsiSB1iwFkhrKVnRTNM)
_[Voler comme un artiste — Austin Kleon](https://www.amazon.com/Steal-Like-Artist-Things-Creative/dp/0761169253" rel="noopener" target="_blank" title=")_

De nombreuses entreprises ont rendu leurs systèmes de design publics et ont même partagé des fichiers Sketch. J'ai partagé une liste ci-dessous. Ce fait, ainsi que les nombreuses autres ressources Sketch, fait de Sketch notre outil de choix.

De plus, il existe des outils qui peuvent vous aider à créer rapidement une base pour votre système de design :

[**Frames pour Sketch - Système de design Web**](http://framesforsketch.com/)  
[_Des composants soigneusement conçus et les meilleures techniques Sketch combinés en un puissant système de design Web._framesforsketch.com](http://framesforsketch.com/)[**Symboles et guides de style**](http://symbols.janlosert.com/)  
[_Le modèle le plus intelligent et votre futur point de départ pour toutes les interfaces utilisateur dans Sketch. Arrêtez de perdre votre temps ensymbols.janlosert.com](http://symbols.janlosert.com/)[**Sketch App Sources - Ressources et plugins de design gratuits - Icônes, UI Kits, Wireframes, iOS, Android**](https://www.sketchappsources.com/search_bootstrap.html)  
[_Sketch App Sources est la plus grande collection d'icônes, de kits UI, de wireframes et de ressources de design gratuites pour Sketch._www.sketchappsources.com](https://www.sketchappsources.com/search_bootstrap.html)

#### 2. Savoir avec quoi vous travaillez

Nous avons décidé qu'il était essentiel de réaliser un audit UI de tous nos sites et propriétés. Nous devrons peut-être demander quelques faveurs pour y parvenir. Mais comme il s'agit simplement de documenter ce qui existe, faire appel à l'aide d'autres personnes ne devrait pas être trop difficile. Cela prendra du temps, mais à la fin, cela en vaudra la peine. Nous pourrons concevoir de manière holistique lors de la création de nouveaux composants.

Cela peut être utile pour apprendre à mener un audit UI :

[**Le guide étape par étape pour un audit UX efficace — Blog InVision**](https://www.invisionapp.com/blog/guide-to-effective-ux-audit/)  
[_Ce guide étape par étape vous apprendra à auditer votre expérience utilisateur. Mais avant de plonger, commençons parwww.invisionapp.com](https://www.invisionapp.com/blog/guide-to-effective-ux-audit/)

#### 3. Construire au fur et à mesure

Un système de design est un document vivant. Sachant que le travail n'est jamais terminé, nous avons décidé de nous lancer et de construire au fur et à mesure. Alors que nous travaillons de manière itérative sur nos projets, nous concevrons en gardant à l'esprit les composants et aurons finalement un système de design. Heureusement, nous sommes plusieurs, ce qui nous permet d'être collaboratifs et de voler les uns des autres.

**Astuce rapide** : Construisez des symboles dans Sketch. Je sais, cela semble chronophage, mais une fois que vous verrez la puissance des symboles, vous apprécierez le vieux dicton :

> **Il faut aller lentement pour aller vite.**

#### 4. Connaître vos limites

Commencez petit.

Certains systèmes de design incluent des extraits de code. C'est l'objectif ultime, car cela augmentera l'adoption dans l'entreprise et créera une expérience utilisateur cohérente. Cependant, mon petite équipe ne peut pas faire cela. Pas encore, en tout cas.

Nous prévoyons de commencer par un fichier Sketch de composants simples. Une fois que nous aurons suffisamment avancé, nous travaillerons avec nos développeurs frontend pour créer du CSS. Permettre aux développeurs d'utiliser leur arme de choix en matière de code pourrait permettre au système de design de vivre. Et avec les bases de code qui changent à un rythme effréné, il est peut-être préférable de ne pas y toucher.

#### 5. Restez organisé

Cela semble simple, mais avec les projets qui s'accumulent et les délais qui approchent, il est tentant de faire les choses de manière rapide et sale. Restez organisé prend du temps et n'est jamais terminé, mais cela maintient tout le monde sain d'esprit et réduit l'encombrement des emails ou des fichiers qui circulent dans tous les sens. Alors que nous commençons à travailler sur de nouvelles choses en utilisant un kit UI que nous allons construire avec l'un des outils listés ci-dessus, nous devons garder une trace. Sinon, nous nous retrouverons là où nous avons commencé — des styles différents partout !

La gestion des versions des documents de design est un rêve pour tous les designers. Aucun produit n'a encore réussi à le faire à 100%. Nous allons essayer Abstract et Plant pour voir comment ils peuvent nous aider à rester sur la bonne voie. Travaillant pour une entreprise, la seule plateforme en ligne que nous pouvons utiliser pour le stockage de fichiers est One Drive. Google Drive et Dropbox sont d'autres options si vous n'êtes pas restreint.

[**Abstract**](https://sketchapphub.com/resource/abstract/)  
[_Contrôle de version et gestion de fichiers pour vos fichiers Sketch. Abstract permet aux designers de versionner et gérer de manière fiablesketchapphub.com](https://sketchapphub.com/resource/abstract/)[**Plant - application de contrôle de version et plugin Sketch pour designers**](https://plantapp.io/)  
[_Plant est une application de contrôle de version et un plugin Sketch pour designers. Synchronisez les versions de design, invitez des coéquipiers et prenez le contrôle totalplantapp.io](https://plantapp.io/)

Ce sont les premières étapes que mon équipe et moi allons essayer en commençant ce voyage. Croisons les doigts pour que nous fassions quelques progrès. J'adorerais entendre d'autres petites équipes, voire une équipe d'une seule personne, pour apprendre comment elles relèvent ce défi.

### Répertoire des systèmes de design

Comme promis, voici quelques systèmes de design pour l'inspiration ou pour voler comme un artiste :

[**miukimiu/design-systems**](https://github.com/miukimiu/design-systems)  
[_design-systems - Une liste organisée de systèmes de design. Matériels d'apprentissage et outils pour créer votre propre système de design._github.com](https://github.com/miukimiu/design-systems)[**Directives de design Atlassian | Atlassian Design**](https://atlassian.design/)  
[_Concevoir, développer et livrer. Utilisez le langage de design de bout en bout d'Atlassian pour créer des expériences simples et belles_atlassian.design](https://atlassian.design/)[**Créer un langage visuel**](https://airbnb.design/building-a-visual-language/)  
[_Dans les coulisses de notre nouveau système de design. Cet article fait partie d'une série sur notre nouveau système de langage de design. Karri_airbnb.design](https://airbnb.design/building-a-visual-language/)[**BBC GEL | Page d'accueil**](http://www.bbc.co.uk/gel/)  
[_Notre langage d'expérience global (GEL) est le cadre de design partagé de la BBC qui nous permet de créer des expériences cohérentes et_www.bbc.co.uk](http://www.bbc.co.uk/gel/)[**Système de design Carbon**](http://carbondesignsystem.com/)  
[_Carbon est le système de design pour les produits IBM Cloud. Il s'agit d'une série de styles individuels, de composants et de directives_carbondesignsystem.com](http://carbondesignsystem.com/)[**Accueil - Office UI Fabric**](https://developer.microsoft.com/en-us/fabric#/)  
[_Le framework frontal officiel pour construire des expériences qui s'intègrent parfaitement dans Office et Office 365._developer.microsoft.com](https://developer.microsoft.com/en-us/fabric#/)[**Système de design Fluent**](https://fluent.microsoft.com/)  
[_Un système de design éloquent pour un monde complexe. C'est le moment pour un design audacieux, évolutif et universel. Ceci est un_fluent.microsoft.com](https://fluent.microsoft.com/)[**Système de design Harmony**](http://harmony.intuit.com/)  
[_Harmony est un système de design vivant qui unit les produits pour petites entreprises d'Intuit, la marque et les expériences marketing à travers_harmony.intuit.com](http://harmony.intuit.com/)[**Langage de design IBM**](https://www.ibm.com/design/language/)  
[_Utilisez le langage de design IBM pour créer des produits magnifiquement conçus et des expériences utilisateur éclairantes._www.ibm.com](https://www.ibm.com/design/language/)[**Système de design Lightning**](https://www.lightningdesignsystem.com/)  
[_Le système de design Lightning fournit un balisage accessible qui servira de base à votre application_www.lightningdesignsystem.com](https://www.lightningdesignsystem.com/)[**Guides de voyage Lonely Planet et informations de voyage**](http://rizzo.lonelyplanet.com/styleguide/design-elements/colours)  
[_Documentation du guide de style Surveillance des performances À propos de Rizzo_rizzo.lonelyplanet.com](http://rizzo.lonelyplanet.com/styleguide/design-elements/colours)[**Material Design**](https://material.io/)  
[_Material Design est un système unifié qui combine la théorie, les ressources et les outils pour créer des expériences numériques._material.io](https://material.io/)[**Nachos | Trello**](https://design.trello.com/)  
[_Trello - Bibliothèque de motifs_design.trello.com](https://design.trello.com/)[**Système de design UX Pega**](https://design.pega.com/)  
[_Pega est un puissant système UX pour engager les clients et les employés. Le logiciel Pega résout des problèmes commerciaux complexes_design.pega.com](https://design.pega.com/)[**Système de design Predix**](https://www.predix-ui.com)  
[_Modifier la description_www.predix-ui.com](https://www.predix-ui.com)[**Normes de design Web des États-Unis : Un système de design pour le gouvernement fédéral**](https://standards.usa.gov/)  
[_Les normes fournissent des motifs de design basés sur la recherche pour construire des expériences numériques accessibles, réactives et cohérentes_standards.usa.gov](https://standards.usa.gov/)[**Directives de design SAP Fiori**](https://experience.sap.com/fiori-design-web/)  
[_L'interface utilisateur SAP Fiori originale pour les applications Web basées sur le framework SAPUI5. Apprenez à concevoir des expériences engageantes et_experience.sap.com](https://experience.sap.com/fiori-design-web/)[**Shopify Polaris**](https://polaris.shopify.com/)  
[_Notre guide de style est le plan pour notre système de design. Il nous aide à collaborer entre disciplines pour construire une grande_polaris.shopify.com](https://polaris.shopify.com/)[**Pattern Lab | Construire des systèmes de design atomiques**](http://patternlab.io/)  
[_Contrairement aux outils de design statiques, Pattern Lab vous permet d'échanger facilement différents contenus représentatifs dans vos composants_patternlab.io](http://patternlab.io/)

#### Bibliothèques de motifs / Guides de style

[**Qu'est-ce que Solid ? - Solid**](https://solid.buzzfeed.com/)  
[_Solid est le guide de style CSS de BuzzFeed. Influencé par des frameworks comme Basscss, Solid utilise des classes CSS atomiques et immuables pour_solid.buzzfeed.com](https://solid.buzzfeed.com/)[**Guide de style**](https://buffer.com/style-guide)  
[_Buffer rend super facile le partage de n'importe quelle page que vous lisez. Gardez votre Buffer rempli et nous les partageons automatiquement_buffer.com](https://buffer.com/style-guide)[**Duolingo : Directives de design**](https://www.duolingo.com/design/)  
[_Lorsque écrit, Duolingo est toujours un seul mot avec un 'D' majuscule. Le 'L' n'est jamais en majuscule, et le nom est_www.duolingo.com](https://www.duolingo.com/design/)[**Bibliothèque de motifs - FutureLearn**](https://www.futurelearn.com/pattern-library)  
[_Profitez de cours en ligne gratuits des meilleures universités britanniques et internationales._www.futurelearn.com](https://www.futurelearn.com/pattern-library)[**Directives de design - La façon dont les produits sont construits.**](http://designguidelines.co/)  
[_Développeur Web de quelque part_designguidelines.co](http://designguidelines.co/)[**Ressources de guide de style de site Web**](http://styleguides.io/)  
[_Une collection collaborative de ressources pour créer des guides de style Front-End et des bibliothèques de motifs_styleguides.io](http://styleguides.io/)[**Système de grille | MailChimp**](https://ux.mailchimp.com/patterns)  
[_Notre système de grille est composé de 8 colonnes flexibles avec une gouttière entre les colonnes de 30px. Nous appliquons border-box afin que_ux.mailchimp.com](https://ux.mailchimp.com/patterns)[**Guide de style**](https://www.yelp.com/styleguide)  
[_Modifier la description_www.yelp.com](https://www.yelp.com/styleguide)

Si vous avez trouvé cela utile, vous savez quoi faire maintenant. [Suivez-moi](https://medium.com/@msNaema) pour obtenir plus d'articles et de tutoriels dans votre fil d'actualité.