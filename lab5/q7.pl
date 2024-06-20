preorder(leaf(Label), [Traversal]) :- Traversal = Label.
preorder(tree(Root, LS, RS), [Root|Traversal]) :- preorder(LS, LT), preorder(RS, RT), append(LT, RT, Traversal).
