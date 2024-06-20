



network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.2 
            }},

    'C': {
        'Parents': [],
        'CPT': {
            (): 0.1
            }},

    'B': {
        'Parents': [],
        'CPT': {
            (): 0.7 
            }},

    'E': {
        'Parents': ['B'],
        'CPT': {
            (True,): 0.5, 
            (False,): 0.3,
            }},

    'D': {
        'Parents': ['B'],
        'CPT': {
            (True,): 0.5, 
            (False,): 0.6,
            }},

}

def main():
    
    print(sorted(network.keys()))

    bd_dependence = network['D']['CPT'][(False,)] != network['D']['CPT'][(True,)]
    be_dependence = network['E']['CPT'][(False,)] != network['E']['CPT'][(True,)]
    print(bd_dependence and be_dependence)

if __name__ == "__main__":
    main()