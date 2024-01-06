not_uniq_str = 'съешь же ещё этих мягких французских булок да выпей чаю'
uniq_str = set(not_uniq_str.replace(' ', ''))
uniq = len(uniq_str)

print(uniq)
