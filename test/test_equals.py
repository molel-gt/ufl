#!/usr/bin/env python

"""
Test of expression comparison.
"""

# These are thin wrappers on top of unittest.TestCase and unittest.main
from ufltestcase import UflTestCase, main

# This imports everything external code will see from ufl
from ufl import *

class TestExprEquals(UflTestCase):

    def test_comparison_of_coefficients(self):
        V = FiniteElement("CG", triangle, 1)
        U = FiniteElement("CG", triangle, 2)
        Ub = FiniteElement("CG", triangle, 2)
        v1 = Coefficient(V, count=1)
        v1b = Coefficient(V, count=1)
        v2 = Coefficient(V, count=2)
        u1 = Coefficient(U, count=1)
        u2 = Coefficient(U, count=2)
        u2b = Coefficient(Ub, count=2)

        # Itentical objects
        self.assertTrue(v1 == v1)
        self.assertTrue(u2 == u2)

        # Equal but distinct objects
        self.assertTrue(v1 == v1b)
        self.assertTrue(u2 == u2b)

        # Different objects
        self.assertFalse(v1 == v2)
        self.assertFalse(u1 == u2)
        self.assertFalse(v1 == u1)
        self.assertFalse(v2 == u2)

    def test_comparison_of_products(self):
        V = FiniteElement("CG", triangle, 1)
        v = Coefficient(V)
        u = Coefficient(V)
        a = (v * 2) * u
        b = (2 * v) * u
        c = 2 * (v * u)
        self.assertTrue(a == b)
        self.assertFalse(a == c)
        self.assertFalse(b == c)

    def test_comparison_of_sums(self):
        V = FiniteElement("CG", triangle, 1)
        v = Coefficient(V)
        u = Coefficient(V)
        a = (v + 2) + u
        b = (2 + v) + u
        c = 2 + (v + u)
        self.assertTrue(a == b)
        self.assertFalse(a == c)
        self.assertFalse(b == c)

    def test_comparison_of_deeply_nested_expression(self):
        V = FiniteElement("CG", triangle, 1)
        v = Coefficient(V, count=1)
        u = Coefficient(V, count=1)
        w = Coefficient(V, count=2)
        def build_expr(a):
            for i in range(100):
                if i % 3 == 0:
                    a = a + i
                elif i % 3 == 1:
                    a = a * i
                elif i % 3 == 2:
                    a = a**i
            return a
        a = build_expr(u)
        b = build_expr(v)
        c = build_expr(w)
        self.assertTrue(a == b)
        self.assertFalse(a == c)
        self.assertFalse(b == c)

# Don't touch these lines, they allow you to run this file directly
if __name__ == "__main__":
    main()

