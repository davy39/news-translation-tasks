---
title: Un guide rapide pour changer votre nom d'utilisateur GitHub
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2019-07-31T14:45:37.000Z'
originalURL: https://freecodecamp.org/news/a-quick-guide-to-changing-your-github-username
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/barcat.png
tags:
- name: GitHub
  slug: github
- name: terminal
  slug: terminal
seo_title: Un guide rapide pour changer votre nom d'utilisateur GitHub
seo_desc: 'Some additional steps to consider after making a change to your username
  on GitHub.

  This being the 2,38947234th and probably last time I’ll change my username, (marriage
  is permanent, right?) I thought I’d better write a quick post on how this transi...'
---

## Quelques étapes supplémentaires à considérer après avoir modifié votre nom d'utilisateur sur GitHub.



Ceci étant la 2,38947234ème et probablement dernière fois que je change mon nom d'utilisateur, (le mariage est permanent, n'est-ce pas ?) J'ai pensé qu'il serait bon d'écrire un rapide article sur la façon de réaliser cette transition aussi facilement que possible. Vous pouvez lire [les instructions officielles sur la façon de changer votre nom d'utilisateur GitHub](https://help.github.com/en/articles/changing-your-github-username?source=post_page---------------------------) ici, et elles vous expliqueront comment le faire et ce qui se passe. Ce qui suit est un guide rapide sur certaines choses à considérer _par la suite_.

# Où apporter des modifications

1. Changer le nom d'utilisateur dans les [paramètres du compte GitHub](https://github.com/settings/admin?source=post_page---------------------------).
2. Si vous utilisez GitHub Pages, changez le nom de votre dépôt "username.github.io".
3. Si vous utilisez d'autres services qui pointent vers l'adresse de votre dépôt "username.github.io", mettez-les à jour.
4. Si vous utilisez Netlify, vous pourriez vouloir vous connecter et reconnecter vos dépôts. (Les miens fonctionnaient toujours, mais en raison d'un problème possiblement sans rapport, je ne suis pas sûr.)
5. Connectez-vous à Travis CI et à d'autres intégrations (vous les trouverez dans l'onglet Paramètres de votre dépôt -> Intégrations et services). Cela mettra à jour votre nom d'utilisateur là-bas.
6. Mettez à jour vos fichiers locaux et les liens de dépôt avec des commandes `find` et `sed` _très soigneusement exécutées_, et renvoyez les modifications vers GitHub.
7. Redéployez tous les sites web que vous pourriez avoir avec votre lien GitHub mis à jour.
8. Corrigiez tous les liens sur le web vers votre profil, vos dépôts ou les Gists que vous pourriez avoir partagés.

# Mises à jour des fichiers locaux

Voici quelques suggestions de chaînes de caractères à rechercher et remplacer votre nom d'utilisateur.

* `github.com/username` (Références à votre page GitHub dans les README ou dans le contenu du site web)
* `username.github.io` (Liens vers votre GitHub Page)
* `git@github.com:username` (URL SSH distantes de la configuration Git)
* `travis-ci.com/username` (Badges Travis dans les README)
* `shields.io/github/.../username` (Badges Shields dans les README, les types incluent `contributors`, `stars`, `tags`, et plus)

Vous pouvez rapidement identifier où se trouvent les chaînes de caractères ci-dessus en utilisant cette commande pour chaque chaîne :

`grep -rnw -e 'foobar'`

Cela recherchera de manière récursive (`r`) tous les fichiers pour les chaînes correspondant au motif (`e`) entier (`w`) fourni et préfixera les résultats avec les numéros de ligne (`n`) afin que vous puissiez les trouver facilement.

L'utilisation de `find` et `sed` peut rendre ces modifications beaucoup plus rapides. Voir [cet article sur la recherche et le remplacement](https://victoria.dev/verbose/how-to-replace-a-string-in-a-dozen-old-blog-posts-with-one-sed-terminal-command/?source=post_page---------------------------).

Profitez de votre nouveau pseudonyme ! (J'espère qu'il restera.)