---
title: Comment créer un écran de démarrage React Native
subtitle: ''
author: Lucas
co_authors: []
series: null
date: '2024-05-08T19:17:54.000Z'
originalURL: https://freecodecamp.org/news/react-native-splash-screen
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/article-1-rnsplash-2.png
tags:
- name: React Native
  slug: react-native
seo_title: Comment créer un écran de démarrage React Native
seo_desc: "In this article, you'll get a hands-on practical guide for creating a native\
  \ splash screen for React Native CLI applications. \nNote that this tutorial is\
  \ not applicable for apps created with Expo.\nSVG Icon Image and Background\nThe\
  \ first thing you nee..."
---

Dans cet article, vous obtiendrez un guide pratique pour créer un écran de démarrage natif pour les applications React Native CLI.

Notez que ce tutoriel n'est pas applicable pour les applications créées avec Expo.

## Image d'icône SVG et arrière-plan

La première chose dont vous avez besoin est une image. Elle peut être dans n'importe quel format, mais je recommande d'utiliser SVG car, à partir de celui-ci, vous générerez des icônes de différentes tailles pour différents types d'appareils Android et iOS.

Vous aurez également besoin d'une couleur d'arrière-plan qui complète ou contraste avec la couleur primaire de votre projet. Dans mon cas, j'utiliserai #074C4E.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/nubble-logo.png)
_image d'icône et couleur d'arrière-plan_

## Ajouter l'image au projet

Ensuite, ajoutez l'image SVG à votre projet. Peu importe où. Le plus important est de se souvenir du chemin car vous devrez y faire référence plus tard.

Dans mon cas, je l'ai placée dans `src/assets/svgs/logo-vertical-white.svg`.

## Comment utiliser la bibliothèque react-native-bootsplash

Vous utiliserez la bibliothèque `[react-native-bootsplash](https://github.com/zoontek/react-native-bootsplash)` pour créer des écrans de démarrage natifs. Cette bibliothèque vous aidera dans trois domaines essentiels pour garantir à vos utilisateurs une excellente expérience lors de l'affichage de l'écran de démarrage.

1. **Écrans de démarrage natifs** : Les applications React Native ont un "côté JavaScript" qui ne se charge qu'après que le côté natif est prêt. Par conséquent, pour présenter rapidement un écran de démarrage, une expérience native est nécessaire. La bonne nouvelle est que tout le code est déjà dans la bibliothèque, vous devez donc simplement le connecter à votre projet.
2. **Génération d'images et de fichiers** : Lors de la création d'écrans de démarrage natifs, il est nécessaire de créer des fichiers d'image spécifiques pour chaque plateforme. Cela peut être fait via des outils comme Xcode et Android Studio. Heureusement, la bibliothèque est livrée avec un CLI (interface de ligne de commande) qui vous permet de générer ces fichiers avec une seule commande !
3. **Masquer au bon moment** : Dans de nombreux cas, même après que le côté natif a chargé, l'application peut ne pas être encore prête à afficher du contenu à l'utilisateur. Du côté JavaScript, vous devez encore charger votre pile de navigation, récupérer le statut d'authentification de l'utilisateur ou appeler l'API pour récupérer des données. Avec `react-native-bootsplash`, vous pouvez choisir quand masquer l'écran de démarrage.

Tout d'abord, ajoutons la bibliothèque. Comme j'utilise Yarn comme gestionnaire de dépendances, j'exécuterai la commande :

```bash
yarn add react-native-bootsplash
```

Étant donné que la bibliothèque a des dépendances natives, vous devez installer les pods du côté iOS. Dans le dossier `ios`, exécutez la commande suivante :

```bash
pod install
```

Super, l'installation de la bibliothèque est terminée 😁. Au cas où vous vous poseriez la question, les dépendances natives Android sont automatiquement installées lorsque vous exécutez la commande `yarn android`. Nous ferons cela plus tard après avoir terminé la configuration.

## Comment générer les fichiers de l'écran de démarrage

En plus d'installer la bibliothèque, vous devez générer les fichiers et images mentionnés précédemment et mettre à jour quelques fichiers natifs après cela.

La bibliothèque `react-native-bootsplash` dispose d'une commande qui nous aide à créer tous les fichiers et images natifs nécessaires pour créer un écran de démarrage natif Android et iOS.

Il est worth de mentionner que la bibliothèque dispose également d'une option premium, où vous pouvez acheter une clé de licence pour débloquer des commandes CLI supplémentaires, comme ajouter plus d'une icône sur l'écran et générer différentes images pour le mode sombre. Vous utiliserez l'écran de démarrage le plus simple, donc vous n'avez pas besoin d'une clé de licence. Mais je vous le recommande vivement si vous avez l'un des cas d'utilisation mentionnés ci-dessus et également pour soutenir l'auteur de la bibliothèque, qui fait un travail incroyable.

Pour générer les fichiers, vous aurez besoin des éléments suivants pour exécuter la commande, que vous devez personnaliser selon votre projet :

1. Chemin et nom du fichier : `src/assets/svgs/logo-vertica-white.svg`
2. La couleur d'arrière-plan : `074C4E`
3. La largeur du logo : `105`

```bash
yarn react-native generate-bootsplash src/assets/svgs/logo-vertica-white.svg \\
   --platforms=android,ios \\
   --background=074C4E \\
   --logo-width=105
```

Après avoir exécuté cette commande, vous verrez que les fichiers d'image natifs, la couleur et le storyboard ont été générés avec succès.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/terminal.png)
_sortie du terminal_

