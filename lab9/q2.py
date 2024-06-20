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


def main():


    prior = 0.05
    likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))

    observation = (True, True, True)

    class_posterior_true = posterior(prior, likelihood, observation)
    print("P(C=False|observation) is approximately {:.5f}"
        .format(1 - class_posterior_true))
    print("P(C=True |observation) is approximately {:.5f}"
        .format(class_posterior_true))  

    prior = 0.05
    likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))

    observation = (True, False, True)

    class_posterior_true = posterior(prior, likelihood, observation)
    print("P(C=False|observation) is approximately {:.5f}"
        .format(1 - class_posterior_true))
    print("P(C=True |observation) is approximately {:.5f}"
        .format(class_posterior_true))  

    prior = 0.05
    likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))

    observation = (False, False, True)

    class_posterior_true = posterior(prior, likelihood, observation)
    print("P(C=False|observation) is approximately {:.5f}"
        .format(1 - class_posterior_true))
    print("P(C=True |observation) is approximately {:.5f}"
        .format(class_posterior_true))  

    prior = 0.05
    likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))

    observation = (False, False, False)

    class_posterior_true = posterior(prior, likelihood, observation)
    print("P(C=False|observation) is approximately {:.5f}"
        .format(1 - class_posterior_true))
    print("P(C=True |observation) is approximately {:.5f}"
        .format(class_posterior_true)) 

if __name__ == "__main__":
    main()