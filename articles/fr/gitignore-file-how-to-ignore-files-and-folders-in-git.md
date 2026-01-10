---
title: Fichier .gitignore – Comment ignorer des fichiers et dossiers dans Git
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-08-23T16:58:02.000Z'
originalURL: https://freecodecamp.org/news/gitignore-file-how-to-ignore-files-and-folders-in-git
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/pexels-ken-tomita-389819.jpg
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: Fichier .gitignore – Comment ignorer des fichiers et dossiers dans Git
seo_desc: 'Git is a popular version control system. It is how developers can collaborate
  and work together on projects.

  Git allows you to track the changes you make to your project over time. On top of
  that, it lets you revert to a previous version if you want ...'
---

Git est un système de contrôle de version populaire. C'est ainsi que les développeurs peuvent collaborer et travailler ensemble sur des projets.

Git vous permet de suivre les modifications que vous apportez à votre projet au fil du temps. En plus de cela, il vous permet de revenir à une version précédente si vous souhaitez annuler une modification.

La manière dont Git fonctionne est que vous mettez en attente des fichiers dans un projet avec la commande `git add`, puis vous les validez avec la commande `git commit`.

Lorsque vous travaillez sur un projet en tant que membre d'une équipe, il y aura des moments où vous ne voudrez pas partager certains fichiers ou parties du projet avec les autres.

En d'autres termes, vous ne voulez pas inclure ou *valider* ces fichiers spécifiques dans la version principale du projet. C'est pourquoi vous ne voudrez peut-être pas utiliser le point `.` avec la commande `git add`, car cela met en attente chaque fichier dans le répertoire Git actuel.

Lorsque vous utilisez la commande `git commit`, chaque fichier est validé – cela inclut également les fichiers qui n'ont pas besoin de l'être ou qui ne devraient pas l'être.

Vous voudrez peut-être que Git ignore des fichiers spécifiques, mais il n'existe pas de commande `git ignore` à cet effet.

Alors, comment dire à Git d'ignorer et de ne pas suivre des fichiers spécifiques ? Avec un fichier `.gitignore`.

Dans cet article, vous apprendrez ce qu'est un fichier `.gitignore`, comment en créer un et comment l'utiliser pour ignorer des fichiers et des dossiers. Vous verrez également comment ignorer un fichier précédemment validé.

Voici ce que nous allons couvrir :

