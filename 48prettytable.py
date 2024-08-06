from prettytable import PrettyTable
table = PrettyTable()   #PrettyTable is a pypi pacakge installed for not to type all asci art


table.add_column("Pokemon Name", ["Pikachu","Squirtle","Charmander"])
table.add_column("Type", ["Electric","Water","Fire"])

table.align = "l"

print(table)

"""https://pypi.org/project/prettytable/"""
