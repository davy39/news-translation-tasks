---
title: Comment ouvrir n'importe quel dépôt dans VS Code sans le cloner
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-06-15T16:06:54.000Z'
originalURL: https://freecodecamp.org/news/you-can-now-edit-anything-on-github-in-vs-code-without-cloning
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/window.jpg
tags:
- name: Productivity
  slug: productivity
- name: Visual Studio Code
  slug: visual-studio-code
- name: Visual Studio Code
  slug: vscode
seo_title: Comment ouvrir n'importe quel dépôt dans VS Code sans le cloner
seo_desc: "By Burke Holland\nYou can now open anything (that you have access to) on\
  \ GitHub directly from VS Code with the official Remote Repositories extension.\
  \ \nAnd I do mean directly. That means no clone. No download. No looking at your\
  \ dev folder and wonderi..."
---

Par Burke Holland

Vous pouvez maintenant ouvrir n'importe quoi (auquel vous avez accès) sur GitHub directement depuis VS Code avec l'extension officielle [Remote Repositories](https://marketplace.visualstudio.com/items?itemName=GitHub.remotehub&WT.mc_id=devcloud-18509-cxa).

Et je veux dire _directement_. Cela signifie pas de clone. Pas de téléchargement. Pas de regard sur votre dossier de développement en vous demandant pourquoi diantre vous avez structuré vos projets de cette manière et OMG TELLEMENT DE REGRETS.

Écoutez, c'est bon. Personne n'est heureux de la façon dont il a encombré son environnement de développement autrefois immaculé. Dans mon dossier "c:\dev", il y a une saison entière de [Hoarders](https://www.aetv.com/shows/hoarders) et non, je ne vais pas supprimer ce projet jQuery. J'en aurai peut-être besoin un jour.

Regardons comment la nouvelle extension Remote Repositories pour VS Code vous permet d'interagir facilement avec n'importe quel projet sur GitHub sans avoir à cloner quoi que ce soit.

## Comment installer l'extension Remote Repositories

Tout d'abord, vous devrez installer l'extension [Remote Repositories](https://marketplace.visualstudio.com/items?itemName=GitHub.remotehub&WT.mc_id=devcloud-18509-cxa) de GitHub pour Visual Studio Code.

%[https://marketplace.visualstudio.com/items?itemName=GitHub.remotehub&WT.mc_id=devcloud-18509-cxa]

Pour ouvrir un dépôt GitHub, cliquez sur l'indicateur vert dans le coin inférieur gauche de VS Code.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-64.png)

Vous verrez une nouvelle option pour "Open Remote Repository".

Si vous avez d'autres extensions Remote pour VS Code installées, vous verrez beaucoup plus d'options dans cette liste, alors cherchez simplement la bonne.

Vous pouvez également accéder à cette option depuis la Palette de commandes si cliquer sur des choses avec une souris est trop fastidieux. Je vous vois, les gens de VIM.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-65.png)

Vous pouvez coller l'URL d'un dépôt GitHub si vous l'avez par hasard sur votre presse-papiers (bizarre) OU vous pouvez parcourir GitHub en sélectionnant "Open Repository from GitHub". La troisième option vous permet d'ouvrir une branche de Pull Request afin de la ~~prétendre~~ examiner minutieusement.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-66.png)

VS Code se rouvrira et vous verrez ce dépôt comme si vous travailliez avec lui localement. Mais ce n'est pas le cas. Vous le regardez _sur_ GitHub _à travers_ la fenêtre de VS Code.

Vous remarquerez des avertissements concernant "certaines fonctionnalités" non disponibles et que vous êtes en "Mode Restreint".

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-145.png)

Cela fait partie des nouveaux paramètres d'espace de travail de confiance dans VS Code.

%[https://code.visualstudio.com/docs/editor/workspace-trust?WT.mc_id=devcloud-30876-buhollan]

Par défaut, VS Code désactive désormais les tâches, le débogage, certains paramètres d'espace de travail et toute extension qui pourrait essayer d'exécuter quelque chose la première fois que vous ouvrez un dossier. Vous devez dire à VS Code que c'est bon, vous connaissez et faites confiance à ce code et vous êtes sûr à 100 % qu'il ne va pas [fermer votre pipeline de pétrole](https://www.nytimes.com/2021/05/08/us/politics/cyberattack-colonial-pipeline.html).

Ok – donc les avertissements de sécurité effrayants écartés, que pouvons-nous faire ici ?

## Comment travailler avec un dépôt distant

Vous avez des capacités d'édition complètes avec une grande différence étant que vous n'avez pas à sauvegarder quoi que ce soit. Vos modifications sont simplement sauvegardées au fur et à mesure.

Elles ne sont pas automatiquement validées sur GitHub. Pour que les modifications soient sauvegardées dans le dépôt, vous devriez les valider depuis la vue de contrôle de source.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-68.png)

Vous n'avez pas à les pousser car vous êtes déjà sur GitHub. Un commit est un commit – pas besoin de push. C'est la même chose que si vous éditiez le fichier directement sur GitHub. Parce que vous le faites essentiellement.

En ce qui concerne l'édition, vous obtenez beaucoup de ce à quoi vous vous attendez dans VS Code.

L'intellisense spécifique au langage fonctionne. Par exemple, si vous commencez à écrire un `fetch`, VS Code vous aidera avec cela parce qu'il connaît `fetch`.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-69.png)

Mais vous n'obtenez pas l'intellisense sur les fichiers de projet que VS Code vous donne lorsqu'il exécute votre projet localement.

Par exemple – localement, VS Code connaît `useEffect` qui provient de l'import `react`. Il le sait parce qu'il inspecte l'import qui est un module node.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-34.png)

Mais avec Remote Repositories, nous regardons directement GitHub et le dossier node_modules n'est jamais poussé vers GitHub sauf si vous êtes moi il y a 10 ans. Il n'y a donc pas d'intellisense pour `useEffect` parce que ce code n'existe pas réellement dans le dépôt.

Vous pouvez utiliser des outils comme Emmet pour composer du HTML et vous obtenez le bel aperçu Markdown en écran divisé que vous aimez probablement comme moi.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-35.png)

