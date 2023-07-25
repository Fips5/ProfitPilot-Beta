def edit_python_file(file_path, line_number, new_line):
    # Read the original file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Modify the specified line with the new line
    lines[line_number - 1] = new_line + '\n'

    # Write the modified lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)

#as you can see the edit_python_file function is made by ChadGPT as i am not that smart

def changeSmaL():
    python_file_path = r'C:\Users\David\Desktop\Pilot\20\sma\SMA20.py'
    line_number = 7
    user_input = input("SMA_L(4,8,12,16,...4*SMA_S): ")
    new_line = f'MAX_ENTRIES = {user_input}'
    edit_python_file(python_file_path, line_number, new_line)

def changeSmaS():
    python_file_path = r'C:\Users\David\Desktop\Pilot\5\sma\SMA5.py'
    line_number = 7
    user_input = input("SMA_S(1,2,3,4): ")
    new_line = f'MAX_ENTRIES = {user_input}'
    edit_python_file(python_file_path, line_number, new_line)
    changeSmaL()

def chnageTIME():
    files = {
        r'C:\Users\David\Desktop\Pilot\5\sma\SMA5.py': {'line_number': 54, 'new_line':   '        time.sleep('},
        r'C:\Users\David\Desktop\Pilot\20\sma\SMA20.py': {'line_number': 49, 'new_line': '        time.sleep('},
        r'C:\Users\David\Desktop\Pilot\20\results.py': {'line_number': 19, 'new_line':   '    time.sleep('},
        r'C:\Users\David\Desktop\Pilot\5\results.py': {'line_number': 19, 'new_line':    '    time.sleep('},
        r'C:\Users\David\Desktop\Pilot\main\SMA.py': {'line_number': 72, 'new_line':     '        time.sleep('}
        
    }

    for file, details in files.items():
        file_path = f'{file}'
        line_number = details['line_number']
        user_input = input(f"TIME for {file}: ")
        new_line = details['new_line'] + f'{user_input})'
        edit_python_file(file_path, line_number, new_line)

        
changeSmaS()

while True:
    user_input = input("Change Time (y/n): ")
    
    if user_input.lower() == 'y':
        chnageTIME()
    elif user_input.lower() == 'n':
        print("GOOD LUCK BRO.")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

def changeTimeRun():
        file_path = r'C:\Users\David\Desktop\Pilot\run.py'
        line_number = 6
        user_input = input(f"TIME for run.py: ")
        new_line = f'    typing_interval = {user_input}'
        edit_python_file(file_path, line_number, new_line)  

while True:
    user_input = input("Change Time run.py (y/n): ")
    
    if user_input.lower() == 'y':
        changeTimeRun()
    elif user_input.lower() == 'n':
        print("GOOD LUCK BRO.")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")