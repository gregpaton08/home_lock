var bleno = require('bleno');
var exec = require('child_process').exec;

var Descriptor = bleno.Descriptor;
var descriptor = new Descriptor({
    uuid: '2901',
    value: 'value' // static value, must be of type Buffer or string if set
});

var Characteristic = bleno.Characteristic;
var characteristic = new Characteristic({
    uuid: 'fff1',
    properties: [ 'read', 'write', 'writeWithoutResponse' ],
    descriptors: [ descriptor ],

    onWriteRequest: function(newData, offset, withoutResponse, callback) {
        console.log('got newData: ' + newData.toString('utf8'));
        exec('./toggleLock.sh', function(error, stdout, stderr) {
        });
        callback(bleno.Characteristic.RESULT_SUCCESS);
    }
});
var PrimaryService = bleno.PrimaryService;
var primaryService = new PrimaryService({
    uuid: 'fffffffffffffffffffffffffffffff0',
    characteristics: [ characteristic ]
});
var services = [ primaryService ];
bleno.on('advertisingStart', function(error) {
    bleno.setServices( services );
});
bleno.on('stateChange', function(state) {
    console.log('BLE stateChanged to: ' + state);
    if (state === 'poweredOn') {
        bleno.startAdvertising('MyDevice',['fffffffffffffffffffffffffffffff0']);
    } else {
        bleno.stopAdvertising();
    }
});
