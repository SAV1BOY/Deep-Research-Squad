# Sensitivity / What-If Analysis

> **Purpose:** Test how conclusions change when key assumptions or inputs are varied.
> Reveals which variables have the greatest influence on outcomes and where uncertainty matters most.
> Use `{{placeholder}}` markers to fill in project-specific details.

---

## When to Use

- Stress-testing a recommendation before presenting to decision-makers
- When findings depend heavily on assumptions that could prove wrong
- When stakeholders ask "what if X changes?" or "how sure are you?"

---

**Project:** {{project_name}}
**Analysis Date:** {{date_yyyy_mm_dd}}
**Analyst:** {{researcher_name}}
**Related Report:** {{link_to_parent_report}}

---

## 1. Base Case Summary

**Primary conclusion:** {{the_main_finding_or_recommendation_under_test}}

**Key metric/outcome:** {{the_quantitative_or_qualitative_outcome_being_measured}}

**Base case value:** {{the_value_or_assessment_under_current_assumptions}}

## 2. Variables Under Test

| # | Variable | Base Case Value | Rationale for Testing | Sensitivity |
|---|----------|----------------|----------------------|-------------|
| 1 | {{variable_name}} | {{current_value}} | {{why_this_might_change}} | {{high_medium_low}} |
| 2 | {{variable_name}} | {{current_value}} | {{why_this_might_change}} | {{sensitivity}} |
| 3 | {{variable_name}} | {{current_value}} | {{why_this_might_change}} | {{sensitivity}} |

> Instruction: Focus on the 3-6 variables that most influence the conclusion.

## 3. Scenario Analysis

### Scenario A: {{scenario_name_eg_optimistic}}

| Variable | Adjusted Value | Basis for Adjustment |
|----------|---------------|---------------------|
| {{variable_1}} | {{new_value}} | {{rationale}} |
| {{variable_2}} | {{new_value}} | {{rationale}} |

**Outcome under Scenario A:** {{how_conclusion_changes}}

### Scenario B: {{scenario_name_eg_pessimistic}}

| Variable | Adjusted Value | Basis for Adjustment |
|----------|---------------|---------------------|
| {{variable_1}} | {{new_value}} | {{rationale}} |
| {{variable_2}} | {{new_value}} | {{rationale}} |

**Outcome under Scenario B:** {{how_conclusion_changes}}

### Scenario C: {{scenario_name_eg_black_swan}}

| Variable | Adjusted Value | Basis for Adjustment |
|----------|---------------|---------------------|
| {{variable_1}} | {{new_value}} | {{rationale}} |

**Outcome under Scenario C:** {{how_conclusion_changes}}

## 4. Sensitivity Summary Table

| Variable | -20% Change | Base Case | +20% Change | Conclusion Holds? |
|----------|------------|-----------|------------|-------------------|
| {{variable_1}} | {{outcome}} | {{base_outcome}} | {{outcome}} | {{yes_no_partially}} |
| {{variable_2}} | {{outcome}} | {{base_outcome}} | {{outcome}} | {{yes_no_partially}} |
| {{variable_3}} | {{outcome}} | {{base_outcome}} | {{outcome}} | {{yes_no_partially}} |

> Instruction: Adjust the percentage range to match what is realistic for each variable.

## 5. Breakpoint Analysis

| Variable | Value at Which Conclusion Flips | How Likely Is This? |
|----------|-------------------------------|-------------------|
| {{variable_1}} | {{threshold_value}} | {{likely_plausible_unlikely}} |
| {{variable_2}} | {{threshold_value}} | {{likelihood}} |

> Instruction: Identify the tipping points. At what value does the recommendation change?

## 6. Key Takeaways

1. {{takeaway_1_eg_conclusion_is_robust_across_most_scenarios}}
2. {{takeaway_2_eg_variable_X_is_the_critical_swing_factor}}
3. {{takeaway_3_eg_monitor_variable_Y_as_early_warning}}

## 7. Recommendations

- **Proceed with confidence if:** {{conditions_under_which_base_case_is_safe}}
- **Revisit conclusion if:** {{trigger_conditions_for_re_analysis}}
- **Monitor closely:** {{variables_requiring_ongoing_tracking}}

---

### Example (Filled)

**Base Case:** Recommend entering Market X (projected 15% ROI over 3 years)

**Breakpoint Analysis:**
| Variable | Breakpoint | Likelihood |
|----------|-----------|-----------|
| Customer acquisition cost | > $340/customer (base: $220) | Plausible if competition intensifies |
| Market growth rate | < 8% CAGR (base: 14%) | Unlikely based on 5-year trend |

**Takeaway:** Recommendation holds unless acquisition costs rise 55%+ above baseline.

---

*Analysis conducted by {{researcher_name}} on {{date_yyyy_mm_dd}}*
