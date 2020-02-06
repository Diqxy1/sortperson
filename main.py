import commands
from controllers.participant_controller import route as participant_route
from controllers.raffle_controller import route as raffle_route

i = True

while i:
    command = input('$>> ')
    if command in commands.EXIT:
        i = False
        print('Scipt finalizado.')
    elif command.split(' ')[0] in commands.PARTICIPANTS:
        participant_route(command.split(' ')[1])
    elif command in commands.CLEAR or command in commands.RANDOM:
        raffle_route(command)
    else:
        print('Comando invalido')