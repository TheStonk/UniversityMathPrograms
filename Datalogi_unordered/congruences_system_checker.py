from math import gcd


# ---------------------------------------------------------
# Solve a system of congruences using the generalized CRT.
# The system is given as a list of pairs (a, m) meaning:
#          x ≡ a  (mod m)
#
# Returns:
#   (has_solution, x0, M)
# where:
#   - has_solution is True/False
#   - x0 is the smallest nonnegative solution (if exists)
#   - M is the modulus of the combined congruence
# ---------------------------------------------------------

def solve_congruence_system(system):
    # Start with a trivial congruence: x ≡ 0 (mod 1)
    x0, M = 0, 1

    for (a, m) in system:
        # Step 1: Check compatibility using gcd
        g = gcd(M, m)
        if (a - x0) % g != 0:
            return (False, None, None)  # No solution exists

        # Step 2: Merge the two congruences:
        # x ≡ x0 (mod M)
        # x ≡ a  (mod m)

        # Solve M * t ≡ a - x0  (mod m)
        # First reduce:
        M_reduced = M // g
        m_reduced = m // g
        rhs = (a - x0) // g

        # Find inverse of M_reduced modulo m_reduced
        # Extended Euclidean Algorithm
        t = pow(M_reduced, -1, m_reduced) * rhs % m_reduced

        # New solution
        x0 = x0 + M * t
        M = M * m_reduced  # lcm(M, m)

        x0 %= M  # keep smallest nonnegative

    return (True, x0, M)


# ---------------------------------------------------------
# Check whether the system has a solution between 0 and LIMIT
# ---------------------------------------------------------
def has_solution_in_range(system, LIMIT=25000):
    has_sol, x0, M = solve_congruence_system(system)
    if not has_sol:
        return False

    # smallest solution ≥ 0 is x0 automatically
    return x0 <= LIMIT


# ---------------------------------------------------------
# Example usage with *multiple* systems
# Each system is a list of (a, m) pairs:
#     x ≡ a (mod m)
# ---------------------------------------------------------

systems = [
    [(1, 20), (2, 44)],
    [(1, 2), (1, 3), (1, 4), (1, 5)],
    [(2, 4), (3, 7), (10, 25), (7, 33)],
]

for i, system in enumerate(systems, 1):
    exists = has_solution_in_range(system)
    print(f"System {i}: {'Solution exists' if exists else 'No solution'}")