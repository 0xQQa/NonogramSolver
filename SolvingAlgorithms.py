class SolvingAlgorithms:

    def __init__(self):
        self.steps = 0

    def req_solv(self, list_to_swp, swp_indx_1, swp_indx_2, max_req, cur_req, results): 
        tmp_list = list_to_swp.copy()
        tmp_list[swp_indx_1], tmp_list[swp_indx_2] = tmp_list[swp_indx_2], tmp_list[swp_indx_1]
        results.append(tmp_list)

        cur_req += 1
        if cur_req == max_req: return
    
        new_swp_indx_1 = swp_indx_1 - 2
        new_vector_range = swp_indx_2 - swp_indx_1
        self.req_step(new_swp_indx_1, new_vector_range, tmp_list, max_req, cur_req, results)

    def req_step(self, new_swp_indx_1, new_vector_range, tmp_list, max_req, cur_req, results):
        for i in range(new_vector_range): 
            new_swp_indx_2 = new_swp_indx_1 + i + 1
            self.req_solv(tmp_list, new_swp_indx_1, new_swp_indx_2, max_req, cur_req, results)

    def init_req_solv(self, first_list, unit_amount, dimension):
        results = []

        tmp_list = first_list.copy()
        results.append(tmp_list)
       
        new_swp_indx_1 = 2 * (unit_amount - 1)
        new_vector_range = len(first_list) - new_swp_indx_1 - 1

        self.req_step(new_swp_indx_1, new_vector_range, tmp_list, unit_amount, 0, results)
        return results

    def get_list_from_vector(self, solution_vec, dimension): 
        first_list = []
     
        for block_size in solution_vec[:-1]: first_list += [block_size, 0]
        first_list.append(solution_vec[-1])

        first_list_dimension = len(first_list) + sum(solution_vec) - len(solution_vec)
        first_list += [0 for _ in range(dimension - first_list_dimension)]

        return first_list

    def get_req_solv_wrap(self, solution_vec, dimension):
        if sum(solution_vec) == 0: return [[0 for i in range(dimension)]]
        return self.get_req_solv(solution_vec, dimension)

    def get_req_solv(self, solution_vec, dimension):
        tmp_solution_vec = solution_vec.copy()

        while tmp_solution_vec[0] == 0: tmp_solution_vec.pop(0) 
        unit_amount = len(tmp_solution_vec)
        first_list = self.get_list_from_vector(tmp_solution_vec, dimension)
        results = self.init_req_solv(first_list, unit_amount, dimension)
        results = self.expand_req_solv_vec(results)
        return results

    def expand_req_solv_vec(self, results):
        new_results = []

        for i in range(len(results)):
            new_results.append([])
            for block_size in results[i]:
                if block_size == 0: new_results[i].append(0)
                else: new_results[i] += [1 for _ in range(block_size)]
        
        return new_results

    def set_fields(self, lists_list):
        hit_index, miss_index = [], []
        list_size, lists_amount = len(lists_list[0]),len(lists_list)
     
        for index in range(list_size):
            is_ok, list_index = True, 0

            for list_index in range(lists_amount - 1):
                if lists_list[list_index][index] != lists_list[list_index + 1][index]: 
                    is_ok = False
                    break
            
            if is_ok:
                if (lists_list[list_index][index]): hit_index.append(index)
                else: miss_index.append(index)

        return hit_index, miss_index

    def show_step(self, board, orientation):
        print(f"{orientation} step no.{self.steps}")
        board.show()

    def init_solv_vertically(self, board):
        self.show_step(board, "Vertical")
        for index in range(board.dimension_x):
            res = self.get_req_solv_wrap(board.get_vector_x(index), board.dimension_y)
            hits, misses = self.set_fields(res)
            
            self.update_hit_miss_vertically(hits, misses, board, index)

    def init_solv_horizontally(self, board):
        self.show_step(board, "Horizontal")
        for index in range(board.dimension_y):
            res = self.get_req_solv_wrap(board.get_vector_y(index), board.dimension_x)
            hits, misses = self.set_fields(res)
            
            self.update_hit_miss_horizontally(hits, misses, board, index)

    def init_solv(self, board):
        self.steps += 1
        self.init_solv_horizontally(board)
        self.init_solv_vertically(board)

    def try_fit(self, results, compared_to):
        solutions, max_matches_probability = [], 0

        for tmp_list in results:
            hits_probability = sum(list(map(lambda x,y: x == y == 1, tmp_list, compared_to))) 
            misses_probability = sum(list(map(lambda x,y: x == 0 and y == -1, tmp_list, compared_to))) 
            matches_probability = hits_probability + misses_probability

            if matches_probability == max_matches_probability:
                solutions.append(tmp_list)
                continue

            if matches_probability > max_matches_probability:
                solutions = [tmp_list]
                max_matches_probability = matches_probability

        return self.set_fields(solutions)

    def next_solv_horizontally(self, board):
        self.show_step(board, "Horizontal")
        for index in range(board.dimension_y): 
            to_comp, solv_vec = board.get_row(index), board.get_vector_y(index)
            res = self.get_req_solv(solv_vec, board.dimension_x)
            hits, misses = self.try_fit(res, to_comp)
            self.update_hit_miss_horizontally(hits, misses, board, index)
            
    def next_solv_vertically(self, board):
        self.show_step(board, "Vertical")
        for index in range(board.dimension_x): 
            to_comp, solv_vec = board.get_column(index), board.get_vector_x(index)
            res = self.get_req_solv(solv_vec, board.dimension_y)         
            hits, misses = self.try_fit(res, to_comp)
            self.update_hit_miss_vertically(hits, misses, board, index)

    def next_solv(self, board):
        self.steps += 1
        self.next_solv_horizontally(board)
        self.next_solv_vertically(board)
                
    def update_hit_miss_vertically(self, hits, misses, board, index):
        for hit in hits: board.set_hit(hit, index)
        for miss in misses: board.set_miss(miss, index)

    def update_hit_miss_horizontally(self, hits, misses, board, index):
        for hit in hits: board.set_hit(index, hit)
        for miss in misses: board.set_miss(index, miss)
