# sandwich_orders = ['сендвич с колбасой', 'сендвич с сыром', 'сендвич со свежими овощами', 'сендвич с мясом']
# finished_sandwich = []
#
# print('Извините сендвич с сыром закончился\n')
#
# while 'сендвич с сыром' in sandwich_orders:
#     sandwich_orders.remove('сендвич с сыром')
#
#
# for sandwich in sandwich_orders:
#     print(f'Я приготовил для тебя {sandwich}.')
# while sandwich_orders:
#     every_sandwich = sandwich_orders.pop()
#     finished_sandwich.append(every_sandwich)
# print('')
#
# for food in finished_sandwich:
#     print(f'Я приготовил для тебя {food}')
#
#
# print(finished_sandwich)


# wish_list = {}
#
# active = True
#
# while active:
#     name = input('Как Вас зовут?')
#     wish = input('Страна в которой хотели побывать?')
#     wish_list[name] = wish
#     repeat = input('Желаете закончить?')
#     if repeat == 'yes':
#         active = False
# print("Results")
# for name, wish in wish_list.items():
#     print(f'{name.title()} хочет поситить страну {wish.title()}')