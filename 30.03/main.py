__author__ = 'Дмитрий'
class leo():
    data = {'action' : 'default',
            'status' : 'hungry'}
    diff = {
        'antelope' : {'full' : {'action' : 'sleep',
                                'status' : 'hungry'},
                      'hungry':{'action' : 'eat',
                                'status' : 'full'}},

        'hunter'    :{'full' :  {'action' : 'run',
                                 'status' : 'hungry'},
                      'hungry': {'action' : 'run',
                                 'status' : 'null'}},

        'tree'      :{'full' : { 'action' : 'see',
                                 'status' : 'hungry'},
                      'hungry' :{'action' : 'sleep',
                                 'status' : 'null'}}
    }