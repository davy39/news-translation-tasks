---
title: How to make sense of the many Android layouts
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
seo_title: null
seo_desc: 'Linear, Relative, Constraint, Table, Frame and so on and so forth. Android
  applications have a whole bunch of layouts to choose from when you want to design
  your application. The question is, which one is the best?

  Before we go into detailing the dif...'
---

Linear, Relative, Constraint, Table, Frame and so on and so forth. Android applications have a whole bunch of layouts to choose from when you want to design your application. **The question is, which one is the best?**

Before we go into detailing the different layouts, we’ll first go over the view object hierarchy and Android’s drawing process.

### View and ViewGroup

Think of ViewGroup as the parent class of any view and also, the base class for layouts. It represents an object which is the container for other views. For example, a **LinearLayout** is a **ViewGroup** since it can contain views and other layouts as well.

View, on the other hand, is the basic building block of UI elements. Views can be a part of a ViewGroup. For example, a **TextView** is a **View**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*AwYBLMUOXQb_tegG6uO5rg.jpeg)
_A hierarchy of ViewGroup and View_

### Measure -> Layout -> Draw -> Repeat

Layouts are saved as [XML](https://whatis.techtarget.com/fileformat/XML-eXtensible-markup-language) files in Android. But how do they get converted to the objects we see on the screen? Each XML file gets instantiated (read: inflated) and a view hierarchy tree is formed. This means that if you have layout B that is nested inside layout A, they will have a child — parent relationship (layout A is the parent of layout B). Once the tree is formed, there are 3 phases that will happen: Measure, Layout and Draw. Each of these phases traverses the tree in a [Depth First Search](https://en.wikipedia.org/wiki/Depth-first_search) order.

#### Measure

In the first phase, each parent node figures out certain constraints its children have regarding their size. It passes these limitations downward to its children, where each child will evaluate its own size (how big it wants to be) and take into consideration the limitations it has been given and its children’s limitations.

#### Layout

Here, each node will decide the final size and position of each of its children on the screen.

#### Draw

Starting from the root node, which draws itself, it then tells its children to draw themselves. In this fashion, what happens is that a parent will be drawn and its children will be drawn on top of it.

> _Keeping the process above in mind, you should try to keep the layout of your application as shallow as possible so as to reduce the time it takes to traverse the view hierarchy_

![Image](https://cdn-media-1.freecodecamp.org/images/0*avZ1dpBsBuTW36Xt)
_“assorted-color photo frame lot” by [Unsplash](https://unsplash.com/@markusspiske?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Markus Spiske</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

### Layouts Breakdown

#### Linear

Organizes its children in a row with an orientation of vertical or horizontal. Meaning, the views will either be all in one row or one column. You can specify the direction by using the **android:orientation** attribute.

One interesting feature a Linear Layout has is the **layout_weight** attribute. This is used to tell Linear Layout how to divide the space between child views. It is useful when you want your layout to be consistent among devices and orientations.

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
        android:text="Hello"
        />

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="World!"
        />

</LinearLayout>
```

Let’s say you wanted the first TextView, containing the word _Hello,_ to always take up 3/4 of the screen’s width. To do this, we can use the layout_weight attribute.

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:layout_weight="4"        // <-- We added a total weight for our layout (4)
    tools:context=".MainActivity">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_weight="3"   // <-- Will have a weight of 3 out of 4 (3/4)
        android:text="Hello" />

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="World!"
        android:layout_weight="1"   // <-- Will have a weight of 1 out of 4 (1/4)
        />

</LinearLayout>
```

#### Relative

As the name implies, this layout will set its inner child views in relative position. This can keep your layout hierarchy flat with no nested view groups. At the same time, however, each Relative Layout has to undergo a process of two Measure passes, which can impact performance.

One useful feature of a RelativeLayout is the ability to center a child view by using the **centerInParent** attribute.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cZwvkUglSVr3oWDmFddnZQ.jpeg)
_layout_centerInParent centers the TextView_

#### Constraint

A _constraint_ is a connection or an alignment to the element the constraint is tied to. You define various constraints for every child view relative to other views present. This gives you the ability to construct complex layouts with a flat view hierarchy (no nested ViewGroups). Similar to RelativeLayout, this layout also requires two Measure passes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TCpUhPhDviNMOdjhnSonYw.jpeg)
_Notice the constraints on the TextView_

#### Frame

This layout is used only to hold a single child view, thus blocking any other view in the layout. The layout itself will be as big as its biggest child view (visible or not), plus some padding.

Avoid having several child views inside a FrameLayout since it will be difficult to avoid the child views from overlapping one another. You can control the positions of these child views by assigning the **layout_gravity** attribute to each child.

![Image](https://cdn-media-1.freecodecamp.org/images/1*BLf1yC1vhGgWaVLa7YT-3w.jpeg)

#### List View/Grid View

Use when you have a need to present several items on screen (like in a restaurant menu). List View is a single column list that the user can scroll through. You can think of Grid View as a List View with more than one column.

What is important to know about these layouts is that the Views are dynamic and created at runtime. To make the items populate at runtime, you need to use an [AdapterView](https://developer.android.com/reference/android/widget/AdapterView).

![Image](https://cdn-media-1.freecodecamp.org/images/1*T6XG2VZ1kpJrx8g9VZS-xg.jpeg)
_You can specify the location of each item in the layout using layout_column and layout_row_

#### TableLayout

Very similar to Grid View, this layout arranges its children into rows and columns. Each layout will contain several TableRow objects, each defining a row.

![Image](https://cdn-media-1.freecodecamp.org/images/1*IxB5s08Z_w-3gKq-DT564A.jpeg)
_We have two TableRow elements_

Don’t be afraid to try different layouts until you find the one that works best for you. Feel free to let me know in the comments below which layout is most useful to you and why.

