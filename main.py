import numpy as np

k = 1
def simplex(B, N, CN, CB, b, k):
    print("--------------ENTER---------------")
    print("k = ", k)
    B_inv = np.linalg.inv(B)
    print("Base = \n", B)
    print("N = \n", N)
    print("CN = ", CN)
    print("CB = ", CB)
    b_barre = B_inv.dot(b)

    print("B_barre = \n", b_barre)


    pi = CB.dot(B_inv)
    print("PI = ", pi)
    CN_barre = CN - pi.dot(N)
    print("CN barre = ", CN_barre)

    if check_cn(CN_barre)["is_pos"]:
        print("Check CN barre = ", check_cn(CN_barre)["is_pos"])
        print("B_barre solution = \n", b_barre)
        return print("solution find")
        
    else:
        s = check_cn(CN_barre)["i_col"]
        s_1 = check_cn(CN_barre)["elem"]
        print("------s = ------ = " , s_1, " -----indice----- = ", s)
        As = As_col(N,s)
        As_barre = B_inv.dot(As)
        print("As = ", As)
        print("Hellooooooo As_barre = ", As_barre)

        #while check_As(As_barre):
        if not check_As(As_barre):
            print("response = ", check_As(As_barre))
            print("not check as")
            answer = "No solution"
            return answer

        else:
            xs_tab = calcul_xs(b_barre, As_barre)
            print("----------here", k, "---------------")
            print("Xs_tab = ", xs_tab)
            indice_min = min_xs(xs_tab)["indice"]
            print("Min xs elem = ",min_xs(xs_tab)["elem_min"])
            print("Min xs indice = ",min_xs(xs_tab)["indice"])

            #at_cols = at_col(B, indice_min)
            print("------------- AS --------------------")
            print("As = ", np.array(As))
            print("-------------------------------------")
            new_bases = new_base(B, As, indice_min)
            new_Ns = new_N(B, N, indice_min, s)
            new_cn = new_CN(CN, CB, s, indice_min)
            new_cb = new_CB(CN, CB, s, indice_min)
            k = k + 1
            print("Base 2 = \n", new_bases)
            print("New 2 = \n", new_Ns)

            simplex(new_bases, new_Ns, new_cn, new_cb, b, k)
        
        # else:
        #     print("No solution")


def check_cn(A):
    resp = True
    i_line = 0
    i_col = 0
    elem_min = 100000
    for i_line,line in enumerate(A):
        for i_elem,elem in enumerate(line):
            if elem < 0 :
                i_line = i_line
                #i_col = i_elem
                resp = False
                if elem < elem_min:
                    elem_min = elem
                    i_col = i_elem
                
    negative_element = {
        "i_line": i_line,
        "i_col": i_col,
        "elem":elem_min,
        "is_pos": resp
    }
    return negative_element

def As_col(A,s):
    col = []
    for elem in A:
        col.append(elem[s])
    return col

def check_As(As):
    resp = False
    for line in As:
        if line > 0:
            resp = True
            break
    return resp

def calcul_xs(b_barre, As_barre):
    xs_tab = []
    for i in range(len(b_barre)):
        xs = b_barre[i][0] / As_barre[i]
        xs_tab.append(xs)
    
    return xs_tab

def min_xs(t):
    indice = 0
    elem_min = 1000
    for index, element in enumerate(t):
        if (element < elem_min) and (element > 0):
            elem_min = element
            indice = index
    
    return {
        "indice": indice,
        "elem_min": elem_min
    }

def at_col(M,indice):
    at_col = []
    for i in range(len(M)):
        at_col.append(M[i][indice])
    return at_col

def new_base(B, As, i):
    As_col = np.array(As)
    #print("As in function = ", As_col)
    B_d = np.delete(B, i, axis=1)
    B_a = np.insert(B_d, i, As_col, axis=1)
    #print("i in function = ", i)
    #print("B_d in function = \n", B_d)
    #print("B_a in function = \n", B_a)
    return B_a
    
def new_N(B, N, i, ind):
    At_col = np.array(at_col(B,i)) 
    N_d = np.delete(N, ind, axis=1)
    N_a = np.insert(N_d, ind, At_col, axis=1)
    return N_a
    
def new_CN(cn, cb, s_cn, ind_cb):
    cn_d = np.delete(cn, s_cn, axis=1)
    c_a = np.insert(cn_d, s_cn, cb[0][ind_cb], axis=1)
    return c_a

def new_CB(cn, cb, s_cn, ind_cb):
    cb_d = np.delete(cb, ind_cb, axis=1)
    cb_a = np.insert(cb_d, ind_cb, cn[0][s_cn], axis=1)
    return cb_a


# B = np.array([[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]])
# N = np.array([[-3.0,2.0],[-1.0,2.0],[1.0,1.0]])
# CB = np.array([[0.0,0.0,0.0]])
# CN = np.array([[-1.0,-2.0]])
# b = np.array([[2],[4],[5]])

# B = np.array([[1.0,0.0,0.0,0.0],[0.0,1.0,0.0,0.0],[0.0,0.0,-1.0,0.0],[0.0,0.0,0.0,-1.0]])
# N = np.array([[1.0, 1.0],[-1.0, 4.0], [1.0, 0.0],[0.0, 1.0]])
# CB = np.array([[0.0,0.0,0.0,0.0]])
# CN = np.array([[-3.0, -4.0]])
# b = np.array([[20],[20],[10],[5]])

# B = np.array([[1.0,0.0],[0.0,1.0]])
# N = np.array([[2.0, 4.0],[3.0, 1.0]])
# CB = np.array([[0.0, 0.0]])
# CN = np.array([[-6,-2]])
# b = np.array([[9],[6]])

# B = np.array([[-1.0,0.0],[0.0,1.0]])
# N = np.array([[1.0, 1.0],[3.0, 5.0]])
# CB = np.array([[0.0, 0.0]])
# CN = np.array([[-2,-3]])
# b = np.array([[10],[15]])

# B = np.array([[-1.0,0.0],[0.0,1.0]])
# N = np.array([[1.0, -1.0],[0.0, 1.0]])
# CB = np.array([[0.0, 0.0]])
# CN = np.array([[1,1]])
# b = np.array([[1],[2]])

# B = np.array([[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]])
# N = np.array([[0.5, 0.25],[0.4, 0.3],[0.2, 0.4]])
# CB = np.array([[0.0, 0.0,0.0]])
# CN = np.array([[-5,-3]])
# b = np.array([[40],[36],[36]])

# B = np.array([[1.0,0.0],[0.0,1.0]])
# N = np.array([[3.0, 4.0,1.0],[1.0, 3.0, 2.0]])
# CB = np.array([[0.0,0.0]])
# CN = np.array([[-3,-6, -2]])
# b = np.array([[2],[1]])

B = np.array([[1.0,0.0],[0.0,1.0],[0.0,0.0]])
N = np.array([[-2.0, 2.0,0.0, -1.0],[5.0, 4.0, -3.0, -1.0],[1.0,1.0,1.0,0.0]])
CB = np.array([[0.0, 0.0]])
CN = np.array([[-1.0, 0.0,0.0,0.0]])
b = np.array([[0],[0],[1]])

# B = np.array([[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]])
# N = np.array([[3.0, 2.0],[2.0, 1.0],[4.0, 6.0]])
# CB = np.array([[0.0, 0.0, 0.0]])
# CN = np.array([[-3,-5]])
# b = np.array([[40],[30],[38]])


simplex_sol = simplex(B, N, CN, CB, b, k)
print("simplex = ", simplex_sol)