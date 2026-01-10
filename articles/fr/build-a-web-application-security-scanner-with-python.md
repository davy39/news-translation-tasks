---
title: 'Création d''un scanner de sécurité d''applications web simple avec Python
  : Un guide pour débutants'
subtitle: ''
author: Chaitanya Rahalkar
co_authors: []
series: null
date: '2024-12-12T15:38:02.640Z'
originalURL: https://freecodecamp.org/news/build-a-web-application-security-scanner-with-python
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1733929791562/042042e3-56e2-4185-be19-2a0f5fa15d25.png
tags:
- name: Python
  slug: python
- name: python projects
  slug: python-projects
- name: Security
  slug: security
- name: '#cybersecurity'
  slug: cybersecurity-1
seo_title: 'Création d''un scanner de sécurité d''applications web simple avec Python
  : Un guide pour débutants'
seo_desc: 'In this article, you are going to learn to create a basic security tool
  that can be helpful in identifying common vulnerabilities in web applications.

  I have two goals here. The first is to empower you with the skills to develop tools
  that can help e...'
---

Dans cet article, vous allez apprendre à créer un outil de sécurité de base qui peut être utile pour identifier les vulnérabilités courantes dans les applications web.

J'ai deux objectifs ici. Le premier est de vous donner les compétences nécessaires pour développer des outils qui peuvent aider à améliorer la posture de sécurité globale de vos sites web. Le second est de vous aider à pratiquer un peu de programmation Python.

Dans ce guide, vous allez construire un scanner de sécurité basé sur Python qui peut détecter les attaques XSS, les injections SQL et les informations personnelles sensibles (PII - Personally Identifiable Information).

### Types de vulnérabilités

