---
title: Comment implémenter n'importe quelle interface utilisateur dans Flutter
subtitle: ''
author: Obum
co_authors: []
series: null
date: '2022-06-08T15:22:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-any-ui-in-flutter
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/anyuicover.png
tags:
- name: Flutter
  slug: flutter
- name: mobile app development
  slug: mobile-app-development
- name: UI Design
  slug: ui-design
- name: User Interface
  slug: user-interface
seo_title: Comment implémenter n'importe quelle interface utilisateur dans Flutter
seo_desc: 'In this article, you will learn how to convert any user interface image,
  piece, or screen into Flutter code.

  This is not a tutorial on building an app. It is rather a guide that will help you
  implement any UI you come across into an app you already h...'
---

Dans cet article, vous apprendrez comment convertir n'importe quelle image, élément ou écran d'interface utilisateur en code [Flutter](https://flutter.dev).

Ce n'est pas un tutoriel sur la création d'une application. Il s'agit plutôt d'un guide qui vous aidera à implémenter n'importe quelle interface utilisateur que vous rencontrez dans une application que vous avez déjà. Ce tutoriel explique également une grande variété de concepts d'interface utilisateur dans Flutter.

## Table des matières

* [Qu'est-ce que Flutter ?](#heading-qu-est-ce-que-flutter)
    
* [Les widgets dans Flutter](#heading-les-widgets-dans-flutter)
    
* [L'arborescence des widgets](#heading-l-arborescence-des-widgets)
    
* [Comment implémenter n'importe quelle interface utilisateur dans Flutter](#heading-comment-implementer-n-import-quelle-interface-utilisateur-dans-flutter)  
    [1\. Implémenter en haut à gauche ; en bas à droite](#heading-1-ecrivez-votre-code-en-commencant-en-haut-a-gauche-et-descendez-vers-le-bas-a-droite)  
    [2\. Choisir un widget](#heading-2-choisir-un-widget)  
    [3\. Utiliser des groupes de widgets](#heading-3-utiliser-des-groupes-de-widgets)  
    [a. Column/Row](#heading-a-colonnerow)  
    [b. Widget Stack](#heading-b-widget-stack)  
    [4\. Créer des widgets personnalisés](#heading-4-creer-des-widgets-personnalises)  
    [5\. Ajouter plus de personnalisation](#heading-5-ajouter-plus-de-personnalisation)  
    [a. Widget Container](#heading-a-widget-container)  
    [b. GestureDetector / InkWell](#heading-b-gesturedetector-inkwell)
    
* [Comment implémenter des interfaces défilantes](#heading-comment-implementer-des-interfaces-defilantes)
    
* [À propos de CustomPaint](#heading-a-propos-de-custompaint)
    
* [Résumé](#heading-resume)
    

## Qu'est-ce que Flutter ?

> Flutter est un framework open source de Google pour créer des applications belles, compilées nativement et multiplateformes à partir d'une seule base de code.  (s[ource: flutter.dev](https://flutter.dev))

Dans Flutter, contrairement à la plupart des frameworks, [Dart](https://dart.dev) est le seul langage de programmation que vous utilisez pour coder. C'est un avantage sous-estimé de Flutter. Surtout pour un outil qui peut créer des applications de bureau, mobiles et web.

La plupart des [plateformes d'interface utilisateur](https://en.wikipedia.org/wiki/User_interface_design) utilisent plus d'un langage. Par exemple, dans le développement web frontal, vous devez écrire [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML), [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) et [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript). Pour [Android](https://developer.android.com/), vous devez écrire [Kotlin](https://developer.android.com/kotlin) (ou [Java](https://developer.android.com/studio/write/java8-support)) et [XML](https://developer.android.com/guide/topics/ui/declaring-layout#write). Mais dans Flutter, il n'y a qu'un seul langage : Dart.

Couplé à l'avantage d'un seul langage de programmation, Flutter est simple car tout dans Flutter est un widget. Par exemple [AnimatedWidget](https://api.flutter.dev/flutter/widgets/AnimatedWidget-class.html), [BottomNavigationBar](https://api.flutter.dev/flutter/material/BottomNavigationBar-class.html), [Container](https://api.flutter.dev/flutter/widgets/Container-class.html), [Drawer](https://api.flutter.dev/flutter/material/Drawer-class.html), [ElevatedButton](https://api.flutter.dev/flutter/material/ElevatedButton-class.html), [FormField](https://api.flutter.dev/flutter/widgets/FormField-class.html), [Image](https://api.flutter.dev/flutter/widgets/Image-class.html), [Opacity](https://api.flutter.dev/flutter/widgets/Opacity-class.html), [Padding](https://api.flutter.dev/flutter/widgets/Padding-class.html), ...

C'est ce qui rend Flutter facile à utiliser  c'est essentiellement de l'anglais simple. Les noms des [widgets](https://docs.flutter.dev/development/ui/widgets) reflètent ce qu'ils sont et leurs propriétés sont faciles à comprendre.

## Les widgets dans Flutter

Un widget est une classe Dart qui étend soit [StatefulWidget](https://api.flutter.dev/flutter/widgets/StatefulWidget-class.html) soit [StatelessWidget](https://api.flutter.dev/flutter/widgets/StatelessWidget-class.html).

Votre installation locale de [Flutter](https://docs.flutter.dev/get-started/install) est livrée avec plusieurs widgets. Pour voir les widgets disponibles par défaut, ouvrez le dossier des packages de votre installation Flutter dans votre éditeur préféré. Ensuite, recherchez dans tous les fichiers "extends StatefulWidget" et "extends StatelessWidget" et notez le nombre de résultats.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/flutter-packages-widget-count.png align="left")

À partir de [Flutter 2.10](https://docs.flutter.dev/development/tools/sdk/release-notes/release-notes-2.10.0), vous obtiendrez **408** StatefulWidgets et **272** StatelessWidgets. Cela fait un total de **680 widgets** disponibles pour que vous puissiez les utiliser et implémenter des interfaces utilisateur.

Ces widgets ont généralement tout ce dont vous avez besoin. Mais parfois, ils peuvent ne pas suffire. [pub.dev](https://pub.dev), le gestionnaire de packages de Dart et Flutter, dispose de nombreux autres widgets que vous pouvez utiliser pour implémenter des interfaces utilisateur.

Il est difficile de compter les widgets dans pub.dev. Mais en recherchant une chaîne vide (ne tapez rien dans la barre de recherche, puis appuyez sur l'icône de recherche) et en définissant le SDK sur Flutter, vous obtenez le nombre total actuel de packages publiés.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/pub.dev-widget-count.png align="left")

Au moment de la rédaction, il y a plus de 23 000 packages Flutter dans pub.dev. Chaque package contient *au moins un* widget. Cela signifie que vous avez plus de 23 000 widgets de pub.dev à implémenter, en plus des 680 disponibles. Cela signifie que vous pouvez vraiment implémenter n'importe quelle interface utilisateur que vous souhaitez facilement dans Flutter.

En plus des nombreux widgets disponibles, vous pouvez également créer vos propres widgets lors de l'implémentation des interfaces utilisateur.

## L'arborescence des widgets

Ce qui suit fait partie du code que vous obtenez lorsque vous créez un nouveau projet Flutter et supprimez les commentaires :

```dart
 @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Text(
              'Vous avez appuyé sur le bouton autant de fois :',
            ),
            Text(
              '$_counter',
              style: Theme.of(context).textTheme.headline4,
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: 'Incrémenter',
        child: const Icon(Icons.add),
      ),
    );
  }
```

Le parent `Scaffold` prend les paramètres `appBar`, `body` et `floatingActionButton`. À son tour, l'[AppBar](https://api.flutter.dev/flutter/material/AppBar-class.html) prend également un paramètre `title` qui a une valeur `Text`.

`body` prend une valeur `Center` qui a un `child` `Column`. La `Column` a à son tour deux `Text` comme `children`. Le `FloatingActionButton` prend le callback `onPressed`, le `tooltip` 'Incrémenter' et un `Icon` pour un `child`.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot--142--2.png align="left")

*Décomposition de l'arborescence des widgets Flutter*

Il s'agit d'une arborescence de widgets simple. Elle a des parents et des descendants. `child` et `children` sont des propriétés courantes de la plupart des widgets Flutter. À mesure que les widgets prennent de plus en plus d'enfants widgets, votre application se développe progressivement en une grande arborescence de widgets.

Lorsque vous implémentez des interfaces utilisateur dans Flutter, gardez à l'esprit que vous construisez une arborescence de widgets. Vous remarquerez que votre code s'indente vers l'intérieur à partir de la margelle gauche. Il semble développer une sorte de signe supérieur virtuel (d'espace vide) à gauche.

**Note :** Les niveaux d'indentation énormes sont un signe que vous devez refactoriser votre code. Cela signifie que vous devez extraire une partie de la hiérarchie des widgets dans un widget séparé.

## Comment implémenter n'importe quelle interface utilisateur dans Flutter

### 1\. Écrivez votre code en commençant en haut à gauche et descendez vers le bas à droite

Vous implémenterez l'interface utilisateur widget après widget selon la position de chaque élément dans l'interface utilisateur. Vous écrirez donc d'abord le code pour les éléments qui apparaissent en haut de l'interface utilisateur. Ensuite, vous continuerez à écrire le code pour les autres éléments en descendant la page jusqu'à atteindre le bas de cette interface utilisateur.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot--143-.png align="left")

C'est intuitif.

Sur l'axe horizontal, allez de gauche à droite. Si nécessaire, ou si c'est une interface utilisateur [de droite à gauche](https://medium.com/@carlolucera/flutter-and-directionality-d9ac42197fb8), alors implémentez-la de droite à gauche.

### 2\. Choisir un widget

Ensuite, vous devrez déterminer logiquement le widget que vous souhaitez utiliser pour un élément d'interface utilisateur donné. Au minimum, pour un élément d'interface utilisateur donné, vous utiliserez des widgets simples que vous connaissez en fonction de ce que leurs noms indiquent qu'ils font.

Il est probable que le nom de ce à quoi ressemble le composant d'interface utilisateur soit le nom du widget. Si vous avez du mal à faire un choix, une rapide recherche en ligne vous donnera les réponses. Flutter dispose d'une grande communauté en ligne.

### 3\. Utiliser des groupes de widgets

Si un groupe d'éléments d'interface utilisateur est disposé verticalement, les uns après les autres, utilisez une [Column](https://api.flutter.dev/flutter/widgets/Column-class.html). S'ils sont disposés horizontalement, les uns après les autres, utilisez une [Row](https://api.flutter.dev/flutter/widgets/Row-class.html). S'ils sont placés les uns sur les autres, utilisez une [Stack](https://api.flutter.dev/flutter/widgets/Stack-class.html), avec les widgets flottants enveloppés dans des widgets [Positioned](https://api.flutter.dev/flutter/widgets/Positioned-class.html).

#### a. Column/Row

À l'intérieur d'une Column ou d'une Row, vous pouvez changer ou ajuster la manière dont les widgets s'aligneront sur l'axe principal ou transversal. Utilisez leurs propriétés [CrossAxisAlignment](https://api.flutter.dev/flutter/rendering/CrossAxisAlignment.html) et [MainAxisAlignment](https://api.flutter.dev/flutter/rendering/MainAxisAlignment.html) pour de tels ajustements.

Pour l'axe transversal, vous pouvez aligner au centre, à la fin, au début et étirer. Pour l'axe principal, vous pouvez aligner au centre, à la fin, espacer autour, espacer entre, espacer uniformément et à la fin.

Dans une `Column`, l'axe vertical est l'axe principal tandis que l'axe horizontal est l'axe transversal. Dans une `Row`, l'axe horizontal est l'axe principal tandis que l'axe vertical est l'axe transversal.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/1Untitled-1-1.png align="left")

*Adapté de https://arzerin.com/2019/11/20/flutter-column/*

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Untitled-1.png align="left")

*Adapté de https://arzerin.com/2019/11/20/flutter-row/*

Dans les Columns et les Rows, si vous voulez qu'un widget enfant particulier prenne autant d'espace disponible que possible, enveloppez ce widget à l'intérieur d'un widget [Expanded](https://api.flutter.dev/flutter/widgets/Expanded-class.html). Si vous êtes familier avec le frontend web, vous remarquerez que les Columns et les Rows sont comme [display: flex;](https://developer.mozilla.org/en-US/docs/Web/CSS/flex) en CSS.

#### b. Widget Stack

Avec `Stack`, le ou les derniers widgets de la liste des `children` apparaissent au-dessus des enfants précédents.

Vous devrez peut-être modifier l'[alignment](https://api.flutter.dev/flutter/widgets/Stack/alignment.html) de la Stack pour indiquer les positions relatives des widgets. Comme [topCenter](https://api.flutter.dev/flutter/painting/AlignmentDirectional/topCenter-constant.html), [center](https://api.flutter.dev/flutter/painting/AlignmentDirectional/center-constant.html), [bottomEnd](https://api.flutter.dev/flutter/painting/AlignmentDirectional/bottomEnd-constant.html), et ainsi de suite.

La taille de la Stack est calculée en fonction des widgets non positionnés (widgets dans la liste des enfants non enveloppés dans un parent [Positioned](https://api.flutter.dev/flutter/widgets/Positioned-class.html)). Lors de la programmation, rappelez-vous que votre Stack doit soit avoir au moins un widget non positionné, soit être enveloppée dans un widget parent qui définit explicitement la taille de la Stack.

Positioned prend l'un ou l'autre ou tous les paramètres [bottom](https://api.flutter.dev/flutter/widgets/Positioned/bottom.html), [top](https://api.flutter.dev/flutter/widgets/Positioned/top.html), [left](https://api.flutter.dev/flutter/widgets/Positioned/left.html), [right](https://api.flutter.dev/flutter/widgets/Positioned/right.html). Ils définissent la position de l'enfant par rapport à la Stack. Les valeurs négatives déplacent l'enfant dans la direction opposée. Cependant, les valeurs négatives rognent des parties de l'enfant. Utilisez [clipBehavior: Clip.none](https://api.flutter.dev/flutter/widgets/Stack/clipBehavior.html) sur la Stack pour afficher toutes les parties du widget positionné.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screenshot--148-.png align="left")

*Code complet* [*ici*](https://gist.github.com/obumnwabude/de06d67b7e636dfb8ae1b852b97624b4)*.*

### 4\. Créer des widgets personnalisés

Lorsque vous construisez l'arborescence des widgets, vous remarquerez deux choses :

1. Soit un morceau de l'arborescence devient trop grand et constitue une unité logique à part entière.
    
2. Soit certains morceaux ou ensembles de widgets peuvent se répéter avec de légères modifications.
    

Ce sont deux indications que vous devriez [refactoriser](https://en.wikipedia.org/wiki/Code_refactoring) votre code. Cela signifie que vous devriez extraire ces widgets et les définir dans un autre fichier Dart.

Votre [éditeur de code](https://docs.flutter.dev/get-started/editor) vous aidera à refactoriser. Avec ou sans l'éditeur, tout ce que vous avez à faire est :

1. Créer un nouveau fichier Dart. Le nom du fichier doit refléter le nom du nouveau widget.
    
2. Créer une nouvelle classe qui étend StatefulWidget ou StatelessWidget, selon que le nouveau widget a un [State](https://api.flutter.dev/flutter/widgets/State-class.html) ou non.
    
3. Ensuite, retourner le morceau de widget à partir d'une méthode [build](https://api.flutter.dev/flutter/widgets/StatelessWidget/build.html).
    
4. (Facultatif) Si nécessaire, votre nouvelle classe Dart peut prendre des paramètres positionnels ou nommés dans son constructeur pour personnaliser l'apparence du widget.
    

```dart
// dans counter_display.dart
import 'package:flutter/material.dart';

class CounterDisplay extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Column(
  	  mainAxisAlignment: MainAxisAlignment.center,
      children: [
        Text('Vous avez appuyé sur le bouton autant de fois :'),
        Text('$counter', style: TextStyle(fontSize: 24)),
      ],
    );
  }
}

// dans main.dart
//
// ... 
  body: Center(child: CounterDisplay()),
// ...
```

Vous créerez de nombreux widgets personnalisés et ils deviendront à leur tour des descendants d'autres widgets personnalisés, et c'est très bien. L'arborescence des widgets est destinée à croître continuellement au fur et à mesure des besoins.

### 5\. Ajouter plus de personnalisation

Vous ne personnaliserez pas les widgets uniquement à cause de la refactorisation et des [répétitions (code DRY)](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself). Vous créerez des widgets personnalisés à cause de l'interface utilisateur que vous implémentez.

Vous créerez des widgets personnalisés car les nombreux widgets disponibles ne répondent pas toujours aux besoins exacts d'une interface utilisateur donnée. Vous devrez les combiner de manière spéciale pour implémenter une interface utilisateur particulière.

#### a. Widget Container

[Container](https://api.flutter.dev/flutter/widgets/Container-class.html) est un widget puissant. Vous pouvez le styliser de différentes manières. Si vous êtes habitué au frontend web, vous remarquerez qu'il est comme une [div](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div) en HTML.

Container est un widget de base. Vous pouvez l'utiliser pour créer n'importe quel élément d'interface utilisateur.

Certains paramètres de Container sont [constraints](https://api.flutter.dev/flutter/widgets/Container/constraints.html), [decoration](https://api.flutter.dev/flutter/widgets/Container/decoration.html), [margin](https://api.flutter.dev/flutter/widgets/Container/margin.html), [padding](https://api.flutter.dev/flutter/widgets/Container/padding.html), [transform](https://api.flutter.dev/flutter/widgets/Container/transform.html), parmi d'autres. Bien sûr, Container prend un [child](https://api.flutter.dev/flutter/widgets/Container/child.html) qui peut être n'importe quel widget.

La propriété decoration peut prendre un [BoxDecoration](https://api.flutter.dev/flutter/painting/BoxDecoration-class.html), qui à son tour peut prendre plusieurs autres propriétés. C'est le cœur de la flexibilité de Container. BoxDecoration prend des paramètres comme [border](https://api.flutter.dev/flutter/painting/BoxDecoration/border.html), [borderRadius](https://api.flutter.dev/flutter/painting/BoxDecoration/borderRadius.html), [boxShadow](https://api.flutter.dev/flutter/painting/BoxDecoration/boxShadow.html), [color](https://api.flutter.dev/flutter/painting/BoxDecoration/color.html), [gradient](https://api.flutter.dev/flutter/painting/BoxDecoration/gradient.html), [image](https://api.flutter.dev/flutter/painting/BoxDecoration/image.html), [shape](https://api.flutter.dev/flutter/painting/BoxDecoration/shape.html), parmi d'autres.

Avec ces paramètres et leurs valeurs, vous pouvez implémenter n'importe quelle interface utilisateur selon vos goûts. Vous pouvez utiliser `Container` au lieu des nombreux [widgets material](https://api.flutter.dev/flutter/material/material-library.html) que Flutter propose. Ainsi, votre application sera à votre goût.

#### b. GestureDetector / InkWell

[GestureDetector](https://api.flutter.dev/flutter/widgets/GestureDetector-class.html), comme son nom l'indique, détecte les interactions de l'utilisateur. Tous les éléments d'interface utilisateur ne sont pas des boutons. Et lors de l'implémentation des interfaces utilisateur, vous aurez besoin que certains widgets réagissent aux actions de l'utilisateur. Dans un tel cas, utilisez GestureDetector.

GestureDetector peut détecter différents types de gestes : taps, double taps, swipes, ... GestureDetector prend bien sûr un [child](https://api.flutter.dev/flutter/widgets/GestureDetector/child.html) (qui peut être n'importe quel widget), et différents callbacks pour différents gestes comme [onTap](https://api.flutter.dev/flutter/widgets/GestureDetector/onTap.html), [onDoubleTap](https://api.flutter.dev/flutter/widgets/GestureDetector/onDoubleTap.html), [onPanUpdate](https://api.flutter.dev/flutter/widgets/GestureDetector/onDoubleTap.html) (pour les swipes), ...

Note : Par défaut, lorsque les utilisateurs interagissent avec les espaces vides dans le child de GestureDetectors, les callbacks ne sont pas appelés. Si vous voulez que votre GestureDetector réagisse aux gestes sur l'espace vide (à l'intérieur de son child), alors définissez la propriété [behavior](https://api.flutter.dev/flutter/widgets/GestureDetector/behavior.html) du GestureDetector sur [HitTestBehavior.translucent](https://api.flutter.dev/flutter/rendering/HitTestBehavior.html).

```dart
GestureDetector(
  // définir le comportement pour détecter les taps sur les espaces vides
  behavior: HitTestBehavior.translucent,
  child: Column(
    children: [
      Text('J\'ai de l\'espace après moi ...'),
      SizedBox(height: 32),
      Text('... qui peut détecter les taps.'),
    ],
  ),
  onTap: () => print('Tapped on empty space.'),
)
```

[InkWell](https://api.flutter.dev/flutter/material/InkWell-class.html) est similaire à GestureDetector. Il répond à certains gestes auxquels GestureDetector répond. Cependant, il montre des effets de vague lorsqu'il est interagi (ce que GestureDetectors ne font pas).

![Image](https://www.freecodecamp.org/news/content/images/2022/06/QqEZ3.gif align="left")

*De https://stackoverflow.com/q/58285012/13644299*

InkWell doit avoir un ancêtre [Material](https://api.flutter.dev/flutter/material/Material-class.html). Donc, si votre widget le plus haut est [MaterialApp](https://api.flutter.dev/flutter/material/MaterialApp-class.html), vous n'avez pas à vous en soucier. Sinon, enveloppez l'InkWell dans un Material.

Vous devriez également faire cet enveloppement si vous changez les couleurs du parent ou de l'enfant de l'InkWell. Si vous ne le faites pas, la vague ne s'affichera pas. Vous devez également définir la [color](https://api.flutter.dev/flutter/material/Material/color.html) du widget Material pour que la vague s'affiche. Vous pouvez définir la couleur sur [Colors.transparent](https://api.flutter.dev/flutter/material/Colors/transparent-constant.html) et Flutter s'occupera du reste.

## Comment implémenter des interfaces défilantes

Le défilement est un sujet un peu délicat. Par défaut, les widgets ne défilent pas dans Flutter. Si votre Column ou Row sera défilante, utilisez une [ListView](https://api.flutter.dev/flutter/widgets/ListView-class.html) à la place. ListView prend également le paramètre children.

ListView dispose également de constructeurs de fabrique comme [ListView.builder](https://api.flutter.dev/flutter/widgets/ListView/ListView.builder.html) et [ListView.separated](https://api.flutter.dev/flutter/widgets/ListView/ListView.separated.html). Le builder vous donne plus de contrôle sur le processus de construction des enfants, tandis que le separated prend en compte un séparateur (comme [Divider](https://api.flutter.dev/flutter/material/Divider-class.html) par exemple).

Par défaut, les ListViews font défiler leurs enfants verticalement. Cependant, vous pouvez changer la [scrollDirection](https://api.flutter.dev/flutter/widgets/ScrollView/scrollDirection.html) d'une ListView en [Axis.horizontal](https://api.flutter.dev/flutter/painting/Axis.html) pour faire défiler ses enfants horizontalement.

Parfois, vous pourriez vouloir utiliser [SingleChildScrollView](https://api.flutter.dev/flutter/widgets/SingleChildScrollView-class.html) au lieu de ListView. Comme son nom l'indique, il prend un seul [child](https://api.flutter.dev/flutter/widgets/SingleChildScrollView/child.html) et il peut défiler. Vous pouvez passer des groupes de widgets comme son child.

[Il existe d'autres widgets de défilement](https://docs.flutter.dev/development/ui/widgets/scrolling).

Mais prenez une note spéciale de [CustomScrollView](https://api.flutter.dev/flutter/widgets/CustomScrollView-class.html). Il vous donne un énorme contrôle du défilement, contrairement aux autres. Il prend des [slivers](https://api.flutter.dev/flutter/widgets/CustomScrollView/slivers.html), qui à leur tour sont des widgets de défilement avec des mécanismes de défilement puissants.

[SliverFillRemaining](https://api.flutter.dev/flutter/widgets/SliverFillRemaining-class.html), [SliverFillViewport](https://api.flutter.dev/flutter/widgets/SliverFillViewport-class.html), [SliverGrid](https://api.flutter.dev/flutter/widgets/SliverGrid-class.html), [SliverList](https://api.flutter.dev/flutter/widgets/SliverList-class.html), [SliverPersistentHeader](https://api.flutter.dev/flutter/widgets/SliverPersistentHeader-class.html) parmi d'autres, sont des exemples de widgets que vous incluez dans la liste des slivers. La plupart de ces widgets prennent un delegate, qui gère la manière dont le défilement se produit.

Un bon cas d'utilisation de CustomScrollView est avec [SliverAppBar](https://api.flutter.dev/flutter/material/SliverAppBar-class.html), où vous voulez que l'AppBar soit étendue par défaut et réduite lors du défilement.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/ap.gif align="left")

Un autre exemple pourrait être avec un [DraggableScrollableSheet](https://api.flutter.dev/flutter/widgets/DraggableScrollableSheet-class.html) où vous gardez certains boutons d'action collés en bas.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/bs.gif align="left")

## À propos de CustomPaint

C'est là que Flutter a donné une flexibilité ultime au monde de l'interface utilisateur.

[CustomPaint](https://api.flutter.dev/flutter/widgets/CustomPaint-class.html) est à Flutter ce que l'API Canvas est à HTML ou SVG est aux images.

CustomPaint est un widget dans Flutter qui vous donne la capacité de concevoir et de dessiner sans limitations. Il vous donne une toile sur laquelle vous pouvez dessiner avec un [painter](https://api.flutter.dev/flutter/widgets/CustomPaint/painter.html).

![Image](https://www.freecodecamp.org/news/content/images/2022/06/visualizer.gif align="left")

*De https://blog.codemagic.io/flutter-custom-painter/*

Vous utiliserez rarement CustomPaint. Mais soyez conscient qu'il existe. Parce qu'il pourrait y avoir des interfaces utilisateur très complexes que les combinaisons de widgets ne pourraient pas implémenter et vous n'aurez d'autre choix que de dessiner avec `CustomPaint`.

Lorsque ce moment viendra, ce ne sera pas difficile pour vous car vous êtes déjà familier avec d'autres widgets.

## Résumé

Pour un élément d'interface utilisateur donné, choisissez un widget, écrivez son code, construisez le widget avec d'autres widgets et voyez quelle grande interface utilisateur vous implémentez avec Flutter.

L'implémentation des interfaces utilisateur est une partie majeure du développement d'applications mobiles, web et de bureau. Flutter est une boîte à outils d'interface utilisateur qui construit des applications multiplateformes pour ces plateformes. La nature déclarative de Flutter et son abondance de widgets rendent l'implémentation des interfaces utilisateur simple.

Continuez à implémenter des interfaces utilisateur dans Flutter. En le faisant, cela deviendra une seconde nature pour vous. Et vous serez en mesure d'implémenter n'importe quelle interface utilisateur dans Flutter.