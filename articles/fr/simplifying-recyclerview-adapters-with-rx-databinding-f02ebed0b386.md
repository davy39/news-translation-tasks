---
title: Simplifier les adaptateurs RecyclerView avec Rx et Databinding
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-12-10T16:03:17.000Z'
originalURL: https://freecodecamp.org/news/simplifying-recyclerview-adapters-with-rx-databinding-f02ebed0b386
coverImage: https://cdn-media-1.freecodecamp.org/images/1*q63b1qjfmWKwQt_MPjYhDQ.png
tags:
- name: Android
  slug: android
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: 'RecyclerView  '
  slug: recyclerview
- name: RxAndroid
  slug: rxandroid
seo_title: Simplifier les adaptateurs RecyclerView avec Rx et Databinding
seo_desc: 'By Ahmed Rizwan

  I recently wanted to dive deeper into Rx. So I experimented with Rx and the RecyclerView
  Adapters, and the results were pretty interesting!

  With Rx in mind, I set out to accomplish three things:


  Create a RecyclerView adapter which sh...'
---

Par Ahmed Rizwan

J'ai récemment voulu approfondir mes connaissances en Rx. J'ai donc expérimenté avec Rx et les adaptateurs RecyclerView, et les résultats étaient assez intéressants !

Avec Rx en tête, je me suis fixé trois objectifs :

1. Créer un adaptateur RecyclerView qui doit être **générique** — une seule classe d'adaptateur pour les gouverner tous !
2. Il doit retourner des **bindings** sous forme de flux Rx !
3. Il doit également y avoir une option pour supporter plusieurs types d'éléments !

Maintenant, vous pourriez penser : ce n'est pas vraiment nécessaire. Je veux dire, pourquoi utiliser Rx en premier lieu avec les RecyclerAdapters ? Et pourquoi exactement avez-vous besoin de bindings sous forme de flux Rx ?

Eh bien, c'est vrai. Personnellement, je pensais que ce serait une bonne expérience d'incorporer Rx dans les adaptateurs RecyclerView, au lieu d'utiliser des callbacks ou des délégués simples. C'était donc un peu expérimental.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6oS0HYL3OOVu9b4PupalmA.gif)

J'ai donc écrit une bibliothèque appelée [**RxRecyclerAdapter**](https://github.com/ahmedrizwan/RxRecyclerAdapter) pour faire fonctionner Rx avec les adaptateurs. Décomposons comment elle simplifie l'utilisation des adaptateurs recycler.

#### RxDataSource simplifie l'utilisation de RxRecyclerAdapter

Supposons que vous avez une belle liste de chaînes que vous voulez afficher :

```
//Dummy DataSetdataSet = new ArrayList<>();dataSet.add("this");dataSet.add("is");dataSet.add("an");dataSet.add("example");dataSet.add("of rx!");
```

Voici ce que vous feriez :

1. Activez la liaison de données en ajoutant ceci dans build.gradle

```
dataBinding {      enabled = true}
```

2. créez le fichier de mise en page pour l'élément :

```
&lt;?xml version="1.0" encoding="utf-8"?>&lt;layout xmlns:android="http://schemas.android.com/apk/res/android"        xmlns:tools="http://schemas.android.com/tools">    <LinearLayout        android:layout_width="match_parent"        android:layout_height="match_parent"        android:orientation="vertical"        android:padding="@dimen/activity_horizontal_margin">        <;TextView android:id="@+id/textViewItem"                  android:layout_width="match_parent"                  android:layout_height="wrap_content"                  tools:text="Recycler Item"/>    </LinearLayout></layout>
```

3. Créez une instance de **RxDataSource** en lui indiquant le type de dataSet :

```
RxDataSource&lt;String> rxDataSource = new RxDataSource<>(dataSet);
```

4. Composez et appelez bindRecyclerView (en passant le RecyclerView et la mise en page) avec LayoutBinding. Grâce au casting, viewHolder peut déduire le type de binding.

