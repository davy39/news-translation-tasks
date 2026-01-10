---
title: Comment j'ai construit un bouton rotatif Android avec Kotlin pour aider mon
  fils à pratiquer le piano
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-28T21:01:46.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-an-android-rotary-knob-using-kotlin
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/knob_cel.png
tags:
- name: android app development
  slug: android-app-development
- name: Kotlin
  slug: kotlin
seo_title: Comment j'ai construit un bouton rotatif Android avec Kotlin pour aider
  mon fils à pratiquer le piano
seo_desc: "By Oren Geva\nWhen my son's piano teacher told him he should use a metronome\
  \ to practice timing, I took it as an opportunity to learn Kotlin. I decided to\
  \ learn the language and Android's ecosystem so I could build a Metronome app. \n\
  My initial impleme..."
---

Par Oren Geva

Lorsque le professeur de piano de mon fils lui a dit qu'il devrait utiliser un métronome pour pratiquer le rythme, j'ai vu cela comme une opportunité d'apprendre Kotlin. J'ai décidé d'apprendre le langage et l'écosystème Android afin de pouvoir construire une application Métronome. 

Ma première implémentation utilisait une SeekBar pour contrôler le BPM (Battements par Minute) — le rythme auquel le métronome fait des ticks. 

Cependant, à mesure que le projet avançait, je voulais qu'il ressemble à une unité numérique physique, comme celle utilisée par de nombreux musiciens dans le monde physique réel.

Les unités physiques n'ont pas de "SeekBar View", et je voulais imiter le bouton rotatif qu'une unité réelle pourrait avoir.

Les boutons rotatifs sont des contrôles UI très utiles. Ils sont très similaires à un curseur ou une SeekBar, utilisables dans de nombreuses situations. Voici quelques-uns de leurs avantages :

* Ils consomment très peu d'espace dans votre application
* Ils peuvent être utilisés pour contrôler des plages de valeurs continues ou discrètes
* Ils sont immédiatement reconnaissables par les utilisateurs grâce aux applications du monde réel
* Ils ne sont pas des contrôles Android standard et confèrent ainsi une sensation "personnalisée" unique à votre application

Bien que quelques bibliothèques de boutons open source pour Android existent, je n'ai pas trouvé exactement ce que je cherchais dans aucune d'entre elles.

Beaucoup étaient trop complexes pour mes besoins modestes, avec des fonctionnalités telles que la définition d'images de fond ou la gestion des taps pour deux opérations de mode ou plus, etc. 
Certaines n'avaient pas la personnalisation que je voulais pour mon projet et venaient avec leur propre image de bouton. 

D'autres encore supposaient une plage discrète de valeurs ou de positions. Et beaucoup d'entre elles semblaient beaucoup plus complexes que nécessaire.

J'ai donc décidé de concevoir le mien — ce qui s'est transformé en un petit projet amusant en soi.

Dans cet article, je vais discuter de la manière dont je l'ai construit.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/app.png)
_L'application métronome résultante et son bouton rotatif_

Alors voyons comment nous pouvons créer un bouton rotatif.

# Concevoir un bouton

La première étape consistait à créer le graphique du bouton lui-même. Je ne suis pas designer, mais il m'est venu à l'esprit que la clé pour créer une sensation de "profondeur" et de mouvement dans un contrôle de bouton serait d'utiliser un dégradé radial décentré. Cela me permettrait de créer l'illusion d'une surface enfoncée et d'une réflexion de la lumière.

J'ai utilisé Sketch pour dessiner le bouton, puis je l'ai exporté en svg. Ensuite, je l'ai réimporté dans Android Studio en tant que drawable.

Vous pouvez trouver le drawable du bouton dans le lien du projet GitHub en bas de cet article.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/knob.png)

# Créer la vue en xml

La première étape pour créer la Vue consiste à créer un fichier xml de mise en page dans le dossier res/layout.

La vue peut être entièrement créée en code, mais une bonne Vue réutilisable dans Android doit être créée en xml.

