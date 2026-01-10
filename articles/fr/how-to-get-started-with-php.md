---
title: Tutoriel PHP – Comment installer PHP et XAMPP pour votre projet
subtitle: ''
author: Okoro Emmanuel Nzube
co_authors: []
series: null
date: '2022-06-02T15:11:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-php
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/PHP.jpg
tags:
- name: PHP
  slug: php
seo_title: Tutoriel PHP – Comment installer PHP et XAMPP pour votre projet
seo_desc: 'Hello and welcome to this tutorial, everyone. Today, we''ll look at how
  you can set up and use PHP in a project.

  But before we get started, we''ll need to understand what PHP is all about.

  What is PHP?

  PHP is an abbreviation or acronym for "Hypertext P...'
---

Bonjour et bienvenue dans ce tutoriel, à tous. Aujourd'hui, nous allons voir comment installer et utiliser PHP dans un projet.

Mais avant de commencer, nous devons comprendre ce qu'est PHP.

## Qu'est-ce que PHP ?

PHP est l'abréviation ou l'acronyme de "Hypertext Preprocessor". C'est un langage de script côté serveur, open source et basé sur le web, intégré dans vos fichiers HTML.

Vous l'utilisez pour créer des pages web à la fois réactives et interactives avec la base de données.

## Avantages de PHP

PHP présente de nombreux avantages, en voici quelques-uns :

### PHP est simple à utiliser

Vous n'avez pas besoin d'étudier longuement pour apprendre et utiliser PHP, car sa syntaxe est sensée et bien organisée. Les fonctions de commande sont également faciles à utiliser car elles vous aident à comprendre exactement ce qu'elles font.

### PHP est flexible

La flexibilité est un avantage majeur que tout langage de script devrait avoir, et PHP ne fait pas exception. Même après le lancement d'un projet, un développeur PHP a la possibilité d'apporter des modifications au projet.

### PHP vous aide à collecter des données à partir de formulaires

Vous pouvez utiliser PHP pour collecter des données à partir d'un formulaire créé avec HTML (comme le nom, l'e-mail, le numéro de téléphone ou le mot de passe). De nombreux sites web utilisent cette fonction particulière de PHP.

### PHP a une bonne sécurité

PHP ne sous-traite pas les données ou informations collectées à partir de formulaires. C'est l'une des raisons pour lesquelles la plupart des sites web et des applications de médias sociaux l'utilisent, car il dispose d'un système de base de données sécurisé.

## Comment installer et configurer PHP dans votre projet

Pour commencer avec PHP, vous aurez besoin de trois choses : un éditeur de code pour écrire votre code, une version installée de PHP et XAMPP.

Nous utiliserons Visual Studio Code dans cet exemple, et je vais vous apprendre à installer une version de PHP et XAMPP sur votre PC.

Allez sur le [site web de PHP](https://www.php.net/) et cliquez sur télécharger dans la barre de navigation. La version actuelle devrait être en haut.

Cliquez sur "Windows downloads", et lorsqu'il s'ouvre, faites défiler un peu vers le bas et vous devriez voir une section qui contient "VS16 x64 Thread Safe (2022-May-11 09:29:42)". La section contient un fichier "zip" en dessous – cliquez dessus et attendez que votre téléchargement se termine.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/PHP_-Hypertext-Preprocessor---Google-Chrome-5_30_2022-7_57_44-PM-1.png align="left")

*Cliquez sur le bouton de téléchargement*

![Image](https://www.freecodecamp.org/news/content/images/2022/05/PHP_-Hypertext-Preprocessor---Google-Chrome-5_30_2022-7_57_58-PM.png align="left")

*Cliquez sur Windows downloads*

![Image](https://www.freecodecamp.org/news/content/images/2022/05/PHP_-Hypertext-Preprocessor---Google-Chrome-5_30_2022-7_58_42-PM.png align="left")

*En dessous de Thread Safe, cliquez sur le fichier zip pour télécharger*

Lorsque le téléchargement est terminé, allez dans le dossier de téléchargements de votre ordinateur et cherchez un fichier zip PHP. Faites un clic droit dessus et sélectionnez extraire le fichier. Il est important d'enregistrer le fichier sur votre disque local.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/bandicam-2022-05-30-20-15-25-892-1.jpg align="left")

*Dossier zip et le dossier extrait*

Ouvrez le disque local et ouvrez le dossier PHP extrait. Cliquez une fois sur la barre qui montre le répertoire actuel, puis copiez le nom du répertoire, qui devrait être dans ce format : C:\\php-8.1.6.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/bandicam-2022-05-30-20-30-59-641.jpg align="left")

*Cliquez une fois sur la barre et copiez le nom du répertoire*

Dans la barre Windows, recherchez « Modifier les propriétés de l'environnement système ». Cliquez sur le bouton « variables d'environnement », cliquez sur « Path », puis sur le bouton modifier en dessous. Cela ouvre un espace où vous pouvez créer une nouvelle variable.

Cliquez donc sur le bouton nouveau, puis collez le nom du répertoire que vous avez copié précédemment (qui devrait être « C:\\php-8.1.6 ») et cliquez sur OK pour tous.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Environment.jpg align="left")

Pour tester si PHP est maintenant installé sur votre ordinateur, recherchez l'invite de commande dans Windows en utilisant le mot-clé de recherche `cmd`. Ouvrez-le, puis tapez `php --version` et cliquez sur entrer. Vous devriez voir quelque chose de similaire à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/bandicam-2022-05-30-20-46-16-280.jpg align="left")

*Version de PHP 8.1.6*

La version actuelle de PHP est installée sur notre PC comme on peut le voir dans l'image ci-dessus. L'étape suivante est d'obtenir XAMPP.