```
rxDataSource  .map(String::toLowerCase)  .repeat(10)  .&lt;ItemLayoutBinding>bindRecyclerView(recyclerView,                               R.layout.item_layout)  .subscribe(viewHolder -> {         ItemLayoutBinding b = viewHolder.getViewDataBinding();         b.textViewItem.setText(viewHolder.getItem());  });
```

Le résultat sera...

![Image](https://cdn-media-1.freecodecamp.org/images/1*T10QOX-L1dbfFlr8UCiAOg.png)

Notez que l'appel à observeOn(AndroidSchedulers.mainThread()) serait inutile ici, car vous êtes déjà sur le mainThread. Et lorsque vous l'appelez, cela provoque un délai d'environ ~20-30 millisecondes dans le flux, ce qui réduirait votre taux de rafraîchissement.

Maintenant, pour un exemple un peu plus pratique.

Supposons que vous voulez mettre à jour dynamiquement le dataSet. Supposons que vous voulez rechercher dans le dataSet et filtrer les résultats spécifiques. Voici comment cela serait fait :

```
RxTextView.afterTextChangeEvents(searchEditText).subscribe(event -> {  rxDataSource.updateDataSet(dataSet)       .filter(s -> s.contains(event.view().getText()))      .updateAdapter();});
```

En combinaison avec [RxBindings](https://github.com/JakeWharton/RxBinding) (parce que RxBindings sont géniaux), je m'inscris aux événements de changement de texte. Et lorsque l'événement se produit, je mets à jour le DataSet avec le **dataSet de base !**

C'est important car le RxDataSource change son instance de dataSet lorsque j'appelle des méthodes comme _filter_, _map_ et ainsi de suite. Donc, le filtrage doit être fait sur le **dataSet original**, et non sur celui modifié. Et... bam !

![Image](https://cdn-media-1.freecodecamp.org/images/1*uMxIbKfiEySpqx027Ilh3A.gif)

J'ai rencontré quelques limitations — l'une étant que vous ne pouvez pas changer le **type** de dataSet après qu'il ait été lié avec la source de données. Donc, les fonctions comme _map_ et _flatmap_ ne peuvent pas retourner un type de dataSet différent. Mais je n'ai pas encore rencontré de situation où j'avais besoin de pouvoir changer le dataSet à l'exécution.

#### RxRecyclerAdapter simplifie les situations où vous avez plusieurs types d'éléments

Maintenant, supposons que vous vouliez plusieurs types d'éléments dans votre RecyclerView, par exemple un en-tête et un type d'élément. Alors vous feriez :

1. Créez une liste de **ViewHolderInfo** spécifiant toutes les mises en page

```
List<ViewHolderInfo> vi = new ArrayList<>();vi.add(new ViewHolderInfo(R.layout.item_layout, TYPE_ITEM)); vi.add(new ViewHolderInfo(R.layout.item_header_layout, TYPE_HEADER)); 
```

2. Créez une instance de **RxDataSource** comme avant :

```
RxDataSource<String> rxDataSource = new RxDataSource<>(dataSet);
```

3. Composez et appelez bindRecyclerView en passant le **recyclerView**, la liste **viewHolderInfo** et l'implémentation de **getItemViewType** :

```
rxDataSource.bindRecyclerView(recyclerView, viewHolderInfoList,    new OnGetItemViewType() {      @Override public int getItemViewType(int position) {        if (position % 2 == 0) {          return TYPE_HEADER; // les en-têtes sont aux positions paires        }        return TYPE_ITEM;      }    }  ).subscribe(vH -> {    // Vérifiez le type d'instance et liez !    final ViewDataBinding b = vH.getViewDataBinding();    if (b instanceof ItemLayoutBinding) {      final ItemLayoutBinding iB = (ItemLayoutBinding) b;      iB.textViewItem.setText("ITEM: " + vH.getItem());    } else if (b instanceof ItemHeaderLayoutBinding) {      ItemHeaderLayoutBinding hB = (ItemHeaderLayoutBinding) b;      hB.textViewHeader.setText("HEADER: " + vH.getItem());    }  });
```

```
/* et comme avant, vous pouvez faire ceci également    rxDataSource.filter(s -> s.length() > 0)               .map(String::toUpperCase)              .updateAdapter();*/
```

Maintenant, le **recyclerView** ressemblerait à quelque chose comme :

![Image](https://cdn-media-1.freecodecamp.org/images/1*bz1gu8r1BtqqOxQ2c0Jo5Q.png)

### Un peu sur l'implémentation

#### PublishSubject

Préface → J'ai utilisé [**PublishSubjects**](http://reactivex.io/documentation/subject.html) pour la plupart, et des **génériques** pour créer l'adaptateur.

PublishSubject est un type d'observable qui peut être à la fois _Observable_ et _Observer_ en même temps.

Parce qu'il est un observateur, il peut s'abonner à un ou plusieurs Observables. Et parce qu'il est un Observable, il peut transmettre les éléments qu'il observe en les réémettant, et il peut également émettre de nouveaux éléments.

#### Internals

En interne, il y a deux adaptateurs, que vous pouvez également accéder directement si vous le souhaitez : **RxAdapter** et **RxAdapterForTypes**.

Pour ces deux, j'ai créé une implémentation générique de **ViewHolder**, qui lie la mise en page avec une instance de ViewDataBinding :

```
public class SimpleViewHolder<T, V extends ViewDataBinding> extends RecyclerView.ViewHolder {    private V mViewDataBinding;    public V getViewDataBinding() {        return mViewDataBinding;    }    public T getItem() {        return mItem;    }    private T mItem;    protected void setItem(final T item) {        mItem = item;    }    public SimpleViewHolder(final View itemView) {        super(itemView);        mViewDataBinding = DataBindingUtil.bind(itemView);    }}
```

Ensuite, j'ai créé RxAdapter — Il prend deux génériques :

```
RxAdapter&lt;DataType, LayoutBinding extends ViewDataBinding>
```

J'ai créé un [PublishSubject](http://reactivex.io/RxJava/javadoc/rx/subjects/PublishSubject.html) pour mon ViewHolder, et dans onBindViewHolder j'appelle onNext. Le viewHolder contient l'élément lui-même :

```
@Overridepublic void onBindViewHolder(final SimpleViewHolder<T, V> holder, final int position) {    holder.setItem(mDataSet.get(position));    mPublishSubject.onNext(holder);}
```

Enfin, j'ai créé une méthode asObservable, qui retourne le publishSubject en tant qu'Observable afin que vous puissiez vous y abonner :

```
public Observable<SimpleViewHolder> asObservable(){    return mPublishSubject.asObservable();}
```

Mais attendez, qu'en est-il du RxDataSource ? Eh bien, ce n'est qu'un wrapper pour les Observables Rx. Son but principal est de vous fournir une abstraction sur les deux adaptateurs et les méthodes Rx. Il connecte essentiellement tout ensemble.

Lorsque je dis que c'est un wrapper, cela signifie que vous n'obtenez que des méthodes qui sont **pertinentes pour un recyclerAdapter**, comme _filter_, _map_, _take_, _first_, _repeat_ et ainsi de suite. Il ne vous donne pas de méthodes qui ont quelque chose à voir avec le threading ou les schedulers.

La classe est assez simple. Vous pouvez consulter le code pour RxDataSource [**ici**](https://github.com/ahmedrizwan/RxRecyclerAdapter/blob/master/rxrecycler-adapter/src/main/java/com/minimize/android/rxrecycleradapter/RxDataSource.java).

C'est à peu près tout... J'espère que vous avez trouvé cet article utile. Essayez [RxAdapter](https://github.com/ahmedrizwan/RxRecyclerAdapter). Et si vous avez des questions (ou des suggestions), n'hésitez pas !

![Image](https://cdn-media-1.freecodecamp.org/images/1*rgZIWDa7Zr8GJhb5zQiyPA.jpeg)

Bon codage !