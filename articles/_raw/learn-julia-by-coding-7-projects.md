---
title: Learn Julia by Coding 7 Projects – Hands-On Programming Tutorial
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-10-28T23:54:26.000Z'
originalURL: https://freecodecamp.org/news/learn-julia-by-coding-7-projects
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/7-projects-1.png
tags:
- name: Julia
  slug: julia
- name: Julialang
  slug: julialang
- name: projects
  slug: projects
seo_title: null
seo_desc: "By Logan Kilpatrick\nThe Julia programming language is used for a lot of\
  \ really impactful and interesting challenges like Machine Learning and Data Science.\
  \ \nBut before you can get to the complex stuff, it is worth exploring the basics\
  \ to develop a so..."
---

By Logan Kilpatrick

The Julia programming language is used for a lot of really impactful and interesting challenges like Machine Learning and Data Science. 

But before you can get to the complex stuff, it is worth exploring the basics to develop a solid foundation. 

In this tutorial, we will go over some of the basics of Julia by building 7 small Julia projects:

* Mad Libs ✍️
* Guess the Number Game 💯
* Computer Number Guesser 🤖
* Rock 🗿, Paper 📃, Scissors ✂️
* Password Generator 🎫
* Dice Rolling Simulator 🎲
* Countdown Timer ⏱️

