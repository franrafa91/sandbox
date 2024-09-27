class Format:
    """
    Instantiate a formating object.
    Integers or Float Numbers will be reformatted according to a parameter. 
    
    :param style: The preset formatting style
    :type style: int
    """

    def __init__(self, style:int = 0) -> None:
        self.style = style
    
    def format(self, number:int) -> str:
        """
        Reformat integer according to Format defined

        param number: Number to format
        type number: int
        """
        if self.style == 0:
            return Format.sci_not(number)
        else: return str(number)
    
    def sci_not(number):
        """
        Format a number into scientific notation
        """
        return '{:.2e}'.format(number)