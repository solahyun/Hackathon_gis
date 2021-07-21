
def decorator(func):
    def decorated(input_text):
        print('Start function!')
        func(input_text)
        print('End function!')
    return decorated

@decorator
def hello_world(input_text):
    print(input_text)

hello_world('Hello guys~')