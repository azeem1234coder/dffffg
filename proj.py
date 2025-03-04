class StringReverser:
    def __init__(self, input_string):
        self.input_string = input_string
    
    def reverse_words(self):
        # Split the string into words, reverse the list of words, and join them back into a string
        words = self.input_string.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)

# Example usage
input_string = "Hello world, this is an example"
reverser = StringReverser(input_string)
reversed_string = reverser.reverse_words()
print(reversed_string)
 