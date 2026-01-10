---
title: Vulnérabilités WordPress que vous devez connaître — et comment les corriger
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-13T17:30:27.000Z'
originalURL: https://freecodecamp.org/news/wordpress-vulnerabilities-you-need-to-know-about-and-how-to-fix-them-497a2d8b2c3e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ZjOP68Ue2tyBjLPZS4Nz1g.jpeg
tags:
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
- name: WordPress
  slug: wordpress
seo_title: Vulnérabilités WordPress que vous devez connaître — et comment les corriger
seo_desc: 'By Joel S. Syder

  WordPress is an incredibly useful and versatile platform for all kinds of blogging.
  It’s become very popular. Unfortunately, that popularity has brought with it quite
  a few vulnerabilities that can be exploited by hackers. It’s impor...'
---

Par Joel S. Syder

WordPress est une plateforme incroyablement utile et polyvalente pour tout type de blogging. Il est devenu très populaire. Malheureusement, cette popularité a apporté avec elle plusieurs vulnérabilités qui peuvent être exploitées par des pirates. Il est important que vous connaissiez ces faiblesses et que vous preniez des mesures pour prévenir leur exploitation. Voici six vulnérabilités WordPress que vous devez connaître.

#### **Connexion WordPress**

"La manière la plus simple pour quelqu'un d'accéder à votre WordPress est d'attaquer votre connexion. Ces types d'attaques par force brute sont la méthode la plus courante pour compromettre votre WordPress. "Cette méthode fonctionne en devinant votre login et mot de passe encore et encore à l'aide de certains logiciels," conseille Martha Goss, programmeuse WP chez [WriteMyX](https://writemyx.com/) et [BritStudent](https://britstudent.com/).

WordPress ne limite pas le nombre de tentatives de connexion, donc les attaques par force brute peuvent être très efficaces. Votre meilleure défense contre cette vulnérabilité est d'installer un plugin qui limitera le nombre de tentatives de connexion autorisées, comme iThemes Security Pro. Vous pouvez également utiliser un gestionnaire de mots de passe pour générer des mots de passe aléatoires qui sont beaucoup moins susceptibles d'être devinés. Évitez les mots de passe qui semblent évidents — n'utilisez rien comme 123456, password, ou quoi que ce soit lié à vous.

Par exemple, pas de noms d'animaux, de noms d'enfants, de noms de partenaires, de noms de rues, etc., car tout cela peut être utilisé contre vous. Si vous pensez que les mélanger pourrait être une meilleure mesure de sécurité tout en restant facile à retenir, détrompez-vous. Vos profils sur les réseaux sociaux sont une porte d'entrée facile dans votre psychologie, et n'importe qui pourrait trouver ces mots de passe parmi vos publications.

Il est préférable de choisir quelque chose qui n'a aucun rapport avec vous — et assurez-vous d'utiliser une bonne combinaison de lettres, de majuscules, de chiffres ainsi que de symboles. Vous ne pouvez jamais être trop prudent ou sous-estimer votre ennemi.

