from NonogramSolver import NonogramSolver

#https://i.stack.imgur.com/EbgM8m.png
def t_1():
    solving_vector_x = [[2],
                        [3],
                        [4],
                        [2],
                        [2]]

    solving_vector_y = [[2], 
                        [3], 
                        [3], 
                        [3,1], 
                        [1]]

    return solving_vector_x, solving_vector_y

#https://www.researchgate.net/profile/Kees-Batenburg/publication/228862924/figure/fig3/AS:667635016552458@1536188000573/a-shows-an-example-of-a-Nonogram-Its-solution-is-shown-in-b-The-description-for.png
def t_2():
    solving_vector_x = [[1],
                        [5],
                        [2],
                        [5], 
                        [2,1], 
                        [2]]
                        
    solving_vector_y = [[2,1,1], 
                        [1,3], 
                        [1,2], 
                        [3], 
                        [4], 
                        [0]]

    return solving_vector_x, solving_vector_y

#https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSkERKPOimiOO3aYVtfEBe3Xvwbzcyw0l7ocGucb3b3NOFPVm9cV2kLH0aKE6u7itZGKBI&usqp=CAU
def t_3():
    solving_vector_x = [[0],
                        [9],
                        [9],
                        [2,2], 
                        [2,2], 
                        [4],
                        [4],
                        [0]]
                        
    solving_vector_y = [[0], 
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

    return solving_vector_x, solving_vector_y

#niedeteremistyczny fixme
def t_4():
    solving_vector_x = [[2],
                        [4,2],
                        [7,3],
                        [6,3], 
                        [5,2], 
                        [6,4],
                        [9],
                        [6],
                        [5],
                        [5],
                        [6],
                        [6],
                        [6],
                        [4],
                        [2]]
                        
    solving_vector_y = [[3,3], 
                        [3,3], 
                        [2,2], 
                        [3,3], 
                        [2,2], 
                        [2,3],
                        [3,2],
                        [2,2],
                        [3,3],
                        [2,2],
                        [2,3],
                        [2,2],
                        [5],
                        [4],
                        [3],
                        [2],
                        [2],
                        [3],
                        [2],
                        [6],
                        [5],
                        [2]]

    return solving_vector_x, solving_vector_y

#https://imgur.com/UOEciP1
def t_5():
    solving_vector_x = [[4,3],
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

    solving_vector_y = [[3,2],
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

    return solving_vector_x, solving_vector_y

#https://puzzlygame.com/static/img/eagle.png
def t_6():
    solving_vector_x = [[6,6,7],
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

    solving_vector_y = [[7],
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

    return solving_vector_x, solving_vector_y


if __name__ == "__main__": 
    solving_vector_x, solving_vector_y = t_1()
    ns = NonogramSolver(solving_vector_x, solving_vector_y) 
    ns.solve(show_step=True)
    print()
    ns.show_clean()