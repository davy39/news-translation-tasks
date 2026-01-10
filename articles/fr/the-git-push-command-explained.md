---
title: La commande Git Push expliquée
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-03T21:52:00.000Z'
originalURL: https://freecodecamp.org/news/the-git-push-command-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e41740569d1a4ca3c2d.jpg
tags:
- name: Git
  slug: git
seo_title: La commande Git Push expliquée
seo_desc: 'The git push command allows you to send (or push) the commits from your
  local branch in your local Git repository to the remote repository.

  To be able to push to your remote repository, you must ensure that all your changes
  to the local repository ar...'
---

La commande `git push` vous permet d'envoyer (ou de _pousser_) les commits de votre branche locale dans votre dépôt Git local vers le dépôt distant.

Pour pouvoir pousser vers votre dépôt distant, vous devez vous assurer que **toutes vos modifications dans le dépôt local sont validées**.

La syntaxe de cette commande est la suivante :

```bash
git push <nom-du-dépôt> <nom-de-la-branche>
```

Il existe plusieurs options différentes que vous pouvez passer avec la commande, vous pouvez en apprendre plus à leur sujet dans la [documentation Git](https://git-scm.com/docs/git-push#_options_a_id_options_a) ou exécuter `git push --help`.

### **Pousser vers un dépôt distant et une branche spécifiques**

Pour pousser du code, vous devez d'abord cloner un dépôt sur votre machine locale.

```bash
# Une fois le dépôt cloné, vous travaillerez dans la branche par défaut (par défaut, c'est `master`)
git clone https://github.com/<utilisateur-git>/<nom-du-dépôt> && cd <nom-du-dépôt>
# faites des modifications et ajoutez vos fichiers (répétez la commande `git add` pour chaque fichier, ou utilisez `git add .` pour tout ajouter)
git add <nom-du-fichier>
# validez maintenant votre code
git commit -m "ajouté des modifications à mon dépôt !"
# poussez les modifications de la branche `master` vers github
git push origin master
```

Pour en savoir plus sur les branches, consultez les liens ci-dessous :

* [git checkout](https://github.com/renington/guides/blob/master/src/pages/git/git-checkout/index.md)
* [git branch](https://github.com/renington/guides/blob/master/src/pages/git/git-branch/index.md)

### **Pousser vers un dépôt distant spécifique et toutes ses branches**

Si vous souhaitez pousser toutes vos modifications vers le dépôt distant et toutes ses branches, vous pouvez utiliser :

```bash
git push --all <NOM-DU-DÉPÔT-DISTANT>
```

où :

* `--all` est le drapeau qui indique que vous souhaitez pousser toutes les branches vers le dépôt distant
* `NOM-DU-DÉPÔT-DISTANT` est le nom du dépôt distant vers lequel vous souhaitez pousser

### **Pousser vers une branche spécifique avec le paramètre force**

Si vous souhaitez ignorer les modifications locales apportées au dépôt Git sur GitHub (ce que la plupart des développeurs font pour une correction rapide sur le serveur de développement), vous pouvez utiliser la commande `--force` pour pousser en ignorant ces modifications.

```bash
git push --force <NOM-DU-DÉPÔT-DISTANT> <NOM-DE-LA-BRANCHE>
```

où :

* `NOM-DU-DÉPÔT-DISTANT` est le nom du dépôt distant vers lequel vous souhaitez pousser les modifications
* `NOM-DE-LA-BRANCHE` est le nom de la branche distante vers laquelle vous souhaitez pousser vos modifications

### **Pousser en ignorant le hook pre-push de Git**

Par défaut, `git push` déclenchera le paramètre `--verify`. Cela signifie que Git exécutera tout script client-side pre-push qui peut avoir été configuré. Si le script pre-push échoue, la commande git push échouera également. (Les hooks pre-push sont utiles pour faire des choses comme vérifier si les messages de commit respectent les normes de l'entreprise, exécuter des tests unitaires, etc.). Parfois, vous pouvez souhaiter ignorer ce comportement par défaut, par exemple dans le scénario où vous souhaitez pousser vos modifications vers une branche de fonctionnalité pour qu'un autre contributeur les récupère, mais vos modifications en cours de travail cassent les tests unitaires. Pour ignorer le hook, entrez simplement votre commande de push et ajoutez le drapeau `--no-verify`

```bash
git push --no-verify
```

### **Plus d'informations :**

* [Documentation Git - push](https://git-scm.com/docs/git-push)
* [Hooks Git](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks)