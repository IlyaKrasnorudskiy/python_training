n = input()
mas_spend = []
mas_required = []
for i in range(0, int(n)):
    elem_spend, elem_required = input().split()
    mas_spend.append(int(elem_spend))
    mas_required.append(int(elem_required))

def proc_energy(spend, required):
    current_energy = 0
    all_energy = 0

    for i in range(0, len(spend)):
        all_energy = max(current_energy + int(required[i]), all_energy)
        current_energy += int(spend[i]) - int(required[i])
    return all_energy


print(proc_energy(mas_spend, mas_required))
print(0%2)