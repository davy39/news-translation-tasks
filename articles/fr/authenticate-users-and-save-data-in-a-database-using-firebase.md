---
title: Comment authentifier les utilisateurs et sauvegarder des données dans une base
  de données en utilisant Firebase
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2020-11-04T18:54:33.000Z'
originalURL: https://freecodecamp.org/news/authenticate-users-and-save-data-in-a-database-using-firebase
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/0_pKW2Wv94Bq6vOE-G.jpg
tags:
- name: authentication
  slug: authentication
- name: database
  slug: database
- name: Firebase
  slug: firebase
seo_title: Comment authentifier les utilisateurs et sauvegarder des données dans une
  base de données en utilisant Firebase
seo_desc: "When you go about building an application, there are a ton of things to\
  \ consider. And those are all mainly concerned with the client part of the project.\
  \ \nWhen you start to think about the server for your application, things can get\
  \ pretty complicate..."
---

Lorsque vous vous lancez dans la construction d'une application, il y a une tonne de choses à considérer. Et celles-ci concernent principalement la partie client du projet.

Lorsque vous commencez à réfléchir au serveur de votre application, les choses peuvent devenir assez compliquées. Une façon d'alléger cette pression est d'utiliser Firebase – et deux fonctionnalités en particulier :

1. Authentifier les utilisateurs en utilisant Firebase Auth
2. Stocker des données en utilisant une base de données en temps réel

Dans cet article, vous apprendrez :

* Comment construire une application Android en Kotlin qui authentifie les utilisateurs avec Firebase Auth
* Comment utiliser Retrofit2 pour faire des requêtes à votre serveur
* Comment construire un serveur en Node.js avec Express qui recevra les requêtes de votre application et récupérera des données depuis une base de données en temps réel dans Firebase

Tout cela peut sembler une tâche simple, mais ce n'est pas le cas. Il y a beaucoup de configuration à faire et nous devons gérer diverses configurations également. Mais je vais également souligner quelques pièges qui vous aideront à gagner du temps et à éviter des frustrations.

**Faites-moi confiance - vous voulez apprendre de mes erreurs.**

Si vous souhaitez sauter toutes les explications, vous pouvez vous rendre en bas de l'article et voir le code source complet via les liens.

Ok, commençons.

## Installation de votre projet

Notre application se composera à la fois d'un front-end et d'un back-end. Du point de vue du front-end, il y aura une page de connexion/inscription et une autre page qui récupérera/enverra des données aléatoires à notre base de données.

Nous utiliserons ici Firebase Authentication pour valider les utilisateurs enregistrés. Il existe plusieurs façons d'authentifier les utilisateurs :

