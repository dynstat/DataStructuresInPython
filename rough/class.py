class Test:
    # First argument of the method is always considered as the self irrespective of its name.
    def print_something(self, name):
        print(f"yo {name}")


if __name__ == "__main__":
    test1 = Test()
    test1.print_something("XS")
