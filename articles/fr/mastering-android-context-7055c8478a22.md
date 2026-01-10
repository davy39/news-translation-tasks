---
title: Maîtriser le contexte Android
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-05T10:11:45.000Z'
originalURL: https://freecodecamp.org/news/mastering-android-context-7055c8478a22
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5tMVgzhvyHZtlBW48OUsug.jpeg
tags:
- name: Android
  slug: android
- name: Apps
  slug: apps-tag
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Maîtriser le contexte Android
seo_desc: 'By Gaurav

  Context in Android is one of the most used and abused objects. But most of the articles
  on the web focus on the definition of what it is. I could not find a good resource
  which gave me insight and helped me understand the bigger picture. So...'
---

Par Gaurav

Le contexte dans Android est l'un des objets les plus utilisés et mal utilisés. Mais la plupart des articles sur le web se concentrent sur la définition de ce qu'il est. Je n'ai pas trouvé de bonne ressource qui m'a donné un aperçu et m'a aidé à comprendre le tableau d'ensemble. J'ai donc essayé de simplifier les choses avec cet article.

![Image](https://cdn-media-1.freecodecamp.org/images/xYtafNOmFZOHjNUTahCLSVsNkwPP7JSR1gxn)
_Quel contexte utiliser ? Crédit image : Pexels_

### Préface

Ma mission pour cet article est de vous aider à maîtriser le contexte Android. C'est l'un des sujets principaux du développement Android, et peu de développeurs utilisent le contexte complètement et de la manière pour laquelle il a été conçu.

J'ai initialement publié cet article sous forme d'une série de quatre posts sur mon [site web](https://gaurav-khanna.in/). Si vous êtes intéressé par la lecture chapitre par chapitre, [n'hésitez pas à lire là-bas](https://gaurav-khanna.in/blogs/android/mastering-android-context/).

### Pour commencer

Avez-vous déjà rencontré cette question : Quelle est la différence entre `getContext()`, `this`, `getBaseContext()`, et `getApplicationContext()` ? Si oui, cet article vous aidera à clarifier la plupart de vos confusions.

**Note :** vous devriez connaître les bases du développement Android, comme Activity, Fragments, Broadcast Receiver, et autres blocs de construction. Si vous êtes un nouveau développeur qui commence tout juste votre voyage dans le monde Android, ce n'est peut-être pas le meilleur endroit pour commencer.

### Qu'est-ce que le contexte ?

Admettons-le, le contexte est l'une des fonctionnalités les plus mal conçues de l'API Android. Vous pourriez l'appeler l'objet "Dieu".

Une application Android ou un kit de package d'application (APK) est un ensemble de composants. Ces composants sont définis dans le Manifest et consistent principalement en Activity (UI), Service (Arrière-plan), BroadcastReceiver (Action), ContentProvider (Données), et Resources (images, chaînes de caractères, etc.).

Le développeur peut choisir d'exposer ces composants au système en utilisant un intent-filter. Par exemple : envoyer un email ou partager une image. Ils peuvent également choisir d'exposer les composants uniquement à d'autres composants de leur application.

De même, le système d'exploitation Android a également été conçu pour exposer des composants. Quelques-uns bien connus sont WifiManager, Vibrator et PackageManager.

Le contexte est le pont entre les composants. Vous l'utilisez pour communiquer entre les composants, instancier des composants et accéder aux composants.

#### **Vos propres composants**

Nous utilisons le contexte pour instancier nos composants avec Activity, Content Provider, BroadcastReceiver, et ainsi de suite. Nous l'utilisons également pour accéder aux ressources et aux systèmes de fichiers.

#### **Votre composant et un composant système**

Le contexte agit comme un point d'entrée vers le système Android. Certains composants système bien utilisés sont WifiManager, Vibrator et PackageManager. Vous pouvez accéder à WifiManager en utilisant `context.getSystemService(Context.WIFI_SERVICE)`.

De la même manière, vous pouvez utiliser le contexte pour accéder au système de fichiers dédié à votre application en tant qu'utilisateur dans le système d'exploitation.

#### **Votre propre composant et un composant d'une autre application**

Communiquer entre vos propres composants et ceux d'autres applications est presque identique si vous utilisez l'approche intent-filter. Après tout, chaque composant est un citoyen égal dans Android.

Un exemple d'intent utilisé pour envoyer un email est ci-dessous. Tous les composants qui offrent cette action d'intent seront servis à l'utilisateur qui peut choisir ce qu'il veut utiliser.  
 `Intent emailIntent = new Intent(android.content.Intent.ACTION_SEND);`

#### Résumé

D'accordons-nous que tout dans Android est un composant. Le contexte est le pont entre les composants. Vous l'utilisez pour communiquer entre les composants, instancier des composants et accéder aux composants. J'espère que la définition est maintenant claire.

### Différents types de contexte

Il existe de nombreuses façons d'obtenir un contexte (**mauvais design repéré**).

La plupart du temps, nous utilisons l'une des méthodes suivantes lorsque nous avons besoin de contexte :

```
- Instance de l'application en tant que contexte- Activity	- Instance de votre activité (this)	- getApplicationContext() dans Activity	- getBaseContext() dans Activity- Fragment	- getContext() dans Fragment- View	- getContext() dans View- Broadcast Receiver	- Contexte reçu dans le broadcast receiver- Service	- Instance de votre service (this)	- getApplicationContext() dans Service- Context	- getApplicationContext() dans l'instance Context
```

Je divise les types de contexte en deux catégories : **Contexte UI** et **Contexte Non-UI**. Cette distinction vous aidera à mieux comprendre les `_n-ways_`.

#### Contexte UI

En réalité, seul le [ContextThemeWrapper](https://developer.android.com/reference/android/view/ContextThemeWrapper) est un Contexte UI — ce qui signifie **Contexte + Votre thème**.

Activity étend `ContextThemeWrapper`. C'est la raison pour laquelle, lorsque vous gonflez un XML, vos vues sont thématiques. Si vous gonflez votre layout avec un contexte Non-UI, votre layout ne sera pas thématique. Allez-y, essayez.

Lorsque vous utilisez Activity comme un placeholder pour Context, vous êtes assuré d'utiliser UI Context. Si vous utilisez la méthode getContext depuis Fragment, vous utilisez indirectement Activity (si vous avez attaché Fragment via fragmentManager dans activity).

Mais `view.getContext()` n'est pas garanti d'être UI Context.

Si View a été instancié en utilisant Layout Inflater et a passé UI Context, vous obtenez UI Context en retour. Mais s'il a été instancié sans passer UI Context, vous obtenez l'autre contexte en retour.

```
Contexte UI- Activity	- Instance de votre activité (this)- Fragment	- getContext() dans Fragment- View	- getContext() dans View (si View a été construit en utilisant UI-Context)
```

#### Contexte Non-UI

Tout ce qui n'est pas Contexte UI est Contexte Non-UI. Techniquement, tout ce qui n'est pas ContextThemeWrapper est Contexte Non-UI.

Le Contexte Non-UI est autorisé à faire **presque** tout ce que le Contexte UI peut faire (**mauvais design repéré**). Mais comme nous l'avons souligné ci-dessus, vous perdez le théming.

```
Contexte Non-UI- Instance de l'application en tant que contexte- Activity	- getApplicationContext() dans Activity- Broadcast Receiver	- Contexte reçu dans le broadcast receiver- Service	- Instance de votre service (this)	- getApplicationContext() dans Service- Context	- getApplicationContext() dans l'instance Context
```

**Astuce** : Tous les types de contexte sont censés être de courte durée sauf le contexte Application. C'est celui que vous obtenez à partir de votre classe d'application ou en utilisant la méthode `getApplicationContext()` lorsque vous avez accès au contexte.

#### Résumé

Nous avons simplifié un peu en mettant le Contexte dans deux catégories. Le Contexte UI est Contexte + Théming, et techniquement toute classe qui est une sous-classe de `ContextThemeWrapper` entre dans cette catégorie. Le Contexte Non-UI est tous les autres types de Contexte.

### Où utiliser quoi

La question se pose : que se passera-t-il si vous utilisez le contexte au mauvais endroit ? Voici quelques scénarios :

#### Scénario 1

Disons que vous gonflez un layout et que vous utilisez un Contexte Non-UI. Qu'est-ce qui peut mal se passer ? Vous pouvez deviner dans ce cas : vous n'obtiendrez pas un layout thématique. Pas si grave, hmm ? C'est supportable.

#### Scénario 2

Vous passez UI-Context à un endroit où tout ce dont il a besoin est l'accès aux ressources ou au système de fichiers. Qu'est-ce qui peut mal se passer ? Réponse courte : Rien. Souvenez-vous, UI-Context = Contexte + Thème. Il servira volontiers de contexte pour vous.

#### Scénario 3

Vous passez UI-Context à un endroit où tout ce dont il a besoin est l'accès aux ressources ou au système de fichiers **mais** c'est une opération longue en arrière-plan. Disons télécharger un fichier. Maintenant, qu'est-ce qui peut mal se passer ? Réponse courte : Fuites de mémoire.

Si vous avez de la chance et que le téléchargement se termine rapidement, l'objet est libéré et tout est bien. Le soleil brille et les oiseaux chantent. C'est l'une des erreurs les plus courantes que commettent les développeurs. Ils passent la référence de UI-Context à des objets de longue durée, et parfois cela n'a aucun effet secondaire.

Cependant, parfois Android veut réclamer de la mémoire pour soit l'un de vos prochains composants, soit les exigences d'un autre composant, et woooshhhh!!! Vous manquez de mémoire dans votre application. Ne vous inquiétez pas, je vais expliquer.

#### Fuites de mémoire ou crash ! C'est tout.

Oui, c'est le pire scénario lorsque vous utilisez le contexte au mauvais endroit. Si vous êtes nouveau dans le monde du développement d'applications, permettez-moi de partager quelques sagesse. Les fuites de mémoire sont inversement proportionnelles à votre expérience. Chaque développeur Android a déjà eu des fuites de mémoire. Il n'y a pas de honte à le faire.

La honte, c'est lorsque vous répétez la même erreur et que vous avez des fuites de la même manière. Si vous avez des fuites de mémoire de manière différente à chaque fois, félicitations, vous grandissez. J'ai expliqué ce qu'est une fuite de mémoire avec une courte histoire [ici](https://gaurav-khanna.in/blogs/android/mastering-android-context/chapter-3/).

#### D'accord, je comprends, mais quel est le rapport avec le Contexte ici ?

Dites-le à voix haute, "Mauvais design repéré".

Presque tout dans Android a besoin d'accéder au Contexte. Les développeurs naïfs passent UI Context, parce que c'est ce à quoi ils ont accès très facilement. Ils passent un contexte de courte durée (généralement le contexte Activity) à des objets de longue durée et avant que la mémoire/l'argent ne soit rendu au système, ils rencontrent une crise. Woooshhh!!!

La manière la plus simple de gérer cela est avec Async Task ou Broadcast Receiver. Mais discuter d'eux n'est pas dans le cadre de cet article.

#### Résumé

* Avez-vous besoin d'accéder à des éléments liés à l'UI ? Utilisez UI-Context. Gonfler des vues et afficher des dialogues sont les deux cas d'utilisation auxquels je pense.
* Sinon, utilisez Non UI Context.
* Assurez-vous de ne pas passer de contexte de courte durée à des objets de longue durée.
* Transmettez des connaissances, aidez les gens, plantez des arbres et invitez-moi pour un café.

### Astuces et conseils

Quelle est la différence entre `this`, `getApplicationContext()` et `getBaseContext()` ?

C'est une question à laquelle chaque développeur Android a été confronté dans sa vie. Je vais essayer de la simplifier autant que possible. Faisons un pas en arrière et revisitons les bases.

Nous savons qu'il y a de nombreux facteurs dans les appareils mobiles. Par exemple, les configurations changent tout le temps, et la locale peut changer explicitement ou implicitement.

Tous ces changements déclenchent les applications à se recréer afin qu'elles puissent choisir les bonnes ressources qui correspondent le mieux à leur configuration actuelle. Portrait, Paysage, Tablette, Chinois, Allemand, et ainsi de suite. Votre application a besoin des meilleures ressources possibles pour offrir la meilleure expérience utilisateur. C'est le Contexte qui est responsable de la livraison de ces meilleures ressources correspondantes.

Essayez de répondre à cette question :  
La configuration de l'utilisateur est actuellement en portrait et vous voulez accéder aux ressources en paysage. Ou la locale de l'utilisateur est `en` et vous voulez accéder aux ressources `uk`. Comment allez-vous faire ?

Voici quelques méthodes magiques de Context :

![Image](https://cdn-media-1.freecodecamp.org/images/pm0XjARPJfj3jaVp6O846mROEem3fKcYVOS1)

Il existe de nombreuses méthodes createX, mais nous nous intéressons principalement à `createConfigurationContext`. Voici comment vous pouvez l'utiliser :

```
Configuration configuration = getResources().getConfiguration();configuration.setLocale(your_custom_locale);context = createConfigurationContext(configuration);
```

Vous pouvez obtenir n'importe quel type de Contexte que vous désirez. Lorsque vous appelez une méthode sur le nouveau Contexte que vous venez d'obtenir, vous aurez accès aux ressources basées sur la configuration que vous avez définie.

Je sais que c'est incroyable. Vous pouvez m'envoyer une carte de remerciement.

De même, vous pouvez créer un Contexte Thématique et l'utiliser pour gonfler des vues avec le thème que vous voulez.

```
ContextThemeWrapper ctw = new ContextThemeWrapper(this, R.style.YOUR_THEME);
```

Revenons à la question délicate que nous avons posée ci-dessus et discutons du Contexte Activity.

Quelle est la différence entre `**this**`**, `getApplicationContext()`** et `**getBaseContext()**`**?**

Ce sont les moyens possibles d'obtenir un Contexte lorsque vous êtes dans le scope `Activity`.

`this` pointe vers Activity elle-même, notre UI Context et contexte de courte durée. `getApplicationContext()` pointe vers votre instance d'application qui est Non-UI et contexte de longue durée.

`**baseContext**` est la base de votre Contexte Activity que vous pouvez définir en utilisant un modèle de délégué. Vous savez déjà que vous pouvez créer un Contexte avec n'importe quelle configuration `xyz` que vous voulez. Vous pouvez combiner votre connaissance de la configuration `xyz` avec Base Context et votre Activity chargera les ressources comme vous le désirez.

Voici la méthode que vous pouvez utiliser :

```
@Overideprotected void attachBaseContext (Context base) {super.attachBaseContext(useYourCustomContext);}
```

Une fois `BaseContext` attaché, votre Activity déléguera les appels à cet objet. Si vous ne l'attachez pas à Activity, il reste `baseContext` et vous obtenez Activity lorsque vous appelez `getBaseContext`.

### Conclusion

Nous pouvons dire que le Contexte est la vie de votre application Android. Du point de vue d'Android, c'est votre application. Vous pouvez faire presque rien sans Contexte. Sans lui, votre application est du code Java simple.

#### Contexte + Code Java => Android

Bon ou mauvais, c'est le design que nous avons et nous devons en faire le meilleur. Dans la première partie de cet article, nous avons appris que nous l'utilisons pour communiquer entre les composants, instancier des composants et accéder aux composants.

Dans la partie suivante, nous avons appris que le Contexte peut être UI ou NonUI, de courte durée ou de longue durée.

Ensuite, nous avons appris que vous devez choisir le contexte avec soin, sinon vous devez gérer les fuites de mémoire et autres problèmes d'UI.

Enfin, vous avez vu que le Contexte est responsable du chargement des meilleures ressources correspondantes pour votre application et que vous pouvez le configurer comme vous le souhaitez. Nous avons également appris la différence entre `this`, `applicationContext` et `baseContext`.

De nombreux développeurs vous conseilleront d'utiliser uniquement le contexte de l'application. N'utilisez pas le Contexte Application partout par peur des fuites de mémoire. Comprenez la cause racine et utilisez toujours le bon Contexte au bon endroit.

Vous, mon cher ami, êtes maintenant un maître du Contexte Android. Vous pouvez suggérer le prochain sujet que vous souhaitez comprendre. [Cliquez ici pour suggérer](https://goo.gl/forms/Du4zTz1MleQsWHHu2).

Ci-dessous se trouvent les liens de la série originale [**Maîtriser le contexte Android**](https://gaurav-khanna.in/blogs/android/mastering-android-context/) sur mon blog.

#### [Chapitre 1](https://gaurav-khanna.in/blogs/android/mastering-android-context/chapter-1/)

Qu'est-ce que le contexte ? Pourquoi en avons-nous besoin et quels sont les différents cas d'utilisation dans le développement quotidien ?

#### [Chapitre 2](https://gaurav-khanna.in/blogs/android/mastering-android-context/chapter-2/)

Simplifier le contexte. Nous discuterons du nombre de types de contexte qui existent et de ceux que vous êtes censé utiliser.

#### [Chapitre 3](https://gaurav-khanna.in/blogs/android/mastering-android-context/chapter-3/)

Où utiliser le contexte UI et où utiliser le contexte Non-UI. Comment utiliser le contexte au mauvais endroit peut conduire à des fuites de mémoire.

#### [Chapitre 4](https://gaurav-khanna.in/blogs/android/mastering-android-context/chapter-4/)

Mon contexte UI m'offre également plusieurs types de contexte. Répondons à cette question et voyons comment éviter les pièges courants.

#### [Formation](https://gaurav-khanna.in/training/)

Savez-vous que de nombreuses fois votre application plante parce que vos développeurs n'utilisent pas correctement le contexte ? Apprenons ensemble. [Je propose des formations en Android, Java et Git.](https://gaurav-khanna.in/training/)

Vous voulez maîtriser les [thèmes Android](https://gaurav-khanna.in/blogs/android/mastering-android-themes/) ? Consultez notre série avec plus de 3k votes positifs.

N'hésitez pas à partager vos commentaires et questions. Bon codage.

Suivez-moi sur [Medium](https://medium.com/@gaurav.khanna) et [Twitter](https://twitter.com/khanna2402) pour les mises à jour.