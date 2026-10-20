# VSU Student Toolkit

Run `python student_toolkit.py` (or `python3 student_toolkit.py`). Python 3.8+ recommended.

Each student creates **one new** file inside `student_tools/`, named using their assigned unique identifier, such as `student_tools/jsmith_tip_calculator.py`. Do not edit `student_toolkit.py` or classmates' files.

Every contribution must define:

```python
TOOL_NAME = 'Descriptive Menu Name'

def run():
    print('Hello from my tool!')
```

The main program discovers files and adds their functions to the menu automatically. Avoid duplicate `TOOL_NAME` values. Do not add top-level `input()` calls or execute your function on import.

## Workflow

1. `git clone REPOSITORY_URL`
2. `cd VSU-Student-Toolkit`
3. `git switch -c feature/YOUR_USERNAME-tool`
4. Create and test your file: `python student_toolkit.py`
5. `git add student_tools/YOUR_FILENAME.py`
6. `git commit -m "Add YOUR_TOOL_NAME utility"`
7. `git push -u origin feature/YOUR_USERNAME-tool`
8. Open a pull request targeting `main`. Do **not** merge it; the class will merge pull requests together.

To get the merged class program later: `git switch main`, `git pull origin main`, `python student_toolkit.py`.
