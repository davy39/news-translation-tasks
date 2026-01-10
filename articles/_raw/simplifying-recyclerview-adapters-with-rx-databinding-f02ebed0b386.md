---
title: Simplifying RecyclerView Adapters with Rx & Databinding
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
seo_title: null
seo_desc: 'By Ahmed Rizwan

  I recently wanted to dive deeper into Rx. So I experimented with Rx and the RecyclerView
  Adapters, and the results were pretty interesting!

  With Rx in mind, I set out to accomplish three things:


  Create a RecyclerView adapter which sh...'
---

By Ahmed Rizwan

I recently wanted to dive deeper into Rx. So I experimented with Rx and the RecyclerView Adapters, and the results were pretty interesting!

With Rx in mind, I set out to accomplish three things:

1. Create a RecyclerView adapter which should be **generic** — one adapter class to rule them all!
2. It should return **bindings** in the form of Rx streams!
3. There should also be an option for supporting multiple item **types**!

Now, you may be thinking: this isn’t really necessary. I mean why use Rx in the first place with RecyclerAdapters? And why exactly do you need bindings as Rx streams?

Well that’s true. Personally, I thought it’d be a good experiment to incorporate Rx into RecyclerView Adapters, instead of using simple callbacks or delegates. So it was sort of experimental.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6oS0HYL3OOVu9b4PupalmA.gif)

