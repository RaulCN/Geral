from sklearn import tree


lisa=1
irregular=0
maça=1
laranja=0

pomar=[[150, lisa], [130, lisa], [180, irregular], [160, irregular]]

resultado=[maça, maça, laranja, laranja]

clf=tree.DecisionTreeClassifier()
clf=clf.fit(pomar,resultado)

peso=input("Entre com o peso: ")
superficie=input("Entre com a superficie (1 para lisa, 0 para irregular): ")

resultadoUsuario=clf.predict([[peso, superficie]])

if resultadoUsuario==1:
    print("É uma maçã")
else:
    print("É uma laranja")
    