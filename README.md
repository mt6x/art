# ART

Art is a package that allows a user to display colourful text inside of their terminal. It is written in Python, and is very simple to use and fast working.

## Syntax

### Defining an RGB colour.

To clarify, an RGB colour is made of three parts. Red, Green and Blue. Each value ranges from 0 - 255, and it is these parts mixed together which is what creates our final colour value. So when defining an RGB colour using Art, it is very simple to do so.

```py
colour = RGB(255,0,255) # Pink
```

You need to provided a minimum of **__two__** colours to the colour text function, else your gradient will simply not render.

### Displaying colourful text.

When displaying colourful text, we want to ensure that we have all of our colours ready, and the provided text that we want to glamourise.

An example of how we would do this is written below.

```py
# Define both of our colours.
colour1 = RGB(255,0,255)
colour2 = RGB(0,255,255)

# Write our text to the terminal.
print(colourString("This is what I want to be coloured", [colour1, colour2]))
```

This would in turn output the text with a gradient effect on top of it. Please note, you can use more than two colours, infact; there is no limit to how many colours you can use. It is up to you to personalise how you want your text to look with Art.