So I wrote a library called [**RxRecyclerAdapter**](https://github.com/ahmedrizwan/RxRecyclerAdapter) to get Rx to work with the Adapters. Let’s break down how it simplifies use of the recycler adapters.

#### RxDataSource simplifies the use of RxRecyclerAdapter

Let’s say you have a beautiful String array list that you want to display:

```
//Dummy DataSetdataSet = new ArrayList<>();dataSet.add("this");dataSet.add("is");dataSet.add("an");dataSet.add("example");dataSet.add("of rx!");
```

Here’s what you would do:

1. Enable data binding by adding this into build.gradle

```
dataBinding {      enabled = true}
```

2. create the layout file for the item:

```
&lt;?xml version="1.0" encoding="utf-8"?>&lt;layout xmlns:android="http://schemas.android.com/apk/res/android"        xmlns:tools="http://schemas.android.com/tools">    <LinearLayout        android:layout_width="match_parent"        android:layout_height="match_parent"        android:orientation="vertical"        android:padding="@dimen/activity_horizontal_margin">        <;TextView android:id="@+id/textViewItem"                  android:layout_width="match_parent"                  android:layout_height="wrap_content"                  tools:text="Recycler Item"/>    </LinearLayout></layout>
```

3. Create an instance of **RxDataSource** telling it what the dataSet type is:

```
RxDataSource&lt;String> rxDataSource = new RxDataSource<>(dataSet);
```

4. Compose and then cast-call bindRecyclerView (passing in the RecyclerView and layout) with LayoutBinding. Because of casting, viewHolder can infer the type of binding.

```
rxDataSource  .map(String::toLowerCase)  .repeat(10)  .&lt;ItemLayoutBinding>bindRecyclerView(recyclerView,                               R.layout.item_layout)  .subscribe(viewHolder -> {         ItemLayoutBinding b = viewHolder.getViewDataBinding();         b.textViewItem.setText(viewHolder.getItem());  });
```

The output will be…

![Image](https://cdn-media-1.freecodecamp.org/images/1*T10QOX-L1dbfFlr8UCiAOg.png)

Note that calling observeOn(AndroidSchedulers.mainThread()) would be unnecessary here, as you’re already on the mainThread. And when you call it, it causes a delay of about ~20–30 milliseconds in the stream, which would lower your frame rate.

Now for a bit more practical example.

Let’s say you want to dynamically update the dataSet. Let’s say you want to search the dataSet and filter out the results specific results. Here’s how that would be done:

```
RxTextView.afterTextChangeEvents(searchEditText).subscribe(event -> {  rxDataSource.updateDataSet(dataSet)       .filter(s -> s.contains(event.view().getText()))      .updateAdapter();});
```

In combination with [RxBindings](https://github.com/JakeWharton/RxBinding) (because RxBindings are awesome), I register for textChange events. And when the event occurs I update the DataSet with the **base dataSet!**

Now this is important because the RxDataSource changes its dataSet instance when I call methods like _filter_, _map_ and so on. So filtering needs to be done on the **original dataSet**, not the changed one. And… bam!

![Image](https://cdn-media-1.freecodecamp.org/images/1*uMxIbKfiEySpqx027Ilh3A.gif)

I did come across some limitations — one being that you can’t change the **type** of dataSet after it has been bound with the data source. So functions like _map_ and _flatmap_ can’t return a different type of dataSet. But I have yet to run into a situation where I needed to be able to change the dataSet at runtime.

#### RxRecyclerAdapter simplifies the situations where you have multiple item types

Now let’s say you wanted multiple Item types in your RecyclerView, for example a header and an item type. Then you would:

1. Create List of **ViewHolderInfo** specifying all the layouts

```
List<ViewHolderInfo> vi = new ArrayList<>();vi.add(new ViewHolderInfo(R.layout.item_layout, TYPE_ITEM)); vi.add(new ViewHolderInfo(R.layout.item_header_layout, TYPE_HEADER)); 
```

2. Create instance of **RxDataSource** like before:

```
RxDataSource<String> rxDataSource = new RxDataSource<>(dataSet);
```

3. Compose and call bindRecyclerView passing in the **recyclerView**, the **viewHolderInfo** list and implementation of **getItemViewType**:

```
rxDataSource.bindRecyclerView(recyclerView, viewHolderInfoList,    new OnGetItemViewType() {      @Override public int getItemViewType(int position) {        if (position % 2 == 0) {          return TYPE_HEADER; //headers are even positions        }        return TYPE_ITEM;      }    }  ).subscribe(vH -> {    //Check instance type and bind!    final ViewDataBinding b = vH.getViewDataBinding();    if (b instanceof ItemLayoutBinding) {      final ItemLayoutBinding iB = (ItemLayoutBinding) b;      iB.textViewItem.setText("ITEM: " + vH.getItem());    } else if (b instanceof ItemHeaderLayoutBinding) {      ItemHeaderLayoutBinding hB = (ItemHeaderLayoutBinding) b;      hB.textViewHeader.setText("HEADER: " + vH.getItem());    }  });
```

```
/* and like before, you can do this as well    rxDataSource.filter(s -> s.length() > 0)               .map(String::toUpperCase)              .updateAdapter();*/
```

Now **recyclerView** would look something like:

![Image](https://cdn-media-1.freecodecamp.org/images/1*bz1gu8r1BtqqOxQ2c0Jo5Q.png)

### A little about the Implementation

#### PublishSubject

Preface → I utilized [**PublishSubjects**](http://reactivex.io/documentation/subject.html) for the most part, and **generics** to create the adapter.

PublishSubject is a type of observable which can be both _Observable_ and an _Observer_ at the same time.

Because it is an observer, it can subscribe to one or more Observables. And because it is an Observable, it can pass through the items it observes by reemitting them, and it can also emit new items.

#### Internals

Internally, there are two adapters, which you can also access directly if you want: **RxAdapter** and **RxAdapterForTypes**.

For these two, I created a generic **ViewHolder** implementation, which binds the layout with an instance of ViewDataBinding:

```
public class SimpleViewHolder<T, V extends ViewDataBinding> extends RecyclerView.ViewHolder {    private V mViewDataBinding;    public V getViewDataBinding() {        return mViewDataBinding;    }    public T getItem() {        return mItem;    }    private T mItem;    protected void setItem(final T item) {        mItem = item;    }    public SimpleViewHolder(final View itemView) {        super(itemView);        mViewDataBinding = DataBindingUtil.bind(itemView);    }}
```

Then I created RxAdapter — It takes two generics:

```
RxAdapter&lt;DataType, LayoutBinding extends ViewDataBinding>
```

I created a [PublishSubject](http://reactivex.io/RxJava/javadoc/rx/subjects/PublishSubject.html) for my ViewHolder, and in onBindViewHolder I call onNext. The viewHolder contains the item itself:

```
@Overridepublic void onBindViewHolder(final SimpleViewHolder<T, V> holder, final int position) {    holder.setItem(mDataSet.get(position));    mPublishSubject.onNext(holder);}
```

Finally, I created a method asObservable, which returns the publishSubject as an Observable so that you can subscribe to it:

```
public Observable<SimpleViewHolder> asObservable(){    return mPublishSubject.asObservable();}
```

But wait, what about the RxDataSource? Well it’s just a wrapper for Rx Observables. It’s main purpose is to provide you with an abstraction over the two adapters and Rx methods. It basically connects everything together.

When I say it’s a wrapper, that means that you only get methods that are **relevant to a recyclerAdapter**, like _filter_, _map_, _take_, _first_, _repeat_ and so on. It doesn’t give you methods which have something to do with threading or schedulers.

As the class is pretty straight-forward. You can check out the code for RxDataSource [**here**](https://github.com/ahmedrizwan/RxRecyclerAdapter/blob/master/rxrecycler-adapter/src/main/java/com/minimize/android/rxrecycleradapter/RxDataSource.java).

That’s pretty much it… I hope you found this article useful. Do give [RxAdapter](https://github.com/ahmedrizwan/RxRecyclerAdapter) a try. And if you have any questions (or suggestions), fire away!

![Image](https://cdn-media-1.freecodecamp.org/images/1*rgZIWDa7Zr8GJhb5zQiyPA.jpeg)

Happy coding!

