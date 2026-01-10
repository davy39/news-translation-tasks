---
title: Comment corriger Git qui demande toujours les identifiants de l'utilisateur
subtitle: ''
author: Bolaji Ayodeji
co_authors: []
series: null
date: '2019-07-21T20:50:38.000Z'
originalURL: https://freecodecamp.org/news/how-to-fix-git-always-asking-for-user-credentials
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/article-banner--10-.png
tags:
- name: Git
  slug: git
- name: terminal
  slug: terminal
- name: version control
  slug: version-control
seo_title: Comment corriger Git qui demande toujours les identifiants de l'utilisateur
seo_desc: Have you ever encountered Git asking you for your username and password
  every time you try to interact with GitHub even after configuring it? Well, this
  is a very common problem among users who use the HTTPS clone URL for their repository.
  In this ar...
---

Avez-vous déjà rencontré Git qui vous demande votre nom d'utilisateur et votre mot de passe chaque fois que vous essayez d'interagir avec GitHub, même après l'avoir configuré ? Eh bien, c'est un problème très courant parmi les utilisateurs qui utilisent l'URL de clonage HTTPS pour leur dépôt. Dans cet article, je vais vous montrer comment corriger cela.

Les URL de clonage `https://` sont disponibles sur tous les dépôts publics et privés. Ces URL fonctionnent partout, même si vous êtes derrière un pare-feu ou un proxy.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/clone.png align="left")

Lorsque vous interagissez avec un dépôt distant en utilisant les URL HTTPS sur la ligne de commande, vous serez invité à entrer votre nom d'utilisateur et votre mot de passe GitHub, ce qui est ennuyeux, n'est-ce pas ?

Eh bien, l'utilisation d'une URL distante HTTPS a certains avantages : elle est plus facile à configurer que SSH :), et fonctionne généralement à travers des pare-feux et des proxys stricts. Cependant, elle vous invite également à entrer vos identifiants GitHub chaque fois que vous tirez ou poussez un dépôt :(.

#### Vous pouvez corriger cela en configurant Git pour qu'il stocke votre mot de passe pour vous.

Voici comment faire :

* Mettez à jour l'URL de la télécommande d'origine en utilisant SSH au lieu de HTTPS ;

```python
git remote set-url origin git@github.com:username/repo.git
```

ou

* Faites en sorte que Git stocke le nom d'utilisateur et le mot de passe et il ne les demandera plus jamais.

```python
git config --global credential.helper store
```

* Enregistrez le nom d'utilisateur et le mot de passe pour une session (mettez-les en cache) ;

```python
git config --global credential.helper cache
```

* Vous pouvez également définir un délai d'expiration pour le paramètre ci-dessus

```python
git config --global credential.helper 'cache --timeout=600'
```

Bingo, vous venez de le corriger, Git ne vous demandera plus jamais vos identifiants.

---

# CONCLUSION

Cependant, pour des raisons de sécurité, il est conseillé d'utiliser SSH pour interagir avec GitHub, surtout si vous travaillez pour une entreprise ou si vous utilisez un ordinateur qui n'est pas le vôtre.

En utilisant le protocole SSH, vous pouvez vous connecter à GitHub sans fournir votre nom d'utilisateur ou votre mot de passe à chaque fois.

Apprenez à vous connecter à GitHub avec SSH [ici](https://help.github.com/en/articles/connecting-to-github-with-ssh).