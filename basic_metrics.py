BASIC_METRICS = [
    {
        'name'         : 'cpu.extra',
        's_type'       : 'delta',
        'unit'         : 'millisecond',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine']
    },
    {
        'name'         : 'cpu.ready',
        's_type'       : 'delta',
        'unit'         : 'millisecond',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    {
        'name'         : 'cpu.usage',
        's_type'       : 'rate',
        'unit'         : 'percent',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    {
        'name'         : 'cpu.usagemhz',
        's_type'       : 'rate',
        'unit'         : 'megaHertz',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'ResourcePool']
    },
    {
        'name'         : 'disk.commandsAborted',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem', 'Datastore']
    },
    {
        'name'         : 'disk.deviceLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    {
        'name'         : 'disk.deviceReadLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    {
        'name'         : 'disk.deviceWriteLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    {
        'name'         : 'disk.queueLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    {
        'name'         : 'disk.totalLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystemDatastore']
    },
    {
        'name'         : 'mem.active',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'ResourcePool']
    },
    {
        'name'         : 'mem.compressed',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'ResourcePool']
    },
    {
        'name'         : 'mem.consumed',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'ResourcePool']
    },
    {
        'name'         : 'mem.overhead',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'ResourcePool']
    },
    {
        'name'         : 'mem.vmmemctl',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'ResourcePool']
    },
]