Remarquez la balise <merge> — nous l'utiliserons puisque nous allons étendre une classe de mise en page Android existante et cette mise en page sera la structure interne de cette mise en page.

Nous utiliserons une ImageView pour le bouton, que nous ferons tourner lorsque l'utilisateur le déplace.

```xml
<?xml version="1.0" encoding="utf-8"?>
<merge xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content">

    <ImageView
        android:id="@+id/knobImageView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        />
</merge>
```

Pour rendre le bouton configurable par xml, nous allons créer des attributs pour la plage de valeurs que le bouton retournera, ainsi que pour le drawable qu'il utilisera pour les visuels.

Nous allons créer un fichier attrs.xml sous res/values.

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <declare-styleable name="RotaryKnobView">
        <attr name="minValue" format="integer" />
        <attr name="maxValue" format="integer" />
        <attr name="initialValue" format="integer" />
        <attr name="knobDrawable" format="reference" />
    </declare-styleable>
</resources>
```

Ensuite, créez un nouveau fichier de classe Kotlin, RotaryKnobView, qui étend RelativeLayout et implémente l'interface GestureDetector.OnGestureListener.

Nous utiliserons RelativeLayout comme conteneur parent pour le contrôle, et implémenter OnGestureListener pour gérer les gestes de mouvement du bouton.

[@JvmOverloads](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.jvm/-jvm-overloads/) est simplement un raccourci pour remplacer les trois versions du constructeur de la Vue.

Ensuite, nous initialiserons quelques valeurs par défaut et définirons les membres de la classe.

```kotlin
class RotaryKnobView @JvmOverloads constructor(
    context: Context, attrs: AttributeSet? = null, defStyleAttr: Int = 0
) : RelativeLayout(context, attrs, defStyleAttr), GestureDetector.OnGestureListener {
    private val gestureDetector: GestureDetectorCompat
    private var maxValue = 99
    private var minValue = 0
    var listener: RotaryKnobListener? = null
    var value = 50
    private var knobDrawable: Drawable? = null
    private var divider = 300f / (maxValue - minValue)
```

Une note sur la variable divider — Je voulais que le bouton ait des positions de début et de fin, plutôt que de pouvoir tourner indéfiniment, un peu comme un bouton de volume sur une chaîne stéréo. J'ai défini les points de début et de fin à -150 et 150 degrés, respectivement. Ainsi, le mouvement effectif pour le bouton n'est que de 300 degrés. 

Nous utiliserons le divider pour distribuer la plage de valeurs que nous voulons que notre bouton retourne sur ces 300 degrés disponibles — afin que nous puissions calculer la valeur réelle en fonction de l'angle de position du bouton.

Ensuite, nous initialisons le composant :

* Gonfler la mise en page.
* Lire les attributs dans les variables.
* Mettre à jour le divider (pour supporter les valeurs minimales et maximales passées.
* Définir l'image.

```kotlin
    init {
        this.maxValue = maxValue + 1

        LayoutInflater.from(context)
            .inflate(R.layout.rotary_knob_view, this, true)

        context.theme.obtainStyledAttributes(
            attrs,
            R.styleable.RotaryKnobView,
            0,
            0
        ).apply {
            try {
                minValue = getInt(R.styleable.RotaryKnobView_minValue, 0)
                maxValue = getInt(R.styleable.RotaryKnobView_maxValue, 100) + 1
                divider = 300f / (maxValue - minValue)
                value = getInt(R.styleable.RotaryKnobView_initialValue, 50)
                knobDrawable = getDrawable(R.styleable.RotaryKnobView_knobDrawable)
                knobImageView.setImageDrawable(knobDrawable)
            } finally {
                recycle()
            }
        }
        gestureDetector = GestureDetectorCompat(context, this)
    }
```

La classe ne compilera pas encore, car nous devons implémenter les fonctions de OnGestureListener. Occupons-nous de cela maintenant.

# Détecter les gestes de l'utilisateur

L'interface OnGestureListener nécessite que nous implémentions six fonctions : onScroll, onTouchEvent, onDown, onSingleTapUp, onFling, onLongPress, onShowPress.

Parmi celles-ci, nous devons consommer (retourner true) sur onDown et onTouchEvent, et implémenter la logique de mouvement dans onScroll.

```kotlin
    override fun onTouchEvent(event: MotionEvent): Boolean {
        return if (gestureDetector.onTouchEvent(event))
            true
        else
            super.onTouchEvent(event)
    }

    override fun onDown(event: MotionEvent): Boolean {
        return true
    }

    override fun onSingleTapUp(e: MotionEvent): Boolean {
        return false
    }

    override fun onFling(arg0: MotionEvent, arg1: MotionEvent, arg2: Float, arg3: Float)
            : Boolean {
        return false
    }

    override fun onLongPress(e: MotionEvent) {}

    override fun onShowPress(e: MotionEvent) {}
```

Voici l'implémentation de onScroll. Nous remplirons les parties manquantes dans le paragraphe suivant.

```kotlin
    override fun onScroll(e1: MotionEvent, e2: MotionEvent, distanceX: Float, distanceY: Float)
            : Boolean {

        val rotationDegrees = calculateAngle(e2.x, e2.y)
        // utiliser uniquement la plage de -150 à 150 (points min/max du bouton
        if (rotationDegrees >= -150 && rotationDegrees <= 150) {
            setKnobPosition(rotationDegrees)

            // Calculer la valeur rotative
            // La plage est les 300 degrés entre -150 et 150, donc nous ajouterons 150 pour ajuster la
            // plage à 0 - 300
            val valueRangeDegrees = rotationDegrees + 150
                value = ((valueRangeDegrees / divider) + minValue).toInt()
                if (listener != null) listener!!.onRotate(value)
        }
        return true
    }
```

onScroll reçoit deux ensembles de coordonnées, e1 et e2, représentant les mouvements de début et de fin du défilement qui a déclenché l'événement.

Nous ne nous intéressons qu'à e2 — la nouvelle position du bouton — afin que nous puissions l'animer en position et calculer la valeur.

J'utilise une fonction que nous passerons en revue dans la section suivante pour calculer l'angle de rotation.

Comme mentionné précédemment, nous n'utilisons que 300 degrés du point de départ du bouton à son point final, donc ici nous calculons également quelle valeur la position du bouton doit représenter en utilisant le divider.

# Calculer l'angle de rotation

Maintenant, écrivons la fonction calculateAngle.

```kotlin
    private fun calculateAngle(x: Float, y: Float): Float {
        val px = (x / width.toFloat()) - 0.5
        val py = ( 1 - y / height.toFloat()) - 0.5
        var angle = -(Math.toDegrees(atan2(py, px)))
            .toFloat() + 90
        if (angle > 180) angle -= 360
        return angle
    }
```

Cette fonction nécessite une explication et quelques mathématiques de niveau 8ème.

Le but de cette fonction est de calculer la position du bouton en angles, en fonction des coordonnées passées.

J'ai choisi de traiter la position 12 heures du bouton comme zéro, puis d'augmenter sa position à des degrés positifs lors de la rotation dans le sens des aiguilles d'une montre, et de réduire à des degrés négatifs lors de la rotation dans le sens inverse des aiguilles d'une montre à partir de 12 heures.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/angle.png)

Nous obtenons les coordonnées x, y de la fonction onScroll, indiquant la position dans la vue où le mouvement s'est terminé (pour cet événement).

X et y représentent un point sur un système de coordonnées cartésien. Nous pouvons convertir cette représentation de point en un système de coordonnées polaires, représentant le point par l'angle au-dessus ou en dessous de l'axe x et la distance du point par rapport au pôle.

La conversion entre les deux systèmes de coordonnées peut être effectuée avec la [fonction atan2](https://en.wikipedia.org/wiki/Polar_coordinate_system#Converting_between_polar_and_Cartesian_coordinates). Heureusement pour nous, la bibliothèque mathématique Kotlin nous fournit une implémentation de atan2, comme le font la plupart des bibliothèques Math.

Nous devons cependant tenir compte de quelques différences entre notre modèle de bouton et l'implémentation mathématique naïve.

1. Les coordonnées (0,0) représentent le coin supérieur droit de la vue et non le milieu. Et tandis que la coordonnée x progresse dans la bonne direction — augmentant à mesure que nous nous déplaçons vers la droite — la coordonnée y est inversée — 0 est le haut de la vue, tandis que la valeur de la hauteur de notre vue est la ligne de pixels la plus basse dans la vue. 
Pour accommoder cela, nous divisons x et y par la largeur et la hauteur respective de la vue pour les obtenir sur une échelle normalisée de 0–1. 
Ensuite, nous soustrayons 0,5 des deux pour déplacer le point 0,0 au milieu. 
Et enfin, nous soustrayons la valeur de y de 1 pour inverser sa direction.
2. Le système de coordonnées polaires est dans la direction inverse de ce dont nous avons besoin. La valeur des degrés augmente à mesure que nous tournons dans le sens inverse des aiguilles d'une montre. Nous ajoutons donc un signe moins pour inverser le résultat de la fonction atan2.
3. Nous voulons que la valeur 0 degré pointe vers le nord, sinon en passant 9 heures, la valeur passera de 0 à 359. 
Nous ajoutons donc 90 au résultat, en prenant soin de réduire la valeur de 360 une fois que l'angle est supérieur à 180 (afin que nous obtenions une plage de -180 < angle < 180 plutôt qu'une plage de 0 < x < 360)

L'étape suivante consiste à animer la rotation du bouton. Nous utiliserons [Matrix](https://developer.android.com/reference/kotlin/android/graphics/Matrix) pour transformer les coordonnées de l'ImageView.

Nous devons simplement faire attention à diviser la hauteur et la largeur de la vue par 2 afin que l'axe de rotation soit le milieu du bouton.

```kotlin
    private fun setKnobPosition(angle: Float) {
        val matrix = Matrix()
        knobImageView.scaleType = ScaleType.MATRIX
        matrix.postRotate(angle, width.toFloat() / 2, height.toFloat() / 2)
        knobImageView.imageMatrix = matrix
    }
```

Et enfin, mais non des moindres, exposons une interface pour que l'Activity ou le Fragment consommateur écoute les événements de rotation :

```kotlin
    interface RotaryKnobListener {
        fun onRotate(value: Int)
    }
```

# Utiliser le bouton

Maintenant, créons une implémentation simple pour tester notre bouton.

Dans l'activité principale, créons un TextView et faisons glisser une vue depuis la liste des conteneurs. Lorsque la sélection de la vue est présentée, sélectionnez RotaryKnobView.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/designer.png)

Modifiez le fichier xml de mise en page de l'activité, et définissez les valeurs minimale, maximale et initiale ainsi que le drawable à utiliser.

```xml
    <geva.oren.rotaryknobdemo.RotaryKnobView
        android:id="@+id/knob"
        class="geva.oren.rotaryknobdemo.RotaryKnobView"
        android:layout_width="@dimen/knob_width"
        android:layout_height="@dimen/knob_height"
        android:layout_marginBottom="312dp"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toBottomOf="@+id/textView"
        app:knobDrawable="@drawable/ic_rotary_knob"
        app:initialValue="50"
        app:maxValue="100"
        app:minValue="0" />
```

Enfin, dans notre classe MainActivity, gonfler la mise en page et implémenter l'interface RotaryKnobListener pour mettre à jour la valeur du TextField.

```kotlin
package geva.oren.rotaryknobdemo

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity(), RotaryKnobView.RotaryKnobListener {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        knob.listener = this
        textView.text = knob.value.toString()
    }

    override fun onRotate(value: Int) {
        textView.text = value.toString()
    }
}
```

Et nous avons terminé ! Ce projet d'exemple est disponible sur [github](https://github.com/o4oren/kotlin-rotary-knob) ainsi que le projet original [metronome](https://github.com/o4oren/android-kotlin-metronome).

L'application Android Metronome est également disponible sur le [Google Play Store](https://play.google.com/store/apps/details?id=geva.oren.android_kotlin_metronome).