# GCP Snowflake Data Egress Cost Guardrail

Data egress cost guardrail for GCP, BigQuery, and Snowflake movement-risk decisions.

![ci](https://github.com/mizcausevic-dev/gcp-snowflake-data-egress-cost-guardrail/actions/workflows/ci.yml/badge.svg)

## Why this exists

This is a Kinetic Gain signal surface for GCP, Snowflake. It turns fragmented operational facts into board-ready questions:

- Where are we exposed?
- Where can we save money?
- Where should we invest?
- What story do we tell with evidence?

## Signal lanes

- egress cost
- warehouse burn
- BigQuery slot pressure
- Snowflake share drift
- data lineage gaps
- FinOps sequencing

## Stack signal

- Primary language signal: Python
- Vertical: Platform Engineering / Data Engineering
- Portfolio family: GCP + Snowflake
- Live surface: https://mizcausevic-dev.github.io/gcp-snowflake-data-egress-cost-guardrail/

## Local verification

~~~bash
npm test
~~~

The validation script checks the generated evidence payload and confirms the static board surface exists.
