#include "includes/headers.p4"
#include "includes/parser.p4"
#include "includes/actions.p4"

table ports {
		reads {
				ipv4.protocol: exact;
		}
		actions {
				set_tcp_ports;
				set_udp_ports;
		}
}

table load_meta {
		reads {
			ethernet.etherType : exact;	
		}
		actions {
				load_up;
		}
}

//table pre {
//		reads {
//				ethernet.etherType : exact;
//		}
//		actions {
//				up_call;
//		}
//}

table table1 {
		reads {
				Ftuple.tuples: ternary;
		}
		actions {
				up_call;
				_nop;
		}
}

table table2 {
		reads {
				Ftuple.tuples : ternary;
		}
		actions {
				send_out;
				_drop;
		}
}

control ingress {
		apply(ports);
		apply(load_meta);
//		apply(pre);
		apply(table1);
		apply(table2);
}

control egress {
}

