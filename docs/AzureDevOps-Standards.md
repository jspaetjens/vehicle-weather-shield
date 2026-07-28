# Vehicle Weather Shield

# Azure DevOps Standards

> *This document defines the Azure DevOps work item standards used to implement the approved Version 1.0 Documentation Baseline.*

**Version:** 1.0

**Status:** Approved Baseline

**Last Updated:** 2026-07-28

**Target Release:** v1.0.0

**License:** MIT

**Author:** Jack Spaetjens

---

## Document History

| Version | Date | Author | Description |
|----------|------------|----------------|------------------------------------------------|
| 0.1 | 2026-07-28 | Jack Spaetjens | Initial Azure DevOps governance document. |
| 1.0 | 2026-07-28 | Jack Spaetjens | Editorial review completed and approved as the Azure DevOps governance baseline for Vehicle Weather Shield Version 1.0. |

---

# Table of Contents

- [Vehicle Weather Shield](#vehicle-weather-shield)
- [Azure DevOps Standards](#azure-devops-standards)
  - [Document History](#document-history)
- [Table of Contents](#table-of-contents)
- [1. Purpose](#1-purpose)
- [2. Scope](#2-scope)
- [3. Source of Truth](#3-source-of-truth)
- [4. Azure DevOps Hierarchy](#4-azure-devops-hierarchy)
- [5. Traceability](#5-traceability)
- [6. Work Item Standards](#6-work-item-standards)
  - [Epic](#epic)
  - [Feature](#feature)
  - [Product Backlog Item](#product-backlog-item)
  - [Task](#task)
- [7. Naming Conventions](#7-naming-conventions)
- [8. Acceptance Criteria](#8-acceptance-criteria)
- [9. Definition of Ready](#9-definition-of-ready)
- [10. Definition of Done](#10-definition-of-done)
- [11. Relationships](#11-relationships)
- [12. Labels and Tags](#12-labels-and-tags)
- [13. Work Item Lifecycle](#13-work-item-lifecycle)
- [14. Governance](#14-governance)

---

# 1. Purpose

This document defines the Azure DevOps standards used by the Vehicle Weather Shield project.

Its purpose is to ensure a consistent backlog structure, maintain complete traceability to the approved Version 1.0 Documentation Baseline, and establish common working practices for planning and implementation.

---

# 2. Scope

These standards apply to every Azure DevOps work item created for Vehicle Weather Shield Version 1.0.

This includes:

- Epics
- Features
- Product Backlog Items (PBIs)
- Tasks

---

# 3. Source of Truth

The approved Version 1.0 Documentation Baseline is the authoritative source for all Azure DevOps work items.

The Azure DevOps backlog shall faithfully represent the approved documentation.

Azure DevOps shall not introduce:

- new functionality
- additional requirements
- undocumented behaviour
- scope extensions

Every work item shall be traceable to one or more approved documentation sections.

---

# 4. Azure DevOps Hierarchy

Vehicle Weather Shield uses the Scrum process.

The following hierarchy shall be used.

Theme

↓

Epic

↓

Feature

↓

Product Backlog Item (PBI)

↓

Task

The mapping to Azure DevOps is:

| Logical Level | Azure DevOps |
|----------------|----------------|
| Theme | Epic |
| Epic | Feature |
| Feature | Product Backlog Item |
| Work | Task |

---

# 5. Traceability

Every Product Backlog Item shall contain:

- Source Document
- Source Section
- Requirement Identifier
- Documentation Version

Example

Source Document

01-PRD.md

Source Section

6. Functional Requirements

Requirement

FR-001

Documentation Version

1.0

---

# 6. Work Item Standards

## Epic

Represents the overall project theme.

Example

Vehicle Weather Shield v1.0

---

## Feature

Represents a major business capability.

Examples

- Weather Detection
- Vehicle Integration
- Notifications
- Home Assistant Integration
- Distribution

---

## Product Backlog Item

Represents one functional requirement or implementation objective.

Example

FR-001 Hail Detection

Every Product Backlog Item shall contain:

- Requirement
- Source Document
- Source Section
- Traceability
- Documentation Version
- Acceptance Criteria

---

## Task

Tasks describe implementation work required to complete a Product Backlog Item.

Typical task categories include:

- Design
- Implementation
- Testing
- Documentation

---

# 7. Naming Conventions

Epics

Vehicle Weather Shield v1.0

Features

Use business capability names.

Example

Weather Detection

PBIs

Use requirement identifiers where available.

Example

FR-001 Hail Detection

Tasks

Use verb-based titles.

Examples

Implement hail detection

Create unit tests

Update documentation

---

# 8. Acceptance Criteria

Acceptance Criteria define the measurable conditions that must be satisfied before a Product Backlog Item can be considered complete.

Acceptance Criteria shall:

- be derived directly from the approved documentation
- not introduce additional requirements
- be objectively testable
- remain traceable to the originating requirement

Example

Requirement

The integration shall detect the risk of hail for the configured location.

Acceptance Criteria

- The integration detects the risk of hail for the configured location.

---

# 9. Definition of Ready

A Product Backlog Item is considered ready when:

- parent Feature exists
- source documentation identified
- traceability established
- acceptance criteria documented
- dependencies identified where applicable

---

# 10. Definition of Done

A Product Backlog Item is complete when:

- implementation completed
- acceptance criteria satisfied
- required unit tests completed
- documentation updated where applicable
- code review completed
- CI pipeline successful

---

# 11. Relationships

Parent-child relationships shall be maintained.

Epic

↓

Feature

↓

Product Backlog Item

↓

Task

No Task shall exist without a parent Product Backlog Item.

---

# 12. Labels and Tags

Tags may be used to improve searching and reporting.

Recommended tags include:

- v1.0
- Documentation
- Architecture
- Testing
- Home Assistant
- Tesla
- Weather
- Notifications

Tags shall not replace traceability.

---

# 13. Work Item Lifecycle

Every work item shall progress through the standard Azure DevOps workflow.

New

↓

Approved

↓

Committed

↓

In Progress

↓

Code Review

↓

Done

---

# 14. Governance

This document defines the Azure DevOps governance standard for Vehicle Weather Shield.

Changes to these standards shall be reviewed and approved before becoming part of the project baseline.

The Azure DevOps backlog shall remain fully aligned with the approved Version 1.0 Documentation Baseline throughout the project lifecycle.