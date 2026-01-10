---
title: How to Use Model-View-ViewModel on Android Like a Pro
subtitle: ''
author: Ryan Michael Kay
co_authors: []
series: null
date: '2020-12-28T15:21:14.000Z'
originalURL: https://freecodecamp.org/news/model-view-viewmodel-android-tutorial
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fe0dcbae6787e098394168f.jpg
tags:
- name: Android
  slug: android
- name: android app development
  slug: android-app-development
- name: mvp
  slug: mvp
- name: software architecture
  slug: software-architecture
seo_title: null
seo_desc: 'My goal in this article is to explain why the Model-View-ViewModel architectural
  pattern presents a very awkward separation of concerns in some situations with regard
  to the presentation logic of a GUI architecture.

  We will explore two variants of MV...'
---

My goal in this article is to explain why the Model-View-ViewModel architectural pattern presents a very awkward separation of concerns in some situations with regard to the presentation logic of a GUI architecture.

We will explore two variants of MVVM (there is **not** just one way to do it), and the reasons why you may prefer one variant over another, based on project requirements.

## MVVM vs MVP/MVC?

It is quite likely that the most common question I am asked during my live Sunday Q&A sessions, is something like:

> MVVM vs MVP/MVC?

Whenever I am asked this question, I am quick emphasize the idea that no single GUI architecture works great in all situations.

Why, you may ask? The best architecture (or at least a good choice) for a given application depends strongly on the requirements at hand.

Let us briefly think about what this word **requirements** actually means:

* **How complex is your UI?** A simple UI does not generally require complex logic to coordinate it, whereas a complex UI may require extensive logic and fine-grained control to work smoothly.
    
* **How much do you care about testing?** Generally speaking, classes which are tightly coupled to frameworks and the OS (especially the **user interface**) require extra work to test.
    
* **How much re-usability and abstraction do you wish to promote?** What if you want to share the back end, domain, and even presentation logic of your application across different platforms?
    
* Are you by nature **pragmatic**, **perfectionist**, **lazy**, or all of the above at different times, in different situations?
    

I would love to write an article where I discuss in fine detail how MVVM works with respect to the requirements and concerns listed above. Unfortunately, some of you have likely been mislead into thinking that there is only one way to do MVVM.

Instead, I will discuss two different approaches to the general idea of MVVM which present very distinct benefits and disadvantages. But first, let us start with the general idea.

## Thou Shalt Not Reference Thy View Classes

*For my friends who cannot read old English:* “**You may not reference view classes**."

Apart from using the name ViewModel (which itself is confusing if the class is full of **logic**), the one iron-clad rule of MVVM architecture is that you may never reference a View, from ViewModel.

Now, the first area of confusion can arise from this word “reference,” which I will restate using several different levels of jargon:

* Your ViewModels may not possess any references (member variables, properties, mutable/immutable fields) to any Views
    
* Your ViewModels may not depend on any Views
    
* Your ViewModels may not talk directly to your Views
    

Now, on the Android platform, the reason for this rule is not simply that breaking it is bad because someone who seems to know about software architecture told you it is bad.

