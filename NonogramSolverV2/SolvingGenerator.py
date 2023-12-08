from itertools import chain, repeat


class SolvingGenerator:

    def SolvingCache(decorated_func: callable) -> callable:
        cache = dict()

        def wrapper(*args: list, **kwargs: dict):
            key = id(args[1])
            if key in cache.keys():
                return cache[key]

            result = decorated_func(*args, **kwargs)
            cache[key] = result
            return result

        return wrapper

    def generate_all_posibilities(self, minimal_solution: list, dimension: int) -> list[list]:
        shuffle_count = dimension - (sum(minimal_solution) + minimal_solution.count(0))
        leading_zeros = repeat(0, shuffle_count)
        minimal_solution_vector = list(leading_zeros) + minimal_solution
        all_possible_list_from_minimal_solution = [minimal_solution_vector.copy()]

        for _ in range(shuffle_count):
            tmp_minimal_solution_vector = minimal_solution_vector[1:] + [0]
            minimal_solution_vector = tmp_minimal_solution_vector
            all_possible_list_from_minimal_solution.append(tmp_minimal_solution_vector)

        return all_possible_list_from_minimal_solution
    
    def req_generate_all_minimal_solutions(self, all_possible_minimal_solution: list, curr_idx: int, minimal_solution: list, dimension: int) -> list[list]:
        if sum(minimal_solution) + minimal_solution.count(0) > dimension:
            return

        all_possible_minimal_solution.append(minimal_solution)
        for idx in range(curr_idx, len(minimal_solution)):
            if minimal_solution[idx] != 0:
                continue

            tmp_minimal_solution = minimal_solution.copy()
            tmp_minimal_solution.insert(idx, 0)
            self.req_generate_all_minimal_solutions(all_possible_minimal_solution, idx + 1, tmp_minimal_solution, dimension)

    def generate_all_minimal_posibilities(self, solution_vec :list, dimension: int) -> list[list]:
        leading_zeros = repeat(0, len(solution_vec))
        minimal_solution_vector = list(chain.from_iterable(zip(solution_vec, leading_zeros)))[:-1]

        all_possible_minimal_solution = []
        self.req_generate_all_minimal_solutions(all_possible_minimal_solution, 0, minimal_solution_vector, dimension)
        return all_possible_minimal_solution

    def transform_vector_to_point_arr(self, solution_vec: list) -> list:
        unit_indexes = [(idx, unit_val) for idx, unit_val in enumerate(solution_vec) if unit_val > 0]
        for idx, unit_val in reversed(unit_indexes):
            solution_vec = solution_vec[:idx] + list(repeat(1, unit_val)) + solution_vec[idx + 1:]

        return solution_vec

    @SolvingCache
    def generate_all_vectors(self, solution_vec: list, dimension: int) -> list[list]:
        tmp_all_possible_minimal_solution = self.generate_all_minimal_posibilities(solution_vec, dimension)
        tmp_all_possible_minimal_solution = map(lambda minimal_vector: self.generate_all_posibilities(minimal_vector, dimension), tmp_all_possible_minimal_solution)
        tmp_all_possible_minimal_solution = chain.from_iterable(tmp_all_possible_minimal_solution)
        tmp_all_possible_minimal_solution = map(self.transform_vector_to_point_arr, tmp_all_possible_minimal_solution)
        return list(tmp_all_possible_minimal_solution)
    
    def get_out_vectors_as_point_arr(self, checking_lists: list[list], dimension: int) -> list:
        count_vector = lambda score_idx : sum(map(lambda vectors_as_point_arr: vectors_as_point_arr[score_idx], checking_lists))
        set_valid_confidence = lambda score: 1 if score == max_confidence_score else -1 if score == 0 else 0

        max_confidence_score = len(checking_lists)    
        confidence_list = map(lambda score_idx: count_vector(score_idx), range(dimension))
        confidence_list = map(set_valid_confidence, confidence_list)
        return list(confidence_list)

    def get_similar_candidates_to_vector(self, all_vectors_as_point_arr: list[list], comparison_vec: list) -> list[list]:
        set_similarity_confidence = lambda valid_item, comparsion_item: comparsion_item == valid_item == 1 or (comparsion_item == -1 and valid_item == 0)
        count_similarity_score = lambda valid_vector: sum(map(lambda x,y: set_similarity_confidence(x, y), valid_vector, comparison_vec))
        
        counted_similarity = list(map(count_similarity_score, all_vectors_as_point_arr))
        max_similarity = max(counted_similarity)
        candidates_list = [unit_val for idx, unit_val in enumerate(all_vectors_as_point_arr) if counted_similarity[idx] == max_similarity]
        return candidates_list
    
    def get_valid_vector(self, solution_vec: list, dimension: int, comparison_vec: list = None) -> list:
        tmp_all_vectors_as_point_arr = self.generate_all_vectors(solution_vec, dimension)
        candidates_list = self.get_similar_candidates_to_vector(tmp_all_vectors_as_point_arr, comparison_vec) if comparison_vec else tmp_all_vectors_as_point_arr
        confidence_vector = self.get_out_vectors_as_point_arr(candidates_list, dimension)
        return confidence_vector
