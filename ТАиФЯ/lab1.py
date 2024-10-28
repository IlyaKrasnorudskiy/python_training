rules = {
    'S': ['aaA'],
    'A': ['bbB', 'a'],
    'B': ['ccC', 'b'],
    'C': ['dD', 'c'],
    'D': ['d']
}

def enumerate_grammar(start_symbol, rules):
    queue = [start_symbol]
    terminal_symbols = {'a', 'b', 'c', 'd'}

    while queue:
        current_string = queue.pop(0)

        if all(symbol in terminal_symbols for symbol in current_string):
            print(current_string)
        else:
            for i, symbol in enumerate(current_string):
                if symbol in rules:
                    for production in rules[symbol]:
                        new_string = current_string[:i] + production + current_string[i + 1:]
                        queue.append(new_string)

enumerate_grammar('S', rules)
