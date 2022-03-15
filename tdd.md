# Test-Driven Development

Development method to help you stay in control even if the code complexity exceeds your mental capacity.

1. Developers write automated tests while they are developing code
2. Most tests come into place before the application code they check
3. Design is taking place continuously and in small steps

### Benefits of TDD

- Tests ensure current functionality does not break
- Continuous Design and Refactoring enhances the life span of software
- Adding tests in retrospective is much harder
- Small steps ensure continuous progress and regular feedback


## Inner Development Cycle: Test-Code-Refactor

1. Add a failing test 
2. Write just enough code to make the test (and all other tests) succeed
3. Clean up code:
   - Remove duplication
   - Choose good names
   - Introduce abstraction (if really necessary)


## The Meta-Process Pattern

1. Think about your next problem
2. Identify criteria/steps for solving the problem
3. Tackle one criterion/step after the other
4. Keep track of open criteria/steps
5. When all criteria are fulfilled, revisit the solution


## Session Inbox: Another Application of the Pattern

1. Collect all features / ideas / tests that are necessary 
   to resolve your next programming task
2. Choose one item from the list and solve it using Test-Code-Refactor
3. Maintain inbox:
   - Add new ideas
   - Remove out-of-scope ideas
   - Add additional tasks that are necessary (e.g. refactorings)
4. If inbox has open items -> Go to 2.
5. If inbox is empty, revisit and review current code and tests


