



def interpretations(atoms):
    distinct_val = 2**(len(atoms))
    poss_vals = [False, True]
    results = []

    for i in range(distinct_val):
        result = dict()
        bin_str = format(i, '0' + str(len(atoms)) + 'b')

        for j, atom in enumerate(atoms):
            result[atom] = bool(int(bin_str[j]))
        
        results.append(result)

    return results

        
        
def main():
    atoms = {'q', 'p'}
    for i in interpretations(atoms):
        print(i)


if __name__ == "__main__":
    main()

