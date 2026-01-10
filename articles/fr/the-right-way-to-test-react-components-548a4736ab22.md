---
title: La bonne façon de tester les composants React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-04T22:41:36.000Z'
originalURL: https://freecodecamp.org/news/the-right-way-to-test-react-components-548a4736ab22
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Ef724ZqepSMHk8AhRCCM7A.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Software Testing
  slug: software-testing
- name: Testing
  slug: testing
- name: Web Development
  slug: web-development
seo_title: La bonne façon de tester les composants React
seo_desc: 'By Lily Scott

  There’s a lot of confusion right now about the “right” way to test your React components.
  Should you write all your tests by hand, or only use snapshots, or some of both?
  Should you test props? State? Styles/Layout?

  I don’t think there’...'
---

Par Lily Scott

Il y a beaucoup de confusion en ce moment sur la « bonne » façon de tester vos composants React. Doit-on écrire tous vos tests à la main, ou n'utiliser que des snapshots, ou un mélange des deux ? Doit-on tester les props ? L'état ? Les styles/disposition ?

Je ne pense pas qu'il y ait une seule « bonne » façon, mais j'ai trouvé quelques modèles et conseils qui fonctionnent vraiment bien pour moi et que je souhaite partager.

**_Mise à jour février 2019_** : Cet article décrit une méthode pour tester les composants React. Avec le temps, j'ai constaté que je tire plus de valeur des tests d'intégration que des tests unitaires, donc **je n'applique plus personnellement cette méthode**.

_Si vous souhaitez écrire des tests d'intégration pour votre application React, **je vous recommande vivement [Cypress](https://www.cypress.io/), que j'utilise maintenant**._

_Cependant, vous pourriez toujours trouver cet article utile - réfléchir à la méthode décrite dans cet article vous aidera à écrire des composants avec des contrats plus clairs qui sont plus réutilisables._

### Contexte : L'application que nous allons tester

Supposons que vous souhaitez tester un composant `LockScreen`, qui se comporte comme un écran de verrouillage de téléphone. Il :

* Affiche l'heure actuelle
* Peut afficher un message défini par l'utilisateur
* Peut afficher une image de fond définie par l'utilisateur
* Dispose d'un widget glisser-pour-déverrouiller en bas

Il ressemble à quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*z_dRikEoV22y7d87sBU_Ww.gif)

Vous pouvez l'essayer [ici](https://suchipi.github.io/react-testing-example-lockscreen), et consulter le code [sur GitHub](https://github.com/suchipi/react-testing-example-lockscreen).

Voici le code pour le composant `App` de niveau supérieur :

Comme vous pouvez le voir, `LockScreen` reçoit trois props : `wallpaperPath`, `userInfoMessage`, et `onUnlocked`.

Voici le code pour `LockScreen` :

`LockScreen` intègre quelques autres composants, mais puisque nous testons uniquement `LockScreen`, concentrons-nous sur celui-ci pour l'instant.

### Contrats de composants

Pour tester `LockScreen`, vous devez d'abord comprendre ce que son **Contrat** est. Comprendre le contrat d'un composant est la partie la plus importante du test d'un composant React. Un contrat définit le comportement attendu de votre composant et quelles hypothèses sont raisonnables à avoir sur son utilisation. Sans un contrat clair, votre composant peut être difficile à comprendre. L'écriture de tests est un excellent moyen de définir formellement le contrat de votre composant.

Chaque composant React a au moins une chose qui contribue à la définition de son contrat :

* **Ce qu'il rend** (ce qui peut être rien)

De plus, la plupart des contrats de composants sont affectés par ces choses également :

* Les **props que le composant reçoit**
* L'**état que le composant détient** (le cas échéant)
* Ce que le composant fait lorsque l'**utilisateur interagit avec lui** (via clics, glissements, entrées clavier, etc.)

Certaines choses moins courantes qui affectent les contrats de composants sont :

* Le **contexte dans lequel le composant est rendu**
* Ce que le composant fait lorsque vous appelez **des méthodes sur son instance** (interface de référence publique)
* Les **effets secondaires** qui se produisent dans le cadre du cycle de vie du composant (componentDidMount, componentWillUnmount, etc.)

Pour trouver le contrat de votre composant, posez-vous des questions comme :

