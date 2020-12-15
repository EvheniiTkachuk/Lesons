# Create a simple prototype of a TV controller in Python. It’ll use the following commands:
# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel. Pay attention that
# the channel numbers start from 1, not from 0.
# next_channel() - turns on the next channel. If the current channel
# is the last one, turns on the first channel.
# previous_channel() - turns on the previous channel. If the current
# channel is the first one, turns on the last channel.
# current_channel() - returns the name of the current channel.
# is_exist(N/'name') - gets 1 argument - the number N or the string
# 'name' and returns "Yes", if the channel N or 'name' exists in the list, or "No" - in the other case.


class TVController():

    def __init__(self, channels: list):
        self.channels = channels
        self.curr_channel = 1

    def first_channel(self):
        self.curr_channel = 1
        return self.channels[self.curr_channel - 1]

    def last_channel(self):
        self.curr_channel = len(self.channels)
        return self.channels[self.curr_channel - 1]

    def turn_channel(self, N):
        self.curr_channel = N
        return self.channels[self.curr_channel - 1]

    def next_channel(self):
        self.curr_channel += 1
        if self.curr_channel > len(self.channels):
            return TVController.first_channel(self)
        else:
            return self.channels[self.curr_channel - 1]

    def previous_channel(self):
        self.curr_channel -= 1
        if self.curr_channel <= 0:
            return TVController.last_channel(self)
        else:
            return self.channels[self.curr_channel - 1]

    def current_channel(self):
        return self.channels[self.curr_channel - 1]

    def is_exist(self, N_or_name):
        try:
            N_or_name = int(N_or_name)
            if type(N_or_name) is int and N_or_name in range(1, len(self.channels) + 1):
                return -1
        except:
            N_or_name = N_or_name.lower()
            list_lower = [str(x).lower() for x in self.channels]
            if list_lower.count(N_or_name):
                return list_lower.index(N_or_name) + 1
            else:
                print('No chanel...')
                return False


CHANNELS = ["BBC", "Discovery", "TV1000"]

controller = TVController(CHANNELS)

# task test -----------------------------------------------------------------

# print(f'controller.first_channel() == {controller.first_channel()}')
# print(f'controller.last_channel() == {controller.last_channel()}')
# print(f'controller.turn_channel(1) == {controller.turn_channel(1)}')
# print(f'controller.next_channel() == {controller.next_channel()}')
# print(f'controller.previous_channel() == {controller.previous_channel()}')
# print(f'controller.current_channel() == {controller.current_channel()}')
# print(f'controller.is_exist(4) == {controller.is_exist(4)}')
# print(f'controller.is_exist(\'BBC\') == {controller.is_exist("BBC")}')

# task test -----------------------------------------------------------------


def print_menu(switch):
    print('')
    for key, val in switch.items():
        print(f'{key} - {val}')


def show_channel_list(channel_list):
    print('\nChannel list:\n')
    for i, val in enumerate(channel_list):
        print(f'{i + 1}. {val}')
    return


def switch_main(option):
    if option == '1':
        show_channel_list(controller.channels)
    elif option == '2':
        print('\n' + controller.first_channel())
    elif option == '3':
        print('\n' + controller.last_channel())
    elif option == '4':
        choice = input(f'\nEnter channel (1 - {len(controller.channels)}) >>> ')
        try:
            choice = int(choice)
            if choice in range(1, len(controller.channels) + 1):
                print('\n' + controller.turn_channel(int(choice)))
                return False
            else:
                print('No chanel...')
                return False
        except:
            print('Incorrect data...')
            return False
    elif option == '5':
        print('\n' + controller.next_channel())
    elif option == '6':
        print('\n' + controller.previous_channel())
    elif option == '7':
        print('\n' + controller.current_channel())
    elif option == '8':
        choice = input('Enter channel (N / name) >>> ')
        res = controller.is_exist(choice)
        if res == -1:
            choice = int(choice)
            print(f'Сhannel found, this is a channel: {controller.channels.index(controller.channels[choice - 1]) + 1}. {controller.channels[choice - 1]}')
        elif res in range(1, len(controller.channels) + 1):
            print(f'Сhannel found, this is a channel: {controller.channels.index(controller.channels[res - 1]) + 1}. {controller.channels[res - 1]}')
            return
        elif res == 0:
            return False
    elif option == '9':
        print('\n\nThank you for use ◕‿◕\n')
        return 1
    else:
        print('No option...')


def menu():
    switcher = {
        1: 'Show channel list',
        2: 'first_channel',
        3: 'last_channel',
        4: 'turn_channel',
        5: 'next_channel',
        6: 'previous_channel',
        7: 'current_channel',
        8: 'is_exist (N / name)',
        9: 'exit',
    }

    while True:
        print_menu(switcher)
        choice = input('\nEnter your choice >>> ')
        option = switch_main(choice)
        if option:
            break


menu()
