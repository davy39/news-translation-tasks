---
title: Comment développer avec CodeIgniter sur Ubuntu – Guide d'installation pas à
  pas de l'environnement
subtitle: ''
author: valentine Gatwiri
co_authors: []
series: null
date: '2025-01-24T14:46:15.280Z'
originalURL: https://freecodecamp.org/news/how-to-develop-with-codeigniter-on-ubuntu-environment-setup
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1737640002689/7c78cd9c-40ef-45b3-82f6-97bc33f713d7.png
tags:
- name: Web Development
  slug: web-development
- name: webdev
  slug: webdev
- name: code
  slug: code
- name: codeigniter
  slug: codeigniter
- name: PHP
  slug: php
seo_title: Comment développer avec CodeIgniter sur Ubuntu – Guide d'installation pas
  à pas de l'environnement
seo_desc: CodeIgniter is a popular open-source PHP framework you can use to build
  dynamic and robust web applications. It’s simple to use, fast, and flexible. This
  makes it a good option for any developer who wants to have a light yet powerful
  framework that w...
---

CodeIgniter est un framework PHP open-source populaire que vous pouvez utiliser pour créer des applications web dynamiques et robustes. Il est simple à utiliser, rapide et flexible. Cela en fait une bonne option pour tout développeur qui souhaite disposer d'un framework léger mais puissant qui lui permettra de prototyper ou de développer des applications scalables rapidement.

De plus, l'architecture MVC (Modèle-Vue-Contrôleur) de CodeIgniter facilite l'organisation du code et la séparation de la logique métier de l'interface utilisateur, ce qui permet d'obtenir des projets plus propres et plus faciles à maintenir.

Que vous construisiez un petit site web ou une application complexe, CodeIgniter dispose d'une série d'outils, de bibliothèques et d'assistants qui simplifient le processus de développement. Ils vous aident à gérer des tâches courantes comme les requêtes de base de données, la gestion des sessions et la validation des formulaires. De nombreux développeurs adorent cet outil pour sa facilité d'utilisation, ce qui en fait un framework idéal pour les débutants comme pour les codeurs expérimentés.

Dans ce guide, je vais vous guider à travers le processus de configuration de CodeIgniter étape par étape, afin que vous disposiez d'un environnement de développement local entièrement fonctionnel pour votre projet.

### Prérequis

Avant de commencer, assurez-vous de répondre aux exigences suivantes :

* Connaissances de base en PHP : La compréhension de la syntaxe PHP et des concepts de programmation de base vous aidera à suivre plus facilement.

* Serveur web (par exemple, Apache ou NGINX) : CodeIgniter a besoin d'un serveur pour fonctionner. Assurez-vous d'avoir un serveur fonctionnel configuré sur votre machine locale ou votre environnement d'hébergement.

* PHP installé : Vous aurez besoin de PHP 7.3 ou supérieur (selon la version de CodeIgniter que vous utilisez).

* Système de gestion de base de données : CodeIgniter prend en charge plusieurs bases de données, mais MySQL est la plus couramment utilisée. Assurez-vous d'avoir accès à un système de gestion de base de données et de connaître ses identifiants.

* Téléchargement de CodeIgniter : Téléchargez la dernière version de CodeIgniter depuis le site officiel, le dépôt GitHub, ou utilisez `composer` pour l'installer.

## Comment utiliser Composer pour installer CodeIgniter

Maintenant que vous comprenez les prérequis et que tout est configuré, passons à l'installation de CodeIgniter. L'une des méthodes les plus simples et efficaces pour installer CodeIgniter est d'utiliser Composer, un outil populaire de gestion des dépendances pour PHP. Dans cette section, je vais vous guider à travers les étapes pour installer CodeIgniter en utilisant Composer.

Tout d'abord, créez un nouveau répertoire avec `mkdir my_project`, puis accédez à ce répertoire avec `cd my_project`. Exécutez la commande Composer suivante pour installer CodeIgniter. Vous pouvez spécifier la version que vous souhaitez (par exemple, `^4.0` pour la dernière version de CodeIgniter 4).

```bash
composer create-project codeigniter4/appstarter .
```

Cette commande téléchargera et installera la dernière version de CodeIgniter 4 et configurera le projet pour vous :

