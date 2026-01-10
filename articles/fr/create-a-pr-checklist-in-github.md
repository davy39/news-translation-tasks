---
title: Comment créer une liste de contrôle automatisée pour les pull requests dans
  GitHub
subtitle: ''
author: Brittany Joiner
co_authors: []
series: null
date: '2022-07-11T23:06:03.000Z'
originalURL: https://freecodecamp.org/news/create-a-pr-checklist-in-github
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/Pink-Money-Making-Apps-YouTube-Thumbnail.png
tags:
- name: automation
  slug: automation
- name: GitHub
  slug: github
seo_title: Comment créer une liste de contrôle automatisée pour les pull requests
  dans GitHub
seo_desc: 'If you''ve ever contributed to a project, whether it''s your app at work
  or an open-source tool, you''ve likely created a pull request. This requests that
  your code changes to merged into the main codebase.

  We use pull requests to ensure only quality co...'
---

Si vous avez déjà contribué à un projet, qu'il s'agisse de votre application au travail ou d'un outil open-source, vous avez probablement créé une pull request. Cela demande que vos modifications de code soient fusionnées dans la base de code principale.

Nous utilisons les pull requests pour nous assurer que seul du code de qualité est fusionné dans nos branches principales. Mais parfois, après une session de codage épuisante pour développer une nouvelle fonctionnalité, nous oublions les petits détails.

Dans le pire des cas, ces erreurs peuvent être manquées par les coéquipiers et fusionnées dans la base de code principale, créant ainsi des bugs ou des inefficacités. Dans le meilleur des cas, trouver ces petits détails peut prendre du temps à d'autres membres de l'équipe pour les remarquer et les signaler.

Je suis particulièrement susceptible d'ouvrir une pull request paresseuse, alors j'ai fait ce que tout développeur ferait... J'ai trouvé un moyen d'automatiser une liste de contrôle de PR et de me forcer à faire le travail !

Ce tutoriel vous montre comment construire une extension dans votre navigateur qui générera automatiquement une liste de contrôle pour les pull requests et cachera le bouton Créer une pull request jusqu'à ce que vous ayez coché chaque élément de cette liste.

## Préparez vos outils

Avant de commencer, vous voudrez rassembler quelques éléments.

### Faites une liste de ce qu'il faut vérifier dans votre code

Oubliez tous les outils ou toute automatisation... pendant quelques minutes, réfléchissez à **ce qui fait une bonne pull request**, et listez ces éléments.

Qu'est-ce qui vous facilite la révision des autres pull requests ? Ou quelle est une erreur courante que vous trouvez souvent commentée par les gens ?

Si vous avez besoin de quelques idées, voici ce que j'ai incorporé dans ma propre liste.

* Tout est trié par ordre alphabétique
* Instructions pour que les réviseurs puissent tester le code localement
* Les tests ont été ajoutés
* Capture d'écran de la fonctionnalité/correction de bug (si applicable)
* Si un nouveau texte est ajouté, il est internationalisé
* Les nouveaux éléments ont des labels aria
* Aucun `console.log` non intentionnel laissé après le débogage
* Ai-je utilisé des noms clairs et concis pour les variables et les fonctions ?
* Ai-je expliqué toutes les solutions possibles et pourquoi j'ai choisi celle que j'ai faite ?
* Ajouté des commentaires pour rendre les nouvelles fonctions plus claires
* Ajouté des labels de PR
* Mise à jour de tout fichier d'historique/changelog

Si vous n'êtes toujours pas sûr, parlez à des développeurs plus expérimentés de votre équipe et voyez ce qu'ils recherchent lorsqu'ils révisent les pull requests.

### Créez un compte PixieBrix (votre outil d'automatisation de navigateur)

Il existe plusieurs extensions de navigateur qui vous permettent de créer des automatisations, mais j'ai trouvé [PixieBrix](https://pixiebrix.com/) extrêmement puissant et la communauté est amicale et serviable.

> PixieBrix offre la plateforme low-code la plus polyvalente pour étendre les applications web que vous et vos équipes utilisez déjà. Le résultat ? Vous obtenez l'expérience productive et personnalisée dont vous avez besoin... et que vous méritez. (Source : site web [PixieBrix](https://www.pixiebrix.com/))

Pour créer l'automatisation que je décris ci-dessous, vous devrez vous inscrire pour un compte PixieBrix gratuit.

