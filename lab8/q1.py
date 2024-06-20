







def joint_prob(network, assignment):
    p = 1
    for var in network:
        if var in assignment:
            print(var)
            value = assignment[var]
            print(value)
            info = network[var]
            print(info)
            p_var = tuple(assignment[i] for i in info['Parents'])
            print(p_var)
            if value:
                print(info['CPT'][p_var])
                p *= info['CPT'][p_var]
                print("p*=")
                print(p)
                print()
            else:
                print(info['CPT'][p_var])
                p *= (1- info['CPT'][p_var])
                print("1-")
                print(p)
                print()
        else:
            continue

    return p






def main():
 
    network = {
        'A': {
            'Parents': [],
            'CPT': {
                (): 0.1
                }},
                
        'B': {
            'Parents': ['A'],
            'CPT': {
                (True,): 0.8,
                (False,): 0.7,
                }},
        }
    
    p = joint_prob(network, {'A': False, 'B':True})
    print("{:.5f}".format(p)) 


    network = {
        'A': {
            'Parents': [],
            'CPT': {
                (): 0.1
                }},
                
        'B': {
            'Parents': ['A'],
            'CPT': {
                (True,): 0.8,
                (False,): 0.7,
                }},
        }
    
    p = joint_prob(network, {'A': False, 'B':False})
    print("{:.5f}".format(p))
    p = joint_prob(network, {'A': False, 'B':True})
    print("{:.5f}".format(p))
    p = joint_prob(network, {'A': True, 'B':False})
    print("{:.5f}".format(p))
    p = joint_prob(network, {'A': True, 'B':True})
    print("{:.5f}".format(p)) 
    print("*******************************************")
          


    network = {
        'Burglary': {
            'Parents': [],
            'CPT': {
                (): 0.001
                }},
                
        'Earthquake': {
            'Parents': [],
            'CPT': {
                (): 0.002,
                }},
        'Alarm': {
            'Parents': ['Burglary','Earthquake'],
            'CPT': {
                (True,True): 0.95,
                (True,False): 0.94,
                (False,True): 0.29,
                (False,False): 0.001,
                }},

        'John': {
            'Parents': ['Alarm'],
            'CPT': {
                (True,): 0.9,
                (False,): 0.05,
                }},

        'Mary': {
            'Parents': ['Alarm'],
            'CPT': {
                (True,): 0.7,
                (False,): 0.01,
                }},
        }

    p = joint_prob(network, {'John': True, 'Mary': True,
                            'Alarm': True, 'Burglary': False,
                            'Earthquake': False})
    print("{:.8f}".format(p)) 
    


if __name__ == "__main__":
    main()