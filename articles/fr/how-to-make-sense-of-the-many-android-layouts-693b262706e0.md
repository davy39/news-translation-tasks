---
title: Comment comprendre les nombreux layouts Android
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2018-12-03T21:32:37.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-sense-of-the-many-android-layouts-693b262706e0
coverImage: https://cdn-media-1.freecodecamp.org/images/0*XavhDgkHntuMq9Ib
tags:
- name: Android
  slug: android
- name: coding
  slug: coding
- name: development
  slug: development
- name: 'tech '
  slug: tech
- name: UI
  slug: ui
seo_title: Comment comprendre les nombreux layouts Android
seo_desc: 'Linear, Relative, Constraint, Table, Frame and so on and so forth. Android
  applications have a whole bunch of layouts to choose from when you want to design
  your application. The question is, which one is the best?

  Before we go into detailing the dif...'
---

Linéaire, Relatif, Contrainte, Table, Frame et ainsi de suite. Les applications Android ont tout un ensemble de layouts parmi lesquels choisir lorsque vous souhaitez concevoir votre application. **La question est, lequel est le meilleur ?**

Avant de détailler les différents layouts, nous allons d'abord passer en revue la hiérarchie des objets de vue et le processus de dessin d'Android.

### View et ViewGroup

Considérez ViewGroup comme la classe parente de toute vue et également comme la classe de base pour les layouts. Il représente un objet qui est le conteneur pour d'autres vues. Par exemple, un **LinearLayout** est un **ViewGroup** puisqu'il peut contenir des vues et d'autres layouts également.

View, en revanche, est le bloc de construction de base des éléments d'interface utilisateur. Les vues peuvent faire partie d'un ViewGroup. Par exemple, un **TextView** est une **View**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*AwYBLMUOXQb_tegG6uO5rg.jpeg)
_Une hiérarchie de ViewGroup et View_

### Mesure -> Layout -> Dessin -> Répéter