Il suffit de sélectionner "Start for Free" sur leur site web, et de suivre l'assistant pour créer un compte. Vous serez invité à installer l'[Extension Chrome PixieBrix](https://chrome.google.com/webstore/detail/pixiebrix/mpjjildhmpddojocokjkgmlkkkfjnepo).

Maintenant, vous êtes prêt à commencer !

## Comment construire l'automatisation de la liste de contrôle des pull requests

D'accord, vous êtes prêt. Maintenant, il est temps de construire.

Si vous voulez prendre le chemin le plus simple, vous pouvez simplement [activer l'extension que j'ai déjà construite](https://app.pixiebrix.com/activate?id=@brittany-joiner/gh-on-a-pr), et la modifier comme vous le souhaitez.

Mais si vous voulez la construire à partir de zéro et vous familiariser avec le fonctionnement de l'automatisation des navigateurs, suivez ces étapes.

### Étape 1 – Ouvrir l'éditeur de page dans PixieBrix

Pour construire des extensions dans PixieBrix, vous n'avez pas besoin de VSCode ou d'un autre éditeur. Vous pouvez tout faire entièrement dans votre navigateur.

J'aime commencer par aller sur la page où je veux que l'action se produise, dans ce cas, `github.com`.

Pour accéder à l'éditeur, faites un clic droit sur n'importe quelle page web pour ouvrir le menu contextuel et sélectionnez `Inspect`. Faites défiler vos onglets _(ceux qui disent des choses comme `Elements`, `Console`, `Network`, etc)_ jusqu'à ce que vous voyiez `PixieBrix`.

![demonstration-of-opening-inspector-and-choosing-pixiebrix-tab](https://www.freecodecamp.org/news/content/images/2022/07/open-page-editor.gif)
_Clic droit pour Inspecter, puis allez à l'onglet PixieBrix_

Il se peut que vous soyez invité à accorder certaines permissions, mais vous trouverez ensuite une page blanche avec un bouton en haut à gauche qui dit "Add". C'est là que nous commencerons.

### Étape 2 – Ajouter une brique de déclenchement

Pour construire une extension dans PixieBrix, vous devez enchaîner des briques ensemble. Vous pouvez penser aux briques comme des fonctions et une extension est la fonction principale qui exécute les fonctions plus petites dans la séquence que vous configurez.

Vous avez plusieurs options pour déclencher cette extension.

![pixiebrix-trigger-options-menu](https://www.freecodecamp.org/news/content/images/2022/07/Screen-Shot-2022-07-10-at-2.33.29-PM.png)
_Options de déclenchement de l'extension dans PixieBrix_

Vous pouvez choisir une action manuelle, comme ajouter un bouton à une page, ou un menu contextuel (qui est lorsque vous faites un clic droit sur une page web – ce même menu où vous accédez à votre inspecteur !) Ou vous pourriez utiliser une commande de barre rapide (un raccourci clavier).

Le panneau de la barre latérale ouvre un panneau sur le côté droit de votre navigateur et n'est pas réellement un déclencheur mais est utilisé pour créer un affichage pour un autre déclencheur.

Pour ce flux de travail spécifique, utilisez l'option `Trigger`, qui exécute l'extension chaque fois que vous chargez une page web spécifique et que des critères supplémentaires que vous configurez sont remplis.

Voici à quoi cela ressemble au début :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Screen-Shot-2022-07-10-at-2.51.09-PM.png)

Vous pouvez changer le nom en haut pour ce que vous voulez appeler cela, comme `Github PR Checklist`.

Pour configurer le déclencheur, réfléchissez à quand vous voulez voir votre liste de contrôle. Vous pourriez la faire apparaître chaque fois que vous allez sur GitHub, mais c'est probablement plus fréquent que vous ne le souhaitez puisque vous n'avez pas besoin de la liste de contrôle lorsque vous lisez les problèmes ou que vous cherchez quelque chose dans un dépôt.

J'ai décidé de déclencher chaque fois qu'un élément de bouton `create pull request` est sur la page, ce qui indique que je suis sur le point d'ouvrir une pull request. Donc c'est probablement un bon moment pour passer en revue ma liste de contrôle !

Alors, passez par les étapes d'ouverture d'une pull request et naviguez jusqu'à une page qui a ce bouton vert (tout en gardant votre éditeur de page ouvert).

![github-create-pull-request-button](https://www.freecodecamp.org/news/content/images/2022/07/Screen-Shot-2022-07-10-at-5.12.04-PM.png)
_Bouton Créer une pull request de GitHub_

Une fois que vous avez ce bouton en vue, faites défiler jusqu'à la section `Advanced: Match Rules` de la brique de déclenchement, et cherchez le champ `Selectors`.

![selector-field-in-pixiebrix-trigger-brick](https://www.freecodecamp.org/news/content/images/2022/07/Screen-Shot-2022-07-10-at-5.13.46-PM.png)
_Section Sélecteur dans la configuration de la brique de déclenchement PixieBrix_

À partir de là, vous pouvez utiliser le bouton de la souris pour ouvrir une vue de sélection d'élément et cliquer pour sélectionner le bouton, ou vous pouvez copier cette classe directement dans le champ.

```
.hx_create-pr-button
```

Donc maintenant vous avez créé un déclencheur qui dit chaque fois que vous chargez une page hébergée sur `github.com`.

D'accord, nous avons identifié la classe de ce bouton, donc la partie la plus difficile est derrière nous ! Maintenant, nous devons simplement le cacher, montrer la liste de contrôle, puis l'afficher à nouveau lorsque la liste de contrôle a été complétée.

### Étape 3 – Masquer le bouton `create pull request`

Sélectionnez le bouton plus sous la brique de déclenchement pour ajouter une autre brique. Vous verrez un marché s'ouvrir vous permettant de rechercher toutes les briques disponibles. Recherchez `hide` et vous verrez cette brique.

![pixiebrix-marketplace-with-hide-brick](https://www.freecodecamp.org/news/content/images/2022/07/Screen-Shot-2022-07-10-at-5.16.07-PM.png)
_Brique Masquer dans le marché PixieBrix_

Passez la souris sur la brique "Hide" et pour voir plus d'options, puis sélectionnez "Add" pour l'ajouter à votre extension.

La seule configuration dont cette brique a besoin est **quel élément masquer**. Dans ce cas, ce sera exactement le même élément que nous avons utilisé dans notre déclencheur – le bouton créer une pull request. Vous pouvez donc copier cette même classe et la définir comme valeur pour le sélecteur.

### Étape 4 – Ouvrir une barre latérale

Ajoutez une autre brique appelée `Show Sidebar`. Cela ouvrira un panneau sur le côté droit de votre navigateur pour afficher du contenu.

J'ai défini le champ `panelHeading` sur `PR` pour spécifier qu'il doit charger l'onglet `PR`. Si vous n'avez pas déjà d'autres panneaux latéraux configurés, vous n'aurez pas besoin de placer quoi que ce soit ici et vous pouvez passer à l'étape suivante.

### Étape 5 – Vous attribuer l'issue

Avant d'arriver à la liste de contrôle, j'ai ajouté une autre pièce d'automatisation à cela en plus d'afficher la liste de contrôle et de masquer le bouton.

J'ai créé une action pour m'attribuer l'issue. Ce n'est qu'un clic, mais pourquoi ne pas faire faire cela par les robots ? 😊

Pour ce faire, ajoutez une autre brique appelée `Simulate a DOM event`. Cette brique fait exactement ce qu'elle semble faire... elle prétend faire quelque chose à un élément spécifique, comme cliquer dessus.

Fournissez un sélecteur pour l'élément avec lequel vous souhaitez interagir, et un événement.

Tout comme dans les briques de déclenchement et de masquage, vous pouvez utiliser le bouton de la souris pour ouvrir un sélecteur sur votre écran et sélectionner le lien `assign yourself` pour appliquer automatiquement ces classes au champ sélecteur.

Vous pouvez également appliquer manuellement la classe en copiant et collant ceci dans le champ `selector` :

```
#new_pull_request .js-issue-assign-self
```

Assurez-vous de sélectionner `click` pour l'`event`, et vous êtes prêt !

### Étape 6 – Créer votre liste de contrôle

Maintenant, nous arrivons au cœur de notre extension. Il est temps de construire la liste de contrôle. Sélectionnez le bouton plus et ajoutez la brique `Show a modal or sidebar form`.

C'est la brique qui conçoit un formulaire, et pour chaque élément que nous voulons reconnaître ou penser avant de soumettre une pull request sera un champ de case à cocher.

#### Définir un titre et une description de formulaire

Ce sont des éléments purement cosmétiques, alors définissez-les comme vous le souhaitez.

![form-settings-for-pixiebrix-form-brick](https://www.freecodecamp.org/news/content/images/2022/07/Screen-Shot-2022-07-10-at-3.09.11-PM-1.png)
_Paramètres de formulaire pour la brique de formulaire PixieBrix_

#### Configurer votre premier champ

Prenez votre liste des éléments à vérifier avant d'ouvrir une pull request, et choisissez le premier. Ce sera notre premier champ de formulaire, et vous devrez définir les champs suivants dans PixieBrix :

* `name`
* `label`
* `input type`

Le nom et le label peuvent être ce que vous voulez. **Gardez le nom simple** car vous devrez vous y référer dans l'étape suivante lorsque vous vérifierez s'il est vrai ou non. **Le label est ce qui apparaît visuellement à côté de la case à cocher**. Pour le type d'entrée, sélectionnez **checkbox**.

![pixiebrix-form-field-configured](https://www.freecodecamp.org/news/content/images/2022/07/Screen-Shot-2022-07-10-at-5.29.30-PM.png)
_Configuration du champ de formulaire PixieBrix_

Vous pouvez prévisualiser son apparence dans le panneau latéral droit de l'éditeur de page PixieBrix.

![previewed-form-in-pixiebrix](https://www.freecodecamp.org/news/content/images/2022/07/Screen-Shot-2022-07-10-at-5.30.21-PM.png)
_Formulaire de prévisualisation dans le panneau de prévisualisation PixieBrix_

#### Ajouter le reste des éléments en tant que nouveaux champs

Faites défiler au-dessus du champ pour sélectionner le bouton bleu qui dit "Add new field", et faites-le à nouveau pour autant d'éléments que vous avez.

#### Configuration finale du formulaire

Presque terminé ! Faites défiler **sous les options de champ de formulaire** jusqu'à ce que vous voyiez `Submit Button Text`. Vous pouvez le laisser tel quel, mais j'ai personnalisé le mien pour qu'il dise `Ready to Open` afin de rendre l'action du bouton plus claire.

Plus important encore, changez la valeur `Location` en `sidebar` au lieu de `modal` en sélectionnant le menu déroulant. Cela définit le formulaire pour qu'il apparaisse dans la barre latérale que nous avons ouverte à l'étape précédente.

### Étape 7 – Afficher le bouton `create pull request` lorsque la liste de contrôle est complétée

Ajoutez une dernière brique à cette extension appelée `Show`. Cela est similaire à Hide, et nous lui passerons cette même classe que nous avons référencée tout ce temps pour le bouton `create pull request`.

La voici à nouveau si vous avez besoin d'un rappel :

```
.hx_create-pr-button
```

Il y a une autre pièce à configurer car nous voulons contrôler quand cette brique s'exécute puisque nous voulons seulement afficher le bouton si chaque élément a été coché dans la soumission du formulaire.

Nous aurions pu simplement rendre chaque champ du formulaire obligatoire afin que vous ne puissiez pas soumettre le formulaire tant que tout n'était pas coché. Mais une autre façon de faire cela est de modifier le champ `Condition` sous les options avancées de cette brique.

C'est ici que vous pouvez spécifier quand cette brique spécifique doit s'exécuter. Vous construirez une instruction qui retourne vrai si chaque champ de la liste de contrôle est vrai.

Voici à quoi ressemble la syntaxe, bien que vous deviez remplacer la valeur `item` par le nom de chaque élément.

```
{{ "true" if @form.item1 and @form.item2 and @form.item3 and @form.item4 and @form.item5 and @form.item6 and @form.item7 and @form.item8 and @form.item9 and @form.item10 and@form.item11 }}
```

Lorsque vous avez terminé, votre brique devrait ressembler à ceci :

![show-brick-configuration](https://www.freecodecamp.org/news/content/images/2022/07/Screen-Shot-2022-07-10-at-5.35.44-PM.png)
_Configuration de la brique Show_

Sélectionnez le bouton bleu de sauvegarde en haut à droite de l'éditeur de page PixieBrix pour sauvegarder votre extension.

## Essayez-le

Maintenant, essayez-le ! Que vous ayez [activé l'extension préconstruite](https://app.pixiebrix.com/activate?id=@brittany-joiner/gh-on-a-pr), ou suivi le tutoriel et l'ayez construite vous-même, vous êtes prêt à tester.

Ouvrez une pull request et vous verrez le formulaire de la barre latérale et aucun bouton vert. Cochez tous les éléments de la liste, et soumettez, puis soudainement votre bouton apparaît, et vous êtes déjà attribué à la PR !

![demo-of-pr-checklist](https://www.freecodecamp.org/news/content/images/2022/07/demo-pr-checklist.gif)
_Démonstration de la liste de contrôle PR_

Si vous avez des difficultés à commencer à construire cela ou si cela ne fonctionne pas comme prévu, la communauté PixieBrix est active et les mainteneurs sont toujours prêts à intervenir et à aider.

Mais si vous êtes plus un apprenant visuel et que vous préférez regarder, j'ai créé une vidéo qui vous montre comment [construire cette liste de contrôle PR automatisée](https://youtu.be/cpZ1J2s-2jk).

Merci d'avoir lu !