
def alg_euclides(a, b) -> str:
    if a < b:
        a, b = b, a #swap a and b, a=b and b=a
    while b != 0:
        a, b = b, a%b
    return a

def alg_ext_euclides(a, b) -> str:
    swap_u_v = False
    if a < b:
        a, b = b, a 
        swap_u_v = True

    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    if swap_u_v:
        old_s, old_t = old_t, old_s
        return r,old_s,old_t
    else:
        return r,old_s,old_t
        
def congruencia_lineal(a, b, m) -> str:
    mcd = alg_euclides(a, m)
    if b % mcd == 0:
        a = a // mcd
        b = b // mcd
        m = m // mcd

        a = a % m
        b = b % m

        r, s, t = alg_ext_euclides(a, m)
        x = (b * s) % m

        return x, m
    else:
        return False, False
    
def ecuacion_diofantica(a, b, c) -> str:

    if (b < 0): 
        b=b * -1


    mcd = alg_euclides(a, b)
    if c % mcd == 0:
        x , m = congruencia_lineal(a, c, b)

        aux1 = a * x
        aux2 = a * m

        aux1 = aux1 - c

        aux1 = aux1 // b
        aux2 = aux2 // b

        y = aux1 
        n = aux2

        return ("{El conjunto de todas las soluciones es (x,y) = (" + str(x) + " + (" + str(m) + ")k, " + str(y) + " + (" + str(n) + ")k), con k ∈ Z}\n")
    else:
        return ("La ecuación no tiene solución: " + str(a) + "x + " + str(b) + "y = " + str(c) + "\n")
    
