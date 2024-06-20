import csv
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

def main():

    prior = learn_prior("spam-labelled.csv")
    print("Prior probability of spam is {:.5f}.".format(prior))

    prior = learn_prior("spam-labelled.csv")
    print("Prior probability of not spam is {:.5f}.".format(1 - prior))


    prior = learn_prior("spam-labelled.csv", pseudo_count = 1)
    print(format(prior, ".5f"))


    prior = learn_prior("spam-labelled.csv", pseudo_count = 2)
    print(format(prior, ".5f"))


    prior = learn_prior("spam-labelled.csv", pseudo_count = 10)
    print(format(prior, ".5f"))


    prior = learn_prior("spam-labelled.csv", pseudo_count = 100)
    print(format(prior, ".5f"))


    prior = learn_prior("spam-labelled.csv", pseudo_count = 1000)
    print(format(prior, ".5f"))

if __name__ == "__main__":
    main()