* Que rend mon composant ?
* Mon composant rend-il différentes choses dans différentes circonstances ?
* Lorsque je passe une fonction en tant que prop, à quoi mon composant l'utilise-t-il ? L'appelle-t-il, ou la donne-t-il simplement à un autre composant ? Si elle l'appelle, avec quoi l'appelle-t-il ?
* Lorsque l'utilisateur interagit avec mon composant, que se passe-t-il ?

### Trouver le contrat de LockScreen

Parcourons la méthode `render` de `LockScreen` et ajoutons des commentaires aux endroits où son comportement peut différer. Vous rechercherez des ternaires, des instructions if et des instructions switch comme indices. Cela nous aidera à trouver des variations dans son contrat.

Nous avons appris trois contraintes qui décrivent le contrat de `LockScreen` :

* Si une prop `wallpaperPath` est passée, le `div` d'enveloppement le plus externe que le composant rend doit avoir une propriété CSS `background-image` dans ses styles en ligne, définie sur la valeur de `wallpaperPath`, enveloppée dans `url(...)`.
* Si une prop `userInfoMessage` est passée, elle doit être passée en tant qu'enfants à un `TopOverlay`, qui doit être rendu avec un ensemble particulier de styles en ligne.
* Si une prop `userInfoMessage` n'est **pas** passée, **aucun** `TopOverlay` ne doit être rendu.

Vous pouvez également trouver certaines contraintes du contrat qui sont toujours vraies :

* Un `div` est toujours rendu, qui contient tout le reste. Il a un ensemble particulier de styles en ligne.
* Un `ClockDisplay` est toujours rendu. Il ne reçoit aucune prop.
* Un `SlideToUnlock` est toujours rendu. Il reçoit la valeur de la prop `onUnlocked` passée en tant que sa prop `onSlide`, indépendamment du fait qu'elle soit définie ou non.

Les `propTypes` du composant sont également un bon endroit pour chercher des indices sur son contrat. Voici quelques autres contraintes que je remarque :

* `wallpaperPath` est censé être une chaîne de caractères et est facultatif.
* `userInfoMessage` est censé être une chaîne de caractères et est facultatif.
* `onUnlocked` est censé être une fonction et est facultatif.

C'est un bon point de départ pour notre contrat de composant. Il peut y avoir plus de contraintes dans ce contrat de composant, et dans le code de production, vous voudrez en trouver autant que possible, mais pour les besoins de cet exemple, travaillons simplement avec celles-ci. Vous pouvez toujours ajouter des tests plus tard si vous découvrez des contraintes supplémentaires.

### Qu'est-ce qui vaut la peine d'être testé ?

Examinons le contrat que nous avons trouvé :

* `wallpaperPath` est censé être une chaîne de caractères et est facultatif.
* `userInfoMessage` est censé être une chaîne de caractères et est facultatif.
* `onUnlocked` est censé être une fonction et est facultatif.
* Un `div` est toujours rendu, qui contient tout le reste. Il a un ensemble particulier de styles en ligne.
* Un `ClockDisplay` est toujours rendu. Il ne reçoit aucune prop.
* Un `SlideToUnlock` est toujours rendu. Il reçoit la valeur de la prop `onUnlocked` passée en tant que sa prop `onSlide`, indépendamment du fait qu'elle soit définie ou non.
* Si une prop `wallpaperPath` est passée, le `div` d'enveloppement le plus externe que le composant rend doit avoir une propriété CSS `background-image` dans ses styles en ligne, définie sur la valeur de `wallpaperPath`, enveloppée dans `url(...)`.
* Si une prop `userInfoMessage` est passée, elle doit être passée en tant qu'enfants à un `TopOverlay`, qui doit être rendu avec un ensemble particulier de styles en ligne.
* Si une prop `userInfoMessage` n'est **pas** passée, **aucun** `TopOverlay` ne doit être rendu.

Certaines de ces contraintes valent la peine d'être testées, et d'autres non. Voici trois règles de base que j'utilise pour déterminer qu'une chose **ne vaut pas la peine d'être testée** :