Vous pouvez également utiliser "Rechercher" et "Rechercher dans les fichiers".

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-37.png)

De nombreuses choses qui fonctionnent localement fonctionnent de la même manière lorsqu'elles sont connectées à un projet directement sur GitHub, mais certaines ne fonctionnent pas. Ce qui est la chose la plus vague que quiconque ait jamais écrite sur Internet, mais comprendre comment tout cela fonctionne éclairera ce à quoi vous pouvez raisonnablement vous attendre.

## Comment cela fonctionne

VS Code dispose d'une [API de fournisseur de système de fichiers](https://github.com/microsoft/vscode/blob/dc8bd9cd7e5231745549ac6218266c63271f48cd/src/vs/vscode.d.ts#L7038) qui existe depuis un certain temps. Ce que fait cette API, c'est fournir un mécanisme pour consommer une API comme si c'était un fichier physique. Dans ce cas, l'extension Remote Repositories consomme et mappe l'API GitHub vers un "Espace de travail virtuel" dans VS Code.

Cela signifie que toute extension qui essaie de travailler avec des fichiers physiques ne fonctionnera pas **jusqu'à ce que** **l'auteur de l'extension met à jour son extension pour utiliser l'API du système de fichiers virtuel**. Ce qui signifie que les choses qui ne fonctionnent pas aujourd'hui pourraient fonctionner à l'avenir à mesure que les extensions sont mises à jour.

Alors, à quoi pouvez-vous vous attendre de fonctionner ? Les thèmes, les raccourcis clavier, les extraits de code et les extensions de grammaire. Ces types d'extensions n'exécutent généralement aucun code, donc vous savez qu'ils n'essaient pas de travailler avec des fichiers, ce qui signifie qu'il est sûr (sûr sur Internet) de supposer qu'ils fonctionneront dans Remote Repositories.

Mais certaines choses ne fonctionneront jamais parce que vous avez besoin d'un accès local aux fichiers pour les faire.

Un exemple typique de cela est Prettier. Prettier est un outil CLI qui modifie vos fichiers locaux en reformattant votre code. Puisqu'il n'y a pas d'accès local aux fichiers, il ne fonctionne pas actuellement avec Remote Repositories. Donc personne ne va changer ces guillemets doubles en simples automatiquement ou remettre ce point-virgule. Ou l'enlever. Je veux sortir de ce paragraphe.

