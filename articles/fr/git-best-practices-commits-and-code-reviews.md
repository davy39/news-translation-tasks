---
title: Bonnes pratiques Git – Comment écrire des commits significatifs, des pull requests
  efficaces et des revues de code
subtitle: ''
author: Grant Riordan
co_authors: []
series: null
date: '2022-08-05T15:45:03.000Z'
originalURL: https://freecodecamp.org/news/git-best-practices-commits-and-code-reviews
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/resized-image-Promo--2-.jpeg
tags:
- name: best practices
  slug: best-practices
- name: code review
  slug: code-review
- name: Git
  slug: git
- name: version control
  slug: version-control
- name: Visual Studio Code
  slug: vscode
seo_title: Bonnes pratiques Git – Comment écrire des commits significatifs, des pull
  requests efficaces et des revues de code
seo_desc: "As developers we push regular code commits – and after a while, it's almost\
  \ second nature to us. \nBut does this mean we're doing things right? Familiarity\
  \ often leads to sloppiness and overlooking the basics.\nIn this article, we will\
  \ explore\n\nHow to ..."
---

En tant que développeurs, nous effectuons régulièrement des commits de code – et après un certain temps, cela devient presque une seconde nature pour nous.

Mais cela signifie-t-il que nous faisons les choses correctement ? La familiarité conduit souvent à de la négligence et à négliger les bases.

Dans cet article, nous allons explorer

* Comment écrire des messages de commit Git significatifs
* Comment créer des pull requests (PR) efficaces
* Comment devenir vraiment bon dans le processus de revue de code et quelques bonnes pratiques à suivre

### Prérequis :

Je préfère utiliser VS Code comme mon éditeur de code. Je l'utilise également pour mon éditeur Git. Je trouve plus facile d'écrire des messages de commit au même endroit où je code. Cela me donne également plus d'espace pour écrire des messages et des descriptions de commit.

Si vous ne l'avez pas encore fait, suivez ces étapes pour faire de VS Code votre éditeur git par défaut.

1. Ouvrez VS Code et dans la palette de commandes, recherchez

> Shell Command: Install 'code' command to PATH

2. Ensuite, exécutez la commande suivante dans votre terminal :

`git config --global core.editor "code --wait"`

Maintenant, lorsque vous exécutez `git commit` ou `git -config --global -e`, cela ouvrira l'éditeur Git dans un fichier dans VS Code.

**Note :** Toutes les commandes données doivent être exécutées dans le terminal (que ce soit votre terminal de choix ou le terminal intégré dans VS Code).

## Comment écrire des messages de commit significatifs

Lorsque vous commitez votre code, il est utile d'écrire des messages de commit utiles. Voici quelques conseils et bonnes pratiques pour vous aider à le faire.

### Utiliser des commandes impératives

