---
title: Comment créer une application de messagerie Android avec présence en ligne
  en utilisant Kotlin
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-05T17:56:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-android-messenger-app-with-online-presence-using-kotlin-fdcb3ea9e73b
coverImage: https://cdn-media-1.freecodecamp.org/images/0*i_KPqp4Nk6gx3M0j.gif
tags:
- name: Android
  slug: android
- name: Apps
  slug: apps-tag
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment créer une application de messagerie Android avec présence en ligne
  en utilisant Kotlin
seo_desc: 'By Neo Ighodaro

  When building a chat application, it is essential to have an online presence feature.
  It is essential because your users will like to know when their friends are online,
  and are more likely to respond to their messages in real time.

  I...'
---

Par Neo Ighodaro

Lors de la création d'une application de chat, il est essentiel d'avoir une fonctionnalité de présence en ligne. Elle est essentielle car vos utilisateurs aimeront savoir quand leurs amis sont en ligne et sont plus susceptibles de répondre à leurs messages en temps réel.

Dans cet article, nous allons créer une application de messagerie avec présence en ligne en utilisant Pusher Channels, Kotlin et Node.js.

Voici une démonstration de ce que nous allons construire :

![Image](https://cdn-media-1.freecodecamp.org/images/dCDSVxz21CA4S8Q6au2enLthTSoZgklQu0XN)

### Prérequis

Pour suivre ce tutoriel, vous avez besoin des éléments suivants :

* Une application Pusher Channel. Vous pouvez en créer une [ici](https://pusher.com/channels).
* Android Studio installé sur votre machine. Vous pouvez vérifier [ici](https://developer.android.com/studio/index.html) pour la dernière version stable. Une version minimale de 3.0 est recommandée.
* Connaissance de base du développement Android et de l'IDE Android Studio.
* Connaissance de base de Kotlin. Voici les [docs officiels](https://kotlinlang.org/docs/reference/).
* Node.js et NPM (Node Package Manager) installés sur votre machine. Téléchargez [ici](https://nodejs.org/en/).
* Mongo DB installé sur votre machine. Vous pouvez l'installer en suivant les instructions [ici](https://docs.mongodb.com/manual/installation/).

Une certaine familiarité avec le développement Android est également requise.

### Construction du serveur backend

Notre serveur sera construit en utilisant Node.js. Pour commencer, créez un nouveau répertoire de projet :

```
$ mkdir backend-server
```

Ensuite, créez un nouveau fichier `index.js` à l'intérieur du répertoire de projet et collez le code suivant :

```
// Fichier : ./index.js    var express = require('express');    var bodyParser = require('body-parser');    const mongoose = require('mongoose');    var Pusher = require('pusher');
```

```
    var app = express();
```

```
    app.use(bodyParser.json());    app.use(bodyParser.urlencoded({ extended: false }));
```

```
    var pusher = new Pusher({      appId: 'PUSHER_APP_ID',      key: 'PUSHER_APP_KEY',      secret: 'PUSHER_APP_SECRET',      cluster: 'PUSHER_APP_CLUSTER'    });
```

```
    mongoose.connect('mongodb://127.0.0.1/db');
```

```
    const Schema = mongoose.Schema;    const userSchema = new Schema({        name: { type: String, required: true, },        count: {type: Number}    });
```

```
    var User = mongoose.model('User', userSchema);    userSchema.pre('save', function(next) {        if (this.isNew) {            User.count().then(res => {              this.count = res; // Incrémente le compte              next();            });          } else {            next();          }    });
```

```
    module.exports = User;
```

```
    var currentUser;
```

```
    /*     =================================    Nous ajouterons nos endpoints ici !!!    =================================    */
```

```
    var port = process.env.PORT || 5000;
```

```
    app.listen(port);
```

Dans l'extrait ci-dessus, nous avons initialisé Pusher, Express et MongoDB. Nous utilisons [Moongose](http://mongoosejs.com/) pour nous connecter à notre instance MongoDB.

> _Remplacez les clés `PUSHER_APP_*` par celles de votre tableau de bord Pusher._

Maintenant, ajoutons nos endpoints. Le premier endpoint que nous ajouterons permettra de connecter un utilisateur. Collez le code ci-dessous dans votre fichier `index.js` sous la déclaration `currentUser` :

```
// Fichier : ./index.js
```

```
    // [...]
```

```
    app.post('/login', (req,res) => {        User.findOne({name: req.body.name}, (err, user) => {            if (err) {                res.send("Erreur de connexion à la base de données");            }
```

```
            // L'utilisateur existe            if (user) {                currentUser = user;                return res.status(200).send(user)            }
```

```
            let newuser = new User({name: req.body.name});
```

```
            newuser.save(function(err) {                if (err) throw err;            });
```

```
            currentUser = newuser;            res.status(200).send(newuser)        });    })
```

```
    // [...]
```

Cet endpoint reçoit un `username` avec la requête, et crée soit un nouvel utilisateur, soit retourne les données de l'utilisateur existant.

Ajoutons le prochain endpoint sous celui ci-dessus :

```
// Fichier : ./index.js
```

```
    // [...]
```

```
    app.get('/users', (req,res) => {        User.find({}, (err, users) => {            if (err) throw err;            res.send(users);        });    })
```

```
    // [...]
```

Ce deuxième endpoint récupère tous les utilisateurs de la base de données et les retourne.

Puisque nous allons utiliser un canal de présence Pusher, nous avons besoin d'un endpoint pour authentifier l'utilisateur. Dans le même fichier, collez ce code sous l'endpoint ci-dessus :

```
// Fichier : ./index.js
```

```
    // [...]
```

```
    app.post('/pusher/auth/presence', (req, res) => {        let socketId = req.body.socket_id;        let channel = req.body.channel_name;
```

```
        let presenceData = {            user_id: currentUser._id,            user_info: {count: currentUser.count, name: currentUser.name}        };
```

```
        let auth = pusher.authenticate(socketId, channel, presenceData);
```

```
        res.send(auth);    });
```

```
    // [...]
```

Puisque nous allons utiliser des canaux privés, nous avons besoin d'un endpoint pour l'authentification. Ajoutez l'endpoint suivant sous l'endpoint ci-dessus :

```
// Fichier : ./index.js
```

```
    // [...]
```

```
    app.post('/pusher/auth/private', (req, res) => {        res.send(pusher.authenticate(req.body.socket_id, req.body.channel_name));    });
```

```
    // [...]
```

```
Enfin, le dernier endpoint sera pour déclencher un événement `new-message` vers un canal. Ajoutez l'endpoint sous le dernier :
```

```
    // Fichier : ./index.js
```

```
    // [...]
```

```
    app.post('/send-message', (req, res) => {        let payload = {message: req.body.message, sender_id: req.body.sender_id}        pusher.trigger(req.body.channel_name, 'new-message', payload);        res.send(200);    });
```

```
    // [...]
```

Après avoir ajouté tous les endpoints, installez les packages npm nécessaires en exécutant cette commande :

```
$ npm install express body-parser mongoose pusher
```

Avant de lancer votre application, assurez-vous que MongoDB est déjà en cours d'exécution en utilisant cette commande :

```
$ mongod --dbpath C:\MongoDB\data\db # Windows    $ mongod --dbpath=/path/to/db/directory # Mac ou Linux
```

Maintenant, vous pouvez lancer votre application en utilisant la commande ci-dessous :

```
$ node index.js
```

Votre application sera disponible ici : [http://localhost:5000](http://localhost:5000/).

### Construction de notre application Android

Créez votre projet Android. Dans l'assistant, entrez le nom de votre projet — disons **MessengerApp.**

Ensuite, entrez votre nom de package. Vous pouvez utiliser un SDK minimum de 19 puis choisir une **Empty Activity.**

Sur la page suivante, changez le **Activity Name** en `LoginActivity`. Après cela, Android Studio construira votre projet pour vous.

Maintenant que nous avons le projet, ajoutons les dépendances requises pour notre application. Ouvrez votre fichier de module d'application `build.gradle` et ajoutez ceci :

```
// Fichier ../app/build.gradle    dependencies {      // [...]
```

```
      implementation 'com.android.support:design:28+'      implementation 'com.pusher:pusher-java-client:1.6.0'      implementation "com.squareup.retrofit2:retrofit:2.4.0"      implementation "com.squareup.retrofit2:converter-scalars:2.4.0"      implementation 'com.squareup.retrofit2:converter-gson:2.3.0'    }
```

Notamment, nous avons ajouté les dépendances pour [Retrofit](http://square.github.io/retrofit/) et Pusher. Retrofit est une bibliothèque cliente HTTP utilisée pour les appels réseau. Nous avons également ajouté la dépendance de la bibliothèque de design car nous voulons utiliser certaines classes de celle-ci. Synchronisez vos fichiers gradle pour obtenir les dépendances.

Ensuite, préparons notre application pour effectuer des appels réseau. Retrofit nécessite une interface pour connaître les endpoints à accéder.

Créez une nouvelle interface nommée `ApiService` et collez ceci :

```
// Fichier : ./app/src/main/java/com/example/messengerapp/ApiService.kt    import okhttp3.RequestBody    import retrofit2.Call    import retrofit2.http.Body    import retrofit2.http.GET    import retrofit2.http.POST
```

```
    interface ApiService {
```

```
      @POST("/login")      fun login(@Body body:RequestBody): Call<UserModel>
```

```
      @POST("/send-message")      fun sendMessage(@Body body:RequestBody): Call<String>
```

```
      @GET("/users")      fun getUsers(): Call<List<UserModel>>    }
```

Ici, nous avons déclaré trois endpoints. Ils sont pour la connexion, l'envoi de messages et la récupération des utilisateurs.

Dans certaines de nos réponses, nous retournons `Call<UserModel>`. Créons le `UserModel`. Créez une nouvelle classe appelée `UserModel` et collez le code suivant :

```
// Fichier : ./app/src/main/java/com/example/messengerapp/UserModel.kt    import com.google.gson.annotations.Expose    import com.google.gson.annotations.SerializedName
```

```
    data class UserModel(@SerializedName("_id") @Expose var id: String,                         @SerializedName("name") @Expose var name: String,                         @SerializedName("count") @Expose var count: Int,                         var online:Boolean = false)
```

Ci-dessus, nous avons utilisé une data class afin que certaines autres fonctions requises pour les classes de modèle telles que `toString` et `hashCode` soient ajoutées à la classe par défaut.

Nous attendons uniquement les valeurs pour `id` et `name` du serveur. Nous avons ajouté la propriété `online` afin de pouvoir la mettre à jour plus tard.

Ensuite, créez une nouvelle classe nommée `RetrofitInstance` et collez le code suivant :

```
// Fichier : ./app/src/main/java/com/example/messengerapp/RetrofitInstance.kt    import okhttp3.OkHttpClient    import retrofit2.Retrofit    import retrofit2.converter.gson.GsonConverterFactory    import retrofit2.converter.scalars.ScalarsConverterFactory
```

```
    class RetrofitInstance {
```

```
      companion object {        val retrofit: ApiService by lazy {          val httpClient = OkHttpClient.Builder()          val builder = Retrofit.Builder()              .baseUrl("http://10.0.2.2:5000/")              .addConverterFactory(ScalarsConverterFactory.create())              .addConverterFactory(GsonConverterFactory.create())
```

```
          val retrofit = builder              .client(httpClient.build())              .build()          retrofit.create(ApiService::class.java)        }      }    }
```

`RetrofitInstance` contient une variable de classe appelée `retrofit`. Elle nous fournit une instance pour Retrofit que nous référencerons dans plus d'une classe.

Enfin, pour demander l'autorisation d'accès à Internet, mettez à jour le fichier `AndroidManifest.xml` comme suit :

```
// Fichier : ./app/src/main/ApiService.kt    <manifest xmlns:android="http://schemas.android.com/apk/res/android"      package="com.example.messengerapp">
```

```
      <uses-permission android:name="android.permission.INTERNET" />      [...]
```

```
    </manifest>
```

Maintenant, nous pouvons faire des requêtes en utilisant Retrofit.

La prochaine fonctionnalité que nous allons implémenter est la connexion. Ouvrez le fichier de layout `LoginActivity` déjà créé `activity_login.xml` et collez ceci :

```
// Fichier : ./app/src/main/res/layout/activity_login.xml    <?xml version="1.0" encoding="utf-8"?>    <android.support.constraint.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"      xmlns:app="http://schemas.android.com/apk/res-auto"      xmlns:tools="http://schemas.android.com/tools"      android:layout_width="match_parent"      android:layout_height="match_parent"      android:layout_margin="20dp"      tools:context=".LoginActivity">
```

```
      <EditText        android:id="@+id/editTextUsername"        android:layout_width="match_parent"        android:layout_height="wrap_content"        app:layout_constraintBottom_toBottomOf="parent"        app:layout_constraintLeft_toLeftOf="parent"        app:layout_constraintRight_toRightOf="parent"        app:layout_constraintTop_toTopOf="parent" />
```

```
      <Button        android:id="@+id/loginButton"        android:layout_width="match_parent"        android:layout_height="wrap_content"        android:text="Login"        app:layout_constraintTop_toBottomOf="@+id/editTextUsername" />
```

```
    </android.support.constraint.ConstraintLayout>
```

Ce layout contient un champ de saisie pour le nom d'utilisateur et un bouton pour faire une requête de connexion.

Ensuite, ouvrez le fichier `LoginActivity.Kt` et collez ceci :

```
// Fichier : ./app/src/main/java/com/example/messengerapp/LoginActivity.kt    import android.content.Intent    import android.os.Bundle    import android.support.v7.app.AppCompatActivity    import android.util.Log    import kotlinx.android.synthetic.main.activity_login.*    import okhttp3.MediaType    import okhttp3.RequestBody    import org.json.JSONObject    import retrofit2.Call    import retrofit2.Callback    import retrofit2.Response
```

```
    class LoginActivity : AppCompatActivity() {
```

```
      override fun onCreate(savedInstanceState: Bundle?) {        super.onCreate(savedInstanceState)        setContentView(R.layout.activity_login)        loginButton.setOnClickListener {          if (editTextUsername.text.isNotEmpty()) {            loginFunction(editTextUsername.text.toString())          }        }      }
```

```
      private fun loginFunction(name:String) {        val jsonObject = JSONObject()        jsonObject.put("name", name)
```

```
        val jsonBody = RequestBody.create(            MediaType.parse("application/json; charset=utf-8"),             jsonObject.toString()        )
```

```
        RetrofitInstance.retrofit.login(jsonBody).enqueue(object:Callback<UserModel> {          override fun onFailure(call: Call<UserModel>?, t: Throwable?) {            Log.i("LoginActivity",t!!.localizedMessage)          }
```

```
          override fun onResponse(call: Call<UserModel>?, response: Response<UserModel>?) {            if (response!!.code() == 200) {              Singleton.getInstance().currentUser = response.body()!!              startActivity(Intent(this@LoginActivity,ContactListActivity::class.java))              finish()            }          }        })      }    }
```

Dans le fichier `LoginActivity.Kt`, nous avons configuré un écouteur pour notre bouton de connexion afin que, lorsqu'il est cliqué, nous puissions envoyer le texte au serveur pour authentification. Nous avons également stocké l'utilisateur connecté dans une classe singleton afin de pouvoir accéder aux détails de l'utilisateur plus tard.

Créez une nouvelle classe appelée `Singleton` et collez ceci :

```
// Fichier : ./app/src/main/java/com/example/messengerapp/RetrofitInstance.kt    class Singleton {      companion object {        private val ourInstance = Singleton()        fun getInstance(): Singleton {          return ourInstance        }      }      lateinit var currentUser: UserModel    }
```

`Singleton` nous donne accès à `currentUser`, qui est l'utilisateur connecté.

Ensuite, créons une nouvelle activité nommée `ContactListActivity`. Pour l'instant, laissez la classe vide et ouvrez le fichier de layout correspondant nommé `activity_contact_list`, et collez le code suivant :

```
// Fichier : ./app/src/main/res/layout/activity_contact_list.xml    <?xml version="1.0" encoding="utf-8"?>    <android.support.constraint.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"      xmlns:app="http://schemas.android.com/apk/res-auto"      xmlns:tools="http://schemas.android.com/tools"      android:layout_width="match_parent"      android:layout_height="match_parent"      tools:context=".ContactListActivity">
```

```
      <android.support.v7.widget.RecyclerView        android:layout_width="match_parent"        android:id="@+id/recyclerViewUserList"        android:layout_height="match_parent"/>
```

```
    </android.support.constraint.ConstraintLayout>
```

Le layout contient une vue de recyclage, qui nous donnera toutes les listes de nos contacts récupérés de la base de données. Puisque nous affichons des éléments dans une liste, nous aurons besoin d'une classe d'adaptateur pour gérer la façon dont les éléments sont gonflés dans le layout.

Créez une nouvelle classe nommée `ContactRecyclerAdapter` et collez ceci :

```
// Fichier : ./app/src/main/java/com/example/messengerapp/ContactRecyclerAdapter.kt    import android.support.v7.widget.RecyclerView    import android.view.LayoutInflater    import android.view.View    import android.view.ViewGroup    import android.widget.ImageView    import android.widget.TextView    import java.util.*
```

```
    class ContactRecyclerAdapter(private var list: ArrayList<UserModel>, private var listener: UserClickListener)      : RecyclerView.Adapter<ContactRecyclerAdapter.ViewHolder>() {
```

```
      override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {        return ViewHolder(LayoutInflater.from(parent.context)            .inflate(R.layout.user_list_row, parent, false))      }
```

```
      override fun onBindViewHolder(holder: ViewHolder, position: Int) = holder.bind(list[position])
```

```
      override fun getItemCount(): Int = list.size
```

```
      fun showUserOnline(updatedUser: UserModel) {        list.forEachIndexed { index, element ->          if (updatedUser.id == element.id) {            updatedUser.online = true            list[index] = updatedUser            notifyItemChanged(index)          }
```

```
        }      }
```

```
      fun showUserOffline(updatedUser: UserModel) {        list.forEachIndexed { index, element ->          if (updatedUser.id == element.id) {            updatedUser.online = false            list[index] = updatedUser            notifyItemChanged(index)          }        }      }
```

```
      fun add(user: UserModel) {        list.add(user)        notifyDataSetChanged()      }
```

```
      inner class ViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {        private val nameTextView: TextView = itemView.findViewById(R.id.usernameTextView)        private val presenceImageView: ImageView = itemView.findViewById(R.id.presenceImageView)
```

```
        fun bind(currentValue: UserModel) = with(itemView) {          this.setOnClickListener {            listener.onUserClicked(currentValue)          }          nameTextView.text = currentValue.name          if (currentValue.online){            presenceImageView.setImageDrawable(this.context.resources.getDrawable(R.drawable.presence_icon_online))          } else {            presenceImageView.setImageDrawable(this.context.resources.getDrawable(R.drawable.presence_icon))
```

```
          }
```

```
        }      }
```

```
      interface UserClickListener {        fun onUserClicked(user: UserModel)      }    }
```

Cet adaptateur a certaines méthodes remplacées et certaines méthodes personnalisées.

La méthode `onCreateViewHolder` gonfle l'apparence de chaque ligne. `onBindViewHolder` lie les données à chaque élément en appelant la méthode `bind` dans la classe interne `ViewHolder`. La méthode `getItemCount` donne la taille de la liste.

Pour nos méthodes personnalisées, `showUserOffline` met à jour l'utilisateur et montre quand ils sont hors ligne. Alors que `showUserOnline` fait l'inverse. Enfin, nous avons la méthode `add`, qui ajoute un nouveau contact à la liste et la rafraîchit.

Dans la classe d'adaptateur ci-dessus, nous avons utilisé un nouveau layout nommé `user_list_row`. Créez un nouveau layout `user_list_row` et collez ceci :

```
// Fichier : ./app/src/main/res/layout/user_list_row.xml    <?xml version="1.0" encoding="utf-8"?>    <LinearLayout      android:orientation="horizontal"      xmlns:android="http://schemas.android.com/apk/res/android"      xmlns:app="http://schemas.android.com/apk/res-auto"      xmlns:tools="http://schemas.android.com/tools"      android:layout_width="match_parent"      android:layout_height="wrap_content"      android:layout_margin="20dp"      android:gravity="center"      tools:context=".LoginActivity">
```

```
      <ImageView        android:id="@+id/presenceImageView"        android:layout_width="15dp"        android:layout_height="15dp"        app:srcCompat="@drawable/presence_icon" />
```

```
      <TextView        android:layout_width="match_parent"        android:layout_height="wrap_content"        tools:text="Neo"        android:textSize="20sp"        android:layout_marginStart="10dp"        android:id="@+id/usernameTextView"        app:layout_constraintTop_toBottomOf="@+id/editTextUsername"        />
```

```
    </LinearLayout>
```

Ce layout est la représentation visuelle de l'apparence de chaque élément du layout. Le layout a une vue d'image qui montre le statut en ligne des utilisateurs. Le layout a également une vue de texte qui montre le nom du contact à côté de l'icône. Les icônes sont des dessins vectoriels. Créons les fichiers.

Créez un nouveau dessin nommé `presence_icon_online` et collez ceci :

```
// Fichier : ./app/src/main/res/drawable/presence_icon_online.xml    <vector android:height="24dp" android:tint="#3FFC3C"        android:viewportHeight="24.0" android:viewportWidth="24.0"        android:width="24dp" xmlns:android="http://schemas.android.com/apk/res/android">        <path android:fillColor="#FF000000" android:pathData="M12,2C6.48,2 2,6.48 2,12s4.48,10 10,10 10,-4.48 10,-10S17.52,2 12,2z"/>    </vector>
```

Créez un autre dessin nommé `presence_icon` et collez ceci :

```
// Fichier : ./app/src/main/res/drawable/presence_icon.xml    <vector android:height="24dp" android:tint="#C0C0C6"        android:viewportHeight="24.0" android:viewportWidth="24.0"        android:width="24dp" xmlns:android="http://schemas.android.com/apk/res/android">        <path android:fillColor="#FF000000" android:pathData="M12,2C6.48,2 2,6.48 2,12s4.48,10 10,10 10,-4.48 10,-10S17.52,2 12,2z"/>    </vector>
```

Ensuite, ouvrez la classe `ContactListActivity` et collez ceci :

```
// Fichier : ./app/src/main/java/com/example/messengerapp/ContactListActivity.kt    import android.content.Intent    import android.os.Bundle    import android.support.v7.app.AppCompatActivity    import android.support.v7.widget.LinearLayoutManager    import android.util.Log    import com.pusher.client.Pusher    import com.pusher.client.PusherOptions    import com.pusher.client.channel.PresenceChannelEventListener    import com.pusher.client.channel.User    import com.pusher.client.util.HttpAuthorizer    import kotlinx.android.synthetic.main.activity_contact_list.*    import retrofit2.Call    import retrofit2.Callback    import retrofit2.Response
```

```
    class ContactListActivity : AppCompatActivity(),        ContactRecyclerAdapter.UserClickListener {
```

```
      private val mAdapter = ContactRecyclerAdapter(ArrayList(), this)
```

```
      override fun onCreate(savedInstanceState: Bundle?) {        super.onCreate(savedInstanceState)        setContentView(R.layout.activity_contact_list)        setupRecyclerView()        fetchUsers()        subscribeToChannel()      }
```

```
    }
```

Dans `ContactListActivity`, nous avons initialisé le `ContactRecyclerAdapter`, puis appelé trois fonctions dans la méthode `onCreate`. Créons ces nouvelles fonctions.

Dans la même classe, ajoutez les méthodes suivantes :

```
private fun setupRecyclerView() {      with(recyclerViewUserList) {        layoutManager = LinearLayoutManager(this@ContactListActivity)        adapter = mAdapter      }    }
```

```
    private fun fetchUsers() {      RetrofitInstance.retrofit.getUsers().enqueue(object : Callback<List<UserModel>> {        override fun onFailure(call: Call<List<UserModel>>?, t: Throwable?) {}        override fun onResponse(call: Call<List<UserModel>>?, response: Response<List<UserModel>>?) {          for (user in response!!.body()!!) {            if (user.id != Singleton.getInstance().currentUser.id) {              mAdapter.add(user)            }          }        }      })    }
```

```
    private fun subscribeToChannel() {
```

```
      val authorizer = HttpAuthorizer("http://10.0.2.2:5000/pusher/auth/presence")      val options = PusherOptions().setAuthorizer(authorizer)      options.setCluster("PUSHER_APP_CLUSTER")
```

```
      val pusher = Pusher("PUSHER_APP_KEY", options)      pusher.connect()
```

```
      pusher.subscribePresence("presence-channel", object : PresenceChannelEventListener {        override fun onUsersInformationReceived(p0: String?, users: MutableSet<User>?) {          for (user in users!!) {            if (user.id!=Singleton.getInstance().currentUser.id){              runOnUiThread {                mAdapter.showUserOnline(user.toUserModel())              }            }          }        }
```

```
        override fun onEvent(p0: String?, p1: String?, p2: String?) {}        override fun onAuthenticationFailure(p0: String?, p1: Exception?) {}        override fun onSubscriptionSucceeded(p0: String?) {}
```

```
        override fun userSubscribed(channelName: String, user: User) {          runOnUiThread {            mAdapter.showUserOnline(user.toUserModel())          }        }
```

```
        override fun userUnsubscribed(channelName: String, user: User) {          runOnUiThread {            mAdapter.showUserOffline(user.toUserModel())          }        }      })    }
```

```
    override fun onUserClicked(user: UserModel) {      val intent = Intent(this, ChatRoom::class.java)      intent.putExtra(ChatRoom.EXTRA_ID,user.id)      intent.putExtra(ChatRoom.EXTRA_NAME,user.name)      intent.putExtra(ChatRoom.EXTRA_COUNT,user.count)      startActivity(intent)    }
```

**Remplacez les clés `PUSHER_APP_*` par les valeurs de votre tableau de bord.**

* `setupRecyclerView` attribue un gestionnaire de layout et un adaptateur à la vue de recyclage. Pour qu'une vue de recyclage fonctionne, vous avez besoin de ces deux éléments.
* `fetchUsers` récupère tous les utilisateurs du serveur et les affiche dans la liste. Il exclut l'utilisateur actuel connecté.
* `subcribeToChannel` s'abonne à un canal de présence. Lorsque vous vous abonnez à un canal de présence, le `onUsersInformationReceived` vous donne tous les utilisateurs abonnés au canal, y compris l'utilisateur actuel. Ainsi, dans ce callback, nous appelons la méthode `showUserOnline` dans la classe d'adaptateur afin que l'icône à côté de l'utilisateur puisse être changée pour signifier que l'utilisateur est en ligne.
* `onUserClicked` est appelé lorsqu'un contact est sélectionné. Nous passons les détails de l'utilisateur à l'activité suivante appelée `ChatRoom`.

Dans l'extrait précédent, nous avons utilisé une fonction d'extension pour transformer l'objet `User` que nous recevons de Pusher en notre propre objet `UserModel`. Définissons cette extension.

Créez une nouvelle classe appelée `Utils` et collez ceci :

```
// Fichier : ./app/src/main/java/com/example/messengerapp/Utils.kt    import com.pusher.client.channel.User    import org.json.JSONObject
```

```
    fun User.toUserModel():UserModel{      val jsonObject = JSONObject(this.info)      val name = jsonObject.getString("name")      val numb = jsonObject.getInt("count")      return UserModel(this.id, name, numb)    }
```

Maintenant, puisque nous avons référencé une activité `ChatRoom` plus tôt dans la méthode `onUserClicked`, créons-la.

Créez une nouvelle activité appelée `ChatRoom`. L'activité vient avec un fichier de layout `activity_chat_room`. Collez ceci dans le fichier de layout :

```
// Fichier : ./app/src/main/res/layout/activity_chat_room.xml    <?xml version="1.0" encoding="utf-8"?>    <android.support.constraint.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"      xmlns:app="http://schemas.android.com/apk/res-auto"      xmlns:tools="http://schemas.android.com/tools"      android:layout_width="match_parent"      android:layout_height="match_parent"      tools:context=".ChatRoom">
```

```
      <android.support.v7.widget.RecyclerView        android:id="@+id/recyclerViewChat"        android:layout_width="match_parent"        android:layout_height="match_parent" />
```

```
      <EditText        android:id="@+id/editText"        android:layout_width="0dp"        android:layout_height="wrap_content"        android:layout_margin="16dp"        android:hint="Enter a message"        app:layout_constraintBottom_toBottomOf="parent"        app:layout_constraintEnd_toStartOf="@+id/sendButton"        app:layout_constraintStart_toStartOf="parent" />
```

```
      <android.support.design.widget.FloatingActionButton        android:id="@+id/sendButton"        android:layout_width="wrap_content"        android:layout_height="wrap_content"        android:layout_gravity="end|bottom"        android:layout_margin="16dp"        android:src="@android:drawable/ic_menu_send"        app:layout_constraintEnd_toEndOf="parent"        app:layout_constraintBottom_toBottomOf="parent" />
```

```
    </android.support.constraint.ConstraintLayout>
```

Le layout ci-dessus contient une vue de recyclage pour les messages de chat, un champ de texte pour collecter les nouveaux messages et un bouton d'action flottant pour envoyer le message.

Ensuite, créez une nouvelle classe appelée `ChatRoomAdapter` et collez le code suivant :

```
// Fichier : ./app/src/main/java/com/example/messengerapp/ChatRoomAdapter.kt    import android.support.v7.widget.CardView    import android.support.v7.widget.RecyclerView    import android.view.LayoutInflater    import android.view.View    import android.view.ViewGroup    import android.widget.RelativeLayout    import android.widget.TextView    import java.util.*
```

```
    class ChatRoomAdapter (private var list: ArrayList<MessageModel>)      : RecyclerView.Adapter<ChatRoomAdapter.ViewHolder>() {
```

```
      override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {        return ViewHolder(LayoutInflater.from(parent.context)            .inflate(R.layout.chat_item, parent, false))      }
```

```
      override fun onBindViewHolder(holder: ViewHolder, position: Int) = holder.bind(list[position])
```

```
      override fun getItemCount(): Int = list.size
```

```
      fun add(message: MessageModel) {        list.add(message)        notifyDataSetChanged()      }
```

```
      inner class ViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {        private val messageTextView: TextView = itemView.findViewById(R.id.text)        private val cardView: CardView = itemView.findViewById(R.id.cardView)
```

```
        fun bind(message: MessageModel) = with(itemView) {          messageTextView.text = message.message          val params = cardView.layoutParams as RelativeLayout.LayoutParams          if (message.senderId==Singleton.getInstance().currentUser.id) {            params.addRule(RelativeLayout.ALIGN_PARENT_RIGHT)          }        }      }    }
```

Cet adaptateur fonctionne de manière similaire à celui que nous avons créé précédemment. Une différence, cependant, est que les méthodes show online et offline ne sont pas nécessaires ici.

Ensuite, créez une autre classe — nommée `MessageModel` — et collez ceci :

```
// Fichier : ./app/src/main/java/com/example/messengerapp/MessageModel.kt    data class MessageModel(val message: String, val senderId: String)
```

Le layout `chat_item` utilisé dans la méthode `onCreateViewHolder` de la classe d'adaptateur représente l'apparence de chaque layout. Créez un nouveau layout appelé `chat_item` et collez ceci :

```
// Fichier : ./app/src/main/res/layout/chat_item.xml    <?xml version="1.0" encoding="utf-8"?>    <RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"      xmlns:app="http://schemas.android.com/apk/res-auto"      android:layout_width="wrap_content"      android:layout_height="wrap_content"      android:layout_margin="16dp"      android:orientation="vertical">
```

```
      <android.support.v7.widget.CardView        android:id="@+id/cardView"        android:layout_width="wrap_content"        android:layout_height="wrap_content"        android:layout_gravity="start"        app:cardCornerRadius="8dp"        app:cardUseCompatPadding="true">
```

```
        <LinearLayout          android:layout_width="wrap_content"          android:layout_height="wrap_content"          android:gravity="start"          android:orientation="vertical"          android:padding="8dp">
```

```
          <TextView            android:id="@+id/text"            android:layout_width="wrap_content"            android:layout_height="wrap_content"            android:layout_gravity="center_vertical|start"            android:layout_marginBottom="4dp"            android:textStyle="bold" />
```

```
        </LinearLayout>
```

```
      </android.support.v7.widget.CardView>
```

```
    </RelativeLayout>
```

#### Mise à jour de la classe ChatRoom

Enfin, ouvrez la classe d'activité `ChatRoom` et collez ceci :

```
// Fichier : ./app/src/main/java/com/example/messengerapp/ChatRoom.kt    import android.app.Activity    import android.os.Bundle    import android.support.v7.app.AppCompatActivity    import android.support.v7.widget.LinearLayoutManager    import android.util.Log    import android.view.View    import android.view.inputmethod.InputMethodManager    import com.pusher.client.Pusher    import com.pusher.client.PusherOptions    import com.pusher.client.channel.PrivateChannelEventListener    import com.pusher.client.util.HttpAuthorizer    import kotlinx.android.synthetic.main.activity_chat_room.*    import okhttp3.MediaType    import okhttp3.RequestBody    import org.json.JSONObject    import retrofit2.Call    import retrofit2.Callback    import retrofit2.Response    import java.lang.Exception    import java.util.*
```

```
    class ChatRoom : AppCompatActivity() {
```

```
      companion object {        const val EXTRA_ID = "id"        const val EXTRA_NAME = "name"        const val EXTRA_COUNT = "numb"      }
```

```
      private lateinit var contactName: String      private lateinit var contactId: String      private var contactNumb: Int = -1      lateinit var nameOfChannel: String      val mAdapter = ChatRoomAdapter(ArrayList())
```

```
      override fun onCreate(savedInstanceState: Bundle?) {        super.onCreate(savedInstanceState)        setContentView(R.layout.activity_chat_room)        fetchExtras()        setupRecyclerView()        subscribeToChannel()        setupClickListener()      }    }
```

Dans ce fichier, nous avons déclaré des constantes utilisées pour envoyer des données à l'activité via des intents. Nous avons également initialisé des variables que nous utiliserons plus tard, comme l'adaptateur et les détails du contact. Nous avons ensuite appelé certaines méthodes supplémentaires dans la méthode `onCreate`. Ajoutons-les à la classe `ChatRoom`.

Ajoutez la méthode `fetchExtras` définie ci-dessous à la classe. La méthode obtient les extras envoyés depuis l'activité de la salle de chat.

```
private fun fetchExtras() {      contactName = intent.extras.getString(ChatRoom.EXTRA_NAME)      contactId = intent.extras.getString(ChatRoom.EXTRA_ID)      contactNumb = intent.extras.getInt(ChatRoom.EXTRA_COUNT)    }
```

La méthode suivante est `setupRecyclerView`. Cela initialise la vue de recyclage avec un adaptateur et un gestionnaire de layout. Collez cette fonction dans la même classe que précédemment :

```
private fun setupRecyclerView() {      with(recyclerViewChat) {        layoutManager = LinearLayoutManager(this@ChatRoom)        adapter = mAdapter      }    }
```

La méthode suivante est `subscribeToChannel`. Cette méthode abonne l'utilisateur à un canal privé avec le contact sélectionné. Collez le code suivant dans la même classe que précédemment :

```
private fun subscribeToChannel() {      val authorizer = HttpAuthorizer("http://10.0.2.2:5000/pusher/auth/private")      val options = PusherOptions().setAuthorizer(authorizer)      options.setCluster("PUSHER_APP_CLUSTER")
```

```
      val pusher = Pusher("PUSHER_APP_KEY", options)      pusher.connect()
```

```
      nameOfChannel = if (Singleton.getInstance().currentUser.count > contactNumb) {        "private-" + Singleton.getInstance().currentUser.id + "-" + contactId      } else {        "private-" + contactId + "-" + Singleton.getInstance().currentUser.id      }
```

```
      Log.i("ChatRoom", nameOfChannel)
```

```
      pusher.subscribePrivate(nameOfChannel, object : PrivateChannelEventListener {        override fun onEvent(channelName: String?, eventName: String?, data: String?) {          val obj = JSONObject(data)          val messageModel = MessageModel(obj.getString("message"), obj.getString("sender_id"))
```

```
          runOnUiThread {            mAdapter.add(messageModel)          }        }
```

```
        override fun onAuthenticationFailure(p0: String?, p1: Exception?) {}        override fun onSubscriptionSucceeded(p0: String?) {}      }, "new-message")    }
```

**Remplacez les clés `PUSHER_APP_*` par les valeurs de votre tableau de bord.**

Le code ci-dessus permet à un utilisateur de s'abonner à un canal privé. Un canal privé nécessite une autorisation comme le canal de présence. Cependant, il n'expose pas de callback qui est déclenché lorsque d'autres utilisateurs s'abonnent.

La méthode suivante à ajouter est `setupClickListener`. Collez la méthode dans la même classe que précédemment :

```
private fun setupClickListener() {      sendButton.setOnClickListener{        if (editText.text.isNotEmpty()) {          val jsonObject = JSONObject()          jsonObject.put("message",editText.text.toString())          jsonObject.put("channel_name",nameOfChannel)          jsonObject.put("sender_id",Singleton.getInstance().currentUser.id)
```

```
          val jsonBody = RequestBody.create(              MediaType.parse("application/json; charset=utf-8"),               jsonObject.toString()          )
```

```
          RetrofitInstance.retrofit.sendMessage(jsonBody).enqueue(object: Callback<String>{            override fun onFailure(call: Call<String>?, t: Throwable?) {}            override fun onResponse(call: Call<String>?, response: Response<String>?) {}          })
```

```
          editText.text.clear()          hideKeyBoard()        }
```

```
      }    }
```

La méthode ci-dessus attribue un écouteur de clic au bouton d'action flottant pour envoyer le message au serveur. Après l'envoi du message, nous effaçons la vue de texte et masquons le clavier.

Ajoutez une méthode à la même classe pour masquer le clavier comme ceci :

```
private fun hideKeyBoard() {      val imm = getSystemService(Activity.INPUT_METHOD_SERVICE) as InputMethodManager      var view = currentFocus
```

```
      if (view == null) {        view = View(this)      }
```

```
      imm.hideSoftInputFromWindow(view.windowToken, 0)    }
```

C'est tout pour l'application. Maintenant, vous pouvez exécuter votre application dans Android Studio et vous devriez voir l'application en action.

**Assurez-vous que l'API Node.js que nous avons construite précédemment est en cours d'exécution avant de lancer l'application Android.**

![Image](https://cdn-media-1.freecodecamp.org/images/PVjZrTyRaGD-teS6M7lsjiNx78fb4eyIIDgj)

### Conclusion

Dans cet article, vous avez été introduit à certaines capacités de Pusher telles que les canaux privés et de présence.

Nous avons appris comment authentifier nos utilisateurs pour les différents canaux.

Nous avons utilisé ces canaux pour implémenter un chat privé entre deux personnes et une notification en ligne pour un contact.

Le code source de l'application construite dans cet article est disponible sur [GitHub](https://github.com/neoighodaro/kotlin-messenger-app-with-online-presence-status).

Cet article est d'abord apparu sur le [Blog Pusher](https://pusher.com/tutorials/android-messenger-presence-kotlin).