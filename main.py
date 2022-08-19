from enum import Enum, auto
import os
from traceback import print_exc

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
    match file:
        case "": return "No todos for today! :)"
        case _: return "Functional TODO app in python\n" + generate_todo_text(parse_rest(file)) + "\n" 

def add_todo(content, inp):
    match content:
        case "": return content + "0" + inp
        case _: return content + "\n" + "0" + inp

def get_todo_index(content, todo):
    match (content, todo):
        case ("", _): return 1
        case (_, 1): return 0
        case _:
            return content.find("\n") + 1 + get_todo_index(content[content.find("\n")+1:], todo-1)

def finish_action(content, inp):
    # This is just making variable in a "pure" way
    match get_todo_index(content, int(inp)):
        case index: return content[:index] + "1" + content[index+1:]

def get_action(inp):
    match inp:
        case "add":
            return add_todo
        case "do":
            return finish_action

def get_file_content(file, inp):
    return ""

# In-pure part of the program

def main():
    os.system("clear")
    while True:
        content = ""
        try:
            with open("todo.txt", "r") as f:
                content = f.read()
                print(get_output(content))
        except FileNotFoundError:
            print(get_output(""))
        with open("todo.txt", "w") as f:
            try:
                command = input().strip()
                if command in ("quit", "exit"): 
                    f.write(content)
                    break
                f.write(get_action(command)(content, input()))
            except IndexError:
                print("TODO with that number was not found")
                input("Press enter to continue")
            except TypeError:
                print("Command not found")
            except:
                print_exc() # This is debug
                f.write(content)
                exit(0)

if __name__ == "__main__":
    main()