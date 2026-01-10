---
title: How and why to use Android Visibility Listeners
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2018-12-27T22:44:38.000Z'
originalURL: https://freecodecamp.org/news/how-and-why-to-use-android-visibility-listeners-971e3b6511ec
coverImage: https://cdn-media-1.freecodecamp.org/images/0*FT5DvBVMqW4zZkQ_
tags:
- name: Android
  slug: android
- name: android app development
  slug: android-app-development
- name: coding
  slug: coding
- name: development
  slug: development
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'The Android UI is built up from Views, and in a regular application, there
  are usually several of them. To find out which View the user is currently looking
  at, you need to install Visibility Listeners.

  Read below to find out about the different opti...'
---

The Android UI is built up from Views, and in a regular application, there are usually several of them. To find out which View the user is currently looking at, you need to install **Visibility Listeners**.

Read below to find out about the different options you have to identify the visibility status of a View.

### How To Become Visible

In order for our listeners to work, we must first make sure our View is found in the layout hierarchy. There are two ways this happens:

1. Your View is already part of your layout as it is defined in an XML file
2. You created a View dynamically, and you need to add it using the addView method

```java
public void addView (View child, ViewGroup.LayoutParams params)
```

A View’s visibility status is of Integer type and can have one of three options:

1. **VISIBLE (0)** - The View is visible to the user
2. **INVISIBLE (4)** - The View is invisible to the user, but still takes up space in the layout
3. **GONE (8)** - The View is invisible, and it does not take up space in the layout

Once inside our layout hierarchy, there are a few native options to help us know when our View’s visibility has changed.

#### [onVisibilityChanged](https://developer.android.com/reference/android/view/View.html#onVisibilityChanged(android.view.View,%20int))

```java
protected void onVisibilityChanged (View changedView, int visibility)
```

This method is triggered when the visibility of the view or of an ancestor of the view has changed. The status of the visibility is found inside the visibility parameter.

#### [onWindowVisibilityChanged](https://developer.android.com/reference/android/view/View.html#onWindowVisibilityChanged(int))

```java
protected void onWindowVisibilityChanged (int visibility)
```

This method is triggered when the containing window of our View has changed its visibility. **This does not guarantee that the window your View is in is visible to the user, as it may be obscured by another window.**

### Visibility Listeners In Action

To see these two listeners in action, let us create a simple project. We will have a LinearLayout with a TextView and a button. We’ll make the button’s on click action add our custom view to the layout.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nYk06TzXhcQz6nW2dbRbfA.jpeg)

Our custom view:

```java
package com.tomerpacific.viewvisibility;

import android.content.Context;
import android.graphics.Color;
import android.util.Log;
import android.view.View;
import android.widget.LinearLayout;
import android.widget.TextView;

import static android.view.Gravity.CENTER;

public class MyCustomView extends LinearLayout {

    private final String TAG = MyCustomView.class.getSimpleName();

    public MyCustomView(Context context) {
        super(context);
        this.setBackgroundColor(Color.GREEN);
        this.setGravity(CENTER);
        TextView myTextView = new TextView(context);
        myTextView.setText("My Custom View");
        addView(myTextView);
    }

    @Override
    public void onVisibilityChanged(View changedView, int visibility) {
        super.onVisibilityChanged(changedView, visibility);

        Log.d(TAG, "View " + changedView + " changed visibility to " + visibility);
    }

    @Override
    public void onWindowVisibilityChanged(int visibility) {
        super.onWindowVisibilityChanged(visibility);

        Log.d(TAG, "Window visibility changed to " + visibility);
    }

}
```

And finally, the code in our MainActivity:

```java
package com.tomerpacific.viewvisibility;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;

public class MainActivity extends AppCompatActivity {

    private Button addCustomViewBtn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        addCustomViewBtn = (Button) findViewById(R.id.addCustomViewBtn);

        addCustomViewBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                LinearLayout mainLayout = (LinearLayout) findViewById(R.id.mainLayout);
                MyCustomView myCustomView = new MyCustomView(getApplicationContext());
                myCustomView.setLayoutParams(new LinearLayout.LayoutParams(
                    LinearLayout.LayoutParams.MATCH_PARENT, 
                    LinearLayout.LayoutParams.WRAP_CONTENT));

                mainLayout.addView(myCustomView);
            }
        });
    }
}
```

When we run the application and press the button we get:

[https://giphy.com/gifs/8JZA6Djt7DmYpEXj2h/html5](https://giphy.com/gifs/8JZA6Djt7DmYpEXj2h/html5)

You can get the sample project [here](https://github.com/TomerPacific/MediumArticles/tree/master/ViewVisibility).

#### [ViewTreeObserver](https://developer.android.com/reference/android/view/ViewTreeObserver)

This is a native object that has a wide range of listeners that are notified of various visibility changes to the view tree. Some prominent ones to take notice of are:

* [OnGlobalLayoutListener](https://developer.android.com/reference/android/view/ViewTreeObserver.OnGlobalLayoutListener.html)
* [OnWindowAttachListener](https://developer.android.com/reference/android/view/ViewTreeObserver.OnWindowAttachListener.html)
* [OnWindowFocusChangeListener](https://developer.android.com/reference/android/view/ViewTreeObserver.OnWindowFocusChangeListener.html)

To attach a ViewTreeObserver, you need to do the following:

```java
LinearLayout linearLayout = (LinearLayout) findViewById(R.id.YOUR_VIEW_ID);

ViewTreeObserver viewTreeObserver = linearLayout.getViewTreeObserver(); 
viewTreeObserver.addOnGlobalLayoutListener (new ViewTreeObserver.OnGlobalLayoutListener() { 
    
    @Override 
    public void onGlobalLayout() {
        linearLayout.getViewTreeObserver().removeOnGlobalLayoutListener(this); 
        //TODO Add Logic
    } 
});
```

The line `linearLayout.getViewTreeObserver().removeOnGlobalLayoutListener(this)` makes sure that the listener will only get called once. If you want to continue listening in on changes, remove it.

If you have any comments or suggestions, feel free to let me know.

