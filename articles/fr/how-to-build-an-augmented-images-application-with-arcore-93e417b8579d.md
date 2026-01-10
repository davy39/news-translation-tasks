---
title: Comment créer une application d'images augmentées avec ARCore
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-28T22:56:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-augmented-images-application-with-arcore-93e417b8579d
coverImage: https://cdn-media-1.freecodecamp.org/images/0*zDtfBdMWSJNSZgyx.jpeg
tags:
- name: Android
  slug: android
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Augmented Reality
  slug: augmented-reality
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
seo_title: Comment créer une application d'images augmentées avec ARCore
seo_desc: 'By Ayusch Jain


  This article was originally posted here.


  In this tutorial, you’ll learn how to place 3D models in the real world by setting
  the anchor as a specific scene instead of a regular plane. ARCore by Google lets
  you augment 2D images which ...'
---

Par Ayusch Jain

> Cet article a été initialement publié [ici](https://ayusch.com/arcore-building-augmented-images-application).

Dans ce tutoriel, vous apprendrez à placer des modèles 3D dans le monde réel en définissant l'ancrage comme une scène spécifique plutôt qu'un plan régulier. **ARCore** de Google vous permet d'augmenter des images 2D qui peuvent être reconnues par ARCore pour ensuite placer des modèles 3D par-dessus.

Vous fournissez des images de référence et le suivi **ARCore** détermine où ces images sont physiquement situées dans l'environnement. Les images augmentées sont déjà largement utilisées, par exemple dans les livres, les journaux, les magazines, etc.

Mais avant de plonger plus profondément dans ce **tutoriel**, vous devez consulter les articles suivants comme **prérequis** à celui-ci :

* [**Qu'est-ce qu'ARCore par Google ?**](https://ayusch.com/what-is-arcore/)
* [**Créer une application de réalité augmentée en utilisant ARCore.**](https://ayusch.com/building-arcore-app-android-studio/)

Une fois que vous avez terminé ces deux articles, vous aurez une compréhension de base de certains termes dans ARCore et Sceneform tels que Scene, Anchor, Node, TransformableNode, etc.

### Qu'est-ce que les images augmentées ?

[Selon la documentation des développeurs](https://developers.google.com/ar/develop/c/augmented-images/), les **images augmentées** dans ARCore vous permettent de créer des applications AR qui peuvent répondre à des images 2D, telles que des affiches ou des emballages de produits, dans l'environnement de l'utilisateur. Vous fournissez un ensemble d'images de référence, et le suivi ARCore vous indique où ces images sont physiquement situées dans une session AR, une fois qu'elles sont détectées dans la vue de la caméra.

En gros, en utilisant des images augmentées, vous pouvez transformer une simple image 2D en une image augmentée qui peut être reconnue par votre application et ensuite utilisée pour placer un modèle 3D au-dessus.

### Quand vous pourriez vouloir utiliser les images augmentées

Voici quelques restrictions que vous pourriez vouloir considérer avant d'utiliser les images augmentées :

* Votre cas d'utilisation ne doit pas impliquer la numérisation de plus de 20 images simultanément (puisque ARCore ne peut suivre que jusqu'à 20 images à la fois).
* La taille de l'objet physique dans le monde réel doit être supérieure à 15 cm X 15 cm et plate.
* Vous ne voulez pas suivre des objets en mouvement. ARCore ne peut pas suivre des images en mouvement, bien qu'il puisse commencer à suivre une fois que l'image s'arrête.
* ARCore utilise des points de fonctionnalité dans l'image de référence et peut stocker des informations sur les points de fonctionnalité pour jusqu'à 1000 images.

### Choisir une bonne image de référence

Voici quelques conseils pour choisir une bonne image de référence afin d'améliorer la détectabilité par ARCore :

* Les images augmentées prennent en charge les formats PNG, JPEG et JPG.
* La détection est basée sur des points de fort contraste et donc les images en couleur et en noir et blanc sont détectées, indépendamment du fait qu'une image de référence en couleur ou en noir et blanc soit utilisée.
* La résolution de l'image doit être d'au moins 300 X 300 pixels.
* L'utilisation d'images haute résolution ne signifie pas une meilleure performance.
* Les images avec des caractéristiques répétitives telles que les motifs et les pois doivent être évitées.
* Utilisez l'outil **arcoreimg** pour évaluer la qualité de votre image de référence. Un score d'au moins 75 est recommandé.

### Comment utiliser l'outil arcoreimg :

* Téléchargez le SDK ARCore pour Android depuis ce lien :
* Extrayez le contenu du fichier zip là où vous le souhaitez.
* Naviguez jusqu'au dossier extrait et allez dans tools -> arcoreimg -> windows (linux/macos selon ce que vous utilisez)
* Ouvrez l'invite de commande à cet emplacement.
* Entrez maintenant cette commande :

```
arcoreimg.exe eval-img --input_image_path=dog.png
```

Remplacez **dog.png** par le chemin complet de votre image.

### Commencer avec l'application d'images augmentées

Maintenant que vous vous êtes familiarisé avec ARCore et Sceneform et que vous avez sélectionné une bonne image de référence avec un **score de 75+**, il est temps de commencer à coder l'application !!

#### Créer un fragment personnalisé

Nous allons créer un fragment personnalisé à ajouter à notre activité. Nous avons besoin d'un fragment personnalisé car nous allons modifier certaines propriétés du fragment par défaut.

Créez une classe nommée **« CustomArFragment »** et étendez-la à partir de **ArFragment**. Voici le code pour CustomArFragment :

```
package com.ayusch.augmentedimages;
```

```
import android.util.Log;
```

```
import com.google.ar.core.Config;import com.google.ar.core.Session;import com.google.ar.sceneform.ux.ArFragment;
```

```
public class CustomArFragment extends ArFragment {
```

```
    @Override    protected Config getSessionConfiguration(Session session) {        getPlaneDiscoveryController().setInstructionView(null);        Config config = new Config(session);        config.setUpdateMode(Config.UpdateMode.LATEST_CAMERA_IMAGE);        session.configure(config);        getArSceneView().setupSession(session);
```

```
        return config;    }
```

```
}
```

**Tout d'abord**, nous définissons l'instruction de découverte de plan à **null**. En faisant cela, nous désactivons cette icône de main qui apparaît juste après l'initialisation du fragment et qui indique à l'utilisateur de déplacer son téléphone. Nous n'en avons plus besoin car nous ne détectons pas des plans aléatoires mais une image spécifique.

Ensuite, nous définissons le mode de mise à jour pour la session à **LATEST_CAMERA_IMAGE**. Cela garantit que votre écouteur de mise à jour est appelé chaque fois que la trame de la caméra est mise à jour. Il configure le comportement de la méthode de mise à jour.

#### Configuration de la base de données des images augmentées

Ajoutez votre image de référence choisie (que vous souhaitez détecter dans le monde physique) dans le dossier **assets**. Si votre dossier assets n'existe pas, créez-en un. Maintenant, nous allons ajouter des images augmentées à notre base de données qui seront ensuite détectées dans le monde réel.

Nous allons configurer cette **base de données** dès que le **fragment (scène)** est créé. Ensuite, nous vérifions le succès et l'échec de cet appel et définissons le journal en conséquence. Ajoutez le code suivant à votre fragment personnalisé :

```
if ((((MainActivity) getActivity()).setupAugmentedImagesDb(config, session))) {    Log.d("SetupAugImgDb", "Success");} else {    Log.e("SetupAugImgDb","Faliure setting up db");}
```

Voici à quoi ressemblerait le **CustomArFragment** :

```
package com.ayusch.augmentedimages;
```

```
import android.util.Log;
```

```
import com.google.ar.core.Config;import com.google.ar.core.Session;import com.google.ar.sceneform.ux.ArFragment;
```

```
public class CustomArFragment extends ArFragment {
```

```
    @Override    protected Config getSessionConfiguration(Session session) {        getPlaneDiscoveryController().setInstructionView(null);        Config config = new Config(session);        config.setUpdateMode(Config.UpdateMode.LATEST_CAMERA_IMAGE);        session.configure(config);        getArSceneView().setupSession(session);
```

```
        if ((((MainActivity) getActivity()).setupAugmentedImagesDb(config, session))) {            Log.d("SetupAugImgDb", "Success");        } else {            Log.e("SetupAugImgDb","Faliure setting up db");        }
```

```
        return config;    }
```

```
}
```

Nous allons bientôt créer la méthode **setupAugmentedImagesDb** dans MainActivity. Maintenant que le CustomArFragment est créé, ajoutons-le à notre activity_main.xml, voici le code pour votre activity_main.xml :

```
<?xml version="1.0" encoding="utf-8"?><android.support.constraint.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"    xmlns:app="http://schemas.android.com/apk/res-auto"    xmlns:tools="http://schemas.android.com/tools"    android:layout_width="match_parent"    android:layout_height="match_parent"    tools:context=".MainActivity">
```

```
    <fragment        android:id="@+id/sceneform_fragment"        android:name="com.ayusch.augmentedimages.CustomArFragment"        android:layout_width="match_parent"        android:layout_height="match_parent" />
```

```
</android.support.constraint.ConstraintLayout>
```

**Remarquez** que nous définissons le nom de ce fragment à notre **CustomArFragment**. Cela est nécessaire pour s'assurer que le fragment ajouté est notre fragment personnalisé. Cela garantira que la gestion des permissions et les initialisations de session sont prises en charge.

#### Ajout d'une image à la base de données des images augmentées

Ici, nous allons configurer notre base de données d'images. Trouvez l'image de référence dans le monde réel et ajoutez ensuite un modèle 3D en conséquence.

Commençons par configurer notre base de données. Créez une fonction publique **setupAugmentedImagesDb** dans la classe **MainActivity.java** :

```
public boolean setupAugmentedImagesDb(Config config, Session session) {    AugmentedImageDatabase augmentedImageDatabase;    Bitmap bitmap = loadAugmentedImage();    if (bitmap == null) {        return false;    }
```

```
    augmentedImageDatabase = new AugmentedImageDatabase(session);    augmentedImageDatabase.addImage("tiger", bitmap);    config.setAugmentedImageDatabase(augmentedImageDatabase);    return true;}
```

```
private Bitmap loadAugmentedImage() {
```

```
try (InputStream is = getAssets().open("blanket.jpeg")) {        return BitmapFactory.decodeStream(is);    } catch (IOException e) {        Log.e("ImageLoad", "IO Exception", e);    }
```

```
    return null;}
```

Nous avons également la méthode loadAugmentedImage qui charge l'image depuis le dossier assets et retourne un bitmap.

Dans **setupAugmentedImagesDb**, nous initialisons d'abord notre base de données pour cette session, puis nous ajoutons une image à cette base de données. Nous nommerons notre image « tiger ». Ensuite, nous définissons la base de données pour cette configuration de session et retournons true, indiquant que l'image est ajoutée avec succès.

#### Détection des images de référence dans le monde réel

Maintenant, nous allons commencer à détecter nos images de référence dans le monde réel. Pour ce faire, nous allons ajouter un écouteur à notre scène qui sera appelé chaque fois qu'une trame est créée, et cette trame sera analysée pour trouver notre image de référence.

Ajoutez cette ligne dans la méthode **onCreate** de MainActivity.java :

```
arFragment.getArSceneView().getScene().addOnUpdateListener(this::onUpdateFrame);
```

Ajoutez maintenant la méthode **onUpdateFrame** à MainActivity :

```
@RequiresApi(api = Build.VERSION_CODES.N)private void onUpdateFrame(FrameTime frameTime) {    Frame frame = arFragment.getArSceneView().getArFrame();
```

```
    Collection<AugmentedImage> augmentedImages = frame.getUpdatedTrackables(AugmentedImage.class);    for (AugmentedImage augmentedImage : augmentedImages) {        if (augmentedImage.getTrackingState() == TrackingState.TRACKING) {            if (augmentedImage.getName().equals("tiger") && shouldAddModel) {                placeObject(arFragment, augmentedImage.createAnchor(augmentedImage.getCenterPose()), Uri.parse("Mesh_BengalTiger.sfb"));                shouldAddModel = false;            }        }    }}
```

Dans la première ligne, nous obtenons la trame de la scène. Une **trame** peut être imaginée comme une capture instantanée au milieu d'une vidéo. Si vous êtes familier avec le fonctionnement de la vidéo, vous savez peut-être qu'elles sont une série d'images fixes retournées les unes après les autres très rapidement, donnant l'impression d'une image en mouvement. Nous extrayons une de ces images.

Une fois que nous avons la trame, nous analysons notre image de référence. Nous extrayons une liste de tous les éléments que ARCore a suivis en utilisant **frame.getUpdatedTrackables**. Il s'agit d'une collection de toutes les images détectées. Nous parcourons ensuite la collection et vérifions si notre image « tiger » est présente dans la trame.

Si nous trouvons une correspondance, nous plaçons un modèle 3D sur l'image détectée.

> _Remarque : J'ai ajouté **shouldAddModel** pour m'assurer que nous ajoutons le modèle une seule fois._

#### Placement d'un modèle 3D sur l'image de référence

Maintenant que nous avons détecté notre image dans le monde réel, nous pouvons commencer à ajouter des modèles 3D par-dessus. Nous allons copier les méthodes placeObject et addNodeToScene de notre [**projet précédent**](https://ayusch.com/building-arcore-app-android-studio/), et les ajouter ici.

Bien que j'aie [précédemment](https://ayusch.com/building-arcore-app-android-studio/) expliqué ce que font ces méthodes ligne par ligne, voici un aperçu :

* **PlaceObject** : Cette méthode est utilisée pour construire un renderable à partir de l'Uri fourni. Une fois le renderable construit, il est passé dans la méthode addNodeToScene où le renderable est attaché à un nœud et ce nœud est placé sur la scène.
* **AddNodeToScene** : Cette méthode crée un AnchorNode à partir de l'ancrage reçu, crée un autre nœud sur lequel le renderable est attaché, puis ajoute ce nœud à l'AnchorNode et ajoute l'AnchorNode à la scène.

Voici notre classe **MainActivity.java** finale :

```
package com.ayusch.augmentedimages;
```

```
import android.graphics.Bitmap;import android.graphics.BitmapFactory;import android.net.Uri;import android.os.Build;import android.support.annotation.RequiresApi;import android.support.v7.app.AppCompatActivity;import android.os.Bundle;import android.util.Log;import android.widget.Toast;
```

```
import com.google.ar.core.Anchor;import com.google.ar.core.AugmentedImage;import com.google.ar.core.AugmentedImageDatabase;import com.google.ar.core.Config;import com.google.ar.core.Frame;import com.google.ar.core.Session;import com.google.ar.core.TrackingState;import com.google.ar.sceneform.AnchorNode;import com.google.ar.sceneform.FrameTime;import com.google.ar.sceneform.rendering.ModelRenderable;import com.google.ar.sceneform.rendering.Renderable;import com.google.ar.sceneform.ux.ArFragment;import com.google.ar.sceneform.ux.TransformableNode;
```

```
import java.io.IOException;import java.io.InputStream;import java.util.Collection;
```

```
public class MainActivity extends AppCompatActivity {    ArFragment arFragment;    boolean shouldAddModel = true;
```

```
    @Override    protected void onCreate(Bundle savedInstanceState) {        super.onCreate(savedInstanceState);        setContentView(R.layout.activity_main);        arFragment = (CustomArFragment) getSupportFragmentManager().findFragmentById(R.id.sceneform_fragment);        arFragment.getPlaneDiscoveryController().hide();        arFragment.getArSceneView().getScene().addOnUpdateListener(this::onUpdateFrame);    }
```

```
    @RequiresApi(api = Build.VERSION_CODES.N)    private void placeObject(ArFragment arFragment, Anchor anchor, Uri uri) {        ModelRenderable.builder()                .setSource(arFragment.getContext(), uri)                .build()                .thenAccept(modelRenderable -> addNodeToScene(arFragment, anchor, modelRenderable))                .exceptionally(throwable -> {                            Toast.makeText(arFragment.getContext(), "Error:" + throwable.getMessage(), Toast.LENGTH_LONG).show();                            return null;                        }
```

```
                );    }
```

```
    @RequiresApi(api = Build.VERSION_CODES.N)    private void onUpdateFrame(FrameTime frameTime) {        Frame frame = arFragment.getArSceneView().getArFrame();
```

```
        Collection<AugmentedImage> augmentedImages = frame.getUpdatedTrackables(AugmentedImage.class);        for (AugmentedImage augmentedImage : augmentedImages) {            if (augmentedImage.getTrackingState() == TrackingState.TRACKING) {                if (augmentedImage.getName().equals("tiger") && shouldAddModel) {                    placeObject(arFragment, augmentedImage.createAnchor(augmentedImage.getCenterPose()), Uri.parse("Mesh_BengalTiger.sfb"));                    shouldAddModel = false;                }            }        }    }
```

```
    public boolean setupAugmentedImagesDb(Config config, Session session) {        AugmentedImageDatabase augmentedImageDatabase;        Bitmap bitmap = loadAugmentedImage();        if (bitmap == null) {            return false;        }
```

```
        augmentedImageDatabase = new AugmentedImageDatabase(session);        augmentedImageDatabase.addImage("tiger", bitmap);        config.setAugmentedImageDatabase(augmentedImageDatabase);        return true;    }
```

```
    private Bitmap loadAugmentedImage() {        try (InputStream is = getAssets().open("blanket.jpeg")) {            return BitmapFactory.decodeStream(is);        } catch (IOException e) {            Log.e("ImageLoad", "IO Exception", e);        }
```

```
        return null;    }
```

```
    private void addNodeToScene(ArFragment arFragment, Anchor anchor, Renderable renderable) {        AnchorNode anchorNode = new AnchorNode(anchor);        TransformableNode node = new TransformableNode(arFragment.getTransformationSystem());        node.setRenderable(renderable);        node.setParent(anchorNode);        arFragment.getArSceneView().getScene().addChild(anchorNode);        node.select();    }
```

```
}
```

Maintenant, exécutez votre application. Vous devriez voir un écran comme montré ci-dessous. Déplacez votre téléphone un peu au-dessus de l'objet de référence. ARCore détectera les points de fonctionnalité et dès qu'il détectera l'image de référence dans le monde réel, il ajoutera votre modèle 3D par-dessus.

[caption id="attachment_1000" align="aligncenter" width="1280"]

![Image](https://cdn-media-1.freecodecamp.org/images/C8OBR4vV4VsxKSeQ1wcr3U9KHCSnI0l56St1)
_J'ai utilisé ma couverture comme référence_

Avec cela, nous avons créé notre toute première application d'images augmentées en utilisant ARCore de Google et le SDK Sceneform !!

**Si vous souhaitez rester informé de tous les derniers articles, abonnez-vous à la newsletter hebdomadaire en entrant votre adresse e-mail dans le formulaire dans la section en haut à droite de cette page.**

_Vous aimez ce que vous lisez ? N'oubliez pas de partager cet article sur [**Facebook**](https://www.facebook.com/AndroidVille), **WhatsApp** et **LinkedIn**._

_Vous pouvez me suivre sur [LinkedIn](https://www.linkedin.com/in/ayuschjain), [Quora](https://www.quora.com/profile/Ayusch-Jain), [Twitter](https://twitter.com/ayuschjain) et [Instagram](https://www.instagram.com/androidville/) où je **réponds** aux questions liées au **développement mobile, en particulier Android et Flutter**._