1.start/stop NIC:
	sudo systemctl start/status/stop nfp-sdk6-rte

2.After starting NIC, a RTE(RunTimeEnvironment) RPC Port(20206) is opened up.

3.Compile P4 to Firmware(If you don't know p4, don't touch this, jump to step4):
	cd /home/ovs1/xiaochen/workspace/ovs/
	sudo /home/ovs1/xiaochen/nfp-sdk-6.0.2/p4/bin/nfp4build -p out/ -d flowcache -o ovs.nffw -l hydrogen -4 ovs.p4

4.Load Firmware to NIC:
	cd /home/ovs1/xiaochen/workspace/ovs/
	sudo /home/ovs1/xiaochen/nfp-sdk-6.0.2/p4/bin/rtecli design-load -f ovs.nffw -p out/pif_design.json

5.Restart 4 Virtual Interfaces:
	sudo /home/ovs1/xiaochen/workspace/VFs_restart.sh

6.Load Static Rules to NIC(Don't edit user_config.json, copy it and modify the copy):
	sudo /home/ovs1/xiaochen/nfp-sdk-6.0.2/p4/bin/rtecli config-reload -c user_config.json

6.2 Check Loaded Rules:
	See sudo /home/ovs1/xiaochen/nfp-sdk-6.0.2/p4/bin/rtecli help for details

7.Run digest(up_call) listener:
	sudo python /home/ovs1/xiaochen/nfp-sdk-6-rte-v6.0.2.0-Ubuntu-Release-r2013-2017-04-14-ubuntu.binary/thrift/client/digest_listener.py

8.Run Packet receiver program on Output Port(enp4s8f1):
	cd /home/ovs1/xiaochen/workspace/ovs/
	sudo python ./receive_1.py

9.Send single test packet(Observe digest_listener & Output Port):
	sudo python ./send_one.py

10. Shut down digest listener and Receiver
	Rerun Step 6 with user_config_new.json
	Repeat Step 7 8 9

11. Unload Firmware from NIC:
	sudo /home/ovs1/xiaochen/nfp-sdk-6.0.2/p4/bin/rtecli design-unload

12. Shut down NIC:
	sudo systemctl stop nfp-sdk6-rte

Note:
For thrift(RPC), please check /home/ovs1/xiaochen/nfp-sdk-6-rte-v6.0.2.0-Ubuntu-Release-r2013-2017-04-14-ubuntu.binary/thrift/
please refer to RunTimeEnvironment.py RTEInterface.py and sdk6_rte_cli.py
For cpp API, please refer to /home/ovs1/xiaochen/nfp-sdk-6-rte-v6.0.2.0-Ubuntu-Release-r2013-2017-04-14-ubuntu.binary/thrift/gen-cpp/
