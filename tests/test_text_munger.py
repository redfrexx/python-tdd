# Develop a function munge(sentence) to manipulate sentences in the following way:
# - Precondition: Only letters a-z, A-Z and spaces are allowed in the input
# - Words are separated by one or more spaces
# - Words of length 3 or less are output without changes: "I can go to the sun" -> "I can go to the sun"
# - Words longer than 3 keep there first and last letter, whereas the other letters are reversed in order:
#   - "I love TDD" -> "I lvoe TDD"
#   - "Python rules the world" -> "Pohtyn relus the wlrod"

import pytest
