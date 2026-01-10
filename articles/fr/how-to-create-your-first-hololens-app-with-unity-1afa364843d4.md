---
title: Comment créer votre première application HoloLens avec Unity
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-15T21:38:16.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-your-first-hololens-app-with-unity-1afa364843d4
coverImage: https://cdn-media-1.freecodecamp.org/images/0*LybjBzQe4KnxejOR.jpg
tags:
- name: hololens
  slug: hololens
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: unity
  slug: unity
- name: Virtual Reality
  slug: virtual-reality
seo_title: Comment créer votre première application HoloLens avec Unity
seo_desc: 'By Max Huddleston

  Microsoft’s HoloLens is pretty freaking awesome. I was introduced to it at my internship
  this summer, and I’ve had a blast developing for it.

  HoloLens apps are created using either DirectX with C++ or Unity with C#. I found
  that it ...'
---

Par Max Huddleston

[Microsofts HoloLens](https://www.microsoft.com/en-us/hololens) est vraiment génial. J'ai été introduit à cela lors de mon stage cet été, et j'ai adoré développer pour cela.

Les applications HoloLens sont créées en utilisant soit DirectX avec C++ soit Unity avec C#. J'ai trouvé qu'il est généralement plus rapide et plus facile de démarrer une application avec Unity.

Dans cet article, nous allons configurer Unity pour le développement HoloLens, créer un cube interactif et lancer l'émulateur HoloLens afin que vous puissiez voir votre création. Cet article est destiné aux débutants complets de Unity, donc si vous avez de l'expérience avec l'éditeur, je vous recommande de suivre [les tutoriels de Microsoft](https://docs.microsoft.com/en-us/windows/mixed-reality/academy).

### Prérequis

1. Un PC Windows 10 avec la mise à jour d'avril 2018
2. L'émulateur HoloLens que vous pouvez télécharger [ici](https://docs.microsoft.com/en-us/windows/mixed-reality/install-the-tools)
3. [Visual Studio 2017](https://developer.microsoft.com/en-us/windows/downloads) — L'édition Community est suffisante
4. [Unity](https://store.unity.com/download) — Assurez-vous d'ajouter le composant Windows .NET scripting backend pendant l'installation
5. Le [HoloToolKit](https://github.com/Microsoft/MixedRealityToolkit-Unity/releases)

Vous pouvez trouver le code source complet [ici](https://github.com/cptn-neemo/FirstHoloLensApplication).

### Installation

Ouvrez Unity. Si c'est la première fois que vous utilisez l'éditeur, vous serez invité à vous connecter ou à vous inscrire. Je recommande Unity Personal sauf si vous prévoyez de monétiser votre application.

Après vous être connecté, créez un nouveau projet et entrez un nom. Vous devriez être accueilli avec cet écran après que le projet ait terminé la configuration initiale.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Nt1kDO3K0sfzQIOfT-gexw.png)
_Éditeur Unity au premier démarrage_

Faites un clic droit sur le dossier Assets dans le coin inférieur gauche. Naviguez jusqu'à Import Package -> Custom Package, et ouvrez le fichier unity HoloToolKit que nous avons téléchargé précédemment. Une fenêtre contextuelle Unity apparaîtra, cliquez sur All et importez les assets.

Ensuite, nous allons créer notre scène. Sélectionnez File -> New Scene et enregistrez-la sous Main.

Unity a besoin d'une configuration spéciale pour construire un projet pour HoloLens. Heureusement, le HoloToolKit dispose de scripts utilitaires qui effectuent cette configuration pour nous. Dans la barre d'outils supérieure, sélectionnez Mixed Reality Toolkit -> Configure -> Apply Mixed Reality Project Settings. Utilisez les valeurs par défaut. Après la fin de la configuration, appliquez les Mixed Reality Scene Settings. Supprimez le GameObject Directional Light.

Super ! Jusqu'à présent, nous avons importé le HoloToolKit et configuré Unity pour le développement HoloLens. Dans la section suivante, je vous présenterai les bases de Unity, et après cela, nous ferons en sorte qu'un cube s'affiche à l'écran.

### Familiarisation avec l'éditeur

Voici à quoi devrait ressembler l'éditeur à ce stade. Remarquez les trois zones encadrées :

![Image](https://cdn-media-1.freecodecamp.org/images/1*-ilX9-KD5YD1BpmjBpHJVw.png)

La zone rouge à gauche est le panneau de hiérarchie de la scène. Ici, nous pouvons ajouter de nouveaux **GameObjects** et obtenir une vue d'ensemble de haut niveau de l'application actuelle. Un [GameObject](https://docs.unity3d.com/ScriptReference/GameObject.html) est une classe de base pour toutes les entités Unity. Ils peuvent être un objet physique comme un cube, ou une collection de scripts comme le Input Manager dans la scène.

La zone bleue en bas contient le menu des assets et la console. Le menu des assets est exactement ce à quoi il ressemble — il contient les scripts C#, les matériaux, les prefabs et les maillages nécessaires pour exécuter votre application.

La zone verte de droite est le menu de l'inspecteur. C'est ici que vous pouvez ajouter et modifier les **Composants** de vos GameObjects. Les [Composants](https://docs.unity3d.com/ScriptReference/Component.html) sont ce qui constitue le comportement de vos GameObjects. Ils déterminent l'apparence, l'interactivité et la physique de leur parent.

### Création d'un cube

Maintenant, nous allons faire en sorte que notre premier GameObject s'affiche à l'écran. Dans le panneau de hiérarchie de la scène, faites un clic droit et sélectionnez 3D Object -> Cube. Un cube devrait apparaître dans l'éditeur.

Double-cliquez sur Cube dans le panneau de hiérarchie, et dans le panneau de l'inspecteur à droite, changez la position en (0,0,2). Définissez l'échelle à (.25, .25, .25). Votre panneau de l'inspecteur devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*KIYP5ws7ST6n_5thE7UmRg.png)
_Panneau de l'inspecteur du cube_

Bien ! Passons aux étapes de construction pour que nous puissions voir notre cube dans l'émulateur HoloLens.

Dans Unity, sélectionnez File->Build Settings. La fenêtre contextuelle de construction devrait apparaître, alors cliquez sur le bouton de construction. Dans la fenêtre contextuelle du dossier, créez un nouveau dossier appelé App et choisissez-le comme destination de construction.

Après la fin de la construction, ouvrez la solution Visual Studio dans le dossier App. Changez les options de débogage en Release, x86, et ciblez l'émulateur HoloLens. Votre barre d'options devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*EJuVLjAtgMeuaLT10oikxw.png)
_Options de débogage pour l'émulateur HoloLens_

Exécutez la solution, et après le démarrage de l'émulateur et le chargement de votre application, vous devriez voir votre cube à l'écran.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4vCqc5n03DuxLsuhK1_z_A.png)
_Cube dans l'émulateur_

### Rendre le cube interactif

Maintenant que nous avons compris comment faire apparaître un cube dans notre application, faisons en sorte que le cube fasse réellement quelque chose. Lorsque nous regardons le cube, il va tourner, et lorsque nous cliquons sur le cube, il va augmenter de taille.

Revenez à Unity et créez un nouveau script dans le panneau des assets appelé InteractiveCube. Pour créer un nouveau script, faites un clic droit sur le panneau des assets et sélectionnez Create -> C# script.

Pour ajouter le script au cube, assurez-vous que le cube est sélectionné, et faites glisser et déposez le script sur le panneau de l'inspecteur. Cela devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*dfj3gWXCP4EZOw8sxvUafA.png)

Double-cliquez sur le script dans l'onglet des assets et une instance de Visual Studio devrait apparaître.

Importez HoloToolkit.Unity.InputModule en haut de notre script, et faites en sorte que InteractiveCube étende IFocusable et IInputClickHandler. Notre code devrait ressembler à ceci :

```
using HoloToolkit.Unity.InputModule;
```

```
public class InteractiveCube : MonoBehaviour, IFocusable, IInputClickHandler {...} 
```

En étendant les interfaces IFocusable et IInputClickHandler, notre composant de script permet au GameObject parent de s'abonner aux événements de focus et de clic.

Faisons tourner le cube lorsque notre regard est dessus. L'interface IFocusable nous oblige à implémenter deux méthodes publiques void : OnFocusEnter et OnFocusExit. Créez un champ booléen privé et nommez-le Rotating. Lorsque nous focalisons le cube, définissez-le sur true, et lorsque notre focus quitte, définissez-le sur false. Notre code devrait ressembler à ceci :

```
public bool Rotating;
```

```
public void OnFocusEnter(){    Rotating = true;}
```

```
public void OnFocusExit(){    Rotating = false;}
```

Nous allons faire la rotation réelle dans Update(). Update() est une méthode spéciale Unity qui est appelée à chaque frame. Pour contrôler la vitesse de la rotation, ajoutez un champ float public nommé RotationSpeed. Tout champ public dans un composant peut être ajusté et initialisé dans l'éditeur Unity.

```
public float RotationSpeed;
```

```
void Update() {    if (Rotating)        transform.Rotate(Vector3.Up * Time.deltaTime            * RotationSpeed);}
```

Dans Unity, le transform est utilisé pour contrôler les attributs physiques tels que la taille, la rotation et la position d'un GameObject. Nous faisons tourner le GameObject parent autour de l'axe y à un degré par seconde multiplié par la vitesse.

Pour faire en sorte que le cube réponde aux événements de clic, ajoutez la méthode OnInputClicked requise par IInputClickHandler. Créez une variable Vector3 publique appelée ScaleChange. Dans la méthode OnInputClicked, nous allons augmenter l'échelle du cube par ScaleChange.

```
public Vector3 ScaleChange;
```

```
public void OnInputClicked(InputClickedEventData eventData) {    transform.localScale += ScaleChange;}
```

Maintenant que nous avons terminé avec le script, revenez à Unity. Assurez-vous que l'objet Cube est sélectionné, et définissez les variables Speed et ScaleChange à 50 et (.025, .025, .025) respectivement. N'hésitez pas à expérimenter avec différentes valeurs ! Notre script devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*voFzBQvBaHVcBtmoYQv6zg.png)

Super ! Nous avons terminé le script InteractiveCube. Construisez votre application à partir de l'éditeur Unity, et exécutez la solution à partir de Visual Studio.

### Résumé

Dans ce guide, vous avez appris comment configurer Unity pour le développement HoloLens, créer un GameObject interactif et exécuter votre application dans l'émulateur.

Si vous aimez le développement HoloLens, je vous encourage à suivre les [tutoriels Microsoft Academy](https://docs.microsoft.com/en-us/windows/mixed-reality/academy). Ils couvrent les divers concepts clés de HoloLens en détail et vous guident à travers la création de quelques applications assez cool.

Si vous avez aimé l'article ou avez des commentaires, laissez un commentaire ci-dessous !