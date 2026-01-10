---
title: Comment et pourquoi utiliser les écouteurs de visibilité Android
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
seo_title: Comment et pourquoi utiliser les écouteurs de visibilité Android
seo_desc: 'The Android UI is built up from Views, and in a regular application, there
  are usually several of them. To find out which View the user is currently looking
  at, you need to install Visibility Listeners.

  Read below to find out about the different opti...'
---

L'interface utilisateur Android est construite à partir de vues, et dans une application régulière, il y en a généralement plusieurs. Pour savoir quelle vue l'utilisateur regarde actuellement, vous devez installer des **écouteurs de visibilité**.

Lisez ci-dessous pour découvrir les différentes options dont vous disposez pour identifier l'état de visibilité d'une vue.

### Comment devenir visible

Pour que nos écouteurs fonctionnent, nous devons d'abord nous assurer que notre vue est trouvée dans la hiérarchie de mise en page. Il y a deux façons pour que cela se produise :

1. Votre vue fait déjà partie de votre mise en page telle qu'elle est définie dans un fichier XML
2. Vous avez créé une vue dynamiquement, et vous devez l'ajouter en utilisant la méthode addView

```java
public void addView (View child, ViewGroup.LayoutParams params)
```

Le statut de visibilité d'une vue est de type Integer et peut avoir l'une des trois options suivantes :

1. **VISIBLE (0)** - La vue est visible pour l'utilisateur
2. **INVISIBLE (4)** - La vue est invisible pour l'utilisateur, mais occupe toujours de l'espace dans la mise en page
3. **GONE (8)** - La vue est invisible et n'occupe pas d'espace dans la mise en page

Une fois dans notre hiérarchie de mise en page, il existe quelques options natives pour nous aider à savoir quand la visibilité de notre vue a changé.

#### [onVisibilityChanged](https://developer.android.com/reference/android/view/View.html#onVisibilityChanged(android.view.View,%20int))

```java
protected void onVisibilityChanged (View changedView, int visibility)
```

Cette méthode est déclenchée lorsque la visibilité de la vue ou d'un ancêtre de la vue a changé. Le statut de la visibilité se trouve à l'intérieur du paramètre de visibilité.

#### [onWindowVisibilityChanged](https://developer.android.com/reference/android/view/View.html#onWindowVisibilityChanged(int))

```java
protected void onWindowVisibilityChanged (int visibility)
```

Cette méthode est déclenchée lorsque la fenêtre contenant notre vue a changé de visibilité. **Cela ne garantit pas que la fenêtre dans laquelle se trouve votre vue est visible pour l'utilisateur, car elle peut être obscurcie par une autre fenêtre.**

### Écouteurs de visibilité en action

Pour voir ces deux écouteurs en action, créons un projet simple. Nous aurons un LinearLayout avec un TextView et un bouton. Nous ferons en sorte que l'action de clic du bouton ajoute notre vue personnalisée à la mise en page.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nYk06TzXhcQz6nW2dbRbfA.jpeg)

Notre vue personnalisée :

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
        myTextView.setText("Ma vue personnalisée");
        addView(myTextView);
    }

    @Override
    public void onVisibilityChanged(View changedView, int visibility) {
        super.onVisibilityChanged(changedView, visibility);

        Log.d(TAG, "La vue " + changedView + " a changé de visibilité pour " + visibility);
    }

    @Override
    public void onWindowVisibilityChanged(int visibility) {
        super.onWindowVisibilityChanged(visibility);

        Log.d(TAG, "La visibilité de la fenêtre a changé pour " + visibility);
    }

}
```

Et enfin, le code dans notre MainActivity :

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

Lorsque nous exécutons l'application et appuyons sur le bouton, nous obtenons :

[https://giphy.com/gifs/8JZA6Djt7DmYpEXj2h/html5](https://giphy.com/gifs/8JZA6Djt7DmYpEXj2h/html5)

Vous pouvez obtenir le projet exemple [ici](https://github.com/TomerPacific/MediumArticles/tree/master/ViewVisibility).

#### [ViewTreeObserver](https://developer.android.com/reference/android/view/ViewTreeObserver)

Il s'agit d'un objet natif qui dispose d'une large gamme d'écouteurs qui sont informés des divers changements de visibilité de l'arborescence des vues. Voici quelques-uns des plus importants à noter :

* [OnGlobalLayoutListener](https://developer.android.com/reference/android/view/ViewTreeObserver.OnGlobalLayoutListener.html)
* [OnWindowAttachListener](https://developer.android.com/reference/android/view/ViewTreeObserver.OnWindowAttachListener.html)
* [OnWindowFocusChangeListener](https://developer.android.com/reference/android/view/ViewTreeObserver.OnWindowFocusChangeListener.html)

Pour attacher un ViewTreeObserver, vous devez faire ce qui suit :

```java
LinearLayout linearLayout = (LinearLayout) findViewById(R.id.YOUR_VIEW_ID);

ViewTreeObserver viewTreeObserver = linearLayout.getViewTreeObserver(); 
viewTreeObserver.addOnGlobalLayoutListener (new ViewTreeObserver.OnGlobalLayoutListener() { 
    
    @Override 
    public void onGlobalLayout() {
        linearLayout.getViewTreeObserver().removeOnGlobalLayoutListener(this); 
        //TODO Ajouter la logique
    } 
});
```

La ligne `linearLayout.getViewTreeObserver().removeOnGlobalLayoutListener(this)` garantit que l'écouteur ne sera appelé qu'une seule fois. Si vous souhaitez continuer à écouter les changements, retirez-la.

Si vous avez des commentaires ou des suggestions, n'hésitez pas à me le faire savoir.