Préfixez vos messages de commit avec des [commandes impératives](https://www.grammar-monster.com/glossary/imperative_mood.htm) telles que : `fix`, `refactor`, `add`, et `remove`

C'est parce que vous devriez pouvoir suffixer un message de commit à la phrase

> "Si appliqué, ce code va..."

et informer les autres développeurs de ce qu'il va faire, par exemple :

> Si appliqué, ce code va corriger le problème avec le bouton de connexion qui ne s'affiche pas

### Soyez bref

Vous n'écrivez pas un monologue, alors soyez bref. En règle générale, un message de commit ne doit pas dépasser 50 caractères.

Mettez-vous à la place du développeur ou du relecteur. Essayez de penser à ce que vous aimeriez savoir si vous regardiez le journal Git de ce dépôt.

* Quel travail avez-vous accompli ?
* Pourquoi l'avez-vous fait ?
* Quel effet cela a-t-il sur la base de code ?

Voici un exemple de message de commit concis mais informatif :

```
fix issue with login button not showing
```

### Comment garder les messages de commit courts mais utiles

Dans vos commits, vous pouvez inclure une description de commit, ce qui nous permet d'ajouter encore plus de détails / de contexte sur ce que vous avez fait.

Ajoutez une ligne vide sous le message de commit, et commencez à écrire une description à la ligne 3. Cela ressemble à ceci :

```
fix issue with login button not showing

- update login form validation
- update login styling for showing the button
```

Maintenant, lorsque d'autres développeurs examinent les journaux Git, les commits, ou ont besoin de revenir en arrière sur le code, ils ont une meilleure indication de l'effet qui aura lieu, et s'il causera des changements cassants.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-29.png)

### Exemples de messages de commit non utiles

D'autre part, voici quelques exemples de messages de commit inefficaces :

* `fixed bug` – Il n'y a aucune référence à quel bug a été corrigé exactement, donc cela n'ajoute aucune valeur à l'historique / aux journaux git. Cela rendra l'examen des commits précédents extrêmement difficile et fastidieux. En tant que développeur, vous devriez ouvrir chaque commit comme celui-ci pour comprendre ce qu'il fait réellement.
* `refactored due to PR comments` – Ce message ne nous donne aucune information sur ce qui a été changé. Nous devrions traquer la pull request pour recueillir un quelconque contexte autour des changements effectués, ou encore ouvrir le commit.
* `fixing previous commit` – Manque de contexte à nouveau
* `made tests pass` – Quel fichier de test a été mis à jour ? Vous devriez au moins donner le nom ou la zone des tests qui ont été corrigés.

Tous ceux-ci sont de mauvais exemples de messages de commit en raison de leur ambiguïté, de leur manque d'information et de leur manque de contexte. Ils forcent les membres de l'équipe à faire plus de travail pour comprendre ce qui se passe, ce qui n'est acceptable dans aucune équipe.

## Comment développer une stratégie de commit

Vous pourriez penser que commiter du code est aussi simple que de commiter et de pousser le code. Mais il y a un peu plus à cela.

Parlons de la façon dont vous pouvez développer une stratégie de commit utile pour rester cohérent et faire des commits utiles.

### Faire des commits petits et spécifiques

Les commits plus petits facilitent le retour du code à un état précédent en cas de problème. Si votre commit affecte trop de zones, revenir en arrière pourrait signifier perdre beaucoup de code.

Il est également beaucoup plus facile pour les relecteurs de comprendre ce que fait le code s'il est lié à un seul objectif.

Regardons un exemple concret de la façon dont cela fonctionnerait. Tout d'abord, nous devons ajouter nos changements de fichiers liés. Nous pouvons voir quels fichiers ont été modifiés dans notre branche en exécutant `git status`

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Screenshot-2022-08-01-at-23.28.59.png)
_Exemple de sortie de git status_

Comme vous pouvez le voir, il y a divers fichiers qui ont été modifiés / ajoutés au projet. Cependant, ils concernent tous différentes zones du projet. En suivant la règle d'or de garder les commits petits et pertinents, voyons comment nous pouvons mettre cela en pratique.

En utilisant `git add` suivi des noms de fichiers, nous pouvons commiter uniquement les fichiers qui sont liés. Nous faisons cela en utilisant la commande `git add`, plus les noms des fichiers que nous souhaitons ajouter les uns après les autres comme ceci :

```
git add login.test.ts login.ts
```

Si nous vérifions `git status` maintenant, nous verrons les deux fichiers indexés :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Screenshot-2022-08-01-at-23.34.35.png)
_Exemple de sortie de Git status après l'indexation des fichiers_

Nous avons les fichiers, maintenant pour créer notre commit. Comme toujours, nous utiliserons `git commit` qui ouvrira l'éditeur git dans VS Code (comme nous l'avons configuré plus tôt). Si vous avez sauté cette étape, le commit s'ouvrira dans votre éditeur préféré.

Nous ajouterons un message de commit des changements :

```
Fix issue with login button not showing
```

Voilà, un commit de fichiers liés et petit. Le message de commit nous dit exactement ce que nous avons fait, où se trouvait le problème, ainsi qu'un petit contexte de ce qu'était le problème.

### Mauvais exemple de commit

Puisque nous l'avons fait avec succès, regardons un mauvais exemple :

Imaginez que nous avons fait tout ce travail, et que le développeur a indexé tous les fichiers en une seule fois, en utilisant la commande `git add -A` qui indexe **tous** les fichiers modifiés/ajoutés.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/Screenshot-2022-08-01-at-23.45.26.png)
_Exemple de plusieurs fichiers non liés indexés pour commit_

Ils créent maintenant un message de commit en utilisant la commande Git en une ligne :

```
git commit -m 'Updated various areas such as validation, registration and products pages'
```

#### Pourquoi est-ce si mauvais ?

1. Tout d'abord, il se passe trop de choses dans ce commit. Trop de fichiers signifient que si nous devons revenir en arrière sur les changements de validation, nous ne pouvons pas. Nous devrions revenir en arrière sur tout le commit en perdant les changements de produits et d'inscription.
2. Le message de commit est long. Nous pouvons supprimer des mots inutiles comme 'various areas such as'. Cela n'ajoute aucune valeur au message de commit et prend des caractères qui pourraient être utilisés pour plus de contexte.
3. Nous n'utilisons pas la voix impérative comme mentionné précédemment. Nous devrions changer "Updated" en 'Update'.

