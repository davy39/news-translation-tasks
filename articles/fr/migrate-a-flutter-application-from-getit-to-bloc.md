---
title: Comment migrer une application Flutter de GetIt à Bloc
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2024-07-19T23:05:13.000Z'
originalURL: https://freecodecamp.org/news/migrate-a-flutter-application-from-getit-to-bloc
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/ryan-quintal-US9Tc9pKNBU-unsplash.jpg
tags:
- name: Flutter
  slug: flutter
- name: mobile app development
  slug: mobile-app-development
seo_title: Comment migrer une application Flutter de GetIt à Bloc
seo_desc: When I first built an application using Flutter, I quickly ran into situations
  where I needed to pass state from widget to widget. These widgets weren’t directly
  related and all I knew back then was that there were only Stateless widgets or Stateful
  ...
---

Lorsque j'ai construit pour la première fois une [application](https://play.google.com/store/apps/details?id=com.tomerpacific.birthday_calendar&hl=en) en utilisant Flutter, j'ai rapidement été confronté à des situations où je devais passer l'état d'un widget à un autre. Ces widgets n'étaient pas directement liés et tout ce que je savais à l'époque, c'est qu'il n'y avait que des widgets Stateless ou Stateful.

J'ai trouvé difficile de comprendre comment je pouvais faire en sorte qu'un widget complètement sans relation sache ce qui se passe dans un autre widget à l'intérieur de mon application. 

Prenons, par exemple, une fonctionnalité que je voulais implémenter qui permettrait à l'utilisateur de choisir le thème de l'application (clair/sombre). Comme j'avais un écran de paramètres avec cette fonctionnalité, je me demandais comment je pouvais faire savoir au reste de l'application que le thème avait changé et réagir en conséquence.

