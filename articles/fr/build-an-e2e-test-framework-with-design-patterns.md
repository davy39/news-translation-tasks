---
title: Comment construire un Framework de Test E2E en utilisant des Design Patterns
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-09T17:14:49.000Z'
originalURL: https://freecodecamp.org/news/build-an-e2e-test-framework-with-design-patterns
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fa818ca49c47664ed81b9ed.jpg
tags:
- name: automation
  slug: automation
- name: design patterns
  slug: design-patterns
- name: Testing
  slug: testing
seo_title: Comment construire un Framework de Test E2E en utilisant des Design Patterns
seo_desc: "By Jose J. Rodríguez\nEnd to End or E2E testing is about simulating the\
  \ user's experience. It doesn't deal with functions, variables, classes, or databases.\
  \ Instead, it deals with buttons, clicks, expected messages, links, and so on. \n\
  You might say th..."
---

Par Jose J. Rodríguez

Les tests End to End ou E2E consistent à simuler l'expérience de l'utilisateur. Ils ne traitent pas des fonctions, des variables, des classes ou des bases de données. Au lieu de cela, ils traitent des boutons, des clics, des messages attendus, des liens, etc. 

On pourrait dire que les tests E2E sont les tests "ultimes" car ils vérifient si le produit dans son ensemble se comporte comme prévu.

En général, les tests E2E sont difficiles à automatiser. Tout d'abord, vous avez besoin d'outils qui peuvent interagir avec l'application testée – remplir des formulaires, attendre qu'une page se charge complètement, ce genre de choses.

Vous devez également obtenir les résultats à partir de l'interface utilisateur. Vous n'avez pas de fonctions retournant des objets, mais des éléments HTML contenant les informations. Simuler un utilisateur réel peut être un défi et peut nécessiter beaucoup de maintenance.

Dans cet article, je vais parler de ma propre expérience dans la construction d'un framework de test E2E. J'ai appliqué quelques Design Patterns intéressants, donc je pense que cela pourrait être intéressant pour vous même si vous n'avez rien à voir avec l'automatisation des tests E2E.

Cet article est _agnostique en termes de langage et d'outil_. Cela signifie que je ne ferai pas référence à un langage de programmation spécifique ou à un outil E2E spécifique comme Selenium, Puppeteer ou Playwright. Au fait, ce sont d'excellents outils pour automatiser les tests E2E. De plus, cet article se concentre sur les tests E2E pour les sites web.

## Le problème que je devais résoudre

Je devais concevoir un framework pour effectuer différents tests E2E sur différents sites web. Plus précisément, je devais effectuer des tests sur des composants React spécifiques à l'intérieur de ces sites web. 

Chaque composant avait la même structure et les mêmes sélecteurs CSS, peu importe le site web, et ne changeait que légèrement d'un site à l'autre. Je devais effectuer des tests pour chaque viewport possible (mobile, tablette et bureau), et les composants devaient changer leur structure lorsque le viewport changeait.

Dans ce scénario, je ne savais rien des développeurs. Je devais donc être préparé à gérer certains changements imprévus dans l'interface relativement facilement. En d'autres termes, il était crucial que le framework soit facile à maintenir.

Alors, comment devrais-je créer un framework de test E2E qui ne se soucie pas trop si les développeurs changent l'attribut id d'un bouton qui était cliqué dans un test ? Comment pourrais-je écrire des tests pour un composant qui n'était pas encore créé ? Et comment pourrais-je rendre chaque test facile à lire et à comprendre ?

J'ai pu atteindre tous ces objectifs en appliquant quelques abstractions et design patterns. Alors, voyons comment je l'ai fait.

## Le Page Object Model

La première chose que nous devons faire est de créer une abstraction pour une page. Cela est important pour plusieurs raisons. 

Tout d'abord, cela augmentera la lisibilité. Par exemple, vous ne voulez pas avoir une ligne dans votre test qui lit ```tool.getByCssSelector("button.btn.btn-submit").click()```. Au lieu de cela, vous voulez avoir une ligne comme celle-ci : ```page.clickSubmitLoginFormButton()``` ou quelque chose de similaire. 

Vous devez également garder tous les sélecteurs CSS et les éléments liés au DOM en un seul endroit. Ainsi, lorsque quelque chose dans l'interface change, vous n'avez besoin de modifier qu'un seul fichier (ou peut-être deux, mais pas plus ;-) ).

