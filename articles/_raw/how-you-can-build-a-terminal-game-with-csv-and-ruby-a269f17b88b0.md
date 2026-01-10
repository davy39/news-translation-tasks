---
title: How you can build a terminal game with CSV and Ruby
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-24T17:57:39.000Z'
originalURL: https://freecodecamp.org/news/how-you-can-build-a-terminal-game-with-csv-and-ruby-a269f17b88b0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*CsSq6749MEFgk7jBOHroEg.gif
tags:
- name: Data Science
  slug: data-science
- name: Games
  slug: games
- name: General Programming
  slug: programming
- name: Ruby
  slug: ruby
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Andrew Bales

  In this article, you’ll learn how to build a terminal game with a CSV and a few
  Ruby gems! See a demo in the video above, and find the code on GitHub.

  This project comes from a lecture I gave at Ada Developers Academy in Seattle. The
  ...'
---

By Andrew Bales

In this article, you’ll learn how to build a terminal game with a CSV and a few Ruby gems! See a demo in the video above, and find the code on [GitHub](https://github.com/agbales/solar-system).

This project comes from a lecture I gave at [Ada Developers Academy](https://www.adadevelopersacademy.org) in Seattle. The topic was the Ruby CSV library, and I wanted a fun way to illustrate its methods and potential.

In class, we discussed how most people use programs like Excel to create and edit CSVs. They make updates by clicking cells and changing values. But the question for us became: what can we do with a CSV if we approach it as **programmers**? Using a programming language like Ruby, how can you open, read, and manipulate those values? Can those orderly rows and columns become a database for an application?

This article covers those questions in three sections:

1. Comma-separated values
2. Ruby’s CSV library: creating, opening, appending, using headers
3. Building the game

### Comma-Separated Values

CSV stands for comma-separated values, and that’s exactly what it sounds like. If you’ve ever opened one of these files in a program like Excel, you’ve seen these values rendered in a spreadsheet.

However, if you were to open that same file in a text editor like Atom or Sublime, you’d find a series of — you guessed it — comma-separated values. As you see below, Excel uses those raw values to render a user-friendly table.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wrExasjrLVB2AOvKDG_TAQ.jpeg)

### Quick Setup

It’s easiest to follow along if you download this [GitHub repository](https://github.com/agbales/solar-system). Once you’ve done that, navigate to that folder in your terminal. This repo includes **all** of the examples below, so please know that you’ll need to comment out sections that you don’t want to run.

Also, you’ll want to install [Awesome Print](https://github.com/awesome-print/awesome_print), which beautifies terminal output:

```
gem install awesome_print
```

### Ruby’s CSV Library

Ruby comes with a [CSV library](http://ruby-doc.org/stdlib-2.0.0/libdoc/csv/rdoc/CSV.html) that allows us to open, read, and manipulate CSV files.

#### **Creating a CSV**

Let’s start by making our own CSV. In the Github repo, you’ll find planets.rb. This file begins by setting the variable planets equal to a two-dimensional array (an array of arrays).

In each, we have planet attributes: id, name, mass, and distance. We’ve assigned the attribute names to the headers variable as another array.

```
require 'csv'require 'awesome_print'
```

```
planets = [  [1, "Mercury", 0.055, 0.4],  [2, "Venus", 0.815, 0.7],  [3, "Earth", 1.0, 1.0],  [4, "Mars", 0.107, 1.5]]headers = ["id", "name", "mass", "distance"]CSV.open("planet_data.csv", "w") do |file|  file << headers  planets.each do |planet|    file << planet  endend
```

Above, CSV.open accepts up to three arguments:

```
CSV.open(file name, mode, options)
```

We have given it a file name (planet_data.csv). Because we have also given the mode of “w” (Write-only), it creates a new file for us even if it didn’t exist already. No options were passed in this time.

The following block does a few things:

1. It adds the headers array to the file we’ve created. This creates a single row with four columns — each with a string entry of the property name.
2. We use planets.each to iterate through the planet array (filled with info about its id, name, and so on) and append each entry as an individual row.

If you run this bit of code, you’ll find the following CSV has been created:

![Image](https://cdn-media-1.freecodecamp.org/images/1*4-WNK1cd7_0AQ_0yKVeNWg.png)

#### Modes

Above, we used “w” as our mode to write a new file. You have a number of other options available to you, depending on the task at hand. The biggest factors to consider are if you want to read and/or write, and where in the CSV you’d like to start your work.

For instance, if you are using the file to populate your website with listings, “r” (read-only) would be an appropriate mode. If you want to add new planets to your CSV, the “a” mode (append read-write) would begin at the end of the file and immediately let you append those rows.

Here’s a complete list of modes:

```
“r”  Read-only, starts at beginning of file (default mode).“r+” Read-write, starts at beginning of file.“w”  Write-only, truncates existing file to zero length.“w+” Read-write, truncates existing file to zero length.“a”  Append write-only, starts at end of file if file exists.“a+” Append read-write, starts at end of file if file exists.“b”  Binary file mode.“t”  Text file mode.
```

#### **Appending**

We can append a new planet to planet_data.csv like this:

```
CSV.open("planet_data.csv", "a") do |file|  file << [5, "Jupiter", 1234, 3321]end
```

In the mode list above, “a” is “write-only” and “starts at end of file.” So Jupiter’s information will be inserted at the end of the existing CSV.

#### Iterating

Because .open with the “r” mode will return an array of arrays, we can use .each to iterate over the rows. The code below will print every row of the CSV in the terminal.

```
CSV.open("planet_data.csv", "r").each do |row|  ap rowend
```

You can take this a step further to create interpolated sentences!

```
CSV.open("planet_data.csv", "r").each do |row|  ap "#{row[1]} has a mass of #{row[2]} and distance of #{row[3]}."end
```

This is great, but it could be a bit better. We’re having to use indices (1, 2, 3) to access the data. This is prone to errors and generally no fun. Next, we’ll see how to fix this by passing in options.

#### Using Headers

When you add in the option for headers to be true, you’ll get back a new CSV::Table object.

```
csv_with_headers = CSV.open("planet_data.csv", "r", headers: true, header_converters: :symbol)csv_with_headers.each do |row|  ap rowend
```

Reading with headers and converting those headers to symbols, we will get back a unique object: an array of hashes. That means it’s possible to iterate through each row as we did before, but then we can also use the symbols in the hash to isolate key data.

If we return to the sentence example, it becomes:

```
CSV.open("planet_data.csv", "r", headers: true, header_converters: :symbol).each do |row|  ap "#{row[:name]} has a mass of #{row[:mass]} and distance of #{row[:distance]}."end
```

That’s much more readable than the number indices we used before!

When headers are set to true, the library gives us the CSV::Table object, which also gives us access to some handy methods. Below, .read is synonymous with .open in the “r” mode:

```
csv = CSV.read("planet_data.csv", headers: true, header_converters: :symbol)ap csv               # <CSV::Table mode:col_or_row row_count:6>ap csv.headers       # Returns an array of headersap csv.by_col[:id]   # Array of id column dataap csv.by_col[:name] # Array of name column dataap csv.by_row[0]     # Entire row at 0 (or any position)ap csv[:name][3]     # Name of the 3rd entry => "Mars"ap csv[3][:name]     # 3rd row's name => "Mars"
```

### Building a Solar System Game!

We know how to open and use data in a CSV file with Ruby, so let’s put those methods to work to make a solar system game.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CsSq6749MEFgk7jBOHroEg.gif)
_Via [SUPERNOVA](https://imahimesama.tumblr.com/post/164924479335" rel="noopener" target="_blank" title=")_

#### **Setup**

You’ll need to install Catpix and Launchy. Catpix allows illustrations in the terminal and Launchy lets us to control a browser window. In the terminal:

```
gem install catpix gem install launchy 
```

#### **CSV as a Database**

You may want to open “Solar System.csv” in Excel to visually get a sense of the attributes for each entry. Once you’re comfortable with the data, we’ll use Ruby to read the CSV file and assign it to a global variable ($solar_system_data). This will serve as our database.

As the game opens, we welcome the user TO THE SOLAR SYSTEM! and create that database like so:

```
require 'catpix'require 'launchy'$solar_system_data = CSV.read("Solar System.csv", headers: true, header_converters: :symbol)
```

```
ap "WELCOME TO THE SOLAR SYSTEM!"
```

The game really starts up when we call the method explore_planet. That method contains this code:

```
ap $solar_system_data.by_col[:name]prompt = "Where would you like to start? 0 - #{$solar_system_data.length}"
```

```
ap promptinput = gets.chomp
```

```
until $selected_planet && /\d/.match(input)  ap prompt  input = gets.chomp  $selected_planet = $solar_system_data[input.to_i]end
```

```
ap $selected_planet
```

Above, the terminal prints all of the names from the “name” column. It then asks the user select an entry between the first (0-index) to the last (our data length). This is a good point to pause to consider the following:

**Question:** If we’ve used headers in order to get a hash, how can solar_system_data.length == 14?

**Answer:** This CSV::Table may **look** like a hash, but it’s actually an array of hashes. Therefore, it has a length and we can iterate through each hash. To select the correct record, we just need to convert the input from a string to an integer (.to_i)

You’ll also see that we used an until statement. This validates the selection — requesting a response until the user gives us a valid number. Once a proper selection is made, the terminal prints out the planet info.

The user can then pick if they want to LEARN about or SEE the planet:

```
prompt = "Do you want to LEARN or SEE?"ap prompt
```

```
while input = gets.chomp  case input.downcase  when "learn"    Launchy.open($selected_planet[:uri])    return  when "see"    Catpix::print_image $selected_planet[:image]    return  else    ap prompt  endend
```

Similar to before, a while statement is used to make sure we get a valid entry. This time, it either uses Launchy to open the associated URI for the planet or prints the image in the terminal with Catpix.

The game has one more piece of functionality. This is held in the select_attribute method. We use the CSV methods we’ve just covered to return specific attributes for **every** planet in our database.

```
ap "Which attribute do want to see for each planet (ex: number_of_moons)?"
```

```
ap $solar_system_data.headers.to_sattribute = gets.chomp
```

```
ap "Here are the #{attribute} findings:"
```

```
$solar_system_data.each do |row|  ap "#{row[:name]} --> #{attribute}: #{row[attribute.to_sym]}"end
```

First, we print out all of the headers as strings. This gives the user a list of attributes to pick from. With the user response, we can list out the planet name along with the attribute requested and its value.

Finally, they can SELECT another attribute or start over and EXPLORE individual planets:

```
prompt = "SELECT another attribute or EXPLORE another planet?"ap prompt
```

```
while input = gets.chomp  case input.downcase  when "select"    select_attribute()  when "explore"    explore_planet()  else    ap prompt  endend
```

I hope this helps clarify CSV methods and gets you excited to make your own games.

If you expand on this one or design something new, leave a comment. I’d love to see what you come up with!

