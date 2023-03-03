module full_adder (a, b, cin, sum, cout );
input bit a ;
input bit b ;
input bit cin ;
output bit sum ;
output bit cout ;

  assign sum = a ^ b ^ cin;
  assign cout = a & b | b & cin | a & cin;

endmodule