Cette abstraction est appelée le **Page Object Model**. Vous créez une classe qui représente uniquement les éléments qui vous intéressent sur la page. Vous mettez tous les éléments liés au DOM dans ces classes.

Dans mon cas, je l'ai fait légèrement différemment. J'ai créé deux classes pour chaque page, un **PageModel** et un **Page Object**. 

Dans la première, j'ai mis les éléments de la page. Par exemple, supposons que nous testons une page de connexion, alors mon **LoginPageModel** serait comme ceci :

```pseudocode

class LoginPageModel

    constructor(tool)

        this.tool = tool


    loginUsernameInput()

        return this.tool.getById('username-input')


    loginPasswordInput()

        return this.tool.getById('password-input')


    loginSubmitButton()

        return this.tool.getById('submit-login-button')

```

Si l'un de ces éléments change à l'avenir, nous n'avons besoin de modifier que la classe **PageModel** correspondante.

Dans la classe **PageObject**, j'ajoute les actions que vous pouvez effectuer sur la page. Un exemple de classe **LoginPageObject** serait :

```pseudocode

class LoginPageObject

    constructor(pageModel)

        this.model = pageModel


    typeUsername(username)

        this.model.loginUsernameInput().type(username)


    typePassword(password)

        this.model.loginPasswordInput().type(password)


    clickLoginSubmitButton()

        this.model.loginSubmitButton().click()

```

Ici, nous pouvons tirer parti d'un langage typé statiquement qui peut obtenir toutes les méthodes de la classe de modèle au moment de la compilation. Ainsi, un outil IntelliSense peut nous rappeler le nom de chaque méthode représentant un élément de page. 

Nous obtenons également plus d'erreurs de compilation et moins d'erreurs d'exécution, ce qui est très bon pour nous et notre santé mentale.

Pourquoi devons-nous séparer les éléments de la page des actions de la page ? Une seule classe contenant à la fois les éléments et les actions peut être très grande. 

Nous pouvons dire qu'en faisant cela, nous appliquons le principe de responsabilité unique et ce serait bien. Mais dans ce cas, cela n'a pas beaucoup de signification pratique au-delà de la lisibilité et de la simplicité des classes.

Avec l'abstraction **Page Object**, nous pouvons créer des tests qui ne dépendent que des objets de page au lieu d'écrire des sélecteurs CSS compliqués au milieu du code de test. 

Nous gardons tous les éléments liés au DOM en un seul endroit et nos tests peuvent être plus expressifs et faciles à comprendre.

## Écrire des tests – le Pattern Facade

Maintenant, nous avons de nombreuses classes qui contiennent tous les éléments et actions de plusieurs pages. Ce que nous devons faire maintenant, c'est construire nos tests. 

Ces tests fourniront une interface simple qui expose la fonctionnalité ```run``` au client. Cette fonctionnalité retourne un résultat de test. 

Le client n'a pas à se soucier d'accéder à un élément ou d'effectuer une action, il doit simplement instancier le test et l'exécuter.

Lorsque nous fournissons une interface simple qui masque une infrastructure plus complexe, nous appliquons le Pattern Facade. Je sais que ce n'est qu'un nom fantaisiste pour quelque chose qu'il est clair que nous devions faire. 

En continuant avec notre exemple de test de page de connexion, le **LoginTest** serait quelque chose comme ceci :

```pseudocode

class LoginTest


    constructor(loginPageObject)

        this.pageObject = loginPageObject


    run()

        this.pageObject.typeUsername("TestUser")

        this.pageObject.typePassword("TestPassword")

        this.pageObject.clickLoginSubmitButton()

        assert that the login was successful
```

La dernière ligne de la méthode ```run``` est une assertion. Selon la complexité des assertions que vous utilisez, vous pouvez soit les définir séparément, soit à l'intérieur du Page Object. 

En choisissant la première option, vous pouvez réutiliser et étendre les assertions. Mais si vos assertions sont très spécifiques à chaque cas et suffisamment simples, la première option peut être excessive et vous serez probablement satisfait avec la seconde.

