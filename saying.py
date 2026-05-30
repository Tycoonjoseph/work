# customing a library for the codes that you always find yourself writing over and over again. For example, if you find yourself writing the same code to print a pyramid of hashes, you can create a function that does that for you. Then, instead of writing the code every time, you can just call the function with the desired height of the pyramid. This not only saves time but also makes your code cleaner and more reusable.
def main():
    hello("World")
    goodbye("World")
def hello(name):
    print(f"Hello, {name}")


def goodbye(name):
    print(f"Goodbye, {name}")
if __name__ == "__main__":
    main()