![Téléchargement de CodeIgniter via Composer.](https://cdn.hashnode.com/res/hashnode/image/upload/v1737222358773/c0be04da-c507-41cf-b98e-8c9126146b31.png align="center")

Une fois l'installation terminée, vous devriez voir la structure du projet CodeIgniter dans votre répertoire. Pour vérifier que tout fonctionne, vous pouvez démarrer le serveur PHP intégré en exécutant :

```bash
php spark serve
```

Sortie :

![Sortie de la commande php spark serve.](https://cdn.hashnode.com/res/hashnode/image/upload/v1737224950979/8e7ccdac-ce8b-4b71-b41b-5ee02dfd9970.png align="center")

Ensuite, ouvrez votre navigateur et allez sur [`http://localhost:8080`](http://localhost:8080). Vous devriez voir la page d'accueil de CodeIgniter.

![Page d'accueil de CodeIgniter.](https://cdn.hashnode.com/res/hashnode/image/upload/v1737225118799/c7a38536-62fa-4788-814d-cd246a973691.png align="center")

## Comment installer CodeIgniter manuellement

Si vous préférez ne pas utiliser Composer, ou si vous travaillez dans un environnement où Composer n'est pas disponible, vous pouvez installer CodeIgniter manuellement. Cette méthode consiste à télécharger directement les fichiers du framework et à configurer votre projet manuellement. Bien que cela nécessite quelques étapes supplémentaires par rapport à l'utilisation de Composer, c'est toujours simple et cela vous donne un contrôle total sur le processus d'installation.

Dans cette section, je vais vous guider à travers les étapes pour installer manuellement CodeIgniter et le configurer pour votre projet.

**Téléchargement via Git :**

```bash
cd /var/www/html
sudo git clone https://github.com/bcit-ci/CodeIgniter.git codeigniter
```

Ou **téléchargement en ZIP (depuis le site officiel de CodeIgniter)** : [Télécharger ici](https://www.codeigniter.com/download). Extrayez-le dans `/var/www/html`. Vous pouvez le faire via le terminal ou l'interface utilisateur.

### Extraction du fichier ZIP via l'interface utilisateur

Si vous n'êtes pas à l'aise avec les outils en ligne de commande, vous pouvez facilement extraire le fichier ZIP en utilisant l'interface graphique de votre ordinateur. Voici comment faire :

Cliquez sur `files/Other Locations/computer` pour accéder à `/var/www/html`. Copiez le fichier `.Zip` que vous avez téléchargé précédemment dans le dossier créé et faites un `clic droit`. Ensuite, cliquez sur `extract here` pour le décompresser.

![Image d'extraction du ZIP.](https://cdn.hashnode.com/res/hashnode/image/upload/v1737210782723/25317e2b-151b-491e-8e83-89c32d9cf5ee.png align="center")

### Extraction du fichier ZIP via le terminal

Si vous êtes à l'aise avec la ligne de commande, vous pouvez extraire le fichier ZIP de CodeIgniter directement via le terminal. Cette méthode est particulièrement utile pour les utilisateurs de Linux et macOS ou si vous travaillez sur un serveur distant sans interface graphique.

Tout d'abord, assurez-vous que `unzip` est installé sur votre système Ubuntu :

```bash
sudo apt update
sudo apt install unzip
```

**Vérifiez vos permissions** pour vous assurer que vous avez l'accès nécessaire au répertoire `/var/www/html`. Si nécessaire, utilisez `sudo` pour les privilèges administratifs.

### Étapes pour extraire le fichier

En supposant que votre fichier téléchargé se trouve actuellement dans `downloads/data...`, déplacez-le vers `/var/www/html` :

```bash
sudo mv /mnt/data/CodeIgniter.zip /var/www/html
```

Accédez au répertoire `/var/www/html` :

```bash
cd /var/www/html
```

Extrayez le fichier ZIP en utilisant la commande `unzip` pour extraire le contenu :

```bash
sudo unzip CodeIgniter.zip
```

Après l'extraction, définissez les bons propriétaires et permissions pour l'accès au serveur web :

```bash
sudo chown -R www-data:www-data /var/www/html
sudo chmod -R 755 /var/www/html
```

> * `www-data` (première partie) → L'**utilisateur**.

> * `www-data` (deuxième partie) → Le **groupe**.

![Image du dossier extrait (Codeigniter-develop).](https://cdn.hashnode.com/res/hashnode/image/upload/v1737212632072/6240acc1-27bd-49fe-acd4-5b3f80a92163.png align="center")

> Renommez le dossier `Codeigniter-develop /bcit-ci-CodeIgniter-bcb17eb/...` en simplement `codeigniter`.

### Vérification de l'extraction

Visitez l'URL de votre serveur web (par exemple, [`http://localhost`](http://localhost)) pour vérifier si le contenu est correctement déployé.

### **Définir les permissions des dossiers**

Après avoir installé CodeIgniter, assurez-vous que les permissions de vos répertoires sont correctes, en particulier pour les répertoires `writable` et `cache`. Cela garantit que CodeIgniter peut écrire des logs, des fichiers cache et des données de session.

Exécutez les commandes suivantes pour définir les permissions correctes :

```bash
sudo chmod -R 755 /var/www/html/codeigniter
```

### **Configurer l'URL de base**

L'URL de base de votre projet doit être configurée dans `application/config/config.php`.

Ouvrez le fichier `config.php` :

```bash
sudo nano /var/www/html/codeigniter/application/config/config.php
```

Sortie :

![Image du terminal config.php.](https://cdn.hashnode.com/res/hashnode/image/upload/v1737213372442/259f712f-2df4-4517-a382-88966b021950.png align="center")

Définissez le `base_url` comme suit :

```php
$config['base_url'] = 'http://votre-domaine-ou-ip/';
```

Remplacez [`http://votre-domaine-ou-ip/`](http://votre-domaine-ou-ip/) par votre domaine ou adresse IP réelle où le projet sera accessible.

Après avoir apporté des modifications :

* **Enregistrez le fichier** : Appuyez sur `Ctrl + O` (Write Out).

* **Confirmez le nom du fichier** : Appuyez sur `Entrée`.

* **Quittez l'éditeur** : Appuyez sur `Ctrl + X`.

<div data-node-type="callout">
<div data-node-type="callout-emoji">💡</div>
<div data-node-type="callout-text">Vous pouvez également éditer les fichiers en utilisant l'interface graphique en y accédant depuis <code>Other Locations//var/www/html/codeigniter</code></div>
</div>

### **Configurer la base de données (si applicable)**

Si votre projet utilise une base de données, vous devrez configurer la connexion à la base de données dans `application/config/database.php`.

Pour ce faire, ouvrez le fichier de configuration de la base de données :

```bash
sudo nano /var/www/html/codeigniter/application/config/database.php
```

Configurez la connexion à la base de données en définissant les options suivantes :

```php
$db['default'] = array(
    'dsn'   => '',
    'hostname' => 'localhost',
    'username' => 'votre-nom-utilisateur-db',
    'password' => 'votre-mot-de-passe-db',
    'database' => 'votre-nom-base-de-donnees',
    'dbdriver' => 'mysqli',
    'dbprefix' => '',
    'pconnect' => FALSE,
    'db_debug' => (ENVIRONMENT !== 'production'),
    'cache_on' => FALSE,
    'cachedir' => '',
    'char_set' => 'utf8',
    'dbcollat' => 'utf8_general_ci',
    'swap_pre' => '',
    'encrypt' => FALSE,
    'compress' => FALSE,
    'stricton' => FALSE,
    'failover' => array(),
    'save_queries' => TRUE
);
```

Remplacez `votre-nom-utilisateur-db`, `votre-mot-de-passe-db` et `votre-nom-base-de-donnees` par vos identifiants de base de données réels.

### **Définir l'environnement**

CodeIgniter utilise le paramètre d'environnement pour charger différents fichiers de configuration en fonction de l'environnement (par exemple, développement, production).

Pour définir l'environnement, ouvrez le fichier `index.php` dans le répertoire racine de votre projet :

```bash
sudo nano /var/www/html/codeigniter/index.php
```

Localisez la ligne suivante :

```php
define('ENVIRONMENT', 'development');
```

Vous pouvez le définir sur `production`, `testing` ou `development` en fonction de votre configuration. Pour le développement, il doit être défini sur `development`.

### **Charger automatiquement les bibliothèques, assistants ou fichiers de configuration**

Vous pouvez spécifier quelles bibliothèques, assistants ou fichiers de configuration charger automatiquement dans `application/config/autoload.php`. Ouvrez le fichier de configuration de chargement automatique :

```bash
sudo nano /var/www/html/codeigniter/application/config/autoload.php
```

Modifiez le tableau de chargement automatique pour charger les bibliothèques et assistants couramment utilisés :

```php
$autoload['libraries'] = array('database', 'session', 'form_validation');
$autoload['helper'] = array('url', 'file');
```

### **Activer Mod Rewrite (pour des URLs propres)**

Si vous souhaitez des URLs propres, vous devez activer `mod_rewrite` sur Apache. Modifiez le fichier de configuration Apache comme suit :

```bash
sudo nano /etc/apache2/sites-available/000-default.conf
```

Assurez-vous que la directive `AllowOverride` est définie sur `All` dans la section `<Directory>` :

```bash
<Directory /var/www/html>
    AllowOverride All
</Directory>
```

Activez mod_rewrite et redémarrez Apache :

```bash
sudo a2enmod rewrite
sudo systemctl restart apache2
```

### Vérifier l'emplacement du répertoire CodeIgniter

Si CodeIgniter n'est pas dans `/opt/lampp/htdocs`, déplacez-le là-bas :

```bash
sudo mv /var/www/html/codeigniter /opt/lampp/htdocs/
```

### **Tester CodeIgniter**

Ouvrez votre navigateur web et accédez à l'URL de base ([`http://votre-domaine-ou-ip`](http://votre-domaine-ou-ip)). Vous devriez voir la page d'accueil par défaut de CodeIgniter si tout est correctement configuré :

![Page d'accueil de CodeIgniter.](https://cdn.hashnode.com/res/hashnode/image/upload/v1737218343140/7a41485a-152e-496e-9ba7-811e5c4b774b.png align="center")

Exécutez `curl` [`ifconfig.me`](http://ifconfig.me) pour trouver votre IP publique. Si vous hébergez CodeIgniter sur une machine locale (par exemple, dans votre réseau domestique), utilisez la commande suivante pour vérifier votre IP locale : `hostname -I`.

## Dépannage

Si vous rencontrez des problèmes lors de la configuration de CodeIgniter, voici quelques problèmes courants et comment les résoudre :

### **Définir CodeIgniter comme application par défaut**

Si vous souhaitez que CodeIgniter se charge comme application par défaut (au lieu de la page d'accueil de XAMPP si vous avez XAMPP installé), supprimez ou renommez le fichier `index.php` par défaut dans le répertoire `htdocs` :

```bash
sudo mv /opt/lampp/htdocs/index.php /opt/lampp/htdocs/index.php.bak
```

Déplacez les fichiers CodeIgniter à la racine du dossier `htdocs` :

```bash
sudo mv /opt/lampp/htdocs/codeigniter/* /opt/lampp/htdocs/
```

### **Redémarrer Apache**

Après avoir apporté des modifications, redémarrez Apache pour appliquer la configuration :

```bash
sudo /opt/lampp/lampp restart
```

### **Créer un contrôleur**

Pour commencer à développer votre application, vous pouvez créer un contrôleur pour gérer les requêtes.

![Dossiers de l'application.](https://cdn.hashnode.com/res/hashnode/image/upload/v1737219751160/af7240e8-2793-45b9-9cff-1f9a74add34f.png align="center")

Créez un nouveau contrôleur dans `application/controllers/` comme suit :

```php
<?php
class Welcome extends CI_Controller {
    public function index() {
        $this->load->view('welcome_message');
    }
}
```

Ensuite, créez des vues et des modèles. Les vues vont dans `application/views/` et les modèles dans `application/models/`. Vous pouvez commencer à ajouter vos vues et modèles en conséquence.

## Conclusion

Configurer un environnement de développement pour CodeIgniter sur Ubuntu est une étape essentielle pour exploiter tout le potentiel de ce framework PHP léger mais puissant.

En suivant attentivement les étapes décrites — de l'installation des prérequis, de la configuration des permissions de fichiers et de la personnalisation des paramètres à la création de contrôleurs, de vues et de modèles — vous êtes maintenant équipé pour commencer à construire des applications web dynamiques.