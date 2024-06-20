
network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.1
            }},
    'B': {
        'Parents': ['A'],
        'CPT': {
            (False,): 0.1,
            (True,): 0.1
            }},
            
    'C': {
        'Parents': ['A'],
        'CPT': {
            (False,): 0.1,
            (True,): 0.1
            }},
}

def main():
    
    print(sorted(network.keys()))

if __name__ == "__main__":
    main()