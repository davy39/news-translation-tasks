---
title: Créer des adapteurs Android Recyclerview comme un pro avec MultiViewAdapter
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-09T18:26:56.000Z'
originalURL: https://freecodecamp.org/news/introducing-multiviewadapter-7f77e5758d3f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*43Kdmm5GaK-E_T29a1Csew.jpeg
tags:
- name: Android
  slug: android
- name: android app development
  slug: android-app-development
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Créer des adapteurs Android Recyclerview comme un pro avec MultiViewAdapter
seo_desc: 'By Riyaz Ahamed

  RecyclerView is an important widget in the Android framework and a large percentage
  of the Android apps out there use it. It’s a powerful tool that covers many generic
  use-cases. However, because of this flexibility, there’s a bit of ...'
---

Par Riyaz Ahamed

RecyclerView est un widget important dans le framework Android et une grande partie des applications Android l'utilisent. C'est un outil puissant qui couvre de nombreux cas d'utilisation génériques. Cependant, en raison de cette flexibilité, il faut un peu de travail pour créer un adaptateur.

Le support pour plusieurs types de vues était l'un des avantages de RecyclerView par rapport à la liste classique. Mais l'affichage de plusieurs types de vues nécessite beaucoup de code standard. Cela peut rapidement devenir ingérable si vous avez plus de trois types de vues. Vous pouvez avoir plusieurs conditions if-else, des cas de commutation, etc. Malheureusement, il n'existe pas de moyen facile de réutiliser le code de création et de liaison des viewholders.

MultiViewAdapter est conçu pour résoudre exactement ce problème. Il existe déjà un certain nombre de solutions disponibles, mais ces bibliothèques ont quelques restrictions :

1. Vos objets de données doivent avoir un parent commun, ce qui peut interférer avec votre modélisation d'objets.
2. Vous êtes obligé de garder l'ID de ressource de mise en page à l'intérieur de la classe de modèle elle-même. Encore une fois, cela rompt la hiérarchie des dépendances.
3. Vous êtes autorisé à gérer vous-même l'ID de type de vue. Habituellement, l'ID de ressource de mise en page est retourné comme type de vue. Vous ne pouvez donc pas utiliser le même fichier de mise en page pour deux types de vues différents.
4. Ils ne tirent pas parti de DiffUtil.
5. Vous devez écrire des cas de commutation, si vous souhaitez avoir différentes décorations d'éléments/taille de span/modes de sélection pour différents types de vues.

MultiViewAdapter résout toutes ces exigences. La bibliothèque a été spécialement conçue de manière à ne pas interférer avec votre modélisation d'objets et votre hiérarchie.

### Code source

