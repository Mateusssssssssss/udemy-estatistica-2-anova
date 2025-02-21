import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import MultiComparison
import matplotlib.pyplot as plt
#Carregar os dados
dados = pd.read_csv('anova.csv', sep=';')
print(dados)
#boxplot agrupando os dados por remedio
graf = dados.boxplot(by='Remedio', grid=False)
plt.show()

#Criação do modelo de regressão linear  e execução do teste
#ols (Mínimos Quadrados Ordinários) 
modelo1 = ols('Horas ~ Remedio', dados).fit()
resultado1 = sm.stats.anova_lm(modelo1)
#observar valor de p maior que 0.05(PR(>F)) hipotese nula de que não há diferença significativa 
# entre os diferentes remedios.
print(resultado1)

#Criação do modelo segundo modelo utilzando mais atributos e execução do teste
modelo2 = ols('Horas ~ Remedio * Sexo', dados).fit()
resultado2 = sm.stats.anova_lm(modelo2)

print(resultado2)

#se houver diferença o teste de turkey é executado
#execução do teste de turkey e visualização dos graficos com os resultados
mc = MultiComparison(dados['Horas'], dados['Remedio'])
resultado_teste = mc.tukeyhsd()
#Vemos que não há diferença significativa entre os remedios pois valores de p > 0.05
print(resultado_teste)
resultado_teste.plot_simultaneous()
plt.show()





