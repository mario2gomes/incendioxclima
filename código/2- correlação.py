# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 19:31:41 2017

@author: mário
"""

import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

caminho = '../tabelas/'
atributos = (('DADOS2009 - vento.xlsx','vento'),('DADOS2009 - temperatura.xlsx','temperatura'),
             ('DADOS2009 - humidade.xlsx','humidade'),('DADOS2009 - chuva.xlsx','chuva'))

for (a,b) in atributos:

    print ('\n\nCorrelação '+b+' x Incêndios\n\n')

    train_dataset = pd.read_excel(caminho+a)
    X = train_dataset[b]
    Y = train_dataset['incendios']

#slope = inclinacao
    slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)
    erroquadratico = r_value**2
    print("erro quadrático: {:.5f}".format(erroquadratico))
    
    print("(Beta)_Inclinacao: {:.2f}".format(slope))
    print("(Alpha)_intercept: {:.2f}".format(intercept))
    print("Coeficiente__Correlacao: {:.5f}".format(r_value))

    print ("P_Value: {:5.2f}".format(p_value))
    print("Erro_do_Desvio_Padrao: {:.2f}".format(std_err))

    plt.title('Modelo de regressão linear '+b)
    plt.xlabel(b)
    plt.ylabel('incendios')
    plt.plot(X,Y,'o', label='original_data')
    plt.plot(X, intercept + slope*X, 'r', label = 'fitted_line')
    plt.legend()
    plt.savefig('../imagens/plotlinearregression'+b+'.png')
    plt.show()