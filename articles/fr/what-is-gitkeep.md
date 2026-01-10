---
title: Qu'est-ce que .gitkeep ? Comment suivre et pousser des dossiers vides dans
  Git
subtitle: ''
author: Kealan Parr
co_authors: []
series: null
date: '2021-11-15T18:07:41.000Z'
originalURL: https://freecodecamp.org/news/what-is-gitkeep
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/Capture.JPG
tags:
- name: Git
  slug: git
- name: how-to
  slug: how-to
- name: version control
  slug: version-control
seo_title: Qu'est-ce que .gitkeep ? Comment suivre et pousser des dossiers vides dans
  Git
seo_desc: 'Let''s say you need to completely restructure the directories of your codebase.

  You need to move some folders higher, move some other folders lower, and move lots
  of files into some new folders you''re going to create.

  You start shifting the code aroun...'
---

Disons que vous devez complètement restructurer les répertoires de votre base de code.

Vous devez déplacer certains dossiers plus haut, déplacer d'autres dossiers plus bas, et déplacer de nombreux fichiers dans de nouveaux dossiers que vous allez créer.

Vous commencez à déplacer le code, à vérifier que tout fonctionne, et à ajouter certains dossiers dont le prochain projet aura besoin.

Ces nouveaux dossiers sont vides pour le moment. Mais le prochain projet commence dans 2 jours et il est préférable d'ajouter ces nouveaux dossiers puisque vous êtes déjà en train de restructurer la base de code.

Vous poussez tout dans votre branche de projet et vous êtes prêt pour que quelqu'un fasse un QA. Vous dites donc au relecteur de code sur Slack que vous avez terminé.

Ils clonent alors votre branche et échouent votre relecture de code parce que vous avez oublié d'ajouter tous les nouveaux dossiers que vous aviez promis d'ajouter.

Attendez.... quoi ?

# Qu'est-il arrivé ?

[git ne peut pas pousser des répertoires vides.](https://git.wiki.kernel.org/index.php/Git_FAQ#Can_I_add_empty_directories.3F) Il ne peut suivre que les fichiers.

Si vous essayez de pousser un dossier vide, bien qu'il existera sur votre machine locale, rien n'ira dans votre branche.

Ainsi, si quelqu'un essaie de cloner votre code, il n'aura pas la même structure de dossiers que vous sur votre machine locale.

Alors, si cela ne fonctionne pas, que devez-vous faire ?

# Comment utiliser .gitkeep

Maintenant, nous savons que Git ne suit que les fichiers, donc nous savons que nous devons ajouter quelque chose au dossier.

Vous pouvez ajouter n'importe quoi. Vous devez simplement ajouter un fichier factice très simple pour vous assurer que le dossier est suivi et sera poussé.

Vous pourriez copier et coller un fichier texte `file.txt` sans rien dedans, et cela fonctionnerait. Vous pourriez mettre une image PNG d'un chat.

Une pratique courante et standardisée pour résoudre ce problème exact, cependant, est de pousser un fichier appelé `.gitkeep` dans vos dossiers vides.

Ce n'est pas une fonctionnalité de Git ! Vous pourriez donc le nommer n'importe comment. Il n'y a rien de spécial dans le nom `.gitkeep` – certains développeurs ajoutent `.gitignore` à la place, par exemple.

`.gitignore` est un peu confus, cependant, car vous essayez de faire en sorte que git **ne** ignore pas votre fichier, et le pousse réellement dans votre branche.

Dans tous les cas, en ajoutant ce simple fichier à vos dossiers, ils seront poussés au moment venu.

# Conclusion

`.gitkeep` est une chose courante que vous verrez dans les bases de code, où un dossier vide doit être suivi via Git.

Le nom du fichier factice n'est pas toujours `.gitkeep`, mais vous verrez cette pratique encore et encore en tant que développeur.

Je tweete mes articles [ici](https://twitter.com/kealanparr) si vous souhaitez lire plus de mes écrits.