import numpy as np
from scipy.stats import poisson, expon
import matplotlib.pyplot as plt
import scipy as scipy


#data_poisson = scipy.stats.poisson.rvs(mu,size=1000)
data_poisson= [14,5,10,8,12,7]
#data_exponencial = scipy.stats.expon.rvs(size=1000)
data_exponencial= [25,20,45,25,13,52,45,25,38,42,55,45,15,70,20,28,30,55,32,58,65,10,85,50,13,10,30,45,15,30]



# Ajustar a la distribución Poisson
mu_poisson = np.mean(data_poisson)
poisson_fit = poisson(mu_poisson)
poisson_pmf = poisson_fit.pmf(np.arange(np.min(data_poisson), np.max(data_poisson)))

# Ajustar a la distribución exponencial
loc, scale = expon.fit(data_exponencial)
expon_fit = expon(loc=loc, scale=scale)
expon_pdf = expon_fit.pdf(np.linspace(np.min(data_exponencial), np.max(data_exponencial), 100))

# Prueba de bondad de ajuste de K-S para la distribución Poisson
ks_statistic_poisson, p_value_poisson = scipy.stats.kstest(data_poisson, lambda x: poisson_fit.cdf(x))
print("Prueba de bondad de ajuste de K-S para Poisson:")
print("Estadística de prueba =", ks_statistic_poisson)
print("Valor p =", p_value_poisson)
if p_value_poisson > 0.05:
    print("Los datos se ajustan bien a la distribución poisson")
else:
    print("Los datos no se ajustan bien a la distribución poisson")

# Prueba de bondad de ajuste de K-S para la distribución exponencial
ks_statistic_expon, p_value_expon = scipy.stats.kstest(data_exponencial, lambda x: expon_fit.cdf(x))
print("Prueba de bondad de ajuste de K-S para exponencial:")
print("Estadística de prueba =", ks_statistic_expon)
print("Valor p =", p_value_expon)
if p_value_expon > 0.05:
    print("Los datos se ajustan bien a la distribución exponencial")
else:
    print("Los datos no se ajustan bien a la distribución exponencial")


# Graficar el histograma de los datos y las distribuciones ajustadas
plt.hist(data_poisson, bins=range(np.max(data_poisson)+2), density=True, alpha=0.5, label="Datos Poisson")
plt.plot(np.arange(np.min(data_poisson), np.max(data_poisson)), poisson_pmf, "o-", label="Poisson")
plt.hist(data_exponencial, bins=50, density=True, alpha=0.5, label="Datos Exponencial")
plt.plot(np.linspace(np.min(data_exponencial), np.max(data_exponencial), 100), expon_pdf, "o-", label="Exponencial")
plt.legend()
plt.show()