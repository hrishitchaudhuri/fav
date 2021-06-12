module array_slice (input wire [2:0] in, input wire clk, reset, load, output wire [2:0] out);
    dfrl df1(clk, reset, load, in[2], out[2]);
	dfrl df2(clk, reset, load, in[1], out[1]);
	dfrl df3(clk, reset, load, in[0], out[0]);
endmodule

module ptr_reg (input wire clk, reset, inc, output wire [2:0] cur_adr, output wire cout);
    wire q_in0, q_in1, q_in2, t0, t1, t2;

    xor2 xor_0(inc, cur_adr[0], q_in0);
    and2 and_0(inc, cur_adr[0], t0);

    xor2 xor_1(t0, cur_adr[1], q_in1);
    and2 and_1(t0, cur_adr[1], t1);

    xor2 xor_2(t1, cur_adr[2], q_in2);
    and2 and_2(t1, cur_adr[2], cout);

    dfr df_0(clk, reset, q_in0, cur_adr[0]);
    dfr df_1(clk, reset, q_in1, cur_adr[1]);
    dfr df_2(clk, reset, q_in2, cur_adr[2]);
endmodule

module register_file(input wire [2:0] din, input wire clk, reset, input wire [7:0] load, output wire [2:0] dout);
    array_slice as0(din, clk, reset, load[0], dout);
    array_slice as1(din, clk, reset, load[1], dout);
    array_slice as2(din, clk, reset, load[2], dout);
    array_slice as3(din, clk, reset, load[3], dout);
    array_slice as4(din, clk, reset, load[4], dout);
    array_slice as5(din, clk, reset, load[5], dout);
    array_slice as6(din, clk, reset, load[6], dout);
    array_slice as7(din, clk, reset, load[7], dout);
endmodule

module queue (input wire [2:0] din, input wire clk, reset, wr_signal, rd_signal, output wire [2:0] dout, output wire empty, full);
    wire [7:0] load;
    wire [2:0] wr_addr;
    wire inc, cout;

    ptr_reg wr_reg(clk, reset, wr_signal, wr_addr, cout)

    demux8 dm0(wr_signal, wr_addr[0], wr_addr[1], wr_addr[2], load);
    register_file rf(din, clk, reset, load, dout);
endmodule