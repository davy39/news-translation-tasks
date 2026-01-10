---
title: Comment créer un formulaire HTML et PHP simple
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-06-20T22:17:13.000Z'
originalURL: https://freecodecamp.org/news/creating-html-forms
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/pexels-john-petalcurin-2115257.jpg
tags:
- name: forms
  slug: forms
- name: HTML
  slug: html
- name: PHP
  slug: php
seo_title: Comment créer un formulaire HTML et PHP simple
seo_desc: "If you have a website, it's only a matter of time before you feel the irrepressible\
  \ urge to gather information about your site's users. \nThe most direct way to do\
  \ that is to ask them some questions. And, in the HTML world, the best tool for\
  \ recording..."
---

Si vous avez un site web, il n'est qu'une question de temps avant que vous ne ressentiez l'irrésistible envie de recueillir des informations sur les utilisateurs de votre site. 

La manière la plus directe de le faire est de leur poser quelques questions. Et, dans le monde HTML, le meilleur outil pour enregistrer les réponses à ces questions est le simple formulaire HTML. 

Dans ce guide, je vais vous montrer comment cela se fait en utilisant du HTML de base et juste une touche de PHP.

Comme vous le verrez bientôt, le HTML dont vous aurez besoin pour présenter un formulaire est, en fait, assez simple. Mais cela ne résoudra que la moitié de votre problème. 

Un formulaire incitera les utilisateurs à entrer les informations que vous demandez. Mais, si nous en restons là, rien ne se passera réellement lorsqu'ils cliqueront sur le bouton Soumettre. Et cela parce que nous n'avons rien qui s'exécute sur notre serveur pour collecter et traiter ces informations.

La construction du back-end qui intégrera votre formulaire avec un moteur de base de données ou une application associée peut devenir vraiment compliquée et dépasse largement notre cadre ici. Mais, une fois que nous comprendrons le formulaire HTML ici, je vous montrerai comment vous pouvez ajouter du code PHP pour gérer le code de manière basique.

