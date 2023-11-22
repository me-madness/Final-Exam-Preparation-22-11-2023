# First task from the lecture

def decode_message(message, commands):
    for command in commands:
        tokens = command.split('|')
        instruction = tokens[0]
        
        if instruction == 'Move':
            num_letters = int(tokens[1])
            message = message[num_letters:] + message[:num_letters]
        elif instruction == 'Insert':
            
            
encrypted_message = input()
commands_list = []

while True:
    command = input()
    if command == "Decode":
        break
    
    
    commands_list.append(command)

decode_message(encrypted_message, commands_list)


# Second task is from me

