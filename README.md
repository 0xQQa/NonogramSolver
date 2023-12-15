# NonogramSolver

NonogramSolver is an application that allows you to autmoatically solve nonograms. It needs to get a vector of horizontal and vertical solutions after which it attempts to solve.

## Usage

```python
#example nonogram from: https://puzzlygame.com/static/img/eagle.png

if __name__ == "__main__":
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
        
        nonogram_solver = NonogramSolver(solving_vector_horizontal, solving_vector_vertical)
        maybe_resolved = nonogram_solver.try_resolve(interactive_output=False)
        print(NonogramSolver.get_output_str(*maybe_resolved))
        #or use interactive_output to watch the nonogram resolving live
        nonogram_solver = NonogramSolver(solving_vector_horizontal, solving_vector_vertical)
        nonogram_solver.try_resolve(interactive_output=True)

        #then you should saw result as:
        #--------------------------------------------------
        #Nonogram was resolved!
        #Nonogram size 25x25
        #Took 17 steps and 0.5693450999997367 s!
        #--------------------------------------------------
        #            ■ ■ ■ ■ ■ ■ ■
        #        ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
        #    ■ ■ ■                 ■ ■ ■
        #■ ■ ■                       ■ ■ ■
        #■ ■ ■ ■                           ■ ■
        #■ ■ ■                               ■ ■
        #■ ■                   ■               ■ ■
        #■ ■ ■                 ■ ■ ■ ■ ■ ■       ■
        #■ ■                         ■ ■   ■   ■ ■
        #■     ■                     ■ ■ ■ ■ ■ ■   ■
        #    ■ ■       ■ ■             ■           ■ ■
        #■ ■ ■         ■ ■             ■ ■           ■ ■
        #■ ■ ■         ■ ■           ■ ■ ■ ■       ■   ■
        #■ ■         ■ ■ ■ ■     ■     ■     ■ ■   ■ ■   ■
        #■ ■         ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■   ■ ■       ■
        #■     ■       ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■     ■
        #■   ■ ■   ■ ■   ■ ■ ■ ■ ■ ■             ■ ■     ■
        #■ ■ ■ ■ ■   ■ ■ ■ ■ ■                     ■   ■
        #■ ■ ■ ■       ■ ■ ■ ■ ■                     ■ ■ ■
        #■ ■ ■       ■ ■ ■ ■ ■ ■                     ■ ■
        #■ ■ ■       ■   ■ ■ ■ ■ ■                   ■
        #■ ■   ■   ■ ■   ■ ■   ■ ■
        #■   ■ ■ ■ ■ ■     ■     ■ ■
        #■   ■ ■ ■ ■ ■     ■     ■ ■
        #■ ■ ■ ■ ■ ■ ■     ■     ■ ■

```

## Contributing

Pull requests are welcome. Fell free to report a bug.

## License

[MIT](https://choosealicense.com/licenses/mit/)