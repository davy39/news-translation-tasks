---
title: Comment prendre en charge plusieurs langues dans votre application Flutter
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2024-11-15T17:24:11.882Z'
originalURL: https://freecodecamp.org/news/how-to-support-multiple-languages-in-flutter
coverImage: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/YeO44yVTl20/upload/2ec70e1bfce727903fecba0c2f9b6b8b.jpeg
tags:
- name: Flutter
  slug: flutter
- name: Dart
  slug: dart
- name: localization
  slug: localization
seo_title: Comment prendre en charge plusieurs langues dans votre application Flutter
seo_desc: 'When building my own applications, I usually don’t stress about having
  multiple language support. All of my applications are pet projects of mine and I
  mostly use them to learn and advance my knowledge.

  Without any intention, some of the applications...'
---

Lorsque je développe mes propres applications, je ne m'inquiète généralement pas de la prise en charge de plusieurs langues. Toutes mes applications sont des projets personnels et je les utilise principalement pour apprendre et approfondir mes connaissances.

Sans aucune intention, certaines des applications que j'ai publiées sur le Google Play Store sont utilisées par un nombre considérable de personnes (à ma grande surprise).

Après m'être félicité, j'ai commencé à examiner les données des utilisateurs qui interagissent (ou qui ont simplement téléchargé) avec mon ou mes applications. L'une des informations disponibles dans la console Google Play est le pays d'origine des utilisateurs. J'ai découvert que certaines de mes applications ont un public fidèle dans des pays non anglophones.

