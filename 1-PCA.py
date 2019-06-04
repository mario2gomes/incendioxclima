import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from sklearn.decomposition import PCA
plt.rcParams.update({'font.size': 40})

pd.set_option('display.notebook_repr_html', False)

plt.style.use('seaborn-white')
# In R, I exported the dataset to a csv file. It is part of the base R distribution.

ano='2009'
df = pd.read_excel('tabelas/0DADOS'+ano+'.xlsx', sheetname=0)
print(df)
print("\nMédia\n")
print(df.mean())
print("\nVariância\n")
print(df.var())
X = pd.DataFrame(scale(df), index=df.index, columns=df.columns)
# The loading vectors
pca_loadings = pd.DataFrame(PCA().fit(X).components_.T, index=df.columns, columns=['V1', 'V2', 'V3', 'V4','V5'])
print("\nPCA_Loadings\n")
print(pca_loadings)
# Fit the PCA model and transform X to get the principal components
pca = PCA()
df_plot = pd.DataFrame(pca.fit_transform(X), columns=['PC1', 'PC2', 'PC3', 'PC4','PC5'], index=X.index)
print(df_plot)
fig , ax1 = plt.subplots(figsize=(17,13))
ax1.set_xlim(-3.5,3.5)
ax1.set_ylim(-3.5,3.5)
# Plot Principal Components 1 and 2
for i in df_plot.index:
    ax1.annotate(i, (-df_plot.PC1.loc[i], -df_plot.PC2.loc[i]), ha='center')
# Plot reference lines
ax1.hlines(0,-3.5,3.5, linestyles='dotted', colors='grey')
ax1.vlines(0,-3.5,3.5, linestyles='dotted', colors='grey')
ax1.set_xlabel('Primeiro Componente Principal')
ax1.set_ylabel('Segundo Componente Principal')    
# Plot Principal Component loading vectors, using a second y-axis.
ax2 = ax1.twinx().twiny() 
ax2.set_ylim(-1,1)
ax2.set_xlim(-1,1)
ax2.tick_params(axis='y', colors='orange')
#ax2.set_xlabel('PCA', color='green')
# Plot labels for vectors. Variable 'a' is a small offset parameter to separate arrow tip and text.
a = 1.1
for i in pca_loadings[['V1', 'V2']].index:
    if i=='INCÊNDIOS':
        ax2.annotate(i, (-pca_loadings.V1.loc[i]*a, -pca_loadings.V2.loc[i]*a), color='red', fontsize=40)
    else:
        ax2.annotate(i, (-pca_loadings.V1.loc[i]*a, -pca_loadings.V2.loc[i]*a), color='green', fontsize=40)
# Plot vectors
ax2.arrow(0,0,-pca_loadings.V1[0], -pca_loadings.V2[0])
ax2.arrow(0,0,-pca_loadings.V1[1], -pca_loadings.V2[1])
ax2.arrow(0,0,-pca_loadings.V1[2], -pca_loadings.V2[2])
ax2.arrow(0,0,-pca_loadings.V1[3], -pca_loadings.V2[3])
ax2.arrow(0,0,-pca_loadings.V1[4], -pca_loadings.V2[4])
plt.savefig('resultados/'+ano+'-incendioxclima.png')
plt.show()