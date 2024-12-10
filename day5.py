from typing import Dict, Tuple


RulePair = Tuple[int, ...] # Could be more strict and say Tuple[int, int], but the assertions get annoying
Rules = Tuple[RulePair, ...]
Update = Tuple[int, ...]
Updates = Tuple[Update, ...]

def get_rules_and_updatess(input: str) -> Tuple[Rules, Updates]:
  rules, updates_str = input.split('\n\n')
  updates_lines = updates_str.split('\n')
  clean_line = lambda line: tuple(int(updates) for updates in line.split(','))
  updatess = updates = tuple(clean_line(line) for line in updates_lines)
  rule_pairs = tuple(tuple(int(e) for e in rule.split('|'))
    for rule in rules.split('\n'))
  return (rule_pairs, updatess)

##############
### Part 1 ###
##############

def get_legal_updates(input: str) -> Tuple[Updates, ...]:
  rules, updatess = get_rules_and_updatess(input)
  rules_dict: Dict[int, Tuple[int, ...]] = {}
  for rule in rules:
    rules_dict[rule[0]] = rules_dict.setdefault(rule[0], tuple()) + (rule[1],)

  def update_legal(updates: Tuple[int, ...]) -> bool:
    return not any(
        any(j in rules_dict.get(update, []) for j in updates[:i])
          for i, update in enumerate(updates))

  legal_updates = tuple(filter(update_legal, updatess))

def get_legal_sum(input: str) -> int:
  legal_updates = get_legal_updates(input)
  return sum(update[(len(update)-1)//2] for update in legal_updates)

##############
### Part 2 ###
##############

def get_ordering(input: Rules) -> Tuple[int]:
  return ...

def get_updated_sum(input: str) -> int:
  rules, updatess = get_rules_and_updatess(input)
  legal_updates = get_legal_updates(input)
  illegal_updates = tuple(filter(lambda u: u not in legal_updates, updatess))
  ordering = get_ordering(rules)
  reordered_updates = tuple(sorted(update,
      key=lambda u: ordering.get_index(u)) for update in illegal_updates)
  return sum(update[(len(update)-1)//2] for update in legal_updates)

##############

if __name__ == '__main__':

  input = '''...'''

  print(f'Sum of middle pages for legal updates: {get_legal_sum(input)}')
  print(f'Sum of middle pages for reordered illegal updates {get_updated_sum(input)}')
