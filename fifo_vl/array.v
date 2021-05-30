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