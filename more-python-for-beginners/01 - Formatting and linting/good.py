
# Type hints
def print_hello(name: str) -> str:
    """
    Greets the user by name

	Parameters:
		name (str): The name of the user
	Returns:
		str: The greeting
	"""
	print('Hello, ' + name)
def test_hello(name):
	print('Hello' + name)
print_hello