---
title: Comment construire des applications Ruby on Rails solides avec le BDD
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-25T02:15:37.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-rock-solid-ruby-on-rails-apps-with-bdd-735de9319cc6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*C238nEDrqoXjgjjASFwfRg.png
tags:
- name: General Programming
  slug: programming
- name: Ruby on Rails
  slug: ruby-on-rails
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment construire des applications Ruby on Rails solides avec le BDD
seo_desc: 'By Marko Anastasov

  Learn best practices for building sustainable web apps with behavior-driven development.



  _“Why do we fall sir? So that we can learn to pick ourselves up.”_—Alfred (Michael
  Cane) in Batman Begins


  I built my first Rails app ten ye...'
---

Par Marko Anastasov

#### Apprenez les meilleures pratiques pour construire des applications web durables avec le développement piloté par le comportement.

![Image](https://cdn-media-1.freecodecamp.org/images/w-cGH0pyQD50cfQWGoB0EBzDfkdm91xuVbiZ)

> _"Pourquoi tombons-nous, monsieur ? Pour apprendre à nous relever."_
> — Alfred (Michael Cane) dans Batman Begins

J'ai construit ma première application Rails il y a dix ans. J'ai essayé toutes les approches, et s'il y a une chose dont je suis certain, c'est que je ne peux pas travailler sans écrire de tests. Et écrire les tests en premier est ce qui m'a le plus aidé à améliorer mes compétences en programmation.

C'est assez simple. Nous voulons nous sentir et être aussi productifs le jour 1000 que le jour 1 du projet. Nous voulons être rapides. Pour cela, nous avons besoin d'un code propre.

Nous ne pouvons pas tout faire correctement dès le premier essai, donc nous devons refactoriser. Cependant, nous ne pouvons pas refactoriser sous une peur constante de casser des choses et d'envoyer des bugs en production sans le savoir. Nous avons besoin de confiance pour détecter et corriger les problèmes dès que nous cassons le code.

D'où vient la confiance ? La suite de tests automatisés nous donne cette confiance. La confiance que nous pouvons changer, supprimer ou ajouter du nouveau code, et qu'aucun problème majeur ne se produira tant que nos tests passent.

Donc, si les tests sont la fondation, écrivons-les en premier. Faites cela pendant un certain temps, et vous remarquerez à quel point votre code et vos tests deviennent propres et efficaces.

### Comprendre le point de vue "comportement"

Lors de l'application du développement piloté par les tests (TDD), les développeurs peuvent facilement tomber dans le piège d'utiliser des tests unitaires pour tester ce qu'un objet ou une méthode **est**, plutôt que ce qu'il **fait**, ce qui est beaucoup plus utile.

Un exemple serait d'écrire un test qui vérifie qu'une collection de commentaires est spécifiquement un tableau, et non l'une de ses caractéristiques uniques, comme être triée par temps. Dans la plupart des cas, cela ne devrait pas importer si nous changeons l'implémentation de cette collection pour retourner une classe énumérable personnalisée. Plus généralement :

> Changer l'implémentation d'un objet ne devrait pas casser sa suite de tests, tant que ce que l'objet fait reste le même.

Le **développement piloté par le comportement** (BDD) met l'accent sur le comportement — ce qu'une chose fait — à tous les niveaux de développement.

Initialement, le mot "comportement" peut sembler étrange. Une autre façon de le formuler est de penser aux descriptions. Nous pouvons décrire chaque méthode de bas niveau, objet, bouton ou écran à une autre personne — et ce que nous allons décrire est exactement ce qu'est un comportement. Adopter cette approche change la façon dont nous abordons l'écriture de code.

#### Le modèle de communication "Étant donné / Quand / Alors"

La plupart des problèmes en développement logiciel sont des problèmes de communication. Par exemple, le chef de produit ne parvient pas à décrire tous les cas d'utilisation d'une fonctionnalité proposée. Les développeurs comprennent mal la portée d'une fonctionnalité. L'équipe produit n'a pas de protocole pour vérifier si une fonctionnalité est terminée.

Le BDD simplifie le langage que nous utilisons pour décrire les scénarios dans lesquels le logiciel doit être utilisé :

> _*Étant donné*_ un certain contexte ou état du monde,

> *_Quand*_ quelque chose se produit,

> *_Alors*_ nous attendons un certain résultat.

_Étant donné, Quand, Alors_ sont des mots simples que nous pouvons utiliser pour décrire une fonctionnalité complexe, un objet de code ou une seule méthode également bien. C'est un modèle que tous les membres de l'équipe dans divers rôles peuvent comprendre.

Ces expressions sont également intégrées dans de nombreux frameworks de test, tels que [Cucumber](https://cucumber.io). Une formulation claire du problème et de la solution que nous devons implémenter nous aide à écrire un meilleur code.

### Aperçu des outils BDD pour Rails

[Ruby on Rails](http://rubyonrails.org) a été le premier framework web à être livré avec un framework de test intégré. Cela a servi de tremplin pour de nouvelles avancées dans le domaine.

En même temps, l'expressivité de Ruby et le gain de productivité dans le développement d'applications web avec Rails ont attiré de nombreux ingénieurs expérimentés et de haut niveau dans la communauté dès le début.

Lorsque vous générez une nouvelle application Rails avec les options par défaut, elle prépare le terrain pour les tests en utilisant `test/unit`, une bibliothèque de test qui vient avec Ruby. Cependant, il existe des outils qui rendent le BDD plus facile à appliquer. Je recommande d'utiliser [RSpec](http://rspec.info/) comme principale bibliothèque de test et [Cucumber](https://cukes.info/) pour écrire des tests d'acceptation de haut niveau.

#### RSpec

RSpec est une bibliothèque de test BDD populaire pour Ruby. Les tests écrits en utilisant RSpec — appelés **specs** — sont des exemples exécutables du comportement attendu d'un morceau de code dans un contexte spécifié. Cela est beaucoup plus facile à comprendre en lisant le code suivant :

```
describe ShoppingCart do  context "lorsqu'il est créé pour la première fois" do    it "est vide" do      shopping_cart = ShoppingCart.new      expect(shopping_cart).to be_empty    end  endend
```

Les specs bien écrits sont faciles à lire, et par conséquent, à comprendre. Essayez de lire le snippet de code ci-dessus à voix haute. Nous **décrivons** un panier d'achat, en disant que, étant donné un contexte vide, lorsque nous créons un nouveau panier d'achat, nous `expect(shopping_cart).to be_empty`.

L'exécution de cette spec produit une sortie qui ressemble à une spécification :

```
ShoppingCart  lorsqu'il est créé pour la première fois    est vide
```

Nous pourrions utiliser RSpec pour spécifier un système entier, cependant nous pouvons également utiliser un outil qui nous aide à écrire et à communiquer encore plus naturellement.

#### Cucumber

Comme je l'ai expliqué dans le premier chapitre de ce guide, nous voulons piloter par les tests la phase d'analyse de chaque nouvelle fonctionnalité. Pour cela, nous avons besoin de **tests d'acceptation client** pour piloter le développement du code qui implémentera réellement la fonctionnalité.

Si vous êtes un développeur travaillant dans une organisation suffisamment complexe, vous pouvez vouloir que quelqu'un d'autre, comme un client ou un chef de produit, écrive des tests d'acceptation pour vous (avertissement : je n'ai jamais travaillé dans un tel environnement). Dans la plupart des cas, le développeur les écrit. C'est une bonne pratique, car cela nous aide à mieux comprendre ce que nous devons construire. Cucumber fournit le langage et le format pour le faire.

Cucumber lit des descriptions en texte brut des fonctionnalités de l'application, organisées en **scénarios**. Chaque étape du scénario est implémentée en utilisant du code concret, et il automatise l'interaction avec votre application du point de vue de l'utilisateur. Par exemple :

```
Fonctionnalité: Lecture d'articles
```

```
Scénario: Commenter un article  Étant donné que je suis connecté  Et que je lis un article avec "2" commentaires  Quand je réponds au dernier commentaire  Alors l'article devrait avoir "3" commentaires  Et je devrais être abonné aux commentaires suivants
```

Si cela était une application web, le scénario ci-dessus pourrait démarrer automatiquement une instance de test de l'application, l'ouvrir dans un navigateur web, effectuer des étapes comme le ferait n'importe quel utilisateur, puis vérifier si certaines attentes ont été satisfaites.

### Le cycle BDD dans Rails

En pratique, le BDD implique une approche **de l'extérieur vers l'intérieur**. Nous commençons par un test d'acceptation, puis nous écrivons du code dans les vues, et nous travaillons jusqu'aux modèles. Cette approche nous aide à découvrir tous les nouveaux objets ou variables dont nous pourrions avoir besoin pour implémenter efficacement notre fonctionnalité dès le début, et à prendre les bonnes décisions de conception en fonction de cela.

Le cycle BDD dans Rails se compose des étapes suivantes :

1. **Commencez par un nouveau scénario Cucumber**. Avant de l'écrire, assurez-vous d'analyser et de comprendre le problème. À ce stade, vous devez savoir comment l'interface utilisateur permet à un utilisateur d'effectuer une tâche. Ne vous inquiétez pas de l'implémentation des étapes du scénario.
2. **Exécutez le scénario et regardez-le échouer**. Cela vous indiquera quelles étapes échouent ou sont en attente d'implémentation. Au début, la plupart de vos étapes seront en attente (non définies).
3. **Écrivez une définition de la première spec échouée ou en attente**. Exécutez le scénario et regardez-le échouer.
4. **Pilotez par les tests l'implémentation d'une vue Rails** en utilisant le cycle rouge-vert-refactor avec RSpec. Vous découvrirez les variables d'instance, les contrôleurs et les actions de contrôleur dont la vue aura besoin pour faire son travail. C'est également la seule phase qui s'est avérée être optionnelle en pratique. Une approche alternative consiste à simplement préparer les vues et les contrôleurs avant de passer à l'étape suivante.
5. **Pilotez par les tests le contrôleur** en utilisant le cycle rouge-vert-refactor avec RSpec. Assurez-vous que les variables d'instance sont assignées et que les actions répondent correctement. Les contrôleurs sont généralement pilotés avec une approche de mocking. Une fois le contrôleur pris en charge, vous saurez ce que les modèles ou vos objets de domaine doivent faire.
6. **Pilotez par les tests les objets de domaine** en utilisant le même cycle rouge-vert-refactor avec RSpec. Assurez-vous qu'ils fournissent les méthodes nécessaires au contrôleur et à la vue. Si vous travaillez sur une nouvelle fonctionnalité pour laquelle un modèle n'existe pas encore, vous devez maintenant générer le modèle et les migrations de base de données correspondantes. À ce stade, vous saurez exactement ce que vous devez faire.
7. Une fois que vous avez implémenté tous les objets et méthodes dont vous avez besoin et que les specs correspondantes passent, **exécutez le scénario Cucumber que vous avez commencé pour vous assurer que l'étape est satisfaite**.

![Image](https://cdn-media-1.freecodecamp.org/images/8WeEWJUk4SLlPc0tC5VrxooSOTwqSZaRHvr0)
_Le cycle BDD dans le développement web Ruby on Rails_

Une fois que la première étape du scénario passe, passez à la suivante et suivez les mêmes étapes. Une fois que votre scénario entier a été implémenté — le scénario passe, ainsi que toutes les specs sous-jacentes — prenez un moment pour réfléchir s'il y a quelque chose que vous pouvez **refactoriser** davantage.

Une fois que vous êtes sûr d'avoir complété le scénario, passez au suivant ou montrez votre travail aux autres. Si vous travaillez en équipe, **créez une pull request** ou une demande équivalente pour une revue de code. L'ouverture d'une pull request devrait automatiquement déclencher une construction d'**intégration continue** ([continuous integration](https://semaphoreci.com/blog/2017/03/02/what-is-proper-continuous-integration.html)). Lorsque vous n'avez plus de scénarios liés, montrez votre travail à votre chef de projet ou à votre client, en leur demandant de vérifier que vous avez construit la bonne chose en déployant une branche de fonctionnalité sur un serveur de staging.

Cet article est adapté de [**Rails Testing Handbook**](https://semaphoreci.com/ebooks/rails-testing-handbook), un ebook gratuit publié par [Semaphore](https://semaphoreci.com). Si vous êtes arrivé jusqu'ici et que vous souhaitez voir des exemples pratiques d'écriture de code piloté par le comportement, [téléchargez le livre](https://semaphoreci.com/ebooks/rails-testing-handbook) et faites-moi savoir ce que vous en pensez. Merci !