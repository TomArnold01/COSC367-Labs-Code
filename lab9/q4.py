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
       

def main():
      

    likelihood = learn_likelihood("spam-labelled.csv")
    print(len(likelihood))
    print([len(item) for item in likelihood])
    
    likelihood = learn_likelihood("spam-labelled.csv")

    print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
    print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
    print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
    print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))


    likelihood = learn_likelihood("spam-labelled.csv", pseudo_count=1)

    print("With Laplacian smoothing:")
    print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
    print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
    print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
    print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))

if __name__ == "__main__":
    main()