---
title: Développement piloté par les tests dans les applications Android – Un guide
  pratique du TDD
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-09-06T06:34:34.000Z'
originalURL: https://freecodecamp.org/news/tdd-in-android-apps
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/TDD--1-.jpg
tags:
- name: Android
  slug: android
- name: TDD (Test-driven development)
  slug: tdd
seo_title: Développement piloté par les tests dans les applications Android – Un guide
  pratique du TDD
seo_desc: "By Siamak Mahmoudi\nTDD, or Test-Driven Development, is a software development\
  \ approach where tests are written before the actual code is implemented. \nIt requires\
  \ a clear understanding of \"What\" and \"How\" in the the requirements of the project/featur..."
---

Par Siamak Mahmoudi

Le TDD, ou Développement Piloté par les Tests, est une approche de développement logiciel où les tests sont écrits avant que le code réel ne soit implémenté. 

Il nécessite une compréhension claire du "Quoi" et du "Comment" dans les exigences du projet/fonctionnalité. 

Le TDD aide à écrire moins de code, mais suffisamment. Il aide à prévenir les erreurs courantes de développement logiciel, telles que le surdimensionnement, une couverture de test excessive, des exigences principales manquantes, des fonctions et des classes trop grandes, et des instructions de code trop compliquées. 

Globalement, il aide à avoir une base de code concise, déjà couverte par des tests unitaires, et [propre](https://www.freecodecamp.org/news/how-to-write-clean-code/). Avec le temps, cela permet également d'économiser les coûts de développement et de maintenance du code.

Dans cet article, nous allons discuter du TDD en action. 

Le contexte est un environnement de développement Android, nous utiliserons donc Kotlin et JUnit5 avec un projet exemple pour démontrer les étapes. 

Cependant, les instructions et techniques présentées ici peuvent être pratiquées dans d'autres langages de programmation également.

## Prérequis

* Connaissance de base de [Kotlin](https://www.freecodecamp.org/news/learn-kotlin-complete-course/)
* Connaissance de base de l'écriture de tests unitaires
* Connaissance des mocks et des assertions

Nous utiliserons Kotlin comme langage de programmation et [JUnit5](https://junit.org/junit5/) pour écrire des tests unitaires.

[Mockito](https://site.mockito.org/) sera utilisé pour travailler avec des mocks et des [spys](https://www.danywalls.com/how-and-when-to-use-mocks-or-spies-on-unit-testing).

Le public cible est tout développeur logiciel de n'importe quelle plateforme cherchant un nouveau chapitre dans sa carrière. 

Bien que le contexte soit Android, le contenu ne parle pas des propriétés spécifiques à la plateforme. Au lieu de cela, nous nous concentrons sur les techniques, les notes et les défis lors du développement avec le TDD.

Si cela vous convient, commençons.

## Comment fonctionne le Développement Piloté par les Tests

![Image](https://www.freecodecamp.org/news/content/images/2023/08/image-232.png)
_Cycle TDD_

Le processus de développement suit un cycle de :

1. Écrire un test qui échoue (carré rose).
2. Implémenter le code pour faire passer le test (carré vert)
3. Refactoriser le code (carré bleu) si nécessaire tout en s'assurant que les tests continuent de passer (carré vert pâle).
4. Écrire un nouveau test qui échoue (redémarrer le flux)

### Écrire un Test qui Échoue (Carré Rose)

Dans cette étape, vous commencez par décrire ce que vous voulez que votre code fasse. 

Imaginez que vous donnez à votre code un test pour vérifier s'il se comporte correctement. Ce test est comme une question que vous posez à votre code, telle que "Pouvez-vous faire cette tâche ?". 

Au début, votre code ne connaît pas la réponse, vous écrivez donc un test qui devrait échouer parce que votre code ne sait pas encore comment faire la tâche. Ce test qui échoue est comme un panneau d'avertissement rose qui vous indique que quelque chose ne va pas.

Une fois que vous avez terminé cette étape, JUnit5 générera un rapport complet à partir des tests que vous avez créés. Ces tests seront une représentation tangible de votre travail. 

Maintenant, imaginez que votre chef de projet lit ces cas de test pour évaluer à la fois leur couverture et la précision de votre compréhension de la fonctionnalité ou du produit. Adopter cette perspective offre une compréhension plus claire de l'importance de cette phase de développement.

Changez votre focus des intrications techniques au comportement du logiciel lui-même. 

Au lieu de vous perdre dans les détails techniques, concentrez-vous sur la manière dont le logiciel fonctionne et interagit avec les utilisateurs et les autres composants. 

Ce changement de perspective vous permet de prioriser les actions et les résultats prévus du logiciel, conduisant à des tests qui reflètent précisément son comportement dans le monde réel. 

En vous concentrant sur le comportement plutôt que sur les détails techniques, vous vous assurez que vos tests sont étroitement alignés avec le but du logiciel et les attentes des utilisateurs. 

Dans certains cas, vous pourriez vous retrouver avec seulement quelques cas de test par composant (ce qui est le but : moins de travail mais ciblé) et c'est tout à fait correct, tant que vous couvrez toutes les exigences comportementales du projet.

#### Conseils

* Soyez spécifique : Écrivez des cas de test clairs et spécifiques qui se concentrent sur un aspect du comportement de votre code.
* Commencez simplement : Commencez par le cas de test le plus simple qui couvre la fonctionnalité de base dont vous avez besoin.

```kotlin
@Test fun `une somme est calculée à partir de deux nombres d'entrée`() {}
```

* Utilisez des noms significatifs : Nommez vos tests de manière descriptive afin que quiconque les lise sache ce que le test vérifie.

```kotlin
@Test fun `Le ratio de police est récupéré depuis la source de données INITIALEMENT`() {}
```

#### Erreurs courantes à éviter

* Tester trop de choses à la fois : Évitez de tester plusieurs choses dans un seul test. Cela peut rendre difficile l'identification de ce qui échoue.

```kotlin
// Ne faites pas cela
@Test fun `pixelSize correspond aux tailles standard tandis que fontSize est plus grand que la taille de police minimale supportée mais correspond à la liste des niveaux spéciaux de taille`() {}
```

* Se fier aux détails d'implémentation : N'écrivez pas de tests qui sont étroitement couplés au fonctionnement interne du code. Les tests doivent se concentrer sur le comportement, pas sur l'implémentation.

```kotlin
// Ne faites pas cela
@Test fun `pixelSize est Long et Non-Null et correspond aux tailles standard alors la taille de police calculée est non-null et de type Dimention`() {}
```

### Implémenter le Code pour Faire Passer le Test (Carré Vert)

Maintenant que vous avez votre test en place, il est temps d'apprendre à votre code à faire la tâche correctement. 

Vous écrivez le code réel qui devrait faire passer le test et votre code répondre à la question correctement. 

Lorsque votre code passe le test, c'est comme un feu vert qui dit : "Oui, je peux faire la tâche maintenant !". 

Cette étape consiste à s'assurer que votre code comprend et peut résoudre le problème que vous lui posez.

### Conseils

* Écrivez un code minimal : Écrivez le code le plus simple qui fait passer le test qui échoue. Vous pouvez lire plus sur la façon d'éviter le surdimensionnement [ici](https://www.rst.software/blog/how-to-avoid-over-engineering). 

```kotlin
// Cas de test 
@Test fun `Storage stocke le ratio de police en clé-valeur`() { 
    
    // Given
    val fontRatio = 2.0f
    val mockEditor = mockk<SharedPreferences.Editor>(relaxed = true)
    every { mockSharedPreference.edit() } returns mockEditor 
    every { mockEditor.putFloat(any(), any()) } returns mockEditor 
    every { mockEditor.apply() } just Runs 

	// When 
    storage.saveFontRatio(fontRatio) 
    
    // Then
    verify(exactly = 1) { 
    	mockEditor.apply() 
    }
}


// Implémentation correcte - Évitez l'implémentation supplémentaire
class SharedPreferenceHelper( 
	private val sharedPreferences: SharedPreferences 
) { 
    fun saveFontRatio(fontRatio: Float) {
    	sharedPreferences.edit().putFloat("font-ratio", fontRatio).apply() 
    } 
}


// Mauvaise implémentation 
class SharedPreferenceHelper(
	private val sharedPreferences: SharedPreferences
) { 
    fun saveFontRatio(fontRatio: Float) { 
    if (fontRatio <= 0.0f) 
    throw IllegalArgumentException("Le ratio de police doit être supérieur à 0.0f") 

	storeValue(key = FONT_RATIO_KEY, value = fontRatio) 

} 

    private fun storeValue(key: String, value: Float){
        val editor = sharedPreferences.edit() editor.putFloat(key, value)
        editor.apply() 
    }

    fun getFontRatio(): Float { 
    return sharedPreferences.getFloat("font_ratio", 1.0f) } 
} 


```

* Évitez la duplication : Ne répétez pas le code. Si vous vous retrouvez à écrire une logique similaire à plusieurs endroits, envisagez de refactoriser. Ces améliorations primaires du code peuvent être faites dans cette phase, mais si la modification peut avoir un effet secondaire, ignorez-la.

```kotlin
class ... {
    override fun getDefaultFontSize(): Float {
        val zoomRatio = DEFAULT_SSPEED * DEFAULT_FONT_RATIO / deviceDensity 
        val fontSize = zoomRatio * standardFontSize 
        return fontSize 
    }
    override fun getFontSizeBySSpeed(speed: Int): Float {
        val zoomRatio = speed * DEFAULT_FONT_RATIO / deviceDensity 
        val fontSize = zoomRatio * standardFontSize 
        return fontSize 
    }
}
```

```kotlin
class ... { 
    override fun getDefaultFontSize(): Float = calculate(DEFAULT_AGE)
    override fun getFontSizeByAge(age: Int): Float = calculate(age) 
    
    private fun calculate(age: Int): Float {
        val zoomRatio = age * DEFAULT_FONT_RATIO / deviceDensity 
        val fontSize = zoomRatio * standardFontSize 
        return fontSize 
    }
}
```

#### Erreurs courantes à éviter :

* Sauter en avant : N'écrivez pas plus de code que nécessaire pour faire passer le test. Le TDD est un développement incrémental. Le TDD encourage une approche incrémentale et étape par étape du développement. Lorsque vous sautez en avant, vous essayez essentiellement de résoudre des problèmes qui ne sont pas encore directement liés au test actuel sur lequel vous travaillez. L'objectif principal est de se concentrer sur la tâche immédiate à accomplir – faire passer le test actuel – sans se laisser distraire par les fonctionnalités futures.
* Ignorer les échecs de test : Si un test ne échoue pas initialement, vous pourriez manquer un cas important. Cela peut sembler peu probable de se produire à première vue, mais après un certain développement dans vos composants de test, vous commencerez à écrire plusieurs tests pour une seule méthode afin de tester différents aspects de la logique. C'est là que vous ne devriez pas être content si votre logique non implémentée passe le test. En termes simples, c'est ainsi que vous attrapez les bugs en phase de développement. Donc, attendez-vous à l'échec lorsqu'il devrait se produire.

### Refactoriser le Code (Carré Bleu) et S'assurer du Succès du Test (Carré Vert Pâle)

Une fois que votre code passe le test, il est temps de nettoyer les choses. 

Vous pourriez voir des moyens de rendre votre code plus organisé, plus facile à comprendre, ou même plus rapide. Pensez à cela comme à ranger votre chambre une fois que vous avez fini de jouer, en rendant tout propre et organisé après avoir fini de jouer. Vous améliorez votre code sans changer ce qu'il fait. 

Alors que vous faites cela, vous continuez à exécuter tous vos tests pour vous assurer qu'ils passent toujours. Si un test échoue pendant cette étape, c'est comme un panneau d'avertissement vert pâle qui vous indique que quelque chose que vous avez nettoyé pourrait avoir accidentellement cassé le code.

Vous pouvez traiter cette partie comme une phase de maintenance de code séparée. 

Supposez que vous avez la tâche de nettoyer un ancien code et de vous assurer qu'il suit les directives de qualité de code de l'équipe ainsi que les exigences du produit. 

Tout au long de ce processus, la clé est de maintenir un équilibre attentif – affiner tout en s'assurant que vos tests continuent de réussir.

Voici quelques idées et stratégies pour la phase de refactorisation :

* Clarté du code : Simplifiez les sections complexes, remplacez les noms de variables peu clairs et améliorez les commentaires pour rendre le code plus facile à comprendre pour les autres (et pour vous-même à l'avenir).
* Modularité : Décomposez les grandes fonctions en fonctions plus petites et ciblées. Cela rend votre code plus modulaire et permet une maintenance et des tests plus faciles.
* Supprimez la redondance : Identifiez le code dupliqué et consolidez-le en fonctions ou classes réutilisables. Cela aide à éliminer la répétition et assure la cohérence.
* Optimisation : Identifiez les zones où les performances peuvent être améliorées. Cependant, optimisez uniquement si vous avez des objectifs de performance spécifiques et des preuves que le code est un goulot d'étranglement. L'optimisation ici est d'éviter le drainage des ressources et non de rendre le code performant.
* Formatage cohérent : Maintenez un style de code cohérent, en adhérant aux conventions de votre équipe ou projet.
* Code inutilisé : Supprimez toutes les variables, fonctions ou imports inutilisés qui encombrent la base de code.
* Améliorations des tests : Contrairement à la perception habituelle concernant le TDD, vous pouvez ajouter des tests chaque fois qu'il y a un besoin. Améliorez la suite de tests en ajoutant de nouveaux cas de test pour couvrir des scénarios qui n'étaient pas précédemment abordés. Cela aide à maintenir une couverture de test complète.
* Documentation : Si le but de votre code n'est pas immédiatement clair à partir du code lui-même, envisagez d'ajouter ou d'améliorer la documentation pour expliquer son intention et son utilisation. Évitez d'en faire une habitude. Cela est destiné à agir comme une explication complémentaire pour les cas cruciaux afin d'éviter la confusion.

Notez que le code TDD doit être auto-expressif et indépendant de la documentation.

Rappelez-vous, lors de la refactorisation, il est crucial de continuer à exécuter tous vos tests pour vous assurer qu'ils continuent de passer.

#### Conseils

* Gardez les tests complets : Assurez-vous que vos tests couvrent divers scénarios pour attraper les effets secondaires non intentionnels pendant la refactorisation.
* Refactorisez progressivement : Apportes des modifications mineures à votre code et exécutez les tests fréquemment pour attraper toute régression tôt.

#### Erreurs courantes à éviter :

* Refactoriser sans tests : Refactoriser sans avoir de tests en place peut conduire à un comportement inattendu. S'il y a une chance de manquer une partie de la logique, envisagez d'écrire des tests pour celle-ci.
* Grand changement de code : Parfois, nous finissons par changer plus de lignes que ce que nous avons développé pour faire passer le test. Envisagez toujours une phase de refactorisation séparée plutôt que de faire trop de changements dans la phase de développement, car c'est une option plus sûre et moins coûteuse.

### Écrire un Nouveau Test qui Échoue (Redémarrer le Flux)

Maintenant, vous pensez à la prochaine chose que vous voulez que votre code fasse. 

Vous commencez par écrire un nouveau test qui devrait échouer parce que votre code ne sait pas encore comment faire la nouvelle tâche. C'est comme donner à votre code un nouveau défi à résoudre. 

Ensuite, vous répétez tout le cycle : faire passer le test avec le code (carré vert), nettoyer si nécessaire (carré bleu), et continuer à tester pour vous assurer que tout fonctionne (carré vert pâle). 

De cette manière, vous avancez toujours et construisez votre code étape par étape.

#### Conseils

* Étapes incrémentales : Ajoutez de nouveaux tests pour de nouvelles fonctionnalités par petites incrémentations afin de maintenir un chemin de développement clair. Au lieu d'essayer d'implémenter une fonctionnalité complexe d'un seul coup, vous la décomposez en morceaux plus petits et gérables, et créez des tests pour chacun de ces morceaux. Cette approche maintient un chemin de développement clair et régulier, vous aidant à rester concentré, à réduire les risques et à vous assurer que chaque ajout à votre logiciel est soigneusement testé.
* Boucle de rétroaction : Utilisez la rétroaction de l'écriture de tests qui échouent pour guider votre implémentation. La boucle de rétroaction met en évidence la nature itérative du TDD. Alors que vous créez de nouveaux tests et observez leur échec, vous gagnez des informations précieuses qui guident votre implémentation. 

Voici comment fonctionne la boucle de rétroaction :

* Définition des attentes : Lorsque vous écrivez un nouveau test, vous définissez vos attentes quant à la manière dont le code devrait se comporter. Cela clarifie ce que vous visez à atteindre avec votre nouvelle fonctionnalité.
* Échec initial : Le test échoue au début parce que le code correspondant pour remplir ses attentes est manquant ou incomplet. Cet échec initial est une partie naturelle du processus TDD.
* Guide votre implémentation : La rétroaction de l'échec du test vous indique la direction de ce qui doit être écrit ou modifié. Cela devient une feuille de route pour votre développement, décrivant à quoi devrait ressembler la nouvelle fonctionnalité.
* Progrès incrémental : Alors que vous implémentez le code nécessaire pour faire passer le test, vous construisez progressivement la fonctionnalité souhaitée. Chaque étape est guidée par la rétroaction fournie par le test qui échoue.
* Vérification : Une fois votre implémentation terminée, vous exécutez à nouveau le test. S'il passe, il vérifie que votre nouveau code satisfait les attentes que vous avez initialement définies.

La boucle de rétroaction garantit que votre développement est étroitement aligné avec les objectifs prévus de votre logiciel.

#### Erreurs courantes à éviter :

* Écrire des tests après l'implémentation : N'écrivez pas de tests après avoir implémenté la fonctionnalité. Le TDD consiste à écrire des tests en premier. Même un petit morceau de logique ajouté avant le code de test signifie qu'il y a un gaspillage de ressources possible/un bug dans le code. Le but est de ne pas ajouter de logique à moins qu'il y ait un besoin pour celle-ci à partir de la suite de tests.
* Sauter les tests qui échouent : Ne sautez pas cette étape même si vous pensez savoir comment implémenter la fonctionnalité.

Voici pourquoi vous ne devriez pas sauter l'étape des tests qui échouent même lorsque vous êtes confiant :

* Clarté de l'intention : Écrire un test qui échoue clarifie votre intention pour la fonctionnalité. Cela vous force à considérer le comportement exact et les résultats que vous visez avant de plonger dans l'implémentation.
* Vérification des hypothèses : Même si vous pensez comprendre la fonctionnalité, créer un test garantit que vos hypothèses sont valides. Votre compréhension peut être correcte, mais le test la valide.
* Filet de sécurité : En écrivant un test qui échoue, vous établissez un filet de sécurité qui empêche les régressions à l'avenir. Il agit comme une spécification pour la fonctionnalité et aide à attraper les effets secondaires non intentionnels.
* Développement incrémental : Le TDD encourage le développement incrémental. Chaque nouvelle fonctionnalité est construite étape par étape, avec une progression claire de l'échec du test à l'implémentation fonctionnelle. Sauter cette étape perturbe cette progression.
* Documentation : Le test qui échoue documente le comportement attendu de la fonctionnalité. Cette documentation est précieuse pour vous et votre équipe, surtout lorsque vous revisitez le code à l'avenir. N'oubliez jamais qu'il existe des systèmes pour générer des rapports en listant tout votre code de test pour les chefs de produit et les QA. Ces rapports exposent les détails que vous avez repérés dans le produit, alors essayez de les convaincre que vous avez compris le point à fond.

## Comment Développer en Utilisant le TDD

Le TDD met l'accent sur l'importance d'écrire des [tests automatisés](https://smartbear.com/learn/automated-testing/what-is-automated-testing/) pour guider la conception et le développement de logiciels. Cela conduit à un code plus fiable, maintenable et plus facile à modifier au fil du temps.

Mais comment pouvons-nous le mettre en pratique ? En l'essayant et en nous y habituant progressivement.

Essayons le TDD tout en développant une nouvelle fonctionnalité pour démontrer comment nous pouvons commencer à l'utiliser dans le monde réel.

Nous allons implémenter une fonctionnalité de réglage automatique de la taille de la police. 

Nous avons une application de nouvelles et un utilisateur peut définir une vitesse de défilement automatique pour le flux de nouvelles. 

Nous voulons implémenter une fonctionnalité qui ajuste la taille de la police de l'écran en fonction de la vitesse de défilement définie dans la page de profil de l'utilisateur.

Si l'utilisateur définit la vitesse de défilement de 0 à 1, alors la taille de la police doit augmenter de 1,3. 

Toute augmentation de la vitesse de défilement au-dessus de 1 entraînera une augmentation de la taille de la police de 1,2. 

Cette fonctionnalité permet aux utilisateurs d'avoir une meilleure expérience lors de la lecture des nouvelles.

J'ai également partagé le code que nous explorons dans [ce dépôt GitHub](https://github.com/thesiamak/tdd-FontSize).

N'hésitez pas à le cloner et à jouer avec.

Essayez de suivre les étapes au fur et à mesure que nous progressons dans le développement. Cela vous aidera à saisir les techniques et la manière de penser dans le contexte du TDD de manière pratique. 

Alors, ouvrez Android Studio et créez un nouveau projet.

### Diagramme de Flux de Données de la Fonctionnalité de Réglage Automatique de la Taille de la Police

![Image](https://www.freecodecamp.org/news/content/images/2023/08/test--2-.png)
_DFD d'une fonctionnalité exemple dans une application android_

Ci-dessus se trouve le diagramme de flux de ce à quoi le flux de données devrait ressembler à la fin. 

Voici un aperçu de chaque composant engageant :

La classe `AutoScrollSettingsUseCase` gérera la logique de calcul et de stockage du `FontRatio` en fonction de la vitesse de défilement sélectionnée. 

Ce cas d'utilisation aura une dépendance au `UserRepository` stockant la valeur `FontRatio`.

Dans le `UserRepository`, il y a des méthodes pour stocker et récupérer la valeur `FontRatio` en utilisant le mécanisme `Storage`. Chaque fois qu'un nouveau `FontRatio` est envoyé au stockage, tous les observables recevront une émission avec la dernière valeur.

Dans le `UserProfileViewModel`, il y a une instance de `AutoScrollSettingsUseCase` qui est appelée chaque fois que l'utilisateur met à jour la vitesse de défilement. Cela déclenchera le recalcul du `FontRatio` et son stockage via le dépôt.

Nous aurons les composants UI nécessaires dans la section des paramètres utilisateur pour permettre à l'utilisateur de saisir sa vitesse de défilement souhaitée. Cela peut être fait en utilisant des éléments UI Android standard tels que `NumberPicker` ou des composants UI personnalisés (nous ne discuterons pas de ces parties).

Voici la décomposition pour une fonctionnalité simple et chaque fois que vous la parcourez, cela devient plus clair quelles sont les étapes et le résultat final. Il est crucial de le faire pour vos changements.

### Comment Écrire les Tests

La première étape consiste toujours à créer la classe de test elle-même. Dans ce cas, nous aurons au moins les classes de test suivantes :

* `UserRepositoryTest`
* `AutoScrollSettingTest` 
* `UserSettingsViewModelTest`

Je préfère commencer par la partie ViewModel. 

Un ViewModel est un composant architectural Android qui échappe aux changements de cycle de vie (comme premier plan, arrière-plan, focalisé). C'est donc un bon endroit pour stocker nos états. 

Créons le fichier de test à l'intérieur du répertoire `unitTest` du code source en suivant le même chemin de package que le code de la fonctionnalité réelle.

Le TDD en pratique est différent du développement de travail hérité. 

Avec le TDD, nous utilisons un IDE pour booster le processus de création de fichiers et de propriétés (champs). Mais nous créons les fichiers de test manuellement ! Après quelques essais, cet aspect de l'IDE deviendra pratique.

Créez la structure de code (packages) puis créez votre classe de test en cliquant avec le bouton droit sur le package et en sélectionnant le type `Class`. 

Choisissez un nom descriptif pour celui-ci (peut-être devriez-vous suivre une convention pour cela si vous ne le faites pas déjà). 

Par exemple : `xxx est testé pour`, où `xxx` est le nom du composant testé.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Screenshot-2023-09-02-at-2.00.39-PM.png)
_Utilisez l'IDE pour créer des fichiers_

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Screenshot-2023-09-02-at-2.01.48-PM.png)

Maintenant, créons des tests vides. Essayez d'être aussi large que possible. 

Selon le diagramme, nous n'aurons pas beaucoup de logique pour cette fonctionnalité. 

Il existe deux stratégies principales pour écrire des fonctions de test unitaire :

* AAA
* Given/When/Then

```junit
@Test fun `stratégie A`(){ 
    // Arrange
    // Act 
    // Assert 
}

@Test fun `stratégie B`(){ 
    // Given 
    // When 
    // Then 
}
```

Choisissons-en une et suivons-la pour tous vos tests.

Le concept est le même : regroupez votre code de test pour le rendre facile à lire et à maintenir.

Voici ce que j'ai pour l'instant :

```junit
class UserProfileViewModel est testé pour` {
    // Classe non implémentée 
    val viewModel = UserProfileViewModel()

    @Test
    fun Le ratio de police est récupéré depuis la source de données`(){}
    
    @Test
    fun `La mise à jour de la vitesse de défilement est appelée donc les calculs de taille de police sont déclenchés`() {}

    @Test
    fun `Le ratio de police est mis à jour avec de nouvelles émissions depuis la source de données`() {}
}
```

Lançons les tests !

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Screenshot-2023-08-06-at-9.42.00-PM.png)
_Test échoué en raison d'une cible de test manquante_

Il échoue. En fait, la construction a échoué - Pas le test. 

Félicitations ! Nous venons de réussir la première étape du cycle TDD :

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Screenshot-2023-08-06-at-9.44.08-PM.png)
_Première étape du cycle TDD_

Puisque le ViewModel n'existe pas encore, nous avons des couleurs rouges. 

Maintenant, créons une instance du ViewModel, 

Nous utilisons donc un IDE pour créer une classe manquante ou un code non implémenté. 

Pour faire apparaître cette boîte de dialogue, je déplace le pointeur vers la partie non implémentée et appuie sur Option + Return (sur macOS). 

Ensuite, suivez les options fournies :

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Screenshot-2023-08-06-at-9.48.22-PM-1.png)
_Action TDD : Créer des fichiers cibles via le fichier UnitTest_

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Screenshot-2023-09-02-at-2.05.10-PM.png)
_Choisissez la destination correcte pour le nouveau fichier_

Et maintenant, relançons les tests (dernière étape) :

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Screenshot-2023-08-06-at-9.52.50-PM.png)
_Affichage du test réussi_

Oui ! Il a réussi.

Notez que ces tests ont un corps vide et ne testent rien ! C'est correct et tout va bien.

Nous devrions même continuer à créer toutes les classes de test (toujours avec un corps de test vide) pour chaque composant dans le diagramme DFD - j'ai partagé ceux-ci au début de l'article.

Cela aide encore plus à avoir une compréhension plus claire de la fonctionnalité avant de l'implémenter.

Finalement, nous aurons environ 3-4 classes de test contenant des scénarios généraux et des tests unitaires à couvrir. 

Cela ressemblera à quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Screenshot-2023-09-02-at-2.07.53-PM.png)
_Cas de test vides minimaux_

Implémentons-en un comme exemple.

Mais, avant cela, nous allons devoir travailler avec les modèles de données UI et Domain de cette fonctionnalité. 

Donc, afin de pouvoir déplacer les données, créons les classes de données dont vous avez besoin à l'avance.

Retour à notre classe de test `ProfileViewModel`, nous avons une fonction de test unitaire vide. Implémentons celle-ci.

Notez que la clé ici est de lire attentivement le test et d'éviter toute implémentation ou assertion supplémentaire. 

Seule l'exigence est autorisée à être implémentée.

Dans ce cas, nous avons besoin d'un flux de données qui est connecté à une source de données précédemment créée (`UserRepository`). 

N'oubliez pas : Nous avons besoin d'un test qui échoue en premier.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Screenshot-2023-08-06-at-11.19.34-PM-1.png)
_Implémenter le corps interne_

Remarquez les parties non implémentées à l'intérieur du corps de la fonction de test (marquées en rouge). 

Maintenant, implémentons le code, puis refactorisons-le pour le faire passer.

J'utilise la bibliothèque [MockK](https://mockk.io/) pour les mocks de classes et d'objets et [Turbine](https://github.com/cashapp/turbine) pour tester les flux Flow ici.

Si vous n'êtes pas familier avec eux, ne paniquez pas ! Consultez simplement leur page web officielle et essayez-les.

Créons d'abord la dépendance et ajoutons-la au ViewModel en utilisant [Named Arguments](https://kotlinlang.org/docs/functions.html#named-arguments). Named Argument nous aide lors de la création du paramètre via l'IDE pour introduire des noms appropriés à travers le code de test.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Screenshot-2023-08-06-at-10.43.23-PM.png)
_Créer un paramètre manquant en utilisant les dialogues de l'IDE_

Faites de même pour la variable `FontRatio` à l'intérieur du Repository. 

Finalement, le code de test final peut être quelque chose comme le code ci-dessous :

```junit
class `UserProfileViewModel est testé pour` {

    init {
        Dispatchers.setMain(Dispatchers.Unconfined)
    }

    val mockUserRepository = mockk<UserRepository>()

    @Test
    fun `Le ratio de police est récupéré depuis la source de données`() = runTest {
        // Given
        val expectedRatio = 2.0f
        every { mockUserRepository.fontRatio } returns flowOf(FontRatioUiModel(expectedRatio))
        val viewModel = UserProfileViewModel(userRepository = mockUserRepository)

        // When
        viewModel.fontRatio.test {
            val fromDataSource = expectItem()

            // Then
            assertEquals(/* expected = */ expectedRatio, /* actual = */ fromDataSource.fontRatio)
        }
    }
...
}
```

Notez que nous n'implémentons pas les parties internes du ViewModel ou du Repository ici.

Nous créons simplement les parties manquantes pour supprimer l'erreur du corps du test. 

Nous implémenterons ces détails dans une prochaine itération. 

Exécutez le test maintenant. 

Bien sûr, il échouera, car nous n'avons pas implémenté `FontRatio` à l'intérieur de `ProfileViewModel`. 

Maintenant, refactorisez le ViewModel pour faire passer le test (implémentation minimale). 

Dans ce cas, il suffit de connecter le flux d'état au dépôt. Nous l'avons déjà ajouté comme dépendance dans l'itération précédente. 

Voici le code final :

```kotlin
class UserProfileViewModel(
    userRepository: UserRepository
) : ViewModel() {

    val fontRatio: StateFlow<FontRatioUiModel> = userRepository.fontRatio.stateIn(
        initialValue = FontRatioUiModel(DEFAULT_FONT_RATIO),
        scope = viewModelScope,
        started = SharingStarted.Lazily
    )

    companion object {
        private const val DEFAULT_FONT_RATIO = 1.0f
    }
}

```

Exécutez le test à nouveau, et Boom ! Il passe !

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Screenshot-2023-08-06-at-11.23.17-PM.png)
_Test réussi après l'implémentation minimale du code principal_

Avec ce test unitaire, nous avons implémenté une partie primaire du composant `UserProfileViewModel`. Mais seulement les parties nécessaires. Faites de même pour le reste des cas de test. 

Ne traitez pas ces cas de test comme vous le faites avec les tests unitaires normaux (qui s'exécutent et passent rapidement). 

Passez un peu de temps dessus pour comprendre les exigences techniques et produit d'abord. Ensuite, déployez le plan et commencez à implémenter. Après quelques essais, il sera plus facile de penser de manière TDD.

### Code Source

Le [code source](https://github.com/thesiamak/tdd-FontSize) et le dépôt pour ce projet sont disponibles sur [ma page GitHub](https://github.com/thesiamak).

N'hésitez pas à le consulter et à compléter les étapes suivantes. J'ai séparé les itérations dans différentes branches afin que vous puissiez les comparer avec votre propre implémentation.

## Conclusion

Alors, après avoir plongé dans le Développement Piloté par les Tests (TDD) et exploré ses tenants et aboutissants, je dois dire que c'est un changement de jeu ! 

Laissez-moi vous le décomposer :

Points clés :

* Le TDD consiste à écrire des tests avant d'écrire le code réel. Cela peut sembler un peu bizarre au début, mais faites-moi confiance, cela fonctionne merveilleusement bien.
* Le processus TDD suit un cycle simple : écrire des tests qui échouent, implémenter le code pour faire passer ces tests, puis refactoriser si nécessaire pour que tout fonctionne en douceur.
* En mettant l'accent sur les tests automatisés, le TDD nous aide à concevoir et développer des logiciels solides, maintenables et adaptables au fil du temps.

Nous avons commencé par créer des classes de test et écrire des fonctions de test vides, mais c'est maintenant votre tâche de les terminer (ou vous pouvez sauter directement au dépôt partagé :) ). 

Cela peut sembler un peu étrange d'avoir des tests qui ne font rien, mais c'est tout à fait partie du plan.

Ensuite, nous avons établi un plan clair de ce que notre fonctionnalité devrait faire, basé sur un diagramme de flux de données. Cela nous a aidé à comprendre les exigences avant de plonger dans l'implémentation.

Avec le plan en main, nous avons commencé à implémenter les composants nécessaires (ViewModel dans ce cas), en nous assurant que nos tests échouent d'abord. C'est exact, les tests qui échouent sont en fait une bonne chose dans le TDD !

Progressivement, nous avons connecté les pièces ensemble, comme la mise en place de la classe `UserAutoScrollSettingsUseCase` pour gérer le calcul de la taille de la police en fonction de la vitesse de défilement automatique (voir le dépôt du projet).

Nous avons également abordé les composants UI, permettant aux utilisateurs de saisir leur vitesse de défilement souhaitée, et en nous assurant que la taille de la police était ajustée en conséquence (voir le dépôt du projet).

Tout au long du processus, nous nous sommes assurés de garder notre code propre et simple, en nous concentrant sur ce qui était nécessaire pour faire passer les tests. Pas de complexité inutile ici !

À la fin, nous avions notre fonctionnalité "Réglage Automatique de la Taille de la Police" en marche, avec des tests qui passaient avec brio.

Rappelez-vous, le TDD ne consiste pas à se précipiter à travers les tests ou à coder comme un fou. Il s'agit d'être délibéré et réfléchit dans votre processus de développement, ce qui porte ses fruits à long terme.

Alors, si vous cherchez à améliorer votre jeu de développement logiciel, essayez le TDD ! C'est une approche puissante qui rendra votre code plus solide, réduira les bugs et fera de vous un meilleur développeur dans l'ensemble.

Ce que j'ai partagé, c'est comment nous travaillons dans mon équipe et cela fonctionne pour nous, mais ce n'est pas la solution parfaite pour chaque équipe/entreprise. Vous devez découvrir si c'est la vôtre ou non. Faites-moi savoir si vous pensez que je peux améliorer cette solution.

Bon codage ! 🚀