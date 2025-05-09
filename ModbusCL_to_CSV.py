from pathlib import Path
from datetime import date, timedelta, datetime
from pyModbusTCP.client import ModbusClient
from time import sleep
import shelve

def chooseName():
    return 'Modbus_example_'+str(date.today())+'_01.csv'

def saveLoop(filePath):
    print("Start server...")
    total = 400
    for i in range(total):
        regs = c.read_holding_registers(17428, 6)
        # if success display registers
        if regs:
            #print(f'reg ad #0 to 1: {regs[0]}')
            
            dtNow = datetime.now()
            fecha = dtNow.strftime('%d/%m/%Y')
            hora = dtNow.strftime('%H:%M:%S.%f')[:-3]            

            with open(filePath, 'a') as archivo:
                archivo.write(f'{fecha},{hora},{regs[0]},{regs[1]},' +
                              f'{regs[2]},{regs[3]},{regs[4]},{regs[5]}\n')
        else:
            print('unable to read registers')

        # sleep 1s before next polling
        print(f"guardando...{i+1}/{total}")
        sleep(0.25)

    

FolderPath = Path('D:/COMPANY_NAME/Datalog')

c = ModbusClient(host='192.168.1.92', port=502)

if __name__ == '__main__':
    todayPath = FolderPath/chooseName()

    print(f'folder: {todayPath.name}')

    with shelve.open(str(FolderPath/'filePath')) as shelfFile:
        #shelfFile['folderPath'] = FolderPath
        shelfFile['currentFile'] = todayPath
    
    if not todayPath.exists():
        with open(todayPath, 'w') as archivo:
            archivo.write('Fecha,Hora,PosAxis1,PosStage2Axis1,PosStage2Axis2,' + 
                          'TorqueAxis1,TorqueStage2Axis1,TorqueStage2Axis2\n')

    saveLoop(todayPath)