* Email et mot de passe
* Compte Google/Facebook/Twitter/Github (ce qu'on appelle l'identification par fournisseur d'identité fédéré)
* Numéro de téléphone
* Autorisation personnalisée
* Autorisation anonyme

Dans notre application, nous utiliserons l'option Email et mot de passe, car c'est l'approche la plus directe (et dans la plupart des cas, la solution la plus courante).

Cette authentification aura lieu dans notre client et il n'y aura pas besoin de communication avec notre back-end pour cette tâche.

Pour faire des requêtes à notre serveur, nous utiliserons [Retrofit2](https://square.github.io/retrofit/) en faisant des requêtes GET. Dans ces requêtes GET, nous enverrons les données qui doivent être mises à jour ainsi qu'un token (plus d'informations sur le token dans la section Serveur).

Du côté du back-end, notre serveur est responsable de l'acceptation des requêtes des utilisateurs utilisant notre application pour récupérer/enregistrer/supprimer des données (ou [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)).

Pour permettre aux utilisateurs authentifiés d'accéder à la base de données, nous devrons utiliser le [SDK Admin de Firebase](https://firebase.google.com/docs/admin/setup). Ce framework nous donnera accès à une API pour vérifier les utilisateurs authentifiés et transmettre les requêtes à notre base de données.

Nous enregistrerons les données des utilisateurs en utilisant la [base de données en temps réel de Firebase](https://firebase.google.com/docs/database). Une fois tout terminé du côté back-end, nous le déployerons via [Heroku](https://www.heroku.com/).

![Image](https://www.freecodecamp.org/news/content/images/2020/11/0_yDHPQePmp9hHocqi.jpg)
_Photo par [dylan nolte](https://unsplash.com/@dylan_nolte?utm_source=medium&amp;utm_medium=referral) sur Unsplash_

### Comment construire le côté client/UI

Après avoir ouvert un nouveau projet Kotlin, nous devons importer certaines dépendances. Tout d'abord, vous devez ajouter Firebase à votre projet.

[Suivez les étapes décrites ici](https://firebase.google.com/docs/android/setup#console) pour le faire.

Une fois cela fait, ajoutez la dépendance suivante à votre fichier build.gradle au niveau de l'application :

```java
implementation 'com.google.firebase:firebase-auth:19.4.0'
```

Lorsque les utilisateurs ouvrent l'application, ils peuvent soit se connecter, soit s'inscrire (si c'est leur première fois).

Puisque nous avons convenu que les utilisateurs seront validés sur la base d'une combinaison de leur email et de leur mot de passe, nous créerons une activité simple qui a deux EditTexts pour faire exactement cela. Nous aurons également deux boutons pour signifier le choix de s'inscrire ou de se connecter.

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:orientation="vertical" android:layout_width="match_parent"
    android:layout_height="match_parent">

    <EditText
        android:id="@+id/email_edit_text"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:ems="10"
        android:hint="Entrez votre email"
        android:inputType="textEmailAddress"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent"
        app:layout_constraintVertical_bias="0.153" />

    <EditText
        android:id="@+id/password_edit_text"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:ems="10"
        android:hint="Entrez votre mot de passe"
        android:inputType="textPassword"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toBottomOf="@+id/email_edit_text"
        app:layout_constraintVertical_bias="0.046" />

    <Button
        android:id="@+id/Login"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Connexion"
        android:background="#39e600"
        android:onClick="loginUser"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintHorizontal_bias="0.139"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toBottomOf="@+id/password_edit_text"
        app:layout_constraintVertical_bias="0.146" />

    <Button
        android:id="@+id/Signup"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Inscription"
        android:background="#4d94ff"
        android:onClick="signupUser"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintHorizontal_bias="0.647"
        app:layout_constraintStart_toEndOf="@+id/Login"
        app:layout_constraintTop_toBottomOf="@+id/password_edit_text"
        app:layout_constraintVertical_bias="0.146" />
</androidx.constraintlayout.widget.ConstraintLayout>
```

```kotlin
package com.tomerpacific.todo.activities

import android.content.Intent
import android.os.Bundle
import android.view.KeyEvent
import android.view.View
import android.view.inputmethod.EditorInfo
import android.widget.EditText
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.google.android.gms.tasks.OnCompleteListener
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.auth.UserProfileChangeRequest
import com.tomerpacific.todo.R

class LoginActivity : AppCompatActivity() {

    private var userEmail : String = ""
    private var userPassword: String = ""

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)
      
      // DÉBUT 1 ---------------------- //

        findViewById<EditText>(R.id.email_edit_text).apply {
            setOnEditorActionListener {_, actionId, keyEvent ->
                if (actionId == EditorInfo.IME_ACTION_SEARCH || actionId == EditorInfo.IME_ACTION_DONE ||
                    keyEvent == null ||
                    keyEvent.keyCode == KeyEvent.KEYCODE_ENTER) {
                    userEmail = text.toString()
                }
                false
            }

            setOnFocusChangeListener {view, gainedFoucs ->
                userEmail = text.toString()
            }
        }

        findViewById<EditText>(R.id.password_edit_text).apply {
            setOnEditorActionListener {_, actionId, keyEvent ->
                if (actionId == EditorInfo.IME_ACTION_SEARCH || actionId == EditorInfo.IME_ACTION_DONE ||
                    keyEvent == null ||
                    keyEvent.keyCode == KeyEvent.KEYCODE_ENTER) {
                    userPassword = text.toString()
                }
                false
            }

            setOnFocusChangeListener {view, gainedFoucs ->
                userPassword = text.toString()
            }
        }
      
      // FIN 1 ---------------------------------------- //
    }

    override fun onStart() {
        super.onStart()
        FirebaseAuth.getInstance().currentUser?.let {
            Intent(this@LoginActivity, MainActivity::class.java).apply {
                startActivity(this)
            }
        }
    }

  // DÉBUT 2 ----------------------- //
    fun loginUser(view : View) {

        if (userEmail.isEmpty() || userPassword.isEmpty()) {
            Toast.makeText(this, "Veuillez vous assurer de remplir votre email et votre mot de passe", Toast.LENGTH_SHORT).show()
            return
        }

        FirebaseAuth.getInstance().signInWithEmailAndPassword(userEmail, userPassword)
            .addOnCompleteListener(this) { task ->
                if (task.isSuccessful) {
                    updateFirebaseUserDisplayName()
                } else {
                    Toast.makeText(this, "Une erreur est survenue lors de la connexion. Veuillez réessayer plus tard.", Toast.LENGTH_SHORT).show()
                }
            }
    }
  
  // FIN 2 ----------------------------- //

  // DÉBUT 3 --------------------------- //
    fun signupUser(view: View) {

        if (userEmail.isEmpty() || userPassword.isEmpty()) {
            Toast.makeText(this, "Veuillez vous assurer de remplir votre email et votre mot de passe", Toast.LENGTH_SHORT).show()
            return
        }

        FirebaseAuth.getInstance().createUserWithEmailAndPassword(userEmail, userPassword)
            .addOnCompleteListener(this) { task ->
                if (task.isSuccessful) {
                    updateFirebaseUserDisplayName()
                } else {
                    Toast.makeText(this, "Une erreur est survenue lors de l'inscription. Veuillez réessayer plus tard.", Toast.LENGTH_SHORT).show()
                }
            }
    }

    private fun updateFirebaseUserDisplayName() {

        FirebaseAuth.getInstance().currentUser?.apply {
            val profileUpdates : UserProfileChangeRequest = UserProfileChangeRequest.Builder().setDisplayName(userEmail).build()
            updateProfile(profileUpdates)?.addOnCompleteListener(OnCompleteListener {
                when(it.isSuccessful) {
                    true -> apply {
                        Intent(this@LoginActivity, MainActivity::class.java).apply {
                            startActivity(this)
                            finish()
                        }
                    }
                    false -> Toast.makeText(this@LoginActivity, "La connexion a échoué", Toast.LENGTH_SHORT).show()
                }
            })
        }
    }
  // FIN 3 ------------------------------------- //

}
```

Voyons ce qui se passe dans le code ci-dessus.

1. Nous attachons des écouteurs à nos champs de texte pour identifier quand ils ont perdu le focus ou quand l'utilisateur a appuyé sur le bouton terminé.
2. La méthode loginUser est responsable de l'authentification de l'utilisateur sur la base de ses identifiants précédents (en utilisant l'API signInWithEmailAndPassword).
3. La méthode signupUser utilise l'API createUserWithEmailAndPassword.
4. Vous pouvez voir que nous avons remplacé la méthode de cycle de vie **onStart** pour identifier quand l'utilisateur revient à l'application et pour mettre à jour l'UI de manière appropriée si l'utilisateur est déjà connecté.

Lorsque nous exécutons notre application, nous verrons ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/1_q4L52_29VKSTqAkOOqOL2w.png)
_Rien de trop fantaisiste_

C'était la partie facile. Avant de passer à l'écriture de la logique pour communiquer avec le back-end, construisons d'abord le back-end.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/0_wsSbgrjdHy9ZUZgn.jpg)
_Photo par [Roger Starnes Sr](https://unsplash.com/@rstar50?utm_source=medium&amp;utm_medium=referral) sur Unsplash_

### Comment configurer le serveur

Nous utiliserons Express pour construire notre serveur. Ci-dessous se trouve un modèle pour un tel serveur qui ajoute également des en-têtes pour contourner les problèmes CORS que nous pourrions rencontrer :

```node.js
const express = require('express')
var bodyParser = require('body-parser')
const app = express()
var port = process.env.PORT || 3000

app.use(bodyParser.urlencoded())

app.use(function(req, res, next) {
  res.setHeader('Access-Control-Allow-Origin', '*')
  res.header('Access-Control-Allow-Methods', 'GET, OPTIONS')
  res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
  res.header('Access-Control-Allow-Credentials', true)
  return next()
});

app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`))
```

De manière similaire à ce que nous avons fait dans le client, nous devons également ajouter Firebase à notre serveur Node.js. Si vous vous souvenez des étapes que vous avez suivies pour créer un projet dans Firebase et que vous avez choisi un projet Android, vous devez ajouter à ce projet une autre application qui représentera notre serveur. En cliquant sur Ajouter une application dans l'écran principal de la console Firebase,

![Image](https://www.freecodecamp.org/news/content/images/2020/11/1_D5U2pOM8pvb73KFPCPyYdg.png)

Vous serez présenté avec une plateforme à choisir :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/1_g5MOxShv5H07Cw_QFEJ61Q.png)
_Vous devez choisir l'option Web (celle avec l'icône &lt;/&gt;)_

Après avoir fait la configuration initiale dans la console Firebase, vous devrez ajouter l'objet de configuration à votre projet :

```node.js
var firebaseConfig = {
  apiKey: "API_KEY",
  authDomain: "PROJECT_ID.firebaseapp.com",
  databaseURL: "https://PROJECT_ID.firebaseio.com",
  projectId: "PROJECT_ID",
  storageBucket: "PROJECT_ID.appspot.com",
  messagingSenderId: "SENDER_ID",
  appId: "APP_ID",
  measurementId: "G-MEASUREMENT_ID",
};
```

Nous placerons ces configurations dans notre fichier principal (app.js) :

```node.js
const express = require('express')
var bodyParser = require('body-parser')
const app = express()
var port = process.env.PORT || 3000

<--- CONFIGURATION FIREBASE --->
var firebaseConfig = {
  apiKey: "API_KEY",
  authDomain: "PROJECT_ID.firebaseapp.com",
  databaseURL: "https://PROJECT_ID.firebaseio.com",
  projectId: "PROJECT_ID",
  storageBucket: "PROJECT_ID.appspot.com",
  messagingSenderId: "SENDER_ID",
  appId: "APP_ID",
  measurementId: "G-MEASUREMENT_ID",
};
  
  // Initialiser Firebase
firebase.initializeApp(firebaseConfig);
<---- FIN CONFIGURATION FIREBASE --->

app.use(bodyParser.urlencoded())

app.use(function(req, res, next) {
  res.setHeader('Access-Control-Allow-Origin', '*')
  res.header('Access-Control-Allow-Methods', 'GET, OPTIONS')
  res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
  res.header('Access-Control-Allow-Credentials', true)
  return next()
});

app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`))
```

Vous pourriez penser : « Je sauvegarde toutes ces informations secrètes dans le client. Elles seront visibles par tout le monde ! ». C'est complètement vrai, mais dans le cas de Firebase, c'est acceptable.

### Comment configurer la base de données

Nous y arrivons, mais nous avons encore quelques configurations à faire. Cette fois, cela concerne notre base de données en temps réel.

Rendez-vous dans votre console Firebase et choisissez le projet que vous avez créé précédemment dans cet article. Dans le menu de gauche, vous verrez une option Realtime Database. Cliquez dessus.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/1_OS0GNYQgtF2GAEBDup02hQ.png)

Ensuite, sur le côté droit, une fenêtre se chargera avec les onglets suivants :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/1_fnyDO96rxl8mmBE0XQbI2A.png)

Sous l'onglet Données, vous trouverez l'URL de votre base de données. Retenez-la car nous en aurons besoin plus tard.

L'autre onglet important à consulter est l'onglet Règles. Ces règles spécifient qui a accès à votre base de données et ce qu'ils peuvent y faire.

Initialement (et à des fins de test), les règles sont assez laxistes et permettent à quiconque de lire et d'écrire dans votre base de données. **Avant de rendre votre application publique, assurez-vous de mettre à jour ces règles avec quelque chose de plus restrictif**. Ne vous inquiétez pas, vous verrez un exemple.

### Comment configurer le SDK Admin de Firebase

Ensuite, nous devons configurer le [SDK Admin de Firebase](https://firebase.google.com/docs/admin/setup). Puisque nous avons déjà configuré les éléments nécessaires dans la console Firebase, nous devons installer le package admin de firebase.

```bash
npm install firebase-admin --save
```

Maintenant, nous devons générer une clé privée puisque notre projet est un compte de service. Dans la console Firebase, suivez ces étapes :

Tout d'abord, à côté de l'aperçu du projet, il y a une icône d'engrenage. Cliquez dessus et choisissez **Paramètres du projet** :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/1_aWjJKvMCZM3DaiX5cukmsQ.png)

Ensuite, cliquez sur l'onglet Comptes de service, et cliquez sur le bouton Créer un compte de service.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/1_cqdWHjt64JUauzNgik5Hcg.jpeg)

Choisissez Node.js comme extrait de configuration, et cliquez sur **Générer une nouvelle clé privée**.

Placez ce fichier dans votre projet et changez le chemin d'accès dans l'extrait de code fourni par Firebase.

⚠️ Assurez-vous d'exclure ce fichier dans votre fichier .gitignore et de ne jamais le télécharger sur un dépôt public.

En mettant tout cela ensemble, notre fichier app.js ressemblera à ceci :

```node.js
const express = require('express')
var bodyParser = require('body-parser')
const app = express()
var port = process.env.PORT || 3000

<--- CONFIGURATION FIREBASE --->
var firebaseConfig = {
  apiKey: "API_KEY",
  authDomain: "PROJECT_ID.firebaseapp.com",
  databaseURL: "https://PROJECT_ID.firebaseio.com",
  projectId: "PROJECT_ID",
  storageBucket: "PROJECT_ID.appspot.com",
  messagingSenderId: "SENDER_ID",
  appId: "APP_ID",
  measurementId: "G-MEASUREMENT_ID",
};
  
  // Initialiser Firebase
firebase.initializeApp(firebaseConfig);
<---- FIN CONFIGURATION FIREBASE --->

const serviceAccount = require("PATH_TO_YOUR_SERVICE_ACCOUNT_FILE.json");

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "URL_TO_DATABASE"
});  
  
