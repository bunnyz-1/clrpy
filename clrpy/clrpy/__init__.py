# rgbio.py

class Color:
    def __init__(self, r=None, g=None, b=None, code=None):
        """
        ( R , G , B )
        """
        if code:
            self.code = code
        elif r is not None and g is not None and b is not None:
            self.code = f"\033[38;2;{r};{g};{b}m"
        else:
            self.code = "\033[0m"
        self.reset = "\033[0m"

    def print(self, *args, **kwargs):
        text = " ".join(str(a) for a in args)
        print(f"{self.code}{text}{self.reset}", **kwargs)

    def input(self, prompt=""):
        return input(f"{self.code}{prompt}{self.reset}")


# ألوان أساسية
red   = Color(code="\033[31m")
green = Color(code="\033[32m")
blue  = Color(code="\033[34m")

# مثال على RGB: orange = Color(255, 165, 0)
