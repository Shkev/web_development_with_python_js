"""Creating a decorator that announces when a function, `f`, runs.
The decorator function takes in a function as input.
The decorator takes the given function, creates a new function (the wrapper)
and runs that new function."""
def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper;

# applying the announce decorator to the function
@announce
def hello():
    print("Hello, world!")

hello()
