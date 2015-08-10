info = {
    'version': .1,
    'author': 'Lawrence'
}

inputs = ['CNC']
outputs = ['OMG', 'BTT']

def runModule(CNC):
    print(CNC)
    omg = 'husk'
    btt = 'blet'

    return {
        'OMG': omg,
        'BTT': btt
    }
