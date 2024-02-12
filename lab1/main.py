import numpy as np
import numpy.matlib
import sympy as sp
import matplotlib.pyplot as plt

def uzd1(a: float = -1.3, b: float = 2.5, n: int = 64):
    """Padalinkite intervalą nuo -1.3 iki 2.5 tolygiai į 64 dalis."""
    ans = [a+(b-a)/n*e for e in range(n+1)]
    ans = list(zip(ans[:-1], ans[1:]))
    return ans
print(uzd1(), end='\n\n')

def uzd2(arr: list[int] = [1, 2, 3, 4], n: int = 4):
    """Sukonstruokite pasikartojantį masyvą pagal duotą N.
    Duotas masyvas [1, 2, 3, 4] ir N = 3
    Rezultatas [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
    Masyvas gali būti bet kokio dydžio ir atsitiktinai sugeneruojamas.
    """
    return arr * n
print(uzd2(), end='\n\n')

def uzd3(num: int = 3, n: int = 4):
    """
    Sukurkite masyvą iš pasikartojančių elementų.
    Duotas skaičius 3 ir pasikartojimų skaičius 4.
    Rezultatas [3, 3, 3, 3]
    """
    return [num] * n
print(uzd3(), end='\n\n')

def uzd4(x: int = 10, y: int = 10):
    """Sukurkite masyvą dydžio 10 x 10 iš nulių "įrėmintų" vienetais."""
    if x <= 2 or y <= 2:
        return [[1]*x]*y
    return (
        [[1]*x] + 
        [[1]+[0]*(x-2)+[1]]*(y-2) + 
        [[1]*x]
    )
[print(line) for line in uzd4()]
print()

def uzd5(n: int = 8):
    """Sukurkite masyvą dydžio 8 x 8, kur 1 ir 0 išdėlioti šachmatine tvarka."""
    return [[(i+j)%2 for i in range(n)]
                     for j in range(n)]
[print(line) for line in uzd5()]
print()

def uzd6(n: int = 8):
    """Sukurkite masyvą dydžio n×n , kurio (i,j)-oji pozicija lygi i+j."""
    return [[i+j for i in range(n)]
                  for j in range(n)]
[print(line) for line in uzd6()]
print()

def uzd7(n: int = 5, col: int = 2):
    """
    Sukurkite atsitiktinį masyvą dydžio 5x5 naudodami np.random.rand(5, 5). Surūšiuokite eilutes pagal antrąjį stulpelį. 
    Užuominos - slicing, argsort, indexing.
    """
    return sorted(np.random.rand(n, n).tolist(), key=lambda x: x[col-1])
[print(line) for line in uzd7()]
print()

def uzd8(matrix: np.matrix):
    """Apskaičiuokite matricos tikrines reikšmes ir tikrinį vektorių."""
    return list(np.linalg.eig(matrix))
print(uzd8(np.matlib.mat([[4,2],[1,3]])), end='\n\n')

def uzd9():
    """
    Apskaičiuokite funkcijos 0.5*x**2 + 5 * x + 4 išvestines su numpy ir sympy paketais.
    Užuominos - poly1d, deriv, diff
    """
    x = sp.symbols('x')
    return sp.diff((0.5*x**2 + 5*x + 4), x)
print(uzd9(), end='\n\n')

def uzd10():
    """Apskaičiuokite funkcijos e-x apibrėžtinį, intervale [0,1], ir neapibrėžtinį integralus."""
    x = sp.symbols('x')
    return (
        sp.integrate(sp.exp(-x), x),
        sp.integrate(sp.exp(-x), (x, 0, 1))
    )
print(uzd10(), end='\n\n')

input()
def uzd11():
    """Pasinaudodami polinėmis koordinatėmis nupieškite kardioidę."""
    # (np.cos(theta) + 1)
    theta = np.linspace(0, 2 * np.pi, 1000)
    plt.figure(figsize=(6, 6))
    my_plot = plt.subplot(111, polar=True)
    my_plot.plot(theta, np.cos(theta)+1)
    plt.show()
    # i don't know what the f am I looking at.
    pass
uzd11()

def uzd12():
    """
    Sugeneruokite masyvą iš 1000 atsitiktinių skaičių, pasiskirsčiusių pagal 
    normalųjį dėsnį su duotais vidurkiu V ir dispersija D. Nupieškite jų histogramą.
    """
    nums = np.random.normal(0, np.sqrt(1), 1000)
    plt.hist(nums, bins=70)
    plt.show()
uzd12()