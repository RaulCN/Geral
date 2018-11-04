#Regression
library (ISwR)
attach (thuesen)
names (thuesen)

#Verificar o modelo linear
lm(short.velocity~blood.glucose)

#extrair outras funções do lm:
summary(lm(short.velocity~blood.glucose))
#gráfico de pontos e da reta de regressão
plot(blood.glucose, short.velocity)
abline(lm(short.velocity~blood.glucose))

#Resíduos e valores estimados 
lm.velo <- lm(short.velocity~blood.glucose)
fitted(lm.velo)#Valores estimados de acordo com o melhor ajuste 
resid(lm.velo) #diferença entre os valores e os observados

plot(blood.glucose,short.velocity)
lines(blood.glucose,fitted(lm.velo))
#trabalhando sem os dados faltantes, melhor opção
options(na.action = na.exclude)
segments(blood.glucose,fitted(lm.velo), blood.glucose,short.velocity)
abline(lm(short.velocity~blood.glucose))