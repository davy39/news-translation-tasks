---
title: How to Generate an Excel Report in a Spring Boot REST API with Apache POI and
  Kotlin
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
seo_title: null
seo_desc: 'By Piotr Wolak

  In this article, I would like to show you how to generate Excel reports in the .xls
  and .xlsx formats (also known as Open XML) in a Spring Boot REST API with Apache
  POI and Kotlin.

  After finishing this guide, you will have a fundamenta...'
---

By Piotr Wolak

In this article, I would like to show you how to generate Excel reports in the **.xls** and **.xlsx** formats (also known as Open XML) in a **Spring Boot REST API** with **Apache POI and Kotlin**.

After finishing this guide, you will have a fundamental understanding of how to create custom cells formats, styles, and fonts. In the end, I will show you how to create Spring Boot REST endpoints so you can easily download generated files.

To better visualize what we'll learn, check out the preview of the resulting file:

![Image](https://www.freecodecamp.org/news/content/images/2020/12/result_file_preview.png)

## Step 1: Add the Necessary Imports

As the first step, let's create a Spring Boot project (I highly recommend using the [Spring Initializr](https://start.spring.io/) page) and add the following imports:

```groovy
implementation("org.springframework.boot:spring-boot-starter-web")
implementation("org.apache.poi:poi:4.1.2")
implementation("org.apache.poi:poi-ooxml:4.1.2")
```

Let me explain the purpose of each library: 

* The **Spring Boot Starter Web** is necessary to create the REST API in our application.
* The **Apache POI** is a complex Java library for working with Excel files. If we would like to work only with the .xls format, then the _poi_ import would be enough. In our case, we would like to add the support for the **.xlsx** format, so the _poi-ooxml_ component is necessary as well.

## Step 2: Create the Models

As the next step, let's create an enum class called **CustomCellStyle** with 4 constants: 

```kotlin
enum class CustomCellStyle {
    GREY_CENTERED_BOLD_ARIAL_WITH_BORDER,
    RIGHT_ALIGNED,
    RED_BOLD_ARIAL_WITH_BORDER,
    RIGHT_ALIGNED_DATE_FORMAT
}
```

Although the purpose of this enum class might seem a bit enigmatic at the moment, it will all become clear in the next sections.

## Step 3: Prepare Cells Styles

The Apache POI library comes with the **CellStyle** interface, which we can use to define custom styling and formatting within rows, columns, and cells.

Let's create a **StylesGenerator** component, which will be responsible for preparing a map containing our custom styles:

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

As you can see, with this approach, we create each style once and put it inside a map so that we will be able to refer to it later. 

There are plenty of design techniques which we could use here, but I believe using a map and enum constants is one of the best ways to keep the code cleaner and easier to modify.

With that being said, let's add some missing functions inside the generator class. Let's start with custom fonts first:

```kotlin
private fun createBoldArialFont(wb: Workbook): Font {
    val font = wb.createFont()
    font.fontName = "Arial"
    font.bold = true
    return font
}
```

The **createBoldArialFont** function creates a new bold Arial Font instance, which we will use later. 

Similarly, let's implement a **createRedBoldArialFont** function and set the font color to red: 

```kotlin
private fun createRedBoldArialFont(wb: Workbook): Font {
    val font = wb.createFont()
    font.fontName = "Arial"
    font.bold = true
    font.color = IndexedColors.RED.index
    return font
}
```

After that, we can add other functions responsible for creating individual **CellStyle** instances: 

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

Please keep in mind that the above examples represent only a small part of **CellStyle's** possibilities. If you would like to see the full list, please refer to the official documentation [here](https://poi.apache.org/apidocs/dev/org/apache/poi/ss/usermodel/CellStyle.html).

## **Step 4: Create the ReportService Class**

As the next step, let's implement a **ReportService** class responsible for creating .xlsx and **.xls** files and returning them as ByteArray instances:

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

As you can see, the only difference between these two formats' generation is the type of **Workbook** implementation we've. used. For the .xlsx format we will use the **XSSFWorkbook** class, and for the .xls we will use **HSSFWorkbook**_._

Let's add the rest of the code to the **ReportService**:

```kotlin
private fun generateReport(wb: Workbook): ByteArray {
    val styles = stylesGenerator.prepareStyles(wb)
    val sheet: Sheet = wb.createSheet("Example sheet name")

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

        cell.setCellValue("Column $columnNumber")
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
    createRowLabelCell(row, styles, "Strings row")

    for (columnNumber in 1 until 5) {
        val cell = row.createCell(columnNumber)

        cell.setCellValue("String $columnNumber")
        cell.cellStyle = styles[CustomCellStyle.RIGHT_ALIGNED]
    }
}

private fun createDoublesRow(sheet: Sheet, styles: Map<CustomCellStyle, CellStyle>) {
    val row = sheet.createRow(2)
    createRowLabelCell(row, styles, "Doubles row")

    for (columnNumber in 1 until 5) {
        val cell = row.createCell(columnNumber)

        cell.setCellValue(BigDecimal("${columnNumber}.99").toDouble())
        cell.cellStyle = styles[CustomCellStyle.RIGHT_ALIGNED]
    }
}

private fun createDatesRow(sheet: Sheet, styles: Map<CustomCellStyle, CellStyle>) {
    val row = sheet.createRow(3)
    createRowLabelCell(row, styles, "Dates row")

    for (columnNumber in 1 until 5) {
        val cell = row.createCell(columnNumber)

        cell.setCellValue((LocalDate.now()))
        cell.cellStyle = styles[CustomCellStyle.RIGHT_ALIGNED_DATE_FORMAT]
    }
}
```

As you can see, the first thing the **generateReport** function does is that it styles the initialization. We pass the **Workbook** instance to the **StylesGenerator** and in return, we get a map, which we will use later to obtain appropriate CellStyles. 

After that, it creates a new sheet within our workbook and passes a name for it. 

Then, it invokes functions responsible for setting the columns' widths and operating on our sheet row by row. 

Finally, it writes out our workbook to a ByteArrayOutputStream.

Let's take a minute and analyze what exactly each function does:

```kotlin
private fun setColumnsWidth(sheet: Sheet) {
    sheet.setColumnWidth(0, 256 * 20)

    for (columnIndex in 1 until 5) {
        sheet.setColumnWidth(columnIndex, 256 * 15)
    }
}
```

As the name suggests, **setColumnsWidth** is responsible for setting widths of columns in our sheet. The first parameter passed to the **setColumnWidth** indicates the columnIndex, whereas the second one sets the width (in units of 1/256th of a character width). 

```kotlin
private fun createRowLabelCell(row: Row, styles: Map<CustomCellStyle, CellStyle>, label: String) {
    val rowLabel = row.createCell(0)
    rowLabel.setCellValue(label)
    rowLabel.cellStyle = styles[CustomCellStyle.RED_BOLD_ARIAL_WITH_BORDER]
}
```

The **createRowLabelCell** function is responsible for adding a cell in the first column of the passed row, alongside setting its value to the specified label and setting the style. I've decided to add this function to slightly reduce the code's redundancy.

All of the below functions are pretty similar. Their purpose is to create a new row, invoking the **createRowLabelCell** function (except for **createHeaderRow**) and adding five columns with data to our sheet.

```kotlin
private fun createHeaderRow(sheet: Sheet, styles: Map<CustomCellStyle, CellStyle>) {
    val row = sheet.createRow(0)

    for (columnNumber in 1 until 5) {
        val cell = row.createCell(columnNumber)

        cell.setCellValue("Column $columnNumber")
        cell.cellStyle = styles[CustomCellStyle.GREY_CENTERED_BOLD_ARIAL_WITH_BORDER]
    }
}
```

```kotlin
private fun createStringsRow(sheet: Sheet, styles: Map<CustomCellStyle, CellStyle>) {
    val row = sheet.createRow(1)
    createRowLabelCell(row, styles, "Strings row")

    for (columnNumber in 1 until 5) {
        val cell = row.createCell(columnNumber)

        cell.setCellValue("String $columnNumber")
        cell.cellStyle = styles[CustomCellStyle.RIGHT_ALIGNED]
    }
}
```

```kotlin
private fun createDoublesRow(sheet: Sheet, styles: Map<CustomCellStyle, CellStyle>) {
    val row = sheet.createRow(2)
    createRowLabelCell(row, styles, "Doubles row")

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
    createRowLabelCell(row, styles, "Dates row")

    for (columnNumber in 1 until 5) {
        val cell = row.createCell(columnNumber)

        cell.setCellValue((LocalDate.now()))
        cell.cellStyle = styles[CustomCellStyle.RIGHT_ALIGNED_DATE_FORMAT]
    }
}
```

## **Step 5: Implement the REST ReportController**

As the last step, we will implement a class named **ReportController**. It will be responsible for handling POST requests coming to our two REST endpoints:

* _/api/report/xlsx -_ creating a report in a _.xlsx_ format 
* _/api/report/xls_ - same as above, but in a .xls format

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

The most interesting part of the above code is the **createResponseEntity** function, which sets the passed ByteArray with its generated report as a response body. 

Additionally, we set the **Content-Type** header of the response as the **application/octet-stream**, and the Content-Disposition as the **attachment; filename=<FILENAME>**.

## **Step 6: Test Everything With Postman**

Finally, we can run and test our Spring Boot application, for instance with the `gradlew` command:

```
./gradlew bootRun
```

By default, the Spring Boot application will be running on port 8080, so let's open up [Postman](https://www.postman.com/) (or any other tool), specify the **POST** request to **localhost:8080/api/report/xls** and hit **Send and Download** button: 

![Image](https://www.freecodecamp.org/news/content/images/2020/12/POST_xls.png)

If everything went well, we should see a window allowing us to save the **.xls** file. 

Similarly, let's test the second endpoint:

![Image](https://www.freecodecamp.org/news/content/images/2020/12/POST_xlsx.png)

This time, the file extension should be .xlsx.

## **Summary**

That's all for this article! We've covered the process of generating Excel reports in a Spring Boot REST API with Apache POI and Kotlin.

If you enjoyed it and would like to learn other topics through similar articles, please visit my blog, [**Codersee**](https://codersee.com/).

And the last thing: for the source code of a fully working project, please refer to [this GitHub repository](https://github.com/codersee-blog/freecodecamp-spring-boot-kotlin-excel).


