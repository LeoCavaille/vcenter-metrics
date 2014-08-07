CPU_METRICS = [
    # CPU Capacity Contention
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'cpu.capacity.contention',
        's_type'       : 'rate',
        'unit'         : 'percent',
        'rollup'       : 'average',
        'entity'       : ['ResourcePool'],
        'instance_tag' : None
    },
    # CPU Capacity Demand
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'cpu.capacity.demand',
        's_type'       : 'rate',
        'unit'         : 'megaHertz',
        'rollup'       : 'average',
        'entity'       : ['ResourcePool'],
        'instance_tag' : None
    },
    # CPU Capacity Entitlement
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'cpu.capacity.entitlement',
        's_type'       : 'absolute',
        'unit'         : 'megaHertz',
        'rollup'       : 'average',
        'entity'       : ['ResourcePool'],
        'instance_tag' : None
    },
    # CPU Capacity Provisioned
    # Compatibility: UNKNOWN
    {
        'name'         : 'cpu.capacity.provisioned',
        's_type'       : 'absolute',
        'unit'         : 'megaHertz',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # CPU Capacity Usage
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'cpu.capacity.usage',
        's_type'       : 'rate',
        'unit'         : 'megaHertz',
        'rollup'       : 'average',
        'entity'       : ['ResourcePool'],
        'instance_tag' : None
    },
    # Core Utilization
    # Compatibility: UNKNOWN
    {
        'name'         : 'cpu.coreUtilization',
        's_type'       : 'rate',
        'unit'         : 'percent',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # CPU Core Count Contention
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'cpu.corecount.contention',
        's_type'       : 'rate',
        'unit'         : 'percent',
        'rollup'       : 'average',
        'entity'       : ['ResourcePool'],
        'instance_tag' : None
    },
    # CPU Core Count Provisioned
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'cpu.corecount.provisioned',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : ['ResourcePool'],
        'instance_tag' : None
    },
    # CPU Core Count Usage
    # Compatibility: UNKNOWN
    {
        'name'         : 'cpu.corecount.usage',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # Co-stop
    # Compatibility: 5.0.0
    {
        'name'         : 'cpu.costop',
        's_type'       : 'delta',
        'unit'         : 'millisecond',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Worst case allocation
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'cpu.cpuentitlement',
        's_type'       : 'absolute',
        'unit'         : 'megaHertz',
        'rollup'       : 'latest',
        'entity'       : ['ResourcePool'],
        'instance_tag' : None
    },
    # Demand
    # Compatibility: 5.0.0
    {
        'name'         : 'cpu.demand',
        's_type'       : 'rate',
        'unit'         : 'megaHertz',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Entitlement
    # Compatibility: 5.0.0
    {
        'name'         : 'cpu.entitlement',
        's_type'       : 'absolute',
        'unit'         : 'megaHertz',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine'],
        'instance_tag' : None
    },
    # Extra
    # Compatibility: 3.5.0
    {
        'name'         : 'cpu.extra',
        's_type'       : 'delta',
        'unit'         : 'millisecond',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine'],
        'instance_tag' : None
    },
    # Guaranteed
    # Compatibility: 3.5.0
    {
        'name'         : 'cpu.guaranteed',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine'],
        'instance_tag' : None
    },
    # Idle
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'cpu.idle',
        's_type'       : 'delta',
        'unit'         : 'millisecond',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Latency
    # Compatibility: 5.0.0
    {
        'name'         : 'cpu.latency',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Max limited
    # Compatibility: 5.0.0
    {
        'name'         : 'cpu.maxlimited',
        's_type'       : 'delta',
        'unit'         : 'millisecond',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine'],
        'instance_tag' : None
    },
    # Overlap
    # Compatibility: 5.0.0
    {
        'name'         : 'cpu.overlap',
        's_type'       : 'delta',
        'unit'         : 'millisecond',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine'],
        'instance_tag' : None
    },
    # Ready
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'cpu.ready',
        's_type'       : 'delta',
        'unit'         : 'millisecond',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Reserved capacity
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'cpu.reservedCapacity',
        's_type'       : 'absolute',
        'unit'         : 'megaHertz',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Run
    # Compatibility: 5.0.0
    {
        'name'         : 'cpu.run',
        's_type'       : 'delta',
        'unit'         : 'millisecond',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine'],
        'instance_tag' : None
    },
    # Swap wait
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'cpu.swapwait',
        's_type'       : 'delta',
        'unit'         : 'millisecond',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # System
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'cpu.system',
        's_type'       : 'delta',
        'unit'         : 'millisecond',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine'],
        'instance_tag' : None
    },
    # Total capacity
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'cpu.totalCapacity',
        's_type'       : 'absolute',
        'unit'         : 'megaHertz',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Total
    # Compatibility: UNKNOWN
    {
        'name'         : 'cpu.totalmhz',
        's_type'       : 'rate',
        'unit'         : 'megaHertz',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # Usage
    # Compatibility: UNKNOWN
    {
        'name'         : 'cpu.usage',
        's_type'       : 'rate',
        'unit'         : 'percent',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Usage in MHz
    # Compatibility: UNKNOWN
    {
        'name'         : 'cpu.usagemhz',
        's_type'       : 'rate',
        'unit'         : 'megaHertz',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'ResourcePool'],
        'instance_tag' : None
    },
    # Used
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'cpu.used',
        's_type'       : 'delta',
        'unit'         : 'millisecond',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Utilization
    # Compatibility: UNKNOWN
    {
        'name'         : 'cpu.utilization',
        's_type'       : 'rate',
        'unit'         : 'percent',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Wait
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'cpu.wait',
        's_type'       : 'delta',
        'unit'         : 'millisecond',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
]


DATASTORE_METRICS = [
    # Bus resets
    # Compatibility: UNKNOWN
    {
        'name'         : 'datastore.busResets',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : ['Datastore'],
        'instance_tag' : None
    },
    # Datastore Command Aborts
    # Compatibility: UNKNOWN
    {
        'name'         : 'datastore.commandsAborted',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : ['Datastore'],
        'instance_tag' : None
    },
    # Storage I/O Control aggregated IOPS
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'datastore.datastoreIops',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Storage I/O Control datastore maximum queue depth
    # Compatibility: 5.0.0
    {
        'name'         : 'datastore.datastoreMaxQueueDepth',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Storage DRS datastore normalized read latency
    # Compatibility: 5.0.0
    {
        'name'         : 'datastore.datastoreNormalReadLatency',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Storage DRS datastore normalized write latency
    # Compatibility: 5.0.0
    {
        'name'         : 'datastore.datastoreNormalWriteLatency',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Storage DRS datastore bytes read
    # Compatibility: 5.0.0
    {
        'name'         : 'datastore.datastoreReadBytes',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Storage DRS datastore read I/O rate
    # Compatibility: 5.0.0
    {
        'name'         : 'datastore.datastoreReadIops',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Storage DRS datastore read workload metric
    # Compatibility: 5.0.0
    {
        'name'         : 'datastore.datastoreReadLoadMetric',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Storage DRS datastore outstanding read requests
    # Compatibility: 5.0.0
    {
        'name'         : 'datastore.datastoreReadOIO',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Storage DRS datastore bytes written
    # Compatibility: 5.0.0
    {
        'name'         : 'datastore.datastoreWriteBytes',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Storage DRS datastore write I/O rate
    # Compatibility: 5.0.0
    {
        'name'         : 'datastore.datastoreWriteIops',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Storage DRS datastore write workload metric
    # Compatibility: 5.0.0
    {
        'name'         : 'datastore.datastoreWriteLoadMetric',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Storage DRS datastore outstanding write requests
    # Compatibility: 5.0.0
    {
        'name'         : 'datastore.datastoreWriteOIO',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Highest latency
    # Compatibility: 5.0.0
    {
        'name'         : 'datastore.maxTotalLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Average read requests per second
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'datastore.numberReadAveraged',
        's_type'       : 'rate',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'Datastore'],
        'instance_tag' : None
    },
    # Average write requests per second
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'datastore.numberWriteAveraged',
        's_type'       : 'rate',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'Datastore'],
        'instance_tag' : None
    },
    # Read rate
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'datastore.read',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'Datastore'],
        'instance_tag' : None
    },
    # Storage I/O Control normalized latency
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'datastore.sizeNormalizedDatastoreLatency',
        's_type'       : 'absolute',
        'unit'         : 'microsecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Datastore Throughput Contention
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'datastore.throughput.contention',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['Datastore'],
        'instance_tag' : None
    },
    # Datastore Throughput Usage
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'datastore.throughput.usage',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['Datastore'],
        'instance_tag' : None
    },
    # Read latency
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'datastore.totalReadLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Write latency
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'datastore.totalWriteLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Write rate
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'datastore.write',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'Datastore'],
        'instance_tag' : None
    },
]


DISK_METRICS = [
    # Bus resets
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.busResets',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem', 'Datastore'],
        'instance_tag' : None
    },
    # Storage Capacity Contention
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.capacity.contention',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'average',
        'entity'       : ['Datastore'],
        'instance_tag' : None
    },
    # Storage Capacity Provisioned
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.capacity.provisioned',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['Datastore'],
        'instance_tag' : None
    },
    # Storage Capacity Usage
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.capacity.usage',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['Datastore'],
        'instance_tag' : None
    },
    # Commands issued
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.commands',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Commands terminated
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.commandsAborted',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem', 'Datastore'],
        'instance_tag' : None
    },
    # Average commands issued per second
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'disk.commandsAveraged',
        's_type'       : 'rate',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Overhead due to delta disk backings
    # Compatibility: UNKNOWN
    {
        'name'         : 'disk.deltaused',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'latest',
        'entity'       : [],
        'instance_tag' : None
    },
    # Physical device command latency
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.deviceLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Physical device read latency
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.deviceReadLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Physical device write latency
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.deviceWriteLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Kernel command latency
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.kernelLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Kernel read latency
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.kernelReadLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Kernel write latency
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.kernelWriteLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Maximum queue depth
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'disk.maxQueueDepth',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Highest latency
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.maxTotalLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Read requests
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.numberRead',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Average read requests per second
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.numberReadAveraged',
        's_type'       : 'rate',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'Datastore'],
        'instance_tag' : None
    },
    # Write requests
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.numberWrite',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Average write requests per second
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.numberWriteAveraged',
        's_type'       : 'rate',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'Datastore'],
        'instance_tag' : None
    },
    # Queue command latency
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.queueLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Queue read latency
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.queueReadLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Queue write latency
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.queueWriteLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Read rate
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.read',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'Datastore'],
        'instance_tag' : None
    },
    # Disk SCSI Reservation Conflicts %
    # Compatibility: UNKNOWN
    {
        'name'         : 'disk.scsiReservationCnflctsPct',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # Disk SCSI Reservation Conflicts
    # Compatibility: UNKNOWN
    {
        'name'         : 'disk.scsiReservationConflicts',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : [],
        'instance_tag' : None
    },
    # Disk Throughput Contention
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.throughput.contention',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['ResourcePool'],
        'instance_tag' : None
    },
    # Disk Throughput Usage
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.throughput.usage',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['ResourcePool'],
        'instance_tag' : None
    },
    # Command latency
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.totalLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystemDatastore'],
        'instance_tag' : None
    },
    # Read latency
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.totalReadLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Write latency
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.totalWriteLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Usage
    # Compatibility: UNKNOWN
    {
        'name'         : 'disk.usage',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Write rate
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.write',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'Datastore'],
        'instance_tag' : None
    },
]


