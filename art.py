# The RGB class allows us to store the colours in a usable manor.
class RGB:
    def __init__(self, r: int, g: int, b: int) -> None:
        self.r = r
        self.g = g
        self.b = b
    
    # Validate if the colour has been defined properly.
    def valid(self) -> bool:
        if (self.r > 255 or self.r < 0) or (self.g > 255 or self.g < 0) or (self.b > 255 or self.b < 0):
            return False
        
        return True
    
    # Convert the RGB class into an ANSI escape code.
    def ansi(self) -> str:
        return f"\x1b[38;2;{self.r};{self.g};{self.b}m"

    # Represent the class with the defined r,g,b methods.
    def __repr__(self):
        return f"rgb({self.r},{self.g},{self.b})"

# Create a linear RGB colour gradient.
def linear_gradient(colours: list, steps: int) -> list:
   # Check if each colour is valid.
   for colour in colours:
    try:
        # Check if the current colour is valid.
        if colour.valid() == False:
            return None
    except:
        # The provided item is not an RGB object.
        return None

    # Check if the user has followed the correct syntax.
    if len(colours) < 2:
        return None

    # Check if there is any requirement to run the algorithm.
    if steps <= len(colours) :
        return colours

    # Contain the output list for the colour steps that will be created.
    output = []

    # Contain the total colour segments that we will be using.
    segments = len(colours) - 1

    # Calculate the amount of colour steps per segment.
    stepsPerSegment = steps // segments

    # Calculate the extra steps that will be needed after each segment.
    remaining = steps % segments

    for i in range(segments):
        # Contain the current step value.
        currentSegment = stepsPerSegment + 1 if i < remaining else stepsPerSegment

        for j in range(currentSegment):
            # Contain the current position in the gradient sequence.
            position = j / currentSegment
            
            # new = start + change * (end - start)
            output.append(RGB(int(colours[i].r + position * (colours[i+1].r - colours[i].r)),int(colours[i].g + position * (colours[i+1].g - colours[i].g)),int(colours[i].b + position * (colours[i+1].b - colours[i].b))))

    return output

# Convert a provided string into a gradient string.
def colourString(string: str, colours: list) -> str:
    # Create the gradient colours.
    colours = linear_gradient(colours, len(string))

    # Check if the user has provided a correct colour array.
    if colours == None:
        return string

    # Contain the output for the string after the gradient has been applied.
    output = []

    for i in range(len(colours)-1):
        output.append(f"{colours[i].ansi()}{string[i]}")
    
    return "".join(output)
