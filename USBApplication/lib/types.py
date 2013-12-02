def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    reverse = dict((value, key) for key, value in enums.iteritems())
    enums['reverse_mapping'] = reverse
    return type('Enum', (), enums)


READING = enum('VOLTAGE', 'CURRENT', 'PERIOD', 'ACTIVE_POWER',
        'REACTIVE_POWER', 'APPARENT_POWER', 'PHASE_ANGLE', 'POWER_FACTOR')
