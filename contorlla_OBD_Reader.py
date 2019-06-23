import obd, schedule
import time
import pyrebase

username = 'Omar Ashour'

firebase_config = {
  "apiKey": "AIzaSyD-oSt1XNChK84u30Bh10waKVR6kGLVdTQ",
  "authDomain": "controlla-e27e8.firebaseapp.com",
  "databaseURL": "https://controlla-e27e8.firebaseio.com/",
  "storageBucket": "gs://controlla-e27e8.appspot.com"
}

firebase = pyrebase.initialize_app(firebase_config)


db = firebase.database()


connection = obd.OBD() # auto-connects to USB or RF port

i = 0


def readOBD():
    global i

    if i==46:
        i=0
    if i == 0:
        result = str(connection.query(obd.commands.ENGINE_LOAD, force=True).value)
        print("ENGINE_LOAD ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_ENGINE_LOAD").set(result)
    elif i==1:
        result = str(connection.query(obd.commands.RPM, force=True).value)
        print("RPM ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_RPM").set(result)
    elif i==2:
        result = str(connection.query(obd.commands.SPEED, force=True).value)
        print("SPEED ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_SPEED").set(result)
    elif i == 3:
        result = str(connection.query(obd.commands.THROTTLE_POS, force=True).value)
        print("THROTTLE_POS ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_THROTTLE_POS").set(result)
    elif i==4:
        result = str(connection.query(obd.commands.COOLANT_TEMP, force=True).value)
        print("COOLANT_TEMP ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_COOLANT_TEMP").set(result)
    elif i==5:
        result = str(connection.query(obd.commands.FUEL_PRESSURE, force=True).value)
        print("FUEL_PRESSURE ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_FUEL_PRESSURE").set(result)
    elif i==6:
        result = str(connection.query(obd.commands.ENGINE_LOAD, force=True).value)
        print("ENGINE_LOAD ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_ENGINE_LOAD").set(result)
    elif i==7:
        result = str(connection.query(obd.commands.RPM, force=True).value)
        print("RPM ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_RPM").set(result)
    elif i==8:
        result = str(connection.query(obd.commands.SPEED, force=True).value)
        print("SPEED ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_SPEED").set(result)
    elif i == 9:
        result = str(connection.query(obd.commands.THROTTLE_POS, force=True).value)
        print("THROTTLE_POS ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_THROTTLE_POS").set(result)
    elif i==10:
        result = str(connection.query(obd.commands.INTAKE_PRESSURE, force=True).value)
        print("INTAKE_PRESSURE ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_INTAKE_PRESSURE").set(result)
    elif i==11:
        result = str(connection.query(obd.commands.ENGINE_LOAD, force=True).value)
        print("ENGINE_LOAD ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_ENGINE_LOAD").set(result)
    elif i==12:
        result = str(connection.query(obd.commands.RPM, force=True).value)
        print("RPM ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_RPM").set(result)
    elif i==13:
        result = str(connection.query(obd.commands.SPEED, force=True).value)
        print("SPEED ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_SPEED").set(result)
    elif i == 14:
        result = str(connection.query(obd.commands.THROTTLE_POS, force=True).value)
        print("THROTTLE_POS ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_THROTTLE_POS").set(result)
    elif i==15:
        result = str(connection.query(obd.commands.TIMING_ADVANCE, force=True).value)
        print("TIMING_ADVANCE ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_TIMING_ADVANCE").set(result)
    elif i==16:
        result = str(connection.query(obd.commands.ENGINE_LOAD, force=True).value)
        print("ENGINE_LOAD ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_ENGINE_LOAD").set(result)
    elif i==17:
        result = str(connection.query(obd.commands.RPM, force=True).value)
        print("RPM ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_RPM").set(result)
    elif i==18:
        result = str(connection.query(obd.commands.SPEED, force=True).value)
        print("SPEED ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_SPEED").set(result)
    elif i == 19:
        result = str(connection.query(obd.commands.THROTTLE_POS, force=True).value)
        print("THROTTLE_POS ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_THROTTLE_POS").set(result)
    elif i==20:
        result = str(connection.query(obd.commands.INTAKE_TEMP, force=True).value)
        print("INTAKE_TEMP ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_INTAKE_TEMP").set(result)
    elif i==21:
        result = str(connection.query(obd.commands.MAF, force=True).value)
        print("MAF ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_MAF").set(result)
    elif i==22:
        result = str(connection.query(obd.commands.ENGINE_LOAD, force=True).value)
        print("ENGINE_LOAD ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_ENGINE_LOAD").set(result)
    elif i==23:
        result = str(connection.query(obd.commands.RPM, force=True).value)
        print("RPM ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_RPM").set(result)
    elif i==24:
        result = str(connection.query(obd.commands.SPEED, force=True).value)
        print("SPEED ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_SPEED").set(result)
    elif i==25:
        result = str(connection.query(obd.commands.THROTTLE_POS, force=True).value)
        print("THROTTLE_POS ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_THROTTLE_POS").set(result)
    elif i==26:
        result = str(connection.query(obd.commands.FUEL_LEVEL, force=True).value)
        print("FUEL_LEVEL ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_FUEL_LEVEL").set(result)
    elif i==29:
        result = str(connection.query(obd.commands.ENGINE_LOAD, force=True).value)
        print("ENGINE_LOAD ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_ENGINE_LOAD").set(result)
    elif i==30:
        result =  str(connection.query(obd.commands.RPM, force=True).value)
        print("RPM ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_RPM").set(result)
    elif i==31:
        result = str(connection.query(obd.commands.SPEED, force=True).value)
        print("SPEED ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_SPEED").set(result)
    elif i == 32:
        result = str(connection.query(obd.commands.THROTTLE_POS, force=True).value)
        print("THROTTLE_POS ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_THROTTLE_POS").set(result)
    elif i==33:
        result = str(connection.query(obd.commands.FUEL_TYPE, force=True).value)
        print("FUEL_TYPE ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_FUEL_TYPE").set(result)
    elif i==34:
        result = str(connection.query(obd.commands.OIL_TEMP, force=True).value)
        print("OIL_TEMP ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_OIL_TEMP").set(result)
    elif i==35:
        result = str(connection.query(obd.commands.ENGINE_LOAD, force=True).value)
        print("ENGINE_LOAD ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_ENGINE_LOAD").set(result)
    elif i==36:
        result = str(connection.query(obd.commands.RPM, force=True).value)
        print("RPM ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_RPM").set(result)
    elif i==37:
        result = str(connection.query(obd.commands.SPEED, force=True).value)
        print("SPEED ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_SPEED").set(result)
    elif i == 38:
        result = str(connection.query(obd.commands.THROTTLE_POS, force=True).value)
        print("THROTTLE_POS ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_THROTTLE_POS").set(result)
    elif i==39:
        result = str(connection.query(obd.commands.FUEL_INJECT_TIMING, force=True).value)
        print("FUEL_INJECT_TIMING ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_FUEL_INJECT_TIMING").set(result)
    elif i==40:
        result = str(connection.query(obd.commands.FUEL_RATE, force=True).value)
        print("FUEL_RATE ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_FUEL_RATE").set(result)
    elif i==41:
        result = str(connection.query(obd.commands.ENGINE_LOAD, force=True).value)
        print("ENGINE_LOAD ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_ENGINE_LOAD").set(result)
    elif i==42:
        result = str(connection.query(obd.commands.RPM, force=True).value)
        print("RPM ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_RPM").set(result)
    elif i==43:
        result = str(connection.query(obd.commands.SPEED, force=True).value)
        print("SPEED ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_SPEED").set(result)
    elif i == 44:
        result = str(connection.query(obd.commands.THROTTLE_POS, force=True).value)
        print("THROTTLE_POS ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_THROTTLE_POS").set(result)
    elif i == 45:
        resultDTC = []
        resultDTC.append(connection.query(obd.commands.GET_DTC, force=True).value)
        DTC_str = []
        DTC_str.append(('1','1'))
        print("DTC ==> " + str(resultDTC))
        if (len(resultDTC)>1):
            DTC_str.clear()
            for x in resultDTC:
                DTC_str.append(x)
            db.child("L_DTCS").child(username).set(DTC_str)
        else:
            db.child("L_DTCS").child(username).set(['NA','NA'])

    i+=1

schedule.every(0.1).seconds.do(readOBD)

while True:
    schedule.run_pending()

