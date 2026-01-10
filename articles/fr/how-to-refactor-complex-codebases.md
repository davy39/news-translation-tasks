---
title: Comment refactoriser des bases de code complexes – Un guide pratique pour les
  développeurs
subtitle: ''
author: Ankur Tyagi
co_authors: []
series: null
date: '2025-05-21T15:47:44.750Z'
originalURL: https://freecodecamp.org/news/how-to-refactor-complex-codebases
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1747835131515/f6ea465a-9b14-4918-8943-87ec225b19b3.png
tags:
- name: Web Development
  slug: web-development
- name: webdev
  slug: webdev
- name: software development
  slug: software-development
- name: General Programming
  slug: programming
- name: code review
  slug: code-review
- name: refactoring
  slug: refactoring
seo_title: Comment refactoriser des bases de code complexes – Un guide pratique pour
  les développeurs
seo_desc: 'Developers often see refactoring as a secondary concern that they can delay
  indefinitely because it doesn’t immediately contribute to revenue or feature development.

  And managers frequently view refactoring as "not a business need" until it boils
  ove...'
---

Les développeurs considèrent souvent le refactoring comme une préoccupation secondaire qu'ils peuvent reporter indéfiniment car il ne contribue pas immédiatement aux revenus ou au développement de nouvelles fonctionnalités.

Et les managers voient fréquemment le refactoring comme "pas un besoin métier" jusqu'à ce que la situation devienne ingérable et devienne le besoin métier le plus significatif possible.

> *"Oh, notre logiciel fonctionne d'une manière ou d'une autre. Nous ne pouvons pas implémenter de nouveaux changements. Et oh, tout le monde démissionne parce que le travail est misérable."*

Dans cet article, je vais vous guider à travers les étapes que j'utilise pour refactoriser une base de code complexe. Nous parlerons de la définition d'objectifs, de l'écriture de tests, de la division des monolithes en modules plus petits, de la vérification des changements, de la garantie que les fonctionnalités existantes fonctionnent toujours, et du suivi des performances. Je vous montrerai également comment accélérer les revues en utilisant des outils d'IA.

En suivant ces étapes, vous pouvez transformer un code complexe et fragile en une base de code propre et fiable que votre équipe peut maîtriser.

