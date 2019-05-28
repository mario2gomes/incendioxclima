# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 19:31:41 2017

@author: mário
"""

import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

caminho = '../planilhas/finais/'
ano = '2007-9'
atributos = (('DADOS',' - vento.xlsx','vento'),('DADOS',' - temperatura.xlsx','temperatura'),
             ('DADOS',' - umidade.xlsx','umidade'),('DADOS',' - chuva.xlsx','chuva'))

for (a,b,c) in atributos:

    print ('\n\nCorrelação '+c+' x Incêndios em '+ano+' :\n\n')

    train_dataset = pd.read_excel(caminho+a+ano+b)
    X = train_dataset[c]
    Y = train_dataset['incendios']    
    print(X,Y)

#slope = inclinacao
    slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)
    erroquadratico = r_value**2
    
    resultado = {
            'medida': ['erroquadratico', '(Beta)inclinação', '(Alpha)interceptação','coeficiente de correlação','P_value','Erro do desvio padrão'],
            'valor': [erroquadratico, slope, intercept,r_value,p_value,std_err]
            }
    resultado = pd.DataFrame(resultado, columns=['medida','valor'])
    print (resultado)

    plt.title('Modelo de regressão linear '+c)
    plt.xlabel(c)
    plt.ylabel('incendios')
    plt.plot(X,Y,'o', label='original_data')
    plt.plot(X, intercept + slope*X, 'r', label = 'fitted_line')
    plt.legend()
    plt.savefig('resultados/regressao_plot'+ano+c+'.png')
    resultado.to_excel('resultados/regressao_resultado'+ano+c+'.xlsx')
    plt.show()
    
    
    
    