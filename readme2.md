# LEVEL-2 REPORT
## 1.b: Bitmanipulation Coprocessor Design Verification(Level-1:Design 2)
The verification environment is setup using Vyoma's UpTickPro provided for the hackathon.

![image](https://github.com/vyomasystems-lab/challenges-Amreen-Kaur/blob/master/images/ss.jpg)

## Verification Environment
The CoCoTb based Python test is developed as explained. The test drives inputs to the Design Under Test Bitmanipulation Coprocessor-ALU(mkbitmanip module here) which takes in four inputs with three of them being mav_putvalue_src1,mav_putvalue_src2,mav_putvalue_src3, which are the input values on which we perform the bitmanipulation instructions(Operands). They are of 32 bits each. The fourth one is an instruction input mav_putvalue_Instr of 32 bits which gives the instructions that tell what operation is to be performed on the input bits(Operations Code/Opcode). The output is a 33 bit value mav_put value with 32 bits of output of the peration performed on the input operands and one bit is a valid bit that tells the validity of the output obtained.
The values are assigned to the input port using-
```python
dut.mav_putvalue_src1.value = mav_putvalue_src1
dut.mav_putvalue_src2.value = mav_putvalue_src2
dut.mav_putvalue_src3.value = mav_putvalue_src3
dut.EN_mav_putvalue.value = 1
dut.mav_putvalue_instr.value = mav_putvalue_instr
```
where input1 and input2 are randomised. It is of half the range of all the possible 2^32 inputs possible as operands.

Two different instruction commands are performed. The first one is for instruction =0x40007033. The second one includes all the remaining instructions that are performed by the coprocessor.

The outputs are obtained for each instruction performed and all the values are simultaneously printed using print and log commands.

The expected values are mapped from the model file and the two outputs obtained are compared using an assert statement as follows-
```python
error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
assert dut_output == expected_mav_putvalue, error_message
```
## Test Scenario
- The test inputs of operands are randomised uptil 65535.

- The instruction input value =0x40007033.

- According to the logic the output is not obtained and throws an error.
```python
AssertionError: Value mismatch DUT = 0x3 does not match MODEL = 0x12641
```
- Expected Output-0x12641.
- Observed Output-0x3.

Output mismatches for the above inputs proving that there is a design bug.

The report obtained is as follows-

![image](https://github.com/vyomasystems-lab/challenges-Amreen-Kaur/blob/master/images/bitman.png)

## Verification Strategy
The working of the Bitmanipulation Coprocessor Model is explained before.
The block diagram of the same is shown below.

![image](https://github.com/vyomasystems-lab/challenges-Amreen-Kaur/blob/master/images/Bitman_dia.png)

The instruction set of the processor is shown below.

![image](https://github.com/vyomasystems-lab/challenges-Amreen-Kaur/blob/master/images/bitman_instr.png)

In order to calculate the input instruction that goes inside the processor we need to calculate the effective instruction. As the
func7, f3 and the opcode form the effective instruction of operation, the correct instruction is input. rs2, rs1 and rd are disregarded while calculating the effective instruction as they are not of influence for block level verification.

By putting in the values of inputs(operands and effective opcodes) we obtain an output value which is then compared to the expected output value from the model. This intensive process to check every instruction helps us to decode that there is a bug in the design's operation.
## Is the verification complete ?
Yes, the verification is complete as per the model provided alongside with the design of the coprocessor.



