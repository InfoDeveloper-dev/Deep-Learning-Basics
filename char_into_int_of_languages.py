"""
Code aims to converts characters of languages such as 
1.) Basic Latin
2.) Greek
3.) Devanagari

Unicode Decimal representation will be used to accomplish this task which is taken from below link
https://www.ssec.wisc.edu/~tomw/java/unicode.html

Why Unicode
ASCII can represent only 127 characters and extended ASCII upto 255 characters whereas unicode can \
represent upo 2,147,483,647 characters which can cover all most all languages and hence unicode is used

What is achieved in this Repo
 1.)  Dictionaries contains the characters of different languages as key and int as their values
"""
class LanguageChartoInt:

	def __init__(self, initialvalue, finalvalue):
		self.initialvalue = initialvalue
		self.finalvalue = finalvalue

	def char_to_int(self):
		# empty dictionary which will contain characters as key and integer as value
		dict_char = dict()
		language_alphabets = [chr(lang_char) for lang_char in range(self.initialvalue, self.finalvalue)]
		# applying the loop
		for index, char in enumerate(language_alphabets): 
			dict_char[char]=index
	    # returning the result in form of dictionary
		return dict_char		
	
latin_object = LanguageChartoInt(0, 128)
print("Char to int in form of dictionary for latin is \n {}".format(latin_object.char_to_int()))
print('-'*100)
greek_object = LanguageChartoInt(880, 1024)
print("Char to int in form of dictionary for greek is \n {}".format(greek_object.char_to_int()))
print('-'*100)
Devanagari_object = LanguageChartoInt(2304, 2432)
print("Char to int in form of dictionary for greek is \n {}".format(Devanagari_object.char_to_int()))
