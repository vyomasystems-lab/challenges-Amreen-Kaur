# See LICENSE.cocotb for details
# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Testtrue for mux"""
    dut.sel.value=0b00000
    dut.inp0.value=0b01
    dut.inp17.value=0b00

    await Timer(2, units='ns')
    assert dut.out.value == 0b01, "Mux result is incorrect for select input:{A} & input :{B} as the output is not :{C} rather it is {D}".format(A = int(dut.sel.value),B = int(dut.inp0.value),C = int(dut.inp0.value),D = int(dut.out.value))
    print("Mux result is correct for select input:{A} & input :{B} as the output is :{C} and not {D}".format(A = int(dut.sel.value),B = int(dut.inp0.value),C = int(dut.out.value),D = int(dut.inp17.value)))

@cocotb.test()
async def test1_mux(dut):
    """Test1_13 for mux"""
    dut.sel.value=0b01101
    dut.inp13.value=0b01
    dut.inp12.value=0b00

    await Timer(2, units='ns')
    assert dut.out.value == 0b01, "Mux result is incorrect for select input:{A} & input :{B} as the output is not :{C} rather it is {D}".format(A = int(dut.sel.value),B = int(dut.inp13.value),C = int(dut.inp13.value),D = int(dut.out.value))
    print("Mux result is correct for select input:{A} & input :{B} as the output is :{C} and not {D}".format(A = int(dut.sel.value),B = int(dut.inp13.value),C = int(dut.out.value),D = int(dut.inp12.value)))

@cocotb.test()
async def test2_mux(dut):
    """Test2_12 for mux"""
    dut.sel.value=0b01100
    dut.inp12.value=0b01
    

    await Timer(2, units='ns')
    assert dut.out.value == 0b01, "Mux result is incorrect for select input :{A} & input :{B} as the output is not :{C} ".format(A = int(dut.sel.value),B = int(dut.inp12.value),C = int(dut.inp12.value))
    print("Mux result is correct for select input:{A} & input :{B} as the output is :{C} ".format(A = int(dut.sel.value),B = int(dut.inp12.value),C = int(dut.out.value)))

@cocotb.test()
async def test3_mux(dut):
    """Test3_30 for mux"""
    dut.sel.value=0b11110
    dut.inp30.value=0b01
    

    await Timer(2, units='ns')
    assert dut.out.value == 0b01, "Mux result is incorrect for select input:{A} & input:{B} as the output is not :{C}".format(A = int(dut.sel.value),B = int(dut.inp30.value),C = int(dut.inp30.value))
    print("Mux result is correct for select input:{A} & input:{B} as the output is:{C}".format(A = int(dut.sel.value),B = int(dut.inp30.value),C = int(dut.inp30.value)))
