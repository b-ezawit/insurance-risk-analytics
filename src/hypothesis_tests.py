import scipy.stats as stats

# -----------------------
# T-TEST (numeric KPIs)
# -----------------------


def t_test(group_a, group_b):
    stat, p_value = stats.ttest_ind(group_a, group_b, equal_var=False)
    return stat, p_value


# -----------------------
# CHI-SQUARE TEST (categorical KPIs)
# -----------------------


def chi_square_test(table):
    stat, p_value, dof, expected = stats.chi2_contingency(table)
    return stat, p_value


# -----------------------
# DECISION FUNCTION
# -----------------------


def decision(p_value, alpha=0.05):
    return "Reject H0" if p_value < alpha else "Fail to Reject H0"