Cet article provient de [mon cours complet LPI Web Development Essentials Study Guide](https://www.udemy.com/course/complete-lpi-web-development-essentials-exam-study-guide/?referralCode=C92570BCBB38302A9257). Si vous le souhaitez, vous pouvez suivre la version vidéo ici :

%[https://www.youtube.com/watch?v=nRWn917ZZ60]

## Comment préparer votre environnement serveur Linux

J'exécute un conteneur virtuel Linux qui a à la fois PHP et le serveur HTTPD Apache installés. Vous pouvez installer ces packages sur une machine Ubuntu de cette manière :

```bash
$ sudo apt install apache2 php
```

Je vais commencer par naviguer vers le répertoire racine web qui est `/var/www/html`. La commande `ls` listera tous les fichiers dans le répertoire. 

```
$ pwd
/var/www/html
$ ls
form.html	index.html	submit.php
```

Ce fichier `index.html` est le fichier de remplacement par défaut qui est créé lorsque Apache est installé. Je le remplacerais par mon propre fichier de page d'accueil si ce site web était un projet réel.

## Comment créer un formulaire HTML

Pour l'instant, je vais vous montrer ce qu'il y a dans ce fichier `form.html` :

```html
<!DOCTYPE html>
<html>
<head>
    <title>Exemple de formulaire</title>
</head>
<body>
    <h1>Exemple de formulaire</h1>
    <form action="submit.php" method="post">
        <label for="name">Nom :</label>
        <input type="text" id="name" name="name" required><br><br>

        <label for="email">Email :</label>
        <input type="email" id="email" name="email" required><br><br>

        <label for="message">Message :</label>
        <textarea id="message" name="message" rows="5" cols="30" required></textarea><br><br>

        <input type="submit" value="Soumettre">
    </form>
</body>
</html>
```

Nous commençons par les balises standard puis par un texte `<h1>` pour un titre. Mais ensuite, nous ouvrons une balise `<form>` où l'attribut `action` pointe vers un fichier appelé `submit.php` et la méthode spécifie `post`. "Post" signifie que tout texte qui a été saisi dans le formulaire sera posté – ou envoyé – au fichier `submit.php` une fois le formulaire soumis.

La balise `<input>` en bas du code juste avant que nous ne fermions la balise `<form>` utilise le type `submit` pour envoyer nos données. 

```html
<input type="submit" value="Soumettre">
```

L'attribut `value` "Soumettre" est là pour imprimer le mot "Soumettre" sur le bouton que nous verrons sur le formulaire. Cela facilitera la compréhension de l'utilisation du formulaire pour les utilisateurs.

Maintenant, le code utilisé par le formulaire lui-même est divisé en trois paires de lignes :

```html
<label for="name">Nom :</label>
<input type="text" id="name" name="name" required><br><br>

<label for="email">Email :</label>
<input type="email" id="email" name="email" required><br><br>

<label for="message">Message :</label>
<textarea id="message" name="message" rows="5" cols="30" required></textarea><br><br>
```

La première ligne ici est une balise `<label>` qui imprime le mot "Nom :" sur le premier champ de saisie. La balise `<input>` accompagnatrice a un attribut `type` de "text", un attribut `id` de "name" et est un champ `required`. Cela signifie que la soumission du formulaire ne sera pas réussie à moins que ce champ ait une valeur.

La paire suivante fait la même chose pour une adresse email. Mais comme nous le voyons à partir de l'attribut `type`, ce champ attend que la saisie soit conforme aux propriétés d'une adresse email valide. Ce champ est également `required`.

La dernière paire – "Message" – prend une balise `<textarea>` et a un nombre maximum de lignes et de colonnes spécifié. Ce champ, comme vous pouvez vous y attendre, permet du texte libre, mais seulement jusqu'à un nombre maximum de caractères.

C'est notre code. Voyons à quoi il ressemble dans un navigateur. Tout d'abord, vous devrez obtenir l'adresse IP publique du conteneur. 

Il y a plusieurs façons de le faire, mais celle qui implique le moins de frappes est d'exécuter `ip a` à l'intérieur du conteneur. 

```bash
$ ip a
[...]
12: eth0@if13: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether 00:16:3e:81:57:1b brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.0.3.216/24 metric 100 brd 10.0.3.255 scope global dynamic eth0
       valid_lft 3154sec preferred_lft 3154sec
    inet6 fd42:e265:3791:64f9:216:3eff:fe81:571b/64 scope global mngtmpaddr noprefixroute 
[...]
```

L'IP que j'ai obtenue était `10.0.3.216`. Il suffit d'ajouter `form.html` à la valeur que vous avez obtenue et de l'insérer dans la barre d'URL de votre navigateur et le site se chargera. Cela dit, il s'agit d'une IP NAT locale, donc elle ne sera pas accessible en dehors de mon réseau domestique.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/form_html.png)

N'hésitez pas à taper quelque chose dans les champs Nom, Email et Message, mais il est inutile de cliquer sur le bouton Soumettre pour l'instant. Cela parce que, sans un peu de magie PHP, rien ne se passera. Et je ne vous ai pas encore montré ce PHP.

## Comment écrire un script PHP pour capturer les entrées utilisateur

PHP, soit dit en passant, est un langage de script adapté au web qui est un choix populaire pour ajouter des fonctionnalités programmées aux pages web. En fait, vous pouvez même incorporer du code PHP directement dans votre code HTML. Mais voici à quoi cela ressemblera seul, dans un fichier appelé `submit.php` :

```php
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Récupérer les données du formulaire
    $name = $_POST["name"];
    $email = $_POST["email"];
    $message = $_POST["message"];

    // Afficher les données soumises
    echo "Nom : " . $name . "<br>";
    echo "Email : " . $email . "<br>";
    echo "Message : " . $message . "<br>";
}
?>
```

Vous vous souvenez comment notre méthode HTML `post` a envoyé les données du formulaire à ce fichier ? Eh bien, voici ce que PHP va en faire. Le bloc `if` recherche les données postées et les organise ensuite par champ : nom, email et message. Normalement, vous enverriez probablement ces données à une base de données, mais pour simplifier, ce code se contentera de les imprimer sur la page pour prouver que nous les avions réellement.

Voyons à quoi cela ressemble. Je clique sur le bouton Soumettre et le formulaire est remplacé par le texte que j'avais saisi. Rien de spectaculaire, mais cela illustre bien comment les formulaires fonctionnent avec PHP.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/results.png)

Avec ce code simple, vous êtes maintenant en mesure de créer vos propres formulaires HTML qui collectent et traitent les entrées utilisateur. 

Votre prochaine étape sera de vous connecter à une base de données back-end afin de pouvoir sauvegarder et manipuler ces données. Pour l'instant, profitez de cet accomplissement !

*Cet article provient de [mon cours complet LPI Web Development Essentials Study Guide](https://www.udemy.com/course/complete-lpi-web-development-essentials-exam-study-guide/?referralCode=C92570BCBB38302A9257).* *Et il y a beaucoup plus de bonnes choses technologiques disponibles sur [bootstrap-it.com](https://bootstrap-it.com/)*