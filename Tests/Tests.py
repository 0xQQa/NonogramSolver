import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..\\NonogramSolver')))

from NonogramSolver import NonogramSolver
import unittest


class TestSolvingAlgorithm(unittest.TestCase):

    def internal_test_nonogram(self, solving_vector_horizontal: list[list],solving_vector_vertical: list[list]) -> bool:
        nonogram_solver = NonogramSolver(solving_vector_horizontal, solving_vector_vertical)
        solving_result, *_ = nonogram_solver.try_resolve(intertactive_output=True)
        return solving_result
    
    #https://i.stack.imgur.com/EbgM8m.png
    def test_nonogram_no_1(self):
        solving_vector_vertical = \
                            [[2],
                            [3],
                            [4],
                            [2],
                            [2]]

        solving_vector_horizontal = \
                            [[2], 
                            [3], 
                            [3], 
                            [3,1], 
                            [1]]
            
        self.assertTrue(self.internal_test_nonogram(solving_vector_horizontal, solving_vector_vertical))
    
    #https://www.researchgate.net/profile/Kees-Batenburg/publication/228862924/figure/fig3/AS:667635016552458@1536188000573/a-shows-an-example-of-a-Nonogram-Its-solution-is-shown-in-b-The-description-for.png
    def test_nonogram_no_2(self):
        solving_vector_vertical = \
                            [[1],
                            [5],
                            [2],
                            [5], 
                            [2,1], 
                            [2]]
                            
        solving_vector_horizontal = \
                            [[2,1,1], 
                            [1,3], 
                            [1,2], 
                            [3], 
                            [4], 
                            [0]]
            
        self.assertTrue(self.internal_test_nonogram(solving_vector_horizontal, solving_vector_vertical))

    #https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSkERKPOimiOO3aYVtfEBe3Xvwbzcyw0l7ocGucb3b3NOFPVm9cV2kLH0aKE6u7itZGKBI&usqp=CAU
    def test_nonogram_no_3(self):
        solving_vector_vertical = \
                            [[0],
                            [9],
                            [9],
                            [2,2], 
                            [2,2], 
                            [4],
                            [4],
                            [0]]
                            
        solving_vector_horizontal = \
                            [[0], 
                            [4], 
                            [6], 
                            [2,2], 
                            [2,2], 
                            [6],
                            [4],
                            [2],
                            [2],
                            [2],
                            [0]]
        
        self.assertTrue(self.internal_test_nonogram(solving_vector_horizontal, solving_vector_vertical))

    #https://imgur.com/UOEciP1
    def test_nonogram_no_4(self):
        solving_vector_vertical = \
                        [[4,3],
                        [1,6,2],
                        [1,2,2,1,1],
                        [1,2,2,1,2],
                        [3,2,3],
                        [2,1,3],
                        [1,1,1],
                        [2,1,4,1],
                        [1,1,1,1,2],
                        [1,4,2],
                        [1,1,2,1],
                        [2,7,1],
                        [2,1,1,2],
                        [1,2,1],
                        [3,3]]

        solving_vector_horizontal = \
                        [[3,2],
                        [1,1,1,1],
                        [1,2,1,2],
                        [1,2,1,1,3],
                        [1,1,2,1],
                        [2,3,1,2],
                        [9,3],
                        [2,3],
                        [1,2],
                        [1,1,1,1],
                        [1,4,1],
                        [1,2,2,2],
                        [1,1,1,1,1,1,2],
                        [2,1,1,2,1,1],
                        [3,4,3,1]]
        
        self.assertTrue(self.internal_test_nonogram(solving_vector_horizontal, solving_vector_vertical))
    
    #https://puzzlygame.com/static/img/eagle.png
    def test_nonogram_no_5(self):
        solving_vector_vertical = \
                            [[6,6,7],
                            [6,4,5,1],
                            [4,1,3,5,3],
                            [3,2,4,4],
                            [2,1,3],
                            [1,2,4],
                            [2,2,1,6],
                            [2,6,3],
                            [2,12],
                            [2,12],
                            [2,7],
                            [2,2,8],
                            [2,1,4,5],
                            [2,1,3,3],
                            [2,3,1,2],
                            [2,9],
                            [1,1,1,2,2],
                            [2,2,1,2],
                            [2,1,1,1],
                            [2,2,3],
                            [3,3],
                            [2,2,2],
                            [2,1,4],
                            [2,2],
                            [6]]

        solving_vector_horizontal = \
                            [[7],
                            [11],
                            [3,3],
                            [3,3],
                            [4,2],
                            [3,2],
                            [2,1,2],
                            [3,6,1],
                            [2,2,1,2],
                            [1,1,6,1],
                            [2,2,1,2],
                            [3,2,2,2],
                            [3,2,4,1,1],
                            [2,4,1,1,2,2,1],
                            [2,12,2,1],
                            [1,1,15,1],
                            [1,2,2,6,2,1],
                            [5,5,1,1],
                            [4,5,3],
                            [3,6,2],
                            [3,1,5,1],
                            [2,1,2,2,2],
                            [1,5,1,2],
                            [1,5,1,2],
                            [7,1,2]]
        
        self.assertTrue(self.internal_test_nonogram(solving_vector_horizontal, solving_vector_vertical))

    #https://pl.pngtree.com/freebackground/fishing-hook-icon-nonogram-pixel-art_1773145.html
    def test_nonogram_no_6(self):
        solving_vector_vertical = \
                            [[1],
                             [11],
                             [16],
                             [18],
                             [15],
                             [13],
                             [4,7],
                             [6,3,6],
                             [10,3,5],
                             [4,4,3,5],
                             [3,3,2,6],
                             [3,3,5,2,5],
                             [2,1,9,1,5],
                             [11,10,5],
                             [2,13,5],
                             [3,15,5],
                             [3,4,11,6],
                             [3,3,9,5],
                             [10,9,7],
                             [8,10,8],
                             [4,21],
                             [18],
                             [15],
                             [12],
                             [4]]

        solving_vector_horizontal = \
                            [[1],
                             [1],
                             [1],
                             [6],
                             [9],
                             [4,1,4],
                             [3,1,3],
                             [3,1,2],
                             [2,1,1,3],
                             [2,1,1,3],
                             [2,3,3],
                             [2,3],
                             [3,2],
                             [3,3],
                             [5,5],
                             [9],
                             [6],
                             [6],
                             [5],
                             [5],
                             [5],
                             [5],
                             [5],
                             [5],
                             [6],
                             [5],
                             [6],
                             [6],
                             [6],
                             [1,6],
                             [2,6],
                             [2,6],
                             [2,6],
                             [4,5],
                             [4,5],
                             [4,5],
                             [5,5],
                             [6,5],
                             [10,5],
                             [12,5],
                             [11,5],
                             [5,5],
                             [5,6],
                             [6,6],
                             [6,7],
                             [9,8],
                             [19],
                             [17],
                             [14],
                             [11],
                             [4]]
        
        self.assertTrue(self.internal_test_nonogram(solving_vector_horizontal, solving_vector_vertical))

if __name__ == '__main__':
    unittest.main()
