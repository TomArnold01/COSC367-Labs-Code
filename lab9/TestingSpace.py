import csv
def learn_likelihood(file_name, pseudo_count=0):
    with open(file_name) as in_file:
        data = [tuple(row) for row in csv.reader(in_file)]
    likelihood = []
    for i in range(12):
        correct_count = 0 #correct Count
        incorrect_count = 0 #incorrect Count
        tot_correct_count = 0 #Total correct Count
        tot_incorrect_count = 0 #Total incorrect Count        
        for j in range(1, len(data)):
            if data[j][-1] == '1':
                if data[j][i] == '1':
                    correct_count += 1
                tot_correct_count += 1
            else:
                if data[j][i] == '1':
                    incorrect_count += 1
                tot_incorrect_count += 1
        likelihood.append(((incorrect_count + pseudo_count) / (tot_incorrect_count + (2*pseudo_count)),
                          (correct_count + pseudo_count) / (tot_correct_count + (2*pseudo_count))))
    return likelihood

def posterior(prior, likelihood, observation):
    correct = prior
    incorrect = (1-prior)
    for i in range(len(observation)):
        if observation[i]:
            correct *= likelihood[i][True]
            incorrect *= likelihood[i][False]
        else:
            correct *= 1 - likelihood[i][True]
            incorrect *= 1 - likelihood[i][False]
    normal = correct + incorrect
    return correct / normal


def learn_prior(file_name, pseudo_count=0):
        with open(file_name) as in_file:
                data = [tuple(row) for row in csv.reader(in_file)]
        correct_count = 0
        incorrect_count = 0
        for i in range(1, len(data)):
                if data[i][-1] == '1':
                        correct_count += 1
                else:
                        incorrect_count += 1
        total_count = correct_count + incorrect_count
        return (correct_count + pseudo_count) / (total_count + (2*pseudo_count))


def nb_classify(prior, likelihood, input_vector):
    p = posterior(prior, likelihood, input_vector)
    if p <= 0.5:
        return (("Not Spam", 1 - p))
    else:
        return (("spam", p))

       

def main():

    prior = learn_prior("spam-labelled.csv")
    likelihood = learn_likelihood("spam-labelled.csv")

    input_vectors = [
        (1,1,0,0,1,1,0,0,0,0,0,0),
        (0,0,1,1,0,0,1,1,1,0,0,1),
        (1,1,1,1,1,0,1,0,0,0,1,1),
        (1,1,1,1,1,0,1,0,0,1,0,1),
        (0,1,0,0,0,0,1,0,1,0,0,0),
        ]

    predictions = [nb_classify(prior, likelihood, vector) 
                for vector in input_vectors]

    for label, certainty in predictions:
        print("Prediction: {}, Certainty: {:.5f}"
            .format(label, certainty))

    prior = learn_prior("spam-labelled.csv", pseudo_count=1)
    likelihood = learn_likelihood("spam-labelled.csv", pseudo_count=1)

    input_vectors = [
        (1,1,0,0,1,1,0,0,0,0,0,0),
        (0,0,1,1,0,0,1,1,1,0,0,1),
        (1,1,1,1,1,0,1,0,0,0,1,1),
        (1,1,1,1,1,0,1,0,0,1,0,1),
        (0,1,0,0,0,0,1,0,1,0,0,0),
        ]

    predictions = [nb_classify(prior, likelihood, vector) 
                for vector in input_vectors]

    for label, certainty in predictions:
        print("Prediction: {}, Certainty: {:.5f}"
            .format(label, certainty))
        
if __name__ == "__main__":
    main()