If you have not downloaded Julia yet, head to: [https://julialang.org/downloads/](https://julialang.org/downloads/) or watch this video:

%[https://www.youtube.com/watch?v=t67TGcf4SmM]

It's also worth noting that if you are totally new to Julia and want a comprehensive introduction to the language, you can [check out this freeCodeCamp article](https://www.freecodecamp.org/news/learn-julia-programming-language/).

## Beginner-Friendly Julia Projects

### How to Build Mad Libs in Julia ✍️

In Mad Libs, the user is prompted to enter different types of words. The random words the user enters are then inserted into a sentence. This leads to some pretty wacky and funny outcomes. Let's try to program a simple version of this using Julia.

At the core of this problem, we want to concatenate (or add together) multiple strings so that we go from a sentence with some placeholders, to a sentence with the user input. 

The simplest way to achieve this in Julia is with String Interpolation:

```julia
julia> name = "Logan"
"Logan"

julia> new_string = "Hello, my name is $name"
"Hello, my name is Logan"
```

Here we can see that we can insert the name variable we defined into the string by using the `$name` syntax.

There are a bunch of other ways to do this, like using the `string` function:

```julia
julia> new_string = string("Hello, my name is ", name)
"Hello, my name is Logan"

```

but string interpolation seems the most straightforward and readable in this case.

Now that we know how we are going to set up the strings, we need to prompt the user for their input. 

To do this, we can use the `readline` function as follows:

```julia
julia> my_name = readline()
Logan
"Logan"
```

The `readline` function takes a single line of input from the user. This is exactly what we will want to use. Let’s put it all together into a simple example:

```julia
function play_mad_libs()

    print("Enter a verb (action): ")
    verb1 = readline()

    print("Enter an adjective (descriptive word): ")
    adj1 = readline()

    print("Enter a noun (person place or thing): ")
    noun1 = readline()

    print("Enter another noun (person place or thing): ")
    noun2 = readline()

    print("Enter a catchphrase (something like 'hands up!'): ")
    phrase1 = readline()
    
    base_sentence = "John $verb1 down the street one night, playing with his $adj1 $noun1. When all of a / sudden, a $noun2 jumped out at him and said $phrase1"
    
    print("\n\n", base_sentence)
end

# Link to source code: https://github.com/logankilpatrick/Julia-Projects-for-Beginners/blob/main/madlibs.jl
```

In this example, we learned how to work with strings, define a function, use print statements, and more! 

As noted before, there are lots of other ways to do the same things we did above. So if you want to find out more about working with strings, [check out the Julia docs here](https://docs.julialang.org/en/v1/manual/strings/).

### How to Build a Guess the Number Game in Julia 💯

In this game, we will have to generate a random number and then try to guess what it is. 

To begin, we will need to generate a random number. As always, there are many ways to do something like this but the most straightforward approach is to do the following:

```julia
julia> rand(1:10)
4
```

The `rand` function takes as input the range of numbers you want to use as the bounds for the number you will generate. In this case, we set the range as `1-10`, inclusive of both numbers.

The other new topic we need to cover for this example to work is while loops. The basic structure of a while loop is:

```julia
while some_condition is true
   do something
end
```

This loop will continue to iterate until the condition for the while loop is no longer met. You will see how we use this soon to keep prompting the user to enter a number until they guess it right.

Lastly, to make it a little easier for us, we are going to add an if statement which tells us if we guess a number that is close to the target number. The structure of an if statement in Julia is:

```julia
if some_condition is true
   do something
end
```

The big difference is that the if statement is checked once and then it is done. The initial condition is not re-checked unless the if statement is in a loop.

Now that we have the basic ideas down, let's see the actual code to build the number guesser. Make sure you try this on your own before checking the solution below. Happy coding! 🎉

```julia
# Number Guessing Game in Julia
# Source: https://github.com/logankilpatrick/10-Julia-Projects-for-Beginners

function play_number_guess_human()

    total_numbers = 25 # 

    # Generate a random number within a certain range
    target_number = rand(1:total_numbers)
    guess = 0

    # While the number has not been guessed, keep prompting for guesses
    while guess != target_number
        print("Please guess a number between 1 and $total_numbers: ")
        guess = parse(Int64, readline())
        # Convert the string value input to a number

        # If we are within +/-2 of the target, give a hint
        if abs(target_number - guess) <= 2 && target_number != guess
            print("\nYou are getting closer!\n")
        end
    end

    print("Nice job, you got it!")
end
```

### How to Build a Computer Number Guesser in Julia 🤖

Now that we have seen what it looks like for us to try and guess what the computer randomly generated, let's see if the computer can do any better. 

In this game, we will select a number and then see how long it takes the computer to guess that number. To do this, we will introduce some new concepts like the Random module and for loops.

We'll begin by thinking about how we can have the computer guess random numbers without repeating any. 

One simple solution is to use the `rand` function, but the issue is that there’s no built-in way to make sure the computer doesn’t guess the same number more than once – since, after all, it is random!

We can solve this issue by combining the `collect` function and the `shuffle` function. We begin by defining a random seed:

```julia
julia> rng = MersenneTwister(1234);
```

Random seeds make it so that random number generators make reproducible results. Next, we need to define all possible guesses:

```julia
julia> a = collect(1:50)
50-element Vector{Int64}:
1
2
3
⋮
```

We now need to use the `shuffle` function to make the guesses random:

```julia
julia> using Random
julia> shuffle(rng, a)
50-element Vector{Int64}:
41
23
13
49
⋮
```

Now that we have the random guesses set up, it's time to loop through them one at a time and see if the number is equal to the target the user inputted. 

Again, give this a try before you check out the solution below:

```julia
# Computer Number Guessing Game in Julia
# Source: https://github.com/logankilpatrick/10-Julia-Projects-for-Beginners

using Random

function play_number_guess_computer()

    print("Please enter a number between 1 and 50 for the computer to try and guess: ")
    
    # Take in the user input and convert it to a number
    target_number = parse(Int64, readline())
    
    # Create an array of 50 numbers
    guess_order = collect(1:50)
    
    # Define our random seed
    rng = MersenneTwister(1234)

    # Shuffle the array randomly given our seed
    shuffled_guess = shuffle(rng, guess_order)

    # Loop through each guess and see if it's right
    for guess in shuffled_guess

        if guess == target_number
            print("\nThe computer cracked the code and guessed it right!")
            break # Stop the for loop if we get it right
        end
        
        print("\nComputer guessed: $guess")
    end
end
```

### How to Build Rock 🗿, Paper 📃, Scissors ✂️ in Julia

If you have never played rock, paper, scissors, you are missing out! The basic gist is you try to beat your opponent with either rock, paper, or scissors. 

In this game, rock beats scissors, scissors beat paper, and paper beats rock. If two people do the same one, you go again.

In this example, we will be playing rock, paper, scissors against the computer. We will also use the `sleep` function to introduce a short delay as if someone was saying the words out loud (which you would do if you played in person).

The sleep function takes in a number that represents how long you want (in seconds) to sleep. We can use this with a function or a loop to slow things down as you will see in this game.

```julia
sleep(1) # Sleep for 1 second

```

Let's also explore a function I found while writing this tutorial, `Base.prompt` , which helps us do what we were previously using `readline` for. 

In this case, however, `prompt` auto-appends a `:` to the end of the line and allows us to avoid having two separate lines for the print and user input:

```julia
human_move = Base.prompt("Please enter 🗿, 📃, or ✂️")

```

We will also need to use an `elseif` to make this example game work. We can chain `if` , `elseif` , and `else` together for completeness. Try putting together the if conditionals, prompts, and sleeps to get the desired behavior, and then check out the code below:

![Image](https://www.freecodecamp.org/news/content/images/2022/10/1-406j3f0e3nN-VxRJUUtK7A.gif)
_Gif of playing Rock Paper Scissors in the Julia REPL_

```julia
# Rock 🗿, Paper 📃, Scissors ✂️ Game in Julia

function play_rock_paper_scissors()
    moves = ["🗿", "📃", "✂️"]
    computer_move = moves[rand(1:3)]

    # Base.prompt is similar to readline which we used before
    human_move = Base.prompt("Please enter 🗿, 📃, or ✂️")
    # Appends a ": " to the end of the line by default

    print("Rock...")
    sleep(0.8)

    print("Paper...")
    sleep(0.8)

    print("Scissors...")
    sleep(0.8)
    
    print("Shoot!\n")

    if computer_move == human_move
        print("You tied, please try again")
    elseif computer_move == "🗿" && human_move == "✂️"
        print("You lose, the computer won with 🗿, please try again")
    elseif computer_move == "📃" && human_move == "🗿"
        print("You lose, the computer won with 📃, please try again")
    elseif computer_move == "✂️" && human_move == "📃"
        print("You lose, the computer won with ✂️, please try again")
    else
        print("You won, the computer lost with $computer_move, nice work!")
    end

end
```

### How to Build a Password Generator in Julia 🎫

**WARNING: Do not use this code to generate real passwords!**

In the age of endless data breaches and people using the same password for every website, having a secure password is important. In this example, we will generate an arbitrary number of passwords with a variable length. 

Given that this could take a long time, we will also add an external package, [ProgressBars.jl](https://github.com/cloud-oak/ProgressBars.jl), to visually show the progress of our for loop. If you have never added an external package before, consider [checking out this robust tutorial](https://blog.devgenius.io/the-most-underrated-feature-of-the-julia-programming-language-the-package-manager-652065f45a3a) on why the package manager is the most underrated feature of the Julia programming language.

To add a Julia package, open the REPL and type `]` followed by `add ProgressBars`. After that, as we did with the Random module (note we did not need to add it since it is part of base Julia), we can say `using ProgressBars` to load it in.

The main new idea we will introduce here is vectors / arrays. In Julia, we can put any type into an array. To create an empty array, we do:

```julia
password_holder = []
```

and then to add something, we use the `push!` function as you will see in the below example. 

As mentioned before, we will use the ProgressBars package to show progress on the screen. Note that Julia is so quick that it likely won’t show you the loading screen unless you manually slow things down with a sleep function call or a high number of passwords. Check out the README for an example of using this in practice. 

As with the other example, try to put some code together before you dissect the example below:

```julia
# Generate Passwords in Julia
# Source: https://github.com/logankilpatrick/10-Julia-Projects-for-Beginners
using ProgressBars
using Random

# WARNING: Do not use this code to generate actual passwords!
function generate_passwords()
    num_passwords = parse(Int64, Base.prompt("How many passwords do you want to generate?"))
    password_length = parse(Int64, Base.prompt("How long should each password be?"))

    # Create an empty vector / array
    password_holder = []

    # Generate a progress bar to show how close we are to being done
    for i in ProgressBar(1:num_passwords)
        # Add the new password into the password holder
        push!(password_holder, randstring(password_length))
        sleep(0.2) # Manually slowdown the generation of passwords
    end
    
    # Only show the passwords if there are less than 100
    if length(password_holder) <= 100
        # Loop through each password one by one
        for password in password_holder
            print("\n", password)
        end
    end
end
```

### How to Build a Dice Rolling Simulator in Julia 🎲

Dice are a fun way to explore and play around with randomness along with unicode characters. 

Julia has amazing support for unicode, and if you want to see all the characters it supports, [head to the Julia docs](https://docs.julialang.org/en/v1/manual/unicode-input/). 

Let's begin by defining an array of dice faces. To access unicode characters, we can use the Julia REPL to do tab completion by typing the following:

```julia
julia> \dicei
```

followed by the tab button. This will create `⚀` which is "Die Face-1". If we do this for all 6 sides of a 6 sided die, we end up with:

```julia
dice_faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
```

For this game, we want to continually ask the user if they want to roll the dice. If they do, we generate a random number between 1 and 6 and then display the dice face from the array we created above. 

Just like we did in previous projects, we will want to use the `rand` function as follows:

```julia
rand(1:num_sides_dice)
```

Give this a try before you check out one possible solution that is highlighted below and keep in mind how we could extend this or use this code to program a much larger game like Monopoly. 

```julia
# Code from https://github.com/logankilpatrick/Julia-Projects-for-Beginners

function rolling_dice()
    
    # Number of sides for dice
    num_sides_dice = 6

    # While the user wants to roll a die, continue to generate a number between 1 and the number of sides
    dice_faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
    
    while true
        print("Do you want to roll a dice? (1=Yes/0=No): ")
        guess = parse(Int64, readline())
        # Convert the string value input to a number

        if guess == 1
            println("Rolling dice")
            current_side = rand(1:num_sides_dice)
            println("Dice has number $(dice_faces[current_side])")
        elseif guess == 0
            println("Exiting")
            break # Stop the while loop if the user decides to do so
        else
            println("Invalid input, please try again")
        end 
    end

end 
```

### How to Build a Countdown Timer in Julia⏱️

Countdowns, for better or worse, are a huge part of life. From New Years Eve to a parent frustratingly trying to convince a child to obey some rule, we see and participate in countdown timers regularly. 

Now, we are going to get a chance to program one (yay). At the core, we will again be using the `sleep` function which we had a chance to play around with in the rock paper scissors example.

As a quick reminder, `sleep` takes in as an argument the number of seconds we want the program to pause for. 

For this example, we are going to try to do some while loop nesting by using functions. We want to have a loop that continues to prompt the user if they want to set a timer, and then if they do, we call a function called `run_timer`. The `run_timer` function should prompt the user to enter how long they want the timer to run for. 

The caveat here is that we also want to print our how long is left for the timer on each iterations. So if the user enters 5, we can't just do `sleep(5)` since the user won't be able to see anything happen for those 5 seconds. 

Below is the main function which is given to you to start. Feel free to modify this as you see fit. Use this starter code and then define the `run_timer` function per the specification above. 

Remember, there's a lot of possible ways to approach this and the solution we include at the bottom is just one possible approach.

```julia
# Code from: https://github.com/logankilpatrick/Julia-Projects-for-Beginners

function run_timer()
	# TODO
end

# Call the run_timer function in a loop until the user quits it
function countdown_timer()

    # While the user chooses to run the countdown timer
    while true
        print("Do you want set a countdown timer? (1=Yes/0=No): ")
        answer = parse(Int64, readline())
        # Convert the string value input to a number

        if answer == 1
            # Run the timer
            run_timer()
        elseif answer == 0
            println("Exiting...")
            break # Stop the countdown timer
        else
            println("Invalid input, please try again")
        end 
    end

end
countdown_timer()
```

Give it a shot and remember you will need to make use of the `parse`, `readline`, `sleep`, and `println` functions to make this function work. 

```julia
# Code from: https://github.com/logankilpatrick/Julia-Projects-for-Beginners

function run_timer()
    print("Enter the amount of seconds: ")
    seconds = parse(Int64, readline())
    
    println("Countdown starts now with $seconds seconds remaining.")
    current_seconds = seconds

    # While the countdown timer is not finished
    while current_seconds != 0

        # Print the current countdown
        if current_seconds != seconds
            println("Seconds left: $current_seconds")
        end

        # Wait for one second
        sleep(1)
        current_seconds = current_seconds - 1
    end
    println("The countdown is over!")
end

# Call the run_timer function in a loop until the user quits it
function countdown_timer()

    # While the user chooses to run the countdown timer
    while true
        print("Do you want set a countdown timer? (1=Yes/0=No): ")
        answer = parse(Int64, readline())
        # Convert the string value input to a number

        if answer == 1
            # Run the timer
            run_timer()
        elseif answer == 0
            println("Exiting...")
            break # Stop the countdown timer
        else
            println("Invalid input, please try again")
        end 
    end

end

countdown_timer()
```

## Wrapping up 🎁

I hope you had as much fun working with and reading about these projects as I did creating them. 

If you want to make your own version of this post and make some small Julia projects and share them with the world, please do so and open a PR here: [https://github.com/logankilpatrick/10-Julia-Projects-for-Beginners](https://github.com/logankilpatrick/10-Julia-Projects-for-Beginners). 

I can easily change the repo name to accommodate an influx of small projects.

I will also note that an exercise like this is also a great way to potentially contribute to Julia. While I was working on this post, I was able to open 2 PR’s to base Julia which I think will help improve the developer experience:

* [https://github.com/JuliaLang/julia/pull/43635](https://github.com/JuliaLang/julia/pull/43635) and
* [https://github.com/JuliaLang/julia/pull/43640](https://github.com/JuliaLang/julia/pull/43640).

If you enjoyed this tutorial, [let’s connect on Twitter](https://twitter.com/OfficialLoganK).




