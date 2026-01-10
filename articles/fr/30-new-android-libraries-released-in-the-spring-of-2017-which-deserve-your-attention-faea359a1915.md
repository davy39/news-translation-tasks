---
title: 30 nouvelles bibliothèques Android publiées au printemps 2017 qui méritent
  votre attention
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-15T07:59:55.000Z'
originalURL: https://freecodecamp.org/news/30-new-android-libraries-released-in-the-spring-of-2017-which-deserve-your-attention-faea359a1915
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3FVOI0HJNamEVvcnmRPqSg.jpeg
tags:
- name: Android
  slug: android
- name: android app development
  slug: android-app-development
- name: mobile
  slug: mobile
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
seo_title: 30 nouvelles bibliothèques Android publiées au printemps 2017 qui méritent
  votre attention
seo_desc: 'By Michal Bialas

  These are my 30 favorite new Android libraries that have come out since March 2017.
  Some of them aren’t production ready yet, but you may have lots of fun using them.
  I hope you enjoy these.

  Here they are in no particular order:

  1. M...'
---

Par Michal Bialas

Voici mes 30 nouvelles bibliothèques Android préférées qui sont sorties depuis mars 2017. Certaines ne sont pas encore prêtes pour la production, mais vous pouvez vous amuser à les utiliser. J'espère que vous les apprécierez.

Les voici dans un ordre quelconque :

#### 1. [Matisse](https://github.com/zhihu/Matisse)

Ceci est un beau sélecteur d'images et de vidéos locales. Fonctionnalités principales :

* Sélection d'images incluant JPEG, PNG, GIF et de vidéos incluant MPEG, MP4,
* application de thèmes personnalisés, incluant deux thèmes intégrés,
* différents chargeurs d'images,
* définition de règles de filtre personnalisées,
* entièrement opérationnel dans les `Activities` et les `Fragments`.

Vous pouvez trouver plus d'informations dans le [wiki](https://github.com/zhihu/Matisse/wiki) de la bibliothèque.