When using the [ViewModel](https://developer.android.com/topic/libraries/architecture/viewmodel) class from Architecture Components (which is designed to have its instance **persist** longer than the Fragment/Activity lifecycle **when appropriate**), referencing a View is asking for **SERIOUS MEMORY LEAKS**.

As for why MVVM in general does not allow such references, the goal is **hypothetically** to make both the View and the ViewModel easier to test and write.

Others may also point out that it promotes reusability of ViewModels, but this is **exactly where things break down with this pattern**.

Before we look at the code, please note that **I personally do not use LiveData** in my own production code. I prefer to write my own Publisher-Subscriber Pattern these days, but what I say below applies to any library which allows for the PubSub/Observer Pattern link from the ViewModel to the View.

This article is accompanied by a video tutorial covering many of the same ideas here:

%[https://youtu.be/j47CSoJ_Hc4] 

## ViewLogic + ViewModel or View + ViewModelController?

When I said “break down” in the previous section, I do not mean to say that the pattern literally breaks. I mean that it breaks down into (at least) two different approaches which have very distinct appearances, benefits, and consequences.

Let us consider these two approaches, and when you may wish to prefer one over the other.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/1_TfbPt5-CcYCjDu2hapFXNg.png align="left")

*Boromir explains that MVVM is not a magic wand that makes your application's presentation logic disappear.*

### First Approach: Prioritize Reusable ViewModels

As far as I can tell, most people who implement MVVM make it a goal to promote re-usability of ViewModels, so that they may be reused for *n* number of different Views (many-to-one ratio).

In simple terms, there are two ways you can achieve this re-usability:

* By not referencing a specific View. Hopefully this is not news to you at this point.
    
* By **knowing** as little as possible about the details of the **UI** in general
    

The second point may sound vague or counter-intuitive (how can it know anything about something which it does not reference?), so I think it is time to look at some code:

```kotlin
class NoteViewModel(val repo: NoteRepo): ViewModel(){
    //Note: you may also publish data to the View via Databinding, RxJava Observables, and other approaches. Although I do not like to use LiveData in back end classes, it works great with Android front end with AAC
    val noteState: MutableLiveData<Note>()
    //...
    fun handleEvent(event: NoteEvent) {
        when (event) {
            is NoteEvent.OnStart -> getNote(event.noteId)
            //...
        }
    }
    private fun getNote(noteId: String){
        noteState.value = repo.getNote(noteId)
    }
}
```

While this is a very simplified example, the point is that the only thing which this particular ViewModel exposes publicly (other than the handleEvent function), is a simple Note object:

```kotlin
data class Note(val creationDate:String,
                val contents:String,
                val imageUrl: String,
                val creator: User?)
```

With this particular approach, the ViewModel is well and truly decoupled from not just a particular View, but also the details, and by extension, **presentation logic** of any particular View.

If what I am saying still seems vague, I promise it will be clear once I describe the other approach.

Although my earlier heading, “**ViewLogic + ViewModel…**” is not meant to be used or taken seriously, I mean that by having very decoupled and re-usable ViewModels, we are now depending on the View itself to do the work of figuring out how to render/bind this Note object on screen.

**Some of us do not like filling View classes with Logic.**

This is where things get very muddy and dependent on project **requirements**. I am not saying that filling View classes with logic such as…:

```pgsql
private fun observeViewModel() {
    viewModel.notes.observe(
        viewLifecycleOwner,
        Observer { notes: List<Note> ->
            if (notes.isEmpty()) showEmptyState()
            else showNoteList(notes)
        }
    )
   //..
}
```

…is **always** a bad thing, but classes which are tightly coupled to the platform (like Fragments) are difficult to test, and classes with logic in them are the most important classes to test!

In a word, it is a failure to apply what I consider to be the golden principle of any good architecture: **Separation of concerns**\*\*.\*\*

My personal opinion is that it is worth it to apply separation of concerns to a very high degree. But make no mistake that plenty of cash cow applications have been written by people who do not have the faintest clue about what that means.

In any case, the approach we will discuss next, while **having its own side effects**, once again removes the presentation logic from the View.

Well, most of it anyways.

### Second Approach: Humble View, Control-Freak ViewModel

Sometimes not having fine-grained control over your Views (which is a consequence of prioritizing re-usability of ViewModels), actually kind of sucks.

To make me even less enthusiastic about applying the previous approach indiscriminately, I find that I **often** **do not** **need to reuse a ViewModel**.

> *Ironically, “too much abstraction” is a common critique of MVP over MVVM.*

With that being said, one cannot simply add a reference back in to the ViewModel in order to regain this fine-grained control over the View. That would basically just be MVP + memory leaks (assuming you are still using ViewModel from AAC).

The alternative then, is to build your ViewModels such that they contain almost all of the **behaviour**, **state**, and **presentation logic** of a given View. The View must still bind to the ViewModel of course, but enough details about the View are present in the ViewModel that the View’s functions are reduced to one liners (with small exceptions).

In Martin Fowler’s naming conventions, this is known as [Passive View/Screen](https://martinfowler.com/eaaDev/PassiveScreen.html). A more generally applicable name for this approach is the **Humble Object Pattern**.

In order to achieve this, you must essentially have your ViewModel possess an observable field (however you achieve that – data binding, Rx, LiveData, whatever) for every control or widget present in the View:

```kotlin
class UserViewModel(
    val repo: IUserRepository,
){

    //The actual data model is kept private to avoid unwanted tampering
    private val userState = MutableLiveData<User>()

    //Control Logic
    internal val authAttemptState = MutableLiveData<Unit>()
    internal val startAnimation = MutableLiveData<Unit>()

    //UI Binding
    internal val signInStatusText = MutableLiveData<String>()
    internal val authButtonText = MutableLiveData<String>()
    internal val satelliteDrawable = MutableLiveData<String>()

    private fun showErrorState() {
        signInStatusText.value = LOGIN_ERROR
        authButtonText.value = SIGN_IN
        satelliteDrawable.value = ANTENNA_EMPTY
    }
    //...
}
```

Subsequently, the View will still need to wire itself up to the ViewModel, but the functions required to do so become trivially simple to write:

```kotlin
class LoginView : Fragment() {

    private lateinit var viewModel: UserViewModel
    //...
    
    //Create and bind to ViewModel
    override fun onStart() {
        super.onStart()
        viewModel = ViewModelProviders.of(
        //...   
        ).get(UserViewModel::class.java)

        //start background anim
        (root_fragment_login.background as AnimationDrawable).startWithFade()

        setUpClickListeners()
        observeViewModel()

        viewModel.handleEvent(LoginEvent.OnStart)
    }

    private fun setUpClickListeners() {
      //...
    }

    private fun observeViewModel() {
        viewModel.signInStatusText.observe(
            viewLifecycleOwner,
            Observer {
                //"it" is the value of the MutableLiveData object, which is inferred to be a String automatically
                lbl_login_status_display.text = it
            }
        )

        viewModel.authButtonText.observe(
            viewLifecycleOwner,
            Observer {
                btn_auth_attempt.text = it
            }
        )

        viewModel.startAnimation.observe(
            viewLifecycleOwner,
            Observer {
                imv_antenna_animation.setImageResource(
                    resources.getIdentifier(ANTENNA_LOOP, "drawable", activity?.packageName)
                )
                (imv_antenna_animation.drawable as AnimationDrawable).start()
            }
        )

        viewModel.authAttemptState.observe(
            viewLifecycleOwner,
            Observer { startSignInFlow() }
        )

        viewModel.satelliteDrawable.observe(
            viewLifecycleOwner,
            Observer {
                imv_antenna_animation.setImageResource(
                    resources.getIdentifier(it, "drawable", activity?.packageName)
                )
            }
        )
    }
```

You can find the full code for this example [here](https://github.com/BracketCove/JetpackNotesMvvmKotlin/tree/master/app/src/main/java/com/wiseassblog/jetpacknotesmvvmkotlin/login).

As you have probably noticed, we are probably not going to be re-using this ViewModel **anywhere else**. Also, our View has become sufficiently humble (depending on your standards and preferences for code coverage), and very easy to write.

Sometimes you will run in to situations where you must find some kind of half-measure between the distribution of **presentation logic** between Views and ViewModels, which does not strictly follow either of these approaches.

I am not advocating one approach over another, but rather encouraging you to be flexible in your approach, based on the requirements at hand.

## Choose Your Architecture Based on Preferences And Requirements

The point of this article was to look at two different approaches which a developer can take in terms of constructing a MVVM style GUI architecture on the Android Platform (with some carry over to other platforms).

In truth, we could get more specific about small differences even within these two approaches.

* Should the View observe a field for every individual widget/control it possesses, or should it observe one field which publishes a single **model** to render the entire View anew each time?
    
* Maybe we could avoid having to make our ViewModels one-to-one, while keeping our Views as Humble Objects, simply by adding something like a Presenter or Controller to the mix?
    

Talk is cheap, and I strongly advise you to try and learn these things **in the code** so that you do not need to rely on people like me to tell you what to do.

Ultimately, I think the two elements which make for a great architecture come down to the following considerations:

Firstly, play with several approaches until you find one which you **prefer**. This is best done by actually building an application (it can be simple) in each style, and seeing what **feels right**.

Secondly, understand that preferences aside, different styles will tend to emphasize different benefits in exchange for different deficits. Eventually, you will be able to pick good choices based on your understanding of the project requirements rather than **blind faith**.

### Learn More About Software Architecture:

%[https://youtu.be/B_C41SF0KbI] 

#### Social

[https://www.instagram.com/rkay301/](https://www.instagram.com/wiseassbrand/)  
[https://www.facebook.com/wiseassblog/](https://www.facebook.com/wiseassblog/)  
[https://twitter.com/wiseass301](https://twitter.com/wiseass301)  
[http://wiseassblog.com/](http://wiseassblog.com/)
