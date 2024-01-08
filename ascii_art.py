import random

def generate_diamond(size, color):
  """Generates an ASCII art diamond of the given size and color."""
  mid = size // 2 + 1
  diamond = ""
  for i in range(1, size + 1, 2):
    spaces = " " * (mid - i)
    stars = "*" * i
    diamond += color + spaces + stars + "\033[0m\n"  # Add color using ANSI escape codes
  for i in range(size - 1, 0, -2):
    spaces = " " * (mid - i // 2)
    stars = "*" * i
    diamond += color + spaces + stars + "\033[0m\n"
  return diamond

def generate_triangle(size, color):
  """Generates an ASCII art triangle of the given size and color."""
  triangle = ""
  for i in range(1, size + 1):
    spaces = " " * (size - i)
    stars = "*" * i
    triangle += color + spaces + stars + "\033[0m\n"
  return triangle

def generate_square(size, color):
  """Generates an ASCII art square of the given size and color."""
  square = ""
  for i in range(size):
    stars = "*" * size
    square += color + stars + "\033[0m\n"
  return square

# Get user input for shape, size, and color
shape = input("Choose a shape (diamond, triangle, square): ")
size = int(input("Enter the size: "))
color = input("Choose a color (red, green, yellow, blue, magenta, cyan, white): ")

# Generate the ASCII art
if shape.lower() == "diamond":
  art = generate_diamond(size, "\033[31m")  # Red color
elif shape.lower() == "triangle":
  art = generate_triangle(size, "\033[32m")  # Green color
elif shape.lower() == "square":
  art = generate_square(size, "\033[34m")  # Blue color
else:
  print("Invalid shape!")
  exit()

# Print the ASCII art
print(art)
