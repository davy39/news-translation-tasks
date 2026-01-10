---
title: Comment économiser votre puissance cérébrale et coder plus efficacement
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2020-06-25T14:10:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-save-your-brainpower-and-code-more-efficiently
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/ergonomics.png
tags:
- name: Productivity
  slug: productivity
- name: remote work
  slug: remote-work
- name: Visual Studio Code
  slug: vscode
seo_title: Comment économiser votre puissance cérébrale et coder plus efficacement
seo_desc: 'If you knew these tools existed, you''d probably be using them by now.

  This article isn’t going to tell you about saving your neck with a Roost stand,
  or your wrists with a split keyboard - I’ve already done that. This article is about
  saving your bra...'
---

### Si vous saviez que ces outils existaient, vous les utiliseriez probablement déjà.

Cet article ne va pas vous parler de sauver votre cou avec un support Roost, ou vos poignets avec un clavier divisé - [je l'ai déjà fait](https://heronebag.com/blog/next-level-ergonomics-for-remote-work-developers/). Cet article parle de sauver votre cerveau - appelons cela l'ergonomie technique.

Quand j'ai commencé à programmer à plein temps, je me suis constamment sentie fatiguée par l'effort mental. Programmer, c'est difficile ! Heureusement, vous pouvez vous consoler en sachant que cela devient plus facile avec la pratique, et avec une excellente équipe de soutien.

Des gens très gentils qui nous ont précédés ont inventé des outils pour rendre les parties difficiles de la communication avec les ordinateurs beaucoup plus faciles pour nos pauvres cerveaux humains.

Je vous invite à explorer ces outils techniques super utiles. Ils amélioreront votre environnement de développement et soulageront une grande partie du stress mental de la programmation. Vous ne croirez bientôt plus que vous avez pu vous en passer.

## Pas votre surlignage de syntaxe moyen

Si vous travaillez encore avec un surlignage de syntaxe qui ne fait que repérer les noms de variables et de classes pour vous, c'est mignon. Il est temps de passer à la vitesse supérieure.

![Mon thème VSC actuel et le surlignage de syntaxe](https://victoria.dev/blog/technical-ergonomics-for-the-efficient-developer/Screenshot_20200612_185858.png)
_Une capture d'écran de [Kabukichō](https://github.com/victoriadrake/kabukicho-vscode) avec des améliorations de surlignage de syntaxe._

En toute sérieux, le surlignage de syntaxe peut grandement faciliter la recherche de ce que vous cherchez sur votre écran : la ligne actuelle, l'endroit où votre bloc de code actuel commence et se termine, ou le surlignage absolu et révolutionnaire des ensembles de crochets dans lesquels vous vous trouvez.

J'utilise principalement Visual Studio Code, mais des extensions similaires peuvent être trouvées pour les principaux éditeurs de texte.

Voici mes préférés :

* [Bracket Pair Colorizer](https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer-2) met en évidence les paires de crochets séquentiels dans différentes couleurs correspondantes, rendant la douleur de trier les crochets et parenthèses imbriqués une chose du passé.
* [TODO Highlight](https://github.com/wayou/vscode-todo-highlight) élimine effectivement toute excuse que vous auriez pu avoir pour commettre involontairement des commentaires `TODO` et `FIXME` en les rendant très faciles à voir. Vous pouvez même ajouter vos propres mots-clés personnalisés à surligner (je suggère `wtf`, mais vous ne l'avez pas entendu de moi.)
* [Indented Block Highlighting](https://github.com/byi8220/indented-block-highlighting) place un surlignage facile à distinguer mais peu intrusif derrière votre bloc de code actuel en retrait, afin que vous puissiez voir exactement où ce `if` se termine et pourquoi ce dernier `else` ne fait absolument rien.
* [Highlight Line](https://github.com/cliffordfajardo/highlight-line-vscode) place une ligne (un peu trop) brillante là où vous avez laissé votre curseur. Vous pouvez personnaliser l'apparence de la ligne - j'ai défini la `borderWidth` de la mienne à `1px`.

Le thème représenté dans Visual Studio Code ci-dessus est [Kabukichō](https://github.com/victoriadrake/kabukicho-vscode). Je l'ai créé.

## Utilisez les hooks Git

Je vous ai précédemment présenté [une liste de contrôle interactive pré-commit à la manière des infopublicités](https://victoria.dev/blog/an-automatic-interactive-pre-commit-checklist-in-the-style-of-infomercials/) qui est à la fois amusante et utile pour renforcer la qualité de vos commits. Mais ce n'est pas tout !

Les hooks Git sont des scripts qui s'exécutent automatiquement à des points prédéterminés dans votre flux de travail. Utilisez-les bien, et vous pouvez économiser beaucoup de puissance cérébrale.

Un hook `pre-commit` se souvient de faire des choses comme lint et formater le code, et même exécute des tests locaux pour vous avant que vous ne poussiez quelque chose d'embarrassant de manière indélébile.

Les hooks peuvent être un peu ennuyeux à partager (le répertoire `.git/hooks` n'est pas suivi et donc omis lorsque vous clonez ou forkez un dépôt) mais il existe un framework pour cela : le [framework pre-commit](https://pre-commit.com/), qui vous permet de créer un fichier de configuration partageable de plugins de hooks Git, pas seulement pour `pre-commit`.

Je passe la majorité de mon temps ces jours-ci à coder en Python, voici donc mon fichier `.pre-commit-config.yaml` préféré actuel :

```yaml
fail_fast: true
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v3.1.0 # Utilisez la référence que vous souhaitez pointer
    hooks:
      - id: detect-aws-credentials
      - id: end-of-file-fixer
      - id: trailing-whitespace
  - repo: https://github.com/psf/black
    rev: 19.3b0
    hooks:
      - id: black
  - repo: https://github.com/asottile/blacken-docs
    rev: v1.7.0
    hooks:
      - id: blacken-docs
        additional_dependencies: [black==19.3b0]
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v0.780
    hooks:
      - id: mypy
  - repo: local
    hooks:
      - id: isort
        name: isort
        stages: [commit]
        language: system
        entry: isort
        types: [python]
      - id: black
        name: black
        stages: [commit]
        language: system
        entry: black
        types: [python]


```

Il existe de nombreuses [hooks supportées](https://pre-commit.com/hooks.html) à explorer.

## Utilisez un système de typage

Si vous écrivez dans des langages comme Python et JavaScript, offrez-vous un cadeau d'anniversaire anticipé et commencez à utiliser un système de typage statique. Non seulement cela vous aidera à améliorer la façon dont vous pensez au code, mais cela peut également rendre les erreurs de type claires avant d'exécuter une seule ligne.

Pour Python, j'aime utiliser [mypy](https://github.com/python/mypy) pour la vérification de type statique. Vous pouvez le configurer comme un hook `pre-commit` (voir ci-dessus) et il est [supporté dans Visual Studio Code également](https://code.visualstudio.com/docs/python/linting#_mypy).

[TypeScript](https://www.typescriptlang.org/) est ma manière préférée d'écrire du JavaScript. Vous pouvez exécuter le compilateur sur la ligne de commande en utilisant Node.js (voir [les instructions dans le dépôt](https://github.com/Microsoft/TypeScript)), il fonctionne assez bien [avec Visual Studio Code](https://code.visualstudio.com/Docs/languages/typescript) dès la sortie de la boîte, et bien sûr, il existe plusieurs options pour [les intégrations d'extensions](https://code.visualstudio.com/Docs/languages/typescript#_typescript-extensions).

## Arrêtez de maltraiter inutilement votre cerveau

Je veux dire, vous ne resteriez pas sur votre tête toute la journée pour faire votre travail. Ce serait plutôt inconfortable de lire les choses à l'envers tout le temps (au moins [jusqu'à ce que votre cerveau s'adapte](https://www.youtube.com/watch?v=jKUVpBJalNQ)), et en tout cas, vous seriez probablement inconfortablement congestionné en peu de temps.

Travailler sans tirer parti des outils ergonomiques techniques que je vous ai donnés aujourd'hui est un peu comme une inversion inutile - pourquoi le feriez-vous, si vous n'avez pas à le faire ?