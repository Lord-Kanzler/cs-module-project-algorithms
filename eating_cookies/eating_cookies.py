"""
Input: an integer
Returns: an integer
"""


def eating_cookies(n, cache=None):
    # Your code here
    if cache == None:
        cache = [0] * (n + 1)
    if n <= 1:
        cache[n] = 1
    elif n == 2:
        cache[n] = 2
    elif cache[n] == 0:
        cache[n] = (
            eating_cookies(n - 1, cache)
            + eating_cookies(n - 2, cache)
            + eating_cookies(n - 3, cache)
        )

    return cache[n]  # runs small in 0.000s and large in 0.001s and both in 0.001s


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies"
    )
