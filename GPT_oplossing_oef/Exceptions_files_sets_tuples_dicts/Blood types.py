# --- Helper data ---

# Possible genotypes for each ABO phenotype
ABO_GENOTYPES = {
    "A": [("A", "A"), ("A", "O")],
    "B": [("B", "B"), ("B", "O")],
    "AB": [("A", "B")],
    "O": [("O", "O")]
}

# Rhesus genotypes
RH_GENOTYPES = {
    "+": [("+", "+"), ("+", "-")],
    "-": [("-", "-")]
}


def get_abo_from_alleles(a1, a2):
    """Return ABO phenotype from two alleles."""
    s = {a1, a2}
    if s == {"A", "B"}:
        return "AB"
    if "A" in s and "B" not in s:
        return "A"
    if "B" in s and "A" not in s:
        return "B"
    return "O"


def get_rh_from_alleles(r1, r2):
    """Return + or - phenotype."""
    return "+" if "+" in (r1, r2) else "-"


def possible_children(father, mother):
    """Return all possible genotype combinations from two parents."""
    f_abo = ABO_GENOTYPES[father[:-1]]
    f_rh = RH_GENOTYPES[father[-1]]

    m_abo = ABO_GENOTYPES[mother[:-1]]
    m_rh = RH_GENOTYPES[mother[-1]]

    children = set()

    for fa1, fa2 in f_abo:
        for ma1, ma2 in m_abo:
            for f_r1, f_r2 in f_rh:
                for m_r1, m_r2 in m_rh:
                    # ABO allele combinations (4 possibilities)
                    for a1 in [fa1, fa2]:
                        for a2 in [ma1, ma2]:
                            abo = get_abo_from_alleles(a1, a2)

                            # Rhesus allele combinations (4 possibilities)
                            for r1 in [f_r1, f_r2]:
                                for r2 in [m_r1, m_r2]:
                                    rh = get_rh_from_alleles(r1, r2)
                                    children.add(abo + rh)

    return children


# ------------------------------------------------
# PART 1 — CHILD BLOODGROUPS
# ------------------------------------------------

def bloodgroup_child(parent1, parent2):
    result = possible_children(parent1, parent2)
    print(result)


# ------------------------------------------------
# PART 2 — POSSIBLE BLOODGROUPS OF UNKNOWN PARENT
# ------------------------------------------------

ALL_GROUPS = ["O-", "O+", "A-", "A+", "B-", "B+", "AB-", "AB+"]


def bloodgroup_parent(parent_known, child):
    possible = set()

    for candidate in ALL_GROUPS:
        children = possible_children(parent_known, candidate)
        if child in children:
            possible.add(candidate)

    print(possible)