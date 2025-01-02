"""
Purpose: Debugging with ipdb

TASK - To display all even numbers between 0 & 100

To install ipdb,
    pip install -U ipdb --user

NOTE: TO make ipdb as the default, when using breakpoint(),
    export PYTHONBREAKPOINT='ipdb.set_trace'

"""


numbers = range(0, 100)

# import ipdb; ipdb.set_trace()
breakpoint()


for each_num in numbers:
    if each_num % 2 == 0:  # each_num % 2
        print(each_num, end=", ")


# Assignment: How to clear one specific breakpoint, in ipdb

#In ipdb, to clear a specific breakpoint, you can first list all breakpoints using the break command. Each breakpoint will be numbered, allowing you to identify which one you want to remove. To clear a specific breakpoint, simply use the clear command followed by the breakpoint number (e.g., clear 2 to remove the second breakpoint). After clearing, you can use the break command again to confirm that the breakpoint has been removed. This method helps you manage breakpoints efficiently during debugging sessions.