#!/usr/bin/env node
// From Blinks various LEDs
const Blynk = require('/usr/lib/node_modules/blynk-library');
const b = require('bonescript');
const util = require('util');

const LED0 = 'USR3';
const LED1 = 'P9_14';
const button = 'P9_16';
b.pinMode(LED0, b.OUTPUT);
b.pinMode(LED1, b.OUTPUT);
b.pinMode(button, b.INPUT);

const AUTH = '7d8ebdeb68404d7e8d3fcfafddc822c5';

var blynk = new Blynk.Blynk(AUTH);

var v0 = new blynk.VirtualPin(0);
var v4 = new blynk.VirtualPin(4);
var v10 = new blynk.WidgetLED(10);


// console.log(util.inspect(v1));
// var v9 = new blynk.VirtualPin(9);

v0.on('write', function(param) {
    console.log('V0:', param[0]);
    b.digitalWrite(LED0, param[0]);
});
v4.on('write', function(param) {
    console.log('V4:', param[0]);   
    b.analogWrite(LED1,param/4096);
});
v10.setValue(0);    // Initiallly off

// v9.on('read', function() {
//     v9.write(new Date().getSeconds());
// });

b.attachInterrupt(button, toggle, b.CHANGE);

function toggle(x) {
    console.log("V1: ", x.value);
    x.value ? v10.turnOff() : v10.turnOn();
}
