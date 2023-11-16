import pytest
from sparse_recommender import SparseMatrix

def test_set_and_get():
    matrix = SparseMatrix()
    matrix.set(0, 1, 3)
    matrix.set(1, 2, 5)
    assert matrix.get(0, 1) == 3
    assert matrix.get(1, 2) == 5
    assert matrix.get(2, 3) == 0

def test_recommend():
    matrix = SparseMatrix()
    matrix.set(0, 0, 4)
    matrix.set(1, 1, 3)
    matrix.set(2, 2, 2)
    vector = [1, 2, 3]
    recommendations = matrix.recommend(vector)
    assert recommendations == {0: 4, 1: 6, 2: 6}

def test_add_movie():
    matrix1 = SparseMatrix()
    matrix1.set(0, 0, 4)
    matrix2 = SparseMatrix()
    matrix2.set(0, 1, 2)
    matrix1.add_movie(matrix2)
    assert matrix1.get(0, 0) == 4
    assert matrix1.get(0, 1) == 2

def test_to_dense():
    matrix = SparseMatrix()
    matrix.set(0, 1, 3)
    matrix.set(1, 2, 5)
    dense_matrix = matrix.to_dense()
    assert dense_matrix == [[0, 3, 0], [0, 0, 5]]
    
def test_errorhandling_for_set():
    with pytest.raises(ValueError):
        matrix = SparseMatrix()
        matrix.set(0, 1,0)

def test_errorhandling_for_recommend():
    with pytest.raises(ValueError):
        matrix = SparseMatrix()
        matrix.set(0, 0, 4)
        matrix.set(1, 1, 3)
        matrix.set(2, 2, 2)
        vector = [1, 2, 3, 4]  
        recommendations = matrix.recommend(vector)

if __name__ == '__main__':
    pytest.main()
    