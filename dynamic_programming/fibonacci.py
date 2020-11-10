import timeit

def naive_fibonacci(n):
    if n <= 2:
        return 1
    return naive_fibonacci(n-1) + naive_fibonacci(n-2)

def fibonacci(memo, n):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    else:
        f = fibonacci(memo, n-1) + fibonacci(memo, n-2)
        memo[n] = f
        return f

n = 30
start_naive = timeit.default_timer()
n_ret = naive_fibonacci(n)
stop_naive = timeit.default_timer()
ex_time_naive = stop_naive - start_naive

start_dp = timeit.default_timer()
dp_ret = fibonacci({}, n)
stop_dp = timeit.default_timer()
ex_time_dp = stop_dp - start_dp

log = (
    f"number: {n}\n"
    f"result naive: {n_ret}\n"
    f"execution time naive: {ex_time_naive}\n\n"
    f"result dynamic programming: {n_ret}\n"
    f"execution time dynamic programming: {ex_time_dp}\n\n"
    f"ex_dp/ex_naive: {ex_time_dp/ex_time_naive*100}%\n\n"
)

with open('fibonacci.log', 'w') as file:
    file.write(log)