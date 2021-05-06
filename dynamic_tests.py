# dynamic tests using cProfile

import cProfile
import driver

# Test 1: translate function
print("1. translate cProf test")
cProfile.run('driver.translate("red")')

# Test 2: reverse_translate function
print("+" * 120)
print("2. reverse_translate cProf test")
cProfile.run('driver.reverse_translate(15)')

# Test 3: win_checker function
print("+" * 120)
print("3. win_checker cProf test")
cProfile.run('driver.win_checker(1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1200, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])')

# Test 4: colour_print function
print("+" * 120)
print("4. colour_print cProf test")
cProfile.run('driver.colour_print(2)')

# Test 5: print_help function
print("+" * 120)
print("5. print_help cProf test")
cProfile.run('driver.print_help()')
