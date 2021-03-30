from NonogramSolver import NonogramSolver

#https://i.stack.imgur.com/EbgM8m.png
def t_1():
    solving_vector_x = [[0,0,0,0,0],
                        [2,3,4,2,2]]

    solving_vector_y = [[0,2], 
                        [0,3], 
                        [0,3], 
                        [3,1], 
                        [0,1]]

    return solving_vector_x, solving_vector_y

#https://www.researchgate.net/profile/Kees-Batenburg/publication/228862924/figure/fig3/AS:667635016552458@1536188000573/a-shows-an-example-of-a-Nonogram-Its-solution-is-shown-in-b-The-description-for.png
def t_2():
    solving_vector_x = [[0,0,0,0,2,0],
                        [1,5,2,5,1,2]]

    solving_vector_y = [[2,1], 
                        [1,3], 
                        [1,2], 
                        [0,3], 
                        [0,4], 
                        [0,1]]

    return solving_vector_x, solving_vector_y

#https://www.puzzle-nonograms.com/art/og/puzzle-nonograms.png
def t_3():
    solving_vector_x = [[1,3,0,0,0,0,0,4,0,0],
                        [4,4,1,1,3,0,5,1,5,0],
                        [1,1,3,1,1,5,1,1,1,3]]

    solving_vector_y = [[0,3,5], 
                        [0,1,5], 
                        [0,1,6], 
                        [0,0,5], 
                        [2,4,1], 
                        [0,2,1],
                        [0,0,3],
                        [0,5,1],
                        [0,0,1],
                        [2,1,1]]

    return solving_vector_x, solving_vector_y

#https://res.cloudinary.com/practicaldev/image/fetch/s--dF6qLl8d--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://lihautan.com/static/277ac809de46a701e6498a7c483c030b/623ee/solution.png
def t_4():
    solving_vector_x = [[0,0,0, 0, 0,0,0,0,0,0,0,0, 0,0,0],
                        [0,1,0, 0, 0,0,1,0,1,0,0,0, 0,0,0],
                        [0,2,0, 0, 4,7,4,1,4,0,4,0, 8,1,0],
                        [4,3,13,0, 2,1,1,3,1,7,2,0, 3,6,4],
                        [4,2,1, 13,2,1,2,3,2,1,1,13,2,2,4]]

    solving_vector_y = [[0,0,0,3,3], 
                        [1,1,5,1,1], 
                        [0,1,4,4,1], 
                        [0,0,0,6,6], 
                        [0,0,0,0,13], 
                        [0,0,0,0,12],
                        [0,0,3,5,3],
                        [0,0,0,6,6],
                        [0,0,5,2,2],
                        [1,2,3,2,1],
                        [1,2,1,2,1],
                        [1,2,3,2,1],
                        [3,2,2,1,1],
                        [0,0,1,2,3],
                        [0,0,0,4,3]]

    return solving_vector_x, solving_vector_y

def t_5():
    solving_vector_x = [[0,3,2,0,0],
                        [0,2,3,0,0],
                        [2,3,3,5,3]]

    solving_vector_y = [[0,0,3], 
                        [0,0,5], 
                        [0,2,2], 
                        [0,0,2],
                        [0,0,2],
                        [0,0,2],
                        [0,0,0],
                        [0,0,2],
                        [0,0,2],
                        [0,0,2]]

    return solving_vector_x, solving_vector_y

def t_6():
    solving_vector_x = [[0,4,7,6,5,6,0,0,0,0,0,0,0,0,0],
                        [2,2,3,3,2,4,9,6,5,5,6,6,6,4,2]]

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
                        [0,5],
                        [0,4],
                        [0,3],
                        [0,2],
                        [0,2],
                        [0,3],
                        [0,2],
                        [0,6],
                        [0,5],
                        [0,2],]

    return solving_vector_x, solving_vector_y

if __name__ == "__main__": 
    solving_vector_x, solving_vector_y = t_6()
    ns = NonogramSolver(solving_vector_x, solving_vector_y) 
    ns.solve(show_step=True)
    print()
    ns.show_clean()