`timescale 1 ns / 100 ps
`define TESTVECS 8

module tb_counter;
    reg clk, reset;
    reg inc;
    wire [2:0] cur_adr;
    wire cout;

    reg test_vecs [0:(`TESTVECS-1)];

    integer i;

    initial begin 
        $dumpfile("tb_counter.vcd"); 
        $dumpvars(0, tb); 
    end

    initial begin 
        reset = 1'b1; 
        #12.5 reset = 1'b0; 
    end
    
    initial clk = 1'b0;
    always #5 clk =~ clk;

    initial begin
        test_vecs[0] = 1'b1;
        test_vecs[1] = 1'b1;
        test_vecs[2] = 1'b1;
        test_vecs[3] = 1'b1;
        test_vecs[4] = 1'b1;
        test_vecs[5] = 1'b1;
        test_vecs[6] = 1'b1;
        test_vecs[7] = 1'b1;
    end

    initial {inc} = 0;
    ptr_reg ptr(clk, reset, inc, cur_adr, cout);

    initial begin
        #6 for (i=0; i<`TESTVECS; i=i+1)
            begin #10 {inc}=test_vecs[i]; end
        #100 $finish;
    end
endmodule