1. [Qu'est-ce qu'un fichier `.gitignore` ?](#introduction)
    1. [Comment créer un fichier `.gitignore`](#creation)
    2. [Que mettre dans un fichier `.gitignore` ?](#contenu)
2. [Comment ignorer un fichier et un dossier dans Git](#ignorer-fichier)
    1. [Comment ignorer un fichier précédemment validé](#fichier-deja-valide)

## Qu'est-ce qu'un fichier `.gitignore` ? À quoi sert un fichier `.gitignore` ? <a name="introduction"></a>

Chacun des fichiers dans un dépôt Git en cours d'utilisation est soit :

- **suivi** – ce sont tous les fichiers ou répertoires que Git connaît. Ce sont les fichiers et répertoires nouvellement mis en attente (ajoutés avec `git add`) et validés (validés avec `git commit`) dans le dépôt principal.
- **non suivi** – ce sont tous les nouveaux fichiers ou répertoires créés dans le répertoire de travail mais qui n'ont pas encore été mis en attente (ou ajoutés en utilisant la commande `git add`).
- **ignoré** – ce sont tous les fichiers ou répertoires que Git sait exclure complètement, ignorer et ne pas prendre en compte dans le dépôt Git. Essentiellement, c'est un moyen de dire à Git quels fichiers non suivis doivent rester non suivis et ne jamais être validés.

Tous les fichiers ignorés sont stockés dans un fichier `.gitignore`.

Un fichier `.gitignore` est un fichier texte brut qui contient une liste de tous les fichiers et dossiers spécifiés du projet que Git doit ignorer et ne pas suivre.

Dans `.gitignore`, vous pouvez dire à Git d'ignorer uniquement un seul fichier ou un seul dossier en mentionnant le nom ou le motif de ce fichier ou dossier spécifique. Vous pouvez également dire à Git d'ignorer plusieurs fichiers ou dossiers en utilisant la même méthode.

### Comment créer un fichier `.gitignore` <a name="creation"></a>

Typiquement, un fichier `.gitignore` est placé dans le répertoire racine du dépôt. Le répertoire racine est également connu sous le nom de parent et de répertoire de travail actuel. Le dossier racine contient tous les fichiers et autres dossiers qui composent le projet.

Cela dit, vous pouvez le placer dans n'importe quel dossier du dépôt. Vous pouvez même avoir plusieurs fichiers `.gitignore`, d'ailleurs.

Pour créer un fichier `.gitignore` sur un système basé sur Unix tel que macOS ou Linux en utilisant la ligne de commande, ouvrez l'application terminal (comme Terminal.app sur macOS). Ensuite, naviguez jusqu'au dossier racine qui contient le projet en utilisant la commande `cd` et entrez la commande suivante pour créer un fichier `.gitignore` pour votre répertoire :

```bash
touch .gitignore
```

Les fichiers avec un point (`.`) précédant leur nom sont cachés par défaut.

Les fichiers cachés ne sont pas visibles lorsque vous utilisez la commande `ls` seule. Pour voir tous les fichiers – y compris les fichiers cachés – depuis la ligne de commande, utilisez le drapeau `-a` avec la commande `ls` comme suit :

```bash
ls -a
```

### Que mettre dans un fichier `.gitignore` <a name="contenu"></a>

Les types de fichiers que vous devriez envisager d'ajouter à un fichier `.gitignore` sont tous les fichiers qui n'ont pas besoin d'être validés.

Vous ne voudrez peut-être pas les valider pour des raisons de sécurité ou parce qu'ils sont locaux à vous et donc inutiles pour les autres développeurs travaillant sur le même projet que vous.

Certains d'entre eux peuvent inclure :

- Les fichiers du système d'exploitation. Chaque système d'exploitation (comme macOS, Windows et Linux) génère des fichiers cachés spécifiques au système que les autres développeurs n'ont pas besoin d'utiliser puisque leur système les génère également. Par exemple, sur macOS, Finder génère un fichier `.DS_Store` qui inclut les préférences de l'utilisateur pour l'apparence et l'affichage des dossiers, comme la taille et la position des icônes.
- Les fichiers de configuration générés par des applications telles que les éditeurs de code et les IDE (IDE signifie Environnement de Développement Intégré). Ces fichiers sont personnalisés pour vous, vos configurations et vos paramètres de préférences.
- Les fichiers qui sont générés automatiquement à partir du langage de programmation ou du framework que vous utilisez dans votre projet et les fichiers spécifiques au code compilé, comme les fichiers `.o`.
- Les dossiers générés par les gestionnaires de paquets, comme le dossier `node_modules` de npm. Il s'agit d'un dossier utilisé pour sauvegarder et suivre les dépendances de chaque paquet que vous installez localement.
- Les fichiers qui contiennent des données sensibles et des informations personnelles. Certains exemples de tels fichiers sont les fichiers avec vos identifiants (nom d'utilisateur et mot de passe) et les fichiers avec des variables d'environnement comme les fichiers `.env` (les fichiers `.env` contiennent des clés API qui doivent rester sécurisées et privées).
- Les fichiers `runtime`, comme les fichiers `.log`. Ils fournissent des informations sur les activités d'utilisation du système d'exploitation et les erreurs, ainsi qu'un historique des événements qui se sont produits au sein du système d'exploitation.

### Comment ignorer un fichier et un dossier dans Git <a name="ignorer-fichier"></a>

Si vous voulez ignorer un seul fichier spécifique, vous devez fournir le chemin complet vers le fichier à partir de la racine du projet.

Par exemple, si vous voulez ignorer un fichier `text.txt` situé dans le répertoire racine, vous feriez ce qui suit :

```bash
/text.txt
```

Et si vous vouliez ignorer un fichier `text.txt` situé dans un répertoire `test` au niveau du répertoire racine, vous feriez ce qui suit :

```bash
/test/text.txt
```

Vous pourriez également écrire ce qui précède comme suit :

```bash
test/text.txt
```

Si vous voulez ignorer tous les fichiers avec un nom spécifique, vous devez écrire le nom littéral du fichier.

Par exemple, si vous vouliez ignorer tous les fichiers `text.txt`, vous ajouteriez ce qui suit à `.gitignore` :

```bash
text.txt
```

Dans ce cas, vous n'avez pas besoin de fournir le chemin complet vers un fichier spécifique. Ce motif ignorera tous les fichiers avec ce nom particulier qui sont situés n'importe où dans le projet.

Pour ignorer un répertoire entier avec tout son contenu, vous devez inclure le nom du répertoire avec une barre oblique `/` à la fin :

```bash
test/
```

Cette commande ignorera tout répertoire (y compris d'autres fichiers et sous-répertoires à l'intérieur du répertoire) nommé `test` situé n'importe où dans votre projet.

Une chose à noter est que si vous écrivez le nom d'un fichier seul ou le nom du répertoire seul sans la barre oblique `/`, alors ce motif correspondra à la fois à tout fichier ou répertoire avec ce nom :

```bash
# correspond à tout fichier et répertoire avec le nom test
test
```

Que faire si vous voulez ignorer tout fichier ou répertoire qui *commence* par un mot spécifique ?

Supposons que vous voulez ignorer tous les fichiers et répertoires dont le nom commence par `img`. Pour ce faire, vous devrez spécifier le nom que vous voulez ignorer suivi du sélecteur générique `*` comme suit :

```bash
img*
```

Cette commande ignorera tous les fichiers et répertoires dont le nom commence par `img`.

Mais que faire si vous voulez ignorer tout fichier ou répertoire qui *se termine* par un mot spécifique ?

Si vous vouliez ignorer tous les fichiers qui se terminent par une extension de fichier spécifique, vous devrez utiliser le sélecteur générique `*` suivi de l'extension de fichier que vous voulez ignorer.

Par exemple, si vous vouliez ignorer tous les fichiers markdown qui se terminent par une extension de fichier `.md`, vous ajouteriez ce qui suit à votre fichier `.gitignore` :

```bash
*.md
```

Ce motif correspondra à tout fichier se terminant par l'extension `.md` situé n'importe où dans le projet.

Plus tôt, vous avez vu comment ignorer tous les fichiers se terminant par un suffixe spécifique. Que se passe-t-il lorsque vous voulez faire une exception, et qu'il y a un fichier avec ce suffixe que vous *ne voulez pas* ignorer ?

Supposons que vous avez ajouté ce qui suit à votre fichier `.gitignore` :

```bash
.md
```

Ce motif ignore tous les fichiers se terminant par `.md`, mais vous *ne voulez pas* que Git ignore un fichier `README.md`.

Pour ce faire, vous devrez utiliser le motif de négation avec un point d'exclamation, `!`, pour négocier un fichier qui serait autrement ignoré :

```bash
# ignore tous les fichiers .md
.md

# ne pas ignorer le fichier README.md
!README.md
```

Avec ces deux motifs dans le fichier `.gitignore`, tous les fichiers se terminant par `.md` sont ignorés sauf le fichier `README.md`.

Une chose à garder à l'esprit est que ce motif ne fonctionnera pas si vous ignorez un répertoire entier.

Supposons que vous ignoriez tous les répertoires `test` :

```bash
test/
```

Supposons que dans un dossier `test`, vous avez un fichier, `example.md`, que vous *ne voulez pas* ignorer.

Vous *ne pouvez pas* négocier un fichier à l'intérieur d'un répertoire ignoré comme suit :

```bash
# ignorer tous les répertoires avec le nom test
test/

# essayer de négocier un fichier à l'intérieur d'un répertoire ignoré ne fonctionnera pas
!test/example.md
```

### Comment ignorer un fichier précédemment validé <a name="fichier-deja-valide"></a>

Il est une bonne pratique de créer un fichier `.gitignore` avec tous les fichiers et les différents motifs de fichiers que vous voulez ignorer lorsque vous créez un nouveau dépôt – avant de le valider.

Git ne peut ignorer que les fichiers non suivis qui n'ont pas encore été validés dans le dépôt.

Que se passe-t-il lorsque vous avez déjà validé un fichier dans le passé et que vous souhaitez ne pas l'avoir fait ?

Supposons que vous avez accidentellement validé un fichier `.env` qui stocke des variables d'environnement.

Vous devez d'abord mettre à jour le fichier `.gitignore` pour inclure le fichier `.env` :

```bash
# ajouter le fichier .env à .gitignore
echo ".env" >> .gitignore
```

Maintenant, vous devrez dire à Git de ne pas suivre ce fichier en le supprimant de l'index :

```bash
git rm --cached .env
```

La commande `git rm`, avec l'option `--cached`, supprime le fichier du dépôt mais ne supprime pas le fichier réel. Cela signifie que le fichier reste sur votre système local et dans votre répertoire de travail en tant que fichier ignoré.

Un `git status` montrera que le fichier n'est plus dans le dépôt, et entrer la commande `ls` montrera que le fichier existe sur votre système de fichiers local.

Si vous voulez supprimer le fichier du dépôt et de votre système local, omettez l'option `--cached`.

Ensuite, ajoutez le `.gitignore` à la zone de staging en utilisant la commande `git add` :

```bash
git add .gitignore
```

Enfin, validez le fichier `.gitignore` en utilisant la commande `git commit` :

```bash
git commit -m "mettre à jour les fichiers ignorés"
```

## Conclusion

Et voilà – vous connaissez maintenant les bases pour ignorer des fichiers et des dossiers dans Git.

Espérons que vous avez trouvé cet article utile.

Pour en savoir plus sur Git, consultez les ressources gratuites suivantes :

- [Git et GitHub pour les débutants - Cours accéléré](https://www.youtube.com/watch?v=RGOj5yH7evk)
- [Tutoriel Git pour les professionnels - Outils et concepts pour maîtriser le contrôle de version avec Git](https://www.youtube.com/watch?v=Uszj_k0DGsg)
- [Tutoriel avancé Git - Rebase interactif, Cherry-Picking, Reflog, Submodules et plus](https://www.youtube.com/watch?v=qsTthZi23VE)


Merci d'avoir lu et bon codage :)