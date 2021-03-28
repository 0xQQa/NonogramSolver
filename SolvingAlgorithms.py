class SolvingAlgorithms:

    def __init__(self):
        self.changes_made = False 

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

        changes_made = (len(hit_index) + len(miss_index)) > 0
        self.changes_made |= changes_made
        return hit_index, miss_index

    def init_solv_vertically(self, board):
        for index in range(board.dimension):
            res = self.get_req_solv(board.get_vector_x(index), board.dimension)
            hits, misses = self.set_fields(res)
            for hit in hits: board.set_hit(hit, index)
            for miss in misses: board.set_hit(miss, index)

    def init_solv_horizontally(self, board):
        for index in range(board.dimension):
            res = self.get_req_solv(board.get_vector_y(index), board.dimension)
            hits, misses = self.set_fields(res)
            for hit in hits: board.set_hit(index, hit)
            for miss in misses: board.set_hit(index, miss)

    def init_solv(self, board):
        self.init_solv_vertically(board)
        self.init_solv_horizontally(board)
