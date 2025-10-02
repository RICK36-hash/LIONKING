# Sample Python Program
# This is a simple hello world application

def greet(name):
    """Function to greet a person"""
    return f"Hello, {name}!"

def main():
    """Main function"""
    print("Welcome to Python in GitHub Codespaces!")
    user_name = "World"
    message = greet(user_name)
    print(message)
    
    # Demonstrate some basic Python features
    numbers = [1, 2, 3, 4, 5]
    print(f"Sum of numbers: {sum(numbers)}")
    print(f"Maximum: {max(numbers)}")
    
if __name__ == "__main__":
    main()