from typing import Any
import sys

class Calculator:
    def __init__(self):
        pass

    def _input_int_validate(raw_input: str) -> None | list[int]:
        if not raw_input or len(raw_input) <= 2: print("ERROR: must be provided atleast 1 number"); return None
        raw_input = raw_input.strip()
        splits = [',', ' ']
        clean_input = []
        for splitter in splits:
            if splitter in raw_input: clean_input = raw_input.split(splitter)
        if not clean_input: print("ERROR: Critical fault whilst splitting"); return None
        list_of_inputs_converted: list[int] | None = []
        for _input in clean_input:
            try:
                if ' ' in _input or ',' in _input:
                    continue
                elif '.' in _input:
                    list_of_inputs_converted.append(float(_input.strip()))
                else:
                    list_of_inputs_converted.append(int(_input.strip()))
            except ValueError as e:
                print(f"ERROR: Invalid input in provided input {_input}. Skipping")
                continue
            except Exception as e:
                print(e)
                continue
        if list_of_inputs_converted: return list_of_inputs_converted
        return None

    @classmethod
    def add(cls,ints: int) -> int | None:
        validated_inputs = cls._input_int_validate(ints)
        if validated_inputs:
            try:return sum(validated_inputs)
            except Exception as e:
                print(e)
                return None
        return None
    
def main() -> None:

    calc = Calculator()
    list_of_commands = []

    main_loop = True
    print("\n(For a list of commands, type \"list cmd\"\n")
    while main_loop:
        command = input("Enter the command you would like to enter: ").lower()

        match command:
            case "list cmd":
                #TBD
                #print(f"{".   \n".join[list_of_commands]}\n")
                ...
            case "add":
                output = calc.add(input("Enter the numbers you would like to add (Seperated): "))
                if output: print(output)
            case "subtract":
                ...
            case "divide":
                ...
            case "multiply":
                ...
            case "exit":
                print("Exiting...")
                sys.exit()
            case _:
                print(f"ERROR: Comand '{command}' not found")
        continue

if __name__ == "__main__":
    main()