---
title: Extensions Visual Studio Code pour booster votre productivité en 2024
subtitle: ''
author: Natalie Pina
co_authors: []
series: null
date: '2024-01-24T22:42:52.000Z'
originalURL: https://freecodecamp.org/news/best-vscode-extensions
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Group-1.png
tags:
- name: Productivity
  slug: productivity
- name: Visual Studio Code
  slug: vscode
seo_title: Extensions Visual Studio Code pour booster votre productivité en 2024
seo_desc: 'According to the 2023 Stack Overflow Developer Survey, Visual Studio Code
  (also known as VSCode) ranked as the most preferred integrated developer environment
  (IDE) tool.

  Visual Studio Code has many great features out-of-the-box, and supports a large...'
---

Selon le [2023 Stack Overflow Developer Survey](https://survey.stackoverflow.co/2023/#section-most-popular-technologies-integrated-development-environment), Visual Studio Code (également connu sous le nom de VSCode) a été classé comme l'environnement de développement intégré (IDE) le plus préféré.

Visual Studio Code possède de nombreuses fonctionnalités intégrées, et supporte une large communauté d'extensions pour ajouter des fonctionnalités améliorées.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-12-at-12.01.59-PM.png align="left")

*Image de l'enquête Stack Overflow montrant la popularité de VSCode (73,71 % des répondants l'utilisent)*

L'utilisation d'extensions peut étendre les fonctionnalités et outils disponibles dans VSCode. Avec une majorité d'outils en un seul endroit, cela permet de réduire les changements de contexte, ce qui a été montré comme [nuisible à la productivité](https://asana.com/resources/context-switching).

J'ai testé plus de 40 extensions différentes au cours de l'année dernière et j'ai affiné une liste sélectionnée de mes préférées. Ces extensions ont boosté ma productivité en tant qu'ingénieur logiciel. Je veux partager cette liste avec vous pour booster votre productivité également.

