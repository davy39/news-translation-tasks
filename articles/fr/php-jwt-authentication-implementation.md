---
title: Comment implémenter les JSON Web Tokens (JWT) en PHP – Tutoriel d'authentification
  PHP
subtitle: ''
author: Oghenekparobo Stephen
co_authors: []
series: null
date: '2024-04-24T18:41:00.000Z'
originalURL: https://freecodecamp.org/news/php-jwt-authentication-implementation
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/How-to-Implement-JSON-Web-Tokens-in-PHP-Cover.png
tags:
- name: authentication
  slug: authentication
- name: authorization
  slug: authorization
- name: handbook
  slug: handbook
- name: PHP
  slug: php
seo_title: Comment implémenter les JSON Web Tokens (JWT) en PHP – Tutoriel d'authentification
  PHP
seo_desc: "In this guide, we'll explore the process of creating JSON Web Tokens (JWTs)\
  \ from scratch in PHP, which is a superior and more secure authentication scheme.\
  \ \nBy implementing this advanced approach, you'll have a robust and highly secure\
  \ authentication..."
---

Dans ce guide, nous allons explorer le processus de création de JSON Web Tokens (JWT) à partir de zéro en PHP, ce qui est un schéma d'authentification supérieur et plus sécurisé. 

En implémentant cette approche avancée, vous disposerez d'un mécanisme d'authentification robuste et hautement sécurisé qui améliore considérablement la protection des données et l'authentification des utilisateurs.

## Table des matières