En fait, vous ne pouvez pas _exécuter_ un projet Remote Repositories du tout. Si vous ouvrez le terminal tout en étant connecté à un Remote Repository, il sera là. Mais il n'aura aucun accès à ce projet.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-70.png)

Ce qui est légitime parce que le projet n'existe pas réellement sur votre machine. Alors, comment obtenez-vous un terminal si vous trouvez que vous voulez vraiment exécuter le code sur lequel vous travaillez, ou simplement améliorer votre expérience d'édition à un VS Code à part entière ?

## Comment passer à VS Code complet

> "Continue sur mon chemin, mon fils égaré" - [un groupe des années 70](https://www.youtube.com/watch?v=2X_2IdybTV0)

Si vous cliquez sur cette partie verte en bas à gauche de la barre d'état qui dit "GitHub" en ce moment, vous verrez une option pour "Continue Working On".

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-71.png)

Cette option vous permettra soit de cloner le projet localement, soit de l'ouvrir dans un GitHub Codespace.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-72.png)

Si vous êtes dans la bêta Codespaces (_[demander l'accès ici](https://github.com/features/codespaces)_), vous pouvez ouvrir le dépôt dans un Codespace. Il s'agit de VS Code s'exécutant dans le navigateur, mais soutenu par un environnement de calcul où vous pouvez exécuter n'importe quoi comme si c'était sur votre bureau. Cela fonctionne parce que VS Code a été initialement conçu pour être une application web. Vraie histoire.

Ou clonez-le localement ! Ouvrez ce dossier `c:\Users\you\Documents\GitHub` que vous regrettez d'avoir choisi pour mettre tous vos projets parce que maintenant votre dossier "Documents" est sauvegardé sur OneDrive et il contient 900 téraoctets de node_modules. Eh bien - maintenant il en contient 920.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-77.png)
_Crédit : Une âme brillante. Veuillez commenter et prendre le crédit pour cette œuvre de génie._

## Cool. Mais pourquoi ?

La question naturelle que vous devriez vous poser maintenant est : "Très cool ! Mais pourquoi en ai-je besoin ?"

Excellente question. Vous êtes perspicace et les gens vous aiment.

Considérez les scénarios suivants...

* **Vous voulez parcourir un dépôt GitHub et regarder le code.** GitHub est un excellent site, mais ce n'est pas le meilleur moyen de sauter rapidement entre les fichiers et d'examiner un projet. Vous avez vraiment besoin d'un éditeur pour cela et Remote Repositories supprime l'étape fastidieuse et souvent intensive en bande passante de cloner simplement pour regarder le code.
* **Vous voulez faire une mise à jour rapide.** Bien que vous feriez presque toujours du codage lourd localement, vous pourriez vouloir sauter dans un dépôt et faire un changement rapide sans avoir à synchroniser votre environnement local. Les README viennent à l'esprit, mais cela pourrait être n'importe quel type de petit changement.
* **Vous travaillez sur du Markdown.** Si vous travaillez sur de la documentation, des README ou d'autres Markdown sur GitHub, il n'est plus nécessaire de cloner le dépôt localement pour cela. À moins que vous ne fassiez tourner un serveur local pour prévisualiser ce Markdown, utiliser l'aperçu intégré est un moyen beaucoup plus rapide de taper 5K mots sur votre API.
* **Vous voulez examiner une PR.** Cela semble évident.

## Obtenez plus de Remote

Maintenant que vous avez Remote Repositories, vous pouvez nettoyer ce dossier de développement. Faites simplement un clic droit et supprimez quelque chose. Voyez comme cela fait du bien ?

Remote Repositories est l'une des plusieurs façons de faire du développement "Remote" avec VS Code. Découvrez ces autres options pour utiliser VS Code pour vous connecter à presque n'importe quoi.

* [Dev Containers](https://code.visualstudio.com/docs/remote/containers?WT.mc_id=devcloud-30876-buhollan) - Utilisez un conteneur Docker comme environnement de développement complet avec
* [Remote SSH](https://code.visualstudio.com/docs/remote/ssh?WT.mc_id=devcloud-30876-buhollan) - Ouvrez un dossier distant dans VS Code sur n'importe quelle machine distante via une connexion SSH
* [Remote WSL](https://code.visualstudio.com/docs/remote/wsl?WT.mc_id=devcloud-30876-buhollan) - Pour utiliser votre WSL comme environnement d'exécution de support à temps plein dans VS Code.