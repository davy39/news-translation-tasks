---
title: Comment construire un Rate Limiter avec Redis et Python pour mettre à l'échelle
  vos applications
subtitle: ''
author: Sravan Karuturi
co_authors: []
series: null
date: '2025-10-03T15:08:16.211Z'
originalURL: https://freecodecamp.org/news/build-a-rate-limiter-with-redis-and-python
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1759503803144/4d974610-95dc-4db8-989a-0d705dc4d431.png
tags:
- name: Python
  slug: python
- name: cybersecurity
  slug: cybersecurity
- name: api
  slug: api
seo_title: Comment construire un Rate Limiter avec Redis et Python pour mettre à l'échelle
  vos applications
seo_desc: If you've ever built a web application, you know that without a proper mechanism
  to control traffic, your application can become overwhelmed, leading to slow response
  times, server crashes, and a poor user experience. Even worse, it can leave you
  vul...
---

Si vous avez déjà construit une application web, vous savez que sans un mécanisme approprié pour contrôler le trafic, votre application peut être submergée, ce qui entraîne des temps de réponse lents, des plantages de serveur et une mauvaise expérience utilisateur. Pire encore, cela peut vous rendre vulnérable aux attaques par déni de service (DoS). C'est là qu'intervient le rate limiting.

Dans ce tutoriel, vous allez construire un Rate Limiter distribué. C'est le genre de système dont vous avez besoin lorsque votre application est déployée sur plusieurs serveurs ou machines virtuelles, et que vous devez appliquer une limite globale à toutes les requêtes entrantes.

Vous allez construire une application simple de réducteur d'URL, puis implémenter un Rate Limiter robuste pour celle-ci en utilisant une combinaison d'outils puissants et efficaces :

* Python et Flask pour votre application web.
    
* Redis comme magasin de données centralisé à haute vitesse pour le suivi des requêtes.
    
* Terraform et Proxmox pour définir et provisionner votre infrastructure de machines virtuelles.
    
* Docker pour conteneuriser votre application afin de faciliter son déploiement.
    
* Nginx comme Load balancer pour distribuer le trafic sur vos serveurs d'application.
    
* k6 pour tester la charge de votre système et prouver que votre Rate Limiter fonctionne réellement.
    

Ce guide est destiné aux nouveaux développeurs qui découvrent les concepts de conception de systèmes ou aux experts qui souhaitent simplement un rappel.

À la fin de ce guide, vous comprendrez non seulement le code, mais aussi l'architecture système complète requise pour déployer une application évolutive et résiliente.

Commençons !

## Prérequis

Bien que cela ne soit pas absolument nécessaire pour suivre, je vous recommande de configurer un serveur Proxmox sur un vieil ordinateur portable pour implémenter les sujets que vous apprenez et coder en même temps que l'article. Je recommande cette [playlist YouTube](https://www.youtube.com/watch?v=5j0Zb6x_hOk&list=PLT98CRl2KxKHnlbYhtABg6cF50bYa8Ulo) pour débuter. Veuillez noter que je ne suis en aucun cas affilié à cette chaîne. Je l'ai simplement trouvée utile.

Cependant, si vous n'avez pas de serveur Proxmox local, vous pouvez ignorer cette partie et simplement suivre pour comprendre comment un Rate Limiter est construit et comment il est configuré pour fonctionner correctement avec plusieurs serveurs.

## Table des matières