## Comment connecter la bibliothèque au projet

Il est temps d'intégrer la bibliothèque et le nouvel écran de démarrage créé avec le projet en modifiant certains fichiers natifs.

### iOS - AppDelegate.mm

Sur iOS, le fichier où vous configurez les bibliothèques avec des dépendances natives est le **AppDelegate.mm**.

Et vous le ferez en deux étapes. Tout d'abord, importez la bibliothèque en haut du fichier :

```cpp
#import "RNBootSplash.h"
```

![Image](https://www.freecodecamp.org/news/content/images/2024/05/ios-import.png)
_importation de BootSplash sur AppDelegate_

Le deuxième changement dans ce fichier consiste à ajouter la fonction qui connectera les côtés natif et JavaScript. Ajoutez ce snippet à la fin du projet avant le dernier `@end`. Le code sera différent si vous utilisez une version de react-native inférieure à 0.74.

```cpp
// ⬇️ Ajoutez ceci avant le @end du fichier (pour react-native 0.74+)
- (void)customizeRootView:(RCTRootView *)rootView {
  [RNBootSplash initWithStoryboard:@"BootSplash" rootView:rootView]; // ⬅️ initialiser l'écran de démarrage
}

// OU

// ⬇️ Ajoutez ceci avant le @end du fichier (pour react-native < 0.74)
- (UIView *)createRootViewWithBridge:(RCTBridge *)bridge
                          moduleName:(NSString *)moduleName
                           initProps:(NSDictionary *)initProps {
  UIView *rootView = [super createRootViewWithBridge:bridge moduleName:moduleName initProps:initProps];
  [RNBootSplash initWithStoryboard:@"BootSplash" rootView:rootView]; // ⬅️ initialiser l'écran de démarrage
  return rootView;
}
```

Dans mon cas, je suis sur react-native 0.73, donc ma modification ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/05/ios-code.png)
_ajout de createRootViewWithBridge (react-native < 0.74)_

### Android - styles.xml

Sur Android, vous devez modifier trois fichiers natifs. Commençons par **styles.xml**.

À l'intérieur du fichier **android/app/src/main/res/values/styles.xml**, ajoutez le snippet de code suivant à l'intérieur de la balise `resources`. N'oubliez pas, il y a déjà une balise `style` à l'intérieur - ne la remplacez pas. Ajoutez-en une supplémentaire.

```xml
<style name="BootTheme" parent="Theme.BootSplash">
    <item name="bootSplashBackground">@color/bootsplash_background</item>
    <item name="bootSplashLogo">@drawable/bootsplash_logo</item>
    <item name="postBootSplashTheme">@style/AppTheme</item>
</style>
```

![Image](https://www.freecodecamp.org/news/content/images/2024/05/android-styles.png)
_styles.xml_

### Android - AndroidManifest.xml

Pour connecter l'écran de démarrage dans le fichier **android/app/src/main/AndroidManifest.xml**, vous devez ajouter la propriété `android:theme="@style/BootTheme"` à l'intérieur de l'`activity`.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/android-AndroidManifest.png)
_Mon AndroidManifest.xml_

### Android - Modifier le MainActivity.java/kt

Vous devez initier l'écran de démarrage dans le `MainActivity`. Selon votre version de React Native, votre fichier peut avoir une extension Java ou Kotlin. Vous devez modifier ou créer la méthode `onCreate` si elle n'existe pas.

J'ai littéralement copié le code ci-dessous du fichier **README** de la bibliothèque, donc vous n'avez pas besoin d'y aller, mais n'hésitez pas à le vérifier [ici](https://github.com/zoontek/react-native-bootsplash?tab=readme-ov-file#android-1).

```java
// Java (react-native < 0.73)
// …

// ajoutez ces imports requis :
import android.os.Bundle;
import com.zoontek.rnbootsplash.RNBootSplash;

public class MainActivity extends ReactActivity {

  // …

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    RNBootSplash.init(this, R.style.BootTheme); // ⬅️ initialiser l'écran de démarrage
    super.onCreate(savedInstanceState); // super.onCreate(null) avec react-native-screens
  }
}
```

![Image](https://www.freecodecamp.org/news/content/images/2024/05/android-MainActivity.png)
_Mon MainActivity.java final_

### Masquer l'écran de démarrage

L'implémentation est prête pour les deux plateformes ! Mais avant de lancer l'application, vous devez masquer l'écran de démarrage à un moment donné du côté JavaScript ; sinon, l'application s'ouvrira et restera bloquée.

Bien sûr, où le placer dépend largement de ce que vous devez charger pour que votre application soit prête à être affichée à l'utilisateur. Un exemple classique est d'attendre que React Navigation charge la pile de navigation, ce qui est signalé via le callback `onReady`.

```ts
import BootSplash from 'react-native-bootsplash';
// ...

export function Router() {
	// ...
	return (
    <NavigationContainer onReady={() => BootSplash.hide({fade: true})}>
      {Stack}
    </NavigationContainer>
  );
}
```

### Vous êtes prêt à partir !

Votre écran de démarrage est prêt à être utilisé ! Cependant, puisque vous avez modifié des fichiers natifs, il est nécessaire de reconstruire l'application. Pour ce faire, exécutez les commandes `yarn ios` et `yarn android` pour voir comment votre implémentation fonctionne.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/showcase.gif)

Merci d'avoir lu ! Si vous parlez portugais et que vous souhaitez plus de contenu sur React Native, abonnez-vous à ma chaîne YouTube [ici](https://www.youtube.com/@Coffstack).