import obd, schedule
import time
import pyrebase
import json

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

    Reset_DTC_Value  = db.child("RESET_DTC").child(username).get().val()
    print("REST DTC ==> "+ Reset_DTC_Value)
    if Reset_DTC_Value=='RESET':
        connection.query(obd.commands.CLEAR_DTC, force=True)
        Reset_DTC_Value = 'DONE'
        db.child("RESET_DTC").child(username).set(Reset_DTC_Value)
        print("REST DTC ==> " + Reset_DTC_Value)

    global i

    if i==46:
        i=0
    if i == 0:
        result = str(connection.query(obd.commands.ENGINE_LOAD, force=True).value)
        print("ENGINE_LOAD ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_ENGINE_LOAD").set(result)
            list = []
            list = json.loads(db.child("HISTORY").child(username).child("H_ENGINE_LOAD").get().val())
            list.append(result)
            db.child("HISTORY").child(username).child("H_ENGINE_LOAD").set(json.dumps(list))
    elif i==1:
        result = str(connection.query(obd.commands.RPM, force=True).value)
        print("RPM ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_RPM").set(result)
            list = []
            list = json.loads(db.child("HISTORY").child(username).child("H_RPM").get().val())
            list.append(result)
            db.child("HISTORY").child(username).child("H_RPM").set(json.dumps(list))
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
            list = []
            list = json.loads(db.child("HISTORY").child(username).child("H_THROTTLE_POSITION").get().val())
            list.append(result)
            db.child("HISTORY").child(username).child("H_THROTTLE_POSITION").set(json.dumps(list))
    elif i==4:
        result = str(connection.query(obd.commands.COOLANT_TEMP, force=True).value)
        print("COOLANT_TEMP ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_COOLANT_TEMP").set(result)
            list = []
            list = json.loads(db.child("HISTORY").child(username).child("H_COOLANT_TEMPERATURE").get().val())
            list.append(result)
            db.child("HISTORY").child(username).child("H_COOLANT_TEMPERATURE").set(json.dumps(list))
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
            list = []
            list = json.loads(db.child("HISTORY").child(username).child("H_ENGINE_LOAD").get().val())
            list.append(result)
            db.child("HISTORY").child(username).child("H_ENGINE_LOAD").set(json.dumps(list))
    elif i==7:
        result = str(connection.query(obd.commands.RPM, force=True).value)
        print("RPM ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_RPM").set(result)
            list = []
            list = json.loads(db.child("HISTORY").child(username).child("H_RPM").get().val())
            list.append(result)
            db.child("HISTORY").child(username).child("H_RPM").set(json.dumps(list))
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
            list = []
            list = json.loads(db.child("HISTORY").child(username).child("H_THROTTLE_POSITION").get().val())
            list.append(result)
            db.child("HISTORY").child(username).child("H_THROTTLE_POSITION").set(json.dumps(list))
    elif i==10:
        result = str(connection.query(obd.commands.INTAKE_PRESSURE, force=True).value)
        print("INTAKE_PRESSURE ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_INTAKE_PRESSURE").set(result)
            list = []
            list = json.loads(db.child("HISTORY").child(username).child("H_INTAKE_PRESSURE").get().val())
            list.append(result)
            db.child("HISTORY").child(username).child("H_INTAKE_PRESSURE").set(json.dumps(list))
    elif i==11:
        result = str(connection.query(obd.commands.ENGINE_LOAD, force=True).value)
        print("ENGINE_LOAD ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_ENGINE_LOAD").set(result)
            list = []
            list = json.loads(db.child("HISTORY").child(username).child("H_ENGINE_LOAD").get().val())
            list.append(result)
            db.child("HISTORY").child(username).child("H_ENGINE_LOAD").set(json.dumps(list))
    elif i==12:
        result = str(connection.query(obd.commands.RPM, force=True).value)
        print("RPM ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_RPM").set(result)
            list = []
            list = json.loads(db.child("HISTORY").child(username).child("H_RPM").get().val())
            list.append(result)
            db.child("HISTORY").child(username).child("H_RPM").set(json.dumps(list))
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
            list = []
            list = json.loads(db.child("HISTORY").child(username).child("H_THROTTLE_POSITION").get().val())
            list.append(result)
            db.child("HISTORY").child(username).child("H_THROTTLE_POSITION").set(json.dumps(list))
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
            list = []
            list = json.loads(db.child("HISTORY").child(username).child("H_ENGINE_LOAD").get().val())
            list.append(result)
            db.child("HISTORY").child(username).child("H_ENGINE_LOAD").set(json.dumps(list))
    elif i==17:
        result = str(connection.query(obd.commands.RPM, force=True).value)
        print("RPM ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_RPM").set(result)
            list = []
            list = json.loads(db.child("HISTORY").child(username).child("H_RPM").get().val())
            list.append(result)
            db.child("HISTORY").child(username).child("H_RPM").set(json.dumps(list))
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
            list = []
            list = json.loads(db.child("HISTORY").child(username).child("H_THROTTLE_POSITION").get().val())
            list.append(result)
            db.child("HISTORY").child(username).child("H_THROTTLE_POSITION").set(json.dumps(list))
    elif i==20:
        result = str(connection.query(obd.commands.INTAKE_TEMP, force=True).value)
        print("INTAKE_TEMP ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_INTAKE_TEMP").set(result)
            list = []
            list = json.loads(db.child("HISTORY").child(username).child("H_INTAKE_PRESSURE").get().val())
            list.append(result)
            db.child("HISTORY").child(username).child("H_INTAKE_PRESSURE").set(json.dumps(list))
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
            list = []
            list = json.loads(db.child("HISTORY").child(username).child("H_ENGINE_LOAD").get().val())
            list.append(result)
            db.child("HISTORY").child(username).child("H_ENGINE_LOAD").set(json.dumps(list))
    elif i==23:
        result = str(connection.query(obd.commands.RPM, force=True).value)
        print("RPM ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_RPM").set(result)
            list = []
            list = json.loads(db.child("HISTORY").child(username).child("H_RPM").get().val())
            list.append(result)
            db.child("HISTORY").child(username).child("H_RPM").set(json.dumps(list))
    elif i==24:
        result = str(connection.query(obd.commands.SPEED, force=True).value)
        print("SPEED ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_SPEED").set(result)
            list = []
            list = json.loads(db.child("HISTORY").child(username).child("H_SPEED").get().val())
            list.append(result)
            db.child("HISTORY").child(username).child("H_SPEED").set(json.dumps(list))
    elif i==25:
        result = str(connection.query(obd.commands.THROTTLE_POS, force=True).value)
        print("THROTTLE_POS ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_THROTTLE_POS").set(result)
            list = []
            list = json.loads(db.child("HISTORY").child(username).child("H_THROTTLE_POSITION").get().val())
            list.append(result)
            db.child("HISTORY").child(username).child("H_THROTTLE_POSITION").set(json.dumps(list))
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
            list = []
            list = json.loads(db.child("HISTORY").child(username).child("H_ENGINE_LOAD").get().val())
            list.append(result)
            db.child("HISTORY").child(username).child("H_ENGINE_LOAD").set(json.dumps(list))
    elif i==30:
        result =  str(connection.query(obd.commands.RPM, force=True).value)
        print("RPM ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_RPM").set(result)
            list = []
            list = json.loads(db.child("HISTORY").child(username).child("H_RPM").get().val())
            list.append(result)
            db.child("HISTORY").child(username).child("H_RPM").set(json.dumps(list))
    elif i==31:
        result = str(connection.query(obd.commands.SPEED, force=True).value)
        print("SPEED ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_SPEED").set(result)
            list = []
            list = json.loads(db.child("HISTORY").child(username).child("H_SPEED").get().val())
            list.append(result)
            db.child("HISTORY").child(username).child("H_SPEED").set(json.dumps(list))
    elif i == 32:
        result = str(connection.query(obd.commands.THROTTLE_POS, force=True).value)
        print("THROTTLE_POS ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_THROTTLE_POS").set(result)
            list = []
            list = json.loads(db.child("HISTORY").child(username).child("H_THROTTLE_POSITION").get().val())
            list.append(result)
            db.child("HISTORY").child(username).child("H_THROTTLE_POSITION").set(json.dumps(list))
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
            list = []
            list = json.loads(db.child("HISTORY").child(username).child("H_ENGINE_LOAD").get().val())
            list.append(result)
            db.child("HISTORY").child(username).child("H_ENGINE_LOAD").set(json.dumps(list))
    elif i==36:
        result = str(connection.query(obd.commands.RPM, force=True).value)
        print("RPM ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_RPM").set(result)
            list = []
            list = json.loads(db.child("HISTORY").child(username).child("H_RPM").get().val())
            list.append(result)
            db.child("HISTORY").child(username).child("H_RPM").set(json.dumps(list))
    elif i==37:
        result = str(connection.query(obd.commands.SPEED, force=True).value)
        print("SPEED ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_SPEED").set(result)
            list = []
            list = json.loads(db.child("HISTORY").child(username).child("H_SPEED").get().val())
            list.append(result)
            db.child("HISTORY").child(username).child("H_SPEED").set(json.dumps(list))
    elif i == 38:
        result = str(connection.query(obd.commands.THROTTLE_POS, force=True).value)
        print("THROTTLE_POS ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_THROTTLE_POS").set(result)
            list = []
            list = json.loads(db.child("HISTORY").child(username).child("H_THROTTLE_POSITION").get().val())
            list.append(result)
            db.child("HISTORY").child(username).child("H_THROTTLE_POSITION").set(json.dumps(list))
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
            list = []
            list = json.loads(db.child("HISTORY").child(username).child("H_ENGINE_LOAD").get().val())
            list.append(result)
            db.child("HISTORY").child(username).child("H_ENGINE_LOAD").set(json.dumps(list))
    elif i==42:
        result = str(connection.query(obd.commands.RPM, force=True).value)
        print("RPM ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_RPM").set(result)
            list = []
            list = json.loads(db.child("HISTORY").child(username).child("H_RPM").get().val())
            list.append(result)
            db.child("HISTORY").child(username).child("H_RPM").set(json.dumps(list))
    elif i==43:
        result = str(connection.query(obd.commands.SPEED, force=True).value)
        print("SPEED ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_SPEED").set(result)
            list = []
            list = json.loads(db.child("HISTORY").child(username).child("H_SPEED").get().val())
            list.append(result)
            db.child("HISTORY").child(username).child("H_SPEED").set(json.dumps(list))
    elif i == 44:
        result = str(connection.query(obd.commands.THROTTLE_POS, force=True).value)
        print("THROTTLE_POS ==> " + result)
        if(result!='None'):
            db.child("L_READINGS").child(username).child("L_THROTTLE_POS").set(result)
            list = []
            list = json.loads(db.child("HISTORY").child(username).child("H_THROTTLE_POSITION").get().val())
            list.append(result)
            db.child("HISTORY").child(username).child("H_THROTTLE_POSITION").set(json.dumps(list))
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