1. Le test devra-t-il **dupliquer exactement** le code de l'application ? Cela le rendra fragile.
2. Les assertions dans le test dupliqueront-elles un comportement qui est **déjà couvert par (et de la responsabilité de) le code de la bibliothèque** ?
3. Du point de vue d'un outsider, **ce détail est-il important, ou n'est-il qu'une préoccupation interne** ? L'effet de ce détail interne peut-il être décrit en utilisant uniquement l'API publique du composant ?

Ce ne sont que des règles de base, alors faites attention à ne pas les utiliser pour justifier de ne pas tester quelque chose simplement parce que c'est difficile. **Souvent, les choses qui semblent difficiles à tester sont les plus importantes à tester**, car le code sous test fait de nombreuses hypothèses sur le reste de l'application.

Parcourons nos contraintes et utilisons ces règles de base pour déterminer lesquelles doivent être testées. Voici les trois premières :

* `wallpaperPath` est censé être une chaîne de caractères et est facultatif.
* `userInfoMessage` est censé être une chaîne de caractères et est facultatif.
* `onUnlocked` est censé être une fonction et est facultatif.

Ces contraintes sont une préoccupation du mécanisme `PropTypes` de React, et donc écrire des tests autour des types de props échoue à la règle #2 (déjà couvert par le code de la bibliothèque). Par conséquent, **je ne teste pas les types de props**. Parce que les tests servent souvent de documentation, je pourrais décider de tester quelque chose qui a échoué à la règle #2 si le code de l'application ne documentait pas très bien les types attendus, mais les `propTypes` sont déjà bien lisibles.

Voici la prochaine contrainte :

* Un `div` est toujours rendu, qui contient tout le reste. Il a un ensemble particulier de styles en ligne.

Cela peut être décomposé en trois contraintes :

* Un `div` est toujours rendu.
* Le `div` rendu contient tout le reste qui est rendu.
* Le `div` rendu a un ensemble particulier de styles en ligne.

Les deux premières contraintes que nous avons décomposées ne échouent à aucune de nos règles de base, donc **nous les testerons**. Cependant, examinons la troisième.

En ignorant la propriété background-image qui est couverte par une autre contrainte, le `div` d'enveloppement a ces styles :

```
hauteur : "100%",
affichage : "flex",
justifyContent : "space-between",
flexDirection : "column",
backgroundColor : "black",
backgroundPosition : "center",
backgroundSize : "cover",
```

Si nous écrivions un test pour vérifier que ces styles sont sur le div, nous devrions tester la valeur de chaque style **exactement** afin de faire des assertions utiles. Donc nos assertions pourraient être quelque chose comme :

* Le div d'enveloppement doit avoir une propriété de style de hauteur de 100%
* Le div d'enveloppement doit avoir une propriété de style d'affichage de flex
* ...Et ainsi de suite pour chaque propriété de style

Même si nous utilisions quelque chose comme `[toMatchObject](https://facebook.github.io/jest/docs/expect.html#tomatchobjectobject)` pour garder ce test succinct, cela dupliquerait les mêmes styles dans le code de l'application, et serait fragile. Si nous ajoutions un autre style, nous devrions mettre le même code exact dans notre test. Si nous ajustions un style, nous devrions l'ajuster dans notre test, même si le comportement du composant n'a peut-être pas changé. Par conséquent, cette contrainte échoue à la règle #1 (duplique le code de l'application ; fragile). Pour cette raison, **je ne teste pas les styles en ligne, sauf s'ils peuvent changer au moment de l'exécution**.

Souvent, si vous écrivez un test qui revient à « il fait ce qu'il fait », ou « il fait exactement cela, qui se trouve être dupliqué dans le code de l'application », alors le test est soit inutile, soit trop large.

Voici les deux prochaines contraintes :

* Un `ClockDisplay` est toujours rendu. Il ne reçoit aucune prop.
* Un `SlideToUnlock` est toujours rendu. Il reçoit la valeur de la prop `onUnlocked` passée en tant que sa prop `onSlide`, indépendamment du fait qu'elle soit définie ou non.

Celles-ci peuvent être décomposées en :

* Un `ClockDisplay` est toujours rendu.
* Le `ClockDisplay` rendu ne reçoit aucune prop.
* Un `SlideToUnlock` est toujours rendu.
* Lorsque la prop `onUnlocked` passée est définie, le `SlideToUnlock` rendu reçoit la valeur de cette prop en tant que sa prop `onSlide`.
* Lorsque la prop `onUnlocked` passée est `undefined`, la prop `onSlide` du `SlideToUnlock` rendu doit également être définie sur `undefined`.