[**DevAhamed/MultiViewAdapter**](https://github.com/DevAhamed/MultiViewAdapter)  
[_MultiViewAdapter - Bibliothèque d'adaptateurs Recyclerview pour créer des view holders composables_github.com](https://github.com/DevAhamed/MultiViewAdapter)

Voici un aperçu de ce que vous pouvez réaliser avec la bibliothèque.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NFAKaiXUb5AXZfwGVFZ2JA.gif)
_Multiples types de vues, décorations d'éléments personnalisées pour différents types de vues, diffutil, etc._

### Fonctionnalités

1. Aucune restriction sur la façon dont vous modélisez vos classes d'objets et leur hiérarchie.
2. Support intégré pour DiffUtil.
3. Prend en charge la sélection unique et la multi-sélection.
4. Chaque type de vue peut avoir son propre nombre de spans ou ItemDecoration, entre autres. Vous n'avez pas besoin de cas de commutation ou de conditions if-else.

### Comment l'utiliser

Ajoutez la dépendance dans le fichier gradle de votre application.

### Concepts derrière MultiViewAdapter

![Image](https://cdn-media-1.freecodecamp.org/images/1*xUtA2hYJeyOcHeqao_ExTA.jpeg)

1. **RecyclerAdapter** — Il s'agit de la classe d'adaptateur. Elle peut avoir plusieurs ItemBinder et DataManagers. Elle étend l'adaptateur officiel RecyclerView.
2. **ItemBinder** — La responsabilité de l'ItemBinder est de créer et de lier les viewholders. ItemBinder a un paramètre de type qui accepte la classe de modèle à afficher. ItemBinder doit être enregistré dans RecyclerAdapter. ItemBinder peut être enregistré avec plusieurs adapteurs.
3. **DataManger** — Il contient les données et appelle les animations nécessaires lorsque le jeu de données est modifié. Il existe deux DataManagers. **DataListManager** pour une liste d'éléments. **DataItemManager** pour un seul élément (en-tête, pied de page, etc.).

### Création d'adaptateurs simples

![Image](https://cdn-media-1.freecodecamp.org/images/1*g4yON409_UBDcl_0uK7lCQ.jpeg)
_MultiViewAdapter avec une liste d'éléments_

Vous avez une liste d'objets, disons des 'Voitures'. Si vous souhaitez afficher une liste de voitures, voici le code complet.

Maintenant, vous êtes prêt à partir. Vous pouvez utiliser l'adaptateur, `CarAdapter carAdapter = new CarAdapter();` et le définir pour recyclerview. C'est tout.

Vous avez peut-être remarqué qu'avec l'approche traditionnelle, nous créons toujours une seule classe `CarAdapter`. Mais en utilisant la bibliothèque, vous devez créer deux classes — `CarAdapter` et `CarBinder`. L'idée ici est que vous pouvez réutiliser le `CarBinder` dans d'autres adapteurs également, par exemple `VehicleAdapter`.

### Utilisation de GridLayoutManager

![Image](https://cdn-media-1.freecodecamp.org/images/1*sxgwzTrn7jBYdOuyVER3dg.jpeg)
_MultiViewAdapter avec des éléments de grille_

Vous n'avez pas besoin de différents adapteurs lorsque vous affichez une grille d'éléments. Vous pouvez remplacer `getSpanSize(int maxSpanCount)` dans votre classe ItemBinder et retourner le nombre de spans.

Maintenant, obtenez la recherche de taille de span à partir de l'adaptateur et définissez-la pour votre GridLayoutManager.

### Pour différents nombres de spans

![Image](https://cdn-media-1.freecodecamp.org/images/1*3Fi3p7ZYvvOQqkPt3_mrYA.jpeg)
_Prend en charge différents nombres de spans pour chaque type de vue_

Pas de soucis ici. Par défaut, chaque ItemBinder retourne 1 comme nombre de spans. Donc, si vous souhaitez un nombre de spans différent de celui par défaut, vous pouvez remplacer la méthode getSpanSize et retourner le nombre de spans nécessaire.

### Décoration d'élément personnalisée

![Image](https://cdn-media-1.freecodecamp.org/images/1*kX-yg-0eZKxyfA6oxQsjkg.jpeg)
_Prend en charge la décoration d'élément personnalisée pour chaque type de vue_

C'est la partie délicate. C'est encore plus délicat lorsque vous n'utilisez pas cette bibliothèque. Il y a trois étapes pour créer une décoration d'élément par type de vue.

1. Créez une classe de décoration d'élément personnalisée en étendant ItemDecorator.

2. Lors de la création de l'ItemBinder, passez l'objet de décoration d'élément personnalisé via le constructeur.

3. Maintenant, obtenez la décoration d'élément à partir de l'adaptateur et ajoutez-la à votre recyclerview.

C'est tout pour la partie délicate. Ouf.

### DiffUtil et charge utile personnalisée

MultiViewAdapter gère DiffUtil par défaut. Si vous souhaitez passer les charges utiles pendant l'opération diffutil, vous devez passer l'objet de PayloadProvider via le constructeur. Pour en savoir plus sur diffutil, lisez [ici](https://developer.android.com/reference/android/support/v7/util/DiffUtil.html).

### **Rendre un adaptateur sélectionnable**

![Image](https://cdn-media-1.freecodecamp.org/images/1*lS_UNTtEceK3qVWvprFdUw.jpeg)
_Les éléments peuvent être sélectionnés_

MultiViewAdapter prend en charge trois options de sélection différentes :

1. Sélection unique — Un seul élément peut être sélectionné. Une fois qu'un élément est sélectionné, il ne peut pas être désélectionné sauf si un autre élément est sélectionné.
2. Sélection unique ou aucune — Un seul élément peut être sélectionné. Un élément peut être désélectionné en effectuant la même opération de sélection.
3. Multi-sélection — Plusieurs éléments peuvent être sélectionnés dans différents DataManagers.

Pour rendre un adaptateur sélectionnable, vous devez utiliser les contreparties "Selectable" de Adapter, ItemBinder et ViewHolder. Par exemple, vous pourriez utiliser SelectableAdapter, SelectableBinder et SelectableViewHolder.

Prenons l'exemple de CarAdapter et rendons-le sélectionnable.

Notes :

1. Il n'est pas nécessaire que tous les ItemBinders soient sélectionnables. Par exemple, si vous avez des en-têtes dans une liste, ils ne peuvent pas être sélectionnables. Étendez donc HeaderBinder à partir de l'ItemBinder normal.
2. Vous pouvez réutiliser n'importe quel binder sélectionnable à l'intérieur de l'adaptateur normal. Il ne sera pas sélectionnable. Pour qu'un élément soit sélectionnable, l'adaptateur et le binder doivent être étendus à partir de leurs contreparties Selectable.
3. Par défaut, lors d'un appui long, un élément sera sélectionné. Si vous souhaitez que l'élément soit sélectionné, vous pouvez appeler `itemSelectionToggled()` à l'intérieur de ViewHolder.
4. Vous pouvez définir ou obtenir les éléments sélectionnés à partir du DataListManager en utilisant `getSelectedItems()` et `setSelectedItems(List<E>` items)

### Écouteurs

Les ViewHolders ont deux écouteurs : OnItemClickListener et OnItemLongClickListener.

DataListManager a un ItemSelectionChangedListener et un MultiSelectionChangedListener. Ces écouteurs peuvent être utilisés avec SelectableAdapter.

### **Remarques finales**

Merci d'avoir lu ! J'espère que cet article vous aidera à commencer avec la bibliothèque MultiViewAdapter. La bibliothèque elle-même est en développement actif et j'ai des plans pour ajouter quelques fonctionnalités passionnantes. Vous pouvez surveiller le dépôt sur GitHub pour recevoir des notifications. De plus, vous pouvez consulter la feuille de route de la bibliothèque sur [GitHub](https://github.com/DevAhamed/MultiViewAdapter).

Si vous avez des questions, des problèmes ou des demandes de fonctionnalités concernant la bibliothèque, vous pouvez me contacter via [Twitter](https://twitter.com/DevAhamed).

Pour aider les autres, veuillez cliquer sur ❤ pour recommander cet article et mettre une étoile à la [bibliothèque](https://github.com/DevAhamed/MultiViewAdapter) si vous l'avez trouvée utile.

Tout le code apparaissant dans cet article et la bibliothèque est sous licence [Apache-2.0](http://www.apache.org/licenses/LICENSE-2.0). Écrit par [Riyaz Ahamed](https://twitter.com/DevAhamed) avec ❤ de Bengaluru, Inde.