Généralement, nous pouvons catégoriser les vulnérabilités de sécurité web dans les catégories suivantes (pour encore plus de catégories, consultez le [OWASP Top 10](https://owasp.org/www-project-top-ten/)) :

* **Injection SQL** : Une technique où les attaquants sont capables d'insérer du code SQL malveillant dans des requêtes SQL via des entrées non validées, leur permettant de modifier/lire le contenu de la base de données.

* **Cross-Site Scripting (XSS)** : Une technique où les attaquants injectent du JavaScript malveillant dans des sites web de confiance. Cela leur permet d'exécuter le code JavaScript dans le contexte du navigateur et de voler des informations sensibles ou d'effectuer des opérations non autorisées.

* **Exposition d'informations sensibles** : Un problème de sécurité où une application révèle involontairement des données sensibles comme des mots de passe, des clés API, etc., via des logs, un stockage non sécurisé et d'autres vulnérabilités.

* **Mauvaises configurations de sécurité courantes** : Des problèmes de sécurité qui surviennent en raison d'une configuration incorrecte des serveurs web - comme des identifiants par défaut pour les comptes administrateur, un mode de débogage activé, des tableaux de bord administrateur publics avec des identifiants faibles, etc.

* **Faiblesses d'authentification de base** : Des problèmes de sécurité qui surviennent en raison de lacunes dans les politiques de mots de passe, les processus d'authentification des utilisateurs, une gestion incorrecte des sessions, etc.

## Table des matières

* [Prérequis](#heading-prerequis)

* [Configuration de notre environnement de développement](#heading-installation-de-notre-environnement-de-developpement)

* [Construction de notre classe de scanner principale](#heading-construction-de-notre-classe-de-scanner-principale)

* [Implémentation du crawler](#heading-implementation-du-crawler)

* [Conception et implémentation des vérifications de sécurité](#heading-conception-et-implementation-des-verifications-de-securite)

  * [Vérification de la détection d'injection SQL](#heading-verification-de-la-detection-dinjection-sql)

  * [Vérification XSS (Cross-Site Scripting)](#heading-verification-xss-cross-site-scripting)

  * [Vérification de l'exposition d'informations sensibles](#heading-verification-de-lexposition-dinformations-sensibles)

* [Implémentation de la logique principale de scan](#heading-implementation-de-la-logique-principale-de-scan)

* [Extension du scanner de sécurité](#heading-extension-du-scanner-de-securite)

* [Conclusion](#heading-conclusion)

## Prérequis

Pour suivre ce tutoriel, vous aurez besoin de :

* Python 3.x

* Une compréhension de base des protocoles HTTP

* Une compréhension de base des applications web

* Une compréhension de base du fonctionnement des attaques XSS, des injections SQL et des attaques de sécurité de base

## Configuration de notre environnement de développement

Installons nos dépendances requises avec la commande suivante :

```bash
pip install requests beautifulsoup4 urllib3 colorama
```

Nous utiliserons ces dépendances dans notre fichier de code :

```python
# Packages requis
import requests
from bs4 import BeautifulSoup
import urllib.parse
import colorama
import re
from concurrent.futures import ThreadPoolExecutor
import sys
from typing import List, Dict, Set
```

## Construction de notre classe de scanner principale

Une fois que vous avez les dépendances, il est temps d'écrire la classe principale du scanner.

Cette classe servira de classe principale qui gérera la fonctionnalité de scan de sécurité web. Elle suivra nos pages visitées et stockera également nos résultats.

Nous avons la fonction `normalize_url` que nous utiliserons pour nous assurer que vous ne rescannez pas les URL déjà vues auparavant. Cette fonction supprimera essentiellement les paramètres HTTP GET de l'URL. Par exemple, `https://example.com/page?id=1` deviendra `https://example.com/page` après normalisation.

```python
class WebSecurityScanner:
    def __init__(self, target_url: str, max_depth: int = 3):
        """
        Initialiser le scanner de sécurité avec une URL cible et une profondeur de crawl maximale.
        
        Args:
            target_url: L'URL de base à scanner
            max_depth: Profondeur maximale pour le crawl des liens (par défaut : 3)
        """
        self.target_url = target_url
        self.max_depth = max_depth
        self.visited_urls: Set[str] = set()
        self.vulnerabilities: List[Dict] = []
        self.session = requests.Session()
        
        # Initialiser colorama pour une sortie colorée multiplateforme
        colorama.init()
    
    def normalize_url(self, url: str) -> str:
        """Normaliser l'URL pour éviter les vérifications en double"""
        parsed = urllib.parse.urlparse(url)
        return f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
```

## Implémentation du crawler

La première étape de notre scanner est d'implémenter un crawler web qui découvrira les pages et les URL dans une application cible donnée. Assurez-vous d'écrire ces fonctions dans notre classe `WebSecurityScanner`.

```python
def crawl(self, url: str, depth: int = 0) -> None:
    """
    Crawler le site web pour découvrir les pages et les endpoints.
    
    Args:
        url: URL actuelle à crawler
        depth: Profondeur actuelle dans l'arbre de crawl
    """
    if depth > self.max_depth or url in self.visited_urls:
        return
        
    try:
        self.visited_urls.add(url)
        response = self.session.get(url, verify=False)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Trouver tous les liens dans la page
        links = soup.find_all('a', href=True)
        for link in links:
            next_url = urllib.parse.urljoin(url, link['href'])
            if next_url.startswith(self.target_url):
                self.crawl(next_url, depth + 1)
                
    except Exception as e:
        print(f"Erreur lors du crawl de {url}: {str(e)}")
```

Cette fonction `crawl` nous aide à effectuer un crawl en profondeur d'un site web. Elle explorera toutes les pages d'un site web tout en restant dans le domaine spécifié.

Par exemple, si vous prévoyez d'utiliser ce scanner sur `https://google.com`, la fonction obtiendra d'abord toutes les URL puis vérifiera une par une si elles appartiennent au domaine spécifié (c'est-à-dire `google.com`). Si c'est le cas, elle continuera récursivement à scanner l'URL vue jusqu'à une profondeur spécifiée qui est fournie avec le paramètre `depth` en tant qu'argument de la fonction. Nous avons également une gestion des exceptions pour nous assurer de gérer les erreurs en douceur et de signaler toute erreur lors du crawl.

## Conception et implémentation des vérifications de sécurité

Maintenant, passons enfin à la partie intéressante et implémentons nos vérifications de sécurité. Nous commencerons d'abord par l'injection SQL.

### Vérification de la détection d'injection SQL

```python
def check_sql_injection(self, url: str) -> None:
    """Tester les vulnérabilités potentielles d'injection SQL"""
    sql_payloads = ["'", "1' OR '1'='1", "' OR 1=1--", "' UNION SELECT NULL--"]
    
    for payload in sql_payloads:
        try:
            # Tester les paramètres GET
            parsed = urllib.parse.urlparse(url)
            params = urllib.parse.parse_qs(parsed.query)
            
            for param in params:
                test_url = url.replace(f"{param}={params[param][0]}", 
                                     f"{param}={payload}")
                response = self.session.get(test_url)
                
                # Rechercher les messages d'erreur SQL
                if any(error in response.text.lower() for error in 
                    ['sql', 'mysql', 'sqlite', 'postgresql', 'oracle']):
                    self.report_vulnerability({
                        'type': 'SQL Injection',
                        'url': url,
                        'parameter': param,
                        'payload': payload
                    })
                    
        except Exception as e:
            print(f"Erreur lors du test d'injection SQL sur {url}: {str(e)}")
```

Cette fonction effectue essentiellement des vérifications de base d'injection SQL en testant l'URL contre des payloads d'injection SQL courants et en recherchant des messages d'erreur qui pourraient indiquer une vulnérabilité de sécurité.

Sur la base du message d'erreur reçu après avoir effectué une simple requête GET sur l'URL, nous vérifions si ce message est une erreur de base de données ou non. Si c'est le cas, nous utilisons la fonction `report_vulnerability` pour signaler cela comme un problème de sécurité dans notre rapport final que ce script générera. Pour l'exemple, nous sélectionnons quelques payloads d'injection SQL couramment testés, mais vous pouvez étendre cela pour en tester encore plus.

### Vérification XSS (Cross-Site Scripting)

Maintenant, implémentons la deuxième vérification de sécurité pour les payloads XSS.

```python
def check_xss(self, url: str) -> None:
    """Tester les vulnérabilités potentielles de Cross-Site Scripting"""
    xss_payloads = [
        "<script>alert('XSS')</script>",
        "<img src=x onerror=alert('XSS')>",
        "javascript:alert('XSS')"
    ]
    
    for payload in xss_payloads:
        try:
            # Tester les paramètres GET
            parsed = urllib.parse.urlparse(url)
            params = urllib.parse.parse_qs(parsed.query)
            
            for param in params:
                test_url = url.replace(f"{param}={params[param][0]}", 
                                     f"{param}={urllib.parse.quote(payload)}")
                response = self.session.get(test_url)
                
                if payload in response.text:
                    self.report_vulnerability({
                        'type': 'Cross-Site Scripting (XSS)',
                        'url': url,
                        'parameter': param,
                        'payload': payload
                    })
                    
        except Exception as e:
            print(f"Erreur lors du test XSS sur {url}: {str(e)}")
```

Cette fonction, comme le testeur d'injection SQL, utilise un ensemble de payloads XSS courants et applique la même idée. Mais la différence clé ici est que nous recherchons notre payload injecté pour apparaître inchangé dans notre réponse plutôt que de rechercher un message d'erreur.

Si vous êtes capable de voir notre payload injecté, il sera probablement exécuté dans le contexte du navigateur de la victime en tant qu'attaque XSS réfléchie.

### Vérification de l'exposition d'informations sensibles

Maintenant, implémentons notre dernière vérification pour les PII sensibles.

```python
def check_sensitive_info(self, url: str) -> None:
    """Vérifier les informations sensibles exposées"""
    sensitive_patterns = {
        'email': r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
        'phone': r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',
        'ssn': r'\b\d{3}-\d{2}-\d{4}\b',
        'api_key': r'api[_-]?key[_-]?([\'"|`])([a-zA-Z0-9]{32,45})\1'
    }
    
    try:
        response = self.session.get(url)
        
        for info_type, pattern in sensitive_patterns.items():
            matches = re.finditer(pattern, response.text)
            for match in matches:
                self.report_vulnerability({
                    'type': 'Sensitive Information Exposure',
                    'url': url,
                    'info_type': info_type,
                    'pattern': pattern
                })
                
    except Exception as e:
        print(f"Erreur lors de la vérification des informations sensibles sur {url}: {str(e)}")
```

Cette fonction utilise un ensemble de motifs Regex prédéfinis pour rechercher des PII comme des emails, des numéros de téléphone, des SSN et des clés API (qui sont préfixées avec api-key-<number>).

Comme les deux fonctions précédentes, nous utilisons le texte de réponse pour l'URL et nos motifs Regex pour trouver ces PII dans le texte de réponse. Si nous en trouvons, nous les signalons avec la fonction `report_vulnerability`. Assurez-vous d'avoir toutes ces fonctions définies dans la classe `WebSecurityScanner`.

## Implémentation de la logique principale de scan

Assemblons enfin tout cela en définissant les fonctions `scan` et `report_vulnerability` dans la classe `WebSecurityScanner` :

```python
def scan(self) -> List[Dict]:
    """
    Méthode principale de scan qui coordonne les vérifications de sécurité
    
    Returns:
        Liste des vulnérabilités découvertes
    """
    print(f"\n{colorama.Fore.BLUE}Début du scan de sécurité de {self.target_url}{colorama.Style.RESET_ALL}\n")
    
    # D'abord, crawler le site web
    self.crawl(self.target_url)
    
    # Ensuite, exécuter les vérifications de sécurité sur toutes les URL découvertes
    with ThreadPoolExecutor(max_workers=5) as executor:
        for url in self.visited_urls:
            executor.submit(self.check_sql_injection, url)
            executor.submit(self.check_xss, url)
            executor.submit(self.check_sensitive_info, url)
    
    return self.vulnerabilities

def report_vulnerability(self, vulnerability: Dict) -> None:
    """Enregistrer et afficher les vulnérabilités trouvées"""
    self.vulnerabilities.append(vulnerability)
    print(f"{colorama.Fore.RED}[VULNÉRABILITÉ TROUVÉE]{colorama.Style.RESET_ALL}")
    for key, value in vulnerability.items():
        print(f"{key}: {value}")
    print()
```

Ce code définit notre fonction `scan` qui invoquera essentiellement la fonction `crawl` et commencera récursivement à crawler le site web. Avec le multithreading, nous appliquerons les trois vérifications de sécurité sur les URL visitées.

Nous avons également défini la fonction `report_vulnerability` qui imprimera effectivement notre vulnérabilité sur la console et les stockera également dans notre tableau `vulnerabilities`.

Maintenant, utilisons enfin notre scanner en l'enregistrant sous `scanner.py` :

```python
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scanner.py <target_url>")
        sys.exit(1)
        
    target_url = sys.argv[1]
    scanner = WebSecurityScanner(target_url)
    vulnerabilities = scanner.scan()
    
    # Imprimer le résumé
    print(f"\n{colorama.Fore.GREEN}Scan terminé !{colorama.Style.RESET_ALL}")
    print(f"Nombre total d'URL scannées : {len(scanner.visited_urls)}")
    print(f"Vulnérabilités trouvées : {len(vulnerabilities)}")
```

L'URL cible sera fournie en tant qu'argument système et nous obtiendrons le résumé des URL scannées et des vulnérabilités trouvées à la fin de notre scan. Maintenant, discutons de la manière dont vous pouvez étendre le scanner et ajouter plus de fonctionnalités.

## Extension du scanner de sécurité

Voici quelques idées pour étendre ce scanner de sécurité de base en quelque chose de plus avancé :

1. Ajouter plus de vérifications de vulnérabilités comme la détection CSRF, le traversal de répertoires, etc.

2. Améliorer les rapports avec une sortie HTML ou PDF.

3. Ajouter des options de configuration pour l'intensité du scan et la portée de la recherche (spécifier la profondeur des scans via un argument CLI).

4. Implémenter une limitation de débit appropriée.

5. Ajouter une prise en charge de l'authentification pour tester les URL qui nécessitent une authentification basée sur une session.

## Conclusion

Maintenant, vous savez comment construire un scanner de sécurité de base ! Ce scanner démontre quelques concepts de base de la sécurité web.

Gardez à l'esprit que ce tutoriel ne doit être utilisé qu'à des fins éducatives. Il existe plusieurs applications professionnelles de qualité entreprise comme Burp Suite et OWASP Zap qui peuvent vérifier des centaines de vulnérabilités de sécurité à une échelle beaucoup plus grande.

J'espère que vous avez appris les bases de la sécurité web et un peu de programmation Python également.