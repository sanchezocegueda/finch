from dataclasses import dataclass
from typing import List, Tuple, Set, Optional
import json


# Base class for all formulas
@dataclass
class Formula:
    """Base class for well-formed formulas in propositional logic."""
    def __str__(self) -> str:
        """Each subclass will implement its own string representation."""
        raise NotImplementedError

# Sentence symbols
@dataclass
class SentenceSymbol(Formula):
    """Represents sentence symbols like A, B, C"""
    name: str

    def __str__(self):
        return self.name
    
# Negation
@dataclass
class Not(Formula):
    """Represents the negation of a formula (¬φ)"""
    phi: Formula

    def __str__(self):
        return f"(¬{self.phi})"

# Binary connectives
@dataclass
class BinaryConnective(Formula):
    """Base class for binary connectives."""
    phi: Formula
    psi: Formula


# Conjunction
@dataclass
class And(BinaryConnective):
    """Represents the conjunction of two formulas (φ ∧ ψ)"""

    def __str__(self):
        return f"({str(self.phi)} ∧ {str(self.psi)})"

# Disjunction
@dataclass
class Or(BinaryConnective):
    """Represents the disjunction of two formulas (φ ∨ ψ)"""

    def __str__(self):
        return f"({str(self.phi)} ∨ {str(self.psi)})"
    
# Implication
@dataclass
class Implies(BinaryConnective):
    """Represents implication between two formulas (φ → ψ)"""

    def __str__(self):
        return f"({str(self.phi)} → {str(self.psi)})"
    
# Biconditional
@dataclass
class Iff(BinaryConnective):
    """Represents biconditional between two formulas (φ ↔ ψ)"""

    def __str__(self):
        return f"({str(self.phi)} ↔ {str(self.psi)})"
    

@dataclass
class Proof():
    premises: List[Formula]
    goal: Formula
    deduction: List[Tuple[Formula, str]]

## Utility functions

def is_equal(a: Formula, b: Formula):

    if not type(a) == type(b):
        return False
    
    if isinstance(a, SentenceSymbol):
        return a.name == b.name
    
    return is_equal(a.phi, b.phi) and is_equal(a.psi, b.psi)

def pretty_print(P: Proof):
    print()
    print(f"Goal: {P.goal}")
    print("   ---------------")

    for i, premise in enumerate(P.premises):
        print(f"{i} | {premise} [P]")
    print("   ---------------")


    for j, step in enumerate(P.deduction):
        formula = step[0]
        justification = step[1]
        print(f"{i + j + 1} | {formula} [{justification}]")