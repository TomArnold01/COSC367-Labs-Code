mirror(leaf(X), leaf(Y)):- X = Y.
mirror(tree(L1, R1), tree(L2, R2)):- mirror(L1,R2), mirror(R1, L2).