> Si appliqué, ce code va corriger le bouton de soumission qui ne s'affiche pas sur la connexion

### Récapitulatif à mi-parcours

À ce stade, nous avons appris :

* Comment formuler un message de commit utile
* Comment formuler une stratégie de commit efficace pour nous permettre de suivre facilement les changements liés et une base de code plus maintenable.
* Ce qui fait un mauvais commit

## Comment créer des pull requests efficaces

### Décider quand pousser

Pousser consiste à envoyer vos commits sur le serveur / l'origine distante, prêts à créer une pull request (PR). Je recommande de pousser dès que la fonctionnalité actuelle ou le bug est terminé.

De plus, il est bon de garder vos PR petites, contenant uniquement des commits liés. Par exemple, si vous aviez les commits suivants :

* `Add new product search component`
* `Add unit tests for product search component`
* `Add documentation for product search component`

Puisque tous ces commits sont liés au même composant, il est recommandé de les regrouper dans une seule PR.

Alors que quelque chose comme :

* `Fix bug within login screen`
* `Refactor registration page for performance`
* `Update validation tests for login form`
* `Update login tests for forgotten password`
* `Update unit tests for product search component`

**Ne devrait pas** aller dans la même PR, car il se passe trop de choses. Ces commits auraient dû être regroupés dans plusieurs PR contenant des commits pertinents à ce moment-là.

Si c'était le journal Git d'une branche, vous ne pourriez pas créer une pull request avec uniquement des fichiers liés, en raison de l'ordre dans lequel les commits ont été créés, car vous ne pouvez pas simplement informer Git que vous voulez que les commits 1, 3 et 4 aillent dans cette PR.

### Gardez-les petites

Rappelez-vous – comme vos commits, gardez vos PR petites. Personne ne veut se frayer un chemin à travers une pull request de 50+ fichiers. Tout ce qui se passera alors, c'est que votre revue souffrira du commun "Looks good to me".

Lorsque vous créez une grande PR, cela se traduit par "_Je n'ai pas pu me donner la peine de regarder tous ces fichiers, mais en les parcourant, cela semble ok_". Avec une PR plus petite, en revanche, cela signifie exactement ce qu'elle dit.

Parfois, les grandes pull requests sont inévitables, comme lors de la mise à jour de fonctions de base et autres. Cependant, vous devriez essayer d'être conscient de la manière dont vous pouvez limiter l'impact sur les autres développeurs.

## Comment préparer votre branche pour la revue de code

Le processus exact de création d'une pull request diffère selon la plateforme d'hébergement de contrôle de version que vous utilisez, mais les concepts sont les mêmes.

Tout d'abord, vous devriez vérifier la branche `main` de votre dépôt. Ensuite, exécutez un `git pull`, qui récupérera tout le dernier code de `main` sur votre système de développement local.

Une fois que vous avez fait cela, vous pouvez revenir à votre propre branche en utilisant `git checkout` et le nom de votre branche, par exemple `git checkout login-fixes`.

Maintenant, nous devons obtenir le code de la branche `main` dans la nôtre. Nous pouvons faire cela en utilisant la commande `git merge`.

```
git merge main
```

S'il y avait des changements, c'est-à-dire s'il y avait des fichiers dans le pull de main, vous devrez créer un "commit de fusion". Ce n'est qu'un autre commit dans votre propre branche contenant les changements fusionnés.

Créez simplement un autre commit, avec un message expliquant que vous avez fusionné depuis main comme ceci :

`git commit -m 'Merge main into login-fixes'`

Poussez vos changements vers le serveur distant en utilisant `git`

## Comment créer la pull request

La manière la plus simple de faire cela est via l'interface web sur votre plateforme de contrôle de version préférée. Dans cet exemple, nous utiliserons GitHub.

Naviguez simplement vers votre dépôt, puis cliquez sur l'onglet Pull Requests.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-21.png)
_Onglet Pull Requests - GitHub_

Sélectionnez "New pull request"

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-22.png)
_Nouvelle Pull Request - Github_

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-24.png)

Lorsque vous créez une pull request, utilisez un titre qui décrit la PR comme vous l'avez fait avec votre commit.

`PR - Fix login button not showing`.

Il peut être utile de fournir aux relecteurs un peu de contexte sur pourquoi cette PR était nécessaire, ou toute information supplémentaire dans la description de la PR.