Ces contraintes se divisent en deux catégories : « Un composant composite est rendu » et « le composant rendu reçoit ces props ». **Les deux sont très importants à tester**, car elles décrivent comment votre composant interagit avec d'autres composants. Nous testerons toutes ces contraintes.

La prochaine contrainte est :

* Si une prop `wallpaperPath` est passée, le `div` d'enveloppement le plus externe que le composant rend doit avoir une propriété CSS `background-image` dans ses styles en ligne, définie sur la valeur de `wallpaperPath`, enveloppée dans `url(...)`.

Vous pourriez penser que, parce que c'est un style en ligne, nous n'avons pas besoin de le tester. Cependant, **parce que la valeur de `background-image` peut changer en fonction de la prop `wallpaperPath`, elle doit être testée.** Si nous ne la testions pas, alors il n'y aurait aucun test autour de l'effet de la prop `wallpaperPath`, qui fait partie de l'interface publique de ce composant. Vous devez toujours tester votre interface publique.

Les deux dernières contraintes sont :

* Si une prop `userInfoMessage` est passée, elle doit être passée en tant qu'enfants à un `TopOverlay`, qui doit être rendu avec un ensemble particulier de styles en ligne.
* Si une prop `userInfoMessage` n'est **pas** passée, **aucun** `TopOverlay` ne doit être rendu.

Celles-ci peuvent être décomposées en :

* Si une prop `userInfoMessage` est passée, un `TopOverlay` doit être rendu.
* Si une prop `userInfoMessage` est passée, sa valeur doit être passée en tant qu'enfants au `TopOverlay` rendu.
* Si une prop `userInfoMessage` est passée, le `TopOverlay` rendu doit être rendu avec un ensemble particulier de styles en ligne.
* Si une prop `userInfoMessage` n'est **pas** passée, **aucun** `TopOverlay` ne doit être rendu.

Les première et quatrième contraintes (un `TopOverlay` doit/ne doit pas être rendu) **décrivent ce que nous rendons, donc nous les testerons**.

La deuxième contrainte vérifie que le `TopOverlay` reçoit une prop particulière en fonction de la valeur de `userInfoMessage`. **Il est important d'écrire des tests autour des props que les composants rendus reçoivent, donc nous la testerons**.

La troisième contrainte vérifie que `TopOverlay` reçoit une prop particulière, donc vous pourriez penser que nous devrions la tester. Cependant, cette prop est juste quelques styles en ligne. Affirmer que les props sont passées est important, mais faire des assertions sur les styles en ligne est fragile et duplique le code de l'application (échoue à la règle #1). Parce qu'il est important de tester les props passées, il n'est pas clair si cela devrait être testé juste en regardant la règle #1 seule ; heureusement, c'est pourquoi j'ai la règle #3. Pour rappel, c'est :

> Du point de vue d'un outsider, **ce détail est-il important, ou n'est-il qu'une préoccupation interne** ? L'effet de ce détail interne peut-il être décrit en utilisant uniquement l'API publique du composant ?