HBR_METRICS = [
    # 
    # Compatibility: 5.0.0
    {
        'name'         : 'hbr.hbrNetRx',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # 
    # Compatibility: 5.0.0
    {
        'name'         : 'hbr.hbrNetTx',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # 
    # Compatibility: 5.0.0
    {
        'name'         : 'hbr.hbrNumVms',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
]


MANAGEMENTAGENT_METRICS = [
    # CPU usage
    # Compatibility: UNKNOWN
    {
        'name'         : 'managementAgent.cpuUsage',
        's_type'       : 'rate',
        'unit'         : 'megaHertz',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # Memory used
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0
    {
        'name'         : 'managementAgent.memUsed',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Memory swap in
    # Compatibility: 3.5.0 / 4.1.0
    {
        'name'         : 'managementAgent.swapIn',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Memory swap out
    # Compatibility: 3.5.0 / 4.1.0
    {
        'name'         : 'managementAgent.swapOut',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Memory swap used
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0
    {
        'name'         : 'managementAgent.swapUsed',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
]


MEM_METRICS = [
    # Active
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.active',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'ResourcePool'],
        'instance_tag' : None
    },
    # Active write
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'mem.activewrite',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Memory Capacity Contention
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'mem.capacity.contention',
        's_type'       : 'rate',
        'unit'         : 'percent',
        'rollup'       : 'average',
        'entity'       : ['ResourcePool'],
        'instance_tag' : None
    },
    # Memory Capacity Entitlement
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'mem.capacity.entitlement',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['ResourcePool'],
        'instance_tag' : None
    },
    # Memory Capacity Provisioned
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'mem.capacity.provisioned',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['ResourcePool'],
        'instance_tag' : None
    },
    # Memory Capacity Usable
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.capacity.usable',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # Memory Capacity Usage
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'mem.capacity.usage',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['ResourcePool'],
        'instance_tag' : None
    },
    # 
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.capacity.usage.userworld',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # 
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.capacity.usage.vm',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # Memory Capacity Usage by VM overhead
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.capacity.usage.vmOvrhd',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # Memory Capacity Usage by VMkernel Overhead
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.capacity.usage.vmkOvrhd',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # Compressed
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'mem.compressed',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'ResourcePool'],
        'instance_tag' : None
    },
    # Compression rate
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'mem.compressionRate',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'ResourcePool'],
        'instance_tag' : None
    },
    # Consumed
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.consumed',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'ResourcePool'],
        'instance_tag' : None
    },
    # Memory Consumed by userworlds
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.consumed.userworlds',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # Memory Consumed by VMs
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.consumed.vms',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # Decompression rate
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'mem.decompressionRate',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'ResourcePool'],
        'instance_tag' : None
    },
    # Entitlement
    # Compatibility: 5.0.0
    {
        'name'         : 'mem.entitlement',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine'],
        'instance_tag' : None
    },
    # Granted
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.granted',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'ResourcePool'],
        'instance_tag' : None
    },
    # Heap
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.heap',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Heap free
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.heapfree',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Latency
    # Compatibility: 5.0.0
    {
        'name'         : 'mem.latency',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Swap in from host cache
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.llSwapIn',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Swap in rate from host cache
    # Compatibility: 5.0.0
    {
        'name'         : 'mem.llSwapInRate',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Swap out to host cache
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.llSwapOut',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Swap out rate to host cache
    # Compatibility: 5.0.0
    {
        'name'         : 'mem.llSwapOutRate',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Host cache used for swapping
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.llSwapUsed',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Low free threshold
    # Compatibility: 5.0.0
    {
        'name'         : 'mem.lowfreethreshold',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Worst case allocation
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'mem.mementitlement',
        's_type'       : 'absolute',
        'unit'         : 'megaBytes',
        'rollup'       : 'latest',
        'entity'       : ['ResourcePool'],
        'instance_tag' : None
    },
    # Overhead
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.overhead',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'ResourcePool'],
        'instance_tag' : None
    },
    # Reserved overhead
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'mem.overheadMax',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine'],
        'instance_tag' : None
    },
    # Overhead touched
    # Compatibility: 5.0.0
    {
        'name'         : 'mem.overheadTouched',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine'],
        'instance_tag' : None
    },
    # Reserved capacity
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'mem.reservedCapacity',
        's_type'       : 'absolute',
        'unit'         : 'megaBytes',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Memory Reserved capacity by userworlds
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.reservedCapacity.userworld',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # Memory Reserved capacity by VMs
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.reservedCapacity.vm',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # Memory Reserved capacity by VM overhead
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.reservedCapacity.vmOvhd',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # Memory Reserved capacity by VMkernel Overhead
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.reservedCapacity.vmkOvrhd',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # Memory Reserved Capacity %
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.reservedCapacityPct',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # Shared
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.shared',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'ResourcePool'],
        'instance_tag' : None
    },
    # Shared common
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.sharedcommon',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # State
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'mem.state',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Swap in
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.swapin',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Swap in rate
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'mem.swapinRate',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Swap out
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.swapout',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Swap out rate
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'mem.swapoutRate',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Swapped
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.swapped',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'ResourcePool'],
        'instance_tag' : None
    },
    # Swap target
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.swaptarget',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine'],
        'instance_tag' : None
    },
    # Swap unreserved
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.swapunreserved',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # Swap used
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.swapused',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Used by VMkernel
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.sysUsage',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Total capacity
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'mem.totalCapacity',
        's_type'       : 'absolute',
        'unit'         : 'megaBytes',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Total
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.totalmb',
        's_type'       : 'absolute',
        'unit'         : 'megaBytes',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # Unreserved
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.unreserved',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Usage
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.usage',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Balloon
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.vmmemctl',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'ResourcePool'],
        'instance_tag' : None
    },
    # Balloon target
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.vmmemctltarget',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine'],
        'instance_tag' : None
    },
    # Zero
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.zero',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'ResourcePool'],
        'instance_tag' : None
    },
    # Memory saved by zipping
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'mem.zipSaved',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine'],
        'instance_tag' : None
    },
    # Zipped memory
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'mem.zipped',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine'],
        'instance_tag' : None
    },
]


