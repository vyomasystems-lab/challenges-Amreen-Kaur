# LEVEL-1 REPORT 
## 1.a: Mux Design Verification(Level-1:Design 1)
The verification environment is setup using Vyoma's UpTickPro provided for the hackathon.

![Image Link](https://github.com/vyomasystems-lab/challenges-Amreen-Kaur/blob/master/images/ss.jpg)

## Verification Environment
The CoCoTb based Python test is developed as explained. The test drives inputs to the Design Under Test (mux module here) which takes 5-bit input values for the select input(sel) and corresponding 2 bit values in inputs:0-31 as follows-
```python
dut.sel.value=0b00000
dut.inp0.value=0b01
```
Assert and print statements are used to check the output's equivalence to the input's value, given corresponding to the integer value depicted by the select line binary input as follows. It is then followed by a print statement for more clearance on the inputs and outputs.
```python
assert dut.out.value == 0b01, "Mux result is incorrect for select input:{A} & input :{B} as the output is not :{C} rather it is {D}".format(A = int(dut.sel.value),B = int(dut.inp0.value),C = int(dut.inp0.value),D = int(dut.out.value))

print("Mux result is correct for select input:{A} & input :{B} as the output is :{C} and not {D}".format(A = int(dut.sel.value),B = int(dut.inp0.value),C = int(dut.out.value),D = int(dut.inp17.value)))
```
This is an example of correct output with the given inputs.
## Test Scenario
1. The test inputs are given as follows-
```python
dut.sel.value=0b01100
dut.inp12.value=0b01
```
- According to the logic the output is not obtained and throws an error.
```python
AssertionError: Mux result is incorrect for select input :12 & input :1 as the output is not :1 rather it is 00.
```
- Expected Output-0b01.
- Observed Output-0b00.

Output mismatches for the above inputs proving that there is a design bug.

2. The test inputs are given as follows-
```python
dut.sel.value=0b11110
dut.inp30.value=0b01  
```
-According to the logic the output is not obtained and throws an error.
```python
AssertionError: Mux result is incorrect for select input:30 & input :1 as the output is not :1.
```
- Expected Output-0b01.

- Observed Output-0b00.

Output mismatches for the above inputs proving that there is a design bug.

The report obtained is as follows-

![Image Link](https://github.com/vyomasystems-lab/challenges-Amreen-Kaur/blob/master/images/mux.png)

## Design Bug
Based on the above test input and analysing the design, we see the following-
```verilog
5'b01101: out = inp12;
5'b01101: out = inp13;
```
Both the inputs 12 and 13 have the same select lines which should not be the case of a multiplexer as each input gets a unique select value.
It should be 5'b01100: out = inp12.
```verilog
5'b11101: out = inp29;
default: out = 0;
```
Here as explained in the question a 31:1 mux needs to compulsarily have 30 inputs. Any value outside 30 needs to get a default value. But only 29 select inputs were provided. So we need to add 5'b11110: out = inp30 to the code.
## Design Fix
Updating the design and re-running the test makes the test pass.

![Image Link](https://github.com/vyomasystems-lab/challenges-Amreen-Kaur/blob/master/images/mux%20corrected.png)

The updated design is checked in as level1_design1_correctcode.v .

## Verification Strategy
According to the digital design of an ideal n:1 mux, there needs to be n unique select input values possible which correspondingly selects n unique input values. Any other value apart from the n input values if given by the select lines results in a default output. This basic functionality of the mux needs to be correctly verified one by one for each of the select inputs and its corresponding outputs. Thus, the tests done perform the same, i.e. check the outputs for all the select inputs and inputs possible in a 31:1 mux and print an error if there is any discrepancy in the process.The block diagram of correct DUT is as shown below.

![image](https://github.com/vyomasystems-lab/challenges-Amreen-Kaur/blob/master/images/mux_dia.png)

## Is the verification complete ?
Yes, the verification is complete as per a 31:1 mux design.



