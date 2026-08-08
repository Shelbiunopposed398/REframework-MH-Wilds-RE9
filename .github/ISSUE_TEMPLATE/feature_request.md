name: Feature request
description: Suggest an idea or enhancement for TavernKeep
title: "[FEATURE] "
labels: ["enhancement"]
body:
  - type: textarea
    id: feature
    attributes:
      label: Feature Proposal
      description: Describe the feature or improvement you would like to see.
    validations:
      required: true
  - type: textarea
    id: motivation
    attributes:
      label: Motivation / Use Case
      description: Why would this feature be useful to users?
    validations:
      required: false