Lorsque j'écris des tests de composants, **je ne teste que l'API publique du composant** (y compris les effets secondaires que cette API a sur l'application) lorsque c'est possible. **La disposition exacte de ce composant n'est pas impactée par l'API publique de ce composant ; c'est une préoccupation du moteur CSS.** À cause de cela, cette contrainte échoue à la règle #3. Parce qu'elle échoue à la règle #1 et à la règle #3, **nous ne testerons pas cette contrainte**, même si elle vérifie que `TopOverlay` reçoit une prop, ce qui est normalement important.

Il était difficile de déterminer si cette dernière contrainte devait être testée ou non. En fin de compte, c'est à vous de décider quelles parties sont importantes à tester ; ces règles de base que j'utilise ne sont que des directives.

Maintenant que nous avons parcouru toutes nos contraintes et que nous savons lesquelles nous allons tester, les voici :

* Un `div` est toujours rendu.
* Le `div` rendu contient tout le reste qui est rendu.
* Un `ClockDisplay` est toujours rendu.
* Le `ClockDisplay` rendu ne reçoit aucune prop.
* Un `SlideToUnlock` est toujours rendu.
* Lorsque la prop `onUnlocked` passée est définie, le `SlideToUnlock` rendu reçoit la valeur de cette prop en tant que sa prop `onSlide`.
* Lorsque la prop `onUnlocked` passée est `undefined`, la prop `onSlide` du `SlideToUnlock` rendu doit également être définie sur `undefined`.
* Si une prop `wallpaperPath` est passée, le `div` d'enveloppement le plus externe que le composant rend doit avoir une propriété CSS `background-image` dans ses styles en ligne, définie sur la valeur de `wallpaperPath`, enveloppée dans `url(...)`.
* Si une prop `userInfoMessage` est passée, un `TopOverlay` doit être rendu.
* Si une prop `userInfoMessage` est passée, sa valeur doit être passée en tant qu'enfants au `TopOverlay` rendu.
* Si une prop `userInfoMessage` n'est **pas** passée, **aucun** `TopOverlay` ne doit être rendu.

En examinant nos contraintes et en les soumettant à un examen minutieux, nous avons décomposé beaucoup d'entre elles en plusieurs contraintes plus petites. **C'est génial !** Cela facilitera l'écriture de notre code de test.

### Mise en place de quelques éléments de test

Commençons à ébaucher un test pour ce composant. J'utiliserai [Jest](https://facebook.github.io/jest/) avec [enzyme](http://airbnb.io/enzyme/) dans mes tests. Jest [fonctionne très bien avec React](https://facebook.github.io/jest/docs/tutorial-react.html) et est également le runner de test inclus dans les applications créées avec [create-react-app](https://github.com/facebookincubator/create-react-app), donc vous pourriez déjà être prêt à l'utiliser. Enzyme est une bibliothèque de test React mature qui fonctionne à la fois dans node et le navigateur.

Même si j'utilise Jest et enzyme dans mes tests, vous pouvez appliquer les concepts ici à presque n'importe quelle configuration de test.

C'est beaucoup de code standard. Laissez-moi expliquer ce que j'ai mis en place ici :

* Je crée des liaisons `let` pour `props` et `mountedLockScreen`, afin que ces variables soient disponibles pour tout ce qui se trouve dans la fonction `describe`.
* Je crée une **fonction** `lockScreen` qui est disponible n'importe où dans la fonction `describe`, qui utilise la variable `mountedLockScreen` pour soit `monter` un `LockScreen` avec les `props` actuelles, soit retourner celui qui a déjà été monté. Cette fonction retourne un enzyme `[ReactWrapper](http://airbnb.io/enzyme/docs/api/mount.html)`. **Nous l'utiliserons dans chaque test.**
* Je configure un `beforeEach` qui réinitialise les variables `props` et `mountedLockScreen` avant chaque test. Sinon, l'état d'un test se propagerait dans un autre. En définissant `mountedLockScreen` sur `undefined` ici, lorsque le test suivant s'exécute, s'il appelle `lockScreen`, un nouveau `LockScreen` sera monté avec les `props` actuelles.

Ce code standard peut sembler beaucoup juste pour tester un composant, mais il nous permet de construire nos props de manière incrémentielle avant de monter notre composant, ce qui aidera à garder nos tests concis. Je l'utilise pour tous mes tests de composants, et j'espère que vous le trouverez utile ; son utilité deviendra plus apparente lorsque nous écrirons les cas de test.

### Écriture des tests !

Parcourons notre liste de contraintes et ajoutons un test pour chacune. Chaque test sera écrit de manière à pouvoir être inséré au commentaire `// All tests will go here` dans le code standard.

* Un `div` est toujours rendu.

* Le `div` rendu contient tout le reste qui est rendu.

* Un `ClockDisplay` est toujours rendu.

* Le `ClockDisplay` rendu ne reçoit aucune prop.

* Un `SlideToUnlock` est toujours rendu.

Toutes les contraintes jusqu'à présent ont été des choses qui sont **toujours** vraies, donc leurs tests étaient relativement simples à écrire. Cependant, les contraintes restantes commencent par des mots comme « Si » et « Lorsque ». Ce sont des indices qu'elles sont **conditionnellement** vraies, et donc nous allons associer `describe` avec `beforeEach` pour les tester. C'est là que tout ce code standard de test que nous avons écrit précédemment entre en jeu.

* Lorsque la prop `onUnlocked` passée est définie, le `SlideToUnlock` rendu reçoit la valeur de cette prop en tant que sa prop `onSlide`.
* Lorsque la prop `onUnlocked` passée est `undefined`, la prop `onSlide` du `SlideToUnlock` rendu doit également être définie sur `undefined`.

Lorsque nous devons décrire un comportement qui ne se produit que dans certaines conditions, nous pouvons `décrire` cette condition, puis utiliser `beforeEach` dans ce `describe` pour configurer cette condition.

* Si une prop `wallpaperPath` est passée, le `div` d'enveloppement le plus externe que le composant rend doit avoir une propriété CSS `background-image` dans ses styles en ligne, définie sur la valeur de `wallpaperPath`, enveloppée dans `url(...)`.

* Si une prop `userInfoMessage` est passée, un `TopOverlay` doit être rendu.
* Si une prop `userInfoMessage` est passée, sa valeur doit être passée en tant qu'enfants au `TopOverlay` rendu.

* Si une prop `userInfoMessage` n'est **pas** passée, **aucun** `TopOverlay` ne doit être rendu.

C'est toutes nos contraintes ! Vous pouvez consulter le fichier de test final [ici](https://gist.github.com/suchipi/8f8d7de60e8e4ae48153db0c36133e63).

### « Pas mon travail »

En regardant le gif animé au début de l'article, vous avez peut-être attendu que nos cas de test se terminent par quelque chose comme :

* Lorsque l'utilisateur fait glisser la poignée de déverrouillage tout à fait à droite, le callback de déverrouillage est appelé
* Si l'utilisateur fait glisser la poignée de déverrouillage partiellement à droite puis la relâche, la poignée est animée pour revenir à sa position d'origine
* L'horloge en haut de l'écran doit toujours afficher l'heure actuelle

Cette intuition est naturelle. Du point de vue de l'application, ce sont certaines des fonctionnalités les plus remarquables.

Cependant, nous n'avons pas fini par écrire des tests pour aucune de ces fonctionnalités. Pourquoi ? Elles n'étaient **pas la préoccupation de `LockScreen`**.

Parce que les composants React sont des unités réutilisables, les tests unitaires sont un choix naturel pour eux. Et lors des tests unitaires, **vous ne devez tester que ce que votre unité réelle prend en charge**. Il est préférable de voir les arbres plutôt que la forêt lors de l'écriture de tests de composants React.

Voici une feuille de triche pratique qui décrit **les préoccupations de la plupart des composants React** :

* Que fais-je avec les props que je reçois ?
* Quels composants je rends ? Que leur passe-je ?
* Est-ce que je garde quelque chose dans l'état ? Si oui, est-ce que je l'invalide lorsque je reçois de nouvelles props ? Quand est-ce que je mets à jour l'état ?
* Si un utilisateur interagit avec moi ou si un composant enfant appelle un callback que je lui ai passé, que fais-je ?
* Est-ce que quelque chose se passe lorsque je suis monté ? Lorsque je suis démonté ?

Les fonctionnalités décrites ci-dessus sont les préoccupations de `SlideToUnlock` et `ClockDisplay`, donc les tests autour de ces fonctionnalités iraient dans les tests pour ces composants, pas ici.

### Résumé

J'espère que ces méthodes vous aideront à écrire vos propres tests de composants React. Pour résumer :

* **Trouvez d'abord votre Contrat de Composant**
* Décidez quelles contraintes valent la peine d'être testées et lesquelles ne le sont pas
* Les types de props ne valent pas la peine d'être testés
* Les styles en ligne ne valent généralement pas la peine d'être testés
* Les composants que vous rendez et les props que vous leur donnez sont importants à tester
* Ne testez pas les choses qui ne sont pas la préoccupation de votre composant

Si vous n'êtes pas d'accord ou si vous avez trouvé cet article utile, j'adorerais avoir de vos nouvelles [sur twitter](https://twitter.com/suchipi). Apprenons tous ensemble comment tester les composants React !

_Bien que cet article soit sous licence tous droits réservés, tous les exemples de code dans cet article sont disponibles sous la licence MIT, comme indiqué dans leur dépôt source [sur GitHub](https://github.com/suchipi/react-testing-example-lockscreen)._