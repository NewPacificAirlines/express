class Webusb {
  isSupported() {
    return 'usb' in navigator;
  }

  async getDevices() {
    return await navigator.usb.getDevices();
  }
  
  async requestDevice() {
    try {
      await navigator.usb.requestDevice({ filters: [] });
    } catch (e) {
      console.error(e);
    }
  }

  async forget(device) {
    await device.forget();
  }
  
  async tsplTestPrint(device) {
    const cmds = [
      
      // my only change //
      
      'BTT1235[A 508250=#01B1 A002220624=38#02C0 1012010202=38#04B1 A017220624=38#05C0 1027010202=38#07B1 A035220624=38#08C0 1045010202=38#20C0M1090050505#21C0MK102470201#22C0M1100050807#23S0M1106010349#25C0M1110050505#26C0MK123470201#27C0M1120050807#28S0M1127010349#29C0MA130200505#32C0MA140201812#34C0MK150470201=82#36C0MA160240303#37S0M1164010349#38B1MA165254032#40B1MC228454032=38#60C0 5474490202=38#62C1 5477480101=84#63C1 5477230101=85#65C0 5480480201=86#66C0 5480230201=87#70C0 5483490202#82C1 5505480101#83C1 5505260101#84C1 5510480101#85C1 5510230101#86C0 5515480201#87C0 5515260201#88C0 5520490202=70#89B1 5530480722=38#90C0 5535480202=38#',
      'BTP123501#01615972#207H 143#21DEP 2000#22ANC#25DL 517#26DEP 2214#27MSP#29DL 5252#32DSM#367H 61-59-72#389808615972#70NEW PACIFIC#82DES MOINES#83MN#84PEDRETTY/#85GARY MR#86NNIXPI#8728JUL23',
      
      // my only change //  
      
      // 'SIZE 48 mm,25 mm',
      // 'CLS',
      // 'TEXT 30,10,"4",0,1,1,"HackerNoon"',
      // 'TEXT 30,50,"2",0,1,1,"WebUSB API"',
      // 'BARCODE 30,80,"128",70,1,0,2,2,"altospos.com"',
      // 'PRINT 1',
      // 'END',
    ];
    

    await device.open();
    await device.selectConfiguration(1);
    await device.claimInterface(0);
    await device.transferOut(
      device.configuration.interfaces[0].alternate.endpoints.find(obj => obj.direction === 'out').endpointNumber,
      new Uint8Array(
        new TextEncoder().encode(cmds.join('\r\n'))
      ),
    );
    await device.close();
  }
}
