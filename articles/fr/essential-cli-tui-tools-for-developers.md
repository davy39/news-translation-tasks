---
title: Outils CLI/TUI essentiels pour les développeurs
subtitle: ''
author: Alex Pliutau
co_authors: []
series: null
date: '2025-01-28T15:53:31.686Z'
originalURL: https://freecodecamp.org/news/essential-cli-tui-tools-for-developers
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1738077620615/22e3c744-d609-4469-ae10-ef8ad4b515a1.png
tags:
- name: terminal
  slug: terminal
- name: Linux
  slug: linux
- name: command line
  slug: command-line
- name: cli
  slug: cli
seo_title: Outils CLI/TUI essentiels pour les développeurs
seo_desc: As developers, we spend a lot of time in our terminals. And there are tons
  of great CLI/TUI tools that can boost our productivity (as well as some that are
  just fun to use). From managing Git repositories and navigating file systems to
  monitoring sys...
---

En tant que développeurs, nous passons beaucoup de temps dans nos terminaux. Et il existe de nombreux excellents outils CLI/TUI qui peuvent booster notre productivité (ainsi que certains qui sont simplement amusants à utiliser). De la gestion des dépôts Git et de la navigation dans les systèmes de fichiers à la surveillance des performances du système et même aux jeux rétro, la ligne de commande offre un environnement puissant et polyvalent.

Dans cet article, nous allons passer en revue une collection d'outils CLI/TUI qui ont été largement adoptés dans la communauté des développeurs, couvrant diverses catégories telles que le contrôle de version, les utilitaires système, les éditeurs de texte, et plus encore. Je voulais vous offrir une sélection variée qui répond à différents besoins et flux de travail.

Pour chaque outil, j'inclurai un aperçu, mettant en avant ses principales fonctionnalités et cas d'utilisation, ainsi que des instructions d'installation claires et concises pour divers systèmes d'exploitation, afin que vous puissiez rapidement commencer à utiliser ces précieux compagnons de ligne de commande.

## **Table des matières**