NETWORK_METRICS = [
    # Broadcast receives
    # Compatibility: 5.0.0
    {
        'name'         : 'network.broadcastRx',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Broadcast transmits
    # Compatibility: 5.0.0
    {
        'name'         : 'network.broadcastTx',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Data receive rate
    # Compatibility: 5.0.0
    {
        'name'         : 'network.bytesRx',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Data transmit rate
    # Compatibility: 5.0.0
    {
        'name'         : 'network.bytesTx',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Receive packets dropped
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'network.droppedRx',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Transmit packets dropped
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'network.droppedTx',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Packet receive errors
    # Compatibility: 5.0.0
    {
        'name'         : 'network.errorsRx',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Packet transmit errors
    # Compatibility: 5.0.0
    {
        'name'         : 'network.errorsTx',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Multicast receives
    # Compatibility: 5.0.0
    {
        'name'         : 'network.multicastRx',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Multicast transmits
    # Compatibility: 5.0.0
    {
        'name'         : 'network.multicastTx',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Packets received
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'network.packetsRx',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Packets transmitted
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'network.packetsTx',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Data receive rate
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'network.received',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # vNic Throughput Contention
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'network.throughput.contention',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : ['ResourcePool'],
        'instance_tag' : None
    },
    # pNic Packets Received and Transmitted per Second
    # Compatibility: UNKNOWN
    {
        'name'         : 'network.throughput.packetsPerSec',
        's_type'       : 'rate',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # pNic Throughput Provisioned
    # Compatibility: UNKNOWN
    {
        'name'         : 'network.throughput.provisioned',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # pNic Throughput Usable
    # Compatibility: UNKNOWN
    {
        'name'         : 'network.throughput.usable',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # vNic Throughput Usage
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'network.throughput.usage',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['ResourcePool'],
        'instance_tag' : None
    },
    # pNic Throughput Usage for FT
    # Compatibility: UNKNOWN
    {
        'name'         : 'network.throughput.usage.ft',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # pNic Throughput Usage for HBR
    # Compatibility: UNKNOWN
    {
        'name'         : 'network.throughput.usage.hbr',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # pNic Throughput Usage for iSCSI
    # Compatibility: UNKNOWN
    {
        'name'         : 'network.throughput.usage.iscsi',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # pNic Throughput Usage for NFS
    # Compatibility: UNKNOWN
    {
        'name'         : 'network.throughput.usage.nfs',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # pNic Throughput Usage for VMs
    # Compatibility: UNKNOWN
    {
        'name'         : 'network.throughput.usage.vm',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # pNic Throughput Usage for vMotion
    # Compatibility: UNKNOWN
    {
        'name'         : 'network.throughput.usage.vmotion',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # Data transmit rate
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'network.transmitted',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Unknown protocol frames
    # Compatibility: 5.0.0
    {
        'name'         : 'network.unknownProtos',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Usage
    # Compatibility: UNKNOWN
    {
        'name'         : 'network.usage',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
]


POWER_METRICS = [
    # Host Power Capacity Usable
    # Compatibility: UNKNOWN
    {
        'name'         : 'power.capacity.usable',
        's_type'       : 'absolute',
        'unit'         : 'watt',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # Power Capacity Usage
    # Compatibility: UNKNOWN
    {
        'name'         : 'power.capacity.usage',
        's_type'       : 'absolute',
        'unit'         : 'watt',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # Host Power Capacity Provisioned
    # Compatibility: UNKNOWN
    {
        'name'         : 'power.capacity.usagePct',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # Energy usage
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'power.energy',
        's_type'       : 'delta',
        'unit'         : 'joule',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem', 'ResourcePool'],
        'instance_tag' : None
    },
    # Usage
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'power.power',
        's_type'       : 'absolute',
        'unit'         : 'watt',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'ResourcePool'],
        'instance_tag' : None
    },
    # Cap
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'power.powerCap',
        's_type'       : 'absolute',
        'unit'         : 'watt',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
]


RESCPU_METRICS = [
    # Active (1 min. average)
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'rescpu.actav1',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Active (15 min. average)
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'rescpu.actav15',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Active (5 min. average)
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'rescpu.actav5',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Active (1 min. peak)
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'rescpu.actpk1',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Active (15 min. peak)
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'rescpu.actpk15',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Active (5 min. peak)
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'rescpu.actpk5',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Throttled (1 min. average)
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'rescpu.maxLimited1',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Throttled (15 min. average)
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'rescpu.maxLimited15',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Throttled (5 min. average)
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'rescpu.maxLimited5',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Running (1 min. average)
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'rescpu.runav1',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Running (15 min. average)
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'rescpu.runav15',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Running (5 min. average)
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'rescpu.runav5',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Running (1 min. peak)
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'rescpu.runpk1',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Running (15 min. peak)
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'rescpu.runpk15',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Running (5 min. peak)
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'rescpu.runpk5',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Group CPU sample count
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'rescpu.sampleCount',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
    # Group CPU sample period
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'rescpu.samplePeriod',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
]


STORAGEADAPTER_METRICS = [
    # Storage Adapter Outstanding I/Os
    # Compatibility: UNKNOWN
    {
        'name'         : 'storageAdapter.OIOsPct',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # Average commands issued per second
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'storageAdapter.commandsAveraged',
        's_type'       : 'rate',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Highest latency
    # Compatibility: 5.0.0
    {
        'name'         : 'storageAdapter.maxTotalLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Average read requests per second
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'storageAdapter.numberReadAveraged',
        's_type'       : 'rate',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Average write requests per second
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'storageAdapter.numberWriteAveraged',
        's_type'       : 'rate',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Storage Adapter Outstanding I/Os
    # Compatibility: UNKNOWN
    {
        'name'         : 'storageAdapter.outstandingIOs',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # Storage Adapter Queue Depth
    # Compatibility: UNKNOWN
    {
        'name'         : 'storageAdapter.queueDepth',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # Storage Adapter Queue Command Latency
    # Compatibility: UNKNOWN
    {
        'name'         : 'storageAdapter.queueLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # Storage Adapter Number Queued
    # Compatibility: UNKNOWN
    {
        'name'         : 'storageAdapter.queued',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # Read rate
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'storageAdapter.read',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Storage Adapter Throughput Contention
    # Compatibility: UNKNOWN
    {
        'name'         : 'storageAdapter.throughput.cont',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # Storage Adapter Throughput Usage
    # Compatibility: UNKNOWN
    {
        'name'         : 'storageAdapter.throughput.usag',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # Read latency
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'storageAdapter.totalReadLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Write latency
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'storageAdapter.totalWriteLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Write rate
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'storageAdapter.write',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
]


STORAGEPATH_METRICS = [
    # Storage Path Bus Resets
    # Compatibility: UNKNOWN
    {
        'name'         : 'storagePath.busResets',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : [],
        'instance_tag' : None
    },
    # Storage Path Command Aborts
    # Compatibility: UNKNOWN
    {
        'name'         : 'storagePath.commandsAborted',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : [],
        'instance_tag' : None
    },
    # Average commands issued per second
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'storagePath.commandsAveraged',
        's_type'       : 'rate',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Highest latency
    # Compatibility: 5.0.0
    {
        'name'         : 'storagePath.maxTotalLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Average read requests per second
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'storagePath.numberReadAveraged',
        's_type'       : 'rate',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Average write requests per second
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'storagePath.numberWriteAveraged',
        's_type'       : 'rate',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Read rate
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'storagePath.read',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Storage Path Throughput Contention
    # Compatibility: UNKNOWN
    {
        'name'         : 'storagePath.throughput.cont',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # Storage Path Throughput Usage
    # Compatibility: UNKNOWN
    {
        'name'         : 'storagePath.throughput.usage',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # Read latency
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'storagePath.totalReadLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Write latency
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'storagePath.totalWriteLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Write rate
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'storagePath.write',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
]


SYSTEM_METRICS = [
    # Disk space usage
    # Compatibility: 4.0.0
    {
        'name'         : 'system.cosDiskUsage',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Disk usage
    # Compatibility: 4.1.0
    {
        'name'         : 'system.diskUsage',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Heartbeat
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.heartbeat',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine'],
        'instance_tag' : None
    },
    # OS Uptime
    # Compatibility: 5.0.0
    {
        'name'         : 'system.osUptime',
        's_type'       : 'absolute',
        'unit'         : 'second',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine'],
        'instance_tag' : None
    },
    # Resource CPU active (1 min. average)
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.resourceCpuAct1',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Resource CPU active (5 min. average)
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.resourceCpuAct5',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Resource CPU allocation maximum, in MHz
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.resourceCpuAllocMax',
        's_type'       : 'absolute',
        'unit'         : 'megaHertz',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Resource CPU allocation minimum, in MHz
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.resourceCpuAllocMin',
        's_type'       : 'absolute',
        'unit'         : 'megaHertz',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Resource CPU allocation shares
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.resourceCpuAllocShares',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Resource CPU maximum limited (1 min.)
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.resourceCpuMaxLimited1',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Resource CPU maximum limited (5 min.)
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.resourceCpuMaxLimited5',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Resource CPU running (1 min. average)
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.resourceCpuRun1',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Resource CPU running (5 min. average)
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.resourceCpuRun5',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Resource CPU usage ({rollupType})
    # Compatibility: UNKNOWN
    {
        'name'         : 'system.resourceCpuUsage',
        's_type'       : 'rate',
        'unit'         : 'megaHertz',
        'rollup'       : 'average',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Resource memory allocation maximum, in KB
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.resourceMemAllocMax',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Resource memory allocation minimum, in KB
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.resourceMemAllocMin',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Resource memory allocation shares
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.resourceMemAllocShares',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Resource memory shared
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.resourceMemCow',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Resource memory mapped
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.resourceMemMapped',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Resource memory overhead
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.resourceMemOverhead',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Resource memory share saved
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.resourceMemShared',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Resource memory swapped
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.resourceMemSwapped',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Resource memory touched
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.resourceMemTouched',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Resource memory zero
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.resourceMemZero',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem'],
        'instance_tag' : None
    },
    # Uptime
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.uptime',
        's_type'       : 'absolute',
        'unit'         : 'second',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem'],
        'instance_tag' : None
    },
]


VIRTUALDISK_METRICS = [
    # Virtual Disk Bus Resets
    # Compatibility: UNKNOWN
    {
        'name'         : 'virtualDisk.busResets',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : [],
        'instance_tag' : None
    },
    # Virtual Disk Command Aborts
    # Compatibility: UNKNOWN
    {
        'name'         : 'virtualDisk.commandsAborted',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : [],
        'instance_tag' : None
    },
    # Average read requests per second
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'virtualDisk.numberReadAveraged',
        's_type'       : 'rate',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine'],
        'instance_tag' : None
    },
    # Average write requests per second
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'virtualDisk.numberWriteAveraged',
        's_type'       : 'rate',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine'],
        'instance_tag' : None
    },
    # Read rate
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'virtualDisk.read',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine'],
        'instance_tag' : None
    },
    # Read workload metric
    # Compatibility: 5.0.0
    {
        'name'         : 'virtualDisk.readLoadMetric',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine'],
        'instance_tag' : None
    },
    # Average number of outstanding read requests
    # Compatibility: 5.0.0
    {
        'name'         : 'virtualDisk.readOIO',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine'],
        'instance_tag' : None
    },
    # Virtual Disk Throughput Contention
    # Compatibility: UNKNOWN
    {
        'name'         : 'virtualDisk.throughput.cont',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # Virtual Disk Throughput Usage
    # Compatibility: UNKNOWN
    {
        'name'         : 'virtualDisk.throughput.usage',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : [],
        'instance_tag' : None
    },
    # Read latency
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'virtualDisk.totalReadLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine'],
        'instance_tag' : None
    },
    # Write latency
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'virtualDisk.totalWriteLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine'],
        'instance_tag' : None
    },
    # Write rate
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'virtualDisk.write',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine'],
        'instance_tag' : None
    },
    # Write workload metric
    # Compatibility: 5.0.0
    {
        'name'         : 'virtualDisk.writeLoadMetric',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine'],
        'instance_tag' : None
    },
    # Average number of outstanding write requests
    # Compatibility: 5.0.0
    {
        'name'         : 'virtualDisk.writeOIO',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine'],
        'instance_tag' : None
    },
]


ALL_METRICS = CPU_METRICS + DATASTORE_METRICS + DISK_METRICS + \
    HBR_METRICS + MANAGEMENTAGENT_METRICS + MEM_METRICS + NETWORK_METRICS + \
    POWER_METRICS + RESCPU_METRICS + STORAGEADAPTER_METRICS + \
    STORAGEPATH_METRICS + VIRTUALDISK_METRICS
