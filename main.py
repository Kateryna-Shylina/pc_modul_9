
AppAssistant = dict()

def parser(command_str):
    command_list = command_str.split()
    
    if len(command_list) == 1:
        word = command_list[0].lower()        
        name = ''
        phone = ''

    elif len(command_list) == 2 and (command_list[1].lower() == 'all' or command_list[1].lower() == 'bye'):
        word = command_list[0].lower() + ' ' + command_list[1].lower()
        name = ''
        phone = ''

    elif len(command_list) == 2 and command_list[0].lower() == 'phone':
        word = command_list[0].lower()
        name = command_list[1].lower() 
        phone = ''  

    else:
        word = command_list[0].lower()
        name = command_list[1].lower()
        phone = int(command_list[2])            

    return word, name, phone

def command_hello(name, phone):
    return 'How can I help you?'

def command_add(name, phone):
    AppAssistant[name] = phone
    return 'None'

def command_change(name, phone):
    old_phone = AppAssistant[name]    
    AppAssistant[name] = phone
    return 'None'

def command_phone(name, phone):
    return AppAssistant[name]

def command_showall(name, phone):
    result = '\n'.join(name + ' ' + str(phone) for name, phone in AppAssistant.items())
    return result

def command_exit(name, phone):
    return 'Good bye!'

OPERATIONS = {
    'hello': command_hello,
    'add': command_add,
    'change': command_change,
    'phone': command_phone,
    'show all': command_showall,
    'good bye': command_exit, 
    'close': command_exit, 
    'exit': command_exit
}


def input_error(func):
    def inner(s):
        try:
            result = func(s)
            return result
        except KeyError:
            return f"Incorent command or tne name doesn't exist. Give me command, name and phone please."
        except IndexError:
            return f"Invalid number of words. Give me command, name and phone please."      
        except ValueError:
            return f"Incorrect input order. Give me command, name and phone please."          
        
    return inner

@input_error
def command_handler(command_str):
    word, name, phone = parser(command_str)    
    command = OPERATIONS[word]
    return command(name, phone)


if __name__ == '__main__':
    while True:
        command_str = input(">>> ")
        result = command_handler(command_str)
        
        if result != 'None':
            print(result)
        
        if result == 'Good bye!':
            break
        