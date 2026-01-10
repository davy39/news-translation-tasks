---
title: Qu'est-ce que le test de bout en bout et quand l'utiliser ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-08T23:39:00.000Z'
originalURL: https://freecodecamp.org/news/end-to-end-testing-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/iam_os-Gr7q7kqfnVU-unsplash.jpg
tags:
- name: best practices
  slug: best-practices
- name: Software Testing
  slug: software-testing
- name: Testing
  slug: testing
- name: unit testing
  slug: unit-testing
seo_title: Qu'est-ce que le test de bout en bout et quand l'utiliser ?
seo_desc: 'By Stan Georgian

  Any serious application should be accompanied by a few test suites to validate its
  stability and performance.

  There are many types of tests, each with their own purpose that cover specific aspects
  of the application. And so when you''...'
---

Par Stan Georgian

Toute application sérieuse devrait être accompagnée de quelques suites de tests pour valider sa stabilité et ses performances.

Il existe de nombreux types de tests, chacun ayant son propre objectif couvrant des aspects spécifiques de l'application. Ainsi, lorsque vous testez votre application, vous devez vous assurer d'avoir un bon équilibre de divers tests.

![Image](http://media.giphy.com/media/UsmcxQeK7BRBK/giphy.gif)

Mais un type de test est souvent privilégié par les développeurs par rapport à tous les autres, et a donc tendance à être surutilisé. Ce type de test est le [test de bout en bout](https://www.freecodecamp.org/news/end-to-end-tests-with-selenium-and-docker-the-ultimate-guide/) (E2E).

## Qu'est-ce que le test de bout en bout ?

Pour ceux qui explorent encore le monde des tests logiciels, le test E2E consiste à valider l'ensemble de votre application de bout en bout, ainsi que toutes ses dépendances.

Dans le test E2E, vous créez un environnement identique à celui qui sera utilisé par les utilisateurs réels. Ensuite, vous testez toutes les actions que vos utilisateurs pourraient effectuer sur votre application.

Avec le test de bout en bout, vous testez des flux entiers – comme se connecter à un site web ou acheter un produit dans une boutique en ligne.

![Image](https://paper-attachments.dropbox.com/s_EA4D61AC224EF8447071464ABC3123BDD99BABBB705D8D6423915F4DE15DDD1B_1603950228233_2_++1+.jpg)

Mais si vous surutilisez le test E2E, vous [inversez la pyramide des tests](https://automationpanda.com/2018/08/01/the-testing-pyramid/). J'ai été dans une situation comme celle-ci. Dans l'un de mes projets, je prévoyais de couvrir la plupart des cas avec des tests E2E – ou pire, d'utiliser uniquement le test E2E. Heureusement, j'ai changé d'avis. Alors maintenant, je veux partager avec vous ce que j'ai appris.

## Pourquoi vous devriez respecter la pyramide des tests

Les tests écrits de manière chaotique semblent et paraissent normaux au début, mais ils seront toujours douloureux à la fin.

Nous écrivons des tests pour gagner du temps, et nous le faisons avec l'automatisation des tests. Bien sûr, nous pourrions ouvrir nos applications nous-mêmes et les tester manuellement. Si nous n'avions à le faire qu'une seule fois, alors il n'y aurait pas de problème. Mais ce n'est rarement le cas.

Les logiciels sont toujours mis à jour. Vous devez donc effectuer des tests continus pour rester à jour. Vous ne pouvez pas exécuter tous les tests manuellement à chaque fois que l'application est mise à jour. Si vous pouvez écrire une suite de tests une fois et ensuite l'exécuter chaque fois que vous voulez tester un aspect de votre application, vous gagnerez beaucoup de temps.

Chaque test a son propre objectif. Si vous dépassez les limites de chaque type de test, vos tests commenceront à vous nuire plutôt qu'à vous aider. Cela est dû au fait que vous passerez plus de temps à écrire des tests et à les maintenir qu'à développer l'application elle-même. En d'autres termes, vous perdrez l'un des plus grands avantages des tests automatisés.

Un bon point de départ est de suivre la pyramide des tests. Elle vous aide à trouver le bon équilibre des tests. Elle représente une directive standard de l'industrie, et elle a perduré depuis le milieu des années 2000 parce qu'elle continue d'être pratique.

Cela signifie-t-il que les développeurs suivent toujours ses directives ? Pas vraiment. Parfois, la pyramide ressemble à une pyramide inversée, où la plupart des tests sont des tests E2E. Ou elle ressemble à un sablier, où il y a beaucoup de tests unitaires et de tests E2E, mais pas beaucoup de tests d'intégration.

![Image](https://paper-attachments.dropbox.com/s_EA4D61AC224EF8447071464ABC3123BDD99BABBB705D8D6423915F4DE15DDD1B_1603950198553_02.jpg)

## Les trois couches de la pyramide des tests

Une pyramide de tests a généralement trois couches : les tests unitaires, les tests d'intégration et les tests de bout en bout. Apprenons-en plus sur eux maintenant.

### 1. Tests unitaires

Les [tests unitaires](https://www.tutorialspoint.com/software_testing_dictionary/unit_testing.htm) se concentrent sur la plus petite unité de code, comme les fonctions ou les classes.

Ils sont courts et n'ont aucune dépendance externe. S'ils ont une dépendance externe, vous utilisez des mocks à la place.

Si un test unitaire échoue, trouver le problème est généralement un processus simple. Ils ont également une portée de test réduite, ce qui les rend simples à écrire, rapides à exécuter et faciles à maintenir.

### 2. Tests d'intégration

Les [tests d'intégration](https://www.tutorialspoint.com/software_testing_dictionary/integration_testing.htm) se concentrent sur l'interaction entre deux entités distinctes. Ils sont généralement plus lents à exécuter car plus de choses doivent être configurées.

Si les tests d'intégration échouent, trouver le problème est un peu plus difficile car la plage de défaillance est plus grande.

Ils sont également plus difficiles à écrire et à maintenir, principalement parce qu'ils nécessitent des mocks plus avancés et une portée de test accrue.

### 3. Tests de bout en bout

Enfin, les tests E2E se concentrent sur les flux, des plus simples aux plus complexes. Ils peuvent être considérés comme un test d'intégration multi-étapes.

Ces tests sont les plus lents à exécuter car ils impliquent la construction, le déploiement, le lancement d'un navigateur et l'exécution d'actions autour de l'application.

Si les tests E2E échouent, trouver le problème est souvent difficile car la plage de défaillance est maintenant étendue à l'ensemble de l'application. En gros, tout pourrait avoir cassé le long du chemin.

Ils sont de loin le type de tests le plus difficile à écrire et à maintenir (parmi les trois types considérés ici) en raison de l'énorme portée des tests et parce qu'ils impliquent l'ensemble de l'application.

Espérons que vous pouvez maintenant voir pourquoi la pyramide des tests a été conçue de cette manière. De bas en haut, chaque couche de test représente une diminution de la **vitesse** et une augmentation de la **portée, de la complexité** et de la **maintenance**.

C'est pourquoi une chose importante à retenir est que le test E2E ne peut pas remplacer d'autres méthodes – il est destiné à les étendre. Le but du test E2E est bien défini, et les tests ne doivent pas dépasser cette limite.

Idéalement, les tests devraient attraper les bugs aussi près que possible de la racine de la pyramide. Le test E2E est là pour valider les boutons, les formulaires, les changements, les liens, les processus externes, et généralement le fonctionnement d'un flux de travail entier sans problèmes.

## Test avec code vs test sans code

En général, il existe deux types de tests : les tests manuels et les tests automatisés. Cela signifie que nous effectuons les tests soit manuellement, soit en utilisant des scripts.

La deuxième méthode est la plus couramment utilisée. Mais le test automatisé peut être encore séparé en deux parties : **test avec code** et **test sans code**.

### Test avec code

Lorsque vous testez avec du code, vous utilisez des frameworks qui peuvent automatiser les navigateurs. L'un des outils les plus populaires est [Selenium](https://www.selenium.dev/), mais je préfère et utilise souvent [Cypress](https://www.cypress.io/) dans mes projets (uniquement pour JavaScript). Pourtant, ils fonctionnent principalement de la même manière.

En gros, avec des outils comme celui-ci, vous simulez des navigateurs web et leur donnez des instructions pour effectuer différentes actions sur votre application cible. Après cela, vous testez pour voir si votre application a répondu aux actions correspondantes.

Voici un exemple simple de simulation tiré de la documentation de Cypress pour vous aider à mieux comprendre comment cet outil fonctionne :

![Image](https://paper-attachments.dropbox.com/s_EA8BC9D2CF83E24BF57AB3EC5A73F372F5ADA41ABD62DE1DA2D26BB58DE3CD82_1603530185695_carbon.png)
_[Code brut de la documentation](https://docs.cypress.io/guides/getting-started/writing-your-first-test.html#Step-4-Make-an-assertion)_

Voyons ce qui se passe :

1. Étant donné qu'un utilisateur visite https://example.cypress.io
2. Lorsqu'il clique sur le lien étiqueté type, alors l'URL devrait inclure /commands/actions
3. S'il tape "[fake@email.com](mailto:fake@email.com)" dans l'entrée .action-email, alors l'entrée .action-email a "[fake@email.com](mailto:fake@email.com)" comme valeur

### Test sans code

Dans une situation de test **sans code**, vous utilisez des frameworks alimentés par l'intelligence artificielle qui enregistrent vos actions. Basé sur certaines informations supplémentaires, ils testent si l'application cible répond comme prévu.

Ces outils ressemblent souvent à des plateformes low-code, où vous faites glisser et déposez différents panneaux. L'un de ces outils est [TestCraft](https://www.testcraft.io/), qui est une solution **sans code** basée sur Selenium.

![Image](https://paper-attachments.dropbox.com/s_EA8BC9D2CF83E24BF57AB3EC5A73F372F5ADA41ABD62DE1DA2D26BB58DE3CD82_1603531312592_ezgif-3-e3440d13da31.gif)

En raison des fonctionnalités qu'ils offrent (comme la création, la maintenance et l'exécution de tests avec des options simples de glisser-déposer et sans connaissance en codage), ce type d'outil est généralement plus cher. Mais je voulais mentionner [TestCraft](https://www.perfecto.io/blog) car ils ont un plan gratuit qui inclut essentiellement tout.

Maintenant, bien sûr, une solution sans code peut être un avantage si vous voulez de la vitesse et de l'argent, mais ces solutions sont encore nouvelles. Par conséquent, elles ne peuvent pas encore atteindre la complexité des suites de tests que vous pouvez développer en écrivant le code vous-même.

Si l'application cible a des flux très complexes qui incluent plusieurs parties mobiles, alors une situation de test classique est la voie à suivre. Mais si vous avez des flux simples, alors une solution sans code est ce dont vous avez besoin.

## Conclusion

Écrire des tests est une nécessité pour toute application. Si vous suivez des principes solides et écrivez vos suites de tests selon leur type, alors vos tests ne feront qu'améliorer votre application et seront également assez faciles à écrire et à maintenir.

Vous ne devriez utiliser les tests de bout en bout, comme tout autre test, que de la manière dont ils sont censés être utilisés. Ils sont créés pour tester le flux de travail de l'application de bout en bout en reproduisant des scénarios d'utilisateurs réels. Mais en fin de compte, rappelez-vous que la plupart des bugs devraient être attrapés aussi près que possible de la racine.