---
title: Comment utiliser Model-View-ViewModel sur Android comme un pro
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
seo_title: Comment utiliser Model-View-ViewModel sur Android comme un pro
seo_desc: 'My goal in this article is to explain why the Model-View-ViewModel architectural
  pattern presents a very awkward separation of concerns in some situations with regard
  to the presentation logic of a GUI architecture.

  We will explore two variants of MV...'
---

Mon objectif dans cet article est d'expliquer pourquoi le modèle architectural Model-View-ViewModel présente une séparation des préoccupations très maladroite dans certaines situations concernant la logique de présentation d'une architecture GUI.

Nous explorerons deux variantes de MVVM (il n'y a **pas** qu'une seule façon de le faire), et les raisons pour lesquelles vous pourriez préférer une variante à une autre, en fonction des exigences du projet.

## MVVM vs MVP/MVC ?

Il est assez probable que la question la plus courante que l'on me pose lors de mes sessions de questions-réponses en direct le dimanche soit quelque chose comme :

> MVVM vs MVP/MVC ?

Chaque fois que l'on me pose cette question, je m'empresse de souligner l'idée qu'aucune architecture GUI ne fonctionne parfaitement dans toutes les situations.

Pourquoi, pourriez-vous demander ? La meilleure architecture (ou au moins un bon choix) pour une application donnée dépend fortement des exigences en question.

Réfléchissons brièvement à ce que signifie réellement ce mot **exigences** :

* **À quel point votre interface utilisateur est-elle complexe ?** Une interface utilisateur simple ne nécessite généralement pas de logique complexe pour la coordonner, tandis qu'une interface utilisateur complexe peut nécessiter une logique extensive et un contrôle fin pour fonctionner en douceur.

* **À quel point vous souciez-vous des tests ?** En général, les classes qui sont étroitement couplées aux frameworks et au système d'exploitation (en particulier l'**interface utilisateur**) nécessitent un travail supplémentaire pour être testées.

* **Combien de réutilisabilité et d'abstraction souhaitez-vous promouvoir ?** Que se passe-t-il si vous souhaitez partager la logique backend, le domaine, et même la logique de présentation de votre application sur différentes plateformes ?

* Êtes-vous par nature **pragmatique**, **perfectionniste**, **paresseux**, ou tout cela à différents moments, dans différentes situations ?

J'adorerais écrire un article où je discute en détail comment MVVM fonctionne par rapport aux exigences et préoccupations listées ci-dessus. Malheureusement, certains d'entre vous ont probablement été induits en erreur en pensant qu'il n'y a qu'une seule façon de faire MVVM.

Au lieu de cela, je vais discuter de deux approches différentes de l'idée générale de MVVM qui présentent des avantages et des inconvénients très distincts. Mais d'abord, commençons par l'idée générale.

## Tu ne dois pas référencer tes classes de vue

*Pour mes amis qui ne peuvent pas lire l'anglais ancien :* « **Tu ne dois pas référencer les classes de vue** ».

Outre l'utilisation du nom ViewModel (qui est en soi confus si la classe est pleine de **logique**), la règle immuable de l'architecture MVVM est que tu ne dois jamais référencer une Vue, depuis ViewModel.

Maintenant, la première zone de confusion peut provenir de ce mot « référence », que je vais reformuler en utilisant plusieurs niveaux de jargon différents :

* Tes ViewModels ne doivent pas posséder de références (variables membres, propriétés, champs mutables/immuables) à des Vues

* Tes ViewModels ne doivent pas dépendre de Vues

* Tes ViewModels ne doivent pas parler directement à tes Vues

Maintenant, sur la plateforme Android, la raison de cette règle n'est pas simplement que la briser est mauvais parce que quelqu'un qui semble connaître l'architecture logicielle te l'a dit.