* [Outils Kubernetes](#heading-outils-kubernetes)
    
* [Outils de conteneurs](#heading-outils-de-conteneurs)
    
* [Outils de fichiers et de texte](#heading-outils-de-fichiers-et-de-texte)
    
* [Outils Git](#heading-outils-git)
    
* [Outils de développement](#heading-outils-de-developpement)
    
* [Outils de réseau](#heading-outils-de-reseau)
    
* [Outils de poste de travail](#heading-outils-de-poste-de-travail)
    

## **Outils Kubernetes**

### [**k9s**](https://github.com/derailed/k9s) — CLI Kubernetes pour gérer vos clusters avec style

K9s est un outil indispensable pour toute personne travaillant avec Kubernetes. Son interface utilisateur intuitive basée sur le terminal, ses capacités de surveillance en temps réel et ses options de commande puissantes en font un outil remarquable dans le monde des outils de gestion Kubernetes.

Le projet K9s est conçu pour surveiller en continu les changements dans le cluster Kubernetes et offrir des commandes ultérieures pour interagir avec les ressources observées. Cela facilite la gestion des applications, surtout dans un environnement complexe et multi-clusters. L'objectif du projet est de rendre la gestion Kubernetes plus accessible et moins intimidante, surtout pour ceux qui ne sont pas des experts Kubernetes.

Il suffit de lancer k9s dans votre terminal et de commencer à explorer les ressources Kubernetes avec facilité.

![Interface K9s](https://miro.medium.com/v2/resize:fit:700/0*tkfwKS01NCnUBE-N.png align="left")

Pour installer K9s :

```bash
# via Homebrew pour macOS
brew install derailed/k9s/k9s

# via snap pour Linux
snap install k9s --devmode

# via Chocolatey pour Windows
choco install k9s

# via go install
go install github.com/derailed/k9s@latest
```

### [**kubectx**](https://github.com/ahmetb/kubectx) — basculer entre les contextes (clusters) sur kubectl plus rapidement.

Kubectx est l'outil le plus populaire pour basculer entre les contextes Kubernetes, mais il a le moins de fonctionnalités ! Il affiche tous les contextes de votre configuration Kubernetes sous forme de liste sélectionnable et vous permet d'en choisir un. C'est tout !

Ce projet comprend 2 outils :

* **kubectx** est un outil qui vous aide à basculer entre les contextes (clusters) sur kubectl plus rapidement.
    
* **kubens** est un outil pour basculer entre les espaces de noms Kubernetes (et les configurer pour kubectl) facilement.
    

Ces outils rendent très facile le basculement entre les clusters et les espaces de noms Kubernetes si vous travaillez avec plusieurs d'entre eux quotidiennement. Voici à quoi cela ressemble en action :

![](https://miro.medium.com/v2/resize:fit:700/0*g442WF-cXW-z1dKQ.gif align="left")

Pour installer kubectx :

```bash
# via Homebrew pour macOS
brew install kubectx

# via apt pour Debian
sudo apt install kubectx

# via pacman pour Arch Linux
sudo pacman -S kubectx

# via Chocolatey pour Windows
choco install kubens kubectx
```

### [**kubescape**](https://github.com/kubescape/kubescape) — Plateforme de sécurité Kubernetes pour votre IDE, pipelines CI/CD et clusters.

J'espère que vous prenez la sécurité de vos clusters Kubernetes au sérieux. Si c'est le cas, **kubescape** est vraiment excellent pour tester si votre cluster Kubernetes est déployé de manière sécurisée selon plusieurs frameworks.

Kubescape peut scanner les clusters, les fichiers YAML et les charts Helm et détecte les mauvaises configurations selon plusieurs sources.

Je l'utilise généralement dans mon CI/CD pour scanner automatiquement les vulnérabilités lors de la modification des manifests Kubernetes ou des templates Helm.

![Scan kubescape](https://miro.medium.com/v2/resize:fit:700/0*Ft2r01ij9Rxj2-V0.png align="left")

Pour installer kubescape :

```bash
# via Homebrew pour macOS
brew install kubescape

# via apt pour Debian
sudo add-apt-repository ppa:kubescape/kubescape
sudo apt update
sudo apt install kubescape

# via Chocolatey pour Windows
choco install kubescape
```

## **Outils de conteneurs**

### [**ctop**](https://github.com/bcicen/ctop) — Une interface de type top pour les métriques des conteneurs.

**ctop** est essentiellement une version améliorée de `docker stats`. Il fournit un aperçu concis et condensé des métriques en temps réel pour plusieurs conteneurs. Il est livré avec un support intégré pour Docker et runC, et des connecteurs pour d'autres systèmes de conteneurs et de clusters sont prévus pour les futures versions.

L'utilisation de ctop est simple. Une fois que vous avez l'outil ouvert, vous verrez tous vos conteneurs actuellement actifs listés.

![ctop en action](https://miro.medium.com/v2/resize:fit:700/0*EJ5kdlEs5M5QxDBy.gif align="left")

Pour installer ctop :

```bash
# via Homebrew pour macOS
brew install ctop

# via pacman pour Arch Linux
sudo pacman -S ctop

# via scoop pour Windows
scoop install ctop
```

### [**lazydocker**](https://github.com/jesseduffield/lazydocker) — Une interface terminal simple pour docker et docker-compose.

Bien que l'interface de ligne de commande de Docker soit puissante, parfois vous pourriez vouloir une approche plus visuelle sans l'overhead d'une GUI complète. Cela est particulièrement vrai lorsque vous gérez des conteneurs Docker sur un serveur Linux sans tête où l'installation d'une GUI basée sur le web pourrait être indésirable.

Lazydocker a été créé par [Jesse Duffield](https://github.com/jesseduffield) pour aider à rendre la gestion des conteneurs docker un peu plus facile. En bref, Lazydocker est une interface terminal (écrite en Golang) pour les commandes docker et docker-compose.

![lazydocker en action](https://miro.medium.com/v2/resize:fit:700/0*Cbmx4ShRSO7ccVy2.gif align="left")

Pour installer lazydocker :

```bash
# via Homebrew pour macOS
brew install lazydocker

# via Chocolatey pour Windows
choco install lazydocker

# via go install
go install github.com/jesseduffield/lazydocker@latest
```

### [**dive**](https://github.com/wagoodman/dive) — Un outil pour explorer chaque couche dans une image Docker.

Une image Docker est composée de couches, et avec chaque couche que vous ajoutez, plus d'espace sera occupé par l'image. Par conséquent, plus il y a de couches dans l'image, plus l'image nécessitera d'espace.

C'est là que **dive** excelle, il vous aide à explorer votre image Docker et le contenu des couches. Il peut également vous aider à trouver des moyens de réduire la taille de votre image Docker/OCI.

![](https://miro.medium.com/v2/resize:fit:700/0*swo_hrKJ9EV7hyMs.gif align="left")

Pour installer dive :

```bash
# via Homebrew pour macOS
brew install dive

# via pacman pour Arch Linux
pacman -S dive

# via go install
go get github.com/wagoodman/dive
```

## **Outils de fichiers et de texte**

### [**jq**](https://github.com/jqlang/jq) — Processeur JSON en ligne de commande.

Vous connaissez peut-être déjà cet outil car il est bien connu dans la communauté des développeurs.

Malheureusement, les shells comme Bash ne peuvent pas interpréter et travailler avec JSON directement. C'est là que vous pouvez utiliser **jq** comme processeur JSON en ligne de commande qui est similaire à sed, awk, grep, etc. pour les données JSON. Il est écrit en C portable et n'a aucune dépendance d'exécution. Cela vous permet de découper, filtrer, mapper et transformer des données structurées avec facilité.

![](https://miro.medium.com/v2/resize:fit:700/0*uwysqWprpmrLrJQP.png align="left")

Pour installer jq, vous pouvez télécharger les dernières versions depuis la [page de release GitHub](https://github.com/jqlang/jq/releases).

### [**bat**](https://github.com/sharkdp/bat) — Un clone de cat(1) avec des ailes.

C'est le CLI le plus utilisé sur ma machine actuellement. Il y a quelques années, c'était **cat**, qui est génial mais ne fournit pas de coloration syntaxique ni d'intégration Git.

La coloration syntaxique de Bat prend en charge de nombreux langages de programmation et de balisage, vous aidant à rendre votre code plus lisible directement dans le terminal. L'intégration Git vous permet de voir les modifications par rapport à l'index, en mettant en évidence les lignes que vous avez ajoutées ou modifiées.

Il suffit de lancer `bat nomdefichier` et de profiter de sa sortie.

![Exemple Bat](https://miro.medium.com/v2/resize:fit:656/0*L02HhsqDcq2_G_z4.png align="left")

Pour installer bat :

```bash
# via Homebrew pour macOS
brew install bat

# via apt pour Debian
sudo apt install bat

# via pacman pour Arch Linux
pacman -S bat

# via Chocolatey pour Windows
choco install bat
```

### [**ripgrep**](https://github.com/BurntSushi/ripgrep) — Rechercher récursivement des répertoires pour un motif regex tout en respectant votre gitignore.

**ripgrep** devient définitivement une alternative populaire (si ce n'est la plus populaire) à la commande **grep**. Même certains éditeurs comme [Visual Studio Code](https://code.visualstudio.com/updates/v1_11) utilisent ripgrep pour alimenter leurs offres de recherche.

Le principal argument de vente est son comportement par défaut pour la recherche récursive et sa vitesse.

Je n'utilise plus guère grep sur ma machine personnelle, car ripgrep est beaucoup plus rapide.

Pour installer ripgrep :

```bash
# via Homebrew pour macOS
brew install ripgrep

# via apt pour Debian
sudo apt-get install ripgrep

# via pacman pour Arch Linux
pacman -S ripgrep

# via Chocolatey pour Windows
choco install ripgrep
```

## **Outils Git**

### [**lazygit**](https://github.com/jesseduffield/lazygit) — Interface terminal simple pour les commandes git.

**lazygit** est une autre excellente interface terminal pour les commandes Git développée par [**Jesse Duffield**](https://github.com/jesseduffield) en utilisant Go.

Je n'ai pas de problème à utiliser directement la CLI Git pour des choses simples, mais elle est notoirement verbeuse pour des cas d'utilisation plus avancés. Je suis simplement trop paresseux pour mémoriser des commandes plus longues.

Et lazigit m'a rendu plus productif avec Git que jamais.

![Interface lazigit](https://miro.medium.com/v2/resize:fit:700/0*ykEtn2HQ9QgU40jx.png align="left")

Pour installer lazigit :

```bash
# via Homebrew pour macOS
brew install jesseduffield/lazygit/lazygit

# via pacman pour Arch Linux
pacman -S lazygit

# via scoop pour Windows
scoop install lazygit
```

## **Outils de développement**

### [**ATAC**](https://github.com/Julien-cpsn/ATAC) — Un client API simple (comme Postman) dans votre terminal.

ATAC signifie Arguably a Terminal API Client. Il est basé sur des clients populaires comme Postman, Insomnia et Bruno, mais il s'exécute dans votre terminal sans avoir besoin d'un environnement graphique particulier.

Il fonctionne mieux pour les développeurs qui ont besoin d'un client API hors ligne et multiplateforme à portée de main (terminal).

![ATAC](https://miro.medium.com/v2/resize:fit:700/0*NoOMeMxkELNFI9RS.png align="left")

Pour installer ATAC :

```bash
# via Homebrew pour macOS
brew tap julien-cpsn/atac
brew install atac

# via pacman pour Arch Linux
pacman -S atac
```

### [**k6**](https://github.com/grafana/k6) — Un outil moderne de test de charge, utilisant Go et JavaScript.

J'ai utilisé de nombreux outils de test de charge dans ma carrière, comme [vegeta](https://github.com/tsenart/vegeta) ou même [ab](https://httpd.apache.org/docs/2.4/programs/ab.html) par le passé. Mais maintenant, j'utilise surtout **k6** car il a tout ce dont j'ai besoin et possède une excellente GUI et TUI.

Pourquoi cela fonctionne bien pour moi :

* k6 a une très bonne [documentation](https://k6.io/docs/)
    
* De nombreuses intégrations disponibles : Swagger, scripts JMeter, etc.
    
* Le reporting des résultats est assez bon
    

![Interface K6](https://cdn.hashnode.com/res/hashnode/image/upload/v1737552000859/df5af273-3706-4d41-9dbe-717d2f2d18b7.webp align="center")

Pour installer k6 :

```bash
# via Homebrew pour macOS
brew install k6

# via apt pour Debian
sudo apt-get install k6

# via Chocolatey pour Windows
choco install k6
```

### [**httpie**](https://github.com/httpie/cli) — client HTTP en ligne de commande moderne et convivial pour l'ère des API.

Ne vous méprenez pas, curl est génial, mais pas très convivial.

HTTPie a une syntaxe simple et expressive, prend en charge JSON et les données de formulaire, gère l'authentification et les en-têtes, et affiche une sortie colorisée et formatée.

![](https://miro.medium.com/v2/resize:fit:700/0*Bqi3gBKgIkeEPEI_.gif align="left")

Pour installer httpie :

```bash
# via Homebrew pour macOS
brew install httpie

# via apt pour Debian
sudo apt install httpie

# via pacman pour Arch Linux
pacman -Syu httpie

# via Chocolatey pour Windows
choco install httpie
```

### [**asciinema**](https://github.com/asciinema/asciinema) — Enregistreur de sessions terminal.

Je l'appelle un YouTube du terminal :)

asciinema est un excellent outil lorsque vous souhaitez partager vos sessions terminal avec quelqu'un d'autre, au lieu d'enregistrer des vidéos lourdes.

Je l'utilise souvent lorsque je développe des outils CLI et que je veux partager la démonstration de leur fonctionnement (sur GitHub, par exemple).

![](https://miro.medium.com/v2/resize:fit:700/0*Exg2XuZlIPaJJ-iB.png align="left")

Pour installer asciinema :

```bash
# via Homebrew pour macOS
brew install asciinema

# via apt pour Debian
sudo apt install asciinema

# via pacman pour Arch Linux
sudo pacman -S asciinema
```

## **Réseau**

### [doggo](https://github.com/mr-karan/doggo) — Un client DNS en ligne de commande.

Il est totalement inspiré par **dog** qui est écrit en Rust.

Par le passé, j'utilisais **dig** pour inspecter le DNS, mais sa sortie est souvent verbeuse et difficile à analyser visuellement.

**doggo** répond à ces lacunes en offrant deux améliorations clés :

* doggo fournit un support de sortie JSON pour un scripting et un parsing faciles.
    
* doggo offre un format de sortie lisible par l'homme qui utilise un codage couleur et une mise en page tabulaire pour présenter les informations DNS de manière claire et concise.
    

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1737552264803/bb902365-bc0d-4a56-9a87-6b065ee5608a.png align="center")

Pour installer doggo :

```bash
# via Homebrew pour macOS
brew install doggo

# via scoop pour Windows
scoop install doggo

# via go install
go install github.com/mr-karan/doggo/cmd/doggo@latest
```

### [**gping**](https://github.com/orf/gping) — Ping, mais avec un graphique.

La commande bien connue **ping** n'est pas la plus intéressante à regarder, et interpréter sa sortie de manière utile peut être difficile.

**gping** donne un graphique de la latence de ping vers un hôte, et la fonctionnalité la plus utile est la capacité d'exécuter des pings simultanés vers plusieurs hôtes et de les tracer tous sur le même graphique.

![](https://miro.medium.com/v2/resize:fit:700/0*IPi1TOpiMnWPN1VU.gif align="left")

Pour installer gping :

```bash
# via Homebrew pour macOS
brew install gping

# via Chocolatey pour Windows
choco install gping

# via apt pour Debian
apt install gping
```

## **Poste de travail**

### [**tmux**](https://github.com/tmux/tmux/wiki) — Un multiplexeur de terminal.

Pourquoi tmux est-il si important ?

Vous avez peut-être rencontré des situations où vous devez afficher plusieurs consoles de terminal en même temps. Par exemple, vous pouvez avoir quelques serveurs en cours d'exécution (par exemple, web, base de données, débogueur) et vous pourriez vouloir surveiller toutes les sorties provenant de ces serveurs en temps réel pour valider le comportement ou exécuter des commandes.

Avant tmux, vous auriez peut-être simplement ouvert quelques onglets différents dans le terminal et basculé entre eux pour voir la sortie.

Heureusement, il existe une méthode plus facile — **tmux**.

En résumé, voici quelques-unes de ses fonctionnalités les plus populaires :

* Gestion des fenêtres/panneaux
    
* Gestion des sessions avec persistance
    
* Sessions partageables avec d'autres utilisateurs
    
* Configurations scriptables
    

![](https://miro.medium.com/v2/resize:fit:700/0*u8o0WxutrPXxg6FG.png align="left")

Pour installer tmux :

```bash
# via Homebrew pour macOS
brew install tmux

# via apt pour Debian
apt install tmux

# via pacman pour Arch Linux
pacman -S tmux
```

### [**zellij**](https://github.com/zellij-org/zellij) — Un espace de travail terminal avec tout inclus.

Puisque j'ai listé tmux ici, il est également logique d'inclure un nouveau concurrent, **Zellij**, qui a gagné en traction dans la communauté des développeurs. Les deux ont leurs propres fonctionnalités et objectifs uniques.

Comparé aux multiplexeurs de terminal traditionnels, zellij offre une interface plus conviviale, des éléments de design modernes, des systèmes de mise en page intégrés et un système de plugins, ce qui le rend plus facile à prendre en main pour les nouveaux venus.

J'aime toujours tmux. Il a une place spéciale dans mon cœur car il a servi un grand but pendant des années. Mais zellij est une autre bonne option.

![](https://miro.medium.com/v2/resize:fit:700/0*VwAit4tO1IjxH9dp.gif align="left")

Pour installer zellij :

```bash
# via Homebrew pour macOS
brew install zellij

# via apt pour Debian
apt install zellij

# via pacman pour Arch Linux
pacman -S zellij
```

### [**btop**](https://github.com/aristocratos/btop) — Un moniteur de ressources.

Je ne peux pas vivre sans btop, et il est installé sur toutes mes machines via mes [dotfiles](https://github.com/plutov/dotfiles) personnels. Je n'utilise plus les GUIs intégrées du système d'exploitation pour vérifier l'utilisation des ressources sur ma machine hôte, car **btop** peut le faire beaucoup mieux.

Je l'utilise pour explorer rapidement ce qui utilise le plus de mémoire, surveiller et tuer certains processus, et plus encore.

![](https://miro.medium.com/v2/resize:fit:700/0*HbuJrCbT6xVApLoh.png align="left")

Pour installer btop :

```bash
# via Homebrew pour macOS
brew install btop

# via snap pour Debian
sudo snap install btop
```

## **Conclusion**

Ces CLIs/TUIs devraient bien fonctionner dans n'importe quel terminal moderne. J'utilise personnellement [Ghostty](https://ghostty.org/) actuellement et cela fonctionne très bien, mais d'autres options populaires comme **iTerm2, Kitty**, et les applications de terminal par défaut sur macOS et Linux devraient également offrir une expérience fluide. L'important est de s'assurer que votre terminal prend en charge des fonctionnalités comme les palettes de 256 couleurs et le codage UTF-8 pour un affichage optimal de ces outils.

Il existe une énorme quantité de CLIs/TUIs, et je n'ai pas pu tous les lister (bien que j'aie essayé d'en lister certains des meilleurs). Cette sélection représente un point de départ pour explorer le riche écosystème d'outils en ligne de commande disponibles pour les développeurs. Je vous encourage à explorer davantage, à découvrir de nouveaux outils qui répondent à vos besoins spécifiques, et à contribuer à la communauté en partageant vos découvertes.

[Explorez plus d'articles sur packagemain.tech](https://packagemain.tech)