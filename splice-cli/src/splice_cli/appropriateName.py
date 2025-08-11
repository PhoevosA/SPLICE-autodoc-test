"""
SPLICE testing stuff
"""

__version__ = "0.1.0"


class NotAStringError(Exception):
    """ Raised if the parameter is not a string"""
    pass


def testing(parameter):
    """
    Description goes here
    
    :param parameter: String to be passed in
    :type parameter: string, not optional
    :raise appropriateName.NotAStringError: If the parameter is not a string.
    :return: The string backwards
    :rtype: string
    """
    try:
        if type(parameter) != str:
            raise NotAStringError

    except NotAStringError:
        print("Not a string")
        return

    print(parameter[::-1])
    return 

def stupidFunction():
    """
    Does nothing - remember to delete this before demonstrating 

    :param None: Not in the budget :( 
    :raise No Errors: Literally does not do anything
    :return: As above 
    """
    
    return 
