from tkinter import E
import matplotlib as plt
import pandas as pd
import csv

fcsv = open('rozladowanie.csv', 'w')
writer = csv.writer(fcsv)
headers = ["mission_time", "value_1", "pressure", "temp_1", "value_2", "temp_2", "value_3", "time_NS", "time_WE", "MARG_AHRS_U_a_x", "MARG_AHRS_U_a_y", "MARG_AHRS_U_a_z", "MARG_AHRS_U_P", "MARG_AHRS_U_Q", "MARG_AHRS_U_R", "MARG_AHRS_U_Hx", "MARG_AHRS_U_Hy", "MARG_AHRS_U_Hz", "dio_label", "geig_label", "i_use", "bat_v", "i_int", "bat_proc", "gps_longitude", "gps_latitude", "gps_altitude", "gps_speed_kph", "gps_track", "gps_h", "gps_m", "gps_s", "sat_num"]
writer.writerow(headers)
with open('pelne_rozladowanie_300mA.txt', mode= 'r', encoding='latin-1', newline='\r\n', closefd=True) as f:
        lines = f.readlines()
        try:
            for line in lines:
                splitted = line.split('ADC')
                tim, rest = splitted[0], splitted[1]
                tim = tim[4:]
                splitted = rest.split('WSU')
                adc,rest = splitted[0], splitted[1]
                adc = adc[1:]
                splitted = rest.split('RAD')
                wsu,rest = splitted[0], splitted[1]
                wsu = wsu[1:]
                splitted = rest.split('POW')
                rad,rest = splitted[0], splitted[1]
                rad = rad[1:]
                splitted = rest.split('GPS')
                pow,gps = splitted[0], splitted[1]
                pow=pow[1:]
                gps=gps[1:]
                mission_time=tim.split('$',1)
                mission_time= float(mission_time[0])
                adc=adc.split('$',6)
                for n in range(len(adc)-1):
                    adc[n]=float(adc[n])
                adc.pop()
                value_1, pressure, temp_1, value_2, temp_2, value_3 = adc
                wsu = wsu.split('$',11)
                wsu.pop()
                for n in range(len(wsu)):
                    wsu[n] = float(wsu[n])

                rad = rad.split('$', 2)
                rad.pop()

                for n in range(len(rad)):
                    rad[n] = float(rad[n])

                time_NS, time_WE, marg_ahrs_U_a_x, marg_ahrs_U_a_y, marg_ahrs_U_a_z, marg_ahrs_U_P, marg_ahrs_U_Q, marg_ahrs_U_R, marg_ahrs_U_Hx, marg_ahrs_U_Hy, marg_ahrs_U_Hz = wsu
                dio_label, gio_label = rad
                
                pow = pow.split('$', 2)
                pow.pop()
                for n in range(len(pow)):
                    pow[n] = float(pow[n])
                i_use, bat_v = pow
                gps = gps.split('$', 6)
                time = gps[5]
                sat_num = gps[6]
                gps = gps[:5]
                for n in range(len(gps)):
                    gps[n] = float(gps[n])
                sat_num = sat_num.split('\r')
                sat_num = sat_num[0]
                gps_longitude, gps_latitude, gps_altitude, gps_speed_kph, gps_track = gps 
                time=time.split(':')
                gps_h, gps_m, gps_s = time
                data = [mission_time, value_1, pressure, temp_1, value_2, temp_2, value_3, time_NS, time_WE, marg_ahrs_U_a_x, marg_ahrs_U_a_y, marg_ahrs_U_a_z, marg_ahrs_U_P, marg_ahrs_U_Q, marg_ahrs_U_R, marg_ahrs_U_Hx, marg_ahrs_U_Hy, marg_ahrs_U_Hz, dio_label, gio_label, i_use, bat_v, gps_longitude, gps_latitude, gps_altitude, gps_speed_kph, gps_track, gps_h, gps_m, gps_s, sat_num]
                writer.writerow(data)
                
                
                
        except Exception as ex:
            print(ex)
            print(line)

        fcsv.close()