![Image](https://cdn-media-1.freecodecamp.org/images/ni50xwZ60UVTlaJQk8pRVXbOCj8fDWOHqeZc)

[**zhihu/Matisse**](https://github.com/zhihu/Matisse)  
[_Matisse - :fireworks: Un sélecteur local d'images et de vidéos bien conçu pour Android_github.com](https://github.com/zhihu/Matisse)

#### 2. [Spruce Android Animation Library](https://github.com/willowtreeapps/spruce-android)

> Spruce est une bibliothèque d'animation légère qui aide à chorégraphier les animations à l'écran. Avec tant de bibliothèques d'animation différentes disponibles, les développeurs doivent s'assurer que chaque vue s'anime au moment approprié. Spruce peut aider les designers à demander des animations multi-vues complexes et éviter que les développeurs ne grimacent devant le prototype.

![Image](https://cdn-media-1.freecodecamp.org/images/UH94wMckAcV6xRGxb5uQqjynEqnISY85GdQ-)

[**willowtreeapps/spruce-android**](https://github.com/willowtreeapps/spruce-android)  
[_spruce-android - Bibliothèque d'animation Spruce_github.com](https://github.com/willowtreeapps/spruce-android)

#### 3. [MaterialChipsInput](https://github.com/pchmn/MaterialChipsInput)

Les puces ont été présentées dans Material Design. Elles

> représentent des entités complexes dans de petits blocs, comme un contact. Une puce peut contenir des entités telles qu'une photo, du texte, des règles, une icône ou un contact.

MaterialChipsInput est une implémentation de ce composant pour Android. La bibliothèque fournit deux vues : `[ChipsInput](https://github.com/pchmn/MaterialChipsInput#chipsinput)` et `[ChipView](https://github.com/pchmn/MaterialChipsInput#chipview)`.

![Image](https://cdn-media-1.freecodecamp.org/images/fvCP1LVsakgC1JrQAlle9Qe2jSs7JwmlC7uo)

[**pchmn/MaterialChipsInput**](https://github.com/pchmn/MaterialChipsInput)  
[_MaterialChipsInput - Implémentation du composant Material Design Chips pour Android_github.com](https://github.com/pchmn/MaterialChipsInput)

#### 4. [Grav](https://github.com/glomadrian/Grav)

Cette bibliothèque permet de créer plusieurs animations basées sur des points. Jetez un coup d'œil — à quel point les animations peuvent être fluides et belles, et faciles à réaliser. Le _README_ contient de nombreux exemples, alors n'hésitez pas à le consulter [ici](https://github.com/glomadrian/Grav).

![Image](https://cdn-media-1.freecodecamp.org/images/gpzT8Pxec-lhFp7NiDRwJDscYlpnmWrVniiR)

[**glomadrian/Grav**](https://github.com/glomadrian/Grav)  
[_Grav - Animations configurables basées sur des points_github.com](https://github.com/glomadrian/Grav)

#### 5. [Litho](https://github.com/facebook/litho)

Litho n'est pas une bibliothèque, c'est un framework. Un framework vraiment puissant pour construire des interfaces utilisateur de manière déclarative. Il a été développé par les développeurs de Facebook, donc même si vous ne voulez pas l'essayer, il est intéressant d'observer et de suivre le processus de développement.

![Image](https://cdn-media-1.freecodecamp.org/images/CR76WikP2ljbT2HdEzRzc5fjFJmke7lJMgkx)

Fonctionnalités principales :

* utilisation d'une API déclarative pour définir les composants UI. Vous décrivez simplement la mise en page de votre UI basée sur un ensemble d'entrées immuables et le framework s'occupe du reste.
* Mise en page asynchrone : Litho peut mesurer et mettre en page votre UI à l'avance sans bloquer le thread UI.
* Aplatissement des vues : Litho utilise [Yoga](https://facebook.github.io/yoga/) pour la mise en page et réduit automatiquement le nombre de ViewGroups que votre UI contient.
* Recyclage fin : Tout composant tel qu'un texte ou une image peut être recyclé et réutilisé n'importe où dans l'UI.

[**facebook/litho**](https://github.com/facebook/litho)  
[_litho - Un framework déclaratif pour construire des UIs efficaces sur Android._github.com](https://github.com/facebook/litho)

#### 6. [Adaptable Bottom Navigation](https://github.com/bufferapp/AdaptableBottomNavigation)

Il y a quelque temps, Google a mis à jour les directives Material Design et a introduit les barres de navigation inférieures, comme l'un des plusieurs bons modèles UI à suivre dans nos applications. Ils ont également ajouté l'implémentation à la Design Support Library.

![Image](https://cdn-media-1.freecodecamp.org/images/tENkpPkox92Iy4iGb337CDxmmPT6npgO5Su8)

Adaptable Bottom Navigation peut facilement remplacer `BottomNavigationView` de la Support Library. Il est implémenté de la manière dont `ViewPager` et `TabLayout` fonctionnent. Voici une brève explication de l'équipe Buffer :

> Comme mentionné, lors de l'utilisation de la Bottom Navigation View de la Android Support Library, il peut y avoir beaucoup de code boilerplate pour le changement de vues. Pour cette raison, nous nous sommes inspirés de la méthode setupWithViewPager() de TabLayout et avons créé un composant ViewSwapper personnalisé qui peut être attaché à une Bottom Navigation View pour simplifier la gestion de l'affichage des vues.

Vous pouvez lire plus d'informations sur Github. Il y a une documentation assez complète et une explication de pourquoi il a été implémenté (astuce : architecture propre ?).

![Image](https://cdn-media-1.freecodecamp.org/images/HDa5h126k8IpjDe-NenW5Mq2YzDzJpcf2Sys)

[**bufferapp/AdaptableBottomNavigation**](https://github.com/bufferapp/AdaptableBottomNavigation)  
[_AdaptableBottomNavigation - Une manière plus simple d'implémenter la Bottom Navigation View sur Android_github.com](https://github.com/bufferapp/AdaptableBottomNavigation)

#### 7. [PatternLockView](https://github.com/aritraroy/PatternLockView)

> Cette bibliothèque vous permet d'implémenter un mécanisme de verrouillage par motif dans votre application facilement et rapidement. Elle est très facile à utiliser et il existe de nombreuses options de personnalisation disponibles pour changer la fonctionnalité et l'apparence de cette vue selon vos besoins.

> Elle supporte également les liaisons de vue RxJava 2, donc si vous êtes un fan de la programmation réactive (comme moi), vous pouvez obtenir un flux de mises à jour lorsque l'utilisateur dessine le motif.

Le _README_ est rempli d'exemples, donc il est facile de commencer avec la bibliothèque.

![Image](https://cdn-media-1.freecodecamp.org/images/TS6ugjUE2TYX2-SnU1VbUUj7eMHCd84k6jXT)

[**aritraroy/PatternLockView**](https://github.com/aritraroy/PatternLockView)  
[_PatternLockView - Une vue de verrouillage par motif facile à utiliser, personnalisable et prête pour Material Design pour Android_github.com](https://github.com/aritraroy/PatternLockView)

#### 8. [Isometric](https://github.com/FabianTerhorst/Isometric)

Ceci est une bibliothèque qui aide à dessiner des formes isométriques. À mon avis, c'est l'une des bibliothèques les plus cool de cette liste, car elle me rappelle le jeu [Monument Valley](https://play.google.com/store/apps/details?id=com.ustwo.monumentvalley).   
La bibliothèque supporte le dessin de plusieurs formes, chemins et structures complexes, comme l'exemple ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/mQBcVMshzkWi8BZ2BDFGgkufgIQJ9hJcFCc-)

[**FabianTerhorst/Isometric**](https://github.com/FabianTerhorst/Isometric)  
[_Isometric - Bibliothèque de dessin isométrique pour Android_github.com](https://github.com/FabianTerhorst/Isometric)

#### 9. [UltraViewPager](https://github.com/alibaba/UltraViewPager)

Nous pouvons traiter cette bibliothèque comme une extension de `ViewPager` qui encapsule de nombreuses fonctionnalités, principalement pour fournir une solution unifiée pour les scénarios de commutation multi-pages.

![Image](https://cdn-media-1.freecodecamp.org/images/rlsdAfFLjlFRg3Ay3RZTQVKSNfZwleb9wev9)

#### UltraViewPager supporte :

* le défilement horizontal et vertical,
* plusieurs vues dans un seul `ViewPager`
* la commutation circulaire des vues. Par exemple, s'il y a 3 vues à afficher dans un `ViewPager`, il doit revenir à la première vue après la troisième vue,
* la fonction de défilement automatique (implémentée avec un timer utilisant `Handler`),
* la définition de la hauteur maximale et de la largeur maximale,
* la définition du rapport d'aspect,
* l'indication de la vue actuelle (cercle et icône),
* deux types d'animations de transition de page intégrées.

Cette bibliothèque dispose également d'une bonne documentation.

[**alibaba/UltraViewPager**](https://github.com/alibaba/UltraViewPager)  
[_UltraViewPager est une extension pour ViewPager pour fournir plusieurs fonctionnalités dans un seul ViewPager._github.com](https://github.com/alibaba/UltraViewPager)

#### 10. [InfiniteCards](https://github.com/BakerJQ/Android-InfiniteCards)

Cette bibliothèque aide à implémenter des cartes UI et à les basculer avec une belle animation.

![Image](https://cdn-media-1.freecodecamp.org/images/qf004N6LxtH3yh9mqx3oVPp-3FKHR8mSLQ2Z)

[**BakerJQ/Android-InfiniteCards**](https://github.com/BakerJQ/Android-InfiniteCards)  
[_Android-InfiniteCards - Une UI de basculement de cartes infinie pour Android, supporte l'animation personnalisée    
	 
	 _github.com](https://github.com/BakerJQ/Android-InfiniteCards)

#### 11. [SlidingRootNav](https://github.com/yarolegovich/SlidingRootNav)

Ceci est une bibliothèque que nous pouvons considérer comme un `ViewGroup` de type DrawerLayout, où un _tiroir_ est caché sous la vue de contenu, puis peut être déplacé pour rendre le tiroir visible. Le _REAMDE_ est assez complet et il est intéressant de le vérifier.

![Image](https://cdn-media-1.freecodecamp.org/images/P1ktU0jkAxeP50TWlXPN6rP1ciPgmctzzlY1)

[**yarolegovich/SlidingRootNav**](https://github.com/yarolegovich/SlidingRootNav)  
[_SlidingRootNav - ViewGroup de type DrawerLayout, où un "tiroir" est caché sous la vue de contenu, qui peut être déplacé…_github.com](https://github.com/yarolegovich/SlidingRootNav)

#### 12. [PasscodeView](https://github.com/hanks-zyh/PasscodeView)

C'est juste une vue où vous pouvez taper votre mot de passe. Mais une vue élégante !

![Image](https://cdn-media-1.freecodecamp.org/images/112Xi-H54JTn0CT0pX9xMxkQoBjaxNTmZJFz)

[**hanks-zyh/PasscodeView**](https://github.com/hanks-zyh/PasscodeView)  
[_PasscodeView Material Design pour Android._github.com](https://github.com/hanks-zyh/PasscodeView)

#### 13. [MusicWave](https://github.com/akshay2211/MusicWave)

Cette bibliothèque permet de représenter le son sous forme de visualisation colorée en dégradé.

![Image](https://cdn-media-1.freecodecamp.org/images/k1uWkgRebqX8P9DfnJ5kIElYGo9ApdACz-OJ)

[**akshay2211/MusicWave**](https://github.com/akshay2211/MusicWave)  
[_Avec MusicWave, représentez votre son dans une visualisation colorée en dégradé_github.com](https://github.com/akshay2211/MusicWave)

#### 14. [ShadowImageView](https://github.com/yingLanNull/ShadowImageView)

Cette bibliothèque vous aide à ajouter une ombre plus significative à vos images. Selon le _README_, elle offre

> Un effet d'ombre plus exquis, utilisé dans certaines scènes spéciales pour améliorer l'expérience utilisateur.

De plus, elle est facile à utiliser.

![Image](https://cdn-media-1.freecodecamp.org/images/rzesrzTTaaElLzSUkcCXSmBDn6xQMBb2-kU8)

[**yingLanNull/ShadowImageView**](https://github.com/yingLanNull/ShadowImageView)  
[_ShadowImageView - Peut changer de couleur en fonction de l'image, effet d'ombre plus délicat_github.com](https://github.com/yingLanNull/ShadowImageView)

#### 15. [PolygonDrawingUtil](https://github.com/stkent/PolygonDrawingUtil)

Ceci est une classe utilitaire Android efficace pour dessiner des polygones réguliers sur un `[Canvas](https://developer.android.com/reference/android/graphics/Canvas.html)`. Nous pouvons spécifier :

* Nombre de côtés (≥ 3),
* coordonnées du centre,
* rayon extérieur (centre vers sommet),
* rayon d'arrondi des coins,
* rotation du polygone,
* remplissage/contour `[Paint](https://developer.android.com/reference/android/graphics/Paint.html)`.

![Image](https://cdn-media-1.freecodecamp.org/images/IdE0e7sFdBZrWEomG0-m89m1m5S0j0vZIeOM)

[**stkent/PolygonDrawingUtil**](https://github.com/stkent/PolygonDrawingUtil)  
[_PolygonDrawingUtil - Une classe utilitaire Android efficace pour dessiner des polygones réguliers sur un Canvas._github.com](https://github.com/stkent/PolygonDrawingUtil)

#### 16. [Tiny](https://github.com/Sunzxyong/Tiny)

Ceci est le deuxième framework de cette liste. Il est responsable de la compression d'images et il est assez puissant. De plus, il

> utilise un pool de threads asynchrones pour compresser les images, et fournira le résultat dans le thread principal lorsque la compression sera terminée.

![Image](https://cdn-media-1.freecodecamp.org/images/rQWpjDOIrni6rWcqiOBTpfcCErFqAvz6jgqe)
_Effets de compression_

[**Sunzxyong/Tiny**](https://github.com/Sunzxyong/Tiny)  
[_Tiny - un framework de compression d'images._github.com](https://github.com/Sunzxyong/Tiny)

#### 17. [ParticleTextView](https://github.com/Yasic/ParticleTextView)

Cette bibliothèque fournit un widget `TextView` personnalisé, qui peut créer du texte à partir de particules en utilisant une variété d'effets d'animation et de propriétés de configuration.

![Image](https://cdn-media-1.freecodecamp.org/images/QuS4sGJOj7DsX7ZJeEQwoUaElMzxRaaDG58f)

[**Yasic/ParticleTextView**](https://github.com/Yasic/ParticleTextView)  
[_ParticleTextView - Une vue Android personnalisée pour afficher du texte avec des particules_github.com](https://github.com/Yasic/ParticleTextView)

#### 18. [CropIwa](https://github.com/steelkiwi/cropiwa)

Ceci est un widget hautement configurable pour le recadrage d'images. La bibliothèque a une architecture modulaire, ce qui la rend hautement configurable. Pour des informations sur la configuration de `CropIwaView`, consultez le [wiki sur Github](https://github.com/steelkiwi/cropiwa).

![Image](https://cdn-media-1.freecodecamp.org/images/3Cd1tyJI9eARL8FzcMbervLTvID-oOTsZ91J)

[**steelkiwi/cropiwa**](https://github.com/steelkiwi/cropiwa)  
[_cropiwa - Widget de recadrage personnalisable pour Android_github.com](https://github.com/steelkiwi/cropiwa)

#### 19. [Project Condom](https://github.com/oasisfeng/condom)

> Ceci est une bibliothèque légère pour envelopper le `Context` nu dans votre projet Android avant de le passer au SDK tiers. **Il est conçu pour empêcher le SDK tiers des comportements indésirables courants qui peuvent nuire à l'expérience utilisateur de votre application.**

Et voici l'explication :

> Lancement massif de processus dans d'autres applications (courant dans les SDK tiers de push), provoquant un démarrage lent de l'application et un lag notable sur les appareils de milieu à bas de gamme. Ce comportement a des effets de **réaction en chaîne** parmi les applications avec des SDK similaires, aggravant considérablement les performances globales de l'appareil.

[**oasisfeng/condom**](https://github.com/oasisfeng/condom)  
[_condom - Un outil ultra-léger pour Android, empêchant les comportements nuisibles courants des SDK tiers, sans affecter les fonctionnalités de l'application. (Par exemple, l'impact sévère sur l'expérience utilisateur causé par le "lancement en chaîne")_github.com](https://github.com/oasisfeng/condom)

#### 20. [AppMethodOrder](https://github.com/zjw-swun/AppMethodOrder)

Cette bibliothèque vous permet de tracer l'ordre de tous les appels de fonctions. Le projet est bien documenté et vous pouvez trouver des manuels détaillés sur son utilisation. La seule contrainte est qu'il est écrit en chinois, mais vous pouvez toujours cliquer sur _Traduire en anglais_ dans votre navigateur et profiter de ce projet.

![Image](https://cdn-media-1.freecodecamp.org/images/FSRfrmdYRKVVbaER0x1q6DkV8nukf93A5qzt)

[**zjw-swun/AppMethodOrder**](https://github.com/zjw-swun/AppMethodOrder)  
[_AppMethodOrder - Une bibliothèque Android qui vous permet de comprendre l'ordre d'appel de toutes les fonctions ainsi que le temps d'exécution des fonctions (sans besoin de code invasif)_github.com](https://github.com/zjw-swun/AppMethodOrder)

#### 21. [Android DebugKit](https://github.com/hulab/debugkit)

Ceci est une bibliothèque intéressante. Elle vous permet de créer et d'utiliser un outil de débogage spécial en survol, pour déclencher des actions définies par vous dans une application. Ces actions peuvent évidemment être déclenchées en temps réel, donc cela peut être utilisé par exemple lors de la rédaction de commentaires ou du test d'un écran de téléphone.   
La bibliothèque utilise le modèle Builder. Elle est facile à utiliser et dans le _README_, il y a un exemple d'utilisation.

![Image](https://cdn-media-1.freecodecamp.org/images/B8Uyd4kyiE6oTb7ESiCiut5XWAma6qGGoIfQ)

[**hulab/debugkit**](https://github.com/hulab/debugkit)  
[_debugkit - Vous avez déjà caché des fonctions de débogage dans votre UI ? Voici maintenant une manière propre de le faire !_github.com](https://github.com/hulab/debugkit)

#### 22. [Aesthetic](https://github.com/afollestad/aesthetic)

Ceci est une nouvelle bibliothèque et toujours en bêta, mais elle fait quelque chose de vraiment cool — elle change votre thème dynamiquement avec le support de Rx ! Selon l'auteur, ceci est

> Un moteur de thème dynamique plug-and-play rapide et facile à utiliser. Alimenté par Rx, pour les applications Android.

La documentation est vraiment bonne, complète et définitivement intéressante à consulter.

![Image](https://cdn-media-1.freecodecamp.org/images/jMkyTOTumqfu3-T3fdXd4aUPgfoIdpRgsUgb)

[**afollestad/aesthetic**](https://github.com/afollestad/aesthetic)  
[_aesthetic - [BÊTA] Un moteur de thème dynamique plug-and-play rapide et facile à utiliser. Alimenté par Rx, pour les applications Android._github.com](https://github.com/afollestad/aesthetic)

#### 23. [EasyCalendar](https://github.com/shichaohui/EasyCalendar)

Ceci est un widget de calendrier personnalisé facile. Les fonctionnalités principales incluent :

* Mise en page personnalisée pour le titre,
* mise en page personnalisée pour la date,
* afficher ou masquer le diviseur pour la date,
* afficher ou masquer la date de débordement,
* écouter les clics sur la vue de la date.

La documentation est complète et la bibliothèque est facile à utiliser.

![Image](https://cdn-media-1.freecodecamp.org/images/F6sUbImwhuiaS9SjYwCOZJEfIajbpnWQBacd)

[**shichaohui/EasyCalendar**](https://github.com/shichaohui/EasyCalendar)  
[_Personnalisez rapidement l'UI du calendrier. Vous pouvez utiliser EasyCalendar pour obtenir rapidement le style d'UI de calendrier._github.com](https://github.com/shichaohui/EasyCalendar)

#### 24. [SimpleRatingBar](https://github.com/ome450901/SimpleRatingBar)

Cette bibliothèque fournit deux barres d'évaluation :

* BaseRatingBar — sans aucune animation,
* ScaleRatingBar — avec une animation progressive et à l'échelle.

Vous pouvez les voir dans un gif ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/WWeFLh9TYLKPrtl4I2CZGUZKB2OFWYlYJaxz)

[**ome450901/SimpleRatingBar**](https://github.com/ome450901/SimpleRatingBar)  
[_SimpleRatingBar - Une simple RatingBar avec animation à l'échelle_github.com](https://github.com/ome450901/SimpleRatingBar)

#### 25. [Magellan](https://github.com/wealthfront/magellan)

Cette bibliothèque est présentée comme la bibliothèque de navigation la plus simple pour Android, mais vous devez vérifier si elle vaut la peine d'être utilisée.   
Fonctionnalités principales :

* La navigation est aussi simple que d'appeler la méthode `goTo(screen)`,
* vous obtenez un contrôle total de la pile de retour,
* les transitions sont gérées automatiquement pour vous.

Elle dispose d'un [wiki](https://github.com/wealthfront/magellan/wiki) complet avec toutes les explications nécessaires.

![Image](https://cdn-media-1.freecodecamp.org/images/21mRvA9y-gXY4O76H-7a8DAsaI39ihbUtWS-)

[**wealthfront/magellan**](https://github.com/wealthfront/magellan)  
[_magellan - La bibliothèque de navigation la plus simple pour Android._github.com](https://github.com/wealthfront/magellan)

#### 26. [ViewPagerAnimator](https://github.com/StylingAndroid/ViewPagerAnimator)

> _ViewPagerAnimator_ est une nouvelle bibliothèque légère, mais puissante d'animation _ViewPager_ pour Android. Elle est conçue pour animer des valeurs arbitraires lorsque l'utilisateur navigue entre les pages dans un _ViewPager_, et suivra précisément le mouvement de [son|sa] doigt. Bien que la bibliothèque elle-même puisse être utile pour certains, le but principal de la publication de cette bibliothèque est de démontrer certaines subtilités de l'API qui se révèlent vraiment lorsque l'on utilise les extensions Java 8 qui arrivent bientôt. Des projets d'exemple pour Java 7 et Java 8 sont fournis.

Elle est écrite par [Mark Allison](https://www.freecodecamp.org/news/30-new-android-libraries-released-in-the-spring-of-2017-which-deserve-your-attention-faea359a1915/undefined) et vous pouvez obtenir plus d'informations sur son [blog Styling Android](https://blog.stylingandroid.com/viewpageranimator-the-basics/).

![Image](https://cdn-media-1.freecodecamp.org/images/VOqxhWKnlb58MyXANonLzBsqWzhvgEbk49ft)

[**StylingAndroid/ViewPagerAnimator**](https://github.com/StylingAndroid/ViewPagerAnimator)  
[_ViewPagerAnimator - Une bibliothèque légère, mais puissante d'animation ViewPager pour Android_github.com](https://github.com/StylingAndroid/ViewPagerAnimator)

#### [27. BlockCanaryEx](https://github.com/seiginonakama/BlockCanaryEx)

Ceci est une bibliothèque qui facilite la recherche de méthodes lourdes dans votre code lorsque votre application est bloquée. Elle est basée sur [BlockCanary](https://github.com/markzhai/AndroidPerformanceMonitor).

![Image](https://cdn-media-1.freecodecamp.org/images/8Lg3xDWhCg79Oxy0HoUycN4qBUGoOJKDNMyZ)

[**seiginonakama/BlockCanaryEx**](https://github.com/seiginonakama/BlockCanaryEx)  
[_BlockCanaryEx — facilite la détection des goulots d'étranglement de performance lorsque l'application est bloquée_github.com](https://github.com/seiginonakama/BlockCanaryEx)

#### 28. [PaletteImageView](https://github.com/DingMouRen/PaletteImageView)

Ceci est une bibliothèque assez cool. Elle ajoute des ombres à vos images, mais la couleur de l'ombre est la couleur dominante de l'image.

![Image](https://cdn-media-1.freecodecamp.org/images/ZY0DtFr5va0OIsdFqk3RHRSHkRAJio4fqv7r)

La documentation est assez pauvre, mais je pense que le code est auto-explicatif.

[**DingMouRen/PaletteImageView**](https://github.com/DingMouRen/PaletteImageView)  
[_PaletteImageView - Ajoute une ombre à l'image, la couleur de l'ombre provient de la couleur principale de l'image_github.com](https://github.com/DingMouRen/PaletteImageView)

#### 29. [RecyclerRefreshLayout](https://github.com/dinuscxj/ShootRefreshView)

Ceci est une animation de rafraîchissement qui ouvre un obturateur d'appareil photo. À mon avis, cela vaut vraiment la peine de vérifier, surtout dans le _README_ où il y a une analyse mathématique sur la façon d'atteindre cet effet !

![Image](https://cdn-media-1.freecodecamp.org/images/Hu6XrZx2yOS2mG-7WiPgf-Ke5OBTIPLJlxk6)

[**dinuscxj/ShootRefreshView**](https://github.com/dinuscxj/ShootRefreshView)  
[_ShootRefreshView - C'est une animation de rafraîchissement qui ouvre l'obturateur_github.com](https://github.com/dinuscxj/ShootRefreshView)

#### 30. [SlimAdapter](https://github.com/MEiDIK/SlimAdapter)

Ceci est une approche pour écrire un Adaptateur sans `ViewHolder`. Les fonctionnalités clés incluent :

* Pas de `ViewHolders`,
* pas de réflexion,
* API fluide et simple,
* adaptateur multi-type,
* support Kotlin,
* support simple de `DiffUtil`.

![Image](https://cdn-media-1.freecodecamp.org/images/KCQNa4FyZI9JJ7zqwnxWRmizyhC3wQeYfALE)

[**MEiDIK/SlimAdapter**](https://github.com/MEiDIK/SlimAdapter)  
[_SlimAdapter - Un Adaptateur mince, propre et typable sans VIEWHOLDER_github.com](https://github.com/MEiDIK/SlimAdapter)

C'est tout. J'espère que vous avez apprécié l'article ! Si je n'ai pas mentionné d'autres grandes bibliothèques publiées ce printemps, faites-le moi savoir dans les commentaires ci-dessous. Continuons à agrandir cette liste ensemble !

Si vous aimez mon article, n'oubliez pas de cliquer sur ??? pour le recommander aux autres ???.

Aussi, pour être informé de mes nouveaux articles et histoires, suivez-moi sur [Medium](https://medium.com/@mmbialas) et [Twitter](https://twitter.com/mmbialas). Vous pouvez également me trouver sur [LinkedIn](https://www.linkedin.com/in/mmbialas). Santé !