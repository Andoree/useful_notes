from sys import stderr


def get_solution_value(w_v_wv_items):
    """
    Calculates total value of items in the given solution (backpack)
    """
    total_value = 0
    for item in w_v_wv_items:
        total_value += item[1]
    return total_value


def get_solution_weight(w_v_wv_items):
    """
    Calculates total weight of items in the given solution (backpack)
    """
    total_weight = 0
    for item in w_v_wv_items:
        total_weight += item[0]
    return total_weight


def find_solution(wei_val_wvrat_array, weight_constraint):
    """
    Solution function. For small item sets calculates solution
    based on value/weight ratio. For larger item sets find the
    best solution among the following solutions: (i) best solution
    for the left item set partition, (ii) best solution for the right
    item set partition, (iii) value/weight ratio-based solution of
    concatenation of (i) and (ii).
    """
    arr_len = len(wei_val_wvrat_array)

    if arr_len < 4:
        # Value/weight ratio-based solution of small item set
        result_solution = find_solution_by_vw_ratio(wei_val_wvrat_array, weight_constraint)
    else:
        pivot = len(wei_val_wvrat_array) // 2
        left_part = wei_val_wvrat_array[:pivot]
        right_part = wei_val_wvrat_array[pivot:]
        # Left partition solution
        left_solution = find_solution(left_part, weight_constraint)
        # Right partition solution
        right_solution = find_solution(right_part, weight_constraint)
        # Value/weight ratio-based solution of solutions' concatenation
        concatenation_solution = find_solution_by_vw_ratio(left_solution + right_solution, weight_constraint)
        # Finding the best solution among 3 obtained candidates
        result_solution = left_solution if get_solution_value(left_solution) > get_solution_value(
            right_solution) else right_solution
        result_solution = result_solution if get_solution_value(result_solution) > get_solution_value(
            concatenation_solution) else concatenation_solution

    return result_solution


def find_solution_by_vw_ratio(w_v_wvr_array, weight_constraint):
    """
    Finds a solution as a combination of items with the highest
    value/weight ratio.
    """
    solution = []
    solution_weight = 0
    w_v_wvr_array.sort(key=lambda x: x[2])
    item_id = len(w_v_wvr_array) - 1
    while item_id >= 0:
        current_item = w_v_wvr_array[item_id]
        item_weight = current_item[0]
        if solution_weight + item_weight <= weight_constraint:
            solution.append(current_item)
            solution_weight += item_weight
        item_id -= 1

    return solution


def main():
    weight_restriction = int(input("Input backpack size:\n"))
    weights_line = input("Input items' weights:\n")
    values_line = input("Input items' values:\n")

    weights_array = [int(x) for x in weights_line.split()]
    values_array = [int(x) for x in values_line.split()]

    if len(weights_array) != len(values_array):
        stderr.write("Weights and values lengths mismatch\n")

    value_weight_ratios = [values_array[i] / weights_array[i] for i in range(len(weights_array))]
    item_array = [(weights_array[i], values_array[i], value_weight_ratios[i]) for i in range(len(weights_array))]
    solution = find_solution(item_array, weight_restriction)
    solution = [(t[0], t[1]) for t in solution]
    sol_weight = get_solution_weight(solution)
    sol_value = get_solution_value(solution)
    print(f"Solution items:{solution}")
    print(f"Solution weight: {sol_weight}, solution value: {sol_value}")


if __name__ == '__main__':
    main()