Lorsque tu utilises la classe [ViewModel](https://developer.android.com/topic/libraries/architecture/viewmodel) des composants d'architecture (qui est conçue pour que son instance **persiste** plus longtemps que le cycle de vie du Fragment/Activity **lorsque cela est approprié**), référencer une Vue demande des **FUITES DE MÉMOIRE SÉRIEUSES**.

Quant à pourquoi MVVM en général n'autorise pas de telles références, le but est **hypothétiquement** de rendre à la fois la Vue et le ViewModel plus faciles à tester et à écrire.

D'autres peuvent également souligner que cela favorise la réutilisabilité des ViewModels, mais c'est **exactement là que les choses se décomposent avec ce modèle**.

Avant de regarder le code, veuillez noter que **je n'utilise pas personnellement LiveData** dans mon propre code de production. Je préfère écrire mon propre modèle Publisher-Subscriber ces jours-ci, mais ce que je dis ci-dessous s'applique à toute bibliothèque qui permet le lien PubSub/Observer Pattern du ViewModel à la Vue.

Cet article est accompagné d'un tutoriel vidéo couvrant de nombreuses idées similaires ici :

%[https://youtu.be/j47CSoJ_Hc4]

## ViewLogic + ViewModel ou View + ViewModelController ?

Lorsque j'ai dit « se décomposer » dans la section précédente, je ne veux pas dire que le modèle se brise littéralement. Je veux dire qu'il se décompose en (au moins) deux approches différentes qui ont des apparences, des avantages et des conséquences très distincts.

Examinons ces deux approches, et quand vous pourriez souhaiter préférer l'une à l'autre.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/1_TfbPt5-CcYCjDu2hapFXNg.png align="left")

*Boromir explique que MVVM n'est pas une baguette magique qui fait disparaître la logique de présentation de votre application.*

### Première approche : Prioriser les ViewModels réutilisables

Pour autant que je sache, la plupart des personnes qui implémentent MVVM en font un objectif de promouvoir la réutilisabilité des ViewModels, afin qu'ils puissent être réutilisés pour *n* nombre de Vues différentes (ratio plusieurs-à-un).

En termes simples, il y a deux façons d'atteindre cette réutilisabilité :

* En ne référençant pas une Vue spécifique. Espérons que ce n'est pas une nouvelle pour vous à ce stade.

* En **connaissant** aussi peu que possible les détails de l'**UI** en général

Le deuxième point peut sembler vague ou contre-intuitif (comment peut-il connaître quelque chose qu'il ne référence pas ?), donc je pense qu'il est temps de regarder un peu de code :

```kotlin
class NoteViewModel(val repo: NoteRepo): ViewModel(){
    //Note: vous pouvez également publier des données vers la Vue via Databinding, RxJava Observables, et d'autres approches. Bien que je n'aime pas utiliser LiveData dans les classes backend, cela fonctionne très bien avec le frontend Android avec AAC
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

Bien que ce soit un exemple très simplifié, le point est que la seule chose que ce ViewModel particulier expose publiquement (autre que la fonction handleEvent), est un simple objet Note :

```kotlin
data class Note(val creationDate:String,
                val contents:String,
                val imageUrl: String,
                val creator: User?)
```

Avec cette approche particulière, le ViewModel est bien et véritablement découplé non seulement d'une Vue particulière, mais aussi des détails, et par extension, de la **logique de présentation** de toute Vue particulière.

Si ce que je dis semble encore vague, je promets que cela deviendra clair une fois que j'aurai décrit l'autre approche.

Bien que mon titre précédent, « **ViewLogic + ViewModel…** » ne soit pas destiné à être utilisé ou pris au sérieux, je veux dire qu'en ayant des ViewModels très découplés et réutilisables, nous dépendons maintenant de la Vue elle-même pour faire le travail de déterminer comment rendre/lier cet objet Note à l'écran.

**Certains d'entre nous n'aiment pas remplir les classes de Vue avec de la logique.**

C'est là que les choses deviennent très floues et dépendantes des exigences du **projet**. Je ne dis pas que remplir les classes de Vue avec de la logique telle que…

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

…est **toujours** une mauvaise chose, mais les classes qui sont étroitement couplées à la plateforme (comme les Fragments) sont difficiles à tester, et les classes avec de la logique sont les plus importantes à tester !

En un mot, c'est un échec à appliquer ce que je considère être le principe d'or de toute bonne architecture : **Séparation des préoccupations**\*\*.\*\*

Mon opinion personnelle est qu'il vaut la peine d'appliquer la séparation des préoccupations à un degré très élevé. Mais ne vous y trompez pas, de nombreuses applications vaches à lait ont été écrites par des personnes qui n'ont pas la moindre idée de ce que cela signifie.

Dans tous les cas, l'approche que nous allons discuter ensuite, bien que **ayant ses propres effets secondaires**, enlève à nouveau la logique de présentation de la Vue.

Eh bien, la plupart du temps en tout cas.

### Deuxième approche : Vue humble, ViewModel contrôleur

Parfois, ne pas avoir de contrôle fin sur vos Vues (ce qui est une conséquence de la priorisation de la réutilisabilité des ViewModels), c'est vraiment nul.

Pour me rendre encore moins enthousiaste à appliquer l'approche précédente de manière indiscriminée, je trouve que je **n'ai souvent pas besoin** de réutiliser un ViewModel.

> *Ironiquement, « trop d'abstraction » est une critique courante de MVP par rapport à MVVM.*

Cela dit, on ne peut pas simplement ajouter une référence au ViewModel pour retrouver ce contrôle fin sur la Vue. Cela serait essentiellement MVP + fuites de mémoire (en supposant que vous utilisez toujours ViewModel depuis AAC).

L'alternative alors est de construire vos ViewModels de manière à ce qu'ils contiennent presque toute la **comportement**, l'**état**, et la **logique de présentation** d'une Vue donnée. La Vue doit toujours se lier au ViewModel, bien sûr, mais suffisamment de détails sur la Vue sont présents dans le ViewModel pour que les fonctions de la Vue soient réduites à des lignes uniques (avec de petites exceptions).

Dans les conventions de nommage de Martin Fowler, cela est connu sous le nom de [Passive View/Screen](https://martinfowler.com/eaaDev/PassiveScreen.html). Un nom plus généralement applicable pour cette approche est le **Humble Object Pattern**.

Pour y parvenir, vous devez essentiellement faire en sorte que votre ViewModel possède un champ observable (quelle que soit la manière dont vous y parvenez - data binding, Rx, LiveData, peu importe) pour chaque contrôle ou widget présent dans la Vue :

```kotlin
class UserViewModel(
    val repo: IUserRepository,
){

    //Le modèle de données réel est gardé privé pour éviter les manipulations indésirables
    private val userState = MutableLiveData<User>()

    //Logique de contrôle
    internal val authAttemptState = MutableLiveData<Unit>()
    internal val startAnimation = MutableLiveData<Unit>()

    //Liaison UI
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

Par la suite, la Vue devra toujours se connecter au ViewModel, mais les fonctions requises pour le faire deviennent trivialement simples à écrire :

```kotlin
class LoginView : Fragment() {

    private lateinit var viewModel: UserViewModel
    //...
    
    //Créer et lier au ViewModel
    override fun onStart() {
        super.onStart()
        viewModel = ViewModelProviders.of(
        //...   
        ).get(UserViewModel::class.java)

        //démarrer l'animation de fond
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
                //"it" est la valeur de l'objet MutableLiveData, qui est inférée comme étant une String automatiquement
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

Vous pouvez trouver le code complet de cet exemple [ici](https://github.com/BracketCove/JetpackNotesMvvmKotlin/tree/master/app/src/main/java/com/wiseassblog/jetpacknotesmvvmkotlin/login).

Comme vous l'avez probablement remarqué, nous ne allons probablement pas réutiliser ce ViewModel **ailleurs**. De plus, notre Vue est devenue suffisamment humble (selon vos normes et préférences pour la couverture de code), et très facile à écrire.

Parfois, vous rencontrerez des situations où vous devrez trouver une sorte de demi-mesure entre la distribution de la **logique de présentation** entre les Vues et les ViewModels, qui ne suit pas strictement l'une ou l'autre de ces approches.

Je ne prône pas une approche plutôt qu'une autre, mais j'encourage plutôt à être flexible dans votre approche, en fonction des exigences en question.

## Choisissez votre architecture en fonction des préférences et des exigences

Le but de cet article était d'examiner deux approches différentes qu'un développeur peut adopter en termes de construction d'une architecture GUI de style MVVM sur la plateforme Android (avec un certain report sur d'autres plateformes).

En vérité, nous pourrions être plus spécifiques sur les petites différences même au sein de ces deux approches.

* La Vue doit-elle observer un champ pour chaque widget/contrôle individuel qu'elle possède, ou doit-elle observer un champ qui publie un seul **modèle** pour rendre toute la Vue à nouveau chaque fois ?

* Peut-être pourrions-nous éviter d'avoir à rendre nos ViewModels un-à-un, tout en gardant nos Vues comme des Objets Humble, simplement en ajoutant quelque chose comme un Présentateur ou un Contrôleur au mélange ?

Les paroles sont bon marché, et je vous conseille vivement d'essayer et d'apprendre ces choses **dans le code** afin de ne pas avoir à dépendre de personnes comme moi pour vous dire quoi faire.

En fin de compte, je pense que les deux éléments qui font une grande architecture se résument aux considérations suivantes :

Tout d'abord, jouez avec plusieurs approches jusqu'à ce que vous en trouviez une que vous **préférez**. Cela se fait mieux en construisant réellement une application (elle peut être simple) dans chaque style, et en voyant ce qui **semble juste**.

Deuxièmement, comprenez que, mis à part les préférences, différents styles tendront à mettre en avant différents avantages en échange de différents défis. Finalement, vous serez en mesure de faire de bons choix en fonction de votre compréhension des exigences du projet plutôt que par **foi aveugle**.

### En savoir plus sur l'architecture logicielle :

%[https://youtu.be/B_C41SF0KbI]

#### Réseaux sociaux

[https://www.instagram.com/rkay301/](https://www.instagram.com/wiseassbrand/)  
[https://www.facebook.com/wiseassblog/](https://www.facebook.com/wiseassblog/)  
[https://twitter.com/wiseass301](https://twitter.com/wiseass301)  
[http://wiseassblog.com/](http://wiseassblog.com/)