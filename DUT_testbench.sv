`timescale 1ns / 1ps
module testbench;
 
 logic a; 
 logic b;
  logic y;
adder dut (    .a(a),    .b(b),    .y(y_out)  );
  reg a;
  reg b;
  wire y_out;
  initial begin
a=1;
b=2;
#1; 
a=0;
b=0;
#1; 
a=1;
b=7;
#1; 
a=3;
b=2;
#1; 
  end
endmodule