* [Prérequis](#heading-prerequis)
    
* [Vue d'ensemble : Notre architecture système](#heading-vue-densemble-notre-architecture-systeme)
    
* [Étape 1 : Comment définir l'infrastructure avec Terraform](#heading-etape-1-comment-definir-linfrastructure-avec-terraform)
    
* [Étape 2 : Comment implémenter la logique du Rate Limiter en Python](#heading-etape-2-comment-implementer-la-logique-du-rate-limiter-en-python)
    
* [Étape 3 : Conteneurisation et tests](#heading-etape-3-conteneurisation-et-tests)
    
* [Conclusion](#heading-conclusion)
    

## Vue d'ensemble : Notre architecture système

Avant de plonger dans le code, examinons l'architecture que nous construisons. J'utiliserai [Proxmox Virtual Environment](https://www.proxmox.com/en/products/proxmox-virtual-environment/overview) pour configurer un cluster de serveurs comme vous le feriez dans un centre de données.

### Comment configurer Proxmox

`Proxmox Virtual Environment` est une plateforme open source pour la virtualisation. Elle vous permet de gérer facilement plusieurs VM, conteneurs et autres clusters. Par exemple, j'ai transformé mon vieil ordinateur de jeu en un serveur Proxmox qui me permet d'exécuter plus de 20 machines virtuelles en même temps, ce qui le rend similaire à mon propre centre de données. Cela me permet d'expérimenter des applications distribuées en simulant des environnements de centre de données.

Pour configurer votre propre cluster, tout ce dont vous avez besoin est un vieil ordinateur. Vous pouvez télécharger l'image ISO [ici](https://www.proxmox.com/en/downloads) et démarrer à partir d'une clé USB. Une fois installé, vous pouvez configurer la machine hôte via un navigateur web sur n'importe quel autre ordinateur du même réseau.

Par exemple, mon serveur Proxmox est situé à `10.0.0.108` et je peux y accéder via le navigateur de mon ordinateur portable.

![Exemple de cluster Proxmox](https://cdn.hashnode.com/res/hashnode/image/upload/v1759194790299/35e9363f-b739-4085-a589-c1bafbac0504.png align="center")

Nous définissons toutes nos machines virtuelles dans notre fichier `main.tf`. Et nous exécutons une commande simple `terraform apply` pour lancer ces serveurs. Pour en savoir plus sur l'utilisation de Terraform avec Proxmox, je recommande cet [article de blog](https://spacelift.io/blog/terraform-proxmox-provider)

Pour en revenir à notre cas d'utilisation, nous aurons quelques machines virtuelles qui serviront de différents types de serveurs :

1. Un Load balancer
    
2. Un Rate Limiter (un cache Redis)
    
3. Deux serveurs Web
    
4. Une base de données Postgres
    
5. Une machine virtuelle qui testera la charge en simulant des centaines d'appels par minute.
    

Si tout cela semble intimidant, ne vous inquiétez pas trop. Vous n'avez pas besoin de tout configurer pour suivre.

### Rate Limiter centralisé

Comme notre application s'exécutera sur plusieurs serveurs (ou "nœuds"), nous ne pouvons pas stocker le nombre de requêtes en mémoire sur chaque serveur individuel. Pourquoi ? Parce que chaque serveur aurait son propre décompte séparé, et nous n'aurions pas de limite de débit *globale*.

La solution consiste à utiliser un magasin de données centralisé auquel tous nos nœuds d'application peuvent accéder. C'est là qu'intervient Redis.

Voici un diagramme de notre configuration :

![Un petit diagramme illustrant l'architecture que nous allons former avec tous ces nœuds virtuels](https://cdn.hashnode.com/res/hashnode/image/upload/v1758476002871/1d70ce5b-e19c-4d7d-9c0b-cc18840a07bf.png align="center")

1. Les requêtes des utilisateurs frappent d'abord notre Load balancer Nginx.
    
2. Le Load balancer distribue le trafic uniformément entre nos deux VM de serveurs web. La configuration est simple, utilisant un bloc upstream pour définir les serveurs.
    
3. Chaque serveur web exécute notre application Python Flask à l'intérieur d'un conteneur Docker.
    
4. Avant de traiter toute requête, l'application Flask communique avec la VM centrale du Rate Limiter Redis pour vérifier si l'utilisateur a dépassé la limite de débit.
    
5. Si l'utilisateur est dans la limite, l'application traite la requête et interagit avec la base de données PostgreSQL. S'il dépasse la limite, elle renvoie une erreur « 429 Too Many Requests ».
    

Cette architecture garantit que quel que soit le serveur web qui gère la requête, la limite de débit est vérifiée par rapport à la même source de données partagée.

## **Étape 1 : Comment définir l'infrastructure avec Terraform**

Configurer manuellement plusieurs machines virtuelles peut être fastidieux et sujet aux erreurs. C'est pourquoi nous utilisons Terraform, un outil d'Infrastructure as Code (IaC). Il nous permet de définir toute notre infrastructure dans des fichiers de configuration.

**Note** : Vous pouvez ignorer cette section si vous voulez simplement voir le Rate Limiter en action et comment il est utilisé.

Notre fichier [main.tf](https://github.com/sravankaruturi/system-design/blob/main/infra/main.tf) définit tous les composants de notre système. Regardons une pièce maîtresse : la VM Redis.

```yaml
# --- Cache Redis pour le Rate Limiter ---
resource "proxmox_vm_qemu" "redis_cache" {

    vmid        = 130
    name        = "redis-cache-rate-limiter"
    target_node = "pve"
    agent       = 1
    cores       = 1
    memory      = 1024
    # ... config cloud-init ...
    ipconfig0  = "ip=10.0.0.130/24,gw=10.0.0.1"
    # ... config disque et réseau ...

    # 1. Installer Docker
    provisioner "remote-exec" {
        inline = [
            "sleep 30; sudo apt-get update -y",
            "sudo apt-get install -y docker.io docker-compose",
            "sudo mkdir -p /opt/redis"
        ]
    }

    # 2. Télécharger le fichier docker-compose
    provisioner "file" {
         source      = "files/redis-docker-compose.yml"
         destination = "/home/${var.ssh_user}/docker-compose.yml"
    }

    # 3. Déplacer le fichier et lancer docker-compose
    provisioner "remote-exec" {
        inline = [
            "sudo mv /home/${var.ssh_user}/docker-compose.yml /opt/redis/docker-compose.yml",
            "cd /opt/redis && sudo docker-compose up -d"
        ]
    }
}
```

Ce bloc indique à Terraform de créer une `machine virtuelle Proxmox QEMU` avec une adresse IP spécifique `(10.0.0.130)`. Une fois la VM créée, elle utilise des provisionneurs pour se connecter via SSH et exécuter des commandes. Ici, elle installe Docker, télécharge notre fichier `redis-docker-compose.yml` et démarre le conteneur Redis.

Le fichier `redis-docker-compose.yml` lui-même est très simple :

```yaml
version: '3.8'
services:
  redis:
    image: redis:latest
    container_name: redis_cache
    restart: always
    ports:
      - "6379:6379"
    volumes:
      - redisdata:/data

volumes:
  redisdata:
```

Cela garantit que nous avons une instance Redis conteneurisée et persistante prête à servir notre application. La configuration Terraform définit de la même manière nos serveurs web, notre Load balancer et nos bases de données.

## **Étape 2 : Comment implémenter la logique du Rate Limiter en Python**

Passons maintenant au cœur de notre système : le code Python qui implémente la logique de limitation de débit. Nous utilisons un algorithme sophistiqué et économe en mémoire appelé Sliding Window Log.

L'idée est simple : pour chaque utilisateur, nous tenons un journal des horodatages de ses requêtes récentes. Nous stockons ce journal dans un Sorted Set Redis.

Décomposons le code de [`app.py`](https://github.com/sravankaruturi/system-design/blob/main/web-servers/app.py).

### **Le hook Flask** `@app.before_request`

Flask nous permet d'exécuter du code avant que toute requête ne soit traitée par sa fonction de vue destinée. C'est l'endroit idéal pour placer notre Rate Limiter.

```python
import psycopg2
import string
import random
import redis
import time
from flask import Flask, request, redirect, jsonify

app = Flask(__name__)

# --- Détails de connexion à la base de données ---
DB_HOST = "10.0.0.200" 
DB_NAME = "urldb"
DB_USER = "myuser"
DB_PASS = "mypassword"

REDIS_HOST = "10.0.0.130" # IP de votre redis-cache-lxc

# --- Paramètres du Rate Limiter ---
RATE_LIMIT_COUNT = 10  # 10 requêtes
RATE_LIMIT_WINDOW = 60 # par 60 secondes

# Établir une connexion Redis réutilisable
redis_client = redis.Redis(host=REDIS_HOST, port=6379, decode_responses=True)

@app.before_request
def rate_limiter():
    # Utiliser l'adresse IP de l'utilisateur comme clé
    # Dans une application réelle, vous géreriez les proxys via request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    key = f"rate_limit:{request.remote_addr}"
    now = time.time()

    # Utiliser un pipeline Redis pour des opérations atomiques
    pipe = redis_client.pipeline()
    # 1. Ajouter l'horodatage de la requête actuelle. Le score et le membre sont identiques.
    pipe.zadd(key, {str(now): now})
    # 2. Supprimer tous les horodatages plus anciens que notre fenêtre
    pipe.zremrangebyscore(key, 0, now - RATE_LIMIT_WINDOW)
    # 3. Obtenir le nombre d'horodatages restants
    pipe.zcard(key)
    # 4. Définir une expiration sur la clé pour qu'elle se nettoie d'elle-même
    pipe.expire(key, RATE_LIMIT_WINDOW)

    # Exécuter le pipeline et obtenir les résultats
    results = pipe.execute()
    request_count = results[2] # Le résultat de la commande zcard

    if request_count > RATE_LIMIT_COUNT:
        # Renvoyer une erreur 429 Too Many Requests
        return jsonify(error="Rate limit exceeded"), 429

def get_db_connection():
    conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASS)
    return conn

def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS urls (
            id SERIAL PRIMARY KEY,
            short_code VARCHAR(6) UNIQUE NOT NULL,
            original_url TEXT NOT NULL
        );
    ''')
    # Vérifier si l'index existe avant de le créer
    cur.execute('''
        SELECT 1 FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace
        WHERE c.relname = 'idx_original_url' AND n.nspname = 'public';
    ''')
    if cur.fetchone() is None:
        cur.execute('CREATE INDEX idx_original_url ON urls (original_url);')
    conn.commit()
    cur.close()
    conn.close()

def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

@app.route("/", methods=['GET'])
def index():
    return "URL Shortener is running!\n", 200

@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form['url']
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT short_code FROM urls WHERE original_url = %s", (original_url,))
    existing_url = cur.fetchone()

    if existing_url:
        short_code = existing_url[0]
    else:
        short_code = generate_short_code()
        cur.execute("INSERT INTO urls (short_code, original_url) VALUES (%s, %s)", (short_code, original_url))
        conn.commit()

    cur.close()
    conn.close()

    return jsonify(short_url=f"/{short_code}")

@app.route('/<short_code>')
def redirect_to_url(short_code):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT original_url FROM urls WHERE short_code = %s", (short_code,))
    url_record = cur.fetchone()
    cur.close()
    conn.close()

    if url_record:
        return redirect(url_record[0])
    else:
        return "URL not found", 404

if __name__ == '__main__':
    init_db() 
    app.run(host='0.0.0.0', port=5000)
```

### **Comment ça marche, étape par étape**

1. **Identifier l'utilisateur :** Nous créons une clé Redis unique pour chaque utilisateur basée sur son adresse IP : `rate_limit:1.2.3.4`.
    
2. **Utiliser un Pipeline :** La latence réseau peut être un goulot d'étranglement. Un pipeline Redis regroupe plusieurs commandes en un seul cycle requête-réponse. C'est beaucoup plus efficace que de les envoyer une par une. Cela garantit également que la séquence de commandes s'exécute sans être interrompue par des commandes d'autres clients.
    
3. **Enregistrer la requête actuelle (ZADD) :** Nous ajoutons l'horodatage actuel (sous forme d'époque Unix) à un Sorted Set. Nous utilisons l'horodatage à la fois pour le « membre » et le « score », ce qui nous permet de filtrer facilement par temps.
    
4. **Nettoyer les anciennes requêtes (ZREMRANGEBYSCORE) :** C'est la partie « fenêtre glissante ». Nous supprimons tous les horodatages de l'ensemble qui sont plus anciens que notre `RATE_LIMIT_WINDOW` (60 secondes). Cela élimine efficacement les requêtes qui ne sont plus pertinentes pour la période de limite de débit actuelle.
    
5. **Compter les requêtes récentes (ZCARD) :** Nous obtenons la cardinalité (le nombre d'éléments) dans l'ensemble. Après l'étape précédente, ce nombre est notre décompte de requêtes au cours des 60 dernières secondes.
    
6. **Marquer l'enregistrement actuel pour expiration (EXPIRE) :** Nous définissons une expiration sur la clé elle-même. Si un utilisateur arrête de faire des requêtes, Redis supprimera automatiquement ses données de limite de débit après 60 secondes, empêchant la mémoire de se remplir de vieilles clés.
    
7. **Exécuter et vérifier :** La commande `pipe.execute()` envoie toutes nos commandes groupées à Redis. Nous vérifions ensuite le résultat de notre commande ZCARD. Si le décompte dépasse notre `RATE_LIMIT_COUNT`, nous renvoyons immédiatement une erreur 429.
    

Cette approche est incroyablement rapide et efficace. Tout le travail lourd est effectué à l'intérieur de Redis, qui est optimisé pour ce genre d'opérations.

## **Étape 3 : Conteneurisation et tests**

Pour déployer notre application de manière cohérente sur plusieurs VM, nous utilisons Docker. Notre Dockerfile est standard pour une application Python : il part d'une image Python, installe les dépendances de `requirements.txt`, copie le code de l'application et définit la commande pour lancer l'application.

Mais comment savoir si cela fonctionne ? Nous le testons !

Nous utilisons `k6`, un outil de test de charge moderne, pour simuler un trafic intense. Notre script de test, `rate-test.js`, est conçu spécifiquement pour vérifier le Rate Limiter.

```javascript
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    // Monter à 20 utilisateurs. C'est plus que la limite de 10 req/min
    // et cela devrait déclencher le Rate Limiter.
    { duration: '30s', target: 20 },
    { duration: '1m', target: 20 },
    { duration: '10s', target: 0 },
  ],
};

export default function () {
  const url = 'http://10.0.0.100/shorten'; // L'IP du Load Balancer
  const payload = { url: `https://www.test-ratelimit-${Math.random()}.com` };

  const res = http.post(url, payload);

  // Vérifier si la requête a réussi OU si elle a été correctement limitée
  check(res, {
    'status is 200 (OK)': (r) => r.status === 200,
    'status is 429 (Too Many Requests)': (r) => r.status === 429,
  });

  sleep(1);
}
```

Le tableau `stages` configure le test pour augmenter progressivement le nombre d'utilisateurs virtuels jusqu'à 20. Comme notre limite de débit est de 10 requêtes par minute, cette charge est garantie de déclencher le limiteur.

La fonction `check` est la partie cruciale. Elle vérifie que le code de réponse du serveur est soit 200 (signifiant que la requête a réussi), soit 429 (signifiant que notre Rate Limiter a correctement bloqué la requête).

Nous devrions voir environ 10 de nos requêtes passer sur les quelque 1600 requêtes par minute que nous envoyons depuis la même adresse IP.

![Un gif montrant l'exécution du script de test de charge](https://cdn.hashnode.com/res/hashnode/image/upload/v1758477504110/3a2f3f0f-8db0-453d-8900-42a6d0966a11.gif align="center")

Nous pouvons également consulter les journaux sur notre serveur web pour voir toutes les requêtes qui lui ont été envoyées.

![Un petit gif illustrant les journaux du serveur Web](https://cdn.hashnode.com/res/hashnode/image/upload/v1758477959201/80a39d07-1c4e-4d45-8a42-9ac2ce6f360d.gif align="center")

Et si nous regardons le cache/base de données Redis lui-même, nous verrons toutes les clés et le TTL auquel elles expirent.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1758478780827/6a07a2ee-0ad0-4b60-899f-d6a0453edbe7.png align="center")

C'est ainsi que nous limitons le débit des applications en utilisant un serveur de cache Redis.

Voici les fichiers complets utilisés dans le projet.

```yaml
    terraform {
    required_providers {
        proxmox = {
        source  = "telmate/proxmox"
        version = "3.0.2-rc04"
        }
    }
    }

    provider "proxmox" {
    pm_api_url          = var.proxmox_api_url
    pm_api_token_id     = var.proxmox_api_token_id
    pm_api_token_secret = var.proxmox_api_token_secret
    pm_tls_insecure     = true
    }

    # --- Paramètres de connexion partagés pour le provisionneur ---
    locals {
        connection_settings = {
            type        = "ssh"
            user        = var.ssh_user
            private_key = file(var.ssh_private_key_path)
        }
    }

    # --- Conteneurs LXC de base de données ---
    resource "proxmox_lxc" "postgres_db" {
    hostname     = "postgres-db-lxc"
    target_node  = var.target_node
    ostemplate   = var.lxc_template

    rootfs {
        storage = "local-lvm"
        size = "8G"
    }

    password     = "admin"
    unprivileged = true
    start        = true

    features {
        nesting = true
        # keyctl = true
    }

    network {
        name   = "eth0"
        bridge = "vmbr0"
        ip     = "10.0.0.200/24"
        gw     = "10.0.0.1"
    }

    provisioner "remote-exec" {
        connection {
        type        = "ssh"
        user        = var.ssh_user
        private_key = file(var.ssh_private_key_path)
        host        = split("/", self.network[0].ip)[0]
        }
        inline = [
        "sudo apt-get update",
        "sudo apt-get install -y docker.io docker-compose python3-setuptools",
        "sudo usermod -aG docker ${var.ssh_user}",
        "sudo mkdir -p /opt/postgres",
        "sudo chown ${var.ssh_user}:${var.ssh_user} /opt/postgres"
        ]
    }

    provisioner "file" {
        connection {
        type        = "ssh"
        user        = var.ssh_user
        private_key = file(var.ssh_private_key_path)
        host        = split("/", self.network[0].ip)[0]
        }
        source      = "../databases/pg-docker-compose.yml"
        destination = "/opt/postgres/docker-compose.yml"
    }

    provisioner "remote-exec" {
        inline     = ["cd /opt/postgres && sudo docker-compose up -d"]

        connection {
        type        = "ssh"
        user        = var.ssh_user
        private_key = file(var.ssh_private_key_path)
        host        = split("/", self.network[0].ip)[0]
        }
    }
    }

    resource "proxmox_lxc" "mongo_db" {
        hostname    = "mongo-db-lxc"
        target_node = var.target_node
        ostemplate  = var.lxc_template

        rootfs {
            storage = "local-lvm"
            size = "8G"
        }

        password    = "admin"
        unprivileged = true
        start       = true

        features {
            nesting = true
        # keyctl = true # Somehow this is blocking the apply command
        }

        network {
            name   = "eth0"
            bridge = "vmbr0"
            ip     = "10.0.0.210/24"
            gw     = "10.0.0.1"
        }
        
        # Provisionneurs similaires à postgres_db
        provisioner "remote-exec" {
            connection {
                type        = "ssh"
                user        = var.ssh_user
                private_key = file(var.ssh_private_key_path)
                host        = split("/", self.network[0].ip)[0]
            }
            inline = [
            "sudo apt-get update",
            "sudo apt-get install -y docker.io docker-compose python3-setuptools",
            "sudo usermod -aG docker ${var.ssh_user}",
            "sudo mkdir -p /opt/mongo",
            "sudo chown ${var.ssh_user}:${var.ssh_user} /opt/mongo"
            ]
        }

        provisioner "file" {
            connection {
            type        = "ssh"
            user        = var.ssh_user
            private_key = file(var.ssh_private_key_path)
            host        = split("/", self.network[0].ip)[0]
            }
            source      = "../databases/mongo-docker-compose.yml"
            destination = "/opt/mongo/docker-compose.yml"
        }

        provisioner "remote-exec" {
            connection {
            type        = "ssh"
            user        = var.ssh_user
            private_key = file(var.ssh_private_key_path)
            host        = split("/", self.network[0].ip)[0]
            }
            inline     = ["cd /opt/mongo && docker-compose up -d"]
        }
    }

    # --- Cache Redis pour le Rate Limiter ---
    resource "proxmox_vm_qemu" "redis_cache" {

        vmid        = 130
        name        = "redis-cache-rate-limiter"
        target_node = "pve"
        agent       = 1
        cpu {
            cores       = 1
        }
        
        memory      = 1024
        boot        = "order=scsi0" # doit être identique au disque OS du template
        clone       = "debian12-cloudinit" # Le nom du template
        scsihw      = "virtio-scsi-single"
        vm_state    = "running"
        automatic_reboot = true

        # Configuration Cloud-Init
        cicustom   = "vendor=local:snippets/qemu-guest-agent.yml" # /var/lib/vz/snippets/qemu-guest-agent.yml
        ciupgrade  = true
        nameserver = "1.1.1.1 8.8.8.8"
        ipconfig0  = "ip=10.0.0.130/24,gw=10.0.0.1"
        skip_ipv6  = true
        ciuser     = var.ssh_user
        cipassword = var.ssh_password
        sshkeys    = var.ssh_key

        # La plupart des images cloud-init nécessitent un périphérique série pour leur affichage
        serial {
            id = 0
        }

        disks {
            scsi {
            scsi0 {
                # Nous devons spécifier le disque de notre template, sinon Terraform pensera qu'il n'est pas censé être là
                disk {
                storage = "local-lvm"
                # La taille du disque doit être au moins aussi grande que celle du template. Si elle est plus petite, le disque sera recréé
                size    = "5G" 
                }
            }
            }
            ide {
            # Certaines images nécessitent un disque cloud-init sur le contrôleur IDE, d'autres sur SCSI ou SATA
            ide1 {
                cloudinit {
                storage = "local-lvm"
                }
            }
            }
        }

        network {
            id = 0
            bridge = "vmbr0"
            model  = "virtio"
        }

        connection {
            type        = "ssh"
            user        = var.ssh_user
            private_key = file(var.ssh_private_key_path)
            host        = "10.0.0.130"
        }

        # 1. Installer Docker et créer le répertoire final de l'application
        provisioner "remote-exec" {
            inline = [
                # Attendre que cloud-init se termine avant de faire quoi que ce soit d'autre
                "echo 'Waiting for cloud-init to finish...'",
                "while [ ! -f /var/lib/cloud/instance/boot-finished ]; do echo 'Still waiting...' && sleep 1; done",
                "echo 'Cloud-init finished.'",

                # Maintenant, installer les paquets en toute sécurité
                "sudo apt-get update -y",
                "sudo apt-get install -y docker.io docker-compose",
                "sudo mkdir -p /opt/redis",
            ]
        }

        provisioner "file" {
            source      = "../caching/redis-docker-compose.yml"
            destination = "/home/${var.ssh_user}/docker-compose.yml"
        }

        provisioner "remote-exec" {
            inline = [ "sudo mv /home/${var.ssh_user}/docker-compose.yml /opt/redis/docker-compose.yml" ]
        }

        provisioner "remote-exec" {
            inline = [ "cd /opt/redis && sudo docker-compose up -d" ]
        }
    }

    resource "proxmox_vm_qemu" "web-servers" {

        count = 2

        vmid        = count.index + 150
        name        = "web-server-tf-${count.index + 1}"
        target_node = "pve"
        agent       = 1
        cpu {
            cores       = 1
        }
        memory      = 1024
        boot        = "order=scsi0" # doit être identique au disque OS du template
        clone       = "debian12-cloudinit" # Le nom du template
        scsihw      = "virtio-scsi-single"
        vm_state    = "running"
        automatic_reboot = true

        # Configuration Cloud-Init
        cicustom   = "vendor=local:snippets/qemu-guest-agent.yml" # /var/lib/vz/snippets/qemu-guest-agent.yml
        ciupgrade  = true
        nameserver = "1.1.1.1 8.8.8.8"
        ipconfig0  = "ip=10.0.0.${111 + count.index}/24,gw=10.0.0.1"
        skip_ipv6  = true
        ciuser     = var.ssh_user
        cipassword = var.ssh_password
        sshkeys    = var.ssh_key

        # La plupart des images cloud-init nécessitent un périphérique série pour leur affichage
        serial {
            id = 0
        }

        disks {
            scsi {
            scsi0 {
                # Nous devons spécifier le disque de notre template, sinon Terraform pensera qu'il n'est pas censé être là
                disk {
                storage = "local-lvm"
                # La taille du disque doit être au moins aussi grande que celle du template. Si elle est plus petite, le disque sera recréé
                size    = "5G" 
                }
            }
            }
            ide {
            # Certaines images nécessitent un disque cloud-init sur le contrôleur IDE, d'autres sur SCSI ou SATA
            ide1 {
                cloudinit {
                storage = "local-lvm"
                }
            }
            }
        }

        network {
            id = 0
            bridge = "vmbr0"
            model  = "virtio"
        }

        connection {
            type        = "ssh"
            user        = var.ssh_user
            private_key = file(var.ssh_private_key_path)
            host        = "10.0.0.${111 + count.index}"
        }

        # 1. Installer Docker et créer le répertoire final de l'application
        provisioner "remote-exec" {
            inline = [
                # Attendre que cloud-init se termine avant de faire quoi que ce soit d'autre
                "echo 'Waiting for cloud-init to finish...'",
                "while [ ! -f /var/lib/cloud/instance/boot-finished ]; do echo 'Still waiting...' && sleep 1; done",
                "echo 'Cloud-init finished.'",

                # Maintenant, installer les paquets en toute sécurité
                "sudo apt-get update -y",
                "sudo apt-get install -y docker.io",
                "sudo mkdir -p /opt/app",
            ]
        }

        # 2. Télécharger UNIQUEMENT les fichiers nécessaires dans le répertoire personnel de l'utilisateur
        provisioner "file" {
            source      = "../web-servers/app.py"
            destination = "/home/${var.ssh_user}/app.py"
        }
        provisioner "file" {
            source      = "../web-servers/Dockerfile"
            destination = "/home/${var.ssh_user}/Dockerfile"
        }
        provisioner "file" {
            source      = "../web-servers/requirements.txt"
            destination = "/home/${var.ssh_user}/requirements.txt"
        }

        # 4. Déplacer les fichiers, construire l'image et lancer le conteneur
        provisioner "remote-exec" {
            inline = [
                # Déplacer chaque fichier individuellement pour être compatible avec tous les shells
                "sudo mv /home/${var.ssh_user}/app.py /opt/app/",
                "sudo mv /home/${var.ssh_user}/Dockerfile /opt/app/",
                "sudo mv /home/${var.ssh_user}/requirements.txt /opt/app/",

                # Construire l'image Docker
                "sudo docker build -t my-python-app /opt/app",
                
                # Arrêter et supprimer les anciens conteneurs pour éviter les conflits
                "sudo docker stop $(sudo docker ps -q --filter ancestor=my-python-app) 2>/dev/null || true",
                "sudo docker rm $(sudo docker ps -aq --filter ancestor=my-python-app) 2>/dev/null || true",

                # Lancer le nouveau conteneur
                "sudo docker run -d --restart always -p 80:5000 my-python-app"
            ]
        }

        # Dans votre ressource proxmox_vm_qemu "web_servers"
        depends_on = [
            proxmox_lxc.postgres_db,
            proxmox_vm_qemu.redis_cache
        ]
    }

    # --- VM Load Balancer ---
    resource "proxmox_vm_qemu" "load_balancer" {
        name        = "lb-1"
        target_node = var.target_node
        clone       = var.vm_template
        agent       = 1
        cpu {
            cores       = 1
        }
        memory      = 512
        boot        = "order=scsi0" # doit être identique au disque OS du template
        scsihw      = "virtio-scsi-single"
        vm_state    = "running"
        automatic_reboot = true

        # --- Ajouter ces lignes pour le lecteur Cloud Init ---
        cicustom   = "vendor=local:snippets/qemu-guest-agent.yml" # /var/lib/vz/snippets/qemu-guest-agent.yml
        ciupgrade  = true
        nameserver = "1.1.1.1 8.8.8.8"
        ipconfig0  = "ip=10.0.0.100/24,gw=10.0.0.1"
        skip_ipv6  = true
        ciuser     = var.ssh_user
        cipassword = var.ssh_password
        sshkeys    = var.ssh_key
        
        # La plupart des images cloud-init nécessitent un périphérique série pour leur affichage
        serial {
            id = 0
        }

        disks {
            scsi {
            scsi0 {
                # Nous devons spécifier le disque de notre template, sinon Terraform pensera qu'il n'est pas censé être là
                disk {
                storage = "local-lvm"
                # La taille du disque doit être au moins aussi grande que celle du template. Si elle est plus petite, le disque sera recréé
                size    = "5G" 
                }
            }
            }
            ide {
            # Certaines images nécessitent un disque cloud-init sur le contrôleur IDE, d'autres sur SCSI ou SATA
            ide1 {
                cloudinit {
                storage = "local-lvm"
                }
            }
            }
        }

        network {
            id = 0
            bridge = "vmbr0"
            model  = "virtio"
        }

        connection {
            type        = "ssh"
            user        = var.ssh_user
            private_key = file(var.ssh_private_key_path)
            host        = "10.0.0.100"
        }

        # Étape 1 : Installer Nginx
        provisioner "remote-exec" {
            inline = [
                # Attendre que cloud-init se termine avant de faire quoi que ce soit d'autre
                "echo 'Waiting for cloud-init to finish...'",
                "while [ ! -f /var/lib/cloud/instance/boot-finished ]; do echo 'Still waiting...' && sleep 1; done",
                "echo 'Cloud-init finished.'",

                # Maintenant, installer les paquets en toute sécurité
                "sudo apt-get update -y",
                "sudo apt-get install -y nginx"
            ]
        }

        # Étape 2 : Télécharger la configuration vers un emplacement temporaire
        provisioner "file" {
            source      = "../web-servers/nginx.conf"
            destination = "/tmp/nginx.conf" # Utiliser /tmp à la place
        }

        # Étape 3 : Utiliser sudo pour déplacer le fichier vers sa destination finale et recharger nginx
        provisioner "remote-exec" {
            inline = [
                "sudo mv /tmp/nginx.conf /etc/nginx/sites-available/default",
                "sudo systemctl reload nginx"
            ]
        }
    }


    # --- VM Load Tester ---
    resource "proxmox_vm_qemu" "load_tester" {
        name        = "load-tester-vm"
        target_node = var.target_node
        clone       = var.vm_template
        agent       = 1
        cpu {
            cores       = 1
        }
        memory      = 1024
        boot        = "order=scsi0" # doit être identique au disque OS du template
        scsihw      = "virtio-scsi-single"
        vm_state    = "running"
        automatic_reboot = true

        # --- Ajouter ces lignes pour le lecteur Cloud Init ---
        cicustom   = "vendor=local:snippets/qemu-guest-agent.yml" # /var/lib/vz/snippets/qemu-guest-agent.yml
        ciupgrade  = true
        nameserver = "1.1.1.1 8.8.8.8"
        ipconfig0  = "ip=10.0.0.160/24,gw=10.0.0.1"
        skip_ipv6  = true
        ciuser     = var.ssh_user
        cipassword = var.ssh_password
        sshkeys    = var.ssh_key

        # La plupart des images cloud-init nécessitent un périphérique série pour leur affichage
        serial {
            id = 0
        }

        disks {
            scsi {
                scsi0 {
                    # Nous devons spécifier le disque de notre template, sinon Terraform pensera qu'il n'est pas censé être là
                    disk {
                    storage = "local-lvm"
                    # La taille du disque doit être au moins aussi grande que celle du template. Si elle est plus petite, le disque sera recréé
                    size    = "5G" 
                    }
                }
            }

            ide {
            # Certaines images nécessitent un disque cloud-init sur le contrôleur IDE, d'autres sur SCSI ou SATA
                ide1 {
                    cloudinit {
                    storage = "local-lvm"
                    }
                }
            }
        }

        network {
            id = 0
            bridge = "vmbr0"
            model  = "virtio"
        }

        provisioner "remote-exec" {
            connection {
                type        = "ssh"
                user        = var.ssh_user
                private_key = file(var.ssh_private_key_path)
                host        = "10.0.0.160"
            }
            inline = [
                # Attendre que cloud-init se termine
                "echo 'Waiting for cloud-init to finish...'",
                "while [ ! -f /var/lib/cloud/instance/boot-finished ]; do echo 'Still waiting...' && sleep 1; done",
                "echo 'Cloud-init finished.'",

                # Installer les prérequis
                "sudo apt-get update -y",
                "sudo apt-get install -y gnupg curl",

                # Ajouter le dépôt k6 et la clé
                "curl -sL https://dl.k6.io/key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/k6-archive-keyring.gpg",
                "echo 'deb [signed-by=/usr/share/keyrings/k6-archive-keyring.gpg] https://dl.k6.io/deb stable main' | sudo tee /etc/apt/sources.list.d/k6.list",

                # Installer k6
                "sudo apt-get update",
                "sudo apt-get install -y k6"
            ]
        }

        provisioner "file" {
            connection {
            type        = "ssh"
            user        = var.ssh_user
            private_key = file(var.ssh_private_key_path)
            host        = "10.0.0.160"
            }
            source      = "../load-testing/script.js"
            destination = "/home/${var.ssh_user}/script.js"
        }

        provisioner "file" {
            connection {
            type        = "ssh"
            user        = var.ssh_user
            private_key = file(var.ssh_private_key_path)
            host        = "10.0.0.160"
            }
            source      = "../load-testing/rate-test.js"
            destination = "/home/${var.ssh_user}/rate-test.js"
        }

    }
```

## **Conclusion**

Vous avez maintenant vu comment construire un système complet, évolutif et résilient qui inclut un composant crucial pour les applications web modernes : un Rate Limiter distribué.

Nous avons couvert l'ensemble de la pile :

* **Infrastructure as Code** avec Terraform pour définir nos machines virtuelles. (consultez mon dépôt [ici](https://github.com/sravankaruturi/system-design) pour tout le code et les mises à jour que j'y apporte).
    
* Un **cache centralisé à haute vitesse** avec Redis pour stocker nos données de limitation de débit.
    
* Un algorithme efficace de **Sliding Window Log** implémenté en Python avec Flask.
    
* La **Conteneurisation** avec Docker pour un déploiement cohérent.
    
* L'**Équilibrage de charge** avec Nginx pour distribuer le trafic.
    
* Les **Tests de charge** avec k6 pour valider notre implémentation.
    

Si vous souhaitez en savoir plus sur les concepts utilisés lors de la construction de systèmes à grande échelle, n'hésitez pas à me suivre sur @[Sravan Karuturi](@sravankaruturi).