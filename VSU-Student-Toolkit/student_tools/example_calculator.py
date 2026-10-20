"""Instructor-provided example. Students should create their own files."""
TOOL_NAME = 'Add Two Numbers (Example)'


def run():
    print('\nAdd Two Numbers')
    try:
        first = float(input('First number: '))
        second = float(input('Second number: '))
    except ValueError:
        print('Please enter valid numbers.')
        return
    print(f'Result: {first + second}')
