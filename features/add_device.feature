Feature: Devices tests

  Scenario: Add device with check
     Given I have added a device
      When Check added device
      Then I see correct status and response
