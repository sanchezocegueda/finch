from wff import *

# proof is a list of wffs
A = SentenceSymbol("A")
B = SentenceSymbol("B")
C = SentenceSymbol("C")

justifications = [
    "ImpIntro",
    "ImpElim",
    "ConjIntro",
    "ConjElim"
]

premises = (A, Implies(A, B), Implies(B, C))
goal = And(B, C)
deduction = [(B, "ImpElim"), (C, "ImpElim"), (And(B, C), "ConjIntro")]

proof = Proof(premises, goal, deduction)

# TODO: Make this more efficient
def getAllSentenceSymbols(premises: List[Formula]):
    symbs = set()

    for premise in premises:
        symbs |= getSentenceSymbols(premise) 
    
    return symbs

def getSentenceSymbols(formula: Formula) -> Set[Formula]:
    if isinstance(formula, SentenceSymbol):
        symbs = set()
        symbs.add(formula.name)
        return symbs
    elif isinstance(formula, Not):
        return getSentenceSymbols(formula.phi)
    else:
        left  = getSentenceSymbols(formula.phi)
        right = getSentenceSymbols(formula.psi)
        return left | right

def findImplication(formula: Formula, facts: List[Formula]):
    
    # Find implication
    for fact in facts:
        if isinstance(fact, Implies) and is_equal(fact.psi,formula):
            hypothesis = fact.phi

            for cand in facts:
                if is_equal(hypothesis, cand):
                    return True

    return False

def findConjunction(formula: And, facts: List[Formula]):
    A = formula.phi
    B = formula.psi

    return A in facts and B in facts

def findJustification(formula: Formula, facts: List[Formula], maxDepth=10):

    # Attempt to synthesize a proof of the formula from the given set of facts
    # First idea: BFS up to a bound

    queue = []

    for a in facts:
        queue.append((a, 0))


    return False

def validate(proof: Proof):
    premises = proof.premises
    goal = proof.goal
    deduction = proof.deduction
    facts = []
    ssymbols = getAllSentenceSymbols(premises)
    facts.extend(premises)
    
    for idx, step in enumerate(deduction):
        formula, justification = step

        if justification == "P":
            if formula not in premises:
                print(f"Incorrect deduction: {formula} was marked with \"P\" but {formula} is not a premise.")
                return False

        elif justification == "ImpElim":
            if not findImplication(formula, facts):
                print(f"Incorrect deduction: {formula} was marked with \"ImpElim\" but no formula of the form (φ → {formula}) was found.")
                return False
        
        elif justification == "ConjIntro":
            if not findConjunction(formula, facts):
                print(f"Incorrect deduction: {formula} was marked with \"ConjIntro\" but one of {formula.phi} or {formula.psi} was not found.")

        # No idea; try something
        elif justification == "?":
            if not findJustification(formula, facts):
                print(f"Incorrect deduction: {formula} was marked with \"?\" but the synthesizer was unable to find a proof.")
                return False
        else: 
            print(f"Incorrectly-formatted justification: {justification}")
            return False

        facts.append(formula)
            

    return facts[len(facts)-1] == goal

print(validate(proof))
pretty_print(proof)