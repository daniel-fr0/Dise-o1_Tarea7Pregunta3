from KMP import kmpPre

# tomando el preprocesamiento que realiza el algoritmo KMP
# podemos encontrar el número de veces que se repite un patrón
# en particular podemos encontrar el prefijo más largo que es sufijo
# de un string dado.

def presufijo(str):
	b = kmpPre(str)
	# se retorna el sufijo más largo que es prefijo
	return str[:b[-1]]

print("something seventy seven:", presufijo("something seventy seven"))
print("seventy seven:", presufijo("seventy seven"))
print("abracadabra:", presufijo("abracadabra"))
print("arepera:", presufijo("arepera"))
print("algoritmo:", presufijo("algoritmo"))
print("aaaaa:", presufijo("aaaaa"))
print("aaaa:", presufijo("aaaa"))
print("aaa:", presufijo("aaa"))
print("aa:", presufijo("aa"))
print("a:", presufijo("a"))