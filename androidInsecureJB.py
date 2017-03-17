import frida, sys

def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)

jscode = """
Java.perform(function () {
    var MainActivity = Java.use('com.android.insecurebankv2.PostLogin');
    MainActivity.doesSUexist.implementation = function () {
        console.log('Done: doesSUexist');
		return false;
    };
	
	MainActivity.doesSuperuserApkExist.implementation = function (b) {
        console.log('Done: doesSuperuserApkExist');
		return false;
    };
});
"""

process = frida.get_usb_device().attach('com.android.insecurebankv2')
script = process.create_script(jscode)
script.on('message', on_message)
script.load()
sys.stdin.read()
