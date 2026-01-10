---
title: How to set up networking in your Android app with Retrofit-RxJava-MVP
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
seo_title: null
seo_desc: 'By Ayusch Jain


  This article was originally posted here


  In this Android App development tutorial, I’ll be demonstrating how you can setup
  Retrofit and RxJava for networking in your android application along with MVP Architecture.

  We’ll be developing...'
---

By Ayusch Jain

> This article was originally posted [here](https://ayusch.com/networking-with-retrofit-rxjava-mvp)

In this Android App development tutorial, I’ll be demonstrating how you can setup Retrofit and RxJava for networking in your android application along with MVP Architecture.

We’ll be developing a very barebones application which will display some data in recyclerview. The data will be obtained from a fake JSON API hosted on [https://jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com). The application will display data in three columns namely ID, Title and Body.

Here are the prerequisites to this tutorial:

* [How to Implement MVP Architecture in Android](https://ayusch.com/mvp-architecture-android/)
* [Understanding RxJava Basics](https://ayusch.com/understanding-rxjava-basics)

Once you go through the above two, you are ready to move forward with this article. I’ve divided this into 4 phases:

* Setting up the project and building layouts.
* Setting up MVP Architecture.
* Creating Model class for data and adapter for RecyclerView.
* Setting up Networking with Retrofit and RxJava.

So, let’s get started!

> Note: Some [online schools](http://microverse.org) such as Udemy and Lynda also have good tutorials on RxJava

### Phase 1: Setting up the project and building layouts.

#### Create a new project

Create a new project in android studio. Go to File -> New Project and select **“Empty Activity”.** Then click Finish.

![Image](https://cdn-media-1.freecodecamp.org/images/QBay9VeS0891s9mHP3ExEtJ-zAGTa8QBOyrl)

#### **Adding a Recyclerview**

To add a recyclerview to your project, open app level build.gradle file and add the following dependency at the bottom:

```
implementation 'com.android.support:design:28.0.0'
```

> _Note: You can also add recyclerview directly instead of the entire design library, but most of you might already have it included so I’m including the design library in this example. You can include just the recyclerview as well._

Now head over to your main layout file, in my case activity_main.xml and add a recyclerview inside the root layout:

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

#### Building Recyclerview Item

Now let’s start building the RecyclerView rows. Here we are only concerned about the architecture of our Android application and how Retrofit, RxJava and MVP Architecture can work in tandem, so don’t complain about the look of the UI :P. You can definitely go ahead and beautify it.

We’ll be creating a really simple three column layout. The first column will display the ID of the item, the second column will display the Title, and finally, the third column will display the body/description.

Go to res->layout and right click on the layout folder. Create a new **“Layout Resource File”.** Name it whatever you want, in my case I’ll name it **recycler_item.**

To create a three-column layout, add a LinearLayout as the root. Then add three textviews and set their width to 0 and their weight to 1,2,3 respectively. This will divide the entire width of your screen into 3 columns in the proportion 1:2:3.

Here’s how your layout will look like:

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
        android:text="Title" />
    
    <TextView
        android:id="@+id/user_body"
        android:layout_width="0dp"
        android:layout_height="wrap_content"
        android:layout_weight="3"
        android:gravity="center"
        android:padding="4dp"
        android:text="Body" />
    
</LinearLayout>
```

**Again, since this is not a design tutorial the UI might not look very pretty, so feel free to customize it as you like ?**

Now with the layouts all done, we can head over to set up our android application in accordance with MVP Architecture. Again, if you aren’t really familiar with MVP, I strongly suggest that you have a look here: [MVP Architecture in Android](https://ayusch.com/mvp-architecture-android/).

### Phase 2: Setting up MVP Architecture

#### Creating the contract

Many people like to keep their View and Presenter interfaces in different files, but according to Google’s suggested guidelines, I like to create an outer interface (Wrapper) named **Contract** and then place my View and Presenter Interfaces inside it.

The benefit of this is that you won’t have to go looking at different files for the view and presenter associated with a single activity, it’s all in a single place. That’s how I like it, but feel free to explore other techniques.

So now let’s create a UserActivityContract. Create a new package named **“contract”.** Inside that package, create a new Java Interface UserActivityContract.

Within **UserActivityContract**, add two nested interfaces: View and Presenter. This is how your contract will look like at the end:

```java
public interface UserContract {
    interface View {
    
    }
    
    interface Presenter {
    
    }
    
}
```

Now let’s add some methods to these. Let’s talk about the View first, we’ll be doing 3 major things inside our view:

* Initial setup of recyclerview (adding layout manager).
* Creating an adapter from recyclerview using the list of users obtained from the API.
* Showing some error message in case any error occurs.

So, let’s add a method for each one of these:

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

Next, let’s talk about the Presenter. The only real task of the presenter is to get the data from the API and send it to the View. So, add a method **loadUsers()** we’ll be making our API call here and passing the result to view if successful, else an error message.

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

Notice that apart from loadUsers(), we have also added a method named **start(),** this is more of like an initializer method for the presenter. You can perform all sorts of init tasks here such as initializing some variables, calling a method of the view to show some init messages etc. Here I’m using it to initialize the Recyclerview inside my UserActivity.java class.

#### Creating Presenter and Implementing View

Once done with the interfaces, it’s time to implement them.

Create a new class named UserPresenter and implement UserContract.Presenter on it and implement the required methods.

Now, open your UserActivity.java class and implement the interface UserContract.View and implement all the required methods. Add a field for the presenter in your activity and initialize it in onCreate as shown below:

```java
mPresenter = new UserPresenter(this);
mPresenter.start();
```

This will call the constructor of our presenter and bind the View and Presenter together. When we call the start method on presenter, presenter in-turn calls the init() method which starts our initialization process.

**With this,** we finish **Phase 2** of our project. Now let’s head over to **Phase 3** and create our model class and a custom adapter to bind data to recyclerview.

### Phase 3: Creating Model class for data and adapter for RecyclerView

#### Creating the model

Let’s go ahead and create our model which will be a POJO class for our data. If you look closely at the JSON response, it consists of 4 fields: id, userId, title, body. And all of this inside a JSON object. And many such JSON objects in an array. So, this is a fairly simple POJO class to create.

But before this, let’s add a dependency for GSON, which will be used to parse the JSON response. Add the following line to your dependencies:

```
implementation 'com.squareup.retrofit2:converter-gson:2.4.0'
```

> _Note: This is not the actual GSON dependency, this is a converter which uses GSON for serialization to and from JSON._

Now, create a package named **model** and inside it, create a java file named **User**. Add the four fields and annotate each of the fields with **@SerializedName**. Now let’s create getters and setters for the fields. Android Studio does this automatically for you, just press ALT+INS on your keyboard and select getters and setters.

This is how your POJO class would look like at the end:

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

> _Note: toString method is optional. I like to include it because when printing log statements, it prints the formatted json._

### Creating RecyclerView Adapter

Let’s now create the recyclerview adapter. Create a package named adapter and create a new Java class named **CustomAdapter.java** inside it. Extend the class from RecyclerView.Adapter class. It will show an error, just press ALT+Enter and override all the required methods.

Inside **CustomAdapter.java** create a nested class named MyViewHolder and extend it from RecyclerView.ViewHolder. Then create a constructor and initialize all the textviews as shown below:

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

We’ll be passing a list of users to this adapter and we would be doing that in the **constructor**. So, first create a field **List<Us**er> and then create a constructor which will take a List<User> as its argument. Now, set the field property to the one obtained in the constructor.

When you overrode the methods, you got onCreateViewHolder. In that method, we’ll inflate our layout for the recyclerview item and return a view holder from it. Head over to onCreateViewHolder and add the following code:

```java
@Override
public MyViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
    View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.recycler_item, parent, false);
    return new MyViewHolder(view);
}
```

Now, in **onBindViewHolder**, we’ll bind the data to our views. This is how the final adapter would look like:

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

### Phase 4: Setting up Networking with Retrofit and RxJava

This is the crux of our android application. This is what you all came here for, so let’s get started.

I’ve divided setting up networking in our project into 4 parts:

* Creating a Retrofit adapter.
* Setting up an API Service interface which defines our endpoints.
* Creating a NetworkingUtil class to bind the Adapter and Service.
* Creating a Utility class to make API calls and return the result to the presenter.

So, let’s get started.

#### Creating a Retrofit Adapter

Create a package named “networking”, and inside networking, create another package named “adapter” (this is how I like my package management and is by no means the recommended way of doing things, but it suits me so +1).

Inside that package, create a class named RetrofitAdapter. In this class we’ll define the following things:

* A converter factory to parse JSON response into our POJO class.
* A call adapter factory.
* A base URL.

Let’s start by adding a **BASE_URL** filed at the top. Set the base URL to [https://jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com)

Now, create a static instance of Gson and Retrofit at the top. Now, create a synchronized method as shown below and add the following code. I’ll explain what’s going on:

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

We are creating a singleton instance of retrofit, if the instance is already created, we just return it, else we create a new one.

To create a new instance, we are using the Retrofit.Builder() method. We set the Base URL to the URL declared at the top, we set the converter factory as Gson which will parse the JSON response for us and add a call adapter factory from RxJava 2.

> _Now, you may ask what is a call adapter? So, a call adapter is basically a tool which manages the execution, and response handling of retrofit. When the client receives a response from the server, it’s meaningless to the user as it is in bytes. So the call adapter converts those bytes into meaningful java objects._  
>   
> _To know more about call adapters take a look at this awesome article : [https://futurestud.io/tutorials/retrofit-2-introduction-to-call-adapters](https://futurestud.io/tutorials/retrofit-2-introduction-to-call-adapters)_

Since we have added **RxJavaCallAdapter** factory, it wraps our responses into **RxJava** types.

This is how our **RetrofitAdapter.java class** looks when complete:

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

#### Creating an API Service

Now, we’ll create an interface to define our URL endpoints.

Create a package named API inside the networking package. Inside API, create a Java Interface named UserService.java

In our very short and concise example, we’ll be calling just a single endpoint, so we’ll have only one method. You can call many different endpoints such as for login, signup, logout etc…

Add a method declaration **getUsers()** and annotate it with the type of request (GET or POST) and pass the endpoint.

This is how your interface must look like at the end. Note that we are returning an **Observable** of type **List**, at the end. Our RxJava call adapter does the work of creating an observable out of the response from the server.

```java
public interface UserService {

    @GET("/posts/")
    Observable<List<User>> getUsers();

}
```

#### Binding Adapter and Service

We need to bind our adapter class to the service. For this, create a utils package inside the networking package and create a new class named **NetworkingUtils.**

Create a static UserService instance and a method which will return a singleton instance of the userService.

This is how your **NetworkingUtils** would look like at the end:

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

#### Creating a Utility class to make API calls

I’ve seen people do this in the Interactor. Interactor is just another layer in your MVP Architecture — some people prefer to include it, some don’t. In some projects, you’ll find Data Managers instead of an Interactor. It all comes down to your personal requirements/preference, but I personally don’t like using interactors (just like I don’t like JS :P) so I am creating a **UserTask** here.

But just before creating this class, let’s create a custom callback class which we can use to receive errors and results. In the root package, create a package named callback and create an interface named Callback inside this package. It will contain two methods, one for the result and other for error. This is how it’ll look like:

```java
public abstract class Callback<T> {
    public abstract void returnResult(T t);
    public abstract void returnError(String message);
}
```

In the root package, create a package named **utils**. Inside this package create a java class named UserTask. This class will be responsible to make API calls and return the result to the presenter which will show the result or the error depending upon what we get.

If you aren’t familiar with RxJava, I strongly recommend having a look here: [Understanding RxJava Basics](https://ayusch.com/understanding-rxjava-basics/).

I’ve explained all about how observeOn and subscribeOn work and what are their roles. Once you’ve gone through it, you’re good to go.

In our **onNext** method, we’ll return the result, and in onError, we’ll return the error.

This is how UserTask.java class looks like at the end:

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

### Finishing Up

With the major part of the work already done, we’re now left with passing the result from presenter to the view and setting the adapter for RecyclerView.

To do this, head over to **UserPresenter.java** class and in the loadUsers method, call **UserTask.getUser()** and provide a callback which returns the result or error.

In the returnResult method, we’ll call **mView.loadDataInList()** method passing a list of users successfully obtained. In the returnError method, we’ll call the **mView.showError()** method which’ll display errors if any. With this, our presenter class is complete, here’s how it looks like at the end:

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

In **UserActivity.java**, inside the loadDataInList method, instantiate our customAdapter and set it to recyclerview, and in showError method, just display a toast message. This is how our UserActivity.java looks like at the end:

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

This is how you can set up your android application to use Retrofit, RxJava and MVP Architecture in tandem with each other. Let me know if you have any suggestions, in the comments section below or shoot me an email and I’ll respond asap ?

![Image](https://cdn-media-1.freecodecamp.org/images/P0ZFbZwgADBFSwaND5ByjyNAUh38E6qBRuLP)

_Like what you read? Don’t forget to share this post on [**Facebook**](https://www.facebook.com/AndroidVille), **Whatsapp**, and **LinkedIn**._

_You can follow me on [LinkedIn](https://www.linkedin.com/in/ayuschjain), [Quora](https://www.quora.com/profile/Ayusch-Jain), [Twitter](https://twitter.com/ayuschjain), and [Instagram](https://www.instagram.com/androidville/) where I **answer** questions related to **Mobile Development, especially Android and Flutter**._

**_If you want to stay updated with all the latest articles, subscribe to the weekly newsletter by entering your email address in the form on the top right section of this page._**

