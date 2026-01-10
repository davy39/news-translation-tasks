---
title: Comment créer un pipeline CI/CD de base avec des webhooks sur Linux
subtitle: ''
author: Juan P. Romano
co_authors: []
series: null
date: '2025-01-28T22:46:46.245Z'
originalURL: https://freecodecamp.org/news/create-a-basic-cicd-pipeline-with-webhooks-on-linux
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1737640144719/9035597c-0a69-4146-93cc-8bd659384169.png
tags:
- name: Linux
  slug: linux
- name: linux for beginners
  slug: linux-for-beginners
- name: Python
  slug: python
- name: Python 3
  slug: python3
- name: python beginner
  slug: python-beginner
- name: ci-cd
  slug: ci-cd
- name: CI/CD
  slug: cicd
seo_title: Comment créer un pipeline CI/CD de base avec des webhooks sur Linux
seo_desc: 'In the fast-paced world of software development, delivering high-quality
  applications quickly and reliably is crucial. This is where CI/CD (Continuous Integration
  and Continuous Delivery/Deployment) comes into play.

  CI/CD is a set of practices and to...'
---

Dans le monde rapide du développement logiciel, livrer des applications de haute qualité rapidement et de manière fiable est crucial. C'est là que le **CI/CD** (Intégration Continue et Livraison/Déploiement Continu) entre en jeu.

Le CI/CD est un ensemble de pratiques et d'outils conçus pour automatiser et rationaliser le processus d'intégration des changements de code, de leur test et de leur déploiement en production. En adoptant le CI/CD, votre équipe peut réduire les erreurs manuelles, accélérer les cycles de publication et garantir que votre code est toujours dans un état déployable.

Dans ce tutoriel, nous nous concentrerons sur une approche adaptée aux débutants pour configurer un pipeline CI/CD de base en utilisant Bitbucket, un serveur Linux et Python avec Flask. Plus précisément, nous créerons un processus automatisé qui récupère les derniers changements d'un dépôt Bitbucket vers votre serveur Linux chaque fois qu'il y a un push ou une fusion vers une branche spécifique.

Ce processus sera alimenté par les webhooks de Bitbucket et un simple serveur Python basé sur Flask qui écoute les événements de webhook entrants et déclenche le déploiement.

Il est important de noter que le CI/CD est un domaine vaste et complexe, et ce tutoriel est conçu pour fournir une compréhension de base plutôt qu'un guide exhaustif.

Nous aborderons les bases de la configuration d'un pipeline CI/CD en utilisant des outils accessibles aux débutants. Gardez simplement à l'esprit que les systèmes CI/CD du monde réel impliquent souvent des outils et des configurations plus avancés, tels que la conteneurisation, l'orchestration et des environnements de test multi-étapes.

À la fin de ce tutoriel, vous aurez un exemple fonctionnel de la façon d'automatiser les déploiements en utilisant Bitbucket, Linux et Python, que vous pourrez personnaliser et développer selon vos besoins.

### Table des matières :

