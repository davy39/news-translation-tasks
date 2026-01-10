---
title: 'Unity vs SceneKit : quel outil utiliser pour construire votre application
  ARKit'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-25T18:18:58.000Z'
originalURL: https://freecodecamp.org/news/unity-vs-scenekit-which-tool-you-should-use-to-build-your-arkit-app-3e93122058b1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yEpBSt5NBKYBhYGdqPv1hw.png
tags:
- name: Game Development
  slug: game-development
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: 'tech '
  slug: tech
seo_title: 'Unity vs SceneKit : quel outil utiliser pour construire votre application
  ARKit'
seo_desc: 'By Neil Mathew

  Everything I wish I knew before building my first ARKit app.


  When starting ARKit development, the first question almost everybody has is what
  tools should I be using to build my AR app? The two most commonly used tools seem
  to be Unit...'
---

Par Neil Mathew

#### Tout ce que j'aurais aimé savoir avant de construire ma première application ARKit.

![Image](https://cdn-media-1.freecodecamp.org/images/CcAQzXvdxuV7jc7CqvVMEAVbq5aVlJJHb32Q)

Lorsque vous commencez le développement avec ARKit, la première question que presque tout le monde se pose est : quels outils devrais-je utiliser pour construire mon application AR ? Les deux outils les plus couramment utilisés semblent être **Unity** et **SceneKit** — mais lequel est le meilleur ? Lequel est le plus puissant, flexible et facile à apprendre ? Lequel a le plus de support ?

J'ai dû travailler sur la plupart de ces questions moi-même, comme la plupart des développeurs qui ont lancé des applications AR jusqu'à présent. J'ai donc pensé qu'il serait utile de plonger dans les principales différences entre les deux plateformes pour vous aider à prendre une décision plus facile sur la manière d'investir votre temps.

Si vous commencez avec le développement AR, **voici quelques choses que j'aurais aimé savoir sur Unity et SceneKit avant de construire ma première application AR.** Alors, c'est parti.

### **Tout d'abord, un rapide aperçu :**

[**Unity**](http://unity3d.com) est un moteur de jeu 3D mature, qui s'est étroitement lié à la VR et à la AR en raison de son fort accent sur le contenu 3D. Le langage principal de développement est le C#. Le développement ARKit dans Unity est réalisé avec le plugin Unity ARKit qui enveloppe le SDK ARKit dans des scripts C# pour un accès facile à toutes les fonctions ARKit.

[**SceneKit**](https://developer.apple.com/scenekit/) est la version d'Apple d'un moteur de jeu 3D pour le développement natif iOS et est directement intégré à Xcode. Les langages principaux sont Swift et Objective C.

### **L'un d'eux est-il objectivement meilleur ?**

Lorsque l'on compare deux produits, la réponse la plus frustrante sur internet semble être : « ça dépend ». Alors, laissez-moi commencer par dire que, dans la plupart des cas, vous constaterez que **Unity** est la meilleure solution pour le développement AR. Il y a cependant certains cas où SceneKit l'emporte, et je vais essayer de mon mieux d'expliquer les avantages et les inconvénients de chaque outil afin que vous puissiez prendre une décision éclairée.

Examinons d'abord deux scénarios probables pour les développeurs d'applications AR en ce moment :

1. Vous construisez une application (grand public, entreprise, etc.)
2. Vous construisez un jeu ou une « expérience »

#### **Vous construisez une application**

Si vous cherchez à intégrer ARKit dans une application iOS existante, ne cherchez pas plus loin. Utilisez SceneKit. SceneKit vous permet d'intégrer facilement une vue AR dans votre application sans changer quoi que ce soit d'autre dans votre UX.

Si vous êtes un développeur iOS expert avec de l'expérience avec XCode, Swift, Cocapods, et ainsi de suite, vous devriez probablement toujours utiliser SceneKit. Vous éviterez la courbe d'apprentissage d'une nouvelle plateforme et vous pourrez assimiler le SDK ARKit assez rapidement.

Si vous construisez une nouvelle application grand public ou entreprise iOS et que vous aimez l'apparence des éléments d'interface utilisateur d'Apple (comme les boutons, les gestes et les notifications), SceneKit est, encore une fois, le meilleur choix. Étant un produit Apple, SceneKit s'intègre magnifiquement avec XCode et vous permet d'intégrer votre vue de scène 3D avec tous leurs éléments d'interface utilisateur 2D intégrés de manière assez transparente.

La règle générale ici est que si le contenu 3D n'est pas l'objectif central de votre application, et que vous vous souciez des modèles d'UX iOS, optez pour SceneKit.

![Image](https://cdn-media-1.freecodecamp.org/images/zicyuUU8h3hK8264a0YRzyod7tFIL6b1yRPZ)
_SceneKit facilite grandement l'ajout de modèles d'interface utilisateur 2D natifs iOS à votre application_

**L'avertissement** est que si vous vous souciez du développement multiplateforme rapide entre iOS et Android, ou si vous avez beaucoup de contenu 3D comme des modèles animés, des effets spéciaux et des physiques prévus pour votre application, vous devriez envisager **Unity**. Il est plus mature en tant qu'outil de développement 3D multiplateforme grâce à ses racines de moteur de jeu.

#### **Vous construisez un jeu**

Si vous construisez un jeu ou une expérience immersive, surtout avec beaucoup de contenu visuel 3D comme des animations de personnages, des cartes de jeu, des effets spéciaux et des simulations physiques, **Unity est définitivement le meilleur choix.**

Unity est rempli de tonnes de méthodes intégrées qui vous permettent de faire tout ce que vous pouvez imaginer. Si ce n'est pas intégré, c'est probablement disponible sur le Unity Asset Store. Grâce à ces facteurs, Unity vous fait gagner beaucoup de temps par rapport à SceneKit, où vous pourriez passer beaucoup de temps à construire et à déboguer des fonctionnalités de base plutôt qu'à construire votre jeu.

De plus, Unity vous permet de compiler rapidement pour un certain nombre de plateformes différentes, vous pouvez donc porter votre jeu ARKit sur Android avec seulement quelques modifications des bibliothèques de suivi AR réelles. (Cela change bientôt aussi — Unity construit un SDK XR multiplateforme qui abstrait les bibliothèques AR de bas niveau pour un port encore plus rapide). La vitesse de développement est souvent un facteur assez majeur pour les développeurs, et devoir réécrire votre application pour différentes plateformes peut être un coût assez important.

### **Critères de décision**

Si vous ne correspondez pas tout à fait aux deux scénarios ci-dessus, ou si vous n'êtes pas sûr de construire un jeu, une application, une application gamifiée ou un jeu application, voici une comparaison générale basée sur certains critères courants auxquels les développeurs AR se soucient.

#### 1. Performance

En général, une application ou un jeu construit avec SceneKit aura une taille de fichier plus petite et pourrait être plus performant dans certains cas. Lorsque vous utilisez Unity, vous apportez un moteur physique complet dans votre application. Donc, si vous n'utilisez pas de calcul 3D lourd, vous pourriez être mieux avec SceneKit.

Cependant, gardez à l'esprit que tout le code de la caméra et les autres modules AR du plugin Unity sont écrits en Objective C, ils sont donc très similaires en termes d'efficacité. Ce sont principalement les scènes 3D lourdes et les inefficacités dans la conception de votre projet qui le ralentiront. Il y a un [bon fil de discussion sur le sujet ici](https://www.reddit.com/r/ARKitCreators/comments/6p1a37/swift_vs_unity/).

**Le verdict : Unity et SceneKit sont assez égaux ici.**

#### 2. Compatibilité des formats 3D

J'ai personnellement eu un temps douloureux à importer des modèles 3D et des animations dans SceneKit. En général, lorsque vous sourcez du contenu 3D pour votre jeu ou votre application, gardez à l'esprit que SceneKit vous limitera à l'utilisation de fichiers Collada (.dae) ou Wavefront (.obj). De plus, j'ai parfois vu que certains fichiers .obj ne s'affichent pas correctement dans Scenekit.

Unity est beaucoup mieux pour gérer n'importe quel type de format 3D. Avec Unity, vous pouvez non seulement importer des fichiers .fbx (modèles 3D qui incluent des animations), mais vous pouvez également charger directement des scènes à partir d'outils de conception 3D comme Blender.

**Le verdict : +1 pour Unity ici.**

#### 3. Facilité de débogage

Unity est un IDE très visuel, avec des outils de débogage visuel impressionnants qui vous permettent de voir et d'interagir avec tout le contenu 3D de votre scène, pendant l'exécution. Bien que vous deviez exécuter votre application directement sur un appareil iOS pour tester et déboguer correctement les problèmes ARKit, vous pouvez utiliser des outils comme [Unity ARKit Remote](https://blogs.unity3d.com/2017/08/03/introducing-the-unity-arkit-remote/) pour prototyper les interactions 3D dans votre application directement dans l'éditeur Unity.

SceneKit, en revanche, ne fournit que le débogage de la console dans XCode. Bien que certains développeurs préfèrent cela, cela peut gêner le test rapide des interactions 3D dans votre application ou votre jeu.

**Le verdict : +1 pour Unity ici.**

![Image](https://cdn-media-1.freecodecamp.org/images/sBxLgTDS8VEOd75fXOaO6XryNCgSBnFUzkT4)
_Le débogueur de scène visuel impressionnant de Unity_

#### **4. Disponibilité des docs / tutoriels / exemples**

Unity dispose de ressources incroyablement vastes de documentation, de tutoriels et de code exemple pour presque tout ce que vous pouvez construire. Grâce à leur grande communauté de développeurs, il y a aussi beaucoup de tutoriels construits par des développeurs.

Bien sûr, la communauté des développeurs iOS est également assez grande. Bien qu'ARKit lui-même puisse être nouveau, la taille de la communauté a entraîné un bon nombre d'exemples, de billets de blog, de tutoriels vidéo et de cours en ligne pour faciliter votre transition vers un développeur AR.

En termes de problèmes de contenu 3D comme la géométrie 3D et les mathématiques, Unity gagne parce que la grande communauté des développeurs de jeux Unity a garanti que la plupart des questions que vous avez auront une réponse quelque part sur internet.

Si vous cherchez à commencer, voici mes tutoriels vidéo introductifs préférés pour Unity et SceneKit.

**Unity** : [Créer une animation de zombie qui marche](https://www.youtube.com/watch?v=S7kKQZuOdlk).  
**Scenekit** : [Créer et visualiser des objets 3D simples](https://www.youtube.com/watch?v=f3xFpRWZEz8).

**Le verdict : +0,5 pour Unity ici**

#### 5. Vitesse de développement

De nombreux développeurs rapportent que la courbe d'apprentissage de Unity est plus courte que celle de Scenekit. Cela est probablement dû au fait que vous pouvez apprendre le développement de contenu 3D de manière beaucoup plus facile sur Unity, avant de vous lancer dans le développement AR.

D'un point de vue technique, un jeu AR est vraiment juste un jeu 3D avec un arrière-plan de caméra. Diviser votre processus d'apprentissage de cette manière rend les choses beaucoup plus intuitives.

L'autre grand facteur ici est le développement multiplateforme. Bien que vous ne puissiez pas construire directement un projet Unity ARKit pour Android, vous pouvez au moins réutiliser le contenu 3D et les interactions que vous avez construits sur n'importe quelle plateforme. Vous n'avez besoin que de brancher un nouveau gestionnaire de caméra par appareil. Unity rend cela encore plus facile maintenant en abstraisant les fonctionnalités spécifiques au matériel comme ARKit et ARCore avec leur nouveau SDK XR.

**Le verdict : +1 pour Unity ici**

### Conclusion

En général, si vous construisez un jeu, Unity est presque toujours la meilleure solution.

Si vous construisez une application, vous devez considérer si vous valorisez le développement natif iOS et les éléments d'interface utilisateur d'Apple par rapport au développement multiplateforme. Si votre application a des interactions 3D minimales, SceneKit sera la meilleure option. Sinon, restez avec Unity.

Un autre conseil que je peux vous donner est de ne pas passer trop de temps sur cette décision. Commencez simplement avec l'un d'eux. Vous perdrez beaucoup moins de temps à essayer un outil et à changer si vous avez l'impression qu'il ne fonctionne pas assez bien. En tant que développeur AR iOS, XCode et Unity seront finalement des compétences utiles à acquérir.

Pour résumer, voici une bonne citation du [subreddit ARKitCreators](https://www.reddit.com/r/ARKitCreators/comments/6p1a37/swift_vs_unity/).

> « Une règle de base décente serait d'utiliser Swift si votre application est relativement simple, ou si l'AR et les interactions 3D ne sont pas au cœur de ce que vous essayez de construire. Et utilisez Unity pour le contraire. »

### Qui suis-je ?

Je suis le PDG et cofondateur de [Placenote](https://placenote.com), un SDK qui donne aux applications AR mobiles la capacité de verrouiller en permanence le contenu AR à tout emplacement physique dans le monde réel. Donc, si vous construisiez, par exemple, une application comme la navigation intérieure, une application de graffiti AR ou même un jeu multijoueur, vous devriez consulter le SDK Placenote.

Le SDK Placenote dispose de code exemple disponible pour les développeurs Unity et SceneKit, n'hésitez donc pas à utiliser nos applications exemples pour vous aider à prendre votre décision de plateforme !

[**Vous pouvez installer le SDK ici**](https://placenote.com/install)

### Références

J'ai compilé cet article avec l'aide de ces multiples fils de discussion Quora et Reddit.

1. [Quels sont les avantages et les inconvénients de la création d'applications de réalité augmentée en Swift vs Unity ?](https://www.quora.com/What-are-the-pros-and-cons-of-creating-augmented-reality-apps-in-Swift-vs-Unity)
2. [Swift vs Unity](https://www.reddit.com/r/ARKitCreators/comments/6p1a37/swift_vs_unity/)
3. [Je veux créer des applications AR, devrais-je apprendre ARKit en premier ou Unity ?](https://www.quora.com/I-want-to-make-AR-apps-should-I-learn-ARKit-first-or-Unity)
4. [Est-il plus facile d'utiliser iOS SceneKit ou le moteur de jeu Unity pour développer un projet iOS 11 ARKit ?](https://www.quora.com/Is-it-easier-to-use-iOS-SceneKit-or-the-Unity-game-engine-to-develop-for-an-iOS-11-ARKit-project)