Source : [https://www.wordfence.com/blog/2017/12/aggressive-brute-force-wordpress-attack/](https://www.wordfence.com/blog/2017/12/aggressive-brute-force-wordpress-attack/)

#### **Compte utilisateur admin par défaut**

Les pirates peuvent accéder à l'arrière-plan de votre compte WordPress en exploitant votre compte utilisateur admin par défaut. Essayez de supprimer votre compte admin et d'accéder à votre site à partir d'un compte commun qui dispose de privilèges admin. Les gens peuvent accéder en injectant des commandes SQL en utilisant un paramètre de valeur de cookie. Pour éviter ce type de compromission, essayez de mettre à jour votre logiciel de sécurité vers l'IPS le plus récent.

Jibu Pro peut également être accessible par des scripts inter-sites car il ne nettoie pas correctement les entrées fournies par l'utilisateur. Pour vous protéger contre cette vulnérabilité, renforcez les permissions sur votre site. Vous pouvez même aller jusqu'à cacher votre connexion admin si bien que personne ne peut la trouver. La meilleure façon de faire cela — et la plus simple de loin — est de lui donner un autre nom. Admin est assez évident, et les pirates chercheront cela. Mais si vous lui donnez un nom entièrement différent — Chat, SpaceMonkey ou choisissez parmi une large variété de possibilités amusantes et intelligentes — les pirates auront du mal à la trouver. Par défaut, ils auront beaucoup plus de mal à injecter une commande SQL — ils ne savent pas où l'injecter.

Source : [https://www.acunetix.com/blog/articles/exploiting-sql-injection-example/](https://www.acunetix.com/blog/articles/exploiting-sql-injection-example/)

#### **Piratage d'URL**

"WordPress utilise PHP pour exécuter tous ses scripts côté serveur, et cela, malheureusement, le rend vulnérable aux attaques par URL. Il est trop facile pour les pirates de s'infiltrer dans les opérations WordPress et de créer des problèmes pour vous," avertit Dorothy Cox, rédactrice technique chez [1Day2Write](https://1day2write.com/). En raison de la nature de sa base de données, il y a amplement d'opportunités pour les pirates de voler vos informations sensibles. Pour éviter ces violations, hébergez votre WordPress sur Apache Web Server, qui utilise des fichiers .htaccess et vous protégera contre le piratage d'URL.

Assurez-vous de désinstaller et de supprimer tous les plugins inutiles que vous avez sur votre site web. Cela limite les points d'accès pour les pirates — les thèmes pourraient également être votre ennemi, surtout si vous en avez une tonne que vous n'utilisez pas. PHP est trop facile à exploiter, et vous devriez protéger votre site web du mieux que vous pouvez. En bonus, ces thèmes et plugins supplémentaires pourraient ralentir votre temps de chargement, donc vous amélioreriez votre SEO tout en protégeant votre site web.

Source : [https://blog.websecurify.com/2017/02/hacking-wordpress-4-7-0-1.html](https://blog.websecurify.com/2017/02/hacking-wordpress-4-7-0-1.html)

#### **Logiciel obsolète**

Chaque fois que vous utilisez WordPress avec un logiciel obsolète, vous courez un risque accru d'être compromis. Il est facile de tomber dans le piège de penser que les mises à jour ne font qu'améliorer les bugs mineurs et les désagréments, mais elles sont également importantes pour les correctifs de sécurité qu'elles incluent.

Garder votre logiciel à jour est une chose très facile à faire, et cela vous protégera contre de nombreuses menaces de piratage. Si vous craignez d'oublier de mettre à jour votre logiciel, installez simplement les mises à jour automatiques avec des plugins tels que la gestion des versions WordPress d'iThemes. Ces types de fonctionnalités vous font gagner du temps et garantissent que vous ne manquez pas un correctif de sécurité et que votre site n'est pas compromis.

Les pirates chercheront quelque chose qui est facile à craquer. En mettant à jour, vous installez probablement de nouveaux correctifs de sécurité qui peuvent empêcher tout pirate d'entrer. De plus, assurez-vous de ne rien installer à partir de sources non sûres. Vous pourriez inviter les pirates directement.

Source : [https://www.kimiweb.com/wordpress-help/updating-wordpress-and-plugins/](https://www.kimiweb.com/wordpress-help/updating-wordpress-and-plugins/)

#### **Préfixe par défaut pour les tables de la base de données**

Il y a de nombreuses tables dans la base de données WordPress, et dans de nombreuses installations, elles sont nommées avec un préfixe par défaut commençant par "_wp_." Cela peut ne pas sembler être un gros problème, mais cela donne un petit avantage aux pirates car c'est une chose de moins à déchiffrer.

Vous pouvez rendre les choses beaucoup plus difficiles pour eux en changeant simplement ces préfixes par défaut. Est-ce que cela arrêtera tous les pirates ? Non, mais cela en arrêtera beaucoup, et c'est juste un outil de plus utile pour défendre votre compte WordPress. C'est un processus simple que vous pouvez facilement faire vous-même — les pirates cherchent toujours un point d'entrée facile en premier, et si vous les éliminez, ils pourraient abandonner.

Source : [https://www.cloudways.com/blog/change-wordpress-database-table-prefix-manually/](https://www.cloudways.com/blog/change-wordpress-database-table-prefix-manually/)

#### **Vulnérabilités PHP**

Les pirates peuvent accéder à votre compte en exploitant votre code PHP, et c'est plus courant que vous ne le pensez. Limitez votre risque en désinstallant puis en supprimant tous les plugins dont vous n'avez pas besoin. Chacun d'eux est un point d'accès potentiel pour les personnes cherchant à compromettre vos informations. Essayez d'éviter d'utiliser des plugins qui ne sont plus mis à jour ; s'il s'est écoulé plus de six mois depuis une mise à jour, il est temps de considérer simplement de le supprimer.

Source : [https://www.cloudways.com/blog/change-wordpress-database-table-prefix-manually/](https://www.cloudways.com/blog/change-wordpress-database-table-prefix-manually/)

#### **Passer à un meilleur hébergement**

Lorsque vous commencez, l'hébergement le moins cher semble être la meilleure idée. Mais, l'hébergement bon marché vient également avec un manque de fonctionnalités de sécurité qui pourrait être nocif. Assurez-vous d'avoir le meilleur et le plus sûr hébergement afin de vous protéger, vous et vos clients.

Source : [https://www.webhostingsecretrevealed.net/blog/web-hosting-guides/switching-web-host/](https://www.webhostingsecretrevealed.net/blog/web-hosting-guides/switching-web-host/)

#### **Conclusion**

Garder votre site sécurisé est l'une des responsabilités les plus importantes lorsque vous gérez un compte WordPress. Limitez le nombre de tentatives pour votre connexion. Changez les préfixes par défaut pour vos tables. Téléchargez les plugins recommandés dans cet article et voyez comment ils fonctionnent pour vous. WordPress est une excellente ressource pour le blogging, mais n'oubliez pas qu'il y a beaucoup de gens qui cherchent sur le site des comptes vulnérables au piratage. Assurez-vous que le vôtre n'en fait pas partie.

_Joel Syder est coach WP chez [Originwritings.com](https://originwritings.com/) et [Australia2write.com](https://australia2write.com/). Il aime aider les gens à construire des sites web de leurs rêves ainsi que créer des articles sur les choses qui l'excitent pour [Academicbrits.com](https://academicbrits.com/), service de tutorat._