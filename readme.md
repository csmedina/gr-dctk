To build follow the instruction:
	
	mkdir build
	cd build

If you have CodeBlocks
	
	cmake .. -G "CodeBlocks - Unix Makefiles"

if dont
	
	cmake ..

Finish with

	make
	sudo make install

To use the GRC, first open the GRC and load the flow graph examples/generic_rx_path.grc, then generate the python code (Press Generatte button).
Close GRC and open again.

Try testing the flow examples/bpsk_tx_rx.grc

Good luck!!!

