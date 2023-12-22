from typing import List
from colorama import init, Back, Style

# By setting autoreset to true, the colors of the terminal will return to normal after the pixel art image is displayed.
init(autoreset=True)

# Colorama allows for only eight colors.
BLACK = Back.BLACK + '  '
RED = Back.RED + '  '
GREEN = Back.GREEN + '  '
YELLOW = Back.YELLOW + '  '
BLUE = Back.BLUE + '  '
MAGENTA = Back.MAGENTA + '  '
CYAN = Back.CYAN + '  '
WHITE = Back.WHITE + '  '

COLORS_DICT = {
  'black' : BLACK,
  'red' : RED,
  'green' : GREEN,
  'yellow' : YELLOW,
  'blue' : BLUE,
  'magenta' : MAGENTA, 
  'cyan' : CYAN,
  'white' : WHITE
}


class Image():
  """
  Main vehicle for creating pixel art image
  """
  def __init__(self, w: int=7, h:int=7)->None:
    """
    Parameters
    ----------
    w: int
      pixel art image width
    h: int
      pixel art image height
    """
    self.width = w
    self.height = h
    self.img = self.init_list()
  
  def init_list(self)->List[List]:
    """
    Return a 2-dimensional empty list representing
    """
    lst = []
    for row in range(self.height):
      lst.append([])
    return lst
  
  def display(self)->None:
    """
    Draw everything to the terminal
    """
    for row in self.img:
      self.display_row(row)
  
  def display_row(self, row:List)->None:
    """
    Display a row of the pixel art
    """
    for pixel in row:
      print(pixel, end='')
    print()
  
  def convert_color(self, str_clr: str)->str:
    """
    Takes a string that represents a color and returns the associated Colorama object
    """
    return COLORS_DICT.get(str_clr, BLACK)

  def add_row(self, *args):
    if len(args) == 2:
      colors = [self.convert_color(args[1]) for i in range(self.width)]
      self.img[args[0]] = colors
    else:
      color_params = args[1:]
      colors = [self.convert_color(arg) for arg in color_params]
      self.img[args[0]] = colors






# test your code here
