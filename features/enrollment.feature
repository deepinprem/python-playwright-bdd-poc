Feature: Kindergarten Online Enrollment Processing

  Scenario: Submit a new kindergarten enrollment application
    Given the user opens the Kindergarten Enrollment portal
    When the user selects the enrollment year "2026"
    And enters the child's full name "Chandni Premkumar"
    And enters parent name "Premkumar" and email "deepinprem@hotmail.com"
    And clicks the Submit Application button
    Then the confirmation heading displays "Student Chandni Premkumar submitted application for Kindergarden successfully"
    And a valid submission timestamp is displayed