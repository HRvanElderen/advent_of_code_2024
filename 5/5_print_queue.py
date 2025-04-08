import numpy as np

def read_input(input):
    rules = []
    updates = []

    with open(input, "r") as f:
        data = f.read()
        rules_and_updates = data.split('\n\n')
        for line in rules_and_updates[0].split('\n'):
            rules.append([int(s) for s in line.split('|')])
        for line in rules_and_updates[1].split('\n'):
            updates.append([int(s) for s in line.split(',')])
    return rules, updates


def part_1(input):
    rules, updates = read_input(input)
    correct = []
    total = 0
    for update in updates:
        rule_broken = False
        for rule in rules:
            if all(elem in update for elem in rule):
                if update.index(rule[0]) > update.index(rule[1]):
                    rule_broken = True
                    break
        if not rule_broken:
            correct.append(update)
            middle = int(len(update) / 2)
            total += update[middle]
    return total

def check_update(rules, update):
    rule_broken = False
    for rule in rules:
        if all(elem in update for elem in rule):
            if update.index(rule[0]) > update.index(rule[1]):
                rule_broken = True
                break
    return rule_broken

def part_2(input):
    rules, updates = read_input(input)
    incorrect = []
    total = 0
    for update in updates:
        if check_update(rules, update):
            incorrect.append(update)
   
    correct_order = []

    for update in incorrect:
        while check_update(rules, update):
            for rule in rules:
                if all(elem in update for elem in rule):
                    i_1 = update.index(rule[0])
                    i_2 = update.index(rule[1])
                    if i_1 > i_2:
                        update[i_1] = rule[1]
                        update[i_2] = rule[0]
        correct_order.append(update)
    
    for update in correct_order:
        middle = int(len(update) / 2)
        total += update[middle]
    return total

print(part_2("input.txt"))