* [Qu'est-ce que les JSON Web Tokens (JWT) ?](#heading-quest-ce-que-les-json-web-tokens-jwt)
* [Prise en main](#heading-prise-en-main)
* [Envoyer nos requêtes](#heading-envoyer-nos-requetes)
* [Tester la connexion à la base de données](#heading-tester-la-connexion-a-la-base-de-donnees)
* [Inscription des utilisateurs](#heading-inscription-des-utilisateurs)
* [Configuration de la classe JWT](#heading-configuration-de-la-classe-jwt)
* [La méthode Encode](#heading-la-methode-encode)
* [Le point de terminaison de connexion](#heading-le-point-de-terminaison-de-connexion)
* [Ressources protégées et décodage des JSON Web Tokens](#heading-ressources-protegees-et-decodage-des-json-web-tokens)
* [Que se passe-t-il maintenant ?](#heading-que-se-passe-t-il-maintenant)
* [Comment configurer la méthode Decode dans notre classe JWT](#heading-comment-configurer-la-methode-decode-dans-notre-classe-jwt)
* [Ressources protégées](#heading-ressources-protegees)
* [Vérification des en-têtes pour le schéma d'autorisation correct](#heading-verification-des-en-tetes-pour-le-schema-dautorisation-correct)
* [Création d'instances dans le point d'entrée de l'API](#heading-creation-dinstances-dans-le-point-dentree-de-lapi)
* [Suggestions](#heading-suggestions)
* [Comment implémenter l'expiration des tokens](#heading-comment-implementer-lexpiration-des-tokens)
* [Structure de dossier mise à jour](#heading-structure-de-dossier-mise-a-jour)
* [Conclusion](#heading-conclusion)

## Qu'est-ce que les JSON Web Tokens (JWT) ?

Un JSON Web Token est une chaîne composée de trois parties, chacune jointe par un point (.), puis encodée en base64url.

Voici les trois parties d'un JWT :

**En-tête** : Un en-tête se compose de métadonnées sur le token, telles que le type de token et l'algorithme utilisé.

```php
 $header = json_encode([
            "alg" => "HS256",
            "typ" => "JWT"
        ]);

        $header = $this->base64urlEncode($header);
```

**Charge utile** : Dans la structure JWT, la charge utile encapsule des indices spécifiques appelés claims, hébergeant les données utilisateur qui sont encodées en utilisant base64url.

```php
$payload = [
    "id" => $user['id'],
    "name" => $user["name"]
];

  $payload = $this->base64urlEncode($payload);
```

**Signature** : Cela est généré en créant un hachage de l'en-tête et de la charge utile, combiné avec une clé secrète généralement générée sous forme de 256 bits ou 32 octets. Par convention, la clé secrète correspond à la taille de la sortie du hachage.

Nous utiliserons le lien ci-dessous pour générer une clé secrète dont nous avons besoin pour ce projet :

%[https://generate-random.org/encryption-key-generator?source=post_page-----ebf5693b931a--------------------------------]

```php
 $signature = hash_hmac("sha256", $header . "." . $payload, $secret_key, true);
 $signature = $this->base64urlEncode($signature);
```

Un JSON Web Token est simplement une combinaison de l'en-tête, de la charge utile et de la signature, où chaque composant est concaténé ensemble avec des points (.) entre eux :

```bash
$header . "." . $payload . "." . $signature;
```

## Prise en main

Pour lancer ce projet, veuillez télécharger le modèle de projet à partir du lien suivant : [Authentification PHP avec JWT Tutoriel](https://github.com/Oghenekparobo/php_auth_jwt_tut). 

Une fois téléchargé, examinez attentivement le fichier **README.md** inclus dans le dépôt pour des informations complètes concernant les packages préinstallés. Le fichier contient des détails essentiels tels que des notes sur la sécurité et les meilleures pratiques. Prendre le temps de lire attentivement le **README** garantira une configuration fluide et une compréhension du projet.

Pour initier la configuration du projet, utilisez Git en exécutant la commande suivante :

```bash
git clone https://github.com/Oghenekparobo/php_auth_jwt_tut.git
```

Cette commande clonera le dépôt du projet sur votre système local, vous permettant de procéder à l'installation et au processus de configuration.

Après avoir cloné le projet depuis GitHub, la structure de votre projet devrait correspondre à la disposition suivante :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/1_ZQ1u8lazV-ID3fJ9bFKUMA.jpg)
_structure du projet sur VS Code_

project_root/

 api/
    .htaccess
    index.php
    (autres fichiers PHP)

 vendor/
    (Dépendances Composer)
    ...

 .env
 README.md
 (autres fichiers du projet)

**Dans cette structure :**

* Le répertoire `api/` contient des fichiers PHP responsables de la gestion des requêtes et des réponses de l'API. Il inclut un fichier `.htaccess` pour la réécriture d'URL et un fichier `index.php`, ainsi que d'autres fichiers PHP pour des fonctionnalités spécifiques.
* Le répertoire `vendor/` contient les dépendances Composer installées pour le projet. Ces dépendances sont gérées par Composer et ne doivent pas être modifiées directement.
* Le fichier `.env` contient des variables d'environnement nécessaires pour configurer l'environnement de l'application, telles que les identifiants de la base de données et les clés API.
* Le fichier `README.md` fournit des informations essentielles sur le projet, y compris les instructions de configuration, les directives d'utilisation et tout autre détail pertinent.

Assurez-vous de maintenir cette structure et suivez les instructions fournies dans le fichier **README** pour configurer et exécuter le projet avec succès.

## Envoyer nos requêtes

Lorsque nous faisons référence à notre projet, l'URL serait généralement structurée comme suit : `http://localhost/php_auth_jwt_tut/api`. Cependant, en fonction du nom du projet, cette URL peut varier en conséquence. Néanmoins, l'URL de base reste cohérente : `[http://localhost/php_auth_jwt_tut/api](http://localhost/php_auth_jwt_tut/api.)`[.](http://localhost/php_auth_jwt_tut/api.)

Grâce à notre implémentation de la réécriture d'URL dans le fichier `.htaccess`, des préfixes supplémentaires tels que `index.php` ou `.php` sont inutiles lors de l'accès à nos URL. Nous avons méticuleusement configuré les paramètres de notre serveur pour garantir une navigation fluide sans ces préfixes.

En termes plus simples, l'accès aux points de terminaison de l'API de notre projet peut se faire directement à partir de l'URL de base : `http://localhost/php_auth_jwt_tut/api`. Cette approche rationalisée améliore l'expérience utilisateur et élimine la complexité inutile pour ce projet.

Pour faciliter les tests des points de terminaison de l'API de notre projet, nous pouvons utiliser le fichier **index.php** situé dans le dossier **api**. Ce fichier sert de point de départ pour notre application et contient toutes les configurations nécessaires.

Tout d'abord, nous imprimerons simplement toute sortie souhaitée dans le fichier **index.php**. Cela nous aide à confirmer que notre point de terminaison fonctionne correctement. Ensuite, nous testerons le point de terminaison en accédant à l'URL : `[http://localhost/php_auth_jwt_tut/api](http://localhost/php_auth_jwt_tut/api.)`[.](http://localhost/php_auth_jwt_tut/api.)

De plus, nous configurerons notre connexion à la base de données pour garantir une communication fluide entre nos points de terminaison de l'API et la base de données. Toutes les configurations requises sont incluses dans le fichier [**bootstrap.php**](https://github.com/Oghenekparobo/php_auth_jwt_tut/blob/main/api/bootstrap.php) pour plus de commodité. En important ce fichier dans notre [**index.php**](https://github.com/Oghenekparobo/php_auth_jwt_tut/blob/main/api/index.php), la gestion des configurations et des imports devient plus simple.

De plus, il est important de noter que nous appliquerons un typage strict dans tout notre code. Cela signifie que nous spécifierons les types de données que nos variables et fonctions peuvent contenir ou retourner. Cela aide à maintenir la cohérence et réduit les chances d'erreurs dans notre code.

## Tester la connexion à la base de données

Avant de procéder aux étapes décrites dans cette section, il est impératif de lire attentivement le fichier **README** de ce projet. Cela vous fournira des instructions complètes sur la manière de configurer correctement votre base de données. À la racine du projet, vous trouverez un fichier nommé [**college.sql**](https://github.com/Oghenekparobo/php_auth_jwt_tut/blob/main/college.sql), qui contient les tables nécessaires pour votre base de données. Suivez simplement les instructions fournies dans le fichier **README** pour importer et configurer la base de données en conséquence.

Dans le dossier **src** de notre projet, nous trouvons des classes et des passerelles essentielles, y compris les connexions de base de données nécessaires pour notre projet. Le fichier responsable de cela est **database.php**, déjà configuré pour établir une connexion de base de données PDO.

Note : Avant utilisation, assurez-vous d'ajuster ou de configurer les variables dans le fichier d'environnement **.env** pour qu'elles correspondent à vos identifiants de base de données.

**Fichier .env** :

```env
DB_HOST= 'db_host'
DB_NAME = 'db_name'
DB_USER = 'db_user'
DB_PASS = 'db_password'
SECRET_KEY = "secret_key"
```

**bootstrap.php** :

```php
require dirname(__DIR__)  . '/vendor/autoload.php';

set_error_handler('ErrorHandler::handleError');
set_exception_handler('ErrorHandler::handleException');

$dotenv = Dotenv\Dotenv::createImmutable(dirname(__DIR__));
$dotenv->load();

header("Content-type: application/json; charset=UTF-8");


$database = new Database(
    $_ENV["DB_HOST"],
    $_ENV["DB_NAME"],
    $_ENV["DB_USER"],
    $_ENV["DB_PASS"]
);
```

Le code prépare notre application en effectuant quelques actions clés. Tout d'abord, il charge les fichiers nécessaires pour gérer les erreurs et les exceptions de manière fluide. Ensuite, il récupère les variables d'environnement à partir d'un fichier spécial (**.env**) où nous stockons des paramètres importants comme les informations de la base de données. Après cela, il indique à l'application d'envoyer des données dans un format spécifique (JSON). Enfin, il établit une connexion à la base de données en utilisant les informations du fichier **.env**. Cette configuration garantit que notre application fonctionne de manière fluide et sécurisée.

**database.php** :

```php
class Database
{
    private ?PDO $conn = null;

    public function __construct(
        private string $host,
        private string $name,
        private string $user,
        private string $password
    ) {
    }

    public function getConnection(): ?PDO
    {
        try {
            if ($this->conn === null) {
                $this->conn = new PDO("mysql:host=$this->host;dbname={$this->name}", $this->user, $this->password);
                $this->conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
                $this->conn->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);
                $this->conn->setAttribute(PDO::ATTR_STRINGIFY_FETCHES, false);
            }

            return $this->conn;
        } catch (PDOException $e) {
            echo "Connection failed: " . $e->getMessage();
            return null;
        }
    }
}
```

Incluez une instruction echo pour indiquer une connexion réussie à la base de données avant de retourner l'objet `$this->conn`. Cela aide à vérifier l'état de la connexion et à assurer le bon fonctionnement de l'application. Par exemple :

```php
try {
    if ($this->conn === null) {
        $this->conn = new PDO("mysql:host=$this->host;dbname={$this->name}", $this->user, $this->password);
        $this->conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $this->conn->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);
        $this->conn->setAttribute(PDO::ATTR_STRINGIFY_FETCHES, false);
        
        // Message d'écho indiquant une connexion réussie à la base de données
        echo "Database connected successfully.";
    }
    
    return $this->conn;
} catch (PDOException $e) {
    echo "Connection failed: " . $e->getMessage();
    return null;
}
```

Procédez au fichier **index.php** pour invoquer la fonction `getConnection` et vérifier le fonctionnement de l'application. Il est important de noter que nous avons initialisé notre classe `Database` dans notre fichier bootstrap PHP, assurant une intégration et un fonctionnement fluides.

L'invocation de la fonction `getConnection` dans le fichier **index.php** devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/1_YrpE0hGl-qf8QB8pChAFdA.jpg)
_fichier index.php_

Après avoir implémenté avec succès la connexion à la base de données et envoyé notre requête, vous pouvez vous attendre à la réponse suivante :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/1_hnCfjp2hp1Gzf2gkuey_nA.jpg)
_connexion à la base de données réussie_

**Note** : Assurez-vous de supprimer l'écho après avoir terminé.

## Inscription des utilisateurs

Pour gérer efficacement les données des utilisateurs, nous allons implémenter une solution frontend minimale en créant un nouveau fichier nommé [**register.php**](https://github.com/Oghenekparobo/php_auth_jwt_tut/blob/main/register.php) dans le répertoire racine de notre projet. De plus, nous allons introduire une feuille de style nommée [**style.css**](https://github.com/Oghenekparobo/php_auth_jwt_tut/blob/main/style.css) pour améliorer la présentation visuelle de la page d'inscription. 

Nous allons établir une connexion à notre base de données, facilitant l'ajout transparent des utilisateurs à la table des utilisateurs dans notre base de données de collège. Après une inscription réussie, un message de confirmation sera affiché pour confirmer l'ajout de l'utilisateur à la base de données.

**register.php** :

```php
require __DIR__ . "/vendor/autoload.php";

if ($_SERVER["REQUEST_METHOD"] === "POST") {

    $dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
    $dotenv->load();

    $database = new Database(
        $_ENV["DB_HOST"],
        $_ENV["DB_NAME"],
        $_ENV["DB_USER"],
        $_ENV["DB_PASS"]
    );

    $conn = $database->getConnection();

    $sql = "INSERT INTO user (name, username, password_hash)
            VALUES (:name, :username, :password_hash)";

    $stmt = $conn->prepare($sql);

    $password_hash = password_hash($_POST["password"], PASSWORD_DEFAULT);


    $stmt->bindValue(":name", $_POST["name"], PDO::PARAM_STR);
    $stmt->bindValue(":username", $_POST["username"], PDO::PARAM_STR);
    $stmt->bindValue(":password_hash", $password_hash, PDO::PARAM_STR);


    $stmt->execute();

    echo "Thank you for registering.";
    exit;
}

?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>
    <div class="container">
        <h2>User Registration</h2>
        <form action="register.php" method="post">
            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required>
            </div>
            <div class="form-group">
                <input type="submit" value="Register">
            </div>
        </form>
    </div>
</body>

</html>
```

**style.css** :

```css
body,
html {
  margin: 0;
  padding: 0;
  font-family: Arial, sans-serif;
}

.container {
  background-color: #fff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  width: 300px;
  margin: 0 auto;
}

h2 {
  text-align: center;
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 20px;
}

label {
  font-weight: bold;
}

input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

input[type="submit"] {
  width: 100%;
  padding: 10px;
  border: none;
  background-color: #007bff;
  color: #fff;
  border-radius: 4px;
  cursor: pointer;
}

input[type="submit"]:hover {
  background-color: #0056b3;
}
```

Note : Assurez-vous que ces fichiers sont placés dans le répertoire racine de votre projet. L'interface utilisateur apparaîtra comme suit :

Processus d'inscription :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/1_KOO1tlf51t0fBLoYvVm9-w.jpg)
_formulaire d'inscription utilisateur_

Inscription réussie :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/1_elpUg7Wz7NIguur_xKYU6w.jpg)
_page d'inscription réussie_

Notre structure de base de données est illustrée dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/1_ZWe06DjCYU3iorRAGBGi8w.jpg)
_structure de la base de données sur phpMyAdmin_

Félicitations ! Vous méritez un grand verre de jus pour être arrivé à ce stade, maintenant passons à la partie suivante, qui consiste à créer un JWT à partir de zéro !

### Configuration de la classe JWT

Dans notre modèle de projet, le fichier **Jwt.php** a déjà été créé. Maintenant, procédons à la création de notre classe `Jwt` et implémentons la logique pour l'encodage et la génération d'un token JWT.

### Encodage en JWT

Pour créer un JWT, nous devons convertir notre en-tête, notre charge utile et notre signature en encodage base64url. Cependant, PHP ne supporte pas le standard Base64URL. Par conséquent, nous allons développer notre propre méthode d'encodage Base64URL pour effectuer l'opération d'encodage nécessaire.

Veuillez copier l'extrait de code suivant et le coller dans la classe `Jwt` située dans le dossier **src**.

```php
class Jwt
{

    public function __construct(private string $key)
    {

    }

  
    private function base64URLEncode(string $text): string
    {

        return str_replace(['+', '/', '='], ['-', '_', ''], base64_encode($text));
    }

  
}
```

Cette classe est responsable de l'encodage des tokens JWT en utilisant le schéma d'encodage base64url. Elle inclut un constructeur qui accepte un paramètre de clé, qui représente apparemment la clé secrète utilisée pour encoder les tokens. De plus, elle contient une méthode privée nommée `base64URLEncode`, qui effectue l'opération d'encodage base64URL.

**La méthode base64URLEncode** : La méthode base64urlEncode est une fonction privée au sein de la classe `Jwt`. Elle prend un paramètre de chaîne, text, et retourne la version encodée en base64URL de la chaîne d'entrée. La méthode applique d'abord l'encodage base64 standard au texte d'entrée en utilisant la fonction base64_encode.

Ensuite, elle remplace les caractères + (plus), / (barre oblique), et = (signe égal) par - (tiret), _ (trait de soulignement), et une chaîne vide, respectivement. Cette substitution est nécessaire pour assurer la compatibilité avec le schéma d'encodage base64URL, qui utilise des caractères sûrs pour les URL. Enfin, la méthode retourne la chaîne encodée en base64URL.

Dans l'ensemble, la méthode base64URLEncode fournit une fonctionnalité cruciale pour l'encodage des données dans les tokens JWT en utilisant le schéma d'encodage base64URL, qui est couramment utilisé dans les implémentations JWT.

### La méthode encode

Collez l'extrait de code suivant dans votre classe `Jwt` :

```php
public function encode(array $payload): string
    {

        $header = json_encode([
            "alg" => "HS256",
            "typ" => "JWT"
        ]);

        $header = $this->base64URLEncode($header);
        $payload = json_encode($payload);
        $payload = $this->base64URLEncode($payload);

        $signature = hash_hmac("sha256", $header . "." . $payload, $this->key, true);
        $signature = $this->base64URLEncode($signature);
        return $header . "." . $payload . "." . $signature;
    }
```

Tout d'abord, nous avons une classe appelée `Jwt`. Cette classe nous aide à créer des tokens JWT. Dans le constructeur de la classe `Jwt`, nous avons spécifié une clé secrète. Cette clé secrète est importante pour créer et vérifier les tokens sur le composant de signature.

La méthode `encode` est là où la magie opère. Elle prend certaines données (que nous appelons la charge utile) et les transforme en un token JWT. Voici comment cela fonctionne :

1. Nous créons un en-tête pour le token. Cet en-tête contient des informations sur la manière dont le token est chiffré et le type de token qu'il est. Nous transformons ensuite cet en-tête en un format base64URL.
2. Ensuite, nous prenons les données de la charge utile (les informations que nous voulons inclure dans le token) et nous les transformons également en un format base64URL.
3. Après cela, nous combinons l'en-tête et la charge utile encodés avec notre clé secrète pour créer une signature. Cette signature aide à garantir que le token n'a pas été falsifié.
4. Enfin, nous mettons tout ensemble : l'en-tête encodé, la charge utile et la signature pour créer le token JWT final. Ce token est ce que nous pouvons utiliser dans nos applications pour authentifier les utilisateurs et autoriser l'accès à certaines ressources.

La méthode base64URLEncode garantit que les données sont encodées dans un format adapté aux URL, les rendant sûres pour la transmission sur le web. Au sein de notre classe `Jwt`, cette méthode est utilisée en interne par la fonction encode pour encoder à la fois les sections d'en-tête et de charge utile du token.

Cela dit, procédons au test et voyons notre premier token JWT, hourra !

### Le point de terminaison de connexion

Dans notre projet, le dossier **api** sert de point d'entrée pour les requêtes. Maintenant que nous avons implémenté l'algorithme pour encoder et créer un token JWT, procédons à son test. Pour ce faire, nous allons créer un fichier **login.php** dans notre dossier **api**. Dans ce fichier, nous allons envoyer une requête contenant le nom d'utilisateur et le mot de passe de l'utilisateur profilé ou créé dans notre interface utilisateur frontend **register.php**. Nous allons transmettre les détails de l'utilisateur requis au format JSON :

```php
{
    "username": "test",
    "password": "12345"
}
```

Veuillez intégrer l'extrait de code suivant dans le fichier **login.php** situé dans notre répertoire **api** :

```php

require __DIR__ . '/bootstrap.php';

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    header('ALLOW: POST');
    exit();
}

$contentType = isset($_SERVER["CONTENT_TYPE"]) ? trim($_SERVER["CONTENT_TYPE"]) : '';


if ($contentType !== 'application/json') {
    http_response_code(415);
    echo json_encode(["message" => "Only JSON content is supported"]);
    exit();
}

$data = json_decode(file_get_contents('php://input'), true);

if ($data === null) {
    http_response_code(400);
    echo json_encode(["message" => "Invalid JSON data"]);
    exit();
}


if (!array_key_exists('username', $data) || !array_key_exists('password', $data)) {
    http_response_code(400);
    echo json_encode(["message" => "Missing login credentials"]);
    exit();
}
```

Cet extrait de code sert de logique backend pour la gestion des requêtes de connexion des utilisateurs. Il commence par inclure le fichier **bootstrap.php** pour initialiser les composants essentiels. Ensuite, il vérifie si la méthode de requête entrante est POST, retournant une erreur Method Not Allowed si ce n'est pas le cas. 

Ensuite, il vérifie que le type de contenu de la requête est JSON, répondant avec une erreur Unsupported Media Type si ce n'est pas le cas. Le code procède au décodage des données JSON du corps de la requête et vérifie leur validité. Si les données JSON sont invalides ou manquent des clés username et password, il retourne une erreur Bad Request.

Avant de procéder avec notre point de terminaison de connexion, nous devons configurer notre classe `UserGateway`, qui est déjà disponible dans notre modèle de projet dans le dossier **src**. Cette classe facilite l'interaction avec les données utilisateur dans la base de données. L'extrait fourni initialise la classe et définit une méthode `getByUsername()` pour récupérer les données utilisateur en fonction du nom d'utilisateur fourni.

```php

class UserGateway
{

    private PDO $conn;

    public function __construct(Database $database)
    {
        $this->conn = $database->getConnection();
    }


    public function getByUsername(string $username): array | false
    {
        $sql = 'SELECT * FROM user WHERE username = :username';
        $stmt = $this->conn->prepare($sql);
        $stmt->bindValue(':username', $username, PDO::PARAM_STR);

        $stmt->execute();

        return $stmt->fetch(PDO::FETCH_ASSOC);
    }
}
```

![Image](https://www.freecodecamp.org/news/content/images/2024/04/1_Tc_Mdl0618eD5ZPmfv-mEA.jpg)

Vous verrez le besoin de cela au fur et à mesure que nous avancions.

Procédez à **login.php**.

D'accord, après cette courte pause publicitaire, nous pouvons créer une instance de classe appelée `$user_gateway` et lui passer notre connexion `$database`. Ensuite, nous récupérons les données utilisateur en fonction du nom d'utilisateur fourni à partir de l'instance `$user_gateway` en utilisant la méthode `getByUsername()`. Si aucun utilisateur n'est trouvé (indiquant une authentification invalide), nous retournons un statut de réponse HTTP 401 ainsi qu'un message d'erreur correspondant au format JSON. 

Nous validons le mot de passe fourni par rapport au mot de passe haché stocké dans les données utilisateur. Si la vérification du mot de passe échoue, nous retournons un statut similaire 401 et un message d'erreur. Si l'authentification est réussie, nous construisons une charge utile contenant l'ID et le nom de l'utilisateur. Par la suite, nous créons un token JWT en encodant la charge utile à l'aide de la classe `Jwt` instanciée avec la clé secrète des variables d'environnement. Enfin, nous répondons avec le token généré au format JSON, permettant l'accès aux ressources protégées, qui seront implémentées dans une section ultérieure.

Le code pour implémenter cette logique serait le suivant :

```php
$user_gateway = new UserGateway($database);

$user = $user_gateway->getByUsername($data['username']);

if ($user === false) {
    http_response_code(401);
    echo json_encode(["message" => "invalid authentication"]);
    exit;
}

if (!password_verify($data['password'], $user['password_hash'])) {
    http_response_code(401);
    echo json_encode(["message" => "invalid authentication"]);
    exit;
}


$payload = [
    "id" => $user['id'],
    "name" => $user["name"]
];


$JwtController = new Jwt($_ENV["SECRET_KEY"]);

$token =$$JwtController->encode($payload);

echo json_encode(["token" => $token]);
```

Code complet de **login.php** :

```php
<?php

require __DIR__ . '/bootstrap.php';

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    header('ALLOW: POST');
    exit();
}

$contentType = isset($_SERVER["CONTENT_TYPE"]) ? trim($_SERVER["CONTENT_TYPE"]) : '';


if ($contentType !== 'application/json') {
    http_response_code(415);
    echo json_encode(["message" => "Only JSON content is supported"]);
    exit();
}

$data = json_decode(file_get_contents('php://input'), true);

if ($data === null) {
    http_response_code(400);
    echo json_encode(["message" => "Invalid JSON data"]);
    exit();
}


if (!array_key_exists('username', $data) || !array_key_exists('password', $data)) {
    http_response_code(400);
    echo json_encode(["message" => "Missing login credentials"]);
    exit();
}

$user_gateway = new UserGateway($database);

$user = $user_gateway->getByUsername($data['username']);

if ($user === false) {
    http_response_code(401);
    echo json_encode(["message" => "invalid authentication"]);
    exit;
}

if (!password_verify($data['password'], $user['password_hash'])) {
    http_response_code(401);
    echo json_encode(["message" => "invalid authentication"]);
    exit;
}


require __DIR__ . "/tokens.php";

$refresh_token_gateway = new RefreshTokenGateway($database, $_ENV["SECRET_KEY"]);

$refresh_token_gateway->create($refresh_token, $refresh_token_expiry);


```

Maintenant que nous avons configuré notre point de terminaison de connexion, établi les connexions à la base de données et implémenté l'algorithme d'encodage JWT, rien ne nous empêche d'obtenir notre premier token JWT. Procédons aux étapes suivantes pour tester notre application :

1. Veuillez naviguer vers notre interface utilisateur pour l'inscription des utilisateurs. L'URL devrait être [http://localhost/php_auth_jwt_tut/register.php](http://localhost/php_auth_jwt_tut/register.php) si vous avez suivi la structure du projet.
2. Envoyez le nom d'utilisateur et le mot de passe de l'utilisateur créé au point de terminaison de connexion ([http://localhost/php_auth_jwt_tut/api/login.php](http://localhost/php_auth_jwt_tut/register.php)) au format JSON, comme ceci, et envoyez la requête :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/1_Yrpa_En9sjEKsK9ruO_jhg.jpg)
_test du point de terminaison_

Et voilà ! Tout simplement, nous obtenons notre token JWT !

## Ressources protégées et décodage des JSON Web Tokens

Ayant généré avec succès un token JWT, explorons maintenant comment nous pouvons protéger nos ressources et vérifier le contenu du token en le décodant.

Vous constaterez que nos classes de contrôleur, `StudentController.php`, et la classe de passerelle `StudentGateway.php`, situées dans le dossier **src**, ont déjà été configurées avec des méthodes essentielles. Maintenant, il ne reste plus qu'à instancier ces classes dans notre **index.php**, servant de point d'entrée pour nos requêtes dans le dossier **api**.

Pour ce faire, ajoutez l'extrait de code suivant dans le fichier **index.php** situé dans le dossier **api** de notre projet :

```php
<?php

require __DIR__ . '/bootstrap.php';

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    header('ALLOW: POST');
    exit();
}

$contentType = isset($_SERVER["CONTENT_TYPE"]) ? trim($_SERVER["CONTENT_TYPE"]) : '';


if ($contentType !== 'application/json') {
    http_response_code(415);
    echo json_encode(["message" => "Only JSON content is supported"]);
    exit();
}

$data = json_decode(file_get_contents('php://input'), true);

if ($data === null) {
    http_response_code(400);
    echo json_encode(["message" => "Invalid JSON data"]);
    exit();
}


if (!array_key_exists('username', $data) || !array_key_exists('password', $data)) {
    http_response_code(400);
    echo json_encode(["message" => "Missing login credentials"]);
    exit();
}

$user_gateway = new UserGateway($database);

$user = $user_gateway->getByUsername($data['username']);

if ($user === false) {
    http_response_code(401);
    echo json_encode(["message" => "invalid authentication"]);
    exit;
}

if (!password_verify($data['password'], $user['password_hash'])) {
    http_response_code(401);
    echo json_encode(["message" => "invalid authentication"]);
    exit;
}


$payload = [
    "id" => $user['id'],
    "name" => $user["name"]
];


$JwtController = new Jwt($_ENV["SECRET_KEY"]);

$token =$JwtController->encode($payload);

echo json_encode(["token" => $token]);

$user = new UserGateway($database);


$gateway = new StudentGateway($database);

$controller = new StudentController($gateway);


$controller->processRequest($_SERVER['REQUEST_METHOD']);
```

Comment les fichiers sont structurés à ce stade actuel :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/1_MAuYnkgxspnOmgDINUvkSQ.jpg)
_structure des fichiers sur VS Code_

Veuillez noter qu'après avoir testé le point de terminaison ([http://localhost/phpAuthJWT/api](http://localhost/phpAuthJWT/api)) à ce stade, vous recevrez le résultat suivant, sans aucune restriction appliquée :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/1__c8i8N9Vm4MGaZK4alfnQA.jpg)
_test du point de terminaison_

Note : Après avoir configuré la connexion à la base de données et importé le fichier fourni, **college.sql**, comme indiqué, les tables, y compris la table students, sont peuplées de données pré-ajoutées. Cela nous permet de visualiser les détails des étudiants qui sont actuellement visibles.

### Que se passe-t-il maintenant ?

Nous établissons une URL personnalisée pour récupérer des données via la méthode HTTP GET. L'URL, `[http://localhost/phpAuthJWT/api/](http://localhost/phpAuthJWT/api/getALLStudents)getAllStudents`, restera fonctionnelle grâce à la configuration du serveur spécifiée dans notre fichier **.htaccess** situé dans le dossier **api**. Lorsque nous faisons des requêtes à cette URL, nous inclurons notre token dans l'en-tête en utilisant l'en-tête de requête d'autorisation HTTP standard, en respectant le format du token porteur :

Authorization: Bearer <jwt token>

Dans notre dossier **src**, nous avons configuré une classe Auth où nous créerons une méthode pour valider le token JWT. Cette méthode vérifie si le token est fourni dans l'en-tête HTTP et le décode.

## Comment configurer la méthode Decode dans notre classe JWT

Lors de la configuration de la fonctionnalité de décodage dans la classe `Jwt`, comme nous l'avons fait avec la méthode d'encodage, nous nous assurerons que notre classe `Jwt`, située dans le dossier **src** de notre projet dans le fichier **jwt.php**, gère cette tâche. Pour ce faire, nous incorporerons les extraits de code suivants dans notre classe `Jwt` - les nouvelles méthodes sont les méthodes `decode` et `base64UrlDecode`, complétant ainsi sa structure. Le code final ressemblera à ce qui suit :

```php

class Jwt
{

    public function __construct(private string $key)
    {

    }

    public function encode(array $payload): string
    {

        $header = json_encode([
            "alg" => "HS256",
            "typ" => "JWT"
        ]);

        $header = $this->base64URLEncode($header);
        $payload = json_encode($payload);
        $payload = $this->base64URLEncode($payload);

        $signature = hash_hmac("sha256", $header . "." . $payload, $this->key, true);
        $signature = $this->base64URLEncode($signature);
        return $header . "." . $payload . "." . $signature;
    }


   
    public function decode(string $token): array
    {
        if (
            preg_match(
                "/^(?<header>.+)\.(?<payload>.+)\.(?<signature>.+)$/",
                $token,
                $matches
            ) !== 1
        ) {

            throw new InvalidArgumentException("invalid token format");
        }

        $signature = hash_hmac(
            "sha256",
            $matches["header"] . "." . $matches["payload"],
            $this->key,
            true
        );

        $signature_from_token = $this->base64URLDecode($matches["signature"]);

        if (!hash_equals($signature, $signature_from_token)) {

            // throw new Exception("signature doesn't match");
            throw new InvalidSignatureException;
        }

        $payload = json_decode($this->base64URLDecode($matches["payload"]), true);

        return $payload;
    }

  
    private function base64URLEncode(string $text): string
    {

        return str_replace(['+', '/', '='], ['-', '_', ''], base64_encode($text));
    }

    private function base64URLDecode(string $text): string
    {
        return base64_decode(
            str_replace(
                ["-", "_"],
                ["+", "/"],
                $text
            )
        );
    }

  
}
```

### Méthode Decode :

La méthode `decode` est responsable du décodage d'un token JWT en ses composants d'en-tête et de charge utile respectifs. Voici un bref aperçu de ce qu'elle fait :

1. **Validation du Token** : Tout d'abord, elle vérifie si le token fourni suit le format attendu de trois sections séparées par des points.
2. **Vérification de la Signature** : Elle recalcule la signature basée sur l'en-tête et la charge utile du token et la compare avec la signature fournie dans le token. Cette étape garantit l'intégrité du token.
3. **Extraction de la Charge Utile** : Si la vérification de la signature réussit, elle décode la composante de charge utile du token à partir de l'encodage base64 URL en un format JSON. Cette charge utile décodée contient des informations sur l'utilisateur associé au token.
4. Enfin, elle retourne la charge utile décodée sous forme de tableau associatif.

### Méthode base64URLDecode :

La méthode `base64URLDecode` est une fonction auxiliaire utilisée spécifiquement pour décoder les chaînes qui ont été encodées en utilisant l'encodage base64 URL. Voici une décomposition de sa fonctionnalité :

1. **Remplacement des Caractères** : Elle remplace d'abord les caractères `-` et `_` dans la chaîne encodée par `+` et `/` respectivement. Cette étape est nécessaire car l'encodage URL remplace certains caractères pour une transmission sûre sur le web.
2. **Décodage Base64** : Après le remplacement des caractères, elle effectue l'opération de décodage base64 standard sur la chaîne modifiée.
3. Enfin, elle retourne la chaîne décodée.

En résumé, la méthode `decode` valide et extrait la charge utile d'un token JWT, tandis que la méthode `base64URLDecode` aide à décoder les chaînes encodées en utilisant l'encodage base64 URL, garantissant l'intégrité et l'exactitude des données décodées.

### Ressources protégées

Maintenant que nous avons terminé la configuration, finalisons notre classe `Jwt`. Il est essentiel de restreindre l'accès à nos points de terminaison sans l'en-tête d'autorisation requis. Par exemple, l'accès à l'URL `[http://localhost/phpAuthJWT/api/](http://localhost/phpAuthJWT/api/getALLStudents)getAllStudents` doit être restreint si l'en-tête d'autorisation nécessaire est absent, et l'accès aux ressources doit être refusé si l'URL est incorrecte.

Pour y parvenir, ajoutez l'extrait de code suivant en haut de votre fichier **index.php**, qui sert de point d'entrée pour accéder à nos données étudiantes. Collez ce code après avoir importé le fichier de configuration **bootstrap.php**.

```php
require __DIR__ . '/bootstrap.php';

$path = parse_url($_SERVER["REQUEST_URI"], PHP_URL_PATH);

$parts = explode("/", $path);


$resource = $parts[3];

$id = $parts[4] ?? null;

if ($resource != "getAllStudents") {

    http_response_code(404);
    exit;
}
```

Cet extrait montre comment nous avons extrait le chemin de l'URI demandé en utilisant la fonction `parse_url()`, isolant le point de terminaison accessible par l'utilisateur. Ensuite, en divisant le chemin en segments en utilisant la fonction `explode()`, nous permettant d'identifier la ressource demandée. Si la ressource demandée n'est pas getAllStudents, indiquant un point de terminaison invalide, le code répond avec un code de statut 404 Not Found, signalant que la ressource demandée n'existe pas. Cela garantit que seuls les points de terminaison valides peuvent être accessibles, empêchant l'accès non autorisé aux ressources de notre API.

Note : Pour vérifier que notre projet fonctionne comme prévu, envoyez une requête au point de terminaison getAllStudents à l'adresse http://localhost/phpAuthJWT/api/getAllStudents

Cette requête nous aidera à nous assurer que notre API est correctement configurée et capable de récupérer toutes les données des étudiants.

### Vérification des en-têtes pour le schéma d'autorisation correct

Nous avons établi une URL personnalisée, mais il est crucial de vérifier que le token JWT fourni dans l'en-tête est valide. Pour ce faire, nous allons utiliser la classe Auth, qui est déjà disponible dans le dossier **src** de notre projet. Cette classe, qui a été fournie avec notre modèle de projet, nous aidera à garantir l'intégrité du token JWT.

**Auth.php** :

```php
class Auth
{



    public function __construct(private UserGateway $user_gateway, private Jwt $JwtCtrl)
    {
    }



    public function authenticateJWTToken(): bool
    {

        if (!preg_match("/^Bearer\s+(.*)$/", $_SERVER["HTTP_AUTHORIZATION"], $matches)) {
            http_response_code(400);
            echo json_encode(["message" => "incomplete authorization header"]);
            return false;
        }

        try {
            $data = $this->JwtCtrl->decode($matches[1]);
        } catch (InvalidSignatureException) {

            http_response_code(401);
            echo json_encode(["message" => "invalid signature"]);
            return false;
        } catch (Exception $e) {

            http_response_code(400);
            echo json_encode(["message" => $e->getMessage()]);
            return false;
        }



        return true;
    }
}
```

Cette classe est responsable de la gestion de l'authentification des tokens JWT. Au sein de la classe, nous avons une méthode de constructeur qui initialise l'objet `Auth` avec des instances de deux autres classes : `UserGateway` et `Jwt`.

Absolument ! Décomposons l'extrait de code de manière plus détaillée et narrative :

Dans l'extrait de code PHP fourni, nous avons défini une classe nommée `Auth`. Cette classe est responsable de la gestion de l'authentification des tokens JWT. Au sein de la classe, nous avons une méthode de constructeur qui initialise l'objet `Auth` avec des instances de deux autres classes : `UserGateway` et `Jwt`.

```php
class Auth
{
    public function __construct(private UserGateway $user_gateway, private Jwt $JwtCtrl)
    {
    }
    // Autres méthodes iront ici...
}
```

La méthode de constructeur permet à la classe `Auth` d'interagir avec les données utilisateur via la classe `UserGateway` et de gérer les tokens JWT en utilisant la classe `Jwt`.

Ensuite, nous avons une méthode appelée `authenticateJWTToken()`, qui est chargée de vérifier la validité d'un token JWT présent dans l'en-tête d'autorisation HTTP des requêtes entrantes.

```php
public function authenticateJWTToken(): bool
{
    
}
```

Au sein de la méthode `authenticateJWTToken()`, le code vérifie d'abord si l'en-tête d'autorisation est correctement formaté et contient un token JWT valide.

```php
if (!preg_match("/^Bearer\s+(.*)$/", $_SERVER["HTTP_AUTHORIZATION"], $matches)) {
    http_response_code(400);
    echo json_encode(["message" => "incomplete authorization header"]);
    return false;
}
```

Si l'en-tête d'autorisation est incomplet ou mal formaté, la méthode retourne une réponse 400 Bad Request avec un message indiquant le problème.

Ensuite, le code tente de décoder le token JWT en utilisant la méthode `decode()` de la classe `Jwt`. Si le processus de décodage échoue en raison d'une signature invalide ou de toute autre exception, des codes de réponse HTTP appropriés et des messages d'erreur sont retournés.

```php
try {
    $data = $this->JwtCtrl->decode($matches[1]);
} catch (InvalidSignatureException) {
    http_response_code(401);
    echo json_encode(["message" => "invalid signature"]);
    return false;
} catch (Exception $e) {
    http_response_code(400);
    echo json_encode(["message" => $e->getMessage()]);
    return false;
}
```

Si le token JWT est décodé avec succès sans aucune exception, la méthode retourne `true`, indiquant que le processus d'authentification a réussi.

La méthode `authenticateJWTToken()` garantit que les requêtes entrantes contiennent un token JWT valide dans l'en-tête d'autorisation et gère divers scénarios d'erreur de manière élégante pour fournir un retour d'information approprié aux clients interagissant avec l'API.

## Création d'instances dans le point d'entrée de l'API

Maintenant que nous avons terminé la configuration de nos méthodes, ajoutons nos instances de classe pour permettre la protection de nos ressources contre les utilisateurs non autorisés.

**index.php** :

```php

declare(strict_types=1);

require __DIR__ . '/bootstrap.php';

$path = parse_url($_SERVER["REQUEST_URI"], PHP_URL_PATH);

$parts = explode("/", $path);


$resource = $parts[3];

if ($resource != "getAllStudents") {

    http_response_code(404);
    exit;
}


$user = new UserGateway($database);


$JwtCtrl = new Jwt($_ENV["SECRET_KEY"]);

$auth = new Auth($user, $JwtCtrl);

if (!$auth->authenticateJWTToken()) {
    exit;
}



$gateway = new StudentGateway($database);

$controller = new StudentController($gateway);



$controller->processRequest($_SERVER['REQUEST_METHOD']);
```

Une fois que nous avons incorporé l'extrait fourni dans notre **index.php**, il est crucial d'observer les différents scénarios qui se produisent lorsque nous accédons à notre point de terminaison de l'API à l'adresse `http://localhost/phpAuthJWT/api/getAllStudents`.

En accédant à cette URL, nous pouvons être témoins de plusieurs résultats possibles, chacun indicatif d'un état ou d'une fonctionnalité différente au sein de notre application. Ces résultats peuvent inclure :

1. **Réponse réussie** : Si le processus d'authentification est réussi et que le token JWT est valide, l'API doit retourner une réponse contenant les données souhaitées, telles qu'une liste de tous les étudiants.
2. **Token invalide** : Dans le cas où le token JWT fourni dans l'en-tête d'autorisation de la requête est invalide, expiré ou mal formaté, l'API doit répondre avec un message d'erreur indiquant le problème. Cela garantit que seuls les utilisateurs autorisés peuvent accéder aux ressources protégées.
3. **Accès non autorisé** : Si la requête n'inclut pas de token JWT ou manque d'autorisation appropriée, l'API doit répondre avec un code de statut 401 Non autorisé, indiquant que l'accès à la ressource demandée est restreint.
4. **Point de terminaison invalide** : Si l'URL fournie ne correspond à aucun des points de terminaison ou routes définis au sein de notre application, l'API doit répondre avec un code de statut 404 Non trouvé, signalant que la ressource demandée n'existe pas.

En examinant ces résultats, nous pouvons obtenir des informations sur la fonctionnalité et la fiabilité de notre API, garantissant qu'elle se comporte comme prévu et fournit des réponses appropriées à différents types de requêtes et de scénarios.

Fonctionnant correctement avec l'en-tête d'autorisation : `http://localhost/phpAuthJWT/api/getAllStudents`

![Image](https://miro.medium.com/v2/resize:fit:700/1*KpQHCYFFD7qN7j2gjTvaBg.png)
_test du point de terminaison_

Ne fonctionnant pas correctement sans l'en-tête d'autorisation : `http://localhost/phpAuthJWT/api/getAllStudents`

![Image](https://miro.medium.com/v2/resize:fit:700/1*BCtXpT7RiFoMq2IshlTl3Q.png)
_test du point de terminaison_

## Suggestions

Après avoir configuré notre JWT, un tout nouveau monde s'ouvre à nous. Vous pouvez expérimenter avec notre API en créant des URL personnalisées pour des tâches spécifiques, comme trouver des étudiants par nom ou permettre aux utilisateurs de créer et de mettre à jour leurs propres profils d'étudiants en suivant l'`user_id` de l'utilisateur. Vous pouvez utiliser diverses méthodes HTTP comme GET, POST, PATCH et DELETE pour gérer les données de manière efficace. Bien que cet article couvre les bases, il existe une abondance de possibilités à explorer lorsqu'il s'agit de créer une API robuste.

Les tokens JWT offrent un moyen pratique et efficace de gérer l'authentification et l'autorisation dans les applications web. Cependant, il est crucial de reconnaître qu'ils ne sont pas absolument infaillibles. Il est essentiel d'éviter de mettre des informations sensibles dans la composante de charge utile du token, car la charge utile est généralement encodée en base64URL et peut être facilement décodée. De plus, la clé secrète utilisée pour signer le token doit être tenue secrète et ne jamais être exposée à des informations publiques, car cela peut compromettre la sécurité du système.

Dans les tokens JWT, l'en-tête, la charge utile et la signature sont tous encodés en base64URL, garantissant la compatibilité avec les URL et une transmission sûre sur le web. Cependant, il est important de noter que les tokens JWT doivent avoir une durée d'expiration pour atténuer le risque de mauvaise utilisation des tokens. Dans la partie suivante, nous explorerons comment implémenter l'expiration des tokens et introduire des tokens de rafraîchissement pour améliorer la sécurité de notre système d'authentification. 

Nous avons exploré l'implémentation des JSON Web Tokens (JWT) et appris comment les utiliser. Cependant, une préoccupation majeure en matière de sécurité persiste : nos tokens, spécifiquement appelés tokens d'accès dans ce contexte, peuvent actuellement accéder à nos ressources indéfiniment. Cette pratique ne respecte pas les normes de l'industrie. Pour améliorer la sécurité, nous devrions implémenter l'expiration des tokens pour nos JWT. De plus, l'adoption d'un système à deux tokens comprenant un token de rafraîchissement en plus de notre token d'accès est recommandée.

## Comment implémenter l'expiration des tokens

![Image](https://miro.medium.com/v2/resize:fit:630/1*iexXyX3pAwzlv3M-YPQJsg.jpeg)

Nous allons nous concentrer sur l'implémentation des tokens d'accès et des tokens de rafraîchissement. Toute addition nécessaire à notre projet ou à la structure de la base de données sera introduite au fur et à mesure de notre progression dans l'implémentation.

Commençons tout de suite !

Les tokens d'accès doivent avoir un mécanisme d'expiration. Nous avons besoin que nos tokens JWT expire automatiquement après une courte période, obligeant les utilisateurs à demander un nouveau token une fois qu'il expire. 

Demander aux utilisateurs de se connecter chaque minute lorsque le token expire n'est pas convivial. Au lieu de cela, nous pouvons émettre un token de rafraîchissement. Le token de rafraîchissement a généralement une durée de vie plus longue que le token d'accès. Lorsque le token d'accès expire, le client peut utiliser le token de rafraîchissement pour obtenir un nouveau token d'accès. Nous allons incorporer un point de terminaison pour que le client rafraîchisse le token d'accès de manière transparente.

En continuant là où nous nous sommes arrêtés, nous allons maintenant créer un point de terminaison de rafraîchissement dans notre dossier **api**. Comme nous le savons, ce point de terminaison sert de point d'entrée pour la gestion des requêtes liées au rafraîchissement des tokens et sera nommé **refresh.php**.

```php
<?php
declare(strict_types=1);

require __DIR__ . "/bootstrap.php";

if ($_SERVER["REQUEST_METHOD"] !== "POST") {
    
    http_response_code(405);
    header("Allow: POST");
    exit;
}

$data = (array) json_decode(file_get_contents("php://input"), true);

if ( ! array_key_exists("token", $data)) {

    http_response_code(400);
    echo json_encode(["message" => "missing token"]);
    exit;
}

$JwtController = new Jwt($_ENV["SECRET_KEY"]);
```

Il vérifie si la méthode de requête entrante est POST ; sinon, il répond avec un code de statut HTTP 405 et permet uniquement les requêtes POST. Le script analyse ensuite les données JSON du corps de la requête, en s'assurant qu'il contient une clé token. Si le token est manquant, il répond avec un code de statut 400 et un message JSON indiquant l'absence du token. Enfin, le script initialise un objet `Jwt` avec une clé secrète des variables d'environnement pour un traitement ultérieur du token.

![Image](https://miro.medium.com/v2/resize:fit:630/1*qPsrno17jnQB-TiKQztLVQ.png)
_fichier refresh.php_

Avant de procéder à la configuration de notre point de terminaison de rafraîchissement, nous allons créer une classe appelée `RefreshTokenGateway.php` pour gérer les opérations liées au rafraîchissement des tokens. La classe `RefreshTokenGateway` inclut des méthodes pour créer, supprimer, récupérer et gérer les tokens de rafraîchissement expirés dans notre base de données.

La classe `RefreshTokenGateway` utilise une connexion PDO et une clé secrète pour le hachage des tokens. Son constructeur initialise les variables de connexion à la base de données et de clé secrète. La méthode `create` génère un hachage pour le token et l'insère dans la table `refresh_token` avec son heure d'expiration. La méthode `delete` supprime un token de la base de données en fonction de sa valeur de hachage. La méthode `getByToken` récupère les détails du token en fonction de son hachage. Enfin, la méthode `deleteExpired` supprime les tokens expirés de la base de données, assurant une gestion efficace des tokens.

Dans l'ensemble, la classe `RefreshTokenGateway` fournit une fonctionnalité essentielle pour maintenir et gérer les tokens de rafraîchissement de manière sécurisée au sein de notre application web.

**RefreshTokenGateway.php** :

```php
<?php

class RefreshTokenGateway
{
    private PDO $conn;
    private string $key;
    
    public function __construct(Database $database, string $key)
    {
        $this->conn = $database->getConnection();
        $this->key = $key;
    }
    
    public function create(string $token, int $expiry): bool
    {
        $hash = hash_hmac("sha256", $token, $this->key);
        
        $sql = "INSERT INTO refresh_token (token_hash, expires_at)
                VALUES (:token_hash, :expires_at)";
                
        $stmt = $this->conn->prepare($sql);
        
        $stmt->bindValue(":token_hash", $hash, PDO::PARAM_STR);
        $stmt->bindValue(":expires_at", $expiry, PDO::PARAM_INT);
        
        return $stmt->execute();
    }
    
    public function delete(string $token): int
    {
        $hash = hash_hmac("sha256", $token, $this->key);
        
        $sql = "DELETE FROM refresh_token
                WHERE token_hash = :token_hash";
                
        $stmt = $this->conn->prepare($sql);
        
        $stmt->bindValue(":token_hash", $hash, PDO::PARAM_STR);
        
        $stmt->execute();
        
        return $stmt->rowCount();
    }
    
    public function getByToken(string $token): array | false
    {
        $hash = hash_hmac("sha256", $token, $this->key);
        
        $sql = "SELECT *
                FROM refresh_token
                WHERE token_hash = :token_hash";
                
        $stmt = $this->conn->prepare($sql);
        
        $stmt->bindValue(":token_hash", $hash, PDO::PARAM_STR);
        
        $stmt->execute();
        
        return $stmt->fetch(PDO::FETCH_ASSOC);
    }
    
    public function deleteExpired(): int
    {
        $sql = "DELETE FROM refresh_token
                WHERE expires_at < UNIX_TIMESTAMP()";
            
        $stmt = $this->conn->query($sql);
        
        return $stmt->rowCount();
    }
}


```

### Structure de dossier mise à jour

D'après l'extrait de code fourni pour notre classe `[RefreshTokenGateway](https://github.com/Oghenekparobo/php_auth_jwt_tut/blob/refresh-token/src/RefreshTokenGateway.php)`, il est évident qu'une nouvelle table a été incorporée dans notre base de données. Nous avons mis à jour notre fichier **college.sql** pour accommoder ce changement. Veuillez importer le fichier SQL mis à jour dans votre base de données, en suivant le processus décrit dans la première partie de cet article.

De plus, une nouvelle classe d'exception nommée `TokenExpiredException` a été introduite. Assurez-vous de mettre à jour la structure de votre projet ou vos fichiers en conséquence pour inclure cette nouvelle gestion d'exception. Cela garantit que votre projet reste à jour et aligné avec les derniers changements dans la gestion des tokens.

Avant de terminer la configuration de notre point de terminaison de rafraîchissement pour obtenir un nouveau token d'accès après expiration, intégrons la récupération de notre token de rafraîchissement et de notre token d'accès dans notre point de terminaison de connexion. Nous avons la classe `RefreshTokenGateway` pour gérer les tokens de rafraîchissement, et nous allons créer le fichier **tokens.php** dans notre dossier **api** pour la création de tokens, qui sera utilisé dans les points de terminaison de rafraîchissement et de connexion. Cette approche garantit un processus de gestion des tokens simple et unifié dans notre application.

**tokens.php** :

```php
<?php

$payload = [
    "sub" => $user["id"],
    "name" => $user["name"],
    "exp" => time() + 20
];

$JwtController = new Jwt($_ENV["SECRET_KEY"]);

$access_token = $JwtController->encode($payload);

$refresh_token_expiry = time() + 432000;

$refresh_token = $JwtController->encode([
    "sub" => $user["id"],
    "exp" => $refresh_token_expiry
]);

echo json_encode([
    "access_token" => $access_token,
    "refresh_token" => $refresh_token
]);
```

La principale différence entre le token de rafraîchissement et la charge utile (les revendications du token d'accès) est que la charge utile contient des informations détaillées sur l'utilisateur comme l'ID et le nom, et son expiration est plus courte (20 secondes) pour des raisons de sécurité. D'autre part, le token de rafraîchissement ne contient que l'ID de l'utilisateur et a une expiration plus longue (5 jours) pour permettre une authentification de longue durée sans nécessiter de connexions fréquentes. Cette séparation des tokens et leurs durées de vie respectives améliore la sécurité et la commodité des utilisateurs dans les systèmes d'authentification basés sur des tokens.

![Image](https://miro.medium.com/v2/resize:fit:630/1*0CqrZ5zsgvCHDyhiKRU53g.png)

**login.php** :

```php
<?php

require __DIR__ . '/bootstrap.php';

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    header('ALLOW: POST');
    exit();
}

$contentType = isset($_SERVER["CONTENT_TYPE"]) ? trim($_SERVER["CONTENT_TYPE"]) : '';


if ($contentType !== 'application/json') {
    http_response_code(415);
    echo json_encode(["message" => "Only JSON content is supported"]);
    exit();
}

$data = json_decode(file_get_contents('php://input'), true);

if ($data === null) {
    http_response_code(400);
    echo json_encode(["message" => "Invalid JSON data"]);
    exit();
}


if (!array_key_exists('username', $data) || !array_key_exists('password', $data)) {
    http_response_code(400);
    echo json_encode(["message" => "Missing login credentials"]);
    exit();
}

$user_gateway = new UserGateway($database);

$user = $user_gateway->getByUsername($data['username']);

if ($user === false) {
    http_response_code(401);
    echo json_encode(["message" => "invalid authentication"]);
    exit;
}

if (!password_verify($data['password'], $user['password_hash'])) {
    http_response_code(401);
    echo json_encode(["message" => "invalid authentication"]);
    exit;
}


require __DIR__ . "/tokens.php";

$refresh_token_gateway = new RefreshTokenGateway($database, $_ENV["SECRET_KEY"]);

$refresh_token_gateway->create($refresh_token, $refresh_token_expiry);


```

Tester notre point de terminaison de connexion avec les bons paramètres devrait donner la réponse suivante :

![Image](https://miro.medium.com/v2/resize:fit:630/1*gSWQIGxsREf7xHoB0ZDpHQ.png)
_test du point de terminaison_

Note : Avant de continuer, mettons à jour notre classe `Jwt`, la fonction `decode` en particulier. La fonction `decode` mise à jour dans la classe `Jwt` vérifie si un token a le bon format, en s'assurant qu'il a un en-tête, une charge utile et une signature. Elle vérifie ensuite la signature du token pour confirmer qu'il n'a pas été falsifié. Après cela, elle décode la charge utile (contenant les informations de l'utilisateur et l'heure d'expiration) à partir du token. Enfin, elle vérifie si le token a expiré, en lançant une erreur si c'est le cas. Dans l'ensemble, ces étapes garantissent que le token est valide, non altéré et dans sa période d'expiration pour une utilisation sécurisée dans l'application.

Classe `Jwt` :

```php
<?php

class Jwt
{

    public function __construct(private string $key)
    {

    }

    public function encode(array $payload): string
    {

        $header = json_encode([
            "alg" => "HS256",
            "typ" => "JWT"
        ]);

        $header = $this->base64URLEncode($header);
        $payload = json_encode($payload);
        $payload = $this->base64URLEncode($payload);

        $signature = hash_hmac("sha256", $header . "." . $payload, $this->key, true);
        $signature = $this->base64URLEncode($signature);
        return $header . "." . $payload . "." . $signature;
    }


   
    public function decode(string $token): array
    {
        if (preg_match("/^(?<header>.+)\.(?<payload>.+)\.(?<signature>.+)$/",
                   $token,
                   $matches) !== 1) {
                       
            throw new InvalidArgumentException("invalid token format");
        }
        
        $signature = hash_hmac("sha256",
                               $matches["header"] . "." . $matches["payload"],
                               $this->key,
                               true);   
                               
        $signature_from_token = $this->base64urlDecode($matches["signature"]);
        
        if ( ! hash_equals($signature, $signature_from_token)) {
            
            throw new InvalidSignatureException;
        }
        
        $payload = json_decode($this->base64urlDecode($matches["payload"]), true);
        
        if ($payload["exp"] < time()) {
            
            throw new TokenExpiredException;
        }
        
        return $payload;
    }
    
  
    private function base64URLEncode(string $text): string
    {

        return str_replace(['+', '/', '='], ['-', '_', ''], base64_encode($text));
    }

    private function base64URLDecode(string $text): string
    {
        return base64_decode(
            str_replace(
                ["-", "_"],
                ["+", "/"],
                $text
            )
        );
    }

  
}

```

Classe **UserGateway.php** mise à jour

```php
<?php

class UserGateway
{
    private PDO $conn;
    
    public function __construct(Database $database)
    {
        $this->conn = $database->getConnection();
    }
    
    public function getByAPIKey(string $key): array | false
    {
        $sql = "SELECT *
                FROM user
                WHERE api_key = :api_key";
                
        $stmt = $this->conn->prepare($sql);
        
        $stmt->bindValue(":api_key", $key, PDO::PARAM_STR);
        
        $stmt->execute();
        
        return $stmt->fetch(PDO::FETCH_ASSOC);
    }
    
    public function getByUsername(string $username): array | false
    {
        $sql = "SELECT *
                FROM user
                WHERE username = :username";
                
        $stmt = $this->conn->prepare($sql);
        
        $stmt->bindValue(":username", $username, PDO::PARAM_STR);
        
        $stmt->execute();
        
        return $stmt->fetch(PDO::FETCH_ASSOC);
    }
    
    public function getByID(int $id): array | false
    {
        $sql = "SELECT *
                FROM user
                WHERE id = :id";
                
        $stmt = $this->conn->prepare($sql);
        
        $stmt->bindValue(":id", $id, PDO::PARAM_INT);
        
        $stmt->execute();
        
        return $stmt->fetch(PDO::FETCH_ASSOC);
    }
}

```

Terminer avec le point de terminaison 'refresh' :

```php
<?php
declare(strict_types=1);

require __DIR__ . "/bootstrap.php";

if ($_SERVER["REQUEST_METHOD"] !== "POST") {
    
    http_response_code(405);
    header("Allow: POST");
    exit;
}

$data = (array) json_decode(file_get_contents("php://input"), true);

if ( ! array_key_exists("token", $data)) {

    http_response_code(400);
    echo json_encode(["message" => "missing token"]);
    exit;
}

$JwtController = new Jwt($_ENV["SECRET_KEY"]);

try {
    $payload = $JwtController->decode($data["token"]);
    
} catch (Exception) {
    
    http_response_code(400);
    echo json_encode(["message" => "invalid token"]);
    exit;
}

$user_id = $payload["sub"];


$refresh_token_gateway = new RefreshTokenGateway($database, $_ENV["SECRET_KEY"]);

$refresh_token = $refresh_token_gateway->getByToken($data["token"]);

if ($refresh_token === false) {
    
    http_response_code(400);
    echo json_encode(["message" => "invalid token (not on whitelist)"]);
    exit;
}
                         
$user_gateway = new UserGateway($database);

$user = $user_gateway->getByID($user_id);

if ($user === false) {
    
    http_response_code(401);
    echo json_encode(["message" => "invalid authentication"]);
    exit;
}

require __DIR__ . "/tokens.php";

$refresh_token_gateway->delete($data["token"]);

$refresh_token_gateway->create($refresh_token, $refresh_token_expiry);

```

Le code procède ensuite à la validation de la méthode de requête HTTP, en s'assurant que seules les requêtes POST sont acceptées pour les opérations sensibles comme la gestion des tokens. Cette validation est significative car elle aide à prévenir l'accès non autorisé et garantit la sécurité des processus d'authentification.

Ensuite, le code récupère et décode les données JSON du corps de la requête, en recherchant spécifiquement une clé token. Ce token est crucial pour l'authentification et le contrôle d'accès au sein de l'application. Si le token est manquant, le code répond avec un message d'erreur, soulignant l'importance d'inclure des tokens valides pour un accès sécurisé.

Le token décodé est ensuite passé à l'instance `JwtController` pour décoder sa charge utile et valider son authenticité. Cette étape est cruciale car elle vérifie l'intégrité du token et s'assure qu'il n'a pas été falsifié ou contrefait.

De plus, le code interagit avec un `RefreshTokenGateway` pour gérer les tokens de rafraîchissement, qui jouent un rôle vital dans la génération sécurisée des tokens d'accès. Les tokens de rafraîchissement offrent un moyen d'obtenir de nouveaux tokens d'accès sans nécessiter que l'utilisateur se connecte à nouveau, améliorant ainsi l'expérience utilisateur et maintenant un accès continu aux ressources.

Lorsque l'utilisateur se connecte via le point de terminaison de connexion, deux tokens cruciaux sont fournis : un token d'accès et un token de rafraîchissement. Le token d'accès accorde un accès immédiat aux ressources, tandis que le token de rafraîchissement sert d'outil d'autorisation à long terme. Si le token d'accès expire, le token de rafraîchissement est alors passé au point de terminaison de rafraîchissement. Cette action déclenche la génération d'un nouveau token d'accès, qui, à son tour, crée un nouveau token de rafraîchissement. Ce processus forme un mécanisme robuste et sécurisé garantissant un accès continu aux ressources tout en maintenant des niveaux élevés de sécurité et de commodité pour l'utilisateur.

![Image](https://miro.medium.com/v2/resize:fit:630/1*FztaD8zQDrfY-nRdYQAbzA.png)
_test du point de terminaison_

![Image](https://miro.medium.com/v2/resize:fit:630/1*tN5iW6surrwPWlwFD0iRLA.png)
_test du point de terminaison_

## Conclusion

Dans les extraits de code analysés et les explications concernant la gestion des tokens, les mécanismes d'authentification et l'utilisation des tokens de rafraîchissement au sein d'une application web, plusieurs conclusions clés peuvent être tirées.

Tout d'abord, l'authentification basée sur les tokens, en particulier l'utilisation des JSON Web Tokens, offre un moyen sécurisé et efficace de gérer les processus d'authentification et d'autorisation des utilisateurs. Les JWT encapsulent les informations utilisateur dans un format compact et sont signés numériquement, garantissant ainsi leur intégrité et leur authenticité.

Deuxièmement, l'implémentation des tokens d'accès et des tokens de rafraîchissement améliore la sécurité et l'expérience utilisateur. Les tokens d'accès fournissent un accès immédiat aux ressources et ont une durée de vie courte, favorisant la sécurité en limitant leur utilité en cas d'accès non autorisé. D'autre part, les tokens de rafraîchissement ont une durée de vie plus longue et permettent aux utilisateurs d'obtenir de nouveaux tokens d'accès sans authentification répétée, améliorant ainsi la commodité pour l'utilisateur.

De plus, l'application stricte du typage, la validation appropriée des méthodes de requête HTTP et les vérifications du format des tokens sont des éléments cruciaux pour garantir la robustesse et la fiabilité des systèmes d'authentification basés sur les tokens. Ces pratiques aident à prévenir les vulnérabilités courantes telles que les tentatives d'accès non autorisé, la falsification des tokens et l'utilisation de tokens invalides.

Dans l'ensemble, en combinant des pratiques de gestion des tokens sécurisées, des mécanismes d'authentification efficaces et le respect des meilleures pratiques de codage, les applications web peuvent atteindre un niveau élevé de sécurité, de convivialité et de résilience contre les menaces potentielles.

Voir le code complet [ici](https://github.com/Oghenekparobo/php_auth_jwt_tut/tree/refresh-token).