En cherchant des conseils en ligne, j'ai remarqué qu'il ne manquait pas de solutions proposées. Chacune avec son propre degré de complexité. **Bloc** était un choix populaire que beaucoup de gens en ligne suggéraient, mais dans le même souffle, il était dit que la courbe d'apprentissage est assez raide. Voulant livrer des fonctionnalités à l'application plus rapidement, j'ai choisi d'utiliser [GetIt](https://pub.dev/packages/get_it).

Pourquoi ai-je choisi GetIt ? Je pense que le ou les créateurs du package le résument assez bien [dans leurs propres mots](https://pub.dev/packages/get_it#why-getit) :

> _GetIt est :_  
> _- Extrêmement rapide (O(1))_  
> _- Facile à apprendre/utiliser_  
> _- N'encombre pas votre arbre UI avec des Widgets spéciaux pour accéder à vos données comme le font Provider ou Redux._

Il est mentionné que GetIt n'est pas une solution de gestion d'état, mais plutôt un outil pour vous aider à accéder aux objets à l'intérieur de votre application.

J'ai donc décidé d'utiliser GetIt en combinaison avec Provider et ChangeNotifier dans mon application. Bien que ce ne soit pas joli, cela a fait le travail.

Pendant le développement des fonctionnalités de mon application et en la rendant plus robuste, je savais au fond de moi que je n'utilisais pas les bons outils pour gérer correctement l'état dans mon application.

Récemment, j'ai décidé qu'il était temps d'apprendre correctement Bloc et de convertir le code à l'intérieur de mon application pour l'utiliser. Je savais que ce ne serait pas une tâche facile, mais après l'avoir fait, je peux admettre qu'après quelques essais et erreurs, cela est devenu plus facile à gérer. À chaque cas d'utilisation que j'ai rencontré, ma compréhension a grandi.

Dans cet article, je vais présenter quelques cas d'utilisation réels où j'ai utilisé GetIt en combinaison avec Provider et ChangeNotifier et les ai remplacés par Bloc. Espérons que vous pourrez utiliser ces exemples pour mieux comprendre comment utiliser Bloc dans vos applications.

## Gestion du thème sombre/clair

Je voulais que mon application supporte différents thèmes. Pour ce faire, j'ai créé un écran de paramètres où l'utilisateur pouvait contrôler la couleur du thème.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/1-1.jpg)
_Écran des paramètres_

Développer cela a été la première fois où j'ai dû gérer des changements dans l'état de l'application qui seraient reflétés dans des widgets qui n'étaient pas directement liés. Donc, en plus de créer un widget pour l'écran des paramètres,

```dart
class SettingsScreen extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    return Scaffold(
              appBar: AppBar(
                title: new Text("Paramètres"),
              ),
              body:
                  Column(
                      mainAxisAlignment: MainAxisAlignment.start,
                      children: [
                        Consumer<SettingsScreenManager>(
                            builder: (context, notifier, child) {
                              return  SwitchListTile(
                                  title: const Text('Mode sombre'),
                                  value: notifier.themeMode == ThemeMode.light ? false : true,
                                  secondary:
                                  new Icon(
                                      Icons.dark_mode,
                                      color: notifier.themeMode == ThemeMode.light ? Color(0xFF642ef3) : Color.fromARGB(200, 243, 231, 106)
                                  ),
                                  onChanged:notifier.handleThemeModeSettingChange
                              );
                            }
                        ),
                        //.....
                      ],
                    ),
                  )
      );
  }
```

J'ai également créé une classe de gestion pour cela appelée SettingsScreenManager, où j'avais cette méthode :

```dart
 void handleThemeModeSettingChange(bool isDarkModeEnabled) {
    _themeMode = _themeMode == ThemeMode.dark ? ThemeMode.light : ThemeMode.dark;
    _storageService.saveThemeModeSetting(isDarkModeEnabled);
    notifyListeners();
  }
```

La connexion entre l'écran et son gestionnaire se fait lorsque le widget est créé, car c'est là que je crée la classe de gestion. Ensuite, tout au long du widget lui-même, j'appelle des méthodes sur la classe de gestion. Pour faire en sorte que le widget se redessine lui-même, j'ai utilisé le widget Consumer.

Ce n'est pas la meilleure approche, et pour rectifier la situation, j'ai créé un Bloc pour gérer le mode de thème :

```dart
import 'package:birthday_calendar/service/storage_service/storage_service.dart';
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

enum ThemeEvent { toggleDark, toggleLight }

class ThemeBloc extends Bloc<ThemeEvent, ThemeMode> {
  ThemeBloc(StorageService storageService, bool isDarkMode) : super(isDarkMode ? ThemeMode.dark : ThemeMode.light) {
    on<ThemeEvent>((event, emit) {
      ThemeMode themeMode = event == ThemeEvent.toggleDark ? ThemeMode.dark : ThemeMode.light;
      emit(themeMode);
      storageService.saveThemeModeSetting(themeMode == ThemeMode.dark ? true : false);
    });
  }
}
```

Décomposons les composants de ce Bloc :

1. J'ai déclaré une énumération appelée **ThemeEvent** pour signifier le choix de l'utilisateur de thème clair/sombre
2. Puisque l'état du Bloc est directement l'objet **ThemeMode**, il n'était pas nécessaire de créer un objet State spécifique
3. Chaque fois que le thème change, j'émet le mode de thème choisi

Et j'ai initialisé ce bloc à l'intérieur de mon fichier **main.dart** afin qu'il soit accessible à n'importe quel widget dans la hiérarchie des widgets. De plus, je voulais que tout changement qui se produisait en raison de ce Bloc soit appliqué à l'ensemble de l'application.

```dart
 @override
  Widget build(BuildContext context) {
    return MultiBlocProvider(
      providers: [
        BlocProvider(create: (context) => ThemeBloc(storageService, isDarkMode)),
        //...
      ],
      child: BlocBuilder<ThemeBloc, ThemeMode>(
        builder: (context, state) {
          return MaterialApp(
              title: applicationName,
              theme: ThemeData.light(),
              themeMode: state,
              darkTheme: ThemeData.dark(),
              home: MainPage(
                  key: Key("BirthdayCalendar"),
                  notificationService: notificationService,
                  contactsService: contactsService,
                  storageService: storageService,
                  title: applicationName,
                  currentMonth: BirthdayCalendarDateUtils.getCurrentMonthNumber()));
        },
      ),
    );
  }
```

## Demande de permission

Il y a une fonctionnalité dans mon application qui permet aux utilisateurs d'importer leurs contacts. Pour ce faire, il est nécessaire de demander d'abord une permission d'exécution. 

Initialement, j'ai géré cela en utilisant la même approche que dans la section précédente, en utilisant la classe SettingsScreenManager, un Consumer et un Provider.

```dart
Consumer<SettingsScreenManager>(
   builder: (context, notifier, child) {
    return ListTile(
      title: const Text("Importer les contacts"),
      leading: Icon(Icons.contacts,
          color: !notifier.isContactsPermissionPermanentlyDenied ? Colors.blue : Colors.grey
      ),
      onTap: () {
        Provider.of<SettingsScreenManager>(context, listen: false).handleImportingContacts(context);
      },
      enabled: !notifier.isContactsPermissionPermanentlyDenied
  );
}),
```

Remplacer cela a été une étape au-dessus de la création du ThemeBloc puisque je devais gérer les différents statuts de permission et aussi me souvenir si la permission était définitivement refusée.

```dart
enum ContactsPermissionStatusEvent {
  PermissionUnknown,
  PermissionDenied,
  PermissionGranted,
  PermissionPermanentlyDenied
}

class ContactsPermissionStatusBloc
    extends Bloc<ContactsPermissionStatusEvent, PermissionStatus> {
  ContactsPermissionStatusBloc(ContactsService contactsService)
      : super(PermissionStatus.denied) {
    on<ContactsPermissionStatusEvent>((event, emit) async {
      if (event == ContactsPermissionStatusEvent.PermissionUnknown) {
        bool permissionStatus =
            await contactsService.isContactsPermissionsPermanentlyDenied();
        if (permissionStatus) {
          emit(PermissionStatus.permanentlyDenied);
          return;
        }
      }
      emit(_convertEventNameToPermissionStatus(event));
    });
  }

  PermissionStatus _convertEventNameToPermissionStatus(
      ContactsPermissionStatusEvent event) {
    switch (event) {
      case ContactsPermissionStatusEvent.PermissionDenied:
        return PermissionStatus.denied;
      case ContactsPermissionStatusEvent.PermissionGranted:
        return PermissionStatus.granted;
      case ContactsPermissionStatusEvent.PermissionPermanentlyDenied:
        return PermissionStatus.permanentlyDenied;
      default:
        return PermissionStatus.denied;
    }
  }
}
```

Ce Bloc a les éléments suivants :

* Une énumération **ContactsPermissionStatusEvent** qui correspond aux différents statuts de permission que le système d'exploitation a
* L'état de ce Bloc peut être facilement représenté avec la classe **PermissionStatus**
* J'ai une méthode d'assistance privée appelée **_convertEventNameToPermissionStatus** pour aider à convertir le nom de l'événement en son statut de permission correspondant

Vous vous demandez peut-être pourquoi j'ai ajouté un événement appelé **PermissionUnknown**. Je l'ai fait pour pouvoir obtenir le statut de permission à l'avance avant que l'utilisateur ne navigue vers le SettingsScreen. Dans le cas où l'utilisateur a précédemment choisi de refuser définitivement la permission, je voulais griser l'option d'importer les contacts pour eux. 

Pour y parvenir, j'ai créé le Bloc dans le fichier main.dart :

```dart
@override
  Widget build(BuildContext context) {
    return MultiBlocProvider(
      providers: [
        BlocProvider(create: (context) => ThemeBloc(storageService, isDarkMode)),
        BlocProvider(
            create: (context) => ContactsPermissionStatusBloc(contactsService)),
        BlocProvider(create: (context) => VersionBloc())
      ],
      child: BlocBuilder<ThemeBloc, ThemeMode>(
        builder: (context, state) {
          return MaterialApp(
```

et j'ai envoyé l'événement à l'intérieur de la méthode initState du widget qui est le parent du SettingsScreen.

```dart
 @override
  void initState() {
    //....
    BlocProvider.of<ContactsPermissionStatusBloc>(context)
        .add(ContactsPermissionStatusEvent.PermissionUnknown);
    super.initState();
  }
```

Et au lieu du gros morceau de code que j'avais auparavant, j'ai maintenant ceci :

```dart
BlocBuilder<ContactsPermissionStatusBloc, PermissionStatus>(
              builder: (context, state) {
            return ListTile(
                title: const Text("Importer les contacts"),
                leading: Icon(Icons.contacts, color: Colors.blue),
                onTap: () {
                  _handleImportingContacts(context);
                },
                enabled: state.isPermanentlyDenied ? false : true);
          }),
```

## Interaction avec une liste

Une partie de mon application permet aux utilisateurs d'ajouter/supprimer des anniversaires à des dates spécifiques du calendrier. Comme pour les fonctionnalités précédentes, j'ai également créé une classe de gestion pour gérer l'état si un utilisateur ajoutait/supprimait un anniversaire. 

Une partie de la logique impliquait la présentation d'une boîte de dialogue d'alerte avec des champs pour ajouter un anniversaire. Cette logique s'est avérée être la plus robuste lors de la migration vers Bloc, car j'ai dû penser à tous les flux utilisateur.

Voici à quoi ressemblait ce widget :

```dart
@override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (context) => BirthdaysForCalendarDayManager(this.birthdays, this.dateOfDay),
          builder: (context, provider) {
              return Scaffold(
              appBar: AppBar(
              title: FittedBox(
                  fit: BoxFit.fitWidth,
                  child: Text(
                      "Anniversaires pour ${_dateService.convertMonthToWord(this.dateOfDay.month)} ${this.dateOfDay.day}")
              )
          ),
            body: Center(
                child: Column(
                  children: [
                      Consumer<BirthdaysForCalendarDayManager>(
                          builder: (context, data, child) =>
                          Expanded(child:
                            ListView.builder(
                                  itemCount: data.birthdays.length,
                                  itemBuilder: (BuildContext context, int index) {
                                  return BirthdayWidget(
                                    key: Key(data.birthdays[index].name),
                                      birthdayOfPerson: data.birthdays[index],
                                      onDeletePressedCallback: () {
                                        Provider.of<BirthdaysForCalendarDayManager>(context, listen: false).removeBirthdayFromList(data.birthdays[index]);
                                    },
                                    indexOfBirthday: index);
                                  },
                                 ),
                           ),
                          )
                      ],
                   )
                ),
                floatingActionButton: FloatingActionButton(
                onPressed: () {
                  Provider.of<BirthdaysForCalendarDayManager>(context, listen: false).handleAddBirthdayBtnPressed(context, dateOfDay);
                  },
                child: Icon(Icons.add)),
              );
          },
    );
  }
```

Et la classe de gestion :

```dart
class BirthdaysForCalendarDayManager extends ChangeNotifier {

  NotificationService _notificationService = getIt<NotificationService>();
  StorageService _storageService = getIt<StorageService>();
  final List<UserBirthday> _currentBirthdays = [];
  DateTime date = DateTime.now();

  UnmodifiableListView<UserBirthday> get birthdays => UnmodifiableListView(_currentBirthdays);

  BirthdaysForCalendarDayManager(List<UserBirthday> birthdays, DateTime dateTime) {
    //....
  }

  void _handleUserInput(UserBirthday userBirthday) {
    //....
  }

  void _addBirthdayToList(UserBirthday userBirthday) {
    //....
    notifyListeners();
  }

  void removeBirthdayFromList(UserBirthday birthdayToRemove) async {
    //....
    notifyListeners();
  }

  void handleAddBirthdayBtnPressed(BuildContext context, DateTime dateOfDay) async {
    //....
  }
```

Alors, comment pouvons-nous migrer toute cette logique vers Bloc ? Eh bien, pensons d'abord aux différents événements dont nous aurons besoin :

1. Ajouter un élément à la liste
2. Supprimer un élément de la liste
3. Présenter la boîte de dialogue qui permet aux utilisateurs d'ajouter un élément à la liste (cela est utilisé pour pouvoir afficher la boîte de dialogue)

Ainsi, notre énumération interne pour les événements peut ressembler à ceci :

```dart
enum BirthdayEvent { AddBirthday, RemoveBirthday, ShowAddBirthdayDialog }

```

Mais que contiendra notre BirthdaysEvent ?

```dart
class BirthdaysEvent {
  final BirthdayEvent eventName;  // 1
  final UserBirthday? birthday;   // 2
  final bool? shouldShowAddBirthdayDialog; // 3
  final List<UserBirthday> birthdays; // 4
  final DateTime? date;  //5

  BirthdaysEvent(
      {required this.eventName,
      this.birthday,
      this.shouldShowAddBirthdayDialog,
      required this.birthdays,
      this.date});
}
```

1. Le nom de l'événement
2. L'anniversaire que nous allons soit ajouter soit supprimer
3. Un indicateur pour indiquer si nous devons présenter la boîte de dialogue
4. La liste complète des anniversaires pour la date spécifique
5. La date à laquelle l'utilisateur souhaite ajouter/supprimer des anniversaires

Vous avez peut-être remarqué que tous les champs ne sont pas nécessaires pour créer un **BirthdaysEvent**. Cela est dû au fait que tous ces champs ne sont pas nécessaires pour les différents types d'événements. Par exemple, lorsque l'utilisateur souhaite ajouter un autre anniversaire, le deuxième argument (intitulé birthday) est sans importance puisque nous voulons créer un anniversaire.

Ensuite, nous devons réfléchir à ce qui doit être inclus dans notre état. En regardant le code ci-dessus, il est clair que nous avons besoin de :

* Conserver la liste des anniversaires, car nous en supprimons ou en ajoutons
* Un indicateur pour indiquer si nous devons afficher la boîte de dialogue d'ajout d'anniversaire
* La date actuelle pour ajouter/supprimer des anniversaires

```dart
class BirthdaysState {
  final DateTime? date;
  final List<UserBirthday>? birthdays;
  final bool showAddBirthdayDialog;

  BirthdaysState(
      {this.date, this.birthdays, required this.showAddBirthdayDialog});
}
```

Nous avons donc nos événements en place et notre état également. Il est maintenant temps d'implémenter la logique dans notre bloc qui gère chacun de ces événements et crée un nouvel état :

```dart
class BirthdaysBloc extends Bloc<BirthdaysEvent, BirthdaysState> {
  BirthdaysBloc(NotificationService notificationService,
      StorageService storageService, List<UserBirthday> birthdaysForDate)
      : super(BirthdaysState(
            date: DateTime.now(),
            birthdays: birthdaysForDate,
            showAddBirthdayDialog: false)) {
    on<BirthdaysEvent>((event, emit) {
      switch (event.eventName) {
        case BirthdayEvent.AddBirthday:
          _handleAddEvent(event, emit, storageService, notificationService);
          break;
        case BirthdayEvent.RemoveBirthday:
          _handleRemoveEvent(event, emit, storageService, notificationService);
          break;
        case BirthdayEvent.ShowAddBirthdayDialog:
          emit(new BirthdaysState(showAddBirthdayDialog: true));
          break;
      }
    });
  }
```

Si nous regardons un événement, **ShowAddBirthdayDialog**, vous pouvez voir que nous émettons simplement un nouvel état BirthdayState où **showAddBirthdayDialog** est défini sur vrai. Mais où est-ce géré ? J'ai dû refactoriser fortement le widget ci-dessus pour qu'il réponde aux changements d'état.

```dart
  @override
  Widget build(BuildContext context) {
   return BlocProvider(                            // 1
        create: (context) =>
            BirthdaysBloc(notificationService, storageService, birthdays),
        child: BlocBuilder<BirthdaysBloc, BirthdaysState>(   // 2
            builder: (context, state) {
          return Scaffold(
            appBar: AppBar(
                title: FittedBox(
                    fit: BoxFit.fitWidth,
                    child: Text(
                        "Anniversaires pour ${BirthdayCalendarDateUtils.convertMonthToWord(this.dateOfDay.month)} ${this.dateOfDay.day}"))),
            body: Center(
                child: Column(
              children: [
                (state.birthdays == null || state.birthdays!.length == 0)
                    ? Spacer()
                    : Expanded(
                        child: ListView.builder(
                          itemCount: state.birthdays != null
                              ? state.birthdays!.length
                              : 0,
                          itemBuilder: (BuildContext context, int index) {
                            return BirthdayWidget(
                                key: Key(state.birthdays![index].name),
                                birthdayOfPerson: state.birthdays![index],
                                onDeletePressedCallback: () {  // 3
                                  BlocProvider.of<BirthdaysBloc>(context).add(
                                      new BirthdaysEvent(
                                          eventName:
                                              BirthdayEvent.RemoveBirthday,
                                          birthday: state.birthdays![index],
                                          birthdays: birthdays));
                                },
                                indexOfBirthday: index,
                                storageService: storageService,
                                notificationService: notificationService);
                          },
                        ),
                      ),
                BlocListener<BirthdaysBloc, BirthdaysState>(  // 4
                  listener: (context, state) {
                    if (state.showAddBirthdayDialog) {
                      showDialog(
                          context: context,
                          builder: (_) => BlocProvider.value(  // 5
                              value: BlocProvider.of<BirthdaysBloc>(context),
                              child: AddBirthdayForm(
                                  dateOfDay: dateOfDay,
                                  storageService: storageService)));
                    }
                  },
                  child: Spacer(),
                )
              ],
            )),
            floatingActionButton: FloatingActionButton(
                onPressed: () { // 6
                  BlocProvider.of<BirthdaysBloc>(context).add(BirthdaysEvent(
                      eventName: BirthdayEvent.ShowAddBirthdayDialog,
                      shouldShowAddBirthdayDialog: true,
                      birthdays: birthdays));
                },
                child: Icon(Icons.add)),
          );
        }));
  }
```

Il y a beaucoup à déballer ici, alors prenons cela une étape à la fois.

1. Le BirthdaysBloc est créé à l'intérieur de ce widget puisqu'il n'est pas nécessaire ailleurs dans l'arborescence des widgets
2. Nous utilisons un BlocBuilder pour que le widget se redessine lui-même lorsque l'état change
3. Lorsqu'un anniversaire est choisi pour être supprimé, nous créons un événement RemoveBirthday et transmettons toutes les informations nécessaires
4. Nous utilisons un BlocListener pour gérer les changements d'état afin d'afficher l'AlertDialog pour ajouter un nouvel anniversaire
5. Puisque notre BirthdaysBloc n'est pas trouvé au niveau global, il est nécessaire de le transmettre au widget **AddBirthdayForm** en utilisant BlocProvider
6. Lorsque l'utilisateur appuie sur le bouton d'action flottant pour signifier une intention d'ajouter un anniversaire, nous créons un événement ShowAddBirthdayDialog

Remarquez que, après tous ces changements, la classe de gestion n'était plus nécessaire et donc, le code lui-même est plus direct et plus facile à maintenir.

Vous êtes plus que bienvenu pour consulter l'intégralité du code montré ci-dessus dans le dépôt GitHub ici :

%[https://github.com/TomerPacific/BirthdayCalendar]

Et si vous le souhaitez, vous pouvez consulter l'application elle-même, [ici](https://play.google.com/store/apps/details?id=com.tomerpacific.birthday_calendar).