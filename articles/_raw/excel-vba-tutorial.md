---
title: Excel VBA Tutorial – How to Write Code in a Spreadsheet Using Visual Basic
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/excel-vba-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/excel-1771393_1920.jpg
tags:
- name: excel
  slug: excel
- name: VBA
  slug: vba
- name: visual basic
  slug: visual-basic
seo_title: null
seo_desc: 'By Chloe Tucker

  Introduction

  This is a tutorial about writing code in Excel spreadsheets using Visual Basic for
  Applications (VBA).

  Excel is one of Microsoft’s most popular products. In 2016, the CEO of Microsoft
  said  "Think about a world without Ex...'
---

By Chloe Tucker

# Introduction

This is a tutorial about writing code in Excel spreadsheets using Visual Basic for Applications (VBA).

Excel is one of Microsoft’s most popular products. In 2016, the CEO of Microsoft said  "Think about a world without Excel. That's just impossible for me.” Well, maybe the world can’t think without Excel.

* In 1996, there were over 30 million users of Microsoft Excel ([source](https://news.microsoft.com/1996/05/20/more-than-30-million-users-make-microsoft-excel-the-worlds-most-popular-spreadsheet-program/)).
* Today, there are an estimated 750 million users of Microsoft Excel. That’s a little more than the population of Europe and 25x more users than there were in 1996.

We’re one big happy family!

In this tutorial, you’ll learn about VBA and how to write code in an Excel spreadsheet using Visual Basic.

### Prerequisites

You don’t need any prior programming experience to understand this tutorial. However, you will need:

* Basic to intermediate familiarity with Microsoft Excel
* If you want to follow along with the VBA examples in this article, you will need access to Microsoft Excel, preferably the latest version (2019) but Excel 2016 and Excel 2013 will work just fine.
* A willingness to try new things

### Learning Objectives

Over the course of this article, you will learn:

1. What VBA is
2. Why you would use VBA
3. How to get set up in Excel to write VBA
4. How to solve some real-world problems with VBA

### Important Concepts

Here are some important concepts that you should be familiar with to fully understand this tutorial.

**Objects**: Excel is object-oriented, which means everything is an object - the Excel window, the workbook, a sheet, a chart, a cell. VBA allows users to manipulate and perform actions with objects in Excel. 

If you don’t have any experience with object-oriented programming and this is a brand new concept, take a second to let that sink in!

**Procedures**: a procedure is a chunk of VBA code, written in the Visual Basic Editor, that accomplishes a task. Sometimes, this is also referred to as a macro (more on macros below). There are two types of procedures:

* Subroutines: a group of VBA statements that performs one or more actions
* Functions: a group of VBA statements that performs one or more actions and <ins>returns one or more values</ins>

Note: you can have functions operating inside of subroutines. You’ll see later.

**Macros**: If you’ve spent any time learning more advanced Excel functionality, you’ve probably encountered the concept of a “macro.” Excel users can record macros, consisting of user commands/keystrokes/clicks, and play them back at lightning speed to accomplish repetitive tasks. Recorded macros generate VBA code, which you can then examine. It’s actually quite fun to record a simple macro and then look at the VBA code.

Please keep in mind that sometimes it may be easier and faster to record a macro rather than hand-code a VBA procedure. 

For example, maybe you work in project management. Once a week, you have to turn a raw exported report from your project management system into a beautifully formatted, clean report for leadership. You need to format the names of the over-budget projects in bold red text. You could record the formatting changes as a macro and run that whenever you need to make the change.

# What is VBA?

Visual Basic for Applications is a programming language developed by Microsoft. Each software program in the Microsoft Office suite is bundled with the VBA language at no extra cost. VBA allows Microsoft Office users to create small programs that operate within Microsoft Office software programs.

Think of VBA like a pizza oven within a restaurant. Excel is the restaurant. The kitchen comes with standard commercial appliances, like large refrigerators, stoves, and regular ole’ ovens - those are all of Excel’s standard features. 

But what if you want to make <ins>wood-fired pizza</ins>? Can’t do that in a standard commercial baking oven. VBA is the pizza oven.

![Pizza in a pizza oven](https://www.freecodecamp.org/news/content/images/2021/11/1-Pizza.jpeg)

Yum.

# Why use VBA in Excel?

Because wood-fired pizza is the best!

But seriously.

A lot of people spend a _lot_ of time in Excel as a part of their jobs. Time in Excel moves differently, too. Depending on the circumstances, 10 minutes in Excel can feel like eternity if you’re not able to do what you need, or 10 hours can go by very quickly if everything is going great. Which is when you should ask yourself, **why on earth am I spending 10 hours in Excel?**

Sometimes, those days are inevitable. But if you’re spending 8-10 hours everyday in Excel doing repetitive tasks, repeating a lot of the same processes, trying to clean up after other users of the file, or even updating other files after changes are made to the Excel file, a VBA procedure just might be the solution for you.

You should consider using VBA if you need to:

* Automate repetitive tasks
* Create easy ways for users to interact with your spreadsheets
* Manipulate large amounts of data

# Getting Set Up to Write VBA in Excel

## Developer Tab

To write VBA, you’ll need to add the Developer tab to the ribbon, so you’ll see the ribbon like this.

![VBA developer tab](https://www.freecodecamp.org/news/content/images/2021/11/2-Developer-Tab.png)

To add the Developer tab to the ribbon:

1. On the File tab, go to Options > Customize Ribbon.
2. Under Customize the Ribbon and under Main Tabs, select the Developer check box.

After you show the tab, the Developer tab stays visible, unless you clear the check box or have to reinstall Excel. [For more information, see Microsoft help documentation.](https://support.office.com/en-us/article/show-the-developer-tab-e1192344-5e56-4d45-931b-e5fd9bea2d45)

## VBA Editor

Navigate to the Developer Tab, and click the Visual Basic button. A new window will pop up - this is the Visual Basic Editor. For the purposes of this tutorial, you just need to be familiar with the Project Explorer pane and the Property Properties pane.

![VBA editor](https://www.freecodecamp.org/news/content/images/2020/06/VBA-Editor.png)

# Excel VBA Examples

First, let’s create a file for us to play around in.

1. Open a new Excel file
2. Save it as a macro-enabled workbook (. xlsm)
3. Select the Developer tab
4. Open the VBA Editor

Let’s rock and roll with some easy examples to get you writing code in a spreadsheet using Visual Basic.

## Example #1: Display a Message when Users Open the Excel Workbook

In the VBA Editor, select Insert -> New Module

Write this code in the Module window (don’t paste!):

Sub Auto_Open()
  MsgBox ("Welcome to the XYZ Workbook.")
End Sub

Save, close the workbook, and reopen the workbook. This dialog should display.

![Welcome to XYZ notebook message example](https://www.freecodecamp.org/news/content/images/2021/11/3-Welcome-to-XYZ-Notebook.png)

Ta da!

### How is it doing that?

Depending on your familiarity with programming, you may have some guesses. It’s not particularly complex, but there’s quite a lot going on:

* Sub (short for “Subroutine): remember from the beginning, “a group of VBA statements that performs one or more actions.”
* Auto_Open: this is the specific subroutine. It automatically runs your code when the Excel file opens - this is the event that triggers the procedure. Auto_Open will only run when the workbook is opened manually; it will not run if the workbook is opened via code from another workbook (Workbook_Open will do that, [learn more about the difference between the two](https://www.pcreview.co.uk/threads/auto_open-vs-workbook_open.953960/ )).
* By default, a subroutine’s access is public. This means any other module can use this subroutine. All examples in this tutorial will be public subroutines. If needed, you can declare subroutines as private. This may be needed in some situations. [Learn more about subroutine access modifiers.](https://www.thespreadsheetguru.com/blog/2014/3/5/explaining-private-vs-public-declarations)
* msgBox: this is a function - a group of VBA statements that performs one or more actions and returns a value. The returned value is the message “Welcome to the XYZ Workbook.”

In short, this is a simple subroutine that contains a function.

### When could I use this?

Maybe you have a very important file that is accessed infrequently (say, once a quarter), but automatically updated daily by another VBA procedure. When it is accessed, it’s by many people in multiple departments, all across the company.

* Problem: Most of the time when users access the file, they are confused about the purpose of this file (why it exists), how it is updated so often, who maintains it, and how they should interact with it. New hires always have tons of questions, and you have to field these questions over and over and over again.
* Solution: create a user message that contains a concise answer to each of these frequently answered questions.

### Real World Examples

* Use the MsgBox function to display a message when there is any event: user closes an Excel workbook, user prints, a new sheet is added to the workbook, etc.
* Use the MsgBox function to display a message when a user needs to fulfill a condition before closing an Excel workbook
* Use the InputBox function to get information from the user

## Example #2: Allow User to Execute another Procedure

In the VBA Editor, select Insert -> New Module

Write this code in the Module window (don’t paste!):				

Sub UserReportQuery()
Dim UserInput As Long
Dim Answer As Integer
UserInput = vbYesNo
Answer = MsgBox("Process the XYZ Report?", UserInput)
If Answer = vbYes Then ProcessReport
End Sub

Sub ProcessReport()
MsgBox ("Thanks for processing the XYZ Report.")
End Sub

Save and navigate back to the Developer tab of Excel and select the “Button” option. Click on a cell and assign the UserReportQuery macro to the button.

Now click the button. This message should display:

![Process the XYZ report message example](https://www.freecodecamp.org/news/content/images/2021/11/4-Process-the-Report.png)

Click “yes” or hit Enter.

![Thanks for processing the XYZ report message example](https://www.freecodecamp.org/news/content/images/2021/11/5-Thanks-for-Processing-the-Report.png)

Once again, tada!

Please note that the secondary subroutine, ProcessReport, could be _anything_. I’ll demonstrate more possibilities in example #3. But first...

### How is it doing that?

This example builds on the previous example and has quite a few new elements. Let’s go over the new stuff:

* Dim UserInput As Long: Dim is short for “dimension” and allows you to declare variable names. In this case, UserInput is the variable name and Long is the data type. In plain English, this line means “Here’s a variable called “UserInput”, and it’s a Long variable type.”
* Dim Answer As Integer: declares another variable called “Answer,” with a data type of Integer. [Learn more about data types here.](https://docs.microsoft.com/en-us/dotnet/visual-basic/language-reference/data-types/)
* UserInput = vbYesNo: assigns a value to the variable. In this case, vbYesNo, which displays Yes and No buttons. There are _many_ button types, [learn more here](https://docs.microsoft.com/en-us/office/vba/language/reference/user-interface-help/msgbox-function).
* Answer = MsgBox(“Process the XYZ Report?”, UserInput): assigns the value of the variable Answer to be a MsgBox function and the UserInput variable. Yes, a variable within a variable.
* If Answer = vbYes Then ProcessReport: this is an “If statement,” a conditional statement, which allows us to say if x is true, then do y. In this case, if the user has selected “Yes,” then execute the ProcessReport subroutine.

### When could I use this?

This could be used in many, many ways. The value and versatility of this functionality is more so defined by what the secondary subroutine does.

For example, maybe you have a file that is used to generate 3 different weekly reports. These reports are formatted in dramatically different ways.

* Problem: Each time one of these reports needs to be generated, a user opens the file and changes formatting and charts; so on and so forth. This file is being edited extensively at least 3 times per week, and it takes at least 30 minutes each time it’s edited.
* Solution: create 1 button per report type, which automatically reformats the necessary components of the reports and generates the necessary charts.

### Real World Examples

* Create a dialog box for user to automatically populate certain information across multiple sheets
* Use the InputBox function to get information from the user, which is then populated across multiple sheets

## Example #3: Add Numbers to a Range with a For-Next Loop

For loops are very useful if you need to perform repetitive tasks on a specific range of values - arrays or cell ranges. In plain English, a loop says “for each x, do y.”

In the VBA Editor, select Insert -> New Module

Write this code in the Module window (don’t paste!):

Sub LoopExample()
Dim X As Integer
For X = 1 To 100
    Range("A" & X).Value = X
Next X
End Sub

Save and navigate back to the Developer tab of Excel and select the Macros button. Run the LoopExample macro.

This should happen:

![For-Next loop results](https://www.freecodecamp.org/news/content/images/2020/06/Screen-Shot-2020-06-01-at-2.53.02-PM.png)

Etc, until the 100th row.

### How is it doing that?

* Dim X As Integer: declares the variable X as a data type of Integer.
* For X = 1 To 100: this is the start of the For loop. Simply put, it tells the loop to keep repeating until X = 100. X is the _counter_. The loop will keep executing until X = 100, execute one last time, and then stop.
* Range("A" & X).Value = X: this declares the range of the loop and what to put in that range. Since X = 1 initially, the first cell will be A1, at which point the loop will put X into that cell.
* Next X: this tells the loop to run again

### When could I use this?

The For-Next loop is one of the most powerful functionalities of VBA; there are numerous potential use cases. This is a more complex example that would require multiple layers of logic, but it communicates the world of possibilities in For-Next loops.

Maybe you have a list of all products sold at your bakery in Column A, the type of product in Column B (cakes, donuts, or muffins), the cost of ingredients in Column C, and the market average cost of each product type in another sheet. 

You need to figure out what should be the retail price of each product. You’re thinking it should be the cost of ingredients plus 20%, but also 1.2% under market average if possible. A For-Next loop would allow you to do this type of calculation.

### Real World Examples

* Use a loop with a nested if statement to add specific values to a separate array only if they meet certain conditions
* Perform mathematical calculations on each value in a range, e.g. calculate additional charges and add them to the value
* Loop through each character in a string and extract all numbers
* Randomly select a number of values from an array

# Conclusion

Now that we’ve talked about pizza and muffins and oh-yeah, how to write VBA code in Excel spreadsheets, let’s do a learning check. See if you can answer these questions.

* What is VBA?
* How do I get set up to start using VBA in Excel?
* Why and when would you use VBA?
* What are some problems I could solve with VBA?

If you have a fair idea of how to you could answer these questions, then this was successful.

Whether you’re an occasional user or a power user, I hope this tutorial provided useful information about what can be accomplished with just a bit of code in your Excel spreadsheets.

Happy coding!

## Learning Resources

* Excel VBA Programming for Dummies, John Walkenbach
* [Get Started with VBA, Microsoft Documentation](https://docs.microsoft.com/en-us/office/vba/library-reference/concepts/getting-started-with-vba-in-office)
* [Learning VBA in Excel, Lynda](https://www.lynda.com/Excel-tutorials/Learning-VBA-Excel/802840-2.html?srchtrk=index%3a5%0alinktypeid%3a2%0aq%3avba%0apage%3a1%0as%3arelevance%0asa%3atrue%0aproducttypeid%3a2)

## A bit about me

I'm Chloe Tucker, an artist and developer in Portland, Oregon. As a former educator, I'm continuously searching for the intersection of learning and teaching, or technology and art. Reach out to me on Twitter [@_chloetucker](https://twitter.com/_chloetucker) and check out my website at [chloe.dev](https://chloe.dev/).

  
  
  

