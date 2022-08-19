from enum import Enum, auto
import os

def parse_todo(line: str) -> tuple[bool, str]:
    return (bool(int(line[0])), line[1:])
def parse_rest(rest) -> list[tuple[bool, str]]:
    match rest.find("\n"):
        case -1: return [parse_todo(rest)]
        case _:
            return [parse_todo(rest[:rest.find("\n")])] + parse_rest(rest[rest.find("\n")+1:])

def generate_todo_marker(completed: bool) -> str:
    match completed:
        case True: return "[x] "
        case False: return "[ ] "

def generate_todo_text(todos: list[tuple[bool, str]]) -> str:
    match todos:
        case []: return ""
        case _:
            return generate_todo_marker(todos[0][0]) + todos[0][1] + "\n" + generate_todo_text(todos[1:])

def get_output(file):
    return "Functional TODO app in python\n" + generate_todo_text(parse_rest(file)) + "\n" 

def add_todo(content, inp):
    return content + "\n" + "0" + inp

def get_action(inp):
    match inp:
        case "add":
            return add_todo

def get_file_content(file, inp):
    return ""

# In-pure part of the program

def main():
    while True:
        content = ""
        try:
            with open("todo.txt", "r") as f:
                content = f.read()
                print(get_output(content))
        except FileNotFoundError:
            print(get_output(""))
        with open("todo.txt", "w") as f:
            command = input().strip()
            if command == "quit": break
            f.write(get_action(command)(content, input()))
            os.system("clear")

if __name__ == "__main__":
    main()