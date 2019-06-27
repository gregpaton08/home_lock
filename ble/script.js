var bleno = require('bleno');
var exec = require('child_process').exec;
var execSync = require('child_process').execSync;

const descriptorUuid = '2901';
const characteristicUuid = 'fff1';
const primaryServiceUuid = 'fffffffffffffffffffffffffffffff0';
const serviceUuid = 'fffffffffffffffffffffffffffffff0';

var Descriptor = bleno.Descriptor;
var descriptor = new Descriptor({
    uuid: descriptorUuid,
    value: 'Get or set the lock status'
});

var Characteristic = bleno.Characteristic;
var characteristic = new Characteristic({
    uuid: characteristicUuid,
    properties: [ 'read', 'write', 'writeWithoutResponse' ],
    // secure: [ 'write', 'writeWithoutResponse' ],
    // secure: [ 'read', 'write', 'writeWithoutResponse' ],
    descriptors: [ descriptor ],

    onReadRequest: function(offset, callback) {
        console.log('onReadRequest', offset);

        // TODO: replace with hardware check once connected to lock.
        var retVal = execSync('./lockStatus.sh');

        callback(Characteristic.RESULT_SUCCESS, Buffer(retVal == 1 ? 'FF' : '00', 'hex'));
    },

    onWriteRequest: function(newData, offset, withoutResponse, callback) {
        console.log('onWriteRequest', newData, offset, withoutResponse)
        console.log('got newData: ' + newData.readInt8(0));

        var status = newData.readInt8(0);
        if (status === -1) {
            // TODO: replace with direct call to hardware once connected to lock.
            console.log('locking...')
            exec('./lock.sh', function(error, stdout, stderr) {
            });
        } else if (status === 0) {
            // TODO: replace with direct call to hardware once connected to lock.
            console.log('unlocking')
            exec('./unlock.sh', function(error, stdout, stderr) {
            });
        } else {
            console.log('invalid command', status)
            callback(bleno.Characteristic.RESULT_INVALID_OFFSET);
        }

        callback(bleno.Characteristic.RESULT_SUCCESS);
    }
});

var PrimaryService = bleno.PrimaryService;
var primaryService = new PrimaryService({
    uuid: primaryServiceUuid,
    characteristics: [ characteristic ]
});

var services = [ primaryService ];
bleno.on('advertisingStart', function(error) {
    bleno.setServices(services);
});

bleno.on('stateChange', function(state) {
    console.log('BLE stateChanged to: ' + state);
    if (state === 'poweredOn') {
        bleno.startAdvertising('home_lock', [ serviceUuid ]);
    } else {
        bleno.stopAdvertising();
    }
});

bleno.on('accept', function(clientAddress) {
    console.log('accept ' + clientAddress);
});

bleno.on('platform', function(platform) {
    console.log('onPlatform', platform)
})
