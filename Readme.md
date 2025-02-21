# **Análise de Variância (ANOVA) e Teste de Tukey**

Este documento descreve um script em Python que realiza uma análise de variância (ANOVA) e, se necessário, aplica o **Teste de Tukey** para comparação múltipla entre grupos.

## **Requisitos**

Antes de executar o código, instale as seguintes bibliotecas:

```bash
pip install pandas scipy statsmodels matplotlib
```

## **Descrição do Código**

### **1. Importação das Bibliotecas**

O script utiliza as seguintes bibliotecas para manipulação de dados, análise estatística e visualização:

- **pandas**: Manipulação de dados.
- **scipy**: Funções estatísticas.
- **statsmodels**: Modelagem estatística e execução da ANOVA.
- **matplotlib**: Visualização de dados.

```python
import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import MultiComparison
import matplotlib.pyplot as plt
```

---

### **2. Carregamento dos Dados**

Os dados são carregados de um arquivo CSV chamado `anova.csv` que utiliza `;` como separador:

```python
dados = pd.read_csv('anova.csv', sep=';')
print(dados)
```

---

### **3. Visualização dos Dados**

Um boxplot é gerado para visualizar a distribuição da variável **Horas** agrupada por **Remedio**:

```python
graf = dados.boxplot(by='Remedio', grid=False)
plt.show()
```

---

### **4. Teste ANOVA**

A Análise de Variância (ANOVA) verifica se existem diferenças estatisticamente significativas entre as médias dos grupos.

#### **Modelo 1: Apenas "Remedio"**

Este modelo avalia se a variável **Horas** difere significativamente entre os grupos de **Remedio**:

```python
modelo1 = ols('Horas ~ Remedio', dados).fit()
resultado1 = sm.stats.anova_lm(modelo1)
print(resultado1)
```

Se o valor de p (**PR(>F)**) for maior que 0.05, não há evidência de diferença significativa entre os grupos.

---

#### **Modelo 2: Interação entre "Remedio" e "Sexo"**

Este modelo inclui também a interação entre **Remedio** e **Sexo** para avaliar possíveis efeitos combinados:

```python
modelo2 = ols('Horas ~ Remedio * Sexo', dados).fit()
resultado2 = sm.stats.anova_lm(modelo2)
print(resultado2)
```

Caso o resultado indique diferenças significativas, é possível prosseguir para a etapa do teste pós-hoc.

---

### **5. Teste de Tukey**

Quando a ANOVA revela diferenças significativas, o **Teste de Tukey** é utilizado para identificar quais grupos apresentam diferenças estatísticas entre si. Esse teste pós-hoc ajusta os valores para múltiplas comparações, controlando o erro do tipo I.

```python
mc = MultiComparison(dados['Horas'], dados['Remedio'])
resultado_teste = mc.tukeyhsd()
print(resultado_teste)
resultado_teste.plot_simultaneous()
plt.show()
```

#### **O que é o Teste de Tukey?**

- **Objetivo:** Comparar todas as possíveis diferenças entre pares de médias dos grupos.
- **Procedimento:** Calcula a diferença entre as médias e a compara com um valor crítico ajustado para múltiplas comparações.
- **Interpretação dos Resultados:**  
  - **p > 0.05:** Não há diferença estatisticamente significativa entre os grupos.  
  - **p < 0.05:** Existe uma diferença estatisticamente significativa entre os grupos.

---

## **Conclusão**

Este script demonstra uma análise estatística completa que abrange desde a análise de variância até a realização do **Teste de Tukey** para comparações múltiplas. Essa abordagem é fundamental para identificar quais grupos apresentam diferenças significativas, garantindo a robustez dos resultados.