Nous injectons également la dépendance Page Object dans le test. Nous ne faisons pas ```this.pageObject = new LoginPageObject()``` mais recevons la dépendance en tant qu'argument dans le constructeur. Cela s'appelle l'_Injection de Dépendance_. Ainsi, nous pouvons instancier le même test pour une autre page. 

Nous injectons également le Page Model dans les instances de Page Object. Ensuite, nous pouvons avoir le même Page Object avec un autre modèle (Exemple : même instance LoginPageObject avec un LoginMobilePageModel au lieu d'un LoginPageModel régulier).

Mais maintenant, pour instancier un test, nous devons instancier un ou plusieurs Page Models, puis un ou plusieurs Page Objects, et enfin le test. Cela semble être trop de travail. C'est précisément l'un des inconvénients de l'utilisation de l'Injection de Dépendance – mais le problème est soluble !

## Le Pattern Factory

Déléguons la responsabilité à une autre abstraction. Dans ce cas, nous allons créer des factories.

Les factories sont des classes utilisées pour instancier d'autres classes. Chaque classe de factory sera responsable de l'instanciation d'un test spécifique. C'est le Pattern Factory en action.

Nous pouvons donc créer une **LoginTestFactory** pour notre LoginTest :

```pseudocode

import tool

class LoginTestFactory


    create(config)

        if config.viewport == 'mobile'
            then return new LoginTest(new LoginPageObject(new LoginMobilePageModel(tool)))
        else
            return new LoginTest(new LoginPageObject(new LoginPageModel(tool)))
```

Ici, avec ```tool```, nous représentons toute technologie possible que vous pourriez utiliser pour obtenir les éléments d'une page et interagir avec eux. 

Peut-être que vous ne passez pas l'outil importé tel quel, mais vous créez des objets en utilisant cet outil et passez ensuite ces objets en paramètres. 

Mais l'idée est que toute la logique relativement complexe pour créer une instance de test est encapsulée dans un objet factory.

Pour exécuter notre test, nous n'avons besoin de faire que quelque chose comme ceci :

```pseudocode

runLoginTestDesktop()

    factory = new LoginTestFactory()

    config = new ConfigObject(viewport = 'desktop')

    test = factory.create(config)

    test.run()



runLoginTestMobile()

    factory = new LoginTestFactory()

    config = new ConfigObject(viewport = 'mobile')

    test = factory.create(config)

    test.run()
```

Maintenant, dans la section des conclusions, nous vérifierons si nous avons accompli nos objectifs initiaux.

## Conclusion

Construire votre framework de test de cette manière peut réduire considérablement le coût des changements dans une interface utilisateur. Tout le code qui dépend de l'interface utilisateur est isolé dans des classes spécifiques qui abstraient le concept de page.

Cette abstraction vous permet également d'écrire vos tests pour la semaine prochaine. (Je veux dire les tests pour les composants qui n'ont pas encore été créés.) Vous faites simplement les nouveaux PageModels et PageObjects nécessaires pour simuler les éléments de la page qui seront créés et vous pouvez construire le reste du processus de la même manière que nous avons vu jusqu'à présent. 

Lorsque vous avez des éléments spécifiques sur l'interface, vous pouvez changer les modèles de page et vérifier si l'application se comporte comme prévu.

Vous avez également des tests très faciles à lire et à comprendre puisque vous faites des actions expressives comme ```this.pageObject.clickLoginSubmitButton()```. Ainsi, vos tests peuvent décrire les exigences de votre application et peuvent être facilement maintenus.

L'automatisation des tests E2E est difficile car il est difficile de la garder simple. Et un test complexe n'est pas un test. 

Dans cet article, j'ai montré quelques design patterns et bonnes pratiques que vous pouvez utiliser pour la rendre plus fluide. J'ai essayé de la rendre agnostique en termes de langage et d'outil afin que vous puissiez appliquer ces pratiques dans votre projet, quel que soit le langage ou la technologie que vous utilisez. Je n'ai supposé qu'un langage de programmation orienté objet.

Que vous créiez ou non un framework de test E2E, je pense que cet article peut encore vous être utile. Certains de ces trucs peuvent être appliqués à une variété relativement large de problèmes.

Vous pouvez visiter mon [blog personnel](https://jj.hashnode.dev) et me suivre sur [Twitter](https://twitter.com/josejorgexl) pour plus de contenu lié à l'informatique.