Comme vous pouvez le voir ci-dessus, j'ai choisi d'inclure ce qu'était la correction, rendant potentiellement la revue plus fluide. J'ai également inclus quelques informations importantes concernant le fait que cette PR ne devrait pas être fusionnée jusqu'à ce qu'une autre PR soit fusionnée.

Lorsque vous travaillez pour certaines entreprises, elles peuvent vous demander d'ajouter une référence de ticket au titre de la PR aussi, mais j'ai déjà discuté pourquoi je pense que ce n'est pas nécessaire.

### Étiquettes de PR

Si vous voulez rendre cela encore plus clair, vous pouvez utiliser des étiquettes de PR. Ce sont des étiquettes qui peuvent être appliquées à la PR pour illustrer soit l'état de la PR, soit des informations simples pour les autres. Vous pouvez les trouver sur la droite de la page de pull request :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-26.png)

Vous pouvez sélectionner parmi des étiquettes prédéfinies ou ajouter les vôtres.

* Cliquez sur Étiquettes
* Entrez l'étiquette que vous souhaitez utiliser. Dans notre scénario, nous allons ajouter une étiquette appelée `Do Not Merge`.
* Appuyez sur entrée une fois que vous avez tapé la valeur, et vous pouvez configurer la couleur et le nom de l'étiquette. Une fois sauvegardée, vous pouvez maintenant la taper à nouveau et elle apparaîtra dans la liste.
* Sélectionnez votre nouvelle étiquette et voilà !

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-27.png)

Cliquez sur Créer la pull request

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-28.png)

Voilà, vous avez créé votre première pull request.

## Comment réviser une PR – Bonnes pratiques

### Que rechercher lors de la révision d'une PR

Prenez toujours du recul et réfléchissez aux éléments clés d'une bonne révision de code. Voici quelques points à considérer :

* Le code suit-il les directives de codage de votre équipe ?
* Le code atteint-il son objectif / ses critères d'acceptation ?
* Le code est-il lisible et est-il facile de comprendre ce qu'il fait sans avoir besoin de commentaires / documentation lourds ? (Celui-ci est pour moi l'un des plus importants, car je suis un grand fan des noms de fonctions et de variables descriptifs.)
* Le code a-t-il besoin d'un refactoring, en considérant la sécurité, la performance ou simplement la facilité de lecture ?
* Le code suit-il des modèles / principes de conception simples, comme la responsabilité unique, l'abstraction, l'encapsulation, et ainsi de suite ? Si ce n'est pas le cas, vous pouvez faire des suggestions sur la manière dont cela peut être réalisé ou peut-être enseigner à ceux qui ne sont pas familiers avec cela ce que cela signifie et les avantages.
* Y a-t-il des "nombres / chaînes magiques" qui seraient mieux servis comme une constante ou une variable nommée ?

### Réviser les PR en temps opportun

Bien que vous ne deviez pas nécessairement vous sentir obligé de regarder une PR immédiatement, ne laissez pas non plus l'auteur en suspens. Cette PR pourrait bloquer un travail futur, ou elle pourrait être importante (si c'est le cas, l'auteur devrait le rendre clair).

Essayez de garder les discussions et les commentaires de PR fluides. Si cela facilite les choses, vous pouvez sauter sur un appel (si vous êtes à distance) ou tirer une chaise dans le bureau et passer en revue la PR ensemble. Cela pourrait accélérer le processus et réduire les allers-retours.

Tout cela étant dit, ne précipitez pas la révision de code. Soyez méticuleux et lisez chaque fichier et chaque changement avec soin. Je vous conseille de télécharger la branche sur laquelle les changements sont effectués, ce qui vous permet de regarder l'ensemble du projet, et pas seulement les lignes modifiées.

De nombreuses fois, si vous ne regardez que des changements de code d'une ou deux lignes, vous ne saurez pas exactement ce que le code est censé faire. Mais si vous regardez le fichier entier, vous pouvez suivre le flux.

Si vous utilisez VS Code et GitHub, vous pouvez utiliser leur propre [extension](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github) pour visualiser les pull requests et les commentaires tout en consultant la branche de PR dans VS Code lui-même.

### Nous sommes tous humains ici

Rappelez-vous que nous sommes tous humains, et que les gens font souvent des erreurs en codant et peuvent simplement négliger des choses.

Tout le monde ne code pas de la même manière que vous non plus, alors ne demandez pas simplement des changements juste parce qu'ils l'ont fait différemment de ce que vous auriez fait. Cela ne signifie pas qu'ils l'ont fait de travers, ni que votre manière est la meilleure.

