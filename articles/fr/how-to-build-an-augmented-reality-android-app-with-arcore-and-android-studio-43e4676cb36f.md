---
title: Comment créer une application Android de réalité augmentée avec ARCore et Android
  Studio
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-15T16:57:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-augmented-reality-android-app-with-arcore-and-android-studio-43e4676cb36f
coverImage: https://cdn-media-1.freecodecamp.org/images/0*YjUBhRlE5eEKPbl-.jpg
tags:
- name: Android
  slug: android
- name: Android Studio
  slug: android-studio
- name: Apps
  slug: apps-tag
- name: Augmented Reality
  slug: augmented-reality
- name: 'tech '
  slug: tech
seo_title: Comment créer une application Android de réalité augmentée avec ARCore
  et Android Studio
seo_desc: 'By Ayusch Jain


  This article was originally posted here


  In the previous post, I explained what ARCore is and how it helps developers build
  awesome augmented reality apps without the need to understand OpenGL or Matrix maths.

  If you haven’t checked i...'
---

Par Ayusch Jain

> Cet article a été initialement publié [ici](http://ayusch.com/building-arcore-app-android-studio/)

[Dans le précédent article](https://ayusch.com/what-is-arcore/), j'ai expliqué [ce qu'est ARCore](https://ayusch.com/what-is-arcore/) et comment il aide les développeurs à créer des applications de réalité augmentée incroyables sans avoir besoin de comprendre **OpenGL** ou les mathématiques de **Matrix**.

Si vous ne l'avez pas encore consulté, je vous recommande vivement de le faire avant de continuer avec cet article et de vous lancer dans le développement d'applications ARCore.

### Aperçu

[Selon Wikipedia](https://en.wikipedia.org/wiki/ARCore), ARCore est un kit de développement logiciel développé par Google qui permet de créer des applications de réalité augmentée.

**ARCore** utilise trois technologies clés pour intégrer du contenu virtuel avec l'environnement réel :

1. **Suivi de mouvement** : il permet au téléphone de comprendre sa position par rapport au monde.
2. **Compréhension de l'environnement** : cela permet au téléphone de détecter la taille et l'emplacement de tous types de surfaces, verticales, horizontales et inclinées.
3. **Estimation de la lumière** : il permet au téléphone d'estimer les conditions d'éclairage actuelles de l'environnement.

### Prise en main

Pour commencer le développement d'une **application ARCore**, vous devez d'abord activer ARCore dans votre projet. Cela est simple car nous allons utiliser Android Studio et le SDK Sceneform. Il y a deux opérations majeures que Sceneform effectue automatiquement :

1. **Vérification de la disponibilité d'ARCore**
2. **Demande de permission pour la caméra**

Vous n'avez pas besoin de vous soucier de ces deux étapes lors de la création d'une application ARCore en utilisant le SDK Sceneform. Mais vous devez inclure le SDK Sceneform dans votre projet.

Créez un nouveau projet Android Studio et sélectionnez une activité vide.

**Ajoutez la dépendance suivante à votre fichier build.gradle au niveau du projet :**

```
dependencies {    classpath 'com.google.ar.sceneform:plugin:1.5.0'}
```

**Ajoutez ce qui suit à votre fichier build.gradle au niveau de l'application :**

```
implementation "com.google.ar.sceneform.ux:sceneform-ux:1.5.0"
```

Maintenant, synchronisez le projet avec les fichiers Gradle et attendez la fin de la construction. Cela installera le SDK Sceneform dans le projet et le plugin Sceneform dans **AndroidStudio**. Il vous aidera à visualiser les fichiers **.sfb**. Ces fichiers sont les modèles 3D qui sont rendus dans votre caméra. Il vous aide également à importer, visualiser et construire des **actifs 3D**.

### Création de votre première application ARCore

Maintenant que notre configuration **Android Studio** est complète et que le SDK Sceneform est installé, nous pouvons commencer à écrire notre toute première **application ARCore**.

Tout d'abord, nous devons ajouter le fragment Sceneform à notre fichier de mise en page. Ce sera la scène où nous placerons tous nos modèles 3D. Il prend en charge l'initialisation de la caméra et la gestion des permissions.

Rendez-vous dans votre fichier de mise en page principal. Dans mon cas, il s'agit de **activity_main.xml** et ajoutez le fragment Sceneform :

```
<?xml version="1.0" encoding="utf-8"?><FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"    xmlns:tools="http://schemas.android.com/tools"    android:layout_width="match_parent"    android:layout_height="match_parent"    tools:context=".MainActivity">
```

```
    <fragment android:name="com.google.ar.sceneform.ux.ArFragment"        android:id="@+id/ux_fragment"        android:layout_width="match_parent"        android:layout_height="match_parent" />
```

```
</FrameLayout>
```

J'ai défini la largeur et la hauteur pour correspondre au parent car cela couvrira toute mon activité. Vous pouvez choisir les dimensions selon vos besoins.

### Vérification de la compatibilité

C'est tout ce que vous devez faire dans le fichier de mise en page. Maintenant, rendez-vous dans le fichier Java, dans mon cas, il s'agit de MainActivity.java. Ajoutez la méthode ci-dessous dans votre classe :

```
public static boolean checkIsSupportedDeviceOrFinish(final Activity activity) {    if (Build.VERSION.SDK_INT < Build.VERSION_CODES.N) {        Log.e(TAG, "Sceneform nécessite Android N ou une version ultérieure");        Toast.makeText(activity, "Sceneform nécessite Android N ou une version ultérieure", Toast.LENGTH_LONG).show();        activity.finish();        return false;    }    String openGlVersionString =            ((ActivityManager) activity.getSystemService(Context.ACTIVITY_SERVICE))                    .getDeviceConfigurationInfo()                    .getGlEsVersion();    if (Double.parseDouble(openGlVersionString) < MIN_OPENGL_VERSION) {        Log.e(TAG, "Sceneform nécessite OpenGL ES 3.0 ou une version ultérieure");        Toast.makeText(activity, "Sceneform nécessite OpenGL ES 3.0 ou une version ultérieure", Toast.LENGTH_LONG)                .show();        activity.finish();        return false;    }    return true;}
```

Cette méthode vérifie si votre appareil peut supporter le SDK Sceneform ou non. Le SDK nécessite le niveau d'API Android 27 ou supérieur et la **version 3.0** de **OpenGL ES** ou supérieure. Si un appareil ne supporte pas ces deux éléments, la scène ne sera pas rendue et votre application affichera un écran vide.

Cependant, vous pouvez toujours continuer à fournir toutes les autres fonctionnalités de votre application qui n'ont pas besoin du SDK Sceneform.

Maintenant que la vérification de la compatibilité de l'appareil est terminée, nous allons construire notre modèle 3D et l'attacher à la scène.

### Ajout des actifs

Vous devrez ajouter les modèles 3D qui seront rendus sur votre écran. Maintenant, vous pouvez construire ces modèles vous-même si vous êtes familier avec la création de modèles 3D. Ou, vous pouvez visiter **Poly**.

Là, vous trouverez une énorme bibliothèque d'actifs 3D parmi lesquels choisir. Ils sont gratuits à télécharger. Il suffit de créditer le créateur et vous êtes prêt à partir.

![Image](https://cdn-media-1.freecodecamp.org/images/n-nw06cs3-ISxbKFW3j1ICdyfLIJM7Jpf0dR)

Dans Android Studio, développez votre dossier d'application disponible dans le volet de projet à gauche. Vous remarquerez un dossier **"sampledata"**. Ce dossier contiendra tous vos actifs de modèles 3D. Créez un dossier pour votre modèle à l'intérieur du dossier sample data.

Lorsque vous téléchargez le fichier zip depuis Poly, vous trouverez probablement 3 fichiers.

1. **.mtl file**
2. **.obj file**
3. **.png file**

Le plus important de ces 3 est le fichier .obj. C'est votre modèle réel. Placez les 3 fichiers à l'intérieur de **sampledata** **-> "dossier de votre modèle"**.

![Image](https://cdn-media-1.freecodecamp.org/images/jInoAjquRuqEpoCSH3RSO4VRoWi5tNu9GLL9)

**Maintenant, faites un clic droit sur le fichier .obj**. La première option serait d'importer l'actif Sceneform. Cliquez dessus, ne changez pas les paramètres par défaut, cliquez simplement sur terminer dans la fenêtre suivante. Votre Gradle se synchronisera pour inclure l'actif dans le dossier des actifs. Une fois la construction Gradle terminée, vous êtes prêt à partir.

Vous avez terminé l'importation d'un actif 3D utilisé par Sceneform dans votre projet. **Ensuite**, construisons l'actif à partir de notre code et incluons-le dans la scène.

### Construction du modèle

Ajoutez le code suivant à votre fichier MainActivity.java (ou quel qu'il soit dans votre cas). Ne vous inquiétez pas, je vais expliquer tout le code ligne par ligne :

```
private static final String TAG = MainActivity.class.getSimpleName();private static final double MIN_OPENGL_VERSION = 3.0;
```

```
ArFragment arFragment;ModelRenderable lampPostRenderable;
```

```
@Override@SuppressWarnings({"AndroidApiChecker", "FutureReturnValueIgnored"})
```

```
protected void onCreate(Bundle savedInstanceState) {    super.onCreate(savedInstanceState);    if (!checkIsSupportedDeviceOrFinish(this)) {        return;    }    setContentView(R.layout.activity_main);    arFragment = (ArFragment) getSupportFragmentManager().findFragmentById(R.id.ux_fragment);
```

```
    ModelRenderable.builder()            .setSource(this, Uri.parse("LampPost.sfb"))            .build()            .thenAccept(renderable -> lampPostRenderable = renderable)            .exceptionally(throwable -> {                Toast toast =                        Toast.makeText(this, "Impossible de charger le renderable andy", Toast.LENGTH_LONG);                toast.setGravity(Gravity.CENTER, 0, 0);                toast.show();                return null;            });
```

```
}
```

**Tout d'abord**, nous trouvons le **arFragment** que nous avons inclus dans le fichier de mise en page. Ce fragment est responsable de l'hébergement de la scène. Vous pouvez le considérer comme le conteneur de notre scène.

**Ensuite**, nous utilisons la classe **ModelRenderable** pour construire notre modèle. Avec l'aide de la méthode setSource, nous chargeons notre modèle à partir du fichier **.sfb**. Ce fichier a été généré lorsque nous avons importé les actifs. La méthode **thenAccept** reçoit le modèle une fois qu'il est construit. Nous définissons le modèle chargé dans notre **lampPostRenderable**.

Pour la gestion des erreurs, nous avons la méthode **.exceptionally**. Elle est appelée en cas d'exception.

Tout cela se passe **de manière asynchrone**, donc vous n'avez pas besoin de vous soucier du multithreading ou de gérer les handlers XD

Avec le modèle chargé et stocké dans la variable **lampPostRenderable**, nous allons maintenant l'ajouter à notre scène.

### Ajout du modèle à la scène

Le **arFragment** héberge notre scène et recevra les événements de tapotement. Nous devons donc définir l'écouteur onTap sur notre fragment pour enregistrer le tapotement et placer un objet en conséquence. Ajoutez le code suivant à la méthode onCreate :

```
arFragment.setOnTapArPlaneListener(        (HitResult hitresult, Plane plane, MotionEvent motionevent) -> {            if (lampPostRenderable == null){                return;            }
```

```
            Anchor anchor = hitresult.createAnchor();            AnchorNode anchorNode = new AnchorNode(anchor);            anchorNode.setParent(arFragment.getArSceneView().getScene());
```

```
            TransformableNode lamp = new TransformableNode(arFragment.getTransformationSystem());            lamp.setParent(anchorNode);            lamp.setRenderable(lampPostRenderable);            lamp.select();        });
```

Nous définissons le **onTapArPlaneListener** sur notre **fragment AR**. Ensuite, ce que vous voyez est la **syntaxe Java 8**, au cas où vous ne la connaissez pas, je vous recommande de consulter [**ce guide**](https://www.tutorialspoint.com/java8/index.htm).

**Tout d'abord**, nous créons notre ancre à partir du HitResult en utilisant **hitresult.createAnchor()** et nous la stockons dans un objet Anchor.

**Ensuite**, créez un nœud à partir de cette ancre. Il sera appelé **AnchorNode**. Il sera attaché à la scène en appelant la méthode setParent sur celui-ci et en passant la scène du fragment.

Maintenant, nous créons un **TransformableNode** qui sera notre **lampadaire** et nous le définissons à l'emplacement de l'ancre ou de notre nœud d'ancre. Le nœud n'a toujours aucune information sur l'objet qu'il doit rendre. Nous passerons cet objet en utilisant la méthode **lamp.setRenderable** qui prend un renderable comme paramètre. Enfin, appelez lamp.select();

**Ouf !!** Beaucoup de terminologie là, mais ne vous inquiétez pas, je vais tout expliquer.

1. **Scène** : C'est l'endroit où tous vos objets 3D seront rendus. Cette scène est hébergée par le fragment AR que nous avons inclus dans la mise en page. Un nœud d'ancre est attaché à cet écran qui agit comme la racine de l'arbre et tous les autres objets sont rendus comme ses objets.
2. **HitResult** : C'est une ligne imaginaire (ou un rayon) venant de l'infini qui donne le point d'intersection de lui-même avec un objet du monde réel.
3. **Ancre** : Une ancre est un emplacement et une orientation fixes dans le monde réel. Elle peut être comprise comme la coordonnée x, y, z dans l'espace 3D. Vous pouvez obtenir les informations de position d'une ancre à partir de celle-ci. **Pose** est la position et l'orientation de l'objet dans la scène. Cela est utilisé pour transformer l'espace de coordonnées local de l'objet en espace de coordonnées du monde réel.
4. AnchorNode : C'est le nœud qui se positionne automatiquement dans le monde. C'est le premier nœud qui est défini lorsque le plan est détecté.
5. **TransformableNode** : C'est un nœud avec lequel on peut interagir. Il peut être déplacé, mis à l'échelle, tourné et bien plus encore. Dans cet exemple, nous pouvons mettre à l'échelle la **lampe** et la faire tourner. D'où le nom Transformable.

Il n'y a pas de science des fusées ici. C'est vraiment simple. Toute la scène peut être vue comme un graphe avec la Scène comme parent, **AnchorNode** comme son enfant, puis en branchant différents nœuds/objets à rendre à l'écran.

Votre fichier MainActivity.java final doit ressembler à ceci :

```
package com.ayusch.arcorefirst;
```

```
import android.app.Activity;import android.app.ActivityManager;import android.content.Context;import android.net.Uri;import android.os.Build;import android.support.v7.app.AppCompatActivity;import android.os.Bundle;import android.util.Log;import android.view.Gravity;import android.view.MotionEvent;import android.widget.Toast;
```

```
import com.google.ar.core.Anchor;import com.google.ar.core.HitResult;import com.google.ar.core.Plane;import com.google.ar.sceneform.AnchorNode;import com.google.ar.sceneform.rendering.ModelRenderable;import com.google.ar.sceneform.ux.ArFragment;import com.google.ar.sceneform.ux.TransformableNode;
```

```
public class MainActivity extends AppCompatActivity {    private static final String TAG = MainActivity.class.getSimpleName();    private static final double MIN_OPENGL_VERSION = 3.0;
```

```
    ArFragment arFragment;    ModelRenderable lampPostRenderable;
```

```
    @Override    @SuppressWarnings({"AndroidApiChecker", "FutureReturnValueIgnored"})    protected void onCreate(Bundle savedInstanceState) {        super.onCreate(savedInstanceState);        if (!checkIsSupportedDeviceOrFinish(this)) {            return;        }        setContentView(R.layout.activity_main);        arFragment = (ArFragment) getSupportFragmentManager().findFragmentById(R.id.ux_fragment);
```

```
        ModelRenderable.builder()                .setSource(this, Uri.parse("LampPost.sfb"))                .build()                .thenAccept(renderable -> lampPostRenderable = renderable)                .exceptionally(throwable -> {                    Toast toast =                            Toast.makeText(this, "Impossible de charger le renderable andy", Toast.LENGTH_LONG);                    toast.setGravity(Gravity.CENTER, 0, 0);                    toast.show();                    return null;                });
```

```
            arFragment.setOnTapArPlaneListener(                    (HitResult hitresult, Plane plane, MotionEvent motionevent) -> {                        if (lampPostRenderable == null){                            return;                        }
```

```
                        Anchor anchor = hitresult.createAnchor();                        AnchorNode anchorNode = new AnchorNode(anchor);                        anchorNode.setParent(arFragment.getArSceneView().getScene());
```

```
                        TransformableNode lamp = new TransformableNode(arFragment.getTransformationSystem());                        lamp.setParent(anchorNode);                        lamp.setRenderable(lampPostRenderable);                        lamp.select();                    }            );
```

```
    }
```

```
    public static boolean checkIsSupportedDeviceOrFinish(final Activity activity) {        if (Build.VERSION.SDK_INT < Build.VERSION_CODES.N) {            Log.e(TAG, "Sceneform nécessite Android N ou une version ultérieure");            Toast.makeText(activity, "Sceneform nécessite Android N ou une version ultérieure", Toast.LENGTH_LONG).show();            activity.finish();            return false;        }        String openGlVersionString =                ((ActivityManager) activity.getSystemService(Context.ACTIVITY_SERVICE))                        .getDeviceConfigurationInfo()                        .getGlEsVersion();        if (Double.parseDouble(openGlVersionString) < MIN_OPENGL_VERSION) {            Log.e(TAG, "Sceneform nécessite OpenGL ES 3.0 ou une version ultérieure");            Toast.makeText(activity, "Sceneform nécessite OpenGL ES 3.0 ou une version ultérieure", Toast.LENGTH_LONG)                    .show();            activity.finish();            return false;        }        return true;    }}
```

**Félicitations !!** Vous venez de terminer votre première application ARCore. Commencez à ajouter des objets et voyez-les prendre vie dans le monde réel !

C'était votre premier aperçu de la création d'une application **ARCore** simple à partir de zéro avec Android Studio. Dans le prochain tutoriel, j'irai plus loin dans ARCore et j'ajouterai plus de fonctionnalités à l'application.

> _Si vous avez des suggestions ou un sujet pour lequel vous aimeriez un tutoriel, mentionnez-le simplement dans la section des commentaires et je serai heureux de vous aider._

_Vous aimez ce que vous lisez ? N'oubliez pas de partager cet article sur [**Facebook**](https://www.facebook.com/AndroidVille), **WhatsApp** et **LinkedIn**._

_Vous pouvez me suivre sur [LinkedIn](https://www.linkedin.com/in/ayuschjain), [Quora](https://www.quora.com/profile/Ayusch-Jain), [Twitter](https://twitter.com/ayuschjain) et [Instagram](https://www.instagram.com/androidville/) où je **réponds** aux questions liées au **développement mobile, en particulier Android et Flutter**._