name: Bug report
description: Create a report to help us improve TavernKeep
title: "[BUG] "
labels: ["bug"]
body:
  - type: textarea
    id: description
    attributes:
      label: Bug Description
      description: A clear and concise description of what the bug is.
    validations:
      required: true
  - type: textarea
    id: reproduction
    attributes:
      label: Steps To Reproduce
      description: Steps to reproduce the behavior.
      placeholder: |
        1. Run `.\scripts\install.ps1`
        2. Open `http://localhost:5000/manager/`
        3. Click on 'Pull Model'
    validations:
      required: true
  - type: dropdown
    id: os
    attributes:
      label: Operating System
      options:
        - Windows
        - Linux
        - macOS
    validations:
      required: true
