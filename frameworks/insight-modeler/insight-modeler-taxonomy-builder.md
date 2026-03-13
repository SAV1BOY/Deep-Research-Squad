# Taxonomy Builder Framework

## Purpose

Build structured taxonomies from research findings. Identify meaningful categories, define relationships and hierarchies among them, and validate the resulting classification system for completeness, consistency, and practical utility. A good taxonomy turns a disorganized set of findings into a navigable knowledge structure.

## When to Use

- When research produces many findings that need to be organized into coherent groups.
- When existing categories are inadequate to describe what has been discovered.
- When stakeholders need a shared vocabulary and classification system for a domain.
- When comparing items that span multiple dimensions and need structured categorization.

## Inputs

- A collection of items, findings, or concepts to be classified.
- Any existing classification systems or taxonomies in the domain.
- Understanding of the purpose the taxonomy will serve (who uses it and for what).
- Domain expertise to validate category boundaries.

## Process

### Step 1: Item Inventory
List every item to be classified. Include descriptions sufficient to distinguish each item from others. Do not pre-categorize at this stage.

### Step 2: Attribute Extraction
For each item, identify its key attributes or properties. What dimensions differentiate items from each other? Look for:
- Functional attributes (what it does).
- Structural attributes (what it is made of or how it is organized).
- Contextual attributes (where, when, or by whom it is used).
- Relational attributes (how it connects to other items).

### Step 3: Bottom-Up Grouping
Cluster items that share key attributes into provisional groups. Use natural similarity rather than forcing items into pre-existing categories. Let the data suggest the categories.

### Step 4: Top-Down Validation
Test provisional groups against the taxonomy's purpose. Ask:
- Does each category serve a distinct function for the user?
- Can a user reliably place a new item into the correct category?
- Are the categories at a useful level of granularity (not too broad, not too narrow)?

### Step 5: Hierarchy Construction
Organize categories into levels. Typical structures:
- **Flat**: All categories at the same level (simple, limited to small sets).
- **Two-level**: Broad categories with subcategories (most common and practical).
- **Multi-level**: Deep hierarchies (powerful but complex, risk over-engineering).
Define parent-child relationships and the principle that governs each level of division.

### Step 6: Boundary Definition
For each category, define:
- **Inclusion criteria**: What must be true for an item to belong here.
- **Exclusion criteria**: What disqualifies an item from this category.
- **Edge cases**: Items that sit near category boundaries, with a ruling on where they belong.

### Step 7: Completeness Check
Test whether the taxonomy covers all items in the inventory. If any item does not fit any category:
- Is the item genuinely different (add a new category)?
- Is the item a hybrid (consider cross-classification or a bridging category)?
- Is the item an outlier (note it explicitly rather than forcing it in)?

### Step 8: Consistency Check
Verify that the same classification principle is applied consistently within each level. Mixing classification principles at the same level (e.g., some categories by function, others by size) creates confusion.

## Outputs

- A taxonomy diagram or structured list showing all categories, subcategories, and their relationships.
- Definitions for each category with inclusion and exclusion criteria.
- A mapping of all original items to their assigned categories.
- A list of edge cases and how they were resolved.
- An assessment of the taxonomy's limitations and where it may need future revision.

## Common Pitfalls

- **Category proliferation**: Creating too many categories, making the taxonomy unusable. Aim for 5-9 categories at each level.
- **Forced fit**: Jamming items into categories where they do not naturally belong rather than creating appropriate new ones.
- **Mixed principles**: Using different classification criteria at the same hierarchical level.
- **Premature rigidity**: Treating the taxonomy as final before testing it against real use cases.
- **Ignoring purpose**: Building an academically elegant taxonomy that does not serve the practical needs of its users.
- **Single-dimension thinking**: Classifying only along one dimension when items naturally vary along multiple dimensions.

## Related Frameworks

- **synthesis-conclusion-ladder.md** - Uses taxonomies to organize findings at the Patterns rung of the ladder.
- **insight-modeler-causal-map.md** - Maps causal relationships between taxonomy categories.
- **insight-modeler-decision-matrix.md** - Uses taxonomy categories as rows or columns in decision analysis.
- **synthesis-layered-synthesis.md** - Organizes taxonomy items by certainty level.