Cette liste est conçue pour être indépendante du langage avec un accent sur la productivité. Si vous êtes intéressé à explorer mes extensions recommandées pour personnaliser le style de votre éditeur, vous pouvez trouver plus de détails [dans cet article](https://www.freecodecamp.org/news/best-colorful-vscode-extensions-for-productivity/).

## Extensions VSCode que nous allons couvrir :

* [Better Comments](#heading-meilleurs-commentaires)
    
* [Bookmarks](#heading-signets)
    
* [Code Spell Checker](#heading-verificateur-dorthographe-de-code)
    
* [CodeSnap](#heading-codesnap)
    
* [CodiumAI](#heading-codiumai)
    
* [Error Lens](#heading-error-lens)
    
* [Git History](#heading-historique-git)
    
* [GitLens](#heading-gitlens)
    
* [GitHub Copilot](#heading-github-copilot)
    
* [Icons Themes](#heading-themes-dicones)
    
* [Indent Rainbow](#heading-indent-rainbow)
    
* [Live Share](#heading-live-share)
    
* [Multiple Cursor Case Preserve](#heading-conservation-de-la-casse-du-curseur-multiple)
    
* [Path Intellisense](#heading-path-intellisense)
    
* [Peacock](#heading-paon)
    
* [Prettier](https://www.freecodecamp.org/news/p/db680fa0-6ecb-42b3-a803-ea6b47c90add/@prettier)
    
* [Project Manager](#heading-gestionnaire-de-projets)
    
* [Tabnine](#heading-tabnine)
    
* [TODO Highlight](#heading-mise-en-evidence-todo)
    
* [Todo Tree](#heading-arborescence-todo)
    

Dans cet article, je vais couvrir toutes ces extensions en détail et conseiller sur la manière dont elles peuvent élever vos niveaux d'efficacité en tant que développeur.

## Meilleurs Commentaires

[Better Comments](https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments) vous aide à renforcer les commentaires dans le code. Les commentaires de code sont bénéfiques pour la lisibilité et fournissent des explications ou du contexte pour référence future. Laisser de bons commentaires de code peut faire gagner du temps aux autres et à vous-même à l'avenir.

Les fonctionnalités prises en charge incluent la possibilité de catégoriser les annotations des alertes, d'écrire des requêtes, de faire une liste de choses à faire et de montrer les points forts. Il existe une liste exhaustive de langages pris en charge.

Les lignes de code qui sont commentées sont stylisées pour être en gris foncé avec un texte barré, soulignant leur exclusion et signalant qu'elles doivent être supprimées.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/better-comments.png align="left")

*Commentaires de code stylisés avec Better Comments.*

## Signets

[Bookmarks](https://marketplace.visualstudio.com/items?itemName=alefragnani.Bookmarks) vous permet de marquer des positions dans votre code. Ces lignes sont notées avec une icône de signet bleu. Les signets peuvent être organisés et nommés pour permettre une référence rapide.

Tous les signets peuvent être trouvés dans une section de barre latérale dédiée. C'est un excellent outil pour améliorer la navigation et vous aider à passer moins de temps à chercher des références.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/printscreen-toggle.png align="left")

*Signets affichés en bleu avec une icône de signet à côté du numéro de ligne.*

## Vérificateur d'orthographe de code

[Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker) porte bien son nom. Il fournit un vérificateur d'orthographe de base pour trouver et corriger les erreurs d'orthographe dans votre base de code. Les mots mal orthographiés sont indiqués par un soulignement ondulé. Il est disponible dans de nombreuses langues.

C'est l'une de mes extensions préférées. J'ai attrapé et corrigé tant de fautes de frappe grâce à celle-ci.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/example.gif align="left")

*Cette image montre comment Spell Checker détecte et corrige les erreurs d'orthographe.*

## CodeSnap

[CodeSnap](https://marketplace.visualstudio.com/items?itemName=adpyke.codesnap) est utilisé pour prendre des captures d'écran de code. Il peut être utile pour partager des extraits de code avec facilité.

Pour prendre une capture de votre code, utilisez (Ctrl+Shift+P sur Windows et Linux, Cmd+Shift+P sur OS X) et recherchez `CodeSnap`. Ensuite, sélectionnez la zone de votre code à capturer, ajustez la largeur et cliquez sur le bouton de l'obturateur. Vous pouvez également prendre une capture en sélectionnant du code, en cliquant avec le bouton droit et en sélectionnant CodeSnap.

Il existe des sites web qui peuvent faire cela, cependant, avoir ces outils directement dans votre éditeur permet de réduire les changements de contexte pour booster la productivité.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/material_operator-mono.png align="left")

*Exemple de capture de code React créé avec CodeSnap.*

## CodiumAI

[CodiumAI](https://marketplace.visualstudio.com/items?itemName=Codium.codium) est une boîte à outils de code alimentée par l'IA gratuite. Elle supporte des fonctionnalités comme l'autocomplétion de code, le chat, la recherche améliorée et les suggestions.

L'IA est devenue un acteur majeur dans l'amélioration de la productivité des développeurs. Imaginez passer la moitié du temps à écrire des tests, vous permettant de passer plus de temps sur d'autres tâches cruciales et créatives.

En matière de tests, CodiumAI excelle. Il peut analyser le code et générer des tests significatifs et des suites de tests complètes.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Tests-Gif.gif align="left")

*CodiumAI générant une suite de tests basée sur une section de code Python.*

C'est une extension relativement nouvelle qui gagne rapidement en popularité. Les langages supportés sont Python, JavaScript, TypeScript, Java, Go, et d'autres.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/g_python_random_gen_with_logo.gif align="left")

*Fonctionnalité d'autocomplétion de CodiumAI utilisée pour créer des fonctions basées sur des invites en langage naturel.*

## Error Lens

[Error Lens](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens) améliore la mise en évidence des erreurs, des avertissements et d'autres diagnostics de langage. C'est un excellent outil de débogage et de prévention des erreurs à avoir.

Les erreurs ne passeront pas inaperçues avec cette extension. Les erreurs et avertissements sont mis en évidence en surlignant toute la ligne, ainsi que le message correspondant imprimé en ligne.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/demo.png align="left")

*Error Lens identifiant une erreur, notifiant qu'il manque un point-virgule et une erreur de syntaxe.*

Passez moins de temps à sourcer les erreurs, car cliquer sur une annotation vous redirige directement vers la ligne de code correspondante.

Il y a un support pour plusieurs langues, ce qui en fait un outil précieux pour les développeurs travaillant sur des projets dans différentes langues. Vous pouvez également configurer l'apparence et le comportement des erreurs et des avertissements.

## Historique Git

[Git History](https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory) est une extension extrêmement utile pour le contrôle de version avec Git (l'extension a 10 millions d'installations, donc il est clair qu'elle est populaire). Cette extension vous permet d'explorer l'historique détaillé de votre dépôt Git directement depuis l'interface VSCode. Vous pouvez voir l'historique des fichiers, le journal git, et effectuer des comparaisons.

Elle fournit une représentation interactive et visuelle des journaux de commit, des branches et des changements de fichiers au fil du temps. Cette extension offre une expérience plus accessible et sans complication pour travailler sur des projets sous contrôle de version.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/gitLogv3--1-.gif align="left")

*Git History est utilisé ici pour créer une balise sur un commit spécifique.*

## GitLens

[GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) est l'outil Git le plus robuste, avec tant de fonctionnalités regroupées dans une seule extension. Il dispose d'une forte communauté open-source et continue de bénéficier d'un support actif avec des mises à jour fréquentes.

Avec GitLens, vous pouvez obtenir des informations puissantes sur vos dépôts directement dans VSCode. Les annotations sont intégrées dans tout l'éditeur, affichant des tonnes d'informations Git.

L'une des fonctionnalités les plus utiles de GitLens est l'annotation de blame. Cela vous permet de voir qui a écrit le code et il y a combien de temps.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/current-line-blame.png align="left")

*GitLens retrace la ligne de code à un commit créé il y a 4 ans par l'utilisateur (Vous).*

Une autre fonctionnalité que j'ai trouvée pratique est l'éditeur de rebase interactif. Cela offre une bonne expérience utilisateur lors de l'exécution de rebases.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/rebase.gif align="left")

*Exemple de GitLens d'un rebase interactif. Les commits peuvent être sélectionnés, modifiés, supprimés, écrasés, et plus encore.*

## GitHub Copilot

[GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) a gagné énormément de traction au cours des deux dernières années. Ce produit a révolutionné l'expérience de codage en exploitant des capacités avancées d'IA. Il aide non seulement à compléter des extraits de code, mais agit également comme un copilote de programmation en paire IA, offrant des suggestions intelligentes pour des lignes ou des blocs de code entiers.

La force de GitHub Copilot réside dans son intégration avec OpenAI, puisant dans un vaste dépôt de code open-source pour fournir des suggestions contextuellement pertinentes et pratiques. Cela accélère non seulement la vitesse de codage, mais sert également d'outil d'apprentissage précieux, vous exposant à divers modèles de codage et meilleures pratiques.

Ce n'est pas un outil gratuit. Un abonnement peut vous coûter 10 $ par mois en tant qu'individu, ou il peut être acheté pour des équipes à un tarif réduit. Si vous souhaitez essayer GitHub Copilot, il y a actuellement une offre d'essai de 30 jours.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/212964557-8d832278-61bb-4288-a8a7-47f35859e868.gif align="left")

*GitHub Copilot utilisant l'autocomplétion intelligente sur une fonction.*

Il existe également des alternatives gratuites dont vous pouvez [lire plus ici](https://www.freecodecamp.org/news/ai-tools-to-use-in-vs-code/) (et je parle également de Tabnine ci-dessous).

## Thèmes d'icônes

Bien que VSCode inclue des icônes par défaut, l'incorporation de packs d'icônes offre un excellent moyen de booster la productivité et d'infuser une esthétique visuellement attrayante dans l'éditeur.

Les packs d'icônes offrent un ensemble d'icônes plus étendu et visuellement reconnaissable par rapport aux icônes par défaut. Cela peut faciliter la distinction visuelle entre les types de fichiers et les dossiers. Cela peut construire une reconnaissance intuitive et réduire la charge cognitive lors de la navigation dans les fichiers.

Il existe de nombreuses options en matière de choix d'un pack d'icônes. Trois choix populaires sont les [Material Theme Icons](https://marketplace.visualstudio.com/items?itemName=Equinusocio.vsc-material-theme-icons), [vscode-icons](https://marketplace.visualstudio.com/items?itemName=vscode-icons-team.vscode-icons), et [file-icons](https://marketplace.visualstudio.com/items?itemName=file-icons.file-icons).

Je trouve qu'un bon ensemble d'icônes améliore la lisibilité globale de l'explorateur de fichiers. J'apprécie les avantages supplémentaires de l'expérience visuelle améliorée.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Group-2.png align="left")

*Comparaison côte à côte de mon éditeur avec les icônes vscode (à gauche) et le thème d'icônes Material (à droite) activés. Il y a des icônes pour les types de fichiers et les dossiers qui indiquent ce qu'ils contiennent.*

## Indent Rainbow

[Indent Rainbow](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow) est une extension colorée que vous pouvez utiliser pour rendre l'indentation compréhensible, aidant à maintenir un code bien organisé et correctement indenté.

Chaque indentation est marquée avec une couleur différente, alternant entre 4 couleurs différentes. La représentation colorée de la structure est non seulement utile mais aussi visuellement attrayante. Cette extension est particulièrement utile pour les langages qui dépendent fortement de l'indentation comme YAML ou Python.

Si vous n'êtes pas amateur des couleurs par défaut, vous pouvez configurer les vôtres !

![Image](https://www.freecodecamp.org/news/content/images/2024/01/example--1-.png align="left")

*Une comparaison côte à côte de deux styles de Indent Rainbow. Celui de gauche montre les lignes de l'indentation en couleur vibrante et l'autre montre toute l'indentation dans un ton atténué.*

## Live Share

[Live Share](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare) est une extension de développement collaboratif, permettant le partage en temps réel.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-18-at-12.10.57-PM.png align="left")

*L'en-tête Live Share dans la place de marché des extensions. Il y a 15 millions d'installations.*

Cette extension vous aide à faciliter le travail d'équipe productif. Contrairement aux sessions traditionnelles de programmation en paire, Live Share vous permet de travailler ensemble tout en conservant vos propres préférences d'éditeur. Chaque personne a son propre curseur, et vous pouvez suivre les curseurs des autres dans la base de code.

Avec Live Share, il n'est pas nécessaire de cloner des dépôts ou de rencontrer des conflits lors du travail sur une branche partagée. Le contexte est immédiatement obtenu à partir de l'environnement lors de l'entrée dans une session.

## Conservation de la casse du curseur multiple

L'extension [Multiple Cursor Case Preserve](https://marketplace.visualstudio.com/items?itemName=Cardinal90.multi-cursor-case-preserve) est un outil qui booste la productivité et aide à l'édition rapide de code.

J'ai personnellement ressenti la frustration lorsque je ciblais plusieurs noms de variables dans un fichier pour les renommer, et que je remplaçais involontairement la casse lors d'une modification.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Example--1-.gif align="left")

*Ciblage de plusieurs variables avec le même mot mais une casse différente, et mise à jour de toutes de 'element' à 'node' avec la casse restant intacte.*

### Astuce : Édition multi-lignes dans VSCode

Profitez de ces raccourcis clavier Mac pour l'édition multi-lignes :

* **Cmd + D** : Sélectionnez rapidement un mot et appuyez à nouveau pour étendre la sélection aux occurrences séquentielles.
    
* **Alt + Shift + Haut/Bas** : Créez plusieurs curseurs au-dessus ou en dessous de votre curseur. Utilisez `Cmd + Droite/Gauche` pour naviguer chaque curseur à la fin ou au début de la ligne, et `Cmd + Gauche/Droite` pour atteindre le début ou la fin d'un mot.
    
* **Alt + Haut/Bas** : Déplacez la ligne actuelle vers le haut ou vers le bas. Combinez avec `Shift + Haut/Bas` pour sélectionner et déplacer plusieurs lignes simultanément, rationalisant ainsi votre processus d'édition de code.
    

En préservant la casse, cela rationalise le processus d'édition en réduisant l'effort manuel nécessaire pour corriger la casse.

## Path Intellisense

[Path Intellisense](https://marketplace.visualstudio.com/items?itemName=christian-kohler.path-intellisense) est un outil de productivité pour les chemins de fichiers. Il offre une autocomplétion intelligente qui suggère dynamiquement les chemins de fichiers et les noms de répertoires au fur et à mesure que vous tapez. Il peut minimiser les erreurs dues à des chemins de fichiers incomplets ou incorrects.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/iaHeUiDeTUZuo.gif align="left")

*Path Intellisense utilisé pour auto-compléter l'attribut 'href' d'un élément de lien avec un fichier style.css.*

Il est compatible avec une variété de langages de programmation. Mais si vous utilisez npm, le plugin [npm Intellisense](https://marketplace.visualstudio.com/items?itemName=christian-kohler.npm-intellisense) est recommandé spécifiquement.

## Paon

[Peacock](https://marketplace.visualstudio.com/items?itemName=johnpapa.vscode-peacock) est l'un de mes préférés, car j'aime ajouter plus de couleur à mon éditeur. Non seulement il encadre votre éditeur en couleur, mais il vous permet également de configurer des couleurs spécifiques pour chaque espace de travail, ce qui est très bénéfique lors des changements de contexte.

Peacock vient avec une gamme de couleurs présélectionnées, tout en permettant également des couleurs personnalisées définies par l'utilisateur.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/peacock-windows.png align="left")

*Une pile d'éditeurs de Peacock montrant les diverses options de couleur par défaut. La couleur est appliquée à la barre latérale et à la section inférieure de la fenêtre de l'éditeur.*

## Prettier

[Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) est un outil de formatage de code largement adopté avec plus de 40 millions d'installations. Il vous fournit une solution partagée pour améliorer la lisibilité du code.

Ce formateur de code opinionné impose un style cohérent dans une base de code. Avec le support de divers langages de programmation, Prettier analyse et formate automatiquement le code selon un ensemble de règles standardisées, éliminant ainsi les débats sur le style de codage et améliorant la collaboration.

L'intégration de Prettier avec "format on save" dans VSCode augmente considérablement la productivité en appliquant automatiquement le formatage, évitant ainsi tout temps passé sur des préoccupations de formatage manuel.

Vous avez probablement déjà entendu parler de Prettier, néanmoins il est important de le mentionner comme l'une des meilleures extensions à avoir.

## Gestionnaire de projets

[Project Manager](https://marketplace.visualstudio.com/items?itemName=alefragnani.project-manager) est un outil simple pour définir des projets (aka Favoris) et y accéder. Il inclut une section de barre latérale dédiée pour gérer tous vos projets en un seul endroit.

C'est un excellent outil lorsque vous avez beaucoup de projets à gérer et que vous devez fréquemment passer de l'un à l'autre. Il vient avec un ensemble de fonctionnalités pratiques comme la possibilité d'organiser davantage les projets par tags.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/vscode-project-manager-side-bar-tags.gif align="left")

*Exemple de Project Manager sur la façon de créer un tag en sélectionnant 'Edit Tags', en choisissant parmi les tags précédemment créés, et où les voir sous Favoris.*

## Tabnine

[Tabnine](https://marketplace.visualstudio.com/items?itemName=TabNine.tabnine-vscode) est un assistant de codage IA gratuit. Il peut aider à augmenter votre productivité en fournissant des complétions de code en temps réel.

Au-delà de la complétion de code de base, il prend en compte le contexte et offre des suggestions supplémentaires pertinentes. Cela peut être particulièrement utile lorsque vous travaillez dans des bases de code complexes nécessitant une exploration approfondie du code.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/completions-main.gif align="left")

*Exemple d'autocomplétion de Tabnine. L'autocomplétion est utilisée pour créer rapidement du code Python et TypeScript.*

Tabnine supporte de nombreux langages de programmation. L'apprentissage adaptatif est utilisé pour s'adapter au style de codage du développeur au fil du temps. Il y a un accent supplémentaire sur la confidentialité, car le code n'est jamais stocké ou partagé.

Comme je l'ai mentionné ci-dessus, Tabnine est souvent comparé à une alternative à GitHub Copilot, et vaut la peine d'être essayé sans coût. Gardez un œil sur celui-ci car ils ajoutent de nouvelles fonctionnalités compétitives.

Le support pour cette extension est solide avec des mises à jour continues. La fonctionnalité de chat est sur le point d'arriver, vous permettant de poser des questions et de générer tout, du code à la documentation.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/260391624-68c486fc-fa0d-4cfe-b8e1-432684b057d8.gif align="left")

*Exemple de Tabnine montrant à quoi ressemblera la nouvelle fonctionnalité de chat IA. L'utilisateur demande une API météo et Tabnine répond avec plusieurs exemples.*

## Mise en évidence TODO

Neubliez plus une autre tâche avec [TODO Highlight](https://marketplace.visualstudio.com/items?itemName=wayou.vscode-todo-highlight). Il met en évidence les `TODO` et autres annotations avec une mise en évidence colorée.

Il est courant de rencontrer un `TODO` ou un `FIXME` relique du passé dans une base de code qui existe depuis un certain temps. Ceux-ci peuvent être difficiles à se souvenir de supprimer. TODO Highlight est là pour vous aider à vous rappeler de ne pas laisser de trace.

Que votre thème soit clair ou sombre, TODO Highlight mettra en lumière les annotations.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/material-night-eighties.png align="left")

*Un peu de code JavaScript avec un TODO mis en évidence en jaune ainsi qu'un FIXME mis en évidence en rose.*

## Arborescence Todo

[Todo Tree](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree) offre une solution rapide et organisée pour découvrir les annotations. Il recherche dans votre espace de travail les `TODO` et autres annotations et les organise dans une arborescence de fichiers.

Il occupe une section spécifique dans la barre d'activité latérale. Cliquer sur chaque `TODO` ouvre le fichier correspondant, où le `TODO` est mis en évidence pour une attention immédiate.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/screenshot.png align="left")

*La section de la barre latérale de Todo Tree avec un todo sélectionné 'TODO Fix this!'. Dans le code à droite, le 'TODO' est mis en évidence avec une couleur violette vive.*

## Résumé

VSCode se distingue par son écosystème d'extensions expansif, en faisant un choix de prédilection pour les développeurs. Ayant testé en profondeur une gamme d'extensions populaires, j'ai soigneusement sélectionné cette liste de mes meilleures recommandations.

Cette liste est un excellent point de départ pour commencer et construire. Je vous encourage vivement à mettre en place des périodes d'essai routinières avec de nouvelles extensions. Explorez d'autres extensions via la [recherche d'extensions Visual Studio Code](https://marketplace.visualstudio.com/vscode).

Reconnaissant l'importance de minimiser la charge cognitive pour une concentration soutenue, chaque extension de cette liste est choisie avec l'objectif de réduire les fardeaux mentaux inutiles comme les changements de contexte. Faites de VSCode votre principal hub de besoins de développement, et vous obtiendrez un mode de concentration amélioré ainsi que d'autres avantages.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-23-at-10.33.01-AM-1.png align="left")

J'espère que ces recommandations vous permettront d'optimiser votre flux de travail, de minimiser les distractions et, en fin de compte, de booster votre productivité !