# Contributing to Deep Research Squad

## How to Contribute

### Adding a New Agent

1. Create the agent file in `agents/` following the standard structure:
   - Identity & Role
   - Mission & Scope
   - Pipeline Position
   - Inputs / Outputs
   - Frameworks (with file paths)
   - Checklists (with file paths)
   - Reasoning Protocol (CoT/ReAct)
   - Escalation Rules
   - Handoff Protocol
   - Anti-patterns

2. Create agent-specific frameworks in `frameworks/<agent-name>/`

3. Create per-agent gate checklists in `checklists/<agent-name>/`

4. Add the agent to `config.yaml` routing

5. Create an agent summary in `authority/agent-summaries/`

### Adding a New Framework

1. Determine if the framework is:
   - **Universal** → place in `frameworks/` root
   - **Agent-specific** → place in `frameworks/<agent-name>/`
   - **Layer-specific** → place in `frameworks/<layer>/`
   - **Reference** → place in `frameworks/reference-intellectual/`

2. Follow the standard framework structure:
   - Purpose and scope
   - When to apply
   - Core principles
   - Step-by-step methodology
   - Output format
   - Integration points

### Adding a New Workflow

1. Assign the next number in sequence (check `workflows/` for current max)
2. Follow the workflow template structure
3. Define inputs, outputs, and agent assignments
4. Specify quality gates

### Adding a New Checklist

1. Determine the checklist type:
   - **Macro** → `checklists/` root
   - **Per-agent gate** → `checklists/<agent-name>/`
   - **System gate** → `checklists/<layer>/`

2. Use `- [ ]` checkbox format for all items
3. Define pass/fail criteria
4. Specify escalation rules

## Quality Standards

- Every file must serve a clear purpose in the research pipeline
- Agent prompts must use SOTA prompt engineering techniques
- Frameworks must be actionable, not theoretical
- Checklists must have measurable pass/fail criteria
- Templates must use `{{placeholder}}` format for variable fields

## File Naming Conventions

- Use kebab-case for all file names
- Agent files: `<role-name>.md`
- Framework files: `<framework-name>.md`
- Checklist files: `<gate-name>-gate.md` or `<checklist-name>-checklist.md`
- Workflow files: `<NN>-<workflow-name>.md`
- Template files: `<template-name>-template.md`

## Language Policy

- Agent prompts, frameworks, workflows: **English**
- References, cultural context, BR-specific content: **Portuguese**
- Documentation: **English** (primary), Portuguese annotations where relevant
