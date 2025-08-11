from fastapi import FastAPI

__doc__ = """This should describe the purpose of this file"""

class ExampleError(Exception):
    """ Raised if the parameter is not a string"""
    pass


def exampleFunction(parameter):
    """
    
	Description of this function
    
	Extended descriptions will appear on automodules but not on the autosummaries (i.e. on the individual pages vs on the summaries page).
	This text can be as long as you like and you can put a blank line between paragraphs in your description

	like so, to format them properly
  
	:param example: Word to be passed into exampleFunction
	:type example: string, not optional 
	:raise example_file.ExampleError: If the parameter is not a string 
	:return: The string backwards 
	:rtype: string 

 	For example, print(exampleFunction("This is an example string"))
  	would return 'gnirts elpmaxe na si sihT'
	"""
    try:
        if type(parameter) != str:
            raise NotAStringError

    except NotAStringError:
        print("Not a string")
        return

    return parameter[::-1]

print(exampleFunction("This is an example string"))