Les layouts sont enregistrés sous forme de fichiers [XML](https://whatis.techtarget.com/fileformat/XML-eXtensible-markup-language) dans Android. Mais comment sont-ils convertis en objets que nous voyons à l'écran ? Chaque fichier XML est instancié (lire : gonflé) et un arbre de hiérarchie de vues est formé. Cela signifie que si vous avez un layout B qui est imbriqué dans le layout A, ils auront une relation parent-enfant (le layout A est le parent du layout B). Une fois l'arbre formé, il y a 3 phases qui se produiront : Mesure, Layout et Dessin. Chacune de ces phases parcourt l'arbre dans un ordre de [Recherche en Profondeur](https://en.wikipedia.org/wiki/Depth-first_search).

#### Mesure

Dans la première phase, chaque nœud parent détermine certaines contraintes que ses enfants ont concernant leur taille. Il transmet ces limitations vers le bas à ses enfants, où chaque enfant évaluera sa propre taille (la taille qu'il souhaite avoir) et prendra en considération les limitations qui lui ont été données et les limitations de ses enfants.

#### Layout

Ici, chaque nœud décidera de la taille finale et de la position de chacun de ses enfants à l'écran.

#### Dessin

En commençant par le nœud racine, qui se dessine lui-même, il demande ensuite à ses enfants de se dessiner eux-mêmes. De cette manière, ce qui se passe, c'est qu'un parent sera dessiné et ses enfants seront dessinés par-dessus.

> _En gardant à l'esprit le processus ci-dessus, vous devriez essayer de garder la hiérarchie de votre application aussi plate que possible afin de réduire le temps nécessaire pour parcourir la hiérarchie des vues_

![Image](https://cdn-media-1.freecodecamp.org/images/0*avZ1dpBsBuTW36Xt)
_"assorted-color photo frame lot" par [Unsplash](https://unsplash.com/@markusspiske?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Markus Spiske</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

### Analyse des Layouts

#### Linéaire

Organise ses enfants en une ligne avec une orientation verticale ou horizontale. Cela signifie que les vues seront soit toutes dans une ligne, soit dans une colonne. Vous pouvez spécifier la direction en utilisant l'attribut **android:orientation**.

Une caractéristique intéressante d'un Linear Layout est l'attribut **layout_weight**. Cela est utilisé pour indiquer au Linear Layout comment diviser l'espace entre les vues enfants. Il est utile lorsque vous souhaitez que votre layout soit cohérent parmi les appareils et les orientations.

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Bonjour"
        />

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Monde !"
        />

</LinearLayout>
```

Supposons que vous souhaitiez que le premier TextView, contenant le mot _Bonjour_, prenne toujours 3/4 de la largeur de l'écran. Pour ce faire, nous pouvons utiliser l'attribut layout_weight.

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:layout_weight="4"        // <-- Nous avons ajouté un poids total pour notre layout (4)
    tools:context=".MainActivity">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_weight="3"   // <-- Aura un poids de 3 sur 4 (3/4)
        android:text="Bonjour" />

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Monde !"
        android:layout_weight="1"   // <-- Aura un poids de 1 sur 4 (1/4)
        />

</LinearLayout>
```

#### Relatif

Comme son nom l'indique, ce layout positionnera ses vues enfants de manière relative. Cela peut garder votre hiérarchie de layout plate sans groupes de vues imbriqués. En même temps, cependant, chaque Relative Layout doit subir un processus de deux passes de Mesure, ce qui peut affecter les performances.

Une caractéristique utile d'un RelativeLayout est la capacité de centrer une vue enfant en utilisant l'attribut **centerInParent**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cZwvkUglSVr3oWDmFddnZQ.jpeg)
_layout_centerInParent centre le TextView_

#### Contrainte

Une _contrainte_ est une connexion ou un alignement avec l'élément auquel la contrainte est liée. Vous définissez diverses contraintes pour chaque vue enfant par rapport aux autres vues présentes. Cela vous donne la capacité de construire des layouts complexes avec une hiérarchie de vues plate (pas de ViewGroups imbriqués). Similaire au RelativeLayout, ce layout nécessite également deux passes de Mesure.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TCpUhPhDviNMOdjhnSonYw.jpeg)
_Remarquez les contraintes sur le TextView_

#### Frame

Ce layout est utilisé uniquement pour contenir une seule vue enfant, bloquant ainsi toute autre vue dans le layout. Le layout lui-même sera aussi grand que sa plus grande vue enfant (visible ou non), plus un peu de remplissage.

Évitez d'avoir plusieurs vues enfants à l'intérieur d'un FrameLayout puisque cela rendra difficile l'éviter que les vues enfants se chevauchent. Vous pouvez contrôler les positions de ces vues enfants en attribuant l'attribut **layout_gravity** à chaque enfant.

![Image](https://cdn-media-1.freecodecamp.org/images/1*BLf1yC1vhGgWaVLa7YT-3w.jpeg)

#### List View/Grid View

À utiliser lorsque vous avez besoin de présenter plusieurs éléments à l'écran (comme dans un menu de restaurant). List View est une liste à une seule colonne que l'utilisateur peut faire défiler. Vous pouvez considérer Grid View comme une List View avec plus d'une colonne.

Ce qui est important à savoir sur ces layouts, c'est que les vues sont dynamiques et créées à l'exécution. Pour faire en sorte que les éléments soient peuplés à l'exécution, vous devez utiliser un [AdapterView](https://developer.android.com/reference/android/widget/AdapterView).

![Image](https://cdn-media-1.freecodecamp.org/images/1*T6XG2VZ1kpJrx8g9VZS-xg.jpeg)
_Vous pouvez spécifier l'emplacement de chaque élément dans le layout en utilisant layout_column et layout_row_

#### TableLayout

Très similaire à Grid View, ce layout organise ses enfants en lignes et colonnes. Chaque layout contiendra plusieurs objets TableRow, chacun définissant une ligne.

![Image](https://cdn-media-1.freecodecamp.org/images/1*IxB5s08Z_w-3gKq-DT564A.jpeg)
_Nous avons deux éléments TableRow_

N'ayez pas peur d'essayer différents layouts jusqu'à ce que vous trouviez celui qui fonctionne le mieux pour vous. N'hésitez pas à me faire savoir dans les commentaires ci-dessous quel layout est le plus utile pour vous et pourquoi.