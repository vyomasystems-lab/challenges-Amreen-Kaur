import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer

@cocotb.test()
async def test_level3_bug1(dut):
    """Test for bist """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    dut.sw[0].value = 0
    dut.sw[1].value = 1
    dut.sw[2].value = 0
    dut.sw[3].value = 1
    await Timer(10, units='ns')
    print("The output obtained of the first led is {A}" .format(A=int(dut.led[0].value)))
    
    await Timer(10, units='ns')
    assert dut.led[0].value==0, "The output is incorrect as the first led itself is not reflecting its corresponding switch."
    
    