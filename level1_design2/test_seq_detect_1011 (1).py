# See LICENSE.vyoma for details
# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0

    #i/p sequence

    dut.inp_bit.value = 0b1
    await FallingEdge(dut.clk)
    cocotb.log.info(f'DUT INTPUT={(dut.inp_bit.value)}')
    cocotb.log.info(f'DUT OUTPUT={(dut.seq_seen.value)}')
    
    dut.inp_bit.value = 0b1
    await FallingEdge(dut.clk)
    cocotb.log.info(f'DUT INTPUT={(dut.inp_bit.value)}')
    cocotb.log.info(f'DUT OUTPUT={(dut.seq_seen.value)}')

    dut.inp_bit.value = 0b1
    await FallingEdge(dut.clk)
    cocotb.log.info(f'DUT INTPUT={(dut.inp_bit.value)}')
    cocotb.log.info(f'DUT OUTPUT={(dut.seq_seen.value)}')
    
    dut.inp_bit.value = 0b0
    await FallingEdge(dut.clk)
    cocotb.log.info(f'DUT INTPUT={(dut.inp_bit.value)}')
    cocotb.log.info(f'DUT OUTPUT={(dut.seq_seen.value)}')
    

    dut.inp_bit.value = 0b1
    await FallingEdge(dut.clk)
    cocotb.log.info(f'DUT INTPUT={(dut.inp_bit.value)}')
    cocotb.log.info(f'DUT OUTPUT={(dut.seq_seen.value)}')
    
    dut.inp_bit.value = 0b1
    await FallingEdge(dut.clk)
    cocotb.log.info(f'DUT INTPUT={(dut.inp_bit.value)}')
    cocotb.log.info(f'DUT OUTPUT={(dut.seq_seen.value)}')
    
    dut.inp_bit.value = 0b0
    await FallingEdge(dut.clk)
    cocotb.log.info(f'DUT INTPUT={(dut.inp_bit.value)}')
    cocotb.log.info(f'DUT OUTPUT={(dut.seq_seen.value)}')
    
    dut.inp_bit.value = 0b1
    await FallingEdge(dut.clk)
    cocotb.log.info(f'DUT INTPUT={(dut.inp_bit.value)}')
    cocotb.log.info(f'DUT OUTPUT={(dut.seq_seen.value)}')
    
    dut.inp_bit.value = 0b1
    await FallingEdge(dut.clk)
    cocotb.log.info(f'DUT INTPUT={(dut.inp_bit.value)}')
    cocotb.log.info(f'DUT OUTPUT={(dut.seq_seen.value)}')
    
    dut.inp_bit.value = 0b0
    await FallingEdge(dut.clk)
    cocotb.log.info(f'DUT INTPUT={(dut.inp_bit.value)}')
    cocotb.log.info(f'DUT OUTPUT={(dut.seq_seen.value)}')
    
    dut.inp_bit.value = 0b1
    await FallingEdge(dut.clk)
    cocotb.log.info(f'DUT INTPUT={(dut.inp_bit.value)}')
    cocotb.log.info(f'DUT OUTPUT={(dut.seq_seen.value)}')
   
    dut.inp_bit.value = 0b1
    await FallingEdge(dut.clk) 
    cocotb.log.info(f'DUT INTPUT={(dut.inp_bit.value)}')
    cocotb.log.info(f'DUT OUTPUT={(dut.seq_seen.value)}')

    assert dut.seq_seen.value == 0b1,"the output of the sequence detector is wrong for the input bit. "
    print("the value of output is {A} ".format(A=dut.seq_seen.value))