### Décrivez les changements clairement et formulez vos commentaires avec soin

Une pull request n'est pas un examen, ce n'est pas non plus une opportunité pour vous de critiquer sévèrement le travail de quelqu'un. C'est une opportunité d'apprentissage et une chance de s'assurer que le meilleur code arrive dans la branche principale. Il s'agit de la qualité du code et de savoir si le code répond aux critères d'acceptation.

Pensez au langage que vous utilisez lorsque vous faites des suggestions. Un commentaire de PR est l'opposé d'un message de commit git. Nous n'utilisons plus la voix impérative. Ne leur ordonnez pas de faire des changements, mais faites plutôt des suggestions plus douces en utilisant le [subjonctif](https://www.grammar-monster.com/glossary/subjunctive_mood.htm) à la place.

Puisque vous critiquez un travail dans lequel quelqu'un a probablement mis beaucoup d'efforts, utilisez des phrases comme :

> Si j'étais vous, je changerais cette instruction if en une instruction switch case car c'est plus lisible.

ou

> Peut-être envisager de renommer cette variable avec un nom plus intuitif, comme {alternative} pour la rendre plus compréhensible dès la première lecture de ce qu'elle fait.

Comme ci-dessus, essayez d'ajouter votre raisonnement quant à la raison pour laquelle vous faites la demande de changement. Cela rendra la demande plus percutante et permettra à l'auteur de réfléchir à la question de savoir s'il serait préférable de faire le changement, ou peut-être de susciter une discussion pour parvenir à un compromis.

### Offrir des suggestions d'amélioration

La plupart des systèmes Git vous permettent de cliquer sur la ligne que vous souhaitez voir modifiée et d'ajouter un commentaire pour spécifier plus simplement la ligne exacte de code que vous voulez voir modifiée.

Les fournisseurs d'hébergement comme GitHub disposent d'une fonctionnalité de "suggestion" qui vous permet d'ajouter une suggestion de code directement dans le commentaire, qui peut être instantanément acceptée et commise depuis la PR.

Si cela n'est pas disponible, assurez-vous que ce que vous demandez est clair et concis. Peut-être même réécrire ou écrire votre suggestion dans le commentaire comme suit :

> Peut-être envisager de changer cette instruction if / else en une instruction ternaire comme suit :

`var backgroundColor = isError ? 'red' : 'blue'`

Cela rend la suggestion claire et accélère même le processus de réécriture (en utilisant copier-coller).

### N'ayez pas peur de défendre votre code

Rappelez-vous qu'une PR est une discussion. C'est un processus à double sens, vous donnant l'opportunité de défendre votre code et d'expliquer avec plus de contexte ce que vous pensiez.

Simplement parce que le code peut ne pas avoir l'air parfait, il peut y avoir une raison. Il peut y avoir eu des questions hors de votre contrôle avec lesquelles vous avez dû composer, vous forçant à l'écrire d'une certaine manière.

N'ayez pas peur d'offrir des contre-arguments, mais soyez prêt avec un raisonnement valide, si vous croyez vraiment en votre solution.

### Communiquer que la PR est approuvée

De nos jours, beaucoup de gens filtrent leurs notifications par e-mail de GitHub ou de contrôle de version dans un dossier qui est rarement consulté en raison du volume de mises à jour sur les dépôts, les commits, les branches, etc.

Pour accélérer le processus et le rendre plus amusant pour l'auteur, envoyez-lui simplement un message. De nombreuses entreprises offrent désormais une forme de service de messagerie instantanée, alors pourquoi ne pas l'utiliser ?

Configurez un canal spécifique sur votre plateforme de messagerie instantanée pour les PR. Publiez dans le canal / la salle de discussion le lien de votre PR et permettez aux relecteurs de vous tenir informé de leurs progrès en répondant dans les fils de discussion. Ajoutez un emoji pour le rendre plus léger (comme nous le savons tous, les PR peuvent être ennuyeuses, alors pourquoi ne pas les égayer un peu).

## Conclusion

Dans cet article, nous avons appris :

* Comment configurer VS Code avec l'intégration Git
* Comment écrire des messages de commit Git utiles
* Quand commiter pour faciliter le travail de l'équipe
* Comment réviser efficacement une PR
* Comment gérer les PR de manière à aider toute votre équipe.

J'espère que vous avez appris quelque chose de nouveau, merci d'avoir lu mon article

N'hésitez pas à me suivre sur Twitter [@gWeaths](https://twitter.com/gweaths)