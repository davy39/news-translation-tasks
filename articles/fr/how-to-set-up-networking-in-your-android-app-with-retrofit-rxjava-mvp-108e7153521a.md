---
title: Comment configurer la mise en réseau dans votre application Android avec Retrofit-RxJava-MVP
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-06T15:31:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-networking-in-your-android-app-with-retrofit-rxjava-mvp-108e7153521a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_qQps59angkeAdcbql2rnA.png
tags:
- name: Android
  slug: android
- name: mobile app development
  slug: mobile-app-development
- name: rxjava
  slug: rxjava
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: Comment configurer la mise en réseau dans votre application Android avec
  Retrofit-RxJava-MVP
seo_desc: 'By Ayusch Jain


  This article was originally posted here


  In this Android App development tutorial, I’ll be demonstrating how you can setup
  Retrofit and RxJava for networking in your android application along with MVP Architecture.

  We’ll be developing...'
---

Par Ayusch Jain

> Cet article a été initialement publié [ici](https://ayusch.com/networking-with-retrofit-rxjava-mvp)

Dans ce tutoriel de développement d'applications Android, je vais démontrer comment configurer Retrofit et RxJava pour la mise en réseau dans votre application Android avec l'architecture MVP.

Nous allons développer une application très basique qui affichera des données dans une recyclerview. Les données seront obtenues à partir d'une fausse API JSON hébergée sur [https://jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com). L'application affichera les données en trois colonnes : ID, Titre et Corps.

Voici les prérequis pour ce tutoriel :

* [Comment implémenter l'architecture MVP dans Android](https://ayusch.com/mvp-architecture-android/)
* [Comprendre les bases de RxJava](https://ayusch.com/understanding-rxjava-basics)

Une fois que vous avez parcouru les deux articles ci-dessus, vous êtes prêt à avancer avec cet article. J'ai divisé cela en 4 phases :

* Configuration du projet et création des layouts.
* Configuration de l'architecture MVP.
* Création de la classe Model pour les données et de l'adaptateur pour RecyclerView.
* Configuration de la mise en réseau avec Retrofit et RxJava.

Alors, commençons !

> Note : Certaines [écoles en ligne](http://microverse.org) comme Udemy et Lynda ont également de bons tutoriels sur RxJava

### Phase 1 : Configuration du projet et création des layouts.

#### Créer un nouveau projet

Créez un nouveau projet dans Android Studio. Allez dans Fichier -> Nouveau Projet et sélectionnez « Empty Activity ». Ensuite, cliquez sur Terminer.

![Image](https://cdn-media-1.freecodecamp.org/images/QBay9VeS0891s9mHP3ExEtJ-zAGTa8QBOyrl)

#### **Ajouter une RecyclerView**

Pour ajouter une recyclerview à votre projet, ouvrez le fichier build.gradle au niveau de l'application et ajoutez la dépendance suivante à la fin :

```
implementation 'com.android.support:design:28.0.0'
```

> _Note : Vous pouvez également ajouter recyclerview directement au lieu de la bibliothèque de design entière, mais la plupart d'entre vous l'ont probablement déjà incluse, donc j'inclus la bibliothèque de design dans cet exemple. Vous pouvez inclure uniquement la recyclerview également._

Maintenant, dirigez-vous vers votre fichier de layout principal, dans mon cas activity_main.xml, et ajoutez une recyclerview à l'intérieur du layout racine :

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".UserActivity">
    
    <android.support.v7.widget.RecyclerView
        android:id="@+id/recyclerview"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />
        
</LinearLayout>
```

#### Création de l'élément RecyclerView

Maintenant, commençons à créer les lignes de la RecyclerView. Ici, nous nous intéressons uniquement à l'architecture de notre application Android et à la manière dont Retrofit, RxJava et l'architecture MVP peuvent fonctionner en tandem, donc ne vous plaignez pas de l'apparence de l'UI :P. Vous pouvez certainement aller de l'avant et l'embellir.

Nous allons créer un layout très simple à trois colonnes. La première colonne affichera l'ID de l'élément, la deuxième colonne affichera le Titre, et enfin, la troisième colonne affichera le corps/description.

Allez dans res->layout et faites un clic droit sur le dossier layout. Créez un nouveau fichier de ressource de layout. Nommez-le comme vous le souhaitez, dans mon cas, je le nommerai **recycler_item.**

Pour créer un layout à trois colonnes, ajoutez un LinearLayout comme racine. Ensuite, ajoutez trois TextViews et définissez leur largeur à 0 et leur poids à 1, 2, 3 respectivement. Cela divisera toute la largeur de votre écran en 3 colonnes dans la proportion 1:2:3.

Voici à quoi ressemblera votre layout :

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:layout_marginTop="16dp"
    android:orientation="horizontal">
    
    <TextView
        android:id="@+id/user_id"
        android:layout_width="0dp"
        android:layout_height="wrap_content"
        android:layout_weight="1"
        android:gravity="center"
        android:padding="4dp"
        android:text="id" />
    
    <TextView
        android:id="@+id/user_title"
        android:layout_width="0dp"
        android:layout_height="wrap_content"
        android:layout_weight="2"
        android:gravity="center"
        android:padding="4dp"
        android:text="Titre" />
    
    <TextView
        android:id="@+id/user_body"
        android:layout_width="0dp"
        android:layout_height="wrap_content"
        android:layout_weight="3"
        android:gravity="center"
        android:padding="4dp"
        android:text="Corps" />
    
</LinearLayout>
```

**Encore une fois, comme il ne s'agit pas d'un tutoriel de design, l'UI peut ne pas être très joli, donc n'hésitez pas à le personnaliser comme vous le souhaitez ?**

Maintenant que les layouts sont terminés, nous pouvons passer à la configuration de notre application Android conformément à l'architecture MVP. Encore une fois, si vous n'êtes pas vraiment familier avec MVP, je vous suggère fortement de jeter un œil ici : [Architecture MVP dans Android](https://ayusch.com/mvp-architecture-android/).

### Phase 2 : Configuration de l'architecture MVP

#### Création du contrat

Beaucoup de gens aiment garder leurs interfaces View et Presenter dans des fichiers différents, mais selon les directives suggérées par Google, j'aime créer une interface externe (Wrapper) nommée **Contract** et y placer mes interfaces View et Presenter.

L'avantage de cela est que vous n'aurez pas à chercher dans différents fichiers pour la vue et le présentateur associés à une seule activité, tout est au même endroit. C'est ainsi que je l'aime, mais n'hésitez pas à explorer d'autres techniques.

Alors maintenant, créons un UserActivityContract. Créez un nouveau package nommé **"contract"**. À l'intérieur de ce package, créez une nouvelle interface Java UserActivityContract.

À l'intérieur de **UserActivityContract**, ajoutez deux interfaces imbriquées : View et Presenter. Voici à quoi ressemblera votre contrat à la fin :

```java
public interface UserContract {
    interface View {
    
    }
    
    interface Presenter {
    
    }
    
}
```

Maintenant, ajoutons quelques méthodes à celles-ci. Parlons d'abord de la View, nous allons faire 3 choses majeures à l'intérieur de notre vue :

* Configuration initiale de la recyclerview (ajout du layout manager).
* Création d'un adaptateur à partir de la recyclerview en utilisant la liste des utilisateurs obtenus à partir de l'API.
* Affichage d'un message d'erreur en cas d'erreur.

Alors, ajoutons une méthode pour chacune de ces étapes :

```java
public interface UserContract {
    interface View {
        void init();
        
        void showError(String message);
        
        void loadDataInList(List<User> users);
    }
    
    interface Presenter {

    }
    
}
```

Ensuite, parlons du Presenter. La seule vraie tâche du présentateur est d'obtenir les données de l'API et de les envoyer à la View. Donc, ajoutez une méthode **loadUsers()**, nous allons faire notre appel API ici et passer le résultat à la vue si c'est un succès, sinon un message d'erreur.

```java
public interface UserContract {
    interface View {
        void init();
        
        void showError(String message);
        
        void loadDataInList(List<User> users);
    }
    
    interface Presenter {
    
        void start();
        
        void loadUsers();
    }
    
}
```

Remarquez qu'en plus de loadUsers(), nous avons également ajouté une méthode nommée **start()**, c'est plus une méthode d'initialisation pour le présentateur. Vous pouvez effectuer toutes sortes de tâches d'init ici, comme initialiser certaines variables, appeler une méthode de la vue pour afficher des messages d'init, etc. Ici, je l'utilise pour initialiser la RecyclerView à l'intérieur de ma classe UserActivity.java.

#### Création du Presenter et implémentation de la View

Une fois les interfaces terminées, il est temps de les implémenter.

Créez une nouvelle classe nommée UserPresenter et implémentez UserContract.Presenter et implémentez les méthodes requises.

Maintenant, ouvrez votre classe UserActivity.java et implémentez l'interface UserContract.View et implémentez toutes les méthodes requises. Ajoutez un champ pour le présentateur dans votre activité et initialisez-le dans onCreate comme montré ci-dessous :

```java
mPresenter = new UserPresenter(this);
mPresenter.start();
```

Cela appellera le constructeur de notre présentateur et liera la View et le Presenter ensemble. Lorsque nous appelons la méthode start sur le présentateur, le présentateur appelle à son tour la méthode init() qui commence notre processus d'initialisation.

**Avec cela,** nous terminons la **Phase 2** de notre projet. Maintenant, passons à la **Phase 3** et créons notre classe de modèle et un adaptateur personnalisé pour lier les données à la recyclerview.

### Phase 3 : Création de la classe Model pour les données et de l'adaptateur pour RecyclerView

#### Création du modèle

Allons-y et créons notre modèle qui sera une classe POJO pour nos données. Si vous regardez de près la réponse JSON, elle se compose de 4 champs : id, userId, title, body. Et tout cela à l'intérieur d'un objet JSON. Et de nombreux objets JSON dans un tableau. Donc, c'est une classe POJO assez simple à créer.

Mais avant cela, ajoutons une dépendance pour GSON, qui sera utilisée pour analyser la réponse JSON. Ajoutez la ligne suivante à vos dépendances :

```
implementation 'com.squareup.retrofit2:converter-gson:2.4.0'
```

> _Note : Ce n'est pas la dépendance GSON réelle, c'est un convertisseur qui utilise GSON pour la sérialisation vers et depuis JSON._

Maintenant, créez un package nommé **model** et à l'intérieur, créez un fichier java nommé **User**. Ajoutez les quatre champs et annotez chacun des champs avec **@SerializedName**. Maintenant, créons des getters et des setters pour les champs. Android Studio le fait automatiquement pour vous, il suffit de presser ALT+INS sur votre clavier et de sélectionner getters et setters.

Voici à quoi ressemblera votre classe POJO à la fin :

```java
public class User{

   @SerializedName("id")
   private int id;
   
   @SerializedName("title")
   private String title;
   
   @SerializedName("body")
   private String body;
   
   @SerializedName("userId")
   private int userId;
   
   public void setId(int id){
      this.id = id;
   }
   
   public int getId(){
      return id;
   }
   
   public void setTitle(String title){
      this.title = title;
   }
   
   public String getTitle(){
      return title;
   }
   
   public void setBody(String body){
      this.body = body;
   }
   
   public String getBody(){
      return body;
   }
   
   public void setUserId(int userId){
      this.userId = userId;
   }
   
   public int getUserId(){
      return userId;
   }
   
   @Override
   public String toString(){
      return 
         "User{" + 
         "id = '" + id + '\'' + 
         ",title = '" + title + '\'' + 
         ",body = '" + body + '\'' + 
         ",userId = '" + userId + '\'' + 
         "}";
      }
}
```

> _Note : la méthode toString est facultative. J'aime l'inclure car lors de l'impression des déclarations de log, elle imprime le json formaté._

### Création de l'adaptateur RecyclerView

Créons maintenant l'adaptateur de la recyclerview. Créez un package nommé adapter et créez une nouvelle classe Java nommée **CustomAdapter.java** à l'intérieur. Étendez la classe à partir de la classe RecyclerView.Adapter. Elle affichera une erreur, appuyez simplement sur ALT+Enter et remplacez toutes les méthodes requises.

À l'intérieur de **CustomAdapter.java**, créez une classe imbriquée nommée MyViewHolder et étendez-la à partir de RecyclerView.ViewHolder. Ensuite, créez un constructeur et initialisez tous les TextViews comme montré ci-dessous :

```java
public class CustomAdapter extends RecyclerView.Adapter<CustomAdapter.MyViewHolder> {

    public CustomAdapter(List<User> userList) {
        
    }
    
    @Override
    public MyViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
    
    }
    
    @Override
    public void onBindViewHolder(MyViewHolder holder, int position) {
    
    }
    
    @Override
    public int getItemCount() {
        return userList.size();
    }
    
    public class MyViewHolder extends RecyclerView.ViewHolder {
    
        TextView tvId, tvTitle, tvBody;
        
        public MyViewHolder(View itemView) {
            super(itemView);
            tvId = (TextView) itemView.findViewById(R.id.user_id);
            tvTitle = (TextView) itemView.findViewById(R.id.user_title);
            tvBody = (TextView) itemView.findViewById(R.id.user_body);
        }
    }
    
}
```

Nous allons passer une liste d'utilisateurs à cet adaptateur et nous le ferons dans le **constructeur**. Donc, créez d'abord un champ **List<User>** puis créez un constructeur qui prendra une List<User> comme argument. Maintenant, définissez la propriété du champ sur celle obtenue dans le constructeur.

Lorsque vous avez remplacé les méthodes, vous avez obtenu onCreateViewHolder. Dans cette méthode, nous allons gonfler notre layout pour l'élément de la recyclerview et retourner un view holder à partir de celui-ci. Dirigez-vous vers onCreateViewHolder et ajoutez le code suivant :

```java
@Override
public MyViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
    View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.recycler_item, parent, false);
    return new MyViewHolder(view);
}
```

Maintenant, dans **onBindViewHolder**, nous allons lier les données à nos vues. Voici à quoi ressemblera l'adaptateur final :

```java
public class CustomAdapter extends RecyclerView.Adapter<CustomAdapter.MyViewHolder> {

    List<User> userList = new ArrayList<>();
    
    public CustomAdapter(List<User> userList) {
        this.userList = userList;
    }
    
    @Override
    public MyViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.recycler_item, parent, false);
        return new MyViewHolder(view);
    }
    
    @Override
    public void onBindViewHolder(MyViewHolder holder, int position) {
        holder.tvTitle.setText(userList.get(position).getTitle());
        holder.tvId.setText(userList.get(position).getId()+"");
        holder.tvBody.setText(userList.get(position).getBody());
    }
    
    @Override
    public int getItemCount() {
        return userList.size();
    }
    
    public class MyViewHolder extends RecyclerView.ViewHolder {
        TextView tvId, tvTitle, tvBody;
        public MyViewHolder(View itemView) {
            super(itemView);
            tvId = (TextView) itemView.findViewById(R.id.user_id);
            tvTitle = (TextView) itemView.findViewById(R.id.user_title);
            tvBody = (TextView) itemView.findViewById(R.id.user_body);
        }
    }
    
}
```

### Phase 4 : Configuration de la mise en réseau avec Retrofit et RxJava

C'est le cœur de notre application Android. C'est ce pour quoi vous êtes tous venus ici, alors commençons.

J'ai divisé la configuration de la mise en réseau dans notre projet en 4 parties :

* Création d'un adaptateur Retrofit.
* Configuration d'une interface de service API qui définit nos endpoints.
* Création d'une classe NetworkingUtil pour lier l'adaptateur et le service.
* Création d'une classe utilitaire pour effectuer des appels API et retourner le résultat au présentateur.

Alors, commençons.

#### Création d'un adaptateur Retrofit

Créez un package nommé "networking", et à l'intérieur de networking, créez un autre package nommé "adapter" (c'est ainsi que j'aime gérer mes packages et ce n'est en aucun cas la méthode recommandée pour faire les choses, mais cela me convient donc +1).

À l'intérieur de ce package, créez une classe nommée RetrofitAdapter. Dans cette classe, nous allons définir les éléments suivants :

* Une usine de convertisseur pour analyser la réponse JSON dans notre classe POJO.
* Une usine d'adaptateur d'appel.
* Une URL de base.

Commençons par ajouter un champ **BASE_URL** en haut. Définissez l'URL de base sur [https://jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com)

Maintenant, créez une instance statique de Gson et Retrofit en haut. Maintenant, créez une méthode synchronisée comme montré ci-dessous et ajoutez le code suivant. Je vais expliquer ce qui se passe :

```java
public static synchronized Retrofit getInstance() {

    if (retrofit == null) {
        if (gson == null) {
            gson = new GsonBuilder().setLenient().create();
        }
        
        retrofit = new Retrofit.Builder()
                .baseUrl(BASE_URL)
                .addConverterFactory(GsonConverterFactory.create(gson))
                .addCallAdapterFactory(RxJavaCallAdapterFactory.create())
                .build();
                
    }
    
    return retrofit;
}
```

Nous créons une instance singleton de retrofit, si l'instance est déjà créée, nous la retournons simplement, sinon nous en créons une nouvelle.

Pour créer une nouvelle instance, nous utilisons la méthode Retrofit.Builder(). Nous définissons l'URL de base sur l'URL déclarée en haut, nous définissons l'usine de convertisseur comme Gson qui analysera la réponse JSON pour nous et ajoutons une usine d'adaptateur d'appel de RxJava 2.

> _Maintenant, vous pouvez demander ce qu'est un adaptateur d'appel ? Donc, un adaptateur d'appel est essentiellement un outil qui gère l'exécution et la gestion des réponses de retrofit. Lorsque le client reçoit une réponse du serveur, elle est sans signification pour l'utilisateur car elle est en bytes. Donc, l'adaptateur d'appel convertit ces bytes en objets java significatifs._  
>   
> _Pour en savoir plus sur les adaptateurs d'appel, consultez cet article génial : [https://futurestud.io/tutorials/retrofit-2-introduction-to-call-adapters](https://futurestud.io/tutorials/retrofit-2-introduction-to-call-adapters)_

Puisque nous avons ajouté l'usine **RxJavaCallAdapter**, elle enveloppe nos réponses dans des types **RxJava**.

Voici à quoi ressemble notre classe **RetrofitAdapter.java** une fois complète :

```java
public class RetrofitAdapter {

    private static Retrofit retrofit;
    private static Gson gson;
    private static final String BASE_URL = "https://jsonplaceholder.typicode.com";
    
    public static synchronized Retrofit getInstance() {
    
        if (retrofit == null) {
            if (gson == null) {
                gson = new GsonBuilder().setLenient().create();
            }
            
            retrofit = new Retrofit.Builder()
                    .baseUrl(BASE_URL)
                    .addConverterFactory(GsonConverterFactory.create(gson))
                    .addCallAdapterFactory(RxJavaCallAdapterFactory.create())
                    .build();
                    
        }
        
        return retrofit;
    }

}
```

#### Création d'un service API

Maintenant, nous allons créer une interface pour définir nos endpoints d'URL.

Créez un package nommé API à l'intérieur du package networking. À l'intérieur de API, créez une interface Java nommée UserService.java

Dans notre exemple très court et concis, nous allons appeler un seul endpoint, donc nous n'aurons qu'une seule méthode. Vous pouvez appeler de nombreux endpoints différents tels que pour la connexion, l'inscription, la déconnexion, etc.

Ajoutez une déclaration de méthode **getUsers()** et annotez-la avec le type de requête (GET ou POST) et passez l'endpoint.

Voici à quoi doit ressembler votre interface à la fin. Notez que nous retournons un **Observable** de type **List**, à la fin. Notre adaptateur d'appel RxJava fait le travail de créer un observable à partir de la réponse du serveur.

```java
public interface UserService {

    @GET("/posts/")
    Observable<List<User>> getUsers();

}
```

#### Liaison de l'adaptateur et du service

Nous devons lier notre classe d'adaptateur au service. Pour cela, créez un package utils à l'intérieur du package networking et créez une nouvelle classe nommée **NetworkingUtils.**

Créez une instance statique UserService et une méthode qui retournera une instance singleton de userService.

Voici à quoi ressemblera votre **NetworkingUtils** à la fin :

```java
public class NetworkingUtils {

    private static UserService userService;
    
    public static UserService getUserApiInstance() {
        if (userService == null)
            userService = RetrofitAdapter.getInstance().create(UserService.class);
            
        return userService;
    }
    
}
```

#### Création d'une classe utilitaire pour effectuer des appels API

J'ai vu des gens faire cela dans l'Interactor. L'Interactor est juste une autre couche dans votre architecture MVP — certaines personnes préfèrent l'inclure, d'autres non. Dans certains projets, vous trouverez des Data Managers au lieu d'un Interactor. Tout dépend de vos exigences/péférences personnelles, mais personnellement, je n'aime pas utiliser les interactors (tout comme je n'aime pas JS :P), donc je crée un **UserTask** ici.

Mais juste avant de créer cette classe, créons une classe de rappel personnalisée que nous pouvons utiliser pour recevoir des erreurs et des résultats. Dans le package racine, créez un package nommé callback et créez une interface nommée Callback à l'intérieur de ce package. Elle contiendra deux méthodes, une pour le résultat et une autre pour l'erreur. Voici à quoi elle ressemblera :

```java
public abstract class Callback<T> {
    public abstract void returnResult(T t);
    public abstract void returnError(String message);
}
```

Dans le package racine, créez un package nommé **utils**. À l'intérieur de ce package, créez une classe java nommée UserTask. Cette classe sera responsable de l'exécution des appels API et du retour du résultat au présentateur qui affichera le résultat ou l'erreur en fonction de ce que nous obtenons.

Si vous n'êtes pas familier avec RxJava, je vous recommande fortement de jeter un œil ici : [Comprendre les bases de RxJava](https://ayusch.com/understanding-rxjava-basics/).

J'ai expliqué tout le fonctionnement de observeOn et subscribeOn et quels sont leurs rôles. Une fois que vous l'avez parcouru, vous êtes prêt à partir.

Dans notre méthode **onNext**, nous retournerons le résultat, et dans onError, nous retournerons l'erreur.

Voici à quoi ressemble la classe UserTask.java à la fin :

```java
public class UserTask {

    public static void getUsers(final Callback<List<User>> callback) {
        NetworkingUtils.getUserApiInstance()
        
                .getUsers()
                .observeOn(AndroidSchedulers.mainThread())
                .subscribeOn(Schedulers.io())
                .subscribe(new Observer<List<User>>() {
                    @Override
                    public void onSubscribe(Disposable d) {
                    
                    }
                    
                    @Override
                    public void onNext(List<User> users) {
                        callback.returnResult(users);
                    }
                    
                    @Override
                    public void onError(Throwable e) {
                        callback.returnError(e.getMessage());
                    }
                    
                    @Override
                    public void onComplete() {
                    
                    }
                });
    }
    
}
```

### Finalisation

La majeure partie du travail étant déjà terminée, il nous reste à passer le résultat du présentateur à la vue et à définir l'adaptateur pour RecyclerView.

Pour ce faire, dirigez-vous vers la classe **UserPresenter.java** et dans la méthode loadUsers, appelez **UserTask.getUser()** et fournissez un rappel qui retourne le résultat ou l'erreur.

Dans la méthode returnResult, nous appellerons la méthode **mView.loadDataInList()** en passant une liste d'utilisateurs obtenus avec succès. Dans la méthode returnError, nous appellerons la méthode **mView.showError()** qui affichera les erreurs le cas échéant. Avec cela, notre classe de présentateur est complète, voici à quoi elle ressemble à la fin :

```java
public class UserPresenter implements UserContract.Presenter {
    UserContract.View mView;

    UserPresenter(UserContract.View mView) {
        this.mView = mView;
    }
    
    @Override
    public void loadUsers() {
        UserTask.getUsers(new Callback<List<User>>() {
            @Override
            public void returnResult(List<User> users) {
                mView.loadDataInList(users);
            }
            
            @Override
            public void returnError(String message) {
                mView.showError(message);
            }
        });
    }
    
    @Override
    public void start() {
        mView.init();
    }
    
}
```

Dans **UserActivity.java**, à l'intérieur de la méthode loadDataInList, instanciez notre customAdapter et définissez-le pour la recyclerview, et dans la méthode showError, affichez simplement un message toast. Voici à quoi ressemble notre UserActivity.java à la fin :

```java
public class UserActivity extends AppCompatActivity implements UserContract.View {
    
    private UserContract.Presenter mPresenter;
    private RecyclerView recyclerview;
    CustomAdapter adapter;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mPresenter = new UserPresenter(this);
        mPresenter.start();
    }
    
    @Override
    public void init() {
        recyclerview = findViewById(R.id.recyclerview);
        RecyclerView.LayoutManager manager = new LinearLayoutManager(this);
        recyclerview.setLayoutManager(manager);
        mPresenter.loadUsers();
    }
    
    @Override
    public void loadDataInList(List<User> users) {
        adapter = new CustomAdapter(users);
        recyclerview.setAdapter(adapter);
    }
    
    @Override
    public void showError(String message) {
        Toast.makeText(this,message,Toast.LENGTH_LONG).show();
    }
    
}
```

### Conclusion

C'est ainsi que vous pouvez configurer votre application Android pour utiliser Retrofit, RxJava et l'architecture MVP en tandem les uns avec les autres. Faites-moi savoir si vous avez des suggestions, dans la section des commentaires ci-dessous ou envoyez-moi un email et je répondrai dès que possible ?

![Image](https://cdn-media-1.freecodecamp.org/images/P0ZFbZwgADBFSwaND5ByjyNAUh38E6qBRuLP)

_Aimez ce que vous lisez ? N'oubliez pas de partager cet article sur [**Facebook**](https://www.facebook.com/AndroidVille), **WhatsApp**, et **LinkedIn**._

_Vous pouvez me suivre sur [LinkedIn](https://www.linkedin.com/in/ayuschjain), [Quora](https://www.quora.com/profile/Ayusch-Jain), [Twitter](https://twitter.com/ayuschjain), et [Instagram](https://www.instagram.com/androidville/) où je **réponds** aux questions liées au **développement mobile, en particulier Android et Flutter**._

**_Si vous souhaitez rester informé de tous les derniers articles, abonnez-vous à la newsletter hebdomadaire en entrant votre adresse e-mail dans le formulaire dans la section en haut à droite de cette page._**