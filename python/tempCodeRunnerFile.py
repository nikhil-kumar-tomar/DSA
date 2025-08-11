
    # print(find_delta(len(new_arr) // 2))
    fin_counts = 0
    delta = find_delta(len(new_arr) // 2)
    for mid in range(delta, c - delta + 1):
        if (mid - delta - (mid + delta)) % len(new_arr) 