# To-Do Application

import time

from commands import commands_dict

def parse(command):
  """
  Takes the command as input and returns the command name and args
  """
  cmd_list = command.split()
  cmd_type = cmd_list[0]
  if (cmd_type == 'help' or cmd_type == 'quit'):
    return cmd_type, []
  elif (cmd_type == 'list'):
    cmd_name = cmd_list[1]
    if (cmd_name in ['show', 'use', 'create']):
      return cmd_name, cmd_list[2:]
    else:
      return 'invalid', []
  elif (cmd_type == 'todo'):
    cmd_name = cmd_list[1]
    if (cmd_name in ['add', 'all', 'edit', 'remove', 'complete', 'incomplete']):
      return cmd_name, cmd_list[2:]
    else:
      return 'invalid', []
  else:
    return 'invalid', []

def main():
    print("!! Starting the Apllication please hold tight !!")
    while True:
        command = input("$ ").lower()
        if (command == "quit"):
            time.sleep(2)
            print("!! Exiting out the apllication !!")
            break
        else:
            continue


if __name__ == '__main__':
    main()