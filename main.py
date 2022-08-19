from enum import Enum, auto


def get_output(file):
    return ""

def get_action(inp):
    return lambda x, y: ""

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
            command = input()
            if command: break
            f.write(get_action(command)(content, input()))

if __name__ == "__main__":
    main()