![code-refactoring](https://lh7-rt.googleusercontent.com/docsz/AD_4nXccvZ3sehF8oGifjnapnY9AUcPde9aKy9t_YEUeL8M2s3dcwxFq_bJLCSp_S02fIvfbwzpZfkz7e-2JQpXpzcdqELqs80EjkLLRpz0Uat6q9_RcRM5VQbjLoUxA2GlaqyeolsKGeA?key=nBTgfzmVkL2-N7DBMJ6e6gyk align="left")

## Le problème de la dette technique

À mesure que les projets grandissent et évoluent, la [dette technique](https://en.wikipedia.org/wiki/Technical_debt) augmente. Le code qui était autrefois fonctionnel et gérable se transforme en un désordre ingérable, où même de petits changements deviennent risqués et chronophages.

Malgré le besoin évident de nettoyage, le refactoring est rarement priorisé car il y a toujours quelque chose de plus urgent : de nouvelles fonctionnalités, des corrections de bugs et des demandes clients.

J'ai eu des conversations avec des ingénieurs, dont beaucoup travaillent sur des logiciels d'entreprise et sont pleinement conscients des odeurs de code et des incohérences de leur base de code. Ils n'aiment pas la situation mais se sentent impuissants à la changer.

Alors, comment passer d'une culture d'écriture pour la pure fonctionnalité à une culture qui valorise la maintenabilité, surtout pour les bases de code complexes ?

Il est généralement une erreur d'arrêter complètement le développement de nouvelles fonctionnalités pour une longue période de refactoring (sauf peut-être en cas d'urgence). Les besoins métiers existent toujours, et tout mettre en pause peut créer des tensions et des opportunités perdues. Il est préférable de trouver un équilibre pour continuer à livrer de la valeur aux utilisateurs tout en nettoyant sous le capot.

![Uncle-bob-take-on-refactoring](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeZx-XKCA2DC6kQQe2-4NU07wKEm0_VZ4kqEjbF6u2vy2paRigdNRUGjr-_AoE6ueNjCxNjnB-mI7uroXFhJ0nFfvWzwYq2VUMsdsPhXu4KvGYSZcUN0nFmKg8U8WzgGJQAgKtUaw?key=nBTgfzmVkL2-N7DBMJ6e6gyk align="left")

Bien qu'il n'existe pas de solution universelle, une approche structurée peut aider les équipes à introduire des pratiques de refactoring durables, même dans des environnements où la direction est réticente. Explorons comment cela fonctionne.

## **Table des matières :**

* [Qu'est-ce que le refactoring ?](#heading-quest-ce-que-le-refactoring)
  
* [Préparation au refactoring](#heading-preparation-au-refactoring)
  
  * [Obtenir l'adhésion de la direction](#heading-obtenir-ladhesion-de-la-direction)
    
  * [Assurer un filet de sécurité avec des tests automatisés](#heading-assurer-un-filet-de-securite-avec-des-tests-automatises)
    
  * [Identifier les zones à haut risque](#heading-identifier-les-zones-a-haut-risque)
    
  * [Définir des objectifs clairs de refactoring](#heading-definir-des-objectifs-clairs-de-refactoring)
    
* [Techniques de refactoring des bases de code complexes](#heading-techniques-de-refactoring-des-bases-de-code-complexes)
  
  * [1. Identifier et isoler les zones problématiques](#heading-1-identifier-et-isoler-les-zones-problematiques)
    
  * [2. Refactoring incrémental vs. Big Bang](#heading-2-refactoring-incremental-vs-big-bang)
    
  * [3. Décomposer le code monolithique](#heading-3-decomposer-le-code-monolithique)
    
  * [4. Assurer la compatibilité ascendante](#heading-4-assurer-la-compatibilite-ascendante)
    
  * [5. Gérer les dépendances et le couplage serré](#heading-5-gerer-les-dependances-et-le-couplage-serre)
    
  * [6. Stratégies de test (Refactoring en toute confiance)](#heading-6-strategies-de-test-refactoring-en-toute-confiance)
    
  * [7. Refactoring sans casser les performances](#heading-7-refactoring-sans-casser-les-performances)
    
  * [8. Automatiser les revues de code avec des outils d'IA](#heading-8-automatiser-les-revues-de-code-avec-des-outils-dia)
    
  * [Résumé](#heading-resume)
    

## **Qu'est-ce que le refactoring ?**

Beaucoup de gens utilisent trop souvent le mot "refactor" lorsqu'ils veulent dire une réécriture ciblée.

Comme l'a dit Martin Fowler :

> *"Le refactoring est une technique contrôlée pour améliorer la conception d'une base de code existante. Son essence est d'appliquer une série de petites transformations préservant le comportement... Cependant, l'effet cumulatif... est assez significatif."*

En pratique, cela signifie polir continuellement le code pour réduire la complexité et la dette technique.

Alors que le développement logiciel traditionnel suit une approche linéaire de conception d'abord et de codage ensuite, les projets du monde réel évoluent souvent de manière à entraîner une décadence structurelle. Le refactoring contre cela en affinant continuellement la base de code, transformant des implémentations désorganisées ou inefficaces en solutions bien structurées et maintenables.

Une réécriture ciblée est une révision ciblée d'un aspect spécifique d'une application, affectant souvent plusieurs parties de la base de code. Elle comporte plus de risques que le refactoring mais reste contrôlée et contenue.

## Préparation au refactoring

Même l'effort de refactoring le plus qualifié peut stagner sans une préparation adéquate. Avant de commencer à déplacer du code, il est crucial de poser une base qui gardera votre travail organisé et votre équipe sur la même longueur d'onde.

![martin-fowler-on-refactoring](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcr3hNpzC9XPUVnG6d7uHuC977aYrG2VVOH-8E4WhzM5Rfz3vzPDUPTwJChrK0l7WUK8BLTzYr5-295_27ARWQvcmjufXOk68Bg8szUjEq3IFVCDO0XfTSRFy1LaxqyjvjVDNddsw?key=nBTgfzmVkL2-N7DBMJ6e6gyk align="left")

Voici quelques étapes que vous pouvez suivre pour garantir le succès de vos efforts de refactoring.

### Obtenir l'adhésion de la direction

Comme je l'ai déjà discuté, obtenir du temps pour le refactoring peut être difficile dans les organisations axées sur les fonctionnalités. Souvent, la direction acceptera l'investissement dans le refactoring si vous pouvez le lier à des résultats métiers, un temps de mise sur le marché plus rapide, moins de pannes (ce qui se traduit par des clients plus heureux), et la capacité à entreprendre de nouvelles initiatives.

Rendez ces connexions explicites. Par exemple, vous pourriez dire :

> *"Si nous refactorisons notre moteur de reporting maintenant, cela rendra possible l'ajout du module d'analyse le trimestre prochain, ce qui débloque un nouveau flux de revenus."*

Ou utilisez des données :

> *"Nous avons passé 30 % de notre dernier sprint à corriger des bugs dans le module Y. Après avoir refactorisé Y, nous nous attendons à ce que cela diminue significativement, libérant du temps pour de nouvelles fonctionnalités."*

Les arguments axés sur les affaires aident à justifier l'équilibre.

### Assurer un filet de sécurité avec des tests automatisés

Lors du refactoring, les tests sont votre filet de sécurité. Avant de modifier un composant, écrivez des tests de caractérisation autour de celui-ci s'ils n'existent pas.

```python
# exemple : test de caractérisation pour une fonction héritée
def legacy_calculate_discount(price, rate):
    # ... logique complexe que vous ne comprenez pas encore complètement ...
    return price * (1 - rate/100) if rate < 100 else 0

def test_legacy_calculate_discount():
    # capture du comportement existant
    assert legacy_calculate_discount(100, 10) == 90
    assert legacy_calculate_discount(50, 200) == 0
```

Ces tests capturent le comportement actuel, donc vous saurez si vous le changez accidentellement. Les tests unitaires, les tests d'intégration et les tests e2e valident tous que le refactoring n'a rien cassé.

![automated-testing-is-imp-for-refactoring](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfWfke-9FxoQIPFwRWVoIWrYN7L40mEmhpdAUkcBm34mwzXJ0R8jXKH8rZ0HjAghAtQ-v6dTUYYvK0T8_QBgyfeab-7R50pnB6BgdDm9L4PkFwvwGlUYTHNo21f37fxMZYt3xeY?key=nBTgfzmVkL2-N7DBMJ6e6gyk align="left")

Il est souvent utile d'investir du temps dans la mise en place d'un pipeline d'intégration continue afin que chaque changement déclenche des tests automatisés. Cela donne un retour rapide et la confiance que vous n'introduisez pas de régressions. Des tests robustes et CI/CD vous permettent de vous déplacer plus rapidement et de refactoriser en toute sérénité.

```powershell
# .github/workflows/ci.yml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with: python-version: '3.10'
      - run: pip install -r requirements.txt
      - run: pytest --maxfail=1 --disable-warnings -q
```

### Identifier les zones à haut risque

La première étape consiste à déterminer ce qu'il faut refactoriser. Les zones à haut risque sont des parties du code susceptibles de causer des bugs ou de ralentir le développement. Les signes courants incluent des méthodes longues, des classes volumineuses, du code dupliqué et une logique conditionnelle complexe.

De telles "odeurs de code" indiquent souvent des problèmes de conception plus profonds. Des outils comme l'analyse statique peuvent automatiquement signaler ces problèmes.

![SonarQube-dashboard](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfS4aFy2hyRSq3UmgB2gQ8NN_-yUksNXcSavTtpnL8KIiWpGGidCSCstLKANZGOjJLqEF69wp-xjMGH6jrjurSaFtUIMS09vUaDgJ6vGtyabP-4QC5ISmT_cMvaaw6c2KlyVa1CKQ?key=nBTgfzmVkL2-N7DBMJ6e6gyk align="left")

Par exemple, SonarQube marquera les odeurs de code (comme une complexité élevée ou des méthodes longues) qui augmentent la dette technique. En utilisant SonarQube ou des outils similaires, vous pouvez générer des rapports sur la complexité du code (par exemple, des métriques de complexité cyclomatique) et trouver les points chauds dans la base de code qui nécessitent plus d'attention.

### Définir des objectifs clairs de refactoring

Avant de refactoriser le code, définissez l'objectif.

Les objectifs doivent être spécifiques et mesurables. Par exemple, vous pourriez viser à réduire la taille d'une classe ou la complexité cyclomatique d'une fonction d'un certain montant ou à augmenter la couverture des tests unitaires de 60 % à 90 %.

Chaque objectif est lié à un résultat mesurable : des méthodes plus courtes, moins d'instructions if ou des classes avec une seule responsabilité, une exécution plus rapide pour le traitement des commandes, une couverture de test plus élevée et aucun code inutilisé. Ces cibles guideront notre plan de refactoring et nous permettront de vérifier quand nous aurons réussi.

**Astuce :** Écrivez vos objectifs de refactoring et partagez-les avec votre équipe. Cela définit les attentes que vous n'ajoutez pas de nouvelles fonctionnalités dans cet effort, juste en rendant le code plus propre et plus robuste. Cela aide également à justifier le temps passé en montrant les avantages (comme des ajouts futurs plus simples et moins de bugs).

## Techniques de refactoring des bases de code complexes

### 1. Identifier et isoler les zones problématiques

Il peut être écrasant de décider par où commencer le refactoring d'une grande base de code. Toutes les parties du code n'ont pas besoin de refactoring – certaines zones sont délicates ou rarement touchées.

Les efforts de refactoring les plus impactants ciblent généralement les "zones problématiques" : les parties de la base de code qui sont trop complexes, sujettes aux erreurs ou qui agissent comme des goulots d'étranglement pour le développement et les performances. Identifier ces zones est une première étape cruciale.

### Techniques pour trouver les points chauds

#### Connaissance de l'équipe et frustration des développeurs

Ne sous-estimez pas la valeur des informations anecdotiques de l'équipe. Quelles parties du code les développeurs redoutent-ils de travailler ? Souvent, les instincts de l'équipe pointent vers des zones difficiles à comprendre ou à modifier (par exemple, "le module de comptabilité est une boîte noire, nous détestons le toucher"). Ces zones pourraient être améliorées.

Selon mon expérience, demander simplement : "Si vous aviez une baguette magique, quelle partie du code réécririez-vous ?" donne des réponses très perspicaces.

#### Métriques de complexité du code

Utilisez des outils d'analyse statique pour mesurer la complexité cyclomatique, la duplication de code, les grandes fonctions/classes, etc. Les fichiers ou modules avec des nombres de complexité extrêmement élevés ou des milliers de lignes sont de bons candidats pour un examen approfondi. Mais la complexité statique seule ne raconte pas toute l'histoire – un fichier peut être laid mais rarement touché.

![SonarQube](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc07SWwlu4GxU6AwoXQEHyyEcQY-6YMOEPr7b7Quhk5UvLD7qx9XyZla2SzP32eGFoYY_Xy-SYZQ9mOMX7Mxeq1YCnFXQxudsMNbvak9CLZfSOeRIvdll_pLW56sAmvRcPZMk36Rg?key=nBTgfzmVkL2-N7DBMJ6e6gyk align="left")

#### Fréquence des changements (Churn)

Examinez l'historique du contrôle de version pour voir quels fichiers sont souvent modifiés, en particulier ceux associés à des corrections de bugs ou à des incidents.

#### Analyse des points chauds

Une approche robuste combine la complexité et la fréquence des changements pour trouver des "points chauds". Par exemple, un outil ou une technique traçant les modules par leur complexité et la fréquence à laquelle ils changent peut mettre en évidence les zones problématiques. CodeScene (un outil d'analyse de code) a popularisé cela : les *points chauds* sont des parties du code qui sont hautement complexes et fréquemment modifiées, indiquant des zones où "rembourser la dette a un impact réel".

Si un module est un désordre et que les développeurs y travaillent chaque semaine, l'amélioration de ce module donnera probablement des bénéfices disproportionnés (moins de bugs, des ajouts plus rapides).

![code-health-dashboard](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdJkGfbDK6UFDN9hqzeyCMBWmajADhAMJwzSouyMNz_63o9SRNfOly9AP_XiY2jqfi02fHSIFkMBCfstkjJfkxVB-NaHCSit0xssTYfztZ2BRQZmqYr_lTc3R750-1-lrJi7eeViQ?key=nBTgfzmVkL2-N7DBMJ6e6gyk align="left")

#### Goulots d'étranglement de performance et plantages

Certaines parties de la base de code deviennent des cibles pour le refactoring car elles causent des problèmes de performance fréquents ou des pannes. Par exemple, si un service ou un travail spécifique plante souvent ou ne peut pas suivre la charge, vous devrez peut-être le refactoriser pour la stabilité.

### Comment isoler les zones problématiques

Une fois que vous avez identifié un point chaud ou une zone problématique, le prochain défi est de l'isoler pour pouvoir la refactoriser en toute sécurité. Dans un système complexe, rien ne vit en isolation complète. Ce module problématique interagit probablement avec de nombreux autres.

Voici des stratégies pour l'isoler et le traiter :

#### Rompre les dépendances (Créer des coutures)

Michael Feathers (dans *Working Effectively with Legacy Code*) a introduit le concept de "coutures" – des endroits où vous pouvez couper dans une base de code pour isoler une partie pour les tests ou le refactoring. Cela peut signifier introduire une interface ou une abstraction entre les composants pour que vous puissiez travailler sur un côté indépendamment.

Par exemple, supposons que PaymentService est étroitement couplé à StripeGateway, avec des appels directs dispersés dans tout le code.

```python
# payment_service.py

def charge_customer(order_id, amount):
    # Dépendance codée en dur à Stripe
    stripe = StripeGateway()
    stripe.charge(order_id, amount)
```

Pour isoler et refactoriser la logique de paiement en toute sécurité, vous pouvez introduire une interface `PaymentProcessor` et faire en sorte que `PaymentService` dépende de cette interface à la place. Ensuite, créez un adaptateur comme StripeAdapter qui implémente PaymentProcessor et délègue à la logique Stripe existante.

De cette façon, vous pouvez refactoriser ou même remplacer l'intégration Stripe derrière le StripeAdapter sans impacter `PaymentService` ou tout autre module qui l'utilise. Tant que l'interface `PaymentProcessor` est respectée, le reste du système reste inchangé.

```python
# interfaces.py

class PaymentProcessor:
    def charge(self, order_id, amount):
        raise NotImplementedError


# stripe_adapter.py

class StripeAdapter(PaymentProcessor):
    def charge(self, order_id, amount):
        # Utilise toujours Stripe en interne
        stripe = StripeGateway()
        stripe.charge(order_id, amount)


# payment_service.py (Refactorisé)

class PaymentService:
    def __init__(self, processor: PaymentProcessor):
        self.processor = processor

    def charge_customer(self, order_id, amount):
        self.processor.charge(order_id, amount)
```

#### "Branch-by-abstraction"

Cette technique est liée à la précédente et est souvent utilisée dans la livraison continue. L'idée est d'ajouter une couche d'abstraction (comme une interface ou un proxy) devant l'ancien code, d'avoir à la fois les implémentations de l'ancien et du nouveau code derrière, puis de déplacer progressivement l'utilisation de l'ancien vers le nouveau. Pendant un certain temps, vous pourriez avoir un état temporaire où les deux versions coexistent (peut-être basculées par une configuration ou un drapeau de fonctionnalité).

![Branch-by-abstraction](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcaFoXSHVYTBz_1DOsucPkvwGQwfo9qrvhPYvvjYOXQsLIh2MCTfseB1g9SOfijpdKMwcwmK4lfPWcyhn4vf5gaFwdliKUZUGDOcQVJ0qupRLjvnhFrSm5LZfe8OoqZtZkHkj9IXw?key=nBTgfzmVkL2-N7DBMJ6e6gyk align="left")

Cela est similaire à la manière dont le modèle de figuier étrangleur fonctionne au niveau architectural. C'est un peu de travail supplémentaire (puisque vous maintenez deux chemins pendant un certain temps), mais cela vous permet de migrer la fonctionnalité et de revenir en arrière si nécessaire de manière incrémentielle.

Visez à identifier les 20 % du code causant 80 % des problèmes. Concentrez votre énergie de refactoring là pour un impact maximal. Lorsque vous le faites, créez un plan pour isoler cette zone via des abstractions, des interfaces, des modules ou d'autres moyens afin que vous puissiez travailler dessus avec un risque minimal d'effets secondaires. Plus vous pouvez contenir le rayon d'explosion d'un refactoring, plus vous pouvez avancer en toute confiance.

### 2. Refactoring incrémental vs. Big Bang

L'une des premières décisions stratégiques est d'aborder le refactoring de manière **incrémentale** ou d'opter pour une révision **"big bang"**. Dans la plupart des cas, une approche incrémentale est préférable, mais il existe des scénarios où des étapes de refactoring plus importantes et coordonnées sont envisagées.

**Décomposons ce que cela signifie :**

```python
# avant : une grande fonction avec plusieurs responsabilités
def process_order(order):
    validate(order)
    apply_discount(order)
    save_to_db(order)
    send_confirmation(order)
    log_metrics(order)
    update_loyalty_points(order)
    # potentiellement plus d'étapes 

# après : refactorisé de manière incrémentale en unités plus claires et plus petites
def process_order(order):
    validate(order)
    apply_discount(order)
    persist_and_notify(order)

def persist_and_notify(order):
    save_to_db(order)
    send_confirmation(order)
    log_metrics(order)
    update_loyalty_points(order)
```

#### Refactoring incrémental

Cela signifie apporter des changements petits et gérables au fil du temps plutôt que de tenter une révision massive en une seule fois. Le système doit rester fonctionnel à chaque étape (même en interne en transition). L'avantage est la mitigation des risques : chaque petit changement est moins susceptible de mal tourner, et il est plus facile de l'identifier et de le corriger si c'est le cas.

![Incremental refactoring](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdaSmnIWRE9FKNmmABBzc6Tk6KFwsj29FQ2YwyQ_kWqryheb0yUdpec51lQHg5XahoxKgCm4vv9twD849H3Yo5dn0678tuGih9Z-HfBBCfhBngs4YhpH6x2pjzqnAeDVYGohXHvDQ?key=nBTgfzmVkL2-N7DBMJ6e6gyk align="left")

La livraison incrémentale vous permet de confirmer les changements en production et facilite le diagnostic des problèmes puisque vous ne changez qu'une seule petite chose à la fois. Cela signifie également que le système continue de fonctionner pendant le refactoring, donc il y a moins de pression pour se dépêcher de "remettre le système en état de marche". Si les priorités changent, vous pouvez faire une pause après quelques incréments et avoir toujours un produit fonctionnel.

#### Refactoring Big Bang (Réécriture)

C'est l'approche "démolir et reconstruire". Vous arrêtez d'ajouter de nouvelles fonctionnalités, geler peut-être le code pendant une période, et consacrez un effort considérable à la reconception ou à la réécriture d'une partie importante (ou de la totalité) du système. L'idée est d'émerger de l'autre côté avec un système *tout neuf et propre*.

Alors, quand (si jamais) un big bang est-il justifié ? Peut-être lorsque le système existant est vraiment intenable – par exemple, une technologie obsolète qui **doit** être remplacée (comme une plateforme qui ne peut pas répondre aux nouvelles exigences de performance ou de sécurité ou un code écrit dans un langage qui n'est plus supporté). Même alors, les équipes avisées simulent souvent un big bang en le divisant en étapes ou en développant le nouveau système en parallèle.

Dans la mesure du possible, privilégiez une stratégie de refactoring incrémental. Les équipes réussissent à réaliser des transformations massives en traitant le grand refactoring comme une série de mini-refactorings sous une vision partagée.

### 3. Décomposer le code monolithique

De nombreuses bases de code complexes commencent leur vie sous la forme d'une seule application monolithique, un seul déploiement, un seul projet de code, ou un ensemble de modules étroitement couplés tous maintenus et publiés ensemble.

Avec le temps, les monolithes peuvent devenir ingérables, les builds prennent une éternité, un changement dans une zone peut affecter involontairement une autre, et les équipes peuvent être complexes à mettre à l'échelle car tout le monde se marche sur les pieds dans le même code. Un défi courant de refactoring pour les ingénieurs seniors est la modularisation ou la division d'un monolithe en morceaux plus gérables.

```python
# définir l'interface
class PaymentProcessor:
    def charge(self, amount): ...
    
# ancienne implémentation
class LegacyProcessor(PaymentProcessor):
    def charge(self, amount):
        # code original

# nouvelle implémentation derrière un drapeau de fonctionnalité
class NewProcessor(PaymentProcessor):
    def charge(self, amount):
        # code plus propre

def get_processor():
    if config.feature_new_payment:
        return NewProcessor()
    return LegacyProcessor()

# l'utilisation reste la même
processor = get_processor()
processor.charge(100)
```

#### Stratégies de modularisation.

* **Séparation des couches :** Commencez par imposer des limites logiques entre les couches. Par exemple, séparez le code de l'interface utilisateur de la logique métier et séparez la logique métier de l'accès aux données. Dans un monolithe désordonné, ces préoccupations sont souvent mélangées. En organisant le code en couches (même au sein du même dépôt), vous pouvez limiter l'effet de propagation des changements.
  
* **Modularisation basée sur le domaine :** Si votre système couvre plusieurs domaines métiers ou zones fonctionnelles, envisagez de le diviser selon ces lignes. Par exemple, un monolithe de commerce électronique pourrait être séparé en modules comme Comptes, Commandes, Produits, Livraison, etc. Chaque module pourrait devenir un sous-système ou un package. L'objectif est de minimiser les informations que ces modules doivent connaître sur les internes des autres (forte cohésion au sein des modules et API claires entre eux).
  
* **Extraction de microservices ou de services :** Ces dernières années, la tendance a été de diviser les monolithes en microservices, des services indépendants qui communiquent via des API. Cette forme de refactoring architectural peut considérablement améliorer la capacité de déploiement indépendant et la scalabilité. Mais c'est une entreprise importante avec des complexités (systèmes distribués, appels réseau, etc.). Si vous décidez de suivre cette voie, faites-le progressivement. Une méthode éprouvée est le **modèle de figuier étrangleur** mentionné précédemment : vous choisissez une pièce de fonctionnalité et la réécrivez ou l'extrayez en tant que service séparé, redirigez le trafic ou les appels vers le nouveau service. En même temps, le reste du monolithe reste intact et faites cela de manière itérative pour d'autres pièces.
  
* **Monolithe modulaire :** Tous les systèmes n'ont pas besoin de passer aux microservices. Il existe une approche appelée monolithe modulaire, qui consiste essentiellement à structurer votre application unique en modules bien définis qui communiquent via des interfaces explicites (presque comme des microservices internes mais sans la surcharge des déploiements séparés). Cela peut vous donner de nombreux avantages des microservices (frontières claires, responsabilité de développement séparée) tout en évitant la complexité opérationnelle.
  
![microservices' advantages](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfLiNAEDyOsR4G_q1oQS3jpSenci3XDJRm10Gy3picTpaO9uHwme2H3YkbJF-Jrvqq3Q-QMxGjJJwy04mqUf1a7D8IRsCDER5pHBT6GTMPRkao5EXXIFGtj4Iki15mOHmRKRLTiWw?key=nBTgfzmVkL2-N7DBMJ6e6gyk align="left")

* **Identifier les utilitaires partagés vs. les composants vraiment indépendants :** En décomposant un monolithe, certains codes sont largement partagés (comme les fonctions utilitaires ou les préoccupations transversales telles que l'authentification). Il peut être judicieux de factoriser ceux-ci en bibliothèques ou services *d'abord*, car ils seront nécessaires par les autres pièces que vous divisez.
  
Lors de la décomposition d'un monolithe, il est essentiel de maintenir la fonctionnalité pendant la transition. Des techniques comme la compatibilité ascendante (discutée ensuite) et des tests approfondis seront votre filet de sécurité.

Enfin, soyez prêt à ce que le flux de travail de l'équipe change. Si vous passez aux microservices, les équipes peuvent prendre en charge différents services, nécessitant plus de DevOps et de communication entre les équipes. Si vous gardez un monolithe modulaire, imposez des règles de propriété ou de révision du code pour empêcher les modules de s'emmêler à nouveau (par exemple, vous pourriez restreindre l'accès direct à la base de données d'un module aux tables d'un autre, etc.).

### 4. Assurer la compatibilité ascendante

Une préoccupation critique lors d'un grand refactoring est : *Nos changements vont-ils casser les contrats existants ?*

En d'autres termes, les autres systèmes, modules ou clients qui dépendent de notre code fonctionneront-ils comme prévu après notre refactoring ? La compatibilité ascendante est particulièrement importante si votre base de code fournit des API publiques (à des clients externes ou à d'autres équipes), des données persistées dans un certain format, des fichiers de configuration que les utilisateurs ont écrits, etc.

Voici quelques stratégies et considérations pour maintenir la compatibilité ascendante :

Supposons que vous avez une fonction largement utilisée comme `send_email(to, subject, body)`. Vous souhaitez refactoriser la logique interne pour prendre en charge des fonctionnalités supplémentaires comme le formatage HTML, mais vous ne voulez pas casser les appelants existants.

Au lieu de changer la signature de la fonction, vous gardez l'API publique inchangée et déléguez à une nouvelle fonction interne :

```python
# API d'origine
def send_email(to, subject, body):

 
 # envoyer le mail...

# internes refactorisés, garder la signature
def send_email(to, subject, body):

 
 sendv2(to=to, subject=subject, body=body)

def sendv2(to, subject, body, html=True):

 
 # nouvelle implémentation avec support HTML
```

La fonction interne `send_email_v2()` ajoute de nouvelles capacités comme le formatage HTML, mais l'ancien code utilisant `send_email()` fonctionne toujours sans aucune modification.

Si vous introduisez une nouvelle version améliorée comme `send_email_v2(to, subject, body, html=True)`, il est bon de :

* Marquer l'ancienne version (send\_email) comme obsolète dans la documentation.
  
* S'assurer que l'ancienne version appelle internement la nouvelle.
  
* Donner aux autres équipes le temps de migrer à leur propre rythme.
  
#### Utiliser la versioning pour les API externes

Si votre système fournit une API HTTP ou similaire à des clients externes, la voie la plus sûre pour les changements majeurs est de versionner l'API. Introduisez un endpoint d'API v2 pour la logique refactorisée, gardez v1 en fonctionnement (peut-être en appelant internement v2 ou en utilisant une couche de traduction). Les clients peuvent passer à v2 à leur propre rythme.

C'est un travail supplémentaire de maintenir deux API temporairement, mais cela empêche un changement de rupture de mécontenter les utilisateurs ou de causer des pannes. Communiquez toujours clairement les changements et fournissez des guides de migration si applicable.

#### Avoir une politique de dépréciation claire

Assurez-vous qu'il y a une politique (et une communication) autour de la durée pendant laquelle les fonctionnalités obsolètes seront supportées. Pour les API internes, peut-être qu'il s'agit d'un cycle de publication. Pour les API externes, peut-être plusieurs cycles ou jamais de suppression sans une augmentation majeure de version. Une bonne pratique est d'annoncer la dépréciation tôt.

Si vous exposez une API HTTP, envisagez d'introduire un nouvel endpoint versionné (par exemple, **/api/v2/send\_email**) et maintenez l'ancien **/api/v1/send\_email temporairement**. Internement, v1 peut appeler v2 avec des paramètres par défaut, garantissant que le comportement reste cohérent pour les clients existants.

En résumé, maintenez la compatibilité ascendante chaque fois que possible, et mettez en œuvre une politique de dépréciation claire pour tout ce que vous changez.

![Clear deprecation policy](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe3xM4som_GQrtHXI3NNR0G-4KJ-1D2YO-JbNdT75IxZ5_upcBRDnOVp7krEESiqwwtXg18pDypLq3VxDr44Hof76cs8HajOZy2w0FZ50kWmPk6Y7EwNByNLNrqAokmhmmL5sP3AA?key=nBTgfzmVkL2-N7DBMJ6e6gyk align="left")

#### Écrire des couches d'adaptation ou de compatibilité

Dans certains cas, vous pouvez écrire un adaptateur pour faire le pont entre les anciens et les nouveaux systèmes. Par exemple, supposons que vous refactorisez le modèle de données sous-jacent de votre application, mais que vous avez toujours d'anciens fichiers de configuration dans l'ancien format. Plutôt que de forcer tous ces fichiers à être réécrits immédiatement, vous pourriez écrire un petit adaptateur qui traduit l'ancien format vers le nouveau à l'exécution (ou pendant le démarrage). De cette façon, les anciennes données continuent de fonctionner.

#### Tester la compatibilité

Incluez des tests qui garantissent spécifiquement la compatibilité ascendante. Par exemple, si vous avez une API publique, conservez une suite de tests utilisant les anciens contrats d'API et exécutez-les contre le code refactorisé, ils doivent toujours passer.

En résumé, assurez-vous que, lors du refactoring, le comportement externe et les contrats restent cohérents. Cette approche prudente protège vos utilisateurs et systèmes en aval, vous permettant de récolter les bénéfices internes du refactoring sans causer de chaos externe.

### 5. Gérer les dépendances et le couplage serré

L'un des aspects les plus délicats du refactoring d'une grande base de code est de traiter le code profondément interdépendant. Les systèmes complexes souffrent souvent de couplage serré. Le module A suppose des détails sur le module B et vice versa, des variables globales ou des singletons sont utilisés partout, ou un changement à un endroit se répercute dans la moitié de la base de code.

Réduire le couplage est un objectif majeur du refactoring car cela rend le code plus modulaire, ce qui signifie que chaque partie peut être comprise, testée et modifiée indépendamment. Alors, comment pouvons-nous progressivement desserrer le couplage dans un système hérité ?

Passons en revue quelques stratégies pour réduire le couplage.

#### Introduire des interfaces ou des couches d'abstraction

Une manière très efficace de découpler est de placer une interface entre les composants. Par exemple, si vous avez une classe qui interroge directement une base de données, introduisez une interface et faites en sorte que la classe utilise celle-ci à la place. Le code de base de données sous-jacent implémente l'interface.

```python
# avant : instanciation directe
class OrderService:
    def __init__(self):
        self.repo = OrderRepository()

# après : injection de dépendance
class OrderService:
    def __init__(self, repo):
        self.repo = repo

# câblage au démarrage de l'application
repo = OrderRepository(db_conn)
service = OrderService(repo)
```

![Introduire des interfaces ou des couches d'abstraction](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfuMNvzC4x3X0EOgoRXzflfOv4C-Dxzc2Tm16KA0NdZcOH0nK300LUwcNzXCL6iqu0rhknHiVhnQN4csDCYUupQLc4Kt6Q4c7d1Pi47NfrXKoF9rhXCUMAhtozsDpFMVT2lo2OX5Q?key=nBTgfzmVkL2-N7DBMJ6e6gyk align="left")

Maintenant, cette classe ne dépend plus de la manière dont les données sont récupérées. En appliquant le principe d'inversion des dépendances, elle dépend des abstractions, pas des concretions.

#### Utiliser l'injection de dépendances

Une fois que vous avez des interfaces, utilisez l'injection de dépendances pour fournir des implémentations concrètes. De nombreux frameworks supportent les conteneurs DI, ou vous pouvez le faire manuellement (en passant les dépendances via les constructeurs). L'injection de dépendances signifie que le code A n'instancie pas le code B lui-même – au lieu de cela, B est passé dans A.

Cette approche facilite également les tests unitaires (vous pouvez injecter des dépendances mock).

#### Façades ou services enveloppants

Si un sous-système particulier est fortement enchevêtré avec d'autres, envisagez de créer une Façade, un objet qui fournit une interface simplifiée à un ensemble plus large de code. D'autres parties du système appellent alors la Façade, et non les nombreuses méthodes internes du sous-système. En interne, le sous-système peut être refactorisé (même divisé en morceaux plus petits) tant que l'interface externe de la Façade reste cohérente.

Cela est similaire au fonctionnement des microservices (les autres services ne se soucient pas de la manière dont un service est implémenté en interne – ils appellent simplement son API), mais vous pouvez le faire en processus également.

![Facades or wrapper services](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe_X2G_VNTR-I2EIp86SgPD3Zlks70Q4iG3BsqIs94PMgh-_qNfRk7ogT4mqONP7qXzg8PpN92k342-2nH6ertfy32Ga6SFH3PdSLwxP4US9PPjMi6Rqc9hy-gHbSKVzvTvYmTzOQ?key=nBTgfzmVkL2-N7DBMJ6e6gyk align="left")

#### Remplacement progressif (Exécution parallèle)

Si un composant spécifique doit être remplacé par une nouvelle implémentation, il peut être utile de les exécuter en parallèle pendant un certain temps. Par exemple, si vous avez un module spaghetti que vous souhaitez refaire correctement, vous pourriez laisser le code spaghetti en place pour les appels hérités mais commencer à router les nouveaux appels vers le nouveau module.

Le résultat est une base de code où les changements dans une zone (espérons-le) ne casseront pas de manière imprévisible une autre, une propriété clé d'un système maintenable.

### 6. Stratégies de test (Refactoring en toute confiance)

Une stratégie de test robuste vous donnera la confiance de faire des changements importants car vous saurez rapidement si quelque chose d'important se casse. Voici comment aborder les tests dans le contexte d'un grand refactoring :

#### Établir une base de référence avec des tests de régression

Avant même de commencer à refactoriser un composant particulier, assurez-vous d'avoir des tests qui couvrent son comportement actuel. Vous avez de la chance si la base de code a déjà une bonne suite de tests, mais de nombreux systèmes hérités ont des tests inadéquats.

L'une des premières tâches dans ces cas est souvent d'écrire des **tests de caractérisation**. Un test de caractérisation est un test qui documente ce que le système *fait actuellement*, et non ce que nous pensons qu'il devrait faire.

Comme le dit Feathers, "un test de caractérisation est un test qui caractérise le comportement réel d'un morceau de code." Cela vous permet de prendre un instantané de ce qu'il fait et de vous assurer qu'il ne change pas.

Cela vous donne un filet de sécurité afin que vous puissiez refactoriser en toute confiance sans introduire de régressions. Utilisez des suites de tests automatisés pour aider les choses à fonctionner en douceur (unité, intégration, bout en bout).

#### Intégration continue (CI)

Il est fortement recommandé que les tests soient intégrés dans un pipeline CI qui s'exécute à chaque commit ou merge. De cette façon, vous attrapez un bug pendant le refactoring dès que vous l'introduisez, resserrant la boucle de feedback.

#### Versions canari et drapeaux de fonctionnalité

Au-delà des tests pré-lancement, envisagez des stratégies pour déployer en toute sécurité le code refactorisé. Une version canari implique de déployer le changement à un petit sous-ensemble d'utilisateurs ou de serveurs en premier, de l'observer, puis de l'étendre progressivement.

![Canary releases and feature flags](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfAif0ftiqEhiRPDygrmhtzSsfrctq6ZPfJnMg04GwKmxKk-NFiP9GjEGE9rfz7U_WKhRcBYSBYlirjKwzr-PvfZz2FJpEWS6U0UqNh-WayiVM5BGIyz3sabSX-zdKKA0j_ojvhIA?key=nBTgfzmVkL2-N7DBMJ6e6gyk align="left")

Cela est idéal pour attraper les problèmes que les tests pourraient manquer (par exemple, des problèmes de performance ou des cas limites dans les données de production). Si le canari semble bon (pas d'erreurs, les métriques sont saines), vous passez au déploiement complet. Sinon, vous revenez en arrière rapidement – avec seulement un petit impact.

#### Tests de performance et de charge

Si la performance est une préoccupation, incorporez des tests de performance dans votre stratégie. Cela peut être fait dans un environnement de staging. Vous pourriez reconsidérer votre approche ou optimiser le nouveau code si vous voyez une régression significative.

#### Tester le code hérité manquant de tests

Si vous traitez une partie du système sans aucun test (ce qui n'est pas rare dans l'ancien code), donnez la priorité à l'obtention d'au moins une certaine couverture. Il existe également des techniques comme les **tests d'approbation** (où vous générez une sortie et faites approuver par un humain qu'elle est correcte, puis utilisez cela comme base pour les tests futurs). L'important est de ne pas refactoriser entièrement dans le noir ; donnez-vous au moins une lampe de poche sous forme de tests !

En somme, une stratégie de test solide est non négociable pour le refactoring de systèmes complexes. C'est votre filet de sécurité, système d'alerte précoce et guide pour savoir que votre "nettoyage" n'a rien cassé de vital.

### 7. Refactoring sans casser les performances

Une préoccupation courante lors du refactoring est de savoir si ces changements de code plus propre vont rendre mon système plus lent ou plus gourmand en ressources. Idéalement, le refactoring concerne la structure interne et ne devrait pas changer le comportement externe, et la performance fait partie du comportement.

En théorie, la performance devrait rester la même si vous ne changez pas les algorithmes ou les structures de données de manière à affecter la complexité.

En pratique, cependant, la performance peut être affectée involontairement par le refactoring. Le nouveau code peut être plus lisible mais utilise plus de mémoire, ou peut-être qu'un mécanisme de mise en cache critique a été supprimé dans un esprit de simplicité.

**Les ingénieurs seniors doivent être attentifs aux parties du système sensibles aux performances lors du refactoring et prendre des mesures pour éviter les régressions (ou même améliorer les performances lorsque cela est possible).**

Voici comment refactoriser en gardant à l'esprit les performances :

#### Identifier les chemins de code critiques pour les performances

Tous les codes ne sont pas égaux en termes d'impact sur les performances. Si vous les refactorisez, traitez-les presque comme un changement fonctionnel : vous devez re-mesurer les performances ensuite. Vous avez plus de latitude pour les parties du code qui s'exécutent rarement ou qui ne sont pas des goulots d'étranglement.

#### Utiliser le profilage avant et après

Un profileur est un outil qui mesure où le temps est passé dans votre code ou comment la mémoire est allouée. Il est très utile d'exécuter un profileur sur le code avant de refactoriser un module pour voir comment il se comporte, puis de l'exécuter après pour comparer. Si vous voyez, par exemple, qu'après le refactoring, une fonction apparaît maintenant comme prenant 30 % du temps d'exécution (alors qu'elle était négligeable avant), c'est un signal d'alarme. Peut-être que le nouveau code l'appelle plus de fois qu'avant.

```python
import cProfile, pstats
from mymodule import slow_function

def profile(fn):
    profiler = cProfile.Profile()
    profiler.enable()
    fn()
    profiler.disable()
    stats = pstats.Stats(profiler).strip_dirs().sort_stats('cumtime')
    stats.print_stats(10)

# exécuter avant le refactoring
profile(lambda: slow_function())

# après avoir refactorisé slow_function(), ré-exécuter et comparer les stats
```

![profiler-dashboard](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd1xNcjypguN9JbN7JtBhAtBkfDrtCV6IwOORRUVT5rOAha_I2GQx3vgKRAjlxpeeUIGLTETRR6J3EnS2y95DY6ypiH95DQJT0vRfcyxv2KIz99hPXa0O8JjTzxpi5eSsk3spN6EQ?key=nBTgfzmVkL2-N7DBMJ6e6gyk align="left")

#### Lorsque cela est possible, améliorer les performances grâce au refactoring

D'un autre côté, le refactoring peut aider les performances.

Par exemple, en refactorisant le code dupliqué en un seul endroit, vous pouvez utiliser une meilleure mise en cache à cet endroit unique. Donc, surveillez les opportunités d'amélioration des performances qui apparaissent naturellement lorsque vous refactorisez.

Les performances doivent être traitées comme faisant partie du "comportement externe" qui doit être préservé dans un bon état d'esprit. Le refactoring ne devrait idéalement pas ralentir les choses pour les utilisateurs. Pour vous en assurer, incorporez des vérifications de performance dans votre plan, surtout pour les sections critiques. Mesurez, ne devinez pas. L'objectif final est une base de code qui est à la fois propre **et** suffisamment rapide.

### 8. Automatiser les revues de code avec des outils d'IA

Le refactoring de code est un processus continu, pas un événement ponctuel – les outils de revue de code IA aident à faire respecter les normes de code propre, à détecter les odeurs de code tôt et à réduire les tâches répétitives qui peuvent ralentir les réviseurs humains. Cela libère vos ingénieurs pour qu'ils se concentrent sur des problèmes architecturaux ou spécifiques au domaine plus profonds.

![CodeRabbit-ai-code-reviewer-tool](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfWs-ZM80TK_JcjwyPEnywdJl6Tf4G6gYFa1cN_J2ugTlniaGr4a397JuUj721m7kUw0EKMnzYHykpHJdG_aW7w3_B2J91bLL1UoaabdNsmH1uckMJHcFVpAhqZM2r855AsVYwDJg?key=nBTgfzmVkL2-N7DBMJ6e6gyk align="left")

Une option puissante est [CodeRabbit](https://www.coderabbit.ai/), une plateforme de revue pilotée par l'IA conçue pour réduire de moitié le temps de revue et les bugs.

Voici comment cela fonctionne et pourquoi cela peut stimuler votre flux de travail de refactoring :

#### Feedback contextuel alimenté par l'IA

CodeRabbit analyse les demandes de tirage ligne par ligne, appliquant à la fois des modèles de langage avancés et une analyse statique sous le capot. Il signale les bugs potentiels, les écarts par rapport aux meilleures pratiques et les problèmes de style avant qu'un humain n'ouvre la PR.

Quelques autres fonctionnalités incluent :

* **Résumé et corrections en 1 clic générés automatiquement** – Résumez les grandes PR et appliquez des corrections simples instantanément.
  
* **Collaboration en temps réel et chat IA** – Discutez avec l'IA pour des clarifications, des extraits de code alternatifs et des feedbacks instantanés.
  
* **Intégration avec les plateformes de développement populaires** – Prend en charge GitHub, GitLab et Azure DevOps pour une analyse transparente des PR.
  

CodeRabbit propose même des revues de code IA gratuites dans VS Code et avec cette [extension VS Code](https://marketplace.visualstudio.com/items?itemName=CodeRabbit.coderabbit-vscode), vous pouvez obtenir les revues de code IA les plus avancées directement dans votre éditeur de code, économisant du temps de revue, attrapant plus de bugs et vous aidant dans le refactoring.

## Résumé

Refactoriser une base de code complexe d'entreprise est comme rénover un grand bâtiment alors que des gens y vivent encore sans faire s'écrouler la structure.

Le refactoring devrait être un processus continu. Vous empêchez la base de code de se dégrader en incorporant ces pratiques dans votre développement régulier (peut-être en allouant un peu de temps chaque sprint pour le refactoring ou en le faisant de manière opportuniste lorsque vous touchez votre code). Chaque refactoring mineur ne devrait pas être trop complexe, et l'effet cumulatif est significatif.

Comme le dit [Martin Fowler](https://martinfowler.com/), une série de petits changements peut conduire à une amélioration significative de la conception.

C'est tout pour ce blog. J'espère que vous avez appris quelque chose de nouveau aujourd'hui.

Si vous voulez lire plus d'articles intéressants sur les outils de développement, React, Next.js, l'IA et plus encore, alors je vous encourage à consulter mon [blog](https://www.devtoolsacademy.com/).

Certains des nouveaux articles intéressants que j'ai écrits au cours des 24 derniers mois.

* [Cursor vs Windsurf](https://www.devtoolsacademy.com/blog/cursor-vs-windsurf/)
  
* [Comment implémenter le contrôle d'accès basé sur les rôles dans Next.js](https://clerk.com/blog/nextjs-role-based-access-control)
  
* [Revueurs de code IA vs Revueurs de code humains](https://www.devtoolsacademy.com/blog/ai-code-reviewers-vs-human-code-reviewers/)
  
* [Comment construire une application de visioconférence personnalisée avec Stream et Next.js](https://www.freecodecamp.org/news/how-i-built-a-custom-video-conferencing-app-with-stream-and-nextjs/)
  
* [Comment effectuer des revues de code dans la tech – La manière indolore](https://www.freecodecamp.org/news/how-to-perform-code-reviews-in-tech-the-painless-way/)
  

Vous pouvez me contacter si vous avez des questions ou des corrections. Je les attends.

Et si vous avez trouvé ce blog utile, veuillez le partager avec vos amis et collègues qui pourraient en bénéficier également. Votre soutien me permet de continuer à produire du contenu utile pour la communauté tech.

Maintenant, il est temps de passer à l'étape suivante en vous abonnant à ma [**newsletter**](https://bytesizedbets.com/) et en me suivant sur [**Twitter**](https://twitter.com/theankurtyagi).