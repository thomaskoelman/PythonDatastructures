def vector(len: int):
    return [None] * len

def vector_set(vector, index, value):
    new_vector = vector.copy()
    new_vector[index] = value
    return new_vector

def vector_ref(vector, index):
    return vector[index]