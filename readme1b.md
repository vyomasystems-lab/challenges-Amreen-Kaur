# LEVEL-1 REPORT
## 1.b: Overlapping- Sequence Detector(1011) Design Verification(Level-1:Design 2)
The verification environment is setup using Vyoma's UpTickPro provided for the hackathon.

![image](https://github.com/vyomasystems-lab/challenges-Amreen-Kaur/blob/master/images/ss.jpg)

## Verification Environment
The CoCoTb based Python test is developed as explained. The test drives inputs to the Design Under Test (seq_detect_1011 module here) which takes in bitwise input 'inp_bit' on every positive edge of an another input named 'clk' or the clock signal. One additional input named reset is also given to initialize the design when needed. This combination yields the bitwise output named 'seq_seen'.The output turns 1 when the input sequence of 1011 is detected.

The input values are given as follows-

```python
dut.inp_bit.value = 0b0
```
The other inputs of clock and reset are also given appropriately and the output is tested using an assert statement.

For better understanding of the working, required outputs and inputs are logged.

The assert statement is used for comparing the adder's outut to the expected value.

```python
assert dut.seq_seen.value == 0b1,"the output of the sequence detector is wrong for the input bits "
print("the value of output is {A} ".format(A=dut.seq_seen.value))
```
## Test Scenario
 - The test inputs are given as-111011011011.
 - According to the logic the output is not obtained and throws an error at the end of the code where an assertion statement is provided.

 ```python
 AssertionError: the output of the sequence detector is wrong for the input bits. 
```
- Expected Output-000001001001.
- Observed Output-000001000000.

Output mismatches for the above inputs proving that there is a design bug.

The report obtained is as follows-

![image](https://github.com/vyomasystems-lab/challenges-Amreen-Kaur/blob/master/images/seq.png)

## Design Bug
Based on the above test input and analysing the design, we see the following-

1. The state SEQ_11 is missing, therefore the code fails when the sequence has more than 2 1's as given in the test case.

```verilog
parameter IDLE = 0,
            SEQ_1 = 1, 
            SEQ_10 = 2,
            SEQ_101 = 3,
            SEQ_1011 = 4;
```
2. The second bug is found to  be that there is no redirection to SEQ_10 to enable the overlapping functionality.Without this the assert statement that was put at the end of the test case was failing.

```verilog
SEQ_1011:
      begin
        next_state = IDLE;
      end
```
## Design Fix
Updating the design and re-running the test makes the test pass.

![image](https://github.com/vyomasystems-lab/challenges-Amreen-Kaur/blob/master/images/seq%20corrected.png)

The updated design is checked in as level1_design2_correctcode.v .

## Verification Strategy
It is seen that the functionality of the module described above can be depicted by the following block diagram.

![image](https://github.com/vyomasystems-lab/challenges-Amreen-Kaur/blob/master/images/seq_dia.png)

The input sequence taken for verification purposes is decided on in such a way that all the states are checked during execution along with the overlapping condition of the sequence detector module. This strategy helps in ensuring that the model detects all possible sequences of 1011. The DUT output is logged at every input which helps us to see whether each and every sequence is detected or not.

## Is the verification complete ?
Yes, the verification is complete as per a 31:1 mux design.