## Qu'est-ce que XAMPP ?

L'acronyme XAMPP signifie multiplateforme, Apache, MySQL, PHP et Perl. XAMPP est un serveur web gratuit et open source qui vous permet de développer, tester et construire des sites web sur un serveur local.

Contrairement à PHP, l'installation de XAMPP est assez simple et sans complication. Recherchez « XAMPP Download » dans votre navigateur ou allez sur leur [site web](https://www.apachefriends.org/index.html). Vous devriez voir la version actuelle de XAMPP pour Windows, Linux et OSX lorsqu'il s'ouvre.

Comme j'utilise un ordinateur Windows, je dois simplement cliquer sur celui pour Windows, et le téléchargement devrait commencer.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/bandicam-2022-05-30-21-01-27-189.jpg align="left")

*Cliquez sur XAMPP pour Windows si vous utilisez Windows*

Lorsque le téléchargement est terminé, allez dans vos téléchargements, faites un clic droit sur le fichier d'installation et sélectionnez « exécuter en tant qu'administrateur ».

Cela vous amènera à l'assistant **Setup-xampp** :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/bandicam-2022-05-30-21-07-14-620.jpg align="left")

*cliquez sur suivant*

Cliquez sur suivant, et vous pourrez sélectionner les composants que vous souhaitez :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/bandicam-2022-05-30-21-07-22-682.jpg align="left")

***Sélectionnez les composants et cliquez sur suivant***

Vous arriverez ensuite au dossier d'installation. Vous devez sélectionner un dossier où vous souhaitez installer XAMPP. Je recommande de créer un dossier dans votre disque local pour installer XAMPP.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/bandicam-2022-05-30-21-07-29-806.jpg align="left")

*sélectionnez un dossier d'installation*

Ensuite, vous sélectionnerez la langue. Vous pouvez choisir soit l'anglais soit l'allemand (au choix) :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/bandicam-2022-05-30-21-09-03-881.jpg align="left")

*sélectionnez la langue*

Vous obtiendrez maintenant Bitnami pour XAMPP :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/bandicam-2022-05-30-21-09-08-433.jpg align="left")

*cliquez sur suivant*

Et vous êtes prêt à installer :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/bandicam-2022-05-30-21-09-25-333.jpg align="left")

*cliquez sur suivant*

Soyez patient pendant que le processus d'installation se termine. Lorsqu'il est terminé, cliquez sur OK.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/bandicam-2022-05-30-21-09-30-643.jpg align="left")

*attendez que l'installation soit terminée*

Une fois le processus d'installation terminé, vous pouvez maintenant utiliser XAMPP dans votre projet.

## Pourquoi avez-vous besoin de XAMPP ?

Pour exécuter PHP pour le web, vous devrez installer un serveur web comme Apache et une base de données comme MySQL – et les deux sont pris en charge par XAMPP.

XAMPP est un serveur local qui peut fonctionner sans problème sur notre ordinateur personnel, et est accepté à la fois sur Windows et Linux. Il vous aide également à tester des sites web et à voir s'ils fonctionnent avant de les publier réellement sur un serveur web.

## Comment exécuter PHP avec XAMPP

Pour exécuter PHP avec XAMPP, vous devrez suivre quelques étapes, et je vais les décomposer pour que vous puissiez comprendre.

Tout d'abord, ouvrez le dossier de stockage local, allez dans le dossier « xampp » et ouvrez-le. Vous devriez voir un dossier nommé « htdocs ». Ouvrez-le, puis créez un nouveau dossier à l'intérieur. Dans mon cas, j'ai nommé le dossier que j'ai créé « Demo » (donc donnez à votre dossier le nom de votre choix).

![Image](https://www.freecodecamp.org/news/content/images/2022/06/1-2-3.jpg align="left")

Ensuite, ouvrez votre VS code, cliquez sur ouvrir le dossier, puis allez à l'emplacement où vous avez enregistré le dossier que vous avez créé (que dans mon cas j'ai nommé « Demo »). Créez un fichier avec l'extension `.php` – dans mon cas, j'ai nommé le mien `test.php`. L'extension `.php` indique à l'éditeur de code que nous travaillons sur un code/projet PHP.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/bandicam-2022-06-01-22-08-09-094.jpg align="left")

*créez un fichier avec une extension .php*

PHP est exécuté avec la balise `<?php (Le code va ici) ?>`. La balise d'ouverture est `<?php`, puis votre code PHP suit avant la balise de fermeture `?>`. Par exemple :

```php
<?php
echo "<h1> Mon nom est Derek </h2>";
?>
```

Le mot-clé echo indique au navigateur d'afficher `Mon nom est Derek` tandis que `<h1></h1>` indique au navigateur web de formater le texte pour qu'il soit en gras/plus grand. Ensuite, enregistrez-le.

Après avoir écrit le code, ouvrez le panneau de contrôle XAMPP et démarrez le module Apache en cliquant sur démarrer sous la section action.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/test.php---Demo---Visual-Studio-Code-6_2_2022-1_23_21-AM.png align="left")

Ensuite, allez dans votre navigateur web et dans la barre de recherche, tapez `localhost/Demo/test.php`, puis entrez. Votre navigateur web devrait afficher ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/06/bandicam-2022-06-01-22-07-50-039.jpg align="left")

*affichage web*

Si votre code a été affiché sur le navigateur web, félicitations ! Vous êtes opérationnel.

## Conclusion

Merci beaucoup d'avoir suivi ce tutoriel. J'espère que vous avez tiré quelque chose de cette leçon et j'espère que vous essaierez d'utiliser PHP et XAMPP.

Restez à l'écoute pour mon prochain tutoriel.

Amusez-vous bien à coder !