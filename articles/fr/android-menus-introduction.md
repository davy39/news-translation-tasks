---
title: Une introduction aux menus Android
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2019-04-03T21:30:00.000Z'
originalURL: https://freecodecamp.org/news/android-menus-introduction
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca3ad740569d1a4ca5d36.jpg
tags:
- name: android app development
  slug: android-app-development
- name: androiddev
  slug: androiddev
seo_title: Une introduction aux menus Android
seo_desc: "There are three types of menus in Android: Popup, Contextual and Options.\
  \ \nEach one has a specific use case and code that goes along with it. To learn\
  \ how to use them, read on.\nEach menu must have an XML file related to it which\
  \ defines its layout. T..."
---

Il existe trois types de menus dans Android : Popup, Contextuel et Options. 

Chacun a un cas d'utilisation spécifique et du code qui l'accompagne. Pour apprendre à les utiliser, continuez votre lecture.

Chaque menu doit avoir un fichier XML associé qui définit sa disposition. Voici les balises associées à l'option de menu :

`<menu>` - Il s'agit de l'élément conteneur pour votre menu (similaire à LinearLayout)

`<item>` - Cela désigne un élément et est imbriqué à l'intérieur de la balise menu. Notez qu'un élément item peut contenir un élément `<menu>` pour représenter un sous-menu

`<group>` - Cela est utilisé pour signifier une certaine propriété ou fonctionnalité à plusieurs éléments de menu (par exemple, état/visibilité)

```xml
<?xml version="1.0" encoding="utf-8"?>
<menu xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:actionProviderClass="http://schemas.android.com/tools">
    <item android:id="@+id/item1"
        android:icon="@drawable/ic_baseline_check_circle_24px"
        android:title="item1"
        app:showAsAction="always"
        />
    <item android:id="@+id/item2"
        android:icon="@drawable/ic_baseline_copyright_24px"
        android:title="item2"
        app:showAsAction="always"
        />
    <item android:id="@+id/item3"
        android:icon="@drawable/ic_baseline_favorite_24px"
        android:title="item3"
        app:showAsAction="always">
    </item>
</menu>
```

