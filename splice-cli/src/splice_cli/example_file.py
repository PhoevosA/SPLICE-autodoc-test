from fastapi import FastAPI

__doc__ = """This should describe the purpose of this file"""

class ExampleError(Exception):
    """ Raised if the parameter is not a string"""
    pass


def exampleFunction(example):
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

 	For example:
  	
  	.. code-block:: python 

   	   from example_file import exampleFunction
	   
	   print(exampleFunction('This is an example string'))
  	   >>>gnirts elpmaxe na si sihT
 
	"""
    try:
        if type(parameter) != str:
            raise NotAStringError

    except NotAStringError:
        print("Not a string")
        return

    return parameter[::-1]

class ClassName():
	"""
	This is a description of ClassName

	:param firstPar: This is the first example parameter
	:type firstPar: string, not optional
	:param secondPar: This is the second example parameter
	:type secondPar: integer, optional
    """
    
	def __init__(self, firstPar, secondPar=0):
		"""Constructor method"""

		self.par1 = firstPar
		self.par2 = secondPar

	def classMethod(self, thirdPar):
		"""
		This is the description of this method

		:param thirdPar: This is the third example parameter
		:type thirdPar: integer, non-optional
		:return: The integer passed in + 1 
		:rtype: integer 
		"""
		
		return thirdPar + 1 


print(exampleFunction("This is an example string"))
