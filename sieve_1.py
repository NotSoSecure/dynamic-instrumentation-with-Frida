import frida, sys

def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)

jscode = """
Java.perform(function () {
    //Obtain referrence of the Activity currently running
    var MainActivity = Java.use('com.mwr.example.sieve.MainLoginActivity');
	//Obtain reference of the function whcih needs to be called
    MainActivity.checkKeyResult.implementation = function (b) {
        send('checkKeyResult');
	//Calling the function and passing the boolean parameter as true
        this.checkKeyResult(true);
		
        console.log('Done:');
    };
});
"""

process = frida.get_usb_device().attach('com.mwr.example.sieve')
script = process.create_script(jscode)
script.on('message', on_message)
script.load()
sys.stdin.read()
