import matplotlib.pyplot as plt
x = ['sedan', 'suv', 'pickup', 'utilitario', 'cuatriciclo']
y = [134000, 45000, 234000, 38000, 21600]
fig, ax = plt.subplots()
ax.bar(x, y)  # barras
ax.set(title='kilometraje por tipos de autos', xlabel='tipos de autos', ylabel='kilometraje')
plt.savefig('grafico.png')
plt.show()


import pandas as pd
x = tipos_autos = pd.Series(['sedan', 'suv', 'pickup', 'utilitario', 'cuatriciclo'])
y = kilometraje = pd.Series([134000, 45000, 234000, 38000, 21600])
df = pd.DataFrame({'Tipo de autos': tipos_autos, 'Kilometraje': kilometraje})
fig, ax = plt.subplots()
ax.bar(df['Tipo de autos'], df['Kilometraje'])
ax.set(title='kilometraje por tipos de autos', xlabel=df.keys()[0], ylabel=df.keys()[1])
plt.show()

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))
fig.tight_layout(pad=5.0)
ax1.bar(df['Tipo de autos'], df['Kilometraje'])
ax1.set(title='kilometraje por tipos de autos', xlabel=df.keys()[0], ylabel=df.keys()[1])
ax2.barh(df['Tipo de autos'], df['Kilometraje'])
ax2.set(title='kilometraje por tipos de autos', ylabel=df.keys()[0], xlabel=df.keys()[1])
ax3.bar(df['Tipo de autos'], df['Kilometraje'])
ax3.set(title='kilometraje por tipos de autos', xlabel=df.keys()[0], ylabel=df.keys()[1])
ax4.stackplot(df['Tipo de autos'], df['Kilometraje'])
ax4.set(title='kilometraje por tipos de autos', xlabel=df.keys()[0], ylabel=df.keys()[1])
plt.show()

x = ['sedan', 'suv', 'pickup', 'utilitario', 'cuatriciclo']
y = [134000, 45000, 234000, 38000, 21600]
colores = ['tab:red', 'tab:blue', 'tab:gray', 'tab:purple']
fig, ax = plt.subplots()
ax.bar(x, y, label=x, color=colores) # barras
ax.legend(title='por color')
ax.set(title='kilometraje por tipos de autos', xlabel='tipos de autos', ylabel='kilometraje')
plt.show()

import seaborn as sns
x = ['sedan', 'suv', 'pickup', 'utilitario', 'cuatriciclo']
y = [134000, 45000, 234000, 38000, 21600]
colores = ['tab:red', 'tab:blue', 'tab:gray', 'tab:purple']
sns.set_theme(style="darkgrid")
fig, ax = plt.subplots()
ax.set(title='kilometraje por tipos de autos', xlabel='tipos de autos', ylabel='kilometraje')
sns.barplot(x=x, y=y, ax=ax)
plt.show()