![Capture d'écran montrant les pays populaires d'où l'application a été téléchargée](https://cdn.hashnode.com/res/hashnode/image/upload/v1731601377555/a9cc451f-9e8a-4084-b58a-55af1428dd51.jpeg align="center")

Ayant à cœur de faire plaisir, j'ai pensé que la meilleure solution serait d'ajouter la prise en charge des langues parlées dans les 3 ou 4 premiers pays de cette liste. C'est là que j'ai découvert le monde merveilleux de l'[Internationalisation d'une application Flutter](https://docs.flutter.dev/ui/accessibility-and-internationalization/internationalization).

Et cela nous amène au but de cet article : vous aider à comprendre comment ajouter la prise en charge de plusieurs langues dans votre application Flutter.

## Table des matières

* [Comment configurer la localisation dans Flutter](#heading-installation-localisation-flutter)
  
* [Localisations avec des valeurs dynamiques](#heading-localisations-avec-valeurs-dynamiques)
  
* [Tests avec localisation](#heading-tests-avec-localisation)
  
* [Références](#heading-references)
  

## Comment configurer la localisation dans Flutter

Tout d'abord, vous devez inclure deux packages dans votre fichier **pubspec.yaml** :

1. [flutter\_localizations](https://api.flutter.dev/flutter/flutter_localizations/flutter_localizations-library.html)
  
2. [intl](https://pub.dev/packages/intl)
  

```yaml
dependencies:
  flutter:
    sdk: flutter
  flutter_localizations:
    sdk: flutter
  intl: any
```

Après avoir fait cela, rendez-vous en bas de votre fichier **pubspec.yaml** et sous la section `flutter`, assurez-vous d'avoir l'attribut `generate` défini sur `true` :

```yaml
flutter:
  generate: true
```

Pour supporter cela, vous devrez créer un autre fichier **.yaml** appelé **l10.yaml** avec ces configurations :

```yaml
arb-dir: lib/l10n   /// C'est ici que se trouvent nos fichiers de traduction
template-arb-file: app_en.arb       /// Définit le modèle anglais
output-localization-file: app_localizations.dart  /// Fichier de sortie où la commande generate générera les localisations
```

📝 Rendez-vous [ici](https://docs.flutter.dev/ui/accessibility-and-internationalization/internationalization#configuring-the-l10n-yaml-file) pour lire plus d'options de configuration dans le fichier **l10.yaml**

Pour permettre à votre application de supporter plusieurs langues, ajoutez ce qui suit à votre widget `MaterialApp` :

```dart
return const MaterialApp(
  title: 'Mon Application',
  localizationsDelegates: [                    /// De ici
    GlobalMaterialLocalizations.delegate,
    GlobalWidgetsLocalizations.delegate,
    GlobalCupertinoLocalizations.delegate,
  ],
  supportedLocales: [             
    Locale('en'), 
    Locale('hi'),
  ],                                           /// À ici
  home: MainScreen(),
);
```

Ayant défini les langues que nous voulons supporter, nous devons créer les fichiers avec les traductions pour ces langues.

Créez un dossier appelé **l10** sous votre répertoire **lib** :

![Montrant la structure des dossiers de l'application](https://cdn.hashnode.com/res/hashnode/image/upload/v1731601527005/01fd2950-9a09-486b-9f5b-a23595c7f607.jpeg align="center")

À l'intérieur du dossier, vous devez placer des fichiers avec une extension **.arb** qui contiendront des paires clé-valeur de traductions. Par exemple, si votre application doit supporter l'anglais et l'hindi, vous devrez créer deux fichiers :

* **app\_en.arb**
  
* **app\_hi.arb**
  

Le contenu de ces fichiers ressemble à ceci :

```json
{
        "appTitle": "Calendrier des anniversaires",
        "settings": "Paramètres",
        "addBirthday": "Ajouter un anniversaire",
        /...
}
```

```json
{
        "appTitle": "जन्मदिन कैलेंडर",
        "settings": "सेटिंग्स",
        "addBirthday": "जन्मदिन जोड़ें",
        /...
}
```

En gros, vous avez un objet JSON, avec des paires clé-valeur, où les clés sont les mêmes dans tous les fichiers JSON, mais les valeurs sont écrites dans une langue différente.

La commande suivante est utilisée pour générer les fichiers associés au contenu des fichiers **.arb** :

```bash
flutter gen-l10n
```

Dans les fichiers où vous prévoyez d'utiliser des traductions, vous devez ajouter l'importation suivante :

```dart
import 'package:flutter_gen/gen_l10n/app_localizations.dart';
```

Pour accéder à l'une des clés des fichiers **.arb**, vous devez utiliser ce code :

```dart

AppLocalizations.of(context)!.appTitle //Ou un autre nom de clé du fichier .arb
```

✍️ Chaque fois que vous ajoutez plus de paires clé-valeur à vos fichiers **.arb**, vous devrez exécuter la commande dans le terminal pour générer ces traductions. Sinon, vous ne pourrez pas y accéder via le code.

## Localisations avec des valeurs dynamiques

Cela semble simple jusqu'à présent, n'est-ce pas ? Mais que faire si vous avez des endroits dans votre application qui dépendent de données dynamiques et non statiques ? Par exemple, dans l'une de mes applications, j'ai une chaîne qui inclut une erreur et cette erreur peut changer en fonction de l'invocation d'une API.

```dart
AlertDialog alertDialog = AlertDialog(
      title: const Text("Échec de la mise à jour de l'installation ❌"),
      content:
          Text("Le calendrier des anniversaires n'a pas pu être mis à jour car : \n $error"),
      actions: [alertDialogTryAgainButton, alertDialogCancelButton],
    );
```

Pour utiliser des chaînes localisées ici, nous devons créer une paire clé-valeur dans notre fichier **.arb** qui a un espace réservé pour l'erreur :

```dart
"updateFailedToInstallDescription": "Le calendrier des anniversaires n'a pas pu être mis à jour car : {error}"
```

Et nous pouvons l'utiliser en faisant ceci :

```dart
AlertDialog alertDialog = AlertDialog(
      title: Text(AppLocalizations.of(context)!.updateFailedToInstallTitle),
      content:
          Text(AppLocalizations.of(context)!.updateFailedToInstallDescription(error)),  /// <--- ICI
      actions: [alertDialogTryAgainButton, alertDialogCancelButton],
    );
```

## Tests avec localisation

Vous avez ajouté des localisations à votre application, mais vous réalisez maintenant que vos tests unitaires doivent être révisés pour accommoder ce changement. Nous allons diviser cette section en deux types de tests que vous pourriez avoir :

* Tests unitaires
  
* Tests d'intégration
  

Pour l'une de mes applications, j'avais une classe utilitaire qui était associée à une classe de test unitaire. Jusqu'à présent, tout va bien. Lorsque j'ai ajouté la prise en charge de la localisation à cette application, l'une des méthodes utilitaires a changé, car elle devait maintenant retourner une valeur basée sur la localisation. Pour ce faire, j'ai dû passer l'objet `AppLocalizations` comme argument à la méthode. Cet argument dépendait du BuildContext :

```dart
 static String convertAndTranslateMonthNumber(
      int month, AppLocalizations appLocalizations) {
    switch (month) {
      case JANUARY_MONTH_NUMBER:
        return appLocalizations.january;
      case FEBRUARY_MONTH_NUMBER:
        return appLocalizations.february;
      case MARCH_MONTH_NUMBER:
        return appLocalizations.march;
      case APRIL_MONTH_NUMBER:
        return appLocalizations.april;
      case MAY_MONTH_NUMBER:
        return appLocalizations.may;
      case JUNE_MONTH_NUMBER:
        return appLocalizations.june;
      case JULY_MONTH_NUMBER:
        return appLocalizations.july;
      case AUGUST_MONTH_NUMBER:
        return appLocalizations.august;
      case SEPTEMBER_MONTH_NUMBER:
        return appLocalizations.september;
      case OCTOBER_MONTH_NUMBER:
        return appLocalizations.october;
      case NOVEMBER_MONTH_NUMBER:
        return appLocalizations.november;
      case DECEMBER_MONTH_NUMBER:
        return appLocalizations.december;
      default:
        return "";
    }
  }
```

Cela n'a pas bien fonctionné dans ma classe de test unitaire correspondante, car j'ai dû créer un `BuildContext`. Comme le faire dans une classe de test unitaire est problématique, il existe une autre façon d'obtenir l'objet `AppLocalizations` sans avoir à dépendre d'un `BuildContext`.

```dart
final appLocalizations = lookupAppLocalizations(const Locale('en'))
```

De cette façon, nous indiquons la locale que nous voulons et nous pouvons l'utiliser dans n'importe lequel de nos tests. Mon test unitaire ressemble à ceci après la révision :

```dart
test("DateService convertir le numéro du mois 8 en août", () {
    final int monthNumber = 8;
    final String monthName =
        BirthdayCalendarDateUtils.convertAndTranslateMonthNumber(
            monthNumber, appLocalizations);
    expect(monthName, "August");
  });
```

En ce qui concerne les tests d'intégration, vous devrez envelopper votre widget dans un widget [Localizations](https://api.flutter.dev/flutter/widgets/Localizations/Localizations.html).

```dart
testWidgets("Description de votre test",
      (WidgetTester tester) async {
    await tester.pumpWidget(
        Localizations(
          delegates: [
            //délégations de localisation
          ],
          locale: Locale('en'),
          child: Widget(),
        );
    );
    //Votre logique ici
  });
```

Pour voir comment tout cela est implémenté dans une application, vous pouvez aller [ici](https://github.com/TomerPacific/BirthdayCalendar).

Et si vous voulez télécharger l'application, vous pouvez vous rendre [ici](https://play.google.com/store/apps/details?id=com.tomerpacific.birthday_calendar).

Si vous souhaitez lire d'autres articles que j'ai écrits, vous pouvez les trouver [ici](https://github.com/TomerPacific/MediumArticles).

## Références

* [Documentation officielle de Flutter](https://docs.flutter.dev/ui/accessibility-and-internationalization/internationalization)