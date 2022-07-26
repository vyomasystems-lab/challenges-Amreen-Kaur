# LEVEL-3 REPORT
## 1.b: Overlapping- Sequence Detector(1011) Design Verification(Level-1:Design 2)
The verification environment is setup using Vyoma's UpTickPro provided for the hackathon.

![image](https://github.com/vyomasystems-lab/challenges-Amreen-Kaur/blob/master/images/ss.jpg)

## Verification Environment
The CoCoTb based Python test is developed as explained. The test drives inputs to the Design Under Test, Built-in Self Test(BIST)(level_3 module here.

It is a self test mechanism in a system which tests
its constituents i.e. the four switches and the four LED’s via
a predefined algorithm on its own for proper operation.It
configures the LED’s when the switches are turned off and the
switches when no internal testing operation is being performed on
the LED’s. It helps in independent testing of the system without
any external help and makes the system robust, offering many
advantages that one could count of.

Clock and Switch inputs are provided to the system and the
LED’s are placed at the outputs. A flag is placed in the system
to test LED’s at F=0 and testing switches when F=1. After
slowing down the clock for LED testing(F=0), the LED’s are
made to glow one after the other and then turned off in a FILO
manner using the slower clock.The switches are tested(F=1) if
the output LED’s reflect the input values switched on.

The input values are given as follows-
```python
    dut.sw[0].value = 0
    dut.sw[1].value = 1
    dut.sw[2].value = 0
    dut.sw[3].value = 1
```
The led outputs are displayed using print outputs and an seert statement verifies the model as follows-
```python
assert dut.led[0].value==0, "The output is incorrect as the first led itself is not reflecting its corresponding switch."
```
## Test Scenario
- Given Input to the switches-0101.
- According to the logic the output is not obtained and throws an error.
```python
AssertionError: The output is incorrect as the first led itself is not reflecting its corresponding switch.
```
- Expected Output-0101.
- Observed Output-1XXX.

Output mismatches for the above inputs proving that there is a design bug.

The report obtained is as follows-

![image](https://github.com/vyomasystems-lab/challenges-Amreen-Kaur/blob/master/images/bist.png)

## Design Bug
Based on the above test input and analysing the design, we see the following-
While writing the code the statement-
```verilog
assign led = ~temp;
```
has been wrongly written as ~temp.
This causes the output to invert completely.

## Design Fix
Updating the design and re-running the test makes the test pass.

![image](https://github.com/vyomasystems-lab/challenges-Amreen-Kaur/blob/master/images/bist%20corrected.png)

The updated design is checked in as level3_correct.v .
## Verification Strategy
It is seen that the functionality of the module described above can be depicted by the following diagram.

![image](https://github.com/vyomasystems-lab/challenges-Amreen-Kaur/blob/master/images/bist_dia.png)
 
 The input is given in such a way that the functionality of switch test is being tested. The test requires that the inputs given be reflected as it is in the output hence just the first output checked is suffcient enough to testify that the bist is working properly.

## Is the verification complete ?
Yes, the verification is complete as per the Built-in Self Test Model.

