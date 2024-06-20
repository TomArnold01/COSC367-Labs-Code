from itertools import product

def joint_prob(network, assignment):
    p = 1
    for var in network:
        if var in assignment:
            value = assignment[var]
            info = network[var]
            p_var = tuple(assignment[i] for i in info['Parents'])
            if value:
                p *= info['CPT'][p_var]
            else:
                p *= (1- info['CPT'][p_var])
        else:
            continue

    return p


def query(network, query_var, evidence):
    
    hidden_vars = network.keys() - evidence.keys() - {query_var}

    raw_dist = {True: 0, False: 0}
     
    assignment = dict(evidence)
    
    for query_value in {True, False}:
        assignment[query_var] = query_value
        
        for values in product((True, False), repeat=len(hidden_vars)):
            hidden_assignments = {var:val for var,val in zip(hidden_vars, values)}
            
            for key, item in hidden_assignments.items():
                assignment[key] = item
            
            p = joint_prob(network, assignment)
            raw_dist[query_value] += p
    
    norm = sum(raw_dist[p] for p in raw_dist)
    
    for key, p in raw_dist.items():
        raw_dist[key] = p/norm
    return raw_dist



def main():


    network = {
        'A': {
            'Parents': [],
            'CPT': {
                (): 0.2
                }},
    }

    answer = query(network, 'A', {})
    print("P(A=true) = {:.5f}".format(answer[True]))
    print("P(A=false) = {:.5f}".format(answer[False]))


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
    
    answer = query(network, 'B', {'A': False})
    print("P(B=true|A=false) = {:.5f}".format(answer[True]))
    print("P(B=false|A=false) = {:.5f}".format(answer[False]))


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
    
    answer = query(network, 'B', {})
    print("P(B=true) = {:.5f}".format(answer[True]))
    print("P(B=false) = {:.5f}".format(answer[False]))


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

    answer = query(network, 'Burglary', {'John': True, 'Mary': True})
    print("Probability of a burglary when both\n"
        "John and Mary have called: {:.3f}".format(answer[True]))                        


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

    answer = query(network, 'John', {'Mary': True})
    print("Probability of John calling if\n"
        "Mary has called: {:.5f}".format(answer[True])) 

if __name__ == "__main__":
    main()