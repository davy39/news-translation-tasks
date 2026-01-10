---
title: 'Vulnérabilités de sécurité PHP : Détournement de session, Scripting inter-sites,
  Injection SQL et comment les corriger'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-27T19:30:00.000Z'
originalURL: https://freecodecamp.org/news/php-security-vulnerabilities
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d68740569d1a4ca3799.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: PHP
  slug: php
- name: toothbrush
  slug: toothbrush
seo_title: 'Vulnérabilités de sécurité PHP : Détournement de session, Scripting inter-sites,
  Injection SQL et comment les corriger'
seo_desc: 'Security in PHP

  When writing PHP code it is very important to keep the following security vulnerabilities
  in mind to avoid writing insecure code.

  Types Of Vulnerabilities

  These are the common vulnerabilities you''ll encounter when writing PHP code. We...'
---

## **Sécurité en PHP**

Lors de l'écriture de code PHP, il est très important de garder à l'esprit les vulnérabilités de sécurité suivantes pour éviter d'écrire du code non sécurisé.

### **Types de vulnérabilités**

Voici les vulnérabilités courantes que vous rencontrerez lors de l'écriture de code PHP. Nous en discuterons quelques-unes plus en détail ci-dessous.

* [Falsification de requête inter-sites](https://guide.freecodecamp.org/php/security/cross-site-request-forgery) Une vulnérabilité dans l'application causée par le programmeur ne vérifiant pas d'où une requête a été envoyée - cette attaque est envoyée à un utilisateur de niveau de privilège élevé pour obtenir un accès de niveau supérieur à l'application.
* [Scripting inter-sites](https://guide.freecodecamp.org/php/security/cross-site-scripting) Une vulnérabilité dans l'application causée par le programmeur ne nettoyant pas l'entrée avant de la sortir vers le navigateur (par exemple un commentaire sur un blog). Il est couramment utilisé pour exécuter du javascript malveillant dans le navigateur afin de réaliser des attaques telles que le vol de cookies de session parmi d'autres actions malveillantes pour obtenir des privilèges de niveau supérieur dans l'application.
* [Inclusion de fichier local](https://guide.freecodecamp.org/php/security/local-file-inclusion) Une vulnérabilité dans l'application causée par le programmeur nécessitant une entrée de fichier fournie par l'utilisateur et ne nettoyant pas l'entrée avant d'accéder au fichier demandé. Cela entraîne l'inclusion d'un fichier là où il n'aurait pas dû l'être.
* [Inclusion de fichier distant](https://guide.freecodecamp.org/php/security/remote-file-inclusion) Une vulnérabilité dans l'application causée par le programmeur nécessitant une entrée de fichier fournie par l'utilisateur et ne nettoyant pas l'entrée avant d'accéder au fichier demandé. Cela entraîne un fichier étant tiré d'un serveur distant et inclus là où il n'aurait pas dû l'être.
* [Détournement de session](https://guide.freecodecamp.org/php/security/session-hijacking) Une vulnérabilité causée par un attaquant obtenant l'accès à l'identifiant de session d'un utilisateur et étant capable d'utiliser le compte d'un autre utilisateur en se faisant passer pour lui. Cela est souvent utilisé pour obtenir l'accès au compte d'un utilisateur administratif.
* [Acquisition d'identifiant de session](https://guide.freecodecamp.org/php/security/session-identifier-acquirement) L'acquisition d'identifiant de session est une vulnérabilité causée par un attaquant étant capable de deviner l'identifiant de session d'un utilisateur ou d'exploiter des vulnérabilités dans l'application elle-même ou le navigateur de l'utilisateur pour obtenir un identifiant de session.
* [Injection SQL](https://guide.freecodecamp.org/php/security/sql-injection) Une vulnérabilité dans l'application causée par le programmeur ne nettoyant pas l'entrée avant de l'inclure dans une requête vers la base de données. Cela conduit à ce que l'attaquant ait un accès complet en lecture et, plus souvent qu'autrement, en écriture à la base de données. Avec ce type d'accès, un attaquant peut faire de très mauvaises choses.

Maintenant, examinons quelques vulnérabilités courantes plus en détail.

## **Détournement de session**

Le détournement de session est une vulnérabilité causée par un attaquant obtenant l'accès à l'identifiant de session d'un utilisateur et étant capable d'utiliser le compte d'un autre utilisateur en se faisant passer pour lui. Cela est souvent utilisé pour obtenir l'accès au compte d'un utilisateur administratif.

### **Se défendre contre les attaques de détournement de session en PHP**

Pour se défendre contre les attaques de détournement de session, vous devez vérifier les informations du navigateur et de l'emplacement de l'utilisateur actuel par rapport aux informations stockées sur la session. Voici un exemple de mise en œuvre qui peut aider à atténuer les effets d'une attaque de détournement de session. Il vérifie l'adresse IP, l'agent utilisateur et si la session a expiré en supprimant une session avant qu'elle ne soit reprise.

```php
<?php
session_start();

// L'adresse IP correspond-elle ?
if ($_SERVER['REMOTE_ADDR'] != $_SESSION['ipaddress'])
{
session_unset();
session_destroy();
}

// L'agent utilisateur correspond-il ?
if ($_SERVER['HTTP_USER_AGENT'] != $_SESSION['useragent'])
{
  session_unset();
  session_destroy();
}

// Le dernier accès remonte-t-il à plus d'une heure ?
if (time() > ($_SESSION['lastaccess'] + 3600))
{
  session_unset();
  session_destroy();
}
else
{
  $_SESSION['lastaccess'] = time();
}
```

## **Scripting inter-sites**

Le scripting inter-sites est un type de vulnérabilité dans une application web causée par le programmeur ne nettoyant pas l'entrée avant de la sortir vers le navigateur web (par exemple un commentaire sur un blog). Il est couramment utilisé pour exécuter du javascript malveillant dans le navigateur web afin de réaliser des attaques telles que le vol de cookies de session parmi d'autres actions malveillantes pour obtenir des privilèges de niveau supérieur dans l'application web.

### **Exemple d'attaque de scripting inter-sites**

Un blog permet aux utilisateurs de styliser leurs commentaires avec des balises HTML, cependant le script alimentant le blog ne supprime pas les balises `<script>` permettant à n'importe quel utilisateur d'exécuter du javascript sur la page. Un attaquant peut utiliser cela à son avantage pour exécuter du javascript malveillant dans le navigateur. Ils pourraient infecter les utilisateurs avec des logiciels malveillants, voler des cookies de session, et plus encore.

```html
<script>
  alert('Scripting inter-sites !');
</script>
```

### **Protéger votre site web contre les attaques de scripting inter-sites en PHP**

En PHP, il existe deux fonctions principales, `htmlspecialchars()` et `strip_tags()`, intégrées pour vous protéger contre les attaques de scripting inter-sites.

La fonction `htmlspecialchars($string)` empêchera une chaîne HTML de se rendre en tant que HTML et l'affichera en tant que texte brut vers le navigateur web. **Exemple de code htmlspecialchars()**

```php
<?php
$usercomment = "<script>alert('Scripting inter-sites !');</script>";
echo htmlspecialchars($usercomment);
```

L'autre approche est la fonction `strip_tags($string, $allowedtags)` qui supprime toutes les balises HTML sauf les balises HTML que vous avez mises sur liste blanche. Il est important de noter qu'avec la fonction `strip_tags()` vous devez être plus prudent, cette fonction n'empêche pas l'utilisateur d'inclure du javascript en tant que lien, vous devrez nettoyer cela par vous-même.

**Exemple de code strip_tags()**

```php
<?php
$usercomment = "<script>alert('Scripting inter-sites !');</script>";
$allowedtags = "<p><a><h1><h2><h3>";
echo strip_tags($usercomment, $allowedtags);
```

**Définir l'en-tête X-XSS-Protection :**

En PHP, vous pouvez envoyer l'en-tête `X-XSS-Protection` qui indiquera aux navigateurs de vérifier une attaque de scripting inter-sites réfléchie et de bloquer le chargement de la page. Cela ne prévient pas toutes les attaques de scripting inter-sites, seulement celles réfléchies, et doit être utilisé en combinaison avec d'autres méthodes.

```php
<?php
header("X-XSS-Protection: 1; mode=block");
```

**Écrire votre propre fonction de nettoyage** Une autre option, si vous souhaitez plus de contrôle sur le fonctionnement du nettoyage, est d'écrire votre propre fonction de nettoyage HTML, cela n'est pas recommandé pour les débutants en PHP car une erreur rendrait votre site web vulnérable.

### **Protéger votre site web contre les attaques de scripting inter-sites avec une politique de sécurité du contenu**

Une approche efficace pour prévenir les attaques de scripting inter-sites, qui peut nécessiter de nombreux ajustements à la conception et à la base de code de votre application web, est d'utiliser une politique de sécurité du contenu.

#### **Définir une politique de sécurité du contenu en tant qu'en-tête HTTP**

La manière la plus courante de définir une politique de sécurité du contenu est de la définir directement dans l'en-tête HTTP. Cela peut être fait par le serveur web en éditant sa configuration ou en l'envoyant via PHP.

**Exemple d'une politique de sécurité du contenu définie dans un en-tête HTTP**

```php
<?php
header("content-security-policy: default-src 'self'; img-src https://*; child-src 'none';");
```

#### **Définir une politique de sécurité du contenu en tant que balises Meta**

Vous pouvez inclure votre politique de sécurité du contenu dans le HTML de la page et la définir page par page. Cette méthode nécessite de la définir sur chaque page ou vous perdez l'avantage de la politique.

**Exemple d'une politique de sécurité du contenu définie dans une balise Meta HTML**

```html
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; img-src https://*; child-src 'none';">
```

## **Injection SQL**

L'injection SQL est une vulnérabilité dans l'application causée par le programmeur ne nettoyant pas l'entrée avant de l'inclure dans une requête vers la base de données. Cela conduit à ce que l'attaquant ait un accès complet en lecture et, plus souvent qu'autrement, en écriture à la base de données. Avec ce type d'accès, un attaquant peut faire de très mauvaises choses.

### **Exemple d'attaque par injection SQL**

Le script PHP ci-dessous exécute une instruction SQL pour obtenir l'email d'un utilisateur par son ID. Cependant, l'entrée n'est pas nettoyée, ce qui la rend vulnérable à l'injection SQL.

```php
<?php
$input = $_GET['id'];
$dbserver = "localhost";
$dbuser = "camper";
$dbpass = "supersecretcampsitepassword";
$dbname = "freecodecamp";

$conn = new mysqli($dbserver, $dbuser, $dbpass, $dbname);

if ($conn->connect_error) {
    die("Échec de la connexion : " . $conn->connect_error);
}

$sql = "SELECT email FROM users WHERE id =" . $input;

$result = $conn->query($sql);

if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        echo $row["email"];
    }
} else {
    echo "aucun résultat";
}

$conn->close();
```

```sql
SELECT email FROM users WHERE id = `$input`;
```

Ainsi, avec ce qui précède, l'entrée n'est pas transtypée (par exemple, le transtypage de l'entrée avec (int) de sorte que seul un nombre soit autorisé) ni échappée, permettant à quelqu'un de réaliser une attaque par injection SQL - par exemple, l'URL `getemailbyuserid.php?id=1'; My Query Here-- -` vous permettrait d'exécuter des requêtes SQL arbitraires avec peu d'effort.

### **Protéger votre site web contre les attaques par injection SQL en PHP**

Il existe plusieurs approches pour protéger votre site web contre les attaques par injection SQL. Ces approches sont la liste blanche, le transtypage et l'échappement des caractères.

**Liste blanche :** L'approche de la liste blanche est utilisée dans les cas où seules quelques entrées sont attendues. Vous pouvez lister chaque entrée attendue dans un switch PHP puis avoir un cas par défaut pour les entrées invalides. Vous n'avez pas à vous soucier d'un problème de transtypage ou d'un contournement d'échappement de caractères, mais l'entrée autorisée est extrêmement limitée. Cela reste une option, voir l'exemple ci-dessous.

```php
<?php
switch ($input) {
  case "1":
    // requête db 1
    break;
  case "2":
    // requête db 2
    break;
  default:
    // entrée invalide, retourner une erreur
}
```

**Transtypage :** L'approche de transtypage est couramment utilisée pour une application utilisant une entrée numérique. Il suffit de transtyper l'entrée avec `(int) $input` et seule une valeur numérique sera autorisée.

**Échappement des caractères :** L'approche d'échappement des caractères échappera les caractères tels que les guillemets et les barres obliques fournis par l'utilisateur pour prévenir une attaque. Si vous utilisez le serveur MySQL et la bibliothèque MySQLi pour accéder à votre base de données, la fonction `mysqli_real_escape_string($conn, $string)` prendra deux arguments, la connexion MySQLi et la chaîne, et échappera correctement l'entrée de l'utilisateur pour bloquer une attaque par injection SQL. La fonction exacte que vous utilisez dépend du type de base de données et de la bibliothèque PHP que vous utilisez. Consultez la documentation de la bibliothèque PHP pour plus d'informations sur l'échappement de l'entrée utilisateur.

## Plus sur PHP :

* [Meilleures pratiques PHP](https://www.freecodecamp.org/news/p/9a508d2b-fa35-4ac1-a15b-8bab8acc356d/)
* [Meilleurs exemples de code PHP](https://www.freecodecamp.org/news/the-best-php-examples/)
* [Comment prévenir une attaque slow loris sur un serveur PHP](https://www.freecodecamp.org/news/slow-loris-attack-using-javascript-on-php-server/)
* [Comment configurer un environnement de débogage local en PHP](https://www.freecodecamp.org/news/set-up-xdebug-phpstorm-in-php5-7-6a8386304fc6/)