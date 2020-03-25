def intervalle(i, j):
    if i >= j:
        return i
    else:
        print("%.2f\n"%i)
        return intervalle(i+0.01, j)

intervalle(0, 5)