Comme montré dans l'extrait de code ci-dessus, chaque élément de menu a divers attributs associés. Je vais détailler les principaux ici, mais si vous voulez voir ce que vous pouvez ajouter d'autre, allez [ici](https://developer.android.com/guide/topics/resources/menu-resource.html).

* **id** - Il s'agit d'un identifiant unique pour l'élément dans le menu. Vous pouvez l'utiliser pour voir exactement quel élément l'utilisateur a cliqué
* **icon** - Si vous voulez afficher une icône associée à cet élément de menu
* **title** - Texte qui sera affiché dans le menu pour cet élément
* **showAsAction** - Cet attribut ne doit être utilisé que lorsque vous utilisez un menu dans une activité qui utilise une [barre d'application](https://developer.android.com/training/appbar/index.html)(ou comme on l'appelle aussi, la barre d'action). Il contrôle quand et comment cet élément doit apparaître comme une action dans la barre d'application. Il y a cinq valeurs : always, never, ifRoom, withText, et collapseActionView

```xml
android:showAsAction="always|never|ifRoom|withText|collapseActionView"

```

Je vais élaborer sur la signification de chacune de ces valeurs dans la section suivante.

De plus, vous devez ajouter la méthode de menu onCreate pertinente à votre activité.

```java
//Menu Options
@Override
public boolean onCreateOptionsMenu(Menu menu) {
    MenuInflater inflater = getMenuInflater();
    inflater.inflate(R.menu.options_menu, menu);
    return super.onCreateOptionsMenu(menu);
}

//Menu Contextuel
@Override
public void onCreateContextMenu(ContextMenu menu, View v,
                                ContextMenu.ContextMenuInfo menuInfo) {
  super.onCreateContextMenu(menu, v, menuInfo);
  MenuInflater inflater = getMenuInflater();
  inflater.inflate(R.menu.context, menu);
}
```

## Menu Options

Ce menu se trouve généralement en haut de votre application et vous devez y placer des actions qui affectent l'application dans son ensemble. Il peut s'agir des paramètres de l'application ou d'une boîte de recherche.

En utilisant la disposition de menu ci-dessus, nous obtenons le menu options suivant :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/1_OAoK8LfsBWCcfQmuZ-tYJQ.jpeg)

Comme promis, passons en revue les valeurs qui peuvent être données pour l'attribut showAsAction :

* always - sera toujours affiché dans la barre d'action
* never - ne sera jamais affiché, et sera donc disponible via le [menu de débordement](https://www.techotopia.com/index.php/Creating_and_Managing_Overflow_Menus_on_Android)
* ifRoom - uniquement s'il y a suffisamment d'espace dans la barre d'action, alors il sera affiché. Gardez à l'esprit que selon la documentation, il y a une limite au nombre d'icônes que vous pouvez avoir sur la barre d'action.
* withText - inclura le titre de l'élément dans la barre d'action
* collapseActionView - si cet élément a une vue d'action associée, il deviendra pliable (à partir de l'API 14 et au-dessus)

Si nous changeons le dernier élément de notre menu en **_showAsAction="never"_**, nous obtenons ce qui suit :

![Image for post](https://miro.medium.com/max/789/1*D_7gZSLnlahTs1hCna76mw.jpeg)
_Le troisième élément de menu a été déplacé vers le menu de débordement_

## Menu Contextuel

Ce menu apparaît lorsque l'utilisateur effectue un clic long sur l'un de vos éléments d'interface utilisateur. Les options trouvées dans ce menu affectent l'élément d'interface utilisateur sur lequel l'utilisateur a cliqué. Il est courant d'utiliser ce type de menu dans les vues de liste ou de grille, où l'interaction de l'utilisateur avec chaque élément peut conduire à une action spécifique.

_Imaginez un scénario où vous avez une application avec une image, et vous voulez présenter à l'utilisateur plusieurs choix lorsqu'ils cliquent sur l'image._

Un menu contextuel peut apparaître de deux manières :

1. Un menu flottant
2. Une barre d'action en haut de votre application

Nous ne démontrerons que l'utilisation de la première option, mais vous pouvez en lire plus sur la deuxième option [ici](https://developer.android.com/guide/topics/ui/menus#CAB).

En utilisant le XML suivant :

```xml
<?xml version="1.0" encoding="utf-8"?>
<menu xmlns:android="http://schemas.android.com/apk/res/android">
    <item
        android:id="@+id/share"
        android:title="Partager"/>
    <item
        android:id="@+id/Mail"
        android:title="Mail"/>
    <item
        android:id="@+id/MoreInfo"
        android:title="Plus d'informations"/>
</menu>
```

Et en ajoutant le code suivant à notre activité principale :

```java
 @Override
    protected void onCreate(Bundle savedInstanceState) {
       super.onCreate(savedInstanceState);
       setContentView(R.layout.activity_main);
       TYPE_OF_LAYOUT layout = (TYPE_OF_LAYOUT)findViewById(R.id.main_layout);
       registerForContextMenu(layout);
  }
```

Nous obtiendrons ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/1_knvV4O1gDMNiW0n8z6TahQ.png)
_Lorsque vous effectuez un clic long sur le texte, le menu contextuel apparaît_

## Menu Popup

Un menu popup est un type de menu qui affiche les éléments dans une liste verticale. Cette liste est attachée à la vue sur laquelle l'utilisateur a cliqué pour invoquer ce menu. Il est important de garder à l'esprit que, lors du choix d'un menu popup, vous ne voulez pas que le choix de l'utilisateur affecte le contenu précédent que l'utilisateur a pressé.

Nous utiliserons la même disposition de menu XML que précédemment, mais nous devrons ajouter le code suivant à notre activité :

```java
void showPopupMenu(View view) {
  PopupMenu popup = new PopupMenu(this, view);
  MenuInflater inflater = popup.getMenuInflater();
  inflater.inflate(R.menu.actions, popup.getMenu());
  popup.show();
}
```

Nous obtiendrons le même résultat que la capture d'écran précédente, mais sans que l'utilisateur ait besoin d'effectuer un clic long.

## Icônes dans les menus Popup

Maintenant, je sais ce que vous cherchez probablement : **_vous voulez savoir comment ajouter des icônes aux menus_**.

Bien que je vais montrer un exemple de comment faire cela, il est judicieux de comprendre que cette fonctionnalité n'est pas activée pour les menus popup et peut causer un comportement inattendu. Vous pouvez y parvenir en utilisant la réflexion pour activer un indicateur appelé **setForceShowIcon**.

```java
//popup est une instance de PopupMenu

try {
      Field[] fields = popup.getClass().getDeclaredFields();
      for (Field field : fields) {
          if ("mPopup".equals(field.getName())) {
              field.setAccessible(true);
              Object menuPopupHelper = field.get(popup);
              Class<?> classPopupHelper = Class.forName(menuPopupHelper
                      .getClass().getName());
              Method setForceIcons = classPopupHelper.getMethod(
                      "setForceShowIcon", boolean.class);
              setForceIcons.invoke(menuPopupHelper, true);
              break;
          }
      }
  } catch (Throwable e) {
      e.printStackTrace();
  }
```

![Image](https://www.freecodecamp.org/news/content/images/2020/07/1__UE6Zw86AlJ50OD6Gj2L7w.jpeg)

J'ai à peine effleuré la surface des menus Android, mais j'espère que cela est suffisant pour vous inspirer à creuser plus profondément.