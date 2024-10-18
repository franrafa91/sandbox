class Format:
    """
    Instantiate a formatting object.
    Integers or Float Numbers will be reformatted according to a parameter.
    
    :param style: The preset formatting style
    :type style: int
    """

    def __init__(self, style:int = 0) -> None:
        self.style = style
    
    def update(self, style:int = 0) -> None:
        self.style = style

    def __call__(self, number:int) -> str:
        """
        Reformat integer according to Format defined

        param number: Number to format
        type number: int
        """
        if self.style == 0:
            return Format.sci_not(number)
        elif self.style == 1:
            return Format.fixed(number)
        elif self.style == 2:
            return Format.general(number)
        else: return str(number)
    
    def sci_not(number) -> str:
        """
        Format a number into scientific notation
        """
        return '{:.2e}'.format(number)
    
    def fixed(number) -> str:
        """
        Format a number into fixed notation with 2 decimals
        """
        return '{:,.2f}'.format(number)
    
    def general(number) -> str:
        """
        Format a number as an general integer 
        """
        return str(round(number))