1. [Pourquoi le CI/CD est-il important ?](#heading-pourquoi-le-cicd-est-il-important)

2. [Étape 1 : Configurer un webhook dans Bitbucket](#heading-etape-1-configurer-un-webhook-dans-bitbucket)

3. [Étape 2 : Configurer le serveur Flask sur votre serveur Linux](#heading-etape-2-configurer-le-serveur-flask-sur-votre-serveur-linux)

4. [Étape 3 : Exposer l'application Flask (Optionnel)](#heading-etape-3-exposer-lapplication-flask-optionnel)

5. [Étape 4 : Tester la configuration](#heading-etape-4-tester-la-configuration)

6. [Étape 5 : Considérations de sécurité](#heading-etape-5-considerations-de-securite)

7. [Conclusion](#heading-conclusion)

## Pourquoi le CI/CD est-il important ?

Le CI/CD est devenu une pierre angulaire du développement logiciel moderne pour plusieurs raisons. Tout d'abord, il accélère le processus de développement. En automatisant les tâches répétitives comme les tests et le déploiement, les développeurs peuvent se concentrer davantage sur l'écriture de code et moins sur les processus manuels. Cela conduit à une livraison plus rapide de nouvelles fonctionnalités et de corrections de bugs, ce qui est particulièrement important dans les marchés concurrentiels où la vitesse peut faire la différence.

Un autre avantage clé du CI/CD est la réduction des erreurs et l'amélioration de la fiabilité. Les tests automatisés garantissent que chaque changement de code est rigoureusement vérifié pour détecter les problèmes avant qu'il ne soit intégré dans la base de code principale. Cela minimise le risque d'introduire des bugs qui pourraient perturber l'application ou nécessiter des corrections coûteuses plus tard. Les pipelines de déploiement automatisés réduisent également la probabilité d'erreurs humaines lors du processus de publication, garantissant que les déploiements sont cohérents et prévisibles.

Le CI/CD favorise également une meilleure collaboration entre les membres de l'équipe. Dans les flux de travail de développement traditionnels, l'intégration des changements de code de plusieurs développeurs peut être un processus long et sujet aux erreurs. Avec le CI/CD, le code est intégré et testé fréquemment, souvent plusieurs fois par jour. Cela signifie que les conflits sont détectés et résolus tôt, et que la base de code reste dans un état stable. En conséquence, les équipes peuvent travailler plus efficacement et avec une plus grande confiance, même lorsque plusieurs contributeurs travaillent sur différentes parties du projet simultanément.

Enfin, le CI/CD soutient l'amélioration continue et l'innovation. En automatisant le processus de déploiement, les équipes peuvent publier des mises à jour en production plus fréquemment et avec moins de risques. Cela leur permet de recueillir des retours des utilisateurs plus rapidement et d'itérer sur leurs produits plus efficacement.

### Ce que nous allons couvrir dans ce tutoriel

Dans ce tutoriel, nous allons passer en revue le processus de configuration d'un pipeline CI/CD simple qui automatise le déploiement des changements de code d'un dépôt Bitbucket vers un serveur Linux. Voici ce que vous allez apprendre :

1. Comment configurer un dépôt Bitbucket pour envoyer des notifications de webhook chaque fois qu'il y a un push ou une fusion vers une branche spécifique.

2. Comment configurer un serveur Python basé sur Flask sur votre serveur Linux pour écouter les événements de webhook entrants.

3. Comment écrire un script qui récupère les derniers changements du dépôt et les déploie sur le serveur.

4. Comment tester et dépanner votre processus de déploiement automatisé.

À la fin de ce tutoriel, vous aurez un exemple fonctionnel d'un pipeline CI/CD de base que vous pourrez personnaliser et étendre selon vos besoins. Commençons !

## **Étape 1 : Configurer un webhook dans Bitbucket**

Avant de commencer la configuration, expliquons brièvement ce qu'est un **webhook** et comment il s'intègre dans notre processus CI/CD.

Un webhook est un mécanisme qui permet à un système de notifier un autre système d'un événement en temps réel. Dans le contexte de Bitbucket, un webhook peut être configuré pour envoyer une requête HTTP (souvent une requête POST avec des données de charge utile) à une URL spécifiée chaque fois qu'un événement spécifique se produit dans votre dépôt, tel qu'un push vers une branche ou une fusion de pull request.

Dans notre cas, le webhook notifiera notre serveur Python basé sur Flask (en cours d'exécution sur votre serveur Linux) chaque fois qu'il y a un push ou une fusion vers une branche spécifique. Cette notification déclenchera un script sur le serveur pour récupérer les derniers changements du dépôt et les déployer automatiquement. Essentiellement, le webhook agit comme un pont entre Bitbucket et votre serveur, permettant une automatisation transparente du processus de déploiement.

Maintenant que vous comprenez le rôle d'un webhook, configurons-en un dans Bitbucket :

1. Connectez-vous à Bitbucket et accédez à votre dépôt.

2. Dans la barre latérale de gauche, cliquez sur **Paramètres**.

3. Dans la section **Workflow**, trouvez et cliquez sur **Webhooks**.

4. Cliquez sur le bouton **Ajouter un webhook**.

5. Entrez un nom pour votre webhook (par exemple, "Automatic Pull").

6. Dans le champ **URL**, fournissez l'URL de votre serveur où le webhook enverra la requête. Si vous exécutez une application Flask localement, cela pourrait être quelque chose comme [`http://votre-ip-de-serveur/pull-repo`](http://votre-ip-de-serveur/pull-repo). (Pour les environnements de production, il est fortement recommandé d'utiliser HTTPS pour sécuriser la communication entre Bitbucket et votre serveur.)

7. Dans la section **Déclencheurs**, choisissez les événements que vous souhaitez écouter. Pour cet exemple, nous sélectionnerons **Push** (et éventuellement, **Pull Request Merged** si vous souhaitez également déployer après les fusions).

8. Enregistrez le webhook avec un nom explicite pour qu'il soit facile à identifier plus tard.

Une fois le webhook configuré, Bitbucket enverra une requête POST à l'URL spécifiée chaque fois que l'événement sélectionné se produit. Dans les étapes suivantes, nous configurerons un serveur Flask pour gérer ces requêtes entrantes et déclencher le processus de déploiement.

Voici ce que vous devriez voir lorsque vous configurez le webhook Bitbucket

![Écran Bitbucket montrant à l'utilisateur la création d'un webhook, où votre serveur récupérera les modifications lorsque vous pousserez ou fusionnerez dans votre dépôt.](https://cdn.hashnode.com/res/hashnode/image/upload/v1738092826221/e0d96fd3-d843-4064-a08d-4de95b985800.png align="center")

## **Étape 2 : Configurer le serveur Flask sur votre serveur Linux**

Dans l'étape suivante, vous allez configurer un simple serveur web sur votre machine Linux qui écoutera le webhook de Bitbucket. Lorsqu'il recevra la notification, il exécutera un `git pull` ou un pull forcé (en cas de modifications locales) pour mettre à jour le dépôt.

### **Installer Flask :**

Pour créer l'application Flask, installez d'abord Flask en exécutant :

```bash
pip install flask
```

### **Créer l'application Flask :**

Créez un nouveau script Python (par exemple, [`app_repo_pull.py`](http://app.py)) sur votre serveur et ajoutez le code suivant :

```python
from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/pull-repo', methods=['POST'])
def pull_repo():
    try:
        # Récupère les derniers changements du dépôt distant
        subprocess.run(["git", "-C", "/chemin/vers/votre/depot", "fetch"], check=True)
        # Réinitialise la branche locale pour correspondre à la branche distante 'test'
        subprocess.run(["git", "-C", "/chemin/vers/votre/depot", "reset", "--hard", "origin/test"], check=True)  # Remplacez 'test' par le nom de votre branche
        return "Force pull successful", 200
    except subprocess.CalledProcessError:
        return "Failed to force pull the repository", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

Voici ce que fait ce code :

* [`subprocess.run`](http://subprocess.run)`(["git", "-C", "/chemin/vers/votre/depot", "fetch"])` : Cette commande récupère les derniers changements du dépôt distant sans affecter le répertoire de travail local.

* [`subprocess.run`](http://subprocess.run)`(["git", "-C", "/chemin/vers/votre/depot", "reset", "--hard", "origin/test"])` : Cette commande effectue une réinitialisation forcée, forçant le dépôt local à correspondre à la branche distante `test`. Remplacez `test` par le nom de votre branche.

Assurez-vous de remplacer `/chemin/vers/votre/depot` par le chemin réel vers votre dépôt Git local.

## **Étape 3 : Exposer l'application Flask (Optionnel)**

Si vous souhaitez que l'application Flask soit accessible depuis l'extérieur de votre serveur, vous devez l'exposer publiquement. Pour cela, vous pouvez configurer un proxy inverse avec NGINX. Voici comment faire :

Tout d'abord, installez NGINX si vous ne l'avez pas déjà en exécutant cette commande :

```bash
sudo apt-get install nginx
```

Ensuite, vous devrez configurer NGINX pour proxyfier les requêtes vers votre application Flask. Ouvrez le fichier de configuration NGINX :

```bash
sudo nano /etc/nginx/sites-available/default
```

Modifiez la configuration pour inclure ce bloc :

```bash
server {
    listen 80;
    server_name votre-ip-de-serveur;

    location /pull-repo {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Maintenant, rechargez simplement NGINX pour appliquer les changements :

```bash
sudo systemctl reload nginx
```

## **Étape 4 : Tester la configuration**

Maintenant que tout est configuré, lancez l'application Flask en exécutant ce script Python :

```bash
python3 app_repo_pull.py
```

Pour tester si tout fonctionne :

1. **Faites un commit** : Poussez un commit vers la branche `test` dans votre dépôt Bitbucket. Cette action déclenchera le webhook.

2. **Déclenchement du webhook** : Le webhook enverra une requête POST à votre serveur. L'application Flask recevra cette requête, effectuera un pull forcé depuis la branche `test` et mettra à jour le dépôt local.

3. **Vérifiez le pull** : Vérifiez la sortie du journal de votre application Flask ou inspectez le dépôt local pour confirmer que les changements ont été récupérés et appliqués avec succès.

## **Étape 5 : Considérations de sécurité**

Lorsque vous exposez une application Flask sur Internet, sécuriser votre serveur et votre application est crucial pour le protéger contre les accès non autorisés, les violations de données et les attaques. Voici les domaines clés sur lesquels se concentrer :

#### **1. Utilisez un serveur sécurisé avec des règles de pare-feu appropriées**

Un serveur sécurisé est un serveur configuré pour minimiser l'exposition aux menaces externes. Cela implique l'utilisation de règles de pare-feu, la minimisation des services inutiles et la garantie que seuls les ports nécessaires sont ouverts pour la communication.

##### **Exemple de configuration d'un serveur sécurisé :**

* **Logiciel minimal** : Installez uniquement le logiciel dont vous avez besoin (par exemple, Python, Flask, NGINX) et supprimez les services inutiles.

* **Mises à jour du système d'exploitation** : Assurez-vous que le système d'exploitation de votre serveur est à jour avec les derniers correctifs de sécurité.

* **Configuration du pare-feu** : Utilisez un pare-feu pour contrôler le trafic entrant et sortant et limiter l'accès à votre serveur.

Par exemple, une configuration de base du **UFW (Uncomplicated Firewall)** sur Ubuntu pourrait ressembler à ceci :

```bash
# Autorisez SSH (port 22) pour l'accès à distance
sudo ufw allow ssh

# Autorisez HTTP (port 80) et HTTPS (port 443) pour le trafic web
sudo ufw allow http
sudo ufw allow https

# Activez le pare-feu
sudo ufw enable

# Vérifiez l'état du pare-feu
sudo ufw status
```

Dans ce cas :

* Le pare-feu autorise les connexions SSH entrantes sur le port 22, HTTP sur le port 80 et HTTPS sur le port 443.

* Tout port ou service inutile doit être bloqué par défaut pour limiter l'exposition aux attaques.

##### **Règles de pare-feu supplémentaires :**

* **Limitez l'accès au point de terminaison du webhook** : Idéalement, autorisez uniquement le trafic vers le point de terminaison du webhook à partir des adresses IP de Bitbucket pour empêcher l'accès externe. Vous pouvez configurer cela dans votre pare-feu ou en utilisant votre serveur web (par exemple, NGINX) en n'acceptant les requêtes que depuis la plage d'IP de Bitbucket.

* **Refusez tout autre trafic entrant** : Pour tout service qui n'a pas besoin d'être exposé à Internet (par exemple, les ports de base de données), assurez-vous que ces ports sont bloqués.

#### **2. Ajoutez une authentification à l'application Flask**

Puisque votre application Flask sera accessible publiquement via l'URL du webhook, vous devriez envisager d'ajouter une authentification pour garantir que seuls les utilisateurs autorisés (comme les serveurs de Bitbucket) peuvent déclencher le pull.

##### **Exemple d'authentification de base :**

Vous pouvez utiliser une authentification basée sur un jeton simple pour sécuriser votre point de terminaison de webhook. Voici un exemple de la façon de modifier votre application Flask pour nécessiter un jeton d'authentification :

```python
from flask import Flask, request, abort
import subprocess

app = Flask(__name__)

# Définissez un jeton secret pour la vérification du webhook
SECRET_TOKEN = 'votre-jeton-secret'

@app.route('/pull-repo', methods=['POST'])
def pull_repo():
    # Vérifiez si la requête contient le jeton correct
    token = request.headers.get('X-Hub-Signature')
    if token != SECRET_TOKEN:
        abort(403)  # Interdit si le jeton est incorrect

    try:
        subprocess.run(["git", "-C", "/chemin/vers/votre/depot", "fetch"], check=True)
        subprocess.run(["git", "-C", "/chemin/vers/votre/depot", "reset", "--hard", "origin/test"], check=True)
        return "Force pull successful", 200
    except subprocess.CalledProcessError:
        return "Failed to force pull the repository", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

##### **Comment cela fonctionne :**

* `X-Hub-Signature` est un en-tête personnalisé que vous ajoutez à la requête lors de la configuration du webhook dans Bitbucket.

* Seules les requêtes avec le jeton correct seront autorisées à déclencher le pull. Si le jeton est manquant ou incorrect, la requête est rejetée avec une réponse `403 Forbidden`.

Vous pouvez également utiliser des formes d'authentification plus complexes, telles que OAuth ou HMAC (Hash-based Message Authentication Code), mais cette approche simple par jeton fonctionne pour de nombreux cas.

#### **3. Utilisez HTTPS pour une communication sécurisée**

Il est crucial de chiffrer les données transmises entre votre application Flask et le webhook Bitbucket, ainsi que toute donnée sensible (telle que les jetons ou les mots de passe) transmise sur le réseau. Cela garantit que les attaquants ne peuvent pas intercepter ou modifier les données.

##### **Pourquoi HTTPS ?**

* **Chiffrement des données** : HTTPS chiffre la communication, garantissant que les données sensibles comme votre jeton d'authentification ne sont pas exposées aux attaques de type man-in-the-middle.

* **Confiance et intégrité** : HTTPS aide à garantir que les données reçues par votre serveur n'ont pas été altérées.

##### **Utilisation de Let's Encrypt pour sécuriser votre application Flask avec SSL :**

1. **Installez Certbot** (l'outil pour obtenir des certificats Let's Encrypt) :

```bash
sudo apt-get update
sudo apt-get install certbot python3-certbot-nginx
```

**Obtenez un certificat SSL gratuit pour votre domaine :**

```bash
sudo certbot --nginx -d votre-domaine.com
```

* Cette commande configurera automatiquement Nginx pour utiliser HTTPS avec un certificat SSL gratuit de Let's Encrypt.

* **Assurez-vous que HTTPS est utilisé** : Assurez-vous que votre application Flask ou la configuration Nginx force tout le trafic à utiliser HTTPS. Vous pouvez le faire en configurant une règle de redirection dans Nginx :

```bash
server {
    listen 80;
    server_name votre-domaine.com;

    # Redirigez HTTP vers HTTPS
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name votre-domaine.com;

    ssl_certificate /etc/letsencrypt/live/votre-domaine.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/votre-domaine.com/privkey.pem;

    # Autres configurations Nginx...
}
```

**Renouvellement automatique** : Les certificats Let's Encrypt sont valables pour 90 jours, il est donc important de configurer le renouvellement automatique :

```bash
sudo certbot renew --dry-run
```

Cette commande teste le processus de renouvellement pour s'assurer que tout fonctionne.

#### **4. Journalisation et surveillance**

Implémentez la journalisation et la surveillance pour votre application Flask afin de suivre les tentatives non autorisées, les erreurs ou les activités inhabituelles :

* **Journalisez les requêtes** : Journalisez toutes les requêtes entrantes, y compris l'adresse IP, les en-têtes de requête et le statut de la réponse, afin de surveiller toute activité suspecte.

* **Utilisez des outils de surveillance** : Configurez des outils comme **Prometheus**, **Grafana** ou **New Relic** pour surveiller les performances du serveur et la santé de l'application.

## Conclusion

Dans ce tutoriel, nous avons exploré comment configurer un pipeline CI/CD simple et adapté aux débutants qui automatise les déploiements en utilisant Bitbucket, un serveur Linux et Python avec Flask. Voici un récapitulatif de ce que vous avez appris :

1. **Fondamentaux du CI/CD** : Nous avons discuté des bases de l'Intégration Continue (CI) et de la Livraison/Déploiement Continu (CD), qui sont des pratiques essentielles pour automatiser l'intégration, les tests et le déploiement du code. Vous avez appris comment le CI/CD aide à accélérer le développement, à réduire les erreurs et à améliorer la collaboration entre les développeurs.

2. **Configuration des webhooks Bitbucket** : Vous avez appris comment configurer un webhook Bitbucket pour notifier votre serveur chaque fois qu'il y a un push ou une fusion vers une branche spécifique. Ce webhook sert de déclencheur pour initier le processus de déploiement automatiquement.

3. **Création d'un écouteur de webhook basé sur Flask** : Nous vous avons montré comment configurer une application Flask sur votre serveur Linux pour écouter les requêtes de webhook entrantes de Bitbucket. Cette application Flask reçoit les notifications et exécute les commandes Git nécessaires pour récupérer et déployer les derniers changements.

4. **Automatisation du processus de déploiement** : En utilisant Python et Flask, nous avons automatisé le processus de récupération des changements du dépôt Bitbucket et effectué un pull forcé pour garantir que le dernier code est déployé. Vous avez également appris comment configurer le serveur pour exposer l'application Flask et accepter les requêtes de manière sécurisée.

5. **Considérations de sécurité** : Nous avons couvert les étapes critiques de sécurité pour protéger votre processus de déploiement :

   * **Règles de pare-feu** : Nous avons discuté de la configuration des règles de pare-feu pour limiter l'exposition et garantir que seul le trafic autorisé (de Bitbucket) peut accéder à votre serveur.

   * **Authentification** : Nous avons ajouté une authentification basée sur un jeton pour garantir que seules les requêtes autorisées peuvent déclencher les déploiements.

   * **HTTPS** : Nous avons expliqué comment sécuriser la communication entre votre serveur et Bitbucket en utilisant des certificats SSL de Let's Encrypt.

   * **Journalisation et surveillance** : Enfin, nous avons recommandé de configurer la journalisation et la surveillance pour suivre toute activité inhabituelle ou erreur.

### **Prochaines étapes**

À la fin de ce tutoriel, vous avez maintenant un exemple fonctionnel d'un pipeline de déploiement automatisé. Bien que ce soit une implémentation de base, elle sert de fondation sur laquelle vous pouvez construire. À mesure que vous vous familiarisez avec le CI/CD, vous pouvez explorer des sujets avancés tels que :

* Pipelines de déploiement multi-étapes

* Intégration avec des outils de conteneurisation comme Docker

* Stratégies de test et de déploiement plus complexes

* Utilisation d'outils d'orchestration comme Kubernetes pour le scaling

Les pratiques CI/CD évoluent constamment, et en maîtrisant les bases, vous vous êtes préparé au succès alors que vous développez vos compétences dans ce domaine. Bonnes automatisations et merci d'avoir lu !

Vous pouvez [forker le code ici](https://github.com/jpromanonet/ci_cd_fcc/tree/main).