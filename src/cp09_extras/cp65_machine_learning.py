import pandas as pd
from matplotlib import pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, ConfusionMatrixDisplay
from sklearn import tree
import seaborn as sns


df = pd.read_csv('DataSet_Titanic.csv')
X = df.drop('Sobreviviente', axis=1)
y = df.Sobreviviente


# Crear un árbol para poder entrenarlo
arbol = DecisionTreeClassifier()
# arbol = DecisionTreeClassifier(max_depth=4)


# Entrenar a la máquina
arbol.fit(X, y)


# Predecir quiénes podrían haber vivido
pred_y = arbol.predict(X)


# Y comparamos el resultado de la predicción con la realidad
print('Precisión: ', accuracy_score(pred_y, y))


# Esto también se puede observar desde una matriz de confusión
ConfusionMatrixDisplay.from_estimator(arbol, X, y, cmap=plt.cm.Blues, values_format='.0f')
ConfusionMatrixDisplay.from_estimator(arbol, X, y, cmap=plt.cm.Blues, values_format='.2f', normalize='true')


# Ver cómo fue tomando las decisiones
plt.figure(figsize=(100, 80))
tree.plot_tree(arbol, filled=True, feature_names=X.columns)
# valor gini => mientras menor sea su valor, mayor es la probabilidad de acierto
plt.savefig('arbol.png')
plt.show()


# Ver cuál fue la importancia de cada categoría:
importancias = arbol.feature_importances_
columnas = X.columns
sns.barplot(x=columnas, y=importancias)
plt.title('Importancia de cada atributo')
plt.show()
