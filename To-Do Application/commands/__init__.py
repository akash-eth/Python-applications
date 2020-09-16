import commands.lists

import commands.todos

commands_dict = {
    'show': lists.show_list,
    'use': lists.use_list,
    'create': lists.create_list,

    'all': todos.show_item,
    'add': todos.add_item
}