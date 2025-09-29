#*1 Vector Operations(King - Man + Woman Analogy (From Scratch))

v_king   = [0.8, 0.65, 0.0]
v_man    = [0.6, 0.4,  0.0]
v_woman  = [0.7, 0.3,  0.2]
v_queen  = [0.9, 0.55, 0.2]

# Check that all vectors have the same dimension
if not (len(v_king) == len(v_man) == len(v_woman) == len(v_queen)):
    raise ValueError("All vectors must have the same dimension!")

def add_vects(v1,v2):
    result=[]
    for i in range(len(v1)):
        result.append(v1[i]+v2[i])
    return result

def sub_vects(v1,v2):
    result=[]
    for i in range(len(v1)):
        result.append(v1[i]-v2[i])
    return result

v_result=add_vects(sub_vects(v_king,v_man),v_woman)

print("Analogy result (from scratch):",v_result)

#-------------------------------------------------

#*2 Cosine Similarity

#formula: uv=u1*v1+u2*v2.....
def dot_product(u,v):
    product=0
    for i in range(len(u)):
        product+= u[i]*v[i]
    return product

#formula: sqrt(u1**2+u2**2.......)
def norm(u):
    total=0
    for i in u:
        total+=i**2
    return total**0.5

def cosine_similarity(u, v):
    return dot_product(u,v)/(norm(u)*norm(v))

similarity=cosine_similarity(v_result,v_queen)

print("Cosine similarity (from scratch):",similarity)

#-------------------------------------------------

#*NumPy Verification
# --- Analogy computation with NumPy ---
import numpy as np
np_king   = np.array(v_king)
np_man    = np.array(v_man)
np_woman  = np.array(v_woman)
np_queen  = np.array(v_queen)

# Check dimensions
if not (np_king.shape == np_man.shape == np_woman.shape == np_queen.shape):
    raise ValueError("All NumPy vectors must have the same shape!")

np_result=np_king-np_man+np_woman
print("Analogy result (NumPy):", np_result)

# --- Cosine similarity with NumPy ---
#np.dot()-for dot product;np.linalg.norm()-for norm
similarity_numpy = np.dot(np_result,np_queen)/(np.linalg.norm(np_result)*np.linalg.norm(np_queen))

print("Cosine similarity (NumPy):", similarity_numpy)
