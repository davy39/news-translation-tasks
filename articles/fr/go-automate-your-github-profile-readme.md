---
title: Comment automatiser votre README de profil GitHub
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2020-07-28T20:47:00.000Z'
originalURL: https://freecodecamp.org/news/go-automate-your-github-profile-readme
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/2C5D1709-D4F5-4019-94FB-3339B5504126.png
tags:
- name: GitHub
  slug: github
- name: GitHub Actions
  slug: github-actions
- name: golang
  slug: golang
- name: Productivity
  slug: productivity
seo_title: Comment automatiser votre README de profil GitHub
seo_desc: "GitHub’s new profile page README feature is bringing some personality to\
  \ the Myspace pages of the developer Internet. \nThough Markdown lends itself best\
  \ to standard static text content, that’s not stopping creative folks from working\
  \ to create a next..."
---

La nouvelle fonctionnalité de README de page de profil de GitHub apporte une touche de personnalité aux pages Myspace de l'Internet des développeurs. 

Bien que Markdown se prête mieux au contenu textuel statique standard, cela n'empêche pas les personnes créatives de travailler à la création d'un README de niveau supérieur. Vous pouvez inclure des GIF et des images pour ajouter du mouvement et du pep's (ils sont couverts dans [GitHub Flavor Markdown](https://github.github.com/gfm/)), mais je pense à quelque chose de plus dynamique.

Puisqu'il est en évidence sur votre profil GitHub, votre README est une excellente opportunité de faire savoir aux gens ce que vous êtes, ce que vous trouvez important, et de mettre en avant quelques points forts de votre travail. 

Vous pourriez aimer montrer vos derniers dépôts, tweets, ou articles de blog. Le maintenir à jour ne doit pas non plus être une corvée, grâce aux outils de livraison continue comme GitHub Actions.

Mon README actuel se rafraîchit quotidiennement avec un lien vers mon dernier article de blog. Voici comment j'ai construit un `README.md` auto-mise à jour avec Go et GitHub actions.

## Lire et écrire des fichiers avec Go

J'ai écrit beaucoup de Python récemment, mais pour certaines choses, j'aime vraiment utiliser Go. On pourrait dire que c'est mon langage de prédilection pour les projets juste-pour-`func`. Désolé. Je n'ai pas pu m'en empêcher.

Pour créer mon README.md, je vais obtenir du contenu statique à partir d'un fichier existant, le mélanger avec du nouveau contenu dynamique que nous allons générer avec Go, puis cuire le tout à 400 degrés jusqu'à ce que quelque chose d'extraordinaire en ressorte.

Voici comment nous lisons un fichier appelé `static.md` et le mettons sous forme de `string` :

```go
// Déballer le contenu Markdown
content, err := ioutil.ReadFile("static.md")
if err != nil {
    log.Fatalf("impossible de lire le fichier : %v", err)
    return err
}

// Le transformer en chaîne de caractères
stringyContent := string(content)

```

Les possibilités pour votre contenu dynamique ne sont limitées que par votre imagination ! Ici, j'utiliserai le [package](https://github.com/mmcdole/gofeed) [`github.com/mmcdole/gofeed`](https://github.com/mmcdole/gofeed) pour lire le flux RSS de mon blog et obtenir le dernier article.

```go
fp := gofeed.NewParser()
feed, err := fp.ParseURL("https://victoria.dev/index.xml")
if err != nil {
    log.Fatalf("erreur lors de la récupération du flux : %v", err)
}
// Obtenir l'élément le plus récent
rssItem := feed.Items[0]

```

Pour assembler ces morceaux et produire une délicieuse chaîne de caractères, nous utilisons [`fmt.Sprintf()`](https://golang.org/pkg/fmt/#Sprintf) pour créer une chaîne formatée.

```go
// Mélanger le contenu statique et dynamique jusqu'à ce que des pics fermes se forment
blog := "Lisez mon dernier article de blog : **[" + rssItem.Title + "](" + rssItem.Link + ")**"
data := fmt.Sprintf("%s\n%s\n", stringyContent, blog)

```

Ensuite, pour créer un nouveau fichier à partir de ce mélange, nous utilisons [`os.Create()`](https://golang.org/pkg/os/#Create). Il y a [plus de choses à savoir sur le report de `file.Close()`](https://www.joeshaw.org/dont-defer-close-on-writable-files/), mais nous n'avons pas besoin d'entrer dans ces détails ici. Nous ajouterons `file.Sync()` pour nous assurer que notre README est écrit.

```go
// Préparer le fichier avec une légère couche de os
file, err := os.Create("README.md")
if err != nil {
    return err
}
defer file.Close()

// Cuire à n octets par seconde jusqu'à ce qu'il soit doré
_, err = io.WriteString(file, data)
if err != nil {
    return err
}
return file.Sync()

```

Voir le code complet [ici dans mon dépôt README](https://github.com/victoriadrake/victoriadrake/blob/master/update/main.go).

Mmmm, ça ne sent pas bon ? ? Faisons en sorte que cela se produise quotidiennement avec une GitHub Action.

## Exécuter votre programme Go selon un calendrier avec Actions

Vous pouvez créer un workflow GitHub Action qui [se déclenche](https://docs.github.com/en/actions/reference/events-that-trigger-workflows) à la fois lors d'un push sur votre branche `master` ainsi que selon un calendrier quotidien. Voici un extrait du `.github/workflows/update.yaml` qui définit cela :

```yaml
on:
  push:
    branches:
      - master
  schedule:
    - cron: '0 11 * * *'

```

Pour exécuter le programme Go qui reconstruit notre README, nous avons d'abord besoin d'une copie de nos fichiers. Nous utilisons `actions/checkout` pour cela :

```yaml
steps:
    - name: ?F4C2 Obtenir une copie de travail
      uses: actions/checkout@master
      with:
        fetch-depth: 1

```

Cette étape exécute notre programme Go :

```yaml
- name: ? Secouer et cuire le README
  run: |
    cd ${GITHUB_WORKSPACE}/update/
    go run main.go

```

Enfin, nous poussons les fichiers mis à jour vers notre dépôt. En savoir plus sur les variables affichées à [Utilisation de variables et de secrets dans un workflow](https://docs.github.com/en/actions/configuring-and-managing-workflows/using-variables-and-secrets-in-a-workflow).

```yaml
- name: ? Déployer
  run: |
    git config user.name "${GITHUB_ACTOR}"
    git config user.email "${GITHUB_ACTOR}@users.noreply.github.com"
    git add .
    git commit -am "Mettre à jour le contenu dynamique"
    git push --all -f https://${{ secrets.GITHUB_TOKEN }}@github.com/${GITHUB_REPOSITORY}.git

```

Voir le code complet de ce workflow d'Action [ici dans mon dépôt README](https://github.com/victoriadrake/victoriadrake/blob/master/.github/workflows/update.yaml).

## Allez de l'avant et mettez à jour automatiquement votre README

Félicitations et bienvenue dans le club des enfants cool ! Vous savez maintenant comment construire un README de profil GitHub à mise à jour automatique. Vous pouvez maintenant aller de l'avant et ajouter toutes sortes d'éléments dynamiques sympas à votre page – allez-y doucement sur les GIF, d'accord ?