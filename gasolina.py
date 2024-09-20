import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')
sns.lineplot(data=df, x='dia', y='venda')
plt.legend(labels=['Preço da gasolina']) ## fica meio redundante, porem colocarei mesmo assim
plt.xlabel('Dia')
plt.ylabel('Preço')
plt.title('Preço da gasolina')
plt.savefig('gasolina.png')

media = df['venda'].mean()
print(f'Preço médio: R$ {media:.2f}')