app.use(bodyParser.urlencoded())

app.use(function(req, res, next) {
  res.setHeader('Access-Control-Allow-Origin', '*')
  res.header('Access-Control-Allow-Methods', 'GET, OPTIONS')
  res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
  res.header('Access-Control-Allow-Credentials', true)
  return next()
});

app.listen(port, () => console.log(`app listening at http://localhost:${port}`))
```

Vous souvenez-vous de l'URL de la base de données dont j'ai parlé plus tôt ? Vous devrez l'insérer dans l'objet que vous passez à la méthode initializeApp de l'admin de Firebase.

### Comment créer un point de terminaison et déployer

Ouf, cela a été beaucoup de configuration. Pour l'instant, notre serveur est capable de fonctionner, mais il ne fera rien puisque aucun point de terminaison n'est configuré.

Pour remédier à cette situation, définissons l'un de nos points de terminaison :

```node.js
app.get('/getData', function (req, res) {
  if (req.headers.authtoken) {
    admin.auth().verifyIdToken(req.headers.authtoken)
    .then(() => {
      var database = admin.database()
      var uid = req.query.uid
      database.ref('/users/' + uid).once('value')
      .then(function(snapshot) {
        var data = snapshot.val() ? snapshot.val() : []
        res.status(200).send({ our_data: data})
      }).catch(function(error) {
        res.status(500).json({ error: error})
      })
    }).catch(() => {
      res.status(403).send('Non autorisé')
    })
  } else {
    res.status(403).send('Non autorisé')
  }
})
```

Notre point de terminaison s'appelle getData et vous pouvez voir que avant de faire toute autre logique, nous extrayons le authtoken envoyé et le vérifions en utilisant Firebase admin.

Si tout fonctionne correctement, nous procédons à l'obtention de l'ID de l'utilisateur et utilisons celui-ci pour récupérer les données de l'utilisateur depuis la base de données.

## Comment faire les requêtes sur le client

Comme je l'ai mentionné précédemment, nous utiliserons Retrofit2 pour faire nos requêtes au serveur.

Je ne vais pas entrer dans les détails de l'utilisation de Retrofit2 ici (il y a beaucoup d'articles qui le font), donc ci-dessous vous pouvez trouver l'implémentation standard de la réalisation de requêtes réseau en utilisant Retrofit2.

```node.js
fun fetchDataFromDB() {
        val user = FirebaseAuth.getInstance().currentUser

        if (user != null) {
            user.getIdToken(false).addOnCompleteListener{
                if (it.isSuccessful) {
                    val token = it.result?.token

                    val retrofit = Retrofit.Builder()
                        .baseUrl(TodoConstants.BASE_URL_FOR_REQUEST)
                        .addConverterFactory(GsonConverterFactory.create())
                        .build()
                    val service = retrofit.create(DataService::class.java)
                    val call = service.getData(token, getUserUUID())

                    call.enqueue(object: Callback<Result> {
                        override fun onResponse(call: Call<Result>, response: Response<Result>) {
                            if (response.isSuccessful) {
                                val body = response.body() as Result
                               //Ici nous avons les données renvoyées par le serveur
                            }
                        }

                        override fun onFailure(call: Call<Result>, t: Throwable) {

                        }
                    })
                }
            }
        }
    }
```

Remarquez qu'après avoir obtenu l'objet FirebaseUser, nous utilisons la méthode getIdToken pour extraire le token qui sera envoyé au serveur.

De la même manière, nous pouvons créer une autre requête GET pour définir des données dans notre base de données.

Et c'est tout ! Merci d'avoir suivi.

Cet article est basé sur ce que j'ai traversé lors de la construction de ma propre application. Vous pouvez la consulter ci-dessous (le code source est également disponible) :

%[https://play.google.com/store/apps/details?id=com.tomerpacific.todo]

%[https://github.com/TomerPacific/Todo]