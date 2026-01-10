---
title: Comment générer un rapport Excel dans une API REST Spring Boot avec Apache
  POI et Kotlin
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-08T01:54:41.000Z'
originalURL: https://freecodecamp.org/news/generate-excel-report-in-spring-rest-api
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/share-1.png
tags:
- name: excel
  slug: excel
- name: Kotlin
  slug: kotlin
- name: REST API
  slug: rest-api
- name: spring-boot
  slug: spring-boot
seo_title: Comment générer un rapport Excel dans une API REST Spring Boot avec Apache
  POI et Kotlin
seo_desc: 'By Piotr Wolak

  In this article, I would like to show you how to generate Excel reports in the .xls
  and .xlsx formats (also known as Open XML) in a Spring Boot REST API with Apache
  POI and Kotlin.

  After finishing this guide, you will have a fundamenta...'
---

Par Piotr Wolak

Dans cet article, je vais vous montrer comment générer des rapports Excel aux formats **.xls** et **.xlsx** (également connus sous le nom d'Open XML) dans une **API REST Spring Boot** avec **Apache POI et Kotlin**.

Après avoir terminé ce guide, vous aurez une compréhension fondamentale de la création de formats de cellules personnalisés, de styles et de polices. Enfin, je vous montrerai comment créer des endpoints REST Spring Boot afin que vous puissiez facilement télécharger les fichiers générés.

Pour mieux visualiser ce que nous allons apprendre, consultez l'aperçu du fichier résultant :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/result_file_preview.png)

## Étape 1 : Ajouter les imports nécessaires

En premier lieu, créons un projet Spring Boot (je recommande vivement d'utiliser la page [Spring Initializr](https://start.spring.io/)) et ajoutons les imports suivants :

```groovy
implementation("org.springframework.boot:spring-boot-starter-web")
implementation("org.apache.poi:poi:4.1.2")
implementation("org.apache.poi:poi-ooxml:4.1.2")
```

Permettez-moi d'expliquer l'utilité de chaque bibliothèque :

* Le **Spring Boot Starter Web** est nécessaire pour créer l'API REST dans notre application.
* **Apache POI** est une bibliothèque Java complexe pour travailler avec des fichiers Excel. Si nous souhaitons travailler uniquement avec le format .xls, alors l'import _poi_ suffirait. Dans notre cas, nous aimerions ajouter la prise en charge du format **.xlsx**, donc le composant _poi-ooxml_ est également nécessaire.

## Étape 2 : Créer les modèles

Ensuite, créons une classe enum appelée **CustomCellStyle** avec 4 constantes :

```kotlin
enum class CustomCellStyle {
    GREY_CENTERED_BOLD_ARIAL_WITH_BORDER,
    RIGHT_ALIGNED,
    RED_BOLD_ARIAL_WITH_BORDER,
    RIGHT_ALIGNED_DATE_FORMAT
}
```

Bien que le but de cette classe enum puisse sembler un peu énigmatique pour le moment, tout deviendra clair dans les sections suivantes.

## Étape 3 : Préparer les styles de cellules

La bibliothèque Apache POI est livrée avec l'interface **CellStyle**, que nous pouvons utiliser pour définir des styles et des formats personnalisés dans les lignes, les colonnes et les cellules.

Créons un composant **StylesGenerator**, qui sera responsable de la préparation d'une map contenant nos styles personnalisés :

```kotlin
@Component
class StylesGenerator {

    fun prepareStyles(wb: Workbook): Map<CustomCellStyle, CellStyle> {
        val boldArial = createBoldArialFont(wb)
        val redBoldArial = createRedBoldArialFont(wb)

        val rightAlignedStyle = createRightAlignedStyle(wb)
        val greyCenteredBoldArialWithBorderStyle =
            createGreyCenteredBoldArialWithBorderStyle(wb, boldArial)
        val redBoldArialWithBorderStyle =
            createRedBoldArialWithBorderStyle(wb, redBoldArial)
        val rightAlignedDateFormatStyle =
            createRightAlignedDateFormatStyle(wb)

        return mapOf(
            CustomCellStyle.RIGHT_ALIGNED to rightAlignedStyle,
            CustomCellStyle.GREY_CENTERED_BOLD_ARIAL_WITH_BORDER to greyCenteredBoldArialWithBorderStyle,
            CustomCellStyle.RED_BOLD_ARIAL_WITH_BORDER to redBoldArialWithBorderStyle,
            CustomCellStyle.RIGHT_ALIGNED_DATE_FORMAT to rightAlignedDateFormatStyle
        )
    }
}
```

Comme vous pouvez le voir, avec cette approche, nous créons chaque style une fois et le plaçons dans une map afin de pouvoir y faire référence plus tard.

Il existe de nombreuses techniques de conception que nous pourrions utiliser ici, mais je pense que l'utilisation d'une map et de constantes enum est l'une des meilleures façons de garder le code plus propre et plus facile à modifier.

Cela dit, ajoutons quelques fonctions manquantes dans la classe du générateur. Commençons d'abord par les polices personnalisées :

```kotlin
private fun createBoldArialFont(wb: Workbook): Font {
    val font = wb.createFont()
    font.fontName = "Arial"
    font.bold = true
    return font
}
```

La fonction **createBoldArialFont** crée une nouvelle instance de police Arial en gras, que nous utiliserons plus tard.

De manière similaire, implémentons une fonction **createRedBoldArialFont** et définissons la couleur de la police sur rouge :

```kotlin
private fun createRedBoldArialFont(wb: Workbook): Font {
    val font = wb.createFont()
    font.fontName = "Arial"
    font.bold = true
    font.color = IndexedColors.RED.index
    return font
}
```

Après cela, nous pouvons ajouter d'autres fonctions responsables de la création d'instances individuelles de **CellStyle** :

```kotlin
private fun createRightAlignedStyle(wb: Workbook): CellStyle {
    val style: CellStyle = wb.createCellStyle()
    style.alignment = HorizontalAlignment.RIGHT
    return style
}

private fun createBorderedStyle(wb: Workbook): CellStyle {
    val thin = BorderStyle.THIN
    val black = IndexedColors.BLACK.getIndex()
    val style = wb.createCellStyle()
    style.borderRight = thin
    style.rightBorderColor = black
    style.borderBottom = thin
    style.bottomBorderColor = black
    style.borderLeft = thin
    style.leftBorderColor = black
    style.borderTop = thin
    style.topBorderColor = black
    return style
}

private fun createGreyCenteredBoldArialWithBorderStyle(wb: Workbook, boldArial: Font): CellStyle {
    val style = createBorderedStyle(wb)
    style.alignment = HorizontalAlignment.CENTER
    style.setFont(boldArial)
    style.fillForegroundColor = IndexedColors.GREY_25_PERCENT.getIndex();
    style.fillPattern = FillPatternType.SOLID_FOREGROUND;
    return style
}

private fun createRedBoldArialWithBorderStyle(wb: Workbook, redBoldArial: Font): CellStyle {
    val style = createBorderedStyle(wb)
    style.setFont(redBoldArial)
    return style
}

private fun createRightAlignedDateFormatStyle(wb: Workbook): CellStyle {
    val style = wb.createCellStyle()
    style.alignment = HorizontalAlignment.RIGHT
    style.dataFormat = 14
    return style
}
```

Veuillez noter que les exemples ci-dessus ne représentent qu'une petite partie des possibilités de **CellStyle**. Si vous souhaitez voir la liste complète, veuillez consulter la documentation officielle [ici](https://poi.apache.org/apidocs/dev/org/apache/poi/ss/usermodel/CellStyle.html).

## **Étape 4 : Créer la classe ReportService**

Ensuite, implémentons une classe **ReportService** responsable de la création de fichiers .xlsx et **.xls** et de leur retour sous forme d'instances ByteArray :

```kotlin
@Service
class ReportService(
    private val stylesGenerator: StylesGenerator
) {
    fun generateXlsxReport(): ByteArray {
        val wb = XSSFWorkbook()

        return generateReport(wb)
    }

    fun generateXlsReport(): ByteArray {
        val wb = HSSFWorkbook()

        return generateReport(wb)
    }
}
```

Comme vous pouvez le voir, la seule différence entre la génération de ces deux formats est le type d'implémentation de **Workbook** que nous avons utilisé. Pour le format .xlsx, nous utiliserons la classe **XSSFWorkbook**, et pour le .xls, nous utiliserons **HSSFWorkbook**.

Ajoutons le reste du code à **ReportService** :

```kotlin
private fun generateReport(wb: Workbook): ByteArray {
    val styles = stylesGenerator.prepareStyles(wb)
    val sheet: Sheet = wb.createSheet("Nom de la feuille d'exemple")

    setColumnsWidth(sheet)

    createHeaderRow(sheet, styles)
    createStringsRow(sheet, styles)
    createDoublesRow(sheet, styles)
    createDatesRow(sheet, styles)

    val out = ByteArrayOutputStream()
    wb.write(out)

    out.close()
    wb.close()

    return out.toByteArray()
}

private fun setColumnsWidth(sheet: Sheet) {
    sheet.setColumnWidth(0, 256 * 20)

    for (columnIndex in 1 until 5) {
        sheet.setColumnWidth(columnIndex, 256 * 15)
    }
}

private fun createHeaderRow(sheet: Sheet, styles: Map<CustomCellStyle, CellStyle>) {
    val row = sheet.createRow(0)

    for (columnNumber in 1 until 5) {
        val cell = row.createCell(columnNumber)

        cell.setCellValue("Colonne $columnNumber")
        cell.cellStyle = styles[CustomCellStyle.GREY_CENTERED_BOLD_ARIAL_WITH_BORDER]
    }
}

private fun createRowLabelCell(row: Row, styles: Map<CustomCellStyle, CellStyle>, label: String) {
    val rowLabel = row.createCell(0)
    rowLabel.setCellValue(label)
    rowLabel.cellStyle = styles[CustomCellStyle.RED_BOLD_ARIAL_WITH_BORDER]
}

private fun createStringsRow(sheet: Sheet, styles: Map<CustomCellStyle, CellStyle>) {
    val row = sheet.createRow(1)
    createRowLabelCell(row, styles, "Ligne de chaînes")

    for (columnNumber in 1 until 5) {
        val cell = row.createCell(columnNumber)

        cell.setCellValue("Chaîne $columnNumber")
        cell.cellStyle = styles[CustomCellStyle.RIGHT_ALIGNED]
    }
}

private fun createDoublesRow(sheet: Sheet, styles: Map<CustomCellStyle, CellStyle>) {
    val row = sheet.createRow(2)
    createRowLabelCell(row, styles, "Ligne de doubles")

    for (columnNumber in 1 until 5) {
        val cell = row.createCell(columnNumber)

        cell.setCellValue(BigDecimal("${columnNumber}.99").toDouble())
        cell.cellStyle = styles[CustomCellStyle.RIGHT_ALIGNED]
    }
}

private fun createDatesRow(sheet: Sheet, styles: Map<CustomCellStyle, CellStyle>) {
    val row = sheet.createRow(3)
    createRowLabelCell(row, styles, "Ligne de dates")

    for (columnNumber in 1 until 5) {
        val cell = row.createCell(columnNumber)

        cell.setCellValue((LocalDate.now()))
        cell.cellStyle = styles[CustomCellStyle.RIGHT_ALIGNED_DATE_FORMAT]
    }
}
```

Comme vous pouvez le voir, la première chose que fait la fonction **generateReport** est d'initialiser les styles. Nous passons l'instance **Workbook** à **StylesGenerator** et en retour, nous obtenons une map, que nous utiliserons plus tard pour obtenir les CellStyles appropriés.

Après cela, elle crée une nouvelle feuille dans notre classeur et lui passe un nom.

Ensuite, elle invoque des fonctions responsables de la définition des largeurs des colonnes et de l'opération sur notre feuille ligne par ligne.

Enfin, elle écrit notre classeur dans un ByteArrayOutputStream.

Prenons un moment pour analyser ce que fait exactement chaque fonction :

```kotlin
private fun setColumnsWidth(sheet: Sheet) {
    sheet.setColumnWidth(0, 256 * 20)

    for (columnIndex in 1 until 5) {
        sheet.setColumnWidth(columnIndex, 256 * 15)
    }
}
```

Comme son nom l'indique, **setColumnsWidth** est responsable de la définition des largeurs des colonnes dans notre feuille. Le premier paramètre passé à **setColumnWidth** indique l'index de la colonne, tandis que le second définit la largeur (en unités de 1/256ème de la largeur d'un caractère).

```kotlin
private fun createRowLabelCell(row: Row, styles: Map<CustomCellStyle, CellStyle>, label: String) {
    val rowLabel = row.createCell(0)
    rowLabel.setCellValue(label)
    rowLabel.cellStyle = styles[CustomCellStyle.RED_BOLD_ARIAL_WITH_BORDER]
}
```

La fonction **createRowLabelCell** est responsable de l'ajout d'une cellule dans la première colonne de la ligne passée, tout en définissant sa valeur sur l'étiquette spécifiée et en définissant le style. J'ai décidé d'ajouter cette fonction pour réduire légèrement la redondance du code.

Toutes les fonctions ci-dessous sont assez similaires. Leur but est de créer une nouvelle ligne, en invoquant la fonction **createRowLabelCell** (sauf pour **createHeaderRow**) et en ajoutant cinq colonnes avec des données à notre feuille.

```kotlin
private fun createHeaderRow(sheet: Sheet, styles: Map<CustomCellStyle, CellStyle>) {
    val row = sheet.createRow(0)

    for (columnNumber in 1 until 5) {
        val cell = row.createCell(columnNumber)

        cell.setCellValue("Colonne $columnNumber")
        cell.cellStyle = styles[CustomCellStyle.GREY_CENTERED_BOLD_ARIAL_WITH_BORDER]
    }
}
```

```kotlin
private fun createStringsRow(sheet: Sheet, styles: Map<CustomCellStyle, CellStyle>) {
    val row = sheet.createRow(1)
    createRowLabelCell(row, styles, "Ligne de chaînes")

    for (columnNumber in 1 until 5) {
        val cell = row.createCell(columnNumber)

        cell.setCellValue("Chaîne $columnNumber")
        cell.cellStyle = styles[CustomCellStyle.RIGHT_ALIGNED]
    }
}
```

```kotlin
private fun createDoublesRow(sheet: Sheet, styles: Map<CustomCellStyle, CellStyle>) {
    val row = sheet.createRow(2)
    createRowLabelCell(row, styles, "Ligne de doubles")

    for (columnNumber in 1 until 5) {
        val cell = row.createCell(columnNumber)

        cell.setCellValue(BigDecimal("${columnNumber}.99").toDouble())
        cell.cellStyle = styles[CustomCellStyle.RIGHT_ALIGNED]
    }
}
```

```kotlin
private fun createDatesRow(sheet: Sheet, styles: Map<CustomCellStyle, CellStyle>) {
    val row = sheet.createRow(3)
    createRowLabelCell(row, styles, "Ligne de dates")

    for (columnNumber in 1 until 5) {
        val cell = row.createCell(columnNumber)

        cell.setCellValue((LocalDate.now()))
        cell.cellStyle = styles[CustomCellStyle.RIGHT_ALIGNED_DATE_FORMAT]
    }
}
```

## **Étape 5 : Implémenter le ReportController REST**

En dernière étape, nous allons implémenter une classe nommée **ReportController**. Elle sera responsable de la gestion des requêtes POST arrivant à nos deux endpoints REST :

* _/api/report/xlsx_ - création d'un rapport au format _.xlsx_ 
* _/api/report/xls_ - même chose que ci-dessus, mais au format .xls

```kotlin
@RestController
@RequestMapping("/api/report")
class ReportController(
    private val reportService: ReportService
) {

    @PostMapping("/xlsx")
    fun generateXlsxReport(): ResponseEntity<ByteArray> {
        val report = reportService.generateXlsxReport()

        return createResponseEntity(report, "report.xlsx")
    }

    @PostMapping("/xls")
    fun generateXlsReport(): ResponseEntity<ByteArray> {
        val report = reportService.generateXlsReport()

        return createResponseEntity(report, "report.xls")
    }

    private fun createResponseEntity(
        report: ByteArray,
        fileName: String
    ): ResponseEntity<ByteArray> =
        ResponseEntity.ok()
            .contentType(MediaType.APPLICATION_OCTET_STREAM)
            .header(HttpHeaders.CONTENT_DISPOSITION, "attachment; filename=\"$fileName\"")
            .body(report)

}
```

La partie la plus intéressante du code ci-dessus est la fonction **createResponseEntity**, qui définit le ByteArray passé avec son rapport généré comme corps de la réponse.

De plus, nous définissons l'en-tête **Content-Type** de la réponse comme **application/octet-stream**, et le Content-Disposition comme **attachment; filename=<FILENAME>**.

## **Étape 6 : Tout tester avec Postman**

Enfin, nous pouvons exécuter et tester notre application Spring Boot, par exemple avec la commande `gradlew` :

```
./gradlew bootRun
```

Par défaut, l'application Spring Boot s'exécutera sur le port 8080, alors ouvrons [Postman](https://www.postman.com/) (ou tout autre outil), spécifions la requête **POST** vers **localhost:8080/api/report/xls** et cliquons sur le bouton **Send and Download** :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/POST_xls.png)

Si tout s'est bien passé, nous devrions voir une fenêtre nous permettant d'enregistrer le fichier **.xls**.

De manière similaire, testons le deuxième endpoint :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/POST_xlsx.png)

Cette fois, l'extension du fichier devrait être .xlsx.

## **Résumé**

C'est tout pour cet article ! Nous avons couvert le processus de génération de rapports Excel dans une API REST Spring Boot avec Apache POI et Kotlin.

Si vous avez apprécié et que vous aimeriez apprendre d'autres sujets à travers des articles similaires, veuillez visiter mon blog, [**Codersee**](https://codersee.com/).

Et une dernière chose : pour le code source d'un projet entièrement fonctionnel, veuillez consulter [ce dépôt GitHub](https://github.com/codersee-blog/freecodecamp-spring-boot-kotlin-excel).