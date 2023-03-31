import os

def change_variable_octave(variable,temp_input):
    var = ''
    with open('forward_model/fwdCompute.m', 'r') as f:
        for line in f:
            if variable in line:
                print(line)
                var = line
            else:
                pass

    temp_input = input("value: ")
    with open('forward_model/fwdCompute.m', 'r') as f:
        code = f.read()

    code = code.replace(var, variable + ' {}; \n'.format(temp_input))

    with open('forward_model/fwdCompute.m', 'w') as f:
        f.write(code)

#change_variable_octave('            sensorInfo.position = ')
#change_variable_octave('        senRes     =')
#change_variable_octave('        gridRes    =')
#change_variable_octave('        gridSenRes =')
#change_variable_octave('        tempC =')
#change_variable_octave('            pr.density =')

#change_variable_octave('            ps.refPoint =')
#change_variable_octave('            ps.pos  =')
#change_variable_octave('            ps.azim =')
#change_variable_octave('            ps.elev =')
#change_variable_octave('            ps.v0 =')
#change_variable_octave('            pr.mass    =')
#change_variable_octave('            pr.caliber =')
#change_variable_octave('            pr.length  =')


########change_variable_octave('            dragModel =')

#change_variable_octave('            srcLevelSph_dB_SPL =')
#change_variable_octave('            srcLevelSw_dB_SPL =')

#change_variable_octave('            ps.levSph   = ')
#change_variable_octave('            ps.levSW    =')
#change_variable_octave('            ps.attnCoef =')

#change_variable_octave('            sensorInfo.position =')

#change_variable_octave('            paramSw.impPosZ =')

