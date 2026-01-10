---
title: Comment effectuer un hachage sécurisé avec le module hashlib de Python
author: Bala Priya C
date: '2025-12-15T22:56:01.475Z'
originalURL: https://freecodecamp.org/news/how-to-perform-secure-hashing-using-pythons-hashlib-module
description: 'Le hachage est une technique fondamentale en programmation qui convertit
  les données en une chaîne de caractères de taille fixe. Contrairement au chiffrement,
  le hachage est un processus à sens unique : vous ne pouvez pas l''inverser pour
  récupérer les données d''origine.

  Cela rend le hachage parfait pour stocker des p...'
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1765839274048/2110b9d7-00c4-4e85-a69b-7223f21f2ac3.png
tags:
- name: Python
  slug: python
- name: Hashing
  slug: hashing
- name: Security
  slug: security
seo_desc: 'Hashing is a fundamental technique in programming that converts data into
  a fixed-size string of characters. Unlike encryption, hashing is a one-way process:
  you can''t reverse it to get the original data back.

  This makes hashing perfect for storing p...'
---


Le hachage est une technique fondamentale en programmation qui convertit les données en une chaîne de caractères de taille fixe. Contrairement au chiffrement, le hachage est un processus à sens unique : vous ne pouvez pas l'inverser pour récupérer les données d'origine.

Cela rend le hachage parfait pour stocker des mots de passe, vérifier l'intégrité des fichiers et créer des identifiants uniques. Dans ce tutoriel, vous apprendrez à utiliser le [module `hashlib` intégré de Python](https://docs.python.org/3/library/hashlib.html) pour implémenter un hachage sécurisé dans vos applications.

À la fin de ce tutoriel, vous comprendrez :

* Comment créer des hachages de base avec différents algorithmes
    
* Pourquoi le hachage simple ne suffit pas pour les mots de passe
    
* Comment ajouter du sel (*salt*) pour prévenir les attaques par tables arc-en-ciel (*rainbow tables*)
    
* Comment utiliser les fonctions de dérivation de clé pour le stockage des mots de passe
    

