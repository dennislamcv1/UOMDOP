# ── Challenge 01 ──────────────────────────────────────────────────────────────

# 1.1 Create a function
def lowercase(s):
    return s.lower()


# 1.2 Use map() to apply the function
vegetables = ["ONION", "pOTatO", "zUCCHINi", "carrot", "PePPeR"]

def lowercase_list(lst):
    return list(map(lowercase, lst))

print(lowercase_list(vegetables))
# ['onion', 'potato', 'zucchini', 'carrot', 'pepper']


# 1.3 Use a lambda expression
def lowercase_lambda(lst):
    return list(map(lambda s: s.lower(), lst))

print(lowercase_lambda(vegetables))


# ── Challenge 02 ──────────────────────────────────────────────────────────────

# Original (provided)
def longer_than_n(strings, n):
    long_strings = []
    for string in strings:
        if len(string) > n:
            long_strings.append(string)
    return long_strings


# 2.1 Refactor with a list comprehension
def refactored_longer_than_n(strings, n):
    return [s for s in strings if len(s) > n]


# 2.2 Inner function and filter()
def refactored_longer_than_n(strings, n):
    def is_long(s):
        return len(s) > n
    return list(filter(is_long, strings))


# 2.3 Refactor pass_fail with a list comprehension + if-else expression
def pass_fail(list_of_grades):
    pass_fail_list = []
    for grade in list_of_grades:
        if grade > 65:
            pass_fail_list.append("pass")
        else:
            pass_fail_list.append("fail")
    return pass_fail_list

def refactored_pass_fail(list_of_grades):
    return ["pass" if grade > 65 else "fail" for grade in list_of_grades]

print(refactored_pass_fail([90, 55, 70, 65, 80]))
# ['pass', 'fail', 'pass', 'fail', 'pass']


# ── Challenge 03 ──────────────────────────────────────────────────────────────

candy_type = ["chocolate", "gummy bear", "chocolate", "taffy", "taffy", "gummy bear", "chocolate"]
grams      = [100, 80, 150, 50, 60, 90, 200]

# 3.1 Zip two sequences
candy_sales = list(zip(candy_type, grams))
print(candy_sales)
# [('chocolate', 100), ('gummy bear', 80), ('chocolate', 150), ...]


# 3.2 Filter orders >= 100 g
def find_big_orders(sales):
    return [candy for candy, weight in sales if weight >= 100]

print(find_big_orders(candy_sales))
# ['chocolate', 'chocolate', 'chocolate']


# 3.3 Total weight by candy type
def calculate_total_sales(sales, candy):
    return sum([weight for c, weight in sales if c == candy])

print(calculate_total_sales(candy_sales, "chocolate"))   # 450
print(calculate_total_sales(candy_sales, "gummy bear"))  # 170
print(calculate_total_sales(candy_sales, "taffy"))       # 110


# 3.4 Bonus – most compact version (generator expression, no intermediate list)
def calculate_total_sales(sales, candy):
    return sum(w for c, w in sales if c == candy)
