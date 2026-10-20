"""VSU Student Toolkit: class collaboration starter project."""
from pathlib import Path
import importlib.util

TOOLS_DIR = Path(__file__).parent / 'student_tools'


def load_tools():
    tools = {}
    for path in sorted(TOOLS_DIR.glob('*.py')):
        if path.name.startswith('_'):
            continue
        spec = importlib.util.spec_from_file_location(path.stem, path)
        module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(module)
            name = getattr(module, 'TOOL_NAME')
            function = getattr(module, 'run')
            if not isinstance(name, str) or not name.strip() or not callable(function):
                raise ValueError('TOOL_NAME must be text and run must be callable')
            if name in tools:
                raise ValueError('Duplicate tool name')
            tools[name] = function
        except Exception as error:
            print(f'Skipping {path.name}: {error}')
    return tools


def main():
    while True:
        tools = load_tools()
        names = list(tools)
        print('\n=== VSU STUDENT TOOLKIT ===')
        if not names:
            print('No student tools installed yet.')
        for number, name in enumerate(names, 1):
            print(f'{number}. {name}')
        print(f'{len(names) + 1}. Exit')
        choice = input('Select an option: ').strip()
        if not choice.isdigit():
            print('Please enter a menu number.')
            continue
        number = int(choice)
        if number == len(names) + 1:
            print('Goodbye!')
            break
        if 1 <= number <= len(names):
            try:
                tools[names[number - 1]]()
            except Exception as error:
                print(f'Tool encountered an error: {error}')
        else:
            print('Invalid menu option.')


if __name__ == '__main__':
    main()