[Vous pouvez trouver le code sur GitHub](https://github.com/balapriyac/python-basics/tree/main/secure-hashing).

## Prerequisites

Pour suivre ce tutoriel, vous devriez avoir :

* **Bases de Python** : Variables, types de données, fonctions et structures de contrôle
    
* **Compréhension des chaînes de caractères et des octets** : Comment encoder des chaînes et travailler avec des données de type `bytes`
    

Aucune bibliothèque externe n'est requise, car [hashlib](https://docs.python.org/3/library/hashlib.html) et [os](https://docs.python.org/3/library/os.html) font tous deux partie de la bibliothèque standard de Python.

## Table of Contents

1. [Hachage de base avec le hashlib de Python](#heading-hachage-de-base-avec-le-hashlib-de-python)
    
2. [Pourquoi le hachage simple ne suffit pas pour les mots de passe](#heading-pourquoi-le-hachage-simple-ne-suffit-pas-pour-les-mots-de-passe)
    
3. [Ajouter du sel à vos hachages](#heading-ajouter-du-sel-a-vos-hachages)
    
4. [Vérifier les mots de passe salés](#heading-verifier-les-mots-de-passe-sales)
    
5. [Utiliser des fonctions de dérivation de clé](#heading-utiliser-des-fonctions-de-derivation-de-cle)
    

## Basic Hashing with Python’s hashlib

Commençons par les fondamentaux. Le module `hashlib` permet d'accéder à plusieurs algorithmes de hachage comme [MD5](https://www.md5hashgenerator.com/), [SHA-1](https://en.wikipedia.org/wiki/SHA-1), [SHA-256](https://emn178.github.io/online-tools/sha256.html), et plus encore.

Voici comment créer un hachage SHA-256 simple :

```python
import hashlib

# Create a simple hash
message = "Hello, World!"
hash_object = hashlib.sha256(message.encode())
hex_digest = hash_object.hexdigest()

print(f"Original: {message}")
print(f"SHA-256 Hash: {hex_digest}")
```

Sortie :

```plaintext
Original: Hello, World!
SHA-256 Hash: dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f
```

Ici, nous importons le module `hashlib`, encodons notre chaîne en octets à l'aide de `.encode()` car `hashlib` nécessite des octets et non des chaînes de caractères.

Ensuite, nous créons un objet de hachage en utilisant `hashlib.sha256()` et obtenons la représentation hexadécimale avec `.hexdigest()`.

Le hachage résultant fait toujours 64 caractères de long, quelle que soit la taille de l'entrée. Cela signifie que vous avez une chaîne de sortie de **256 bits**. Comme chaque caractère hexadécimal nécessite 4 bits, **la sortie comporte 256/4 = 64 caractères hexadécimaux**. Même le changement d'un seul caractère produit un hachage complètement différent.

Vérifions cela :

```python
import hashlib

# Small change, big difference
message1 = "Hello, World!"
message2 = "Hello, World?"  # Only changed ! to ?

hash1 = hashlib.sha256(message1.encode()).hexdigest()
hash2 = hashlib.sha256(message2.encode()).hexdigest()

print(f"Message 1: {message1}")
print(f"Hash 1:    {hash1}")
print(f"\nMessage 2: {message2}")
print(f"Hash 2:    {hash2}")
print(f"\nAre they the same? {hash1 == hash2}")
```

Sortie :

```plaintext
Message 1: Hello, World!
Hash 1:    dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f

Message 2: Hello, World?
Hash 2:    f16c3bb0532537acd5b2e418f2b1235b29181e35cffee7cc29d84de4a1d62e4d

Are they the same? False
```

Cette propriété est appelée l'[effet d'avalanche](https://fr.wikipedia.org/wiki/Effet_d%27avalanche) où un changement minime crée une sortie complètement différente.

## Why Simple Hashing Isn't Enough for Passwords

Vous pourriez penser qu'il suffit de hacher les mots de passe et de les stocker dans votre base de données. Mais il y a un problème : les attaquants utilisent des [tables arc-en-ciel](https://fr.wikipedia.org/wiki/Table_arc-en-ciel), qui sont des bases de données précalculées de hachages pour les mots de passe courants.

Voici ce qui se passe :

```python
import hashlib

# Simple password hashing (DON'T USE THIS!)
password = "password123"
hashed = hashlib.sha256(password.encode()).hexdigest()

print(f"Password: {password}")
print(f"Hash: {hashed}")
```

Sortie :

```plaintext
Password: password123
Hash: ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f
```

Si deux utilisateurs ont le même mot de passe, ils auront des hachages identiques. Un attaquant qui casse un hachage connaît le mot de passe de tous les utilisateurs ayant ce hachage.

Alors, comment gérer cela ? Apprenons-le dans la section suivante.

## Adding Salt to Your Hashes

La solution est le **salage** (*salting*) : ajouter des données aléatoires à chaque mot de passe avant le hachage. De cette façon, même des mots de passe identiques produisent des hachages différents.

Voici comment implémenter le hachage salé :

```python
import hashlib
import os

def hash_password_with_salt(password):
    # Generate a random salt (16 bytes = 128 bits)
    salt = os.urandom(16)
    
    # Combine password and salt, then hash
    hash_object = hashlib.sha256(salt + password.encode())
    password_hash = hash_object.hexdigest()
    
    # Return both salt and hash (you need the salt to verify later)
    return salt.hex(), password_hash

# Hash the same password twice
password = "password123"

salt1, hash1 = hash_password_with_salt(password)
salt2, hash2 = hash_password_with_salt(password)

print(f"Password: {password}\n")
print(f"First attempt:")
print(f"  Salt: {salt1}")
print(f"  Hash: {hash1}\n")
print(f"Second attempt:")
print(f"  Salt: {salt2}")
print(f"  Hash: {hash2}\n")
print(f"Same password, different hashes? {hash1 != hash2}")
```

Sortie :

```plaintext
Password: password123

First attempt:
  Salt: fc24b2d2245ff65b80c5bced38744171
  Hash: 5ce634c05941d25871e7ee334b5c24c75f64c4f6d557db66909fcaa793d869f9

Second attempt:
  Salt: bc8a1f79b07e56b51285557211f88bb0
  Hash: 043599d90b2aa0556265869cead35724c7d9d9d37129d897c6b68bade9e737e6

Same password, different hashes? True
```

Comment cela fonctionne :

* `os.urandom(16)` génère 16 octets aléatoires, ce qui constitue notre sel.
    
* Nous concaténons le sel et les octets du mot de passe avant le hachage.
    
* Nous retournons à la fois le sel (en `hex`) et le hachage.
    
* Vous devez stocker à la fois le sel et le hachage dans votre base de données.
    

Lorsqu'un utilisateur se connecte, vous récupérez son sel, hachez le mot de passe saisi avec ce sel, et comparez le résultat au hachage stocké.

## Verifying Salted Passwords

Créons maintenant une fonction pour vérifier les mots de passe par rapport aux hachages salés :

```python
import hashlib
import os

def hash_password(password, salt=None):
    """Hash a password with a salt. Generate new salt if not provided."""
    if salt is None:
        salt = os.urandom(16)
    else:
        # Convert hex string back to bytes if needed
        if isinstance(salt, str):
            salt = bytes.fromhex(salt)
    
    password_hash = hashlib.sha256(salt + password.encode()).hexdigest()
    return salt.hex(), password_hash

def verify_password(password, stored_salt, stored_hash):
    """Verify a password against a stored salt and hash."""
    # Hash the provided password with the stored salt
    _, new_hash = hash_password(password, stored_salt)
    
    # Compare the hashes
    return new_hash == stored_hash
```

Voici comment vous pouvez utiliser ce qui précède :

```python
print("=== User Registration ===")
user_password = "mySecurePassword!"
salt, password_hash = hash_password(user_password)
print(f"Password: {user_password}")
print(f"Salt: {salt}")
print(f"Hash: {password_hash}")

# Simulate user login attempts
print("\n=== Login Attempts ===")
correct_attempt = "mySecurePassword!"
wrong_attempt = "wrongPassword"

print(f"Attempt 1: '{correct_attempt}'")
print(f"  Valid? {verify_password(correct_attempt, salt, password_hash)}")

print(f"\nAttempt 2: '{wrong_attempt}'")
print(f"  Valid? {verify_password(wrong_attempt, salt, password_hash)}")
```

Sortie :

```plaintext
=== User Registration ===
Password: mySecurePassword!
Salt: 381779b5262deea84183e4b9454b98b1
Hash: 9756e1f0bc4c1aa4a72f35b0be8d3c8f430d31613371cf7de3c615bc475de98f

=== Login Attempts ===
Attempt 1: 'mySecurePassword!'
  Valid? True

Attempt 2: 'wrongPassword'
  Valid? False
```

Cette implémentation montre un flux complet d'inscription et de connexion.

## Using Key Derivation Functions

Bien que le SHA-256 salé soit meilleur que le hachage simple, les applications modernes devraient utiliser des fonctions de dérivation de clé (KDF) spécifiquement conçues pour le hachage de mots de passe. Celles-ci incluent [PBKDF2](https://www.npmjs.com/package/pbkdf2) (Password-Based Key Derivation Function 2), [bcrypt](https://bcrypt-generator.com/), [scrypt](https://en.wikipedia.org/wiki/Scrypt), et [Argon2](https://en.wikipedia.org/wiki/Argon2). Vous pouvez consulter les liens pour en savoir plus sur ces fonctions de dérivation de clé.

Ces algorithmes sont intentionnellement lents et nécessitent plus de ressources informatiques, ce qui rend les attaques par force brute beaucoup plus difficiles. Implémentons PBKDF2, qui est intégré à Python :

```python
import hashlib
import os

def hash_password_pbkdf2(password, salt=None, iterations=600000):
    """Hash password using PBKDF2 with SHA-256."""
    if salt is None:
        salt = os.urandom(32)  # 32 bytes = 256 bits
    elif isinstance(salt, str):
        salt = bytes.fromhex(salt)
    
    # PBKDF2 with 600,000 iterations (OWASP recommendation for 2024)
    password_hash = hashlib.pbkdf2_hmac(
        'sha256',          # Hash algorithm
        password.encode(), # Password as bytes
        salt,              # Salt as bytes
        iterations,        # Number of iterations
        dklen=32           # Desired key length (32 bytes = 256 bits)
    )
    
    return salt.hex(), password_hash.hex(), iterations

def verify_password_pbkdf2(password, stored_salt, stored_hash, iterations):
    """Verify password against PBKDF2 hash."""
    _, new_hash, _ = hash_password_pbkdf2(password, stored_salt, iterations)
    return new_hash == stored_hash

# Hash a password
print("=== PBKDF2 Password Hashing ===")
password = "SuperSecure123!"
salt, hash_value, iterations = hash_password_pbkdf2(password)

print(f"Password: {password}")
print(f"Salt: {salt}")
print(f"Hash: {hash_value}")
print(f"Iterations: {iterations:,}")
```

Ceci affiche :

```plaintext
=== PBKDF2 Password Hashing ===
Password: SuperSecure123!
Salt: b388aecd774f6a7ddd95405091548bb50102c99beb1a10326a4c54070da4a3a5
Hash: c681450f41d0cec9ea2aad1108efe2a430b9c3d9fc3af621071be10ac9b3615a
Iterations: 600,000
```

Maintenant, vérifions le mot de passe et comparons également les vitesses de SHA-256 par rapport à PBKDF2 :

```python
print("\n=== Verification ===")
is_valid = verify_password_pbkdf2(password, salt, hash_value, iterations)
print(f"Password valid? {is_valid}")

# Show time comparison
import time

print("\n=== Speed Comparison ===")
test_password = "test123"

# Simple SHA-256
start = time.time()
for _ in range(100):
    hashlib.sha256(test_password.encode()).hexdigest()
sha256_time = time.time() - start

# PBKDF2
start = time.time()
for _ in range(100):
    hash_password_pbkdf2(test_password)
pbkdf2_time = time.time() - start

print(f"1000 SHA-256 hashes: {sha256_time:.3f} seconds")
print(f"1000 PBKDF2 hashes: {pbkdf2_time:.3f} seconds")
print(f"PBKDF2 is {pbkdf2_time/sha256_time:.1f}x slower")
```

Sortie :

```plaintext

=== Verification ===
Password valid? True

=== Speed Comparison ===
100 SHA-256 hashes: 0.000 seconds
100 PBKDF2 hashes: 53.631 seconds
PBKDF2 is 240068.1x slower
```

Comment fonctionne PBKDF2 :

* Il prend votre mot de passe et votre sel.
    
* Il applique la fonction de hachage (SHA-256) de manière répétée – 600 000 fois dans cet exemple.
    
* Chaque itération rend le calcul plus lent et plus difficile à forcer.
    
* Vous stockez le sel, le hachage ET le nombre d'itérations (afin de pouvoir vérifier plus tard).
    

Le nombre d'itérations peut être augmenté au fil du temps à mesure que les ordinateurs deviennent plus rapides. Les recommandations modernes (2024) suggèrent 600 000 itérations pour PBKDF2-SHA256.

## Conclusion

Vous avez appris à implémenter un hachage de mot de passe sécurisé en Python à l'aide du module `hashlib`. Voici les points clés à retenir :

* Le hachage de base avec SHA-256 est utile pour l'intégrité des données, pas pour les mots de passe.
    
* Le salage empêche les attaques par tables arc-en-ciel en rendant chaque hachage unique.
    
* PBKDF2 ajoute un coût de calcul via des itérations, ralentissant les attaquants.
    
* Stockez toujours le sel, le hachage et le nombre d'itérations ensemble.
    
* Utilisez des fonctions de dérivation de clé (PBKDF2, bcrypt, Argon2) pour les mots de passe.
    

Les exemples de code de ce tutoriel fournissent une base solide pour implémenter l'authentification dans vos projets. Mais n'oubliez pas que la sécurité est un processus continu. Tenez-vous au courant des meilleures pratiques et révisez régulièrement vos implémentations de sécurité.

Bon codage (sécurisé) !