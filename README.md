# homework_helper (not finished)

## Some notes

After trying hard to replace hand writings in Physics homework in this quarter, I figured out it is not an easy job to do. Few significant difficulties are,

1. It's not always easy to use programming to do some approximation in Physics calculations. Sometime physicists would use order of magnitude estimation to guess some physical relation, and I have no clue how to do it using plain Python.
2. Sometime the integrations are tricky. In some forms of integrations we will treat them as a result of a special function (e.g., delta function). It's not easy to automatically generate this kind of intuitions.

And, some trade-off using programming to do Physics homework,

1. You will not have a chance to practice your calculation skills using your bare hands. It sounds crazy, but you are not allowed to bring Python into midterms or final exams or qualification exam.
2. You usually spent more time on writing codes to solve hand-writing problems. For a 3 hr homework, I usually spent 5 hr if I used coding. (I believe if we could figure out a standard to do hand-writing problems by codes, this problem would be solved.)

The current best strategy for me to do homework in python is,

1. Define your problem into `Sympy` symbols, construct your expression of the question first.
    1. **Derivation problem**:
        1. `diff` and `integral` are useful for differential equations.
        2. `solve` is useful to solve plain equations.
        3. `simlipy`: get the expression shorter, really useful for changing the outlook of your mathematics equations. 
        4. `sympy.latex`: sometime you need to simplify your expression by hand. In this case, generate the latex expression of your sympy expression and using latex editor to do the math.
        5. `sympy.parsing.latex.parse_latex`: when you finish your hand derivations, convert the latex code back to sympy expression using this parsing function.
    2. **Numerical problem**: it is not necessary to use sympy in numerical homework, but it is easy to keep track your math derivations if you are using sympy.
        1. `subs` : especially useful for substitute the variables in the expression to numbers.
        2. `evalf` : sympy would not convert your results into numbers unless you force the expression to `evalf`.
        3. `astropy.units` : for the problems involving unit conversions (usually happens in astronomy), `astropy.units` is a good tool to help you keep track your units and help you to do unit conversion automatically.