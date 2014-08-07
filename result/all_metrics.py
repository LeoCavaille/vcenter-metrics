CPU_METRICS = [
    # CPU Capacity Contention
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'cpu.capacity.contention',
        's_type'       : 'rate',
        'unit'         : 'percent',
        'rollup'       : 'average',
        'entity'       : ['ResourcePool']
    },
    # CPU Capacity Demand
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'cpu.capacity.demand',
        's_type'       : 'rate',
        'unit'         : 'megaHertz',
        'rollup'       : 'average',
        'entity'       : ['ResourcePool']
    },
    # CPU Capacity Entitlement
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'cpu.capacity.entitlement',
        's_type'       : 'absolute',
        'unit'         : 'megaHertz',
        'rollup'       : 'average',
        'entity'       : ['ResourcePool']
    },
    # CPU Capacity Provisioned
    # Compatibility: UNKNOWN
    {
        'name'         : 'cpu.capacity.provisioned',
        's_type'       : 'absolute',
        'unit'         : 'megaHertz',
        'rollup'       : 'average',
        'entity'       : []
    },
    # CPU Capacity Usage
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'cpu.capacity.usage',
        's_type'       : 'rate',
        'unit'         : 'megaHertz',
        'rollup'       : 'average',
        'entity'       : ['ResourcePool']
    },
    # Core Utilization
    # Compatibility: UNKNOWN
    {
        'name'         : 'cpu.coreUtilization',
        's_type'       : 'rate',
        'unit'         : 'percent',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # CPU Core Count Contention
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'cpu.corecount.contention',
        's_type'       : 'rate',
        'unit'         : 'percent',
        'rollup'       : 'average',
        'entity'       : ['ResourcePool']
    },
    # CPU Core Count Provisioned
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'cpu.corecount.provisioned',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : ['ResourcePool']
    },
    # CPU Core Count Usage
    # Compatibility: UNKNOWN
    {
        'name'         : 'cpu.corecount.usage',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : []
    },
    # Co-stop
    # Compatibility: 5.0.0
    {
        'name'         : 'cpu.costop',
        's_type'       : 'delta',
        'unit'         : 'millisecond',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Worst case allocation
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'cpu.cpuentitlement',
        's_type'       : 'absolute',
        'unit'         : 'megaHertz',
        'rollup'       : 'latest',
        'entity'       : ['ResourcePool']
    },
    # Demand
    # Compatibility: 5.0.0
    {
        'name'         : 'cpu.demand',
        's_type'       : 'rate',
        'unit'         : 'megaHertz',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Entitlement
    # Compatibility: 5.0.0
    {
        'name'         : 'cpu.entitlement',
        's_type'       : 'absolute',
        'unit'         : 'megaHertz',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine']
    },
    # Extra
    # Compatibility: 3.5.0
    {
        'name'         : 'cpu.extra',
        's_type'       : 'delta',
        'unit'         : 'millisecond',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine']
    },
    # Guaranteed
    # Compatibility: 3.5.0
    {
        'name'         : 'cpu.guaranteed',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine']
    },
    # Idle
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'cpu.idle',
        's_type'       : 'delta',
        'unit'         : 'millisecond',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Latency
    # Compatibility: 5.0.0
    {
        'name'         : 'cpu.latency',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Max limited
    # Compatibility: 5.0.0
    {
        'name'         : 'cpu.maxlimited',
        's_type'       : 'delta',
        'unit'         : 'millisecond',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine']
    },
    # Overlap
    # Compatibility: 5.0.0
    {
        'name'         : 'cpu.overlap',
        's_type'       : 'delta',
        'unit'         : 'millisecond',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine']
    },
    # Ready
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'cpu.ready',
        's_type'       : 'delta',
        'unit'         : 'millisecond',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Reserved capacity
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'cpu.reservedCapacity',
        's_type'       : 'absolute',
        'unit'         : 'megaHertz',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Run
    # Compatibility: 5.0.0
    {
        'name'         : 'cpu.run',
        's_type'       : 'delta',
        'unit'         : 'millisecond',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine']
    },
    # Swap wait
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'cpu.swapwait',
        's_type'       : 'delta',
        'unit'         : 'millisecond',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # System
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'cpu.system',
        's_type'       : 'delta',
        'unit'         : 'millisecond',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine']
    },
    # Total capacity
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'cpu.totalCapacity',
        's_type'       : 'absolute',
        'unit'         : 'megaHertz',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Total
    # Compatibility: UNKNOWN
    {
        'name'         : 'cpu.totalmhz',
        's_type'       : 'rate',
        'unit'         : 'megaHertz',
        'rollup'       : 'average',
        'entity'       : []
    },
    # Usage
    # Compatibility: UNKNOWN
    {
        'name'         : 'cpu.usage',
        's_type'       : 'rate',
        'unit'         : 'percent',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Usage in MHz
    # Compatibility: UNKNOWN
    {
        'name'         : 'cpu.usagemhz',
        's_type'       : 'rate',
        'unit'         : 'megaHertz',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'ResourcePool']
    },
    # Used
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'cpu.used',
        's_type'       : 'delta',
        'unit'         : 'millisecond',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Utilization
    # Compatibility: UNKNOWN
    {
        'name'         : 'cpu.utilization',
        's_type'       : 'rate',
        'unit'         : 'percent',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Wait
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'cpu.wait',
        's_type'       : 'delta',
        'unit'         : 'millisecond',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem']
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
        'entity'       : ['Datastore']
    },
    # Datastore Command Aborts
    # Compatibility: UNKNOWN
    {
        'name'         : 'datastore.commandsAborted',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : ['Datastore']
    },
    # Storage I/O Control aggregated IOPS
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'datastore.datastoreIops',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Storage I/O Control datastore maximum queue depth
    # Compatibility: 5.0.0
    {
        'name'         : 'datastore.datastoreMaxQueueDepth',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem']
    },
    # Storage DRS datastore normalized read latency
    # Compatibility: 5.0.0
    {
        'name'         : 'datastore.datastoreNormalReadLatency',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem']
    },
    # Storage DRS datastore normalized write latency
    # Compatibility: 5.0.0
    {
        'name'         : 'datastore.datastoreNormalWriteLatency',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem']
    },
    # Storage DRS datastore bytes read
    # Compatibility: 5.0.0
    {
        'name'         : 'datastore.datastoreReadBytes',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem']
    },
    # Storage DRS datastore read I/O rate
    # Compatibility: 5.0.0
    {
        'name'         : 'datastore.datastoreReadIops',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem']
    },
    # Storage DRS datastore read workload metric
    # Compatibility: 5.0.0
    {
        'name'         : 'datastore.datastoreReadLoadMetric',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem']
    },
    # Storage DRS datastore outstanding read requests
    # Compatibility: 5.0.0
    {
        'name'         : 'datastore.datastoreReadOIO',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem']
    },
    # Storage DRS datastore bytes written
    # Compatibility: 5.0.0
    {
        'name'         : 'datastore.datastoreWriteBytes',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem']
    },
    # Storage DRS datastore write I/O rate
    # Compatibility: 5.0.0
    {
        'name'         : 'datastore.datastoreWriteIops',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem']
    },
    # Storage DRS datastore write workload metric
    # Compatibility: 5.0.0
    {
        'name'         : 'datastore.datastoreWriteLoadMetric',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem']
    },
    # Storage DRS datastore outstanding write requests
    # Compatibility: 5.0.0
    {
        'name'         : 'datastore.datastoreWriteOIO',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem']
    },
    # Highest latency
    # Compatibility: 5.0.0
    {
        'name'         : 'datastore.maxTotalLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Average read requests per second
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'datastore.numberReadAveraged',
        's_type'       : 'rate',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'Datastore']
    },
    # Average write requests per second
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'datastore.numberWriteAveraged',
        's_type'       : 'rate',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'Datastore']
    },
    # Read rate
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'datastore.read',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'Datastore']
    },
    # Storage I/O Control normalized latency
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'datastore.sizeNormalizedDatastoreLatency',
        's_type'       : 'absolute',
        'unit'         : 'microsecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Datastore Throughput Contention
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'datastore.throughput.contention',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['Datastore']
    },
    # Datastore Throughput Usage
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'datastore.throughput.usage',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['Datastore']
    },
    # Read latency
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'datastore.totalReadLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Write latency
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'datastore.totalWriteLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Write rate
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'datastore.write',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'Datastore']
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
        'entity'       : ['VirtualMachine', 'HostSystem', 'Datastore']
    },
    # Storage Capacity Contention
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.capacity.contention',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'average',
        'entity'       : ['Datastore']
    },
    # Storage Capacity Provisioned
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.capacity.provisioned',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['Datastore']
    },
    # Storage Capacity Usage
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.capacity.usage',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['Datastore']
    },
    # Commands issued
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.commands',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Commands terminated
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.commandsAborted',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem', 'Datastore']
    },
    # Average commands issued per second
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'disk.commandsAveraged',
        's_type'       : 'rate',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Overhead due to delta disk backings
    # Compatibility: UNKNOWN
    {
        'name'         : 'disk.deltaused',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'latest',
        'entity'       : []
    },
    # Physical device command latency
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.deviceLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Physical device read latency
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.deviceReadLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Physical device write latency
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.deviceWriteLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Kernel command latency
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.kernelLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Kernel read latency
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.kernelReadLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Kernel write latency
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.kernelWriteLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Maximum queue depth
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'disk.maxQueueDepth',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Highest latency
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.maxTotalLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Read requests
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.numberRead',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Average read requests per second
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.numberReadAveraged',
        's_type'       : 'rate',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'Datastore']
    },
    # Write requests
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.numberWrite',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Average write requests per second
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.numberWriteAveraged',
        's_type'       : 'rate',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'Datastore']
    },
    # Queue command latency
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.queueLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Queue read latency
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.queueReadLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Queue write latency
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.queueWriteLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Read rate
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.read',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'Datastore']
    },
    # Disk SCSI Reservation Conflicts %
    # Compatibility: UNKNOWN
    {
        'name'         : 'disk.scsiReservationCnflctsPct',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'average',
        'entity'       : []
    },
    # Disk SCSI Reservation Conflicts
    # Compatibility: UNKNOWN
    {
        'name'         : 'disk.scsiReservationConflicts',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : []
    },
    # Disk Throughput Contention
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.throughput.contention',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['ResourcePool']
    },
    # Disk Throughput Usage
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.throughput.usage',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['ResourcePool']
    },
    # Command latency
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.totalLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystemDatastore']
    },
    # Read latency
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.totalReadLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Write latency
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.totalWriteLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Usage
    # Compatibility: UNKNOWN
    {
        'name'         : 'disk.usage',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Write rate
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'disk.write',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'Datastore']
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
        'entity'       : ['HostSystem']
    },
    # 
    # Compatibility: 5.0.0
    {
        'name'         : 'hbr.hbrNetTx',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # 
    # Compatibility: 5.0.0
    {
        'name'         : 'hbr.hbrNumVms',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
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
        'entity'       : []
    },
    # Memory used
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0
    {
        'name'         : 'managementAgent.memUsed',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Memory swap in
    # Compatibility: 3.5.0 / 4.1.0
    {
        'name'         : 'managementAgent.swapIn',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Memory swap out
    # Compatibility: 3.5.0 / 4.1.0
    {
        'name'         : 'managementAgent.swapOut',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Memory swap used
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0
    {
        'name'         : 'managementAgent.swapUsed',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
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
        'entity'       : ['VirtualMachine', 'HostSystem', 'ResourcePool']
    },
    # Active write
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'mem.activewrite',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Memory Capacity Contention
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'mem.capacity.contention',
        's_type'       : 'rate',
        'unit'         : 'percent',
        'rollup'       : 'average',
        'entity'       : ['ResourcePool']
    },
    # Memory Capacity Entitlement
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'mem.capacity.entitlement',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['ResourcePool']
    },
    # Memory Capacity Provisioned
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'mem.capacity.provisioned',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['ResourcePool']
    },
    # Memory Capacity Usable
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.capacity.usable',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : []
    },
    # Memory Capacity Usage
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'mem.capacity.usage',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['ResourcePool']
    },
    # 
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.capacity.usage.userworld',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : []
    },
    # 
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.capacity.usage.vm',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : []
    },
    # Memory Capacity Usage by VM overhead
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.capacity.usage.vmOvrhd',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : []
    },
    # Memory Capacity Usage by VMkernel Overhead
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.capacity.usage.vmkOvrhd',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : []
    },
    # Compressed
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'mem.compressed',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'ResourcePool']
    },
    # Compression rate
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'mem.compressionRate',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'ResourcePool']
    },
    # Consumed
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.consumed',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'ResourcePool']
    },
    # Memory Consumed by userworlds
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.consumed.userworlds',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : []
    },
    # Memory Consumed by VMs
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.consumed.vms',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : []
    },
    # Decompression rate
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'mem.decompressionRate',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'ResourcePool']
    },
    # Entitlement
    # Compatibility: 5.0.0
    {
        'name'         : 'mem.entitlement',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine']
    },
    # Granted
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.granted',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'ResourcePool']
    },
    # Heap
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.heap',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Heap free
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.heapfree',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Latency
    # Compatibility: 5.0.0
    {
        'name'         : 'mem.latency',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Swap in from host cache
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.llSwapIn',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Swap in rate from host cache
    # Compatibility: 5.0.0
    {
        'name'         : 'mem.llSwapInRate',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Swap out to host cache
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.llSwapOut',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Swap out rate to host cache
    # Compatibility: 5.0.0
    {
        'name'         : 'mem.llSwapOutRate',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Host cache used for swapping
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.llSwapUsed',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Low free threshold
    # Compatibility: 5.0.0
    {
        'name'         : 'mem.lowfreethreshold',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Worst case allocation
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'mem.mementitlement',
        's_type'       : 'absolute',
        'unit'         : 'megaBytes',
        'rollup'       : 'latest',
        'entity'       : ['ResourcePool']
    },
    # Overhead
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.overhead',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'ResourcePool']
    },
    # Reserved overhead
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'mem.overheadMax',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine']
    },
    # Overhead touched
    # Compatibility: 5.0.0
    {
        'name'         : 'mem.overheadTouched',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine']
    },
    # Reserved capacity
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'mem.reservedCapacity',
        's_type'       : 'absolute',
        'unit'         : 'megaBytes',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Memory Reserved capacity by userworlds
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.reservedCapacity.userworld',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : []
    },
    # Memory Reserved capacity by VMs
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.reservedCapacity.vm',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : []
    },
    # Memory Reserved capacity by VM overhead
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.reservedCapacity.vmOvhd',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : []
    },
    # Memory Reserved capacity by VMkernel Overhead
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.reservedCapacity.vmkOvrhd',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : []
    },
    # Memory Reserved Capacity %
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.reservedCapacityPct',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'average',
        'entity'       : []
    },
    # Shared
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.shared',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'ResourcePool']
    },
    # Shared common
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.sharedcommon',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # State
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'mem.state',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem']
    },
    # Swap in
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.swapin',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Swap in rate
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'mem.swapinRate',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Swap out
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.swapout',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Swap out rate
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'mem.swapoutRate',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Swapped
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.swapped',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'ResourcePool']
    },
    # Swap target
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.swaptarget',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine']
    },
    # Swap unreserved
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.swapunreserved',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : []
    },
    # Swap used
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.swapused',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Used by VMkernel
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.sysUsage',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Total capacity
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'mem.totalCapacity',
        's_type'       : 'absolute',
        'unit'         : 'megaBytes',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Total
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.totalmb',
        's_type'       : 'absolute',
        'unit'         : 'megaBytes',
        'rollup'       : 'average',
        'entity'       : []
    },
    # Unreserved
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.unreserved',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Usage
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.usage',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Balloon
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.vmmemctl',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'ResourcePool']
    },
    # Balloon target
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.vmmemctltarget',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine']
    },
    # Zero
    # Compatibility: UNKNOWN
    {
        'name'         : 'mem.zero',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'ResourcePool']
    },
    # Memory saved by zipping
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'mem.zipSaved',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine']
    },
    # Zipped memory
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'mem.zipped',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine']
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
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Broadcast transmits
    # Compatibility: 5.0.0
    {
        'name'         : 'network.broadcastTx',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Data receive rate
    # Compatibility: 5.0.0
    {
        'name'         : 'network.bytesRx',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Data transmit rate
    # Compatibility: 5.0.0
    {
        'name'         : 'network.bytesTx',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Receive packets dropped
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'network.droppedRx',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Transmit packets dropped
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'network.droppedTx',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Packet receive errors
    # Compatibility: 5.0.0
    {
        'name'         : 'network.errorsRx',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : ['HostSystem']
    },
    # Packet transmit errors
    # Compatibility: 5.0.0
    {
        'name'         : 'network.errorsTx',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : ['HostSystem']
    },
    # Multicast receives
    # Compatibility: 5.0.0
    {
        'name'         : 'network.multicastRx',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Multicast transmits
    # Compatibility: 5.0.0
    {
        'name'         : 'network.multicastTx',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Packets received
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'network.packetsRx',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Packets transmitted
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'network.packetsTx',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Data receive rate
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'network.received',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # vNic Throughput Contention
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'network.throughput.contention',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : ['ResourcePool']
    },
    # pNic Packets Received and Transmitted per Second
    # Compatibility: UNKNOWN
    {
        'name'         : 'network.throughput.packetsPerSec',
        's_type'       : 'rate',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : []
    },
    # pNic Throughput Provisioned
    # Compatibility: UNKNOWN
    {
        'name'         : 'network.throughput.provisioned',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : []
    },
    # pNic Throughput Usable
    # Compatibility: UNKNOWN
    {
        'name'         : 'network.throughput.usable',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : []
    },
    # vNic Throughput Usage
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'network.throughput.usage',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['ResourcePool']
    },
    # pNic Throughput Usage for FT
    # Compatibility: UNKNOWN
    {
        'name'         : 'network.throughput.usage.ft',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : []
    },
    # pNic Throughput Usage for HBR
    # Compatibility: UNKNOWN
    {
        'name'         : 'network.throughput.usage.hbr',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : []
    },
    # pNic Throughput Usage for iSCSI
    # Compatibility: UNKNOWN
    {
        'name'         : 'network.throughput.usage.iscsi',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : []
    },
    # pNic Throughput Usage for NFS
    # Compatibility: UNKNOWN
    {
        'name'         : 'network.throughput.usage.nfs',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : []
    },
    # pNic Throughput Usage for VMs
    # Compatibility: UNKNOWN
    {
        'name'         : 'network.throughput.usage.vm',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : []
    },
    # pNic Throughput Usage for vMotion
    # Compatibility: UNKNOWN
    {
        'name'         : 'network.throughput.usage.vmotion',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : []
    },
    # Data transmit rate
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'network.transmitted',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Unknown protocol frames
    # Compatibility: 5.0.0
    {
        'name'         : 'network.unknownProtos',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : ['HostSystem']
    },
    # Usage
    # Compatibility: UNKNOWN
    {
        'name'         : 'network.usage',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem']
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
        'entity'       : []
    },
    # Power Capacity Usage
    # Compatibility: UNKNOWN
    {
        'name'         : 'power.capacity.usage',
        's_type'       : 'absolute',
        'unit'         : 'watt',
        'rollup'       : 'average',
        'entity'       : []
    },
    # Host Power Capacity Provisioned
    # Compatibility: UNKNOWN
    {
        'name'         : 'power.capacity.usagePct',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'average',
        'entity'       : []
    },
    # Energy usage
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'power.energy',
        's_type'       : 'delta',
        'unit'         : 'joule',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine', 'HostSystem', 'ResourcePool']
    },
    # Usage
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'power.power',
        's_type'       : 'absolute',
        'unit'         : 'watt',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine', 'HostSystem', 'ResourcePool']
    },
    # Cap
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'power.powerCap',
        's_type'       : 'absolute',
        'unit'         : 'watt',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
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
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Active (15 min. average)
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'rescpu.actav15',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Active (5 min. average)
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'rescpu.actav5',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Active (1 min. peak)
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'rescpu.actpk1',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Active (15 min. peak)
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'rescpu.actpk15',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Active (5 min. peak)
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'rescpu.actpk5',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Throttled (1 min. average)
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'rescpu.maxLimited1',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Throttled (15 min. average)
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'rescpu.maxLimited15',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Throttled (5 min. average)
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'rescpu.maxLimited5',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Running (1 min. average)
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'rescpu.runav1',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Running (15 min. average)
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'rescpu.runav15',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Running (5 min. average)
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'rescpu.runav5',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Running (1 min. peak)
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'rescpu.runpk1',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Running (15 min. peak)
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'rescpu.runpk15',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Running (5 min. peak)
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'rescpu.runpk5',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Group CPU sample count
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'rescpu.sampleCount',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem']
    },
    # Group CPU sample period
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'rescpu.samplePeriod',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem']
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
        'entity'       : []
    },
    # Average commands issued per second
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'storageAdapter.commandsAveraged',
        's_type'       : 'rate',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Highest latency
    # Compatibility: 5.0.0
    {
        'name'         : 'storageAdapter.maxTotalLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem']
    },
    # Average read requests per second
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'storageAdapter.numberReadAveraged',
        's_type'       : 'rate',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Average write requests per second
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'storageAdapter.numberWriteAveraged',
        's_type'       : 'rate',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Storage Adapter Outstanding I/Os
    # Compatibility: UNKNOWN
    {
        'name'         : 'storageAdapter.outstandingIOs',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : []
    },
    # Storage Adapter Queue Depth
    # Compatibility: UNKNOWN
    {
        'name'         : 'storageAdapter.queueDepth',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : []
    },
    # Storage Adapter Queue Command Latency
    # Compatibility: UNKNOWN
    {
        'name'         : 'storageAdapter.queueLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : []
    },
    # Storage Adapter Number Queued
    # Compatibility: UNKNOWN
    {
        'name'         : 'storageAdapter.queued',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : []
    },
    # Read rate
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'storageAdapter.read',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Storage Adapter Throughput Contention
    # Compatibility: UNKNOWN
    {
        'name'         : 'storageAdapter.throughput.cont',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : []
    },
    # Storage Adapter Throughput Usage
    # Compatibility: UNKNOWN
    {
        'name'         : 'storageAdapter.throughput.usag',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : []
    },
    # Read latency
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'storageAdapter.totalReadLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Write latency
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'storageAdapter.totalWriteLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Write rate
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'storageAdapter.write',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
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
        'entity'       : []
    },
    # Storage Path Command Aborts
    # Compatibility: UNKNOWN
    {
        'name'         : 'storagePath.commandsAborted',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : []
    },
    # Average commands issued per second
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'storagePath.commandsAveraged',
        's_type'       : 'rate',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Highest latency
    # Compatibility: 5.0.0
    {
        'name'         : 'storagePath.maxTotalLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem']
    },
    # Average read requests per second
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'storagePath.numberReadAveraged',
        's_type'       : 'rate',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Average write requests per second
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'storagePath.numberWriteAveraged',
        's_type'       : 'rate',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Read rate
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'storagePath.read',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Storage Path Throughput Contention
    # Compatibility: UNKNOWN
    {
        'name'         : 'storagePath.throughput.cont',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : []
    },
    # Storage Path Throughput Usage
    # Compatibility: UNKNOWN
    {
        'name'         : 'storagePath.throughput.usage',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : []
    },
    # Read latency
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'storagePath.totalReadLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Write latency
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'storagePath.totalWriteLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Write rate
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'storagePath.write',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
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
        'entity'       : ['HostSystem']
    },
    # Disk usage
    # Compatibility: 4.1.0
    {
        'name'         : 'system.diskUsage',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem']
    },
    # Heartbeat
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.heartbeat',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : ['VirtualMachine']
    },
    # OS Uptime
    # Compatibility: 5.0.0
    {
        'name'         : 'system.osUptime',
        's_type'       : 'absolute',
        'unit'         : 'second',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine']
    },
    # Resource CPU active (1 min. average)
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.resourceCpuAct1',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem']
    },
    # Resource CPU active (5 min. average)
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.resourceCpuAct5',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem']
    },
    # Resource CPU allocation maximum, in MHz
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.resourceCpuAllocMax',
        's_type'       : 'absolute',
        'unit'         : 'megaHertz',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem']
    },
    # Resource CPU allocation minimum, in MHz
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.resourceCpuAllocMin',
        's_type'       : 'absolute',
        'unit'         : 'megaHertz',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem']
    },
    # Resource CPU allocation shares
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.resourceCpuAllocShares',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem']
    },
    # Resource CPU maximum limited (1 min.)
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.resourceCpuMaxLimited1',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem']
    },
    # Resource CPU maximum limited (5 min.)
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.resourceCpuMaxLimited5',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem']
    },
    # Resource CPU running (1 min. average)
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.resourceCpuRun1',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem']
    },
    # Resource CPU running (5 min. average)
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.resourceCpuRun5',
        's_type'       : 'absolute',
        'unit'         : 'percent',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem']
    },
    # Resource CPU usage ({rollupType})
    # Compatibility: UNKNOWN
    {
        'name'         : 'system.resourceCpuUsage',
        's_type'       : 'rate',
        'unit'         : 'megaHertz',
        'rollup'       : 'average',
        'entity'       : ['HostSystem']
    },
    # Resource memory allocation maximum, in KB
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.resourceMemAllocMax',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem']
    },
    # Resource memory allocation minimum, in KB
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.resourceMemAllocMin',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem']
    },
    # Resource memory allocation shares
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.resourceMemAllocShares',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem']
    },
    # Resource memory shared
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.resourceMemCow',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem']
    },
    # Resource memory mapped
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.resourceMemMapped',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem']
    },
    # Resource memory overhead
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.resourceMemOverhead',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem']
    },
    # Resource memory share saved
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.resourceMemShared',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem']
    },
    # Resource memory swapped
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.resourceMemSwapped',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem']
    },
    # Resource memory touched
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.resourceMemTouched',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem']
    },
    # Resource memory zero
    # Compatibility: 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.resourceMemZero',
        's_type'       : 'absolute',
        'unit'         : 'kiloBytes',
        'rollup'       : 'latest',
        'entity'       : ['HostSystem']
    },
    # Uptime
    # Compatibility: 3.5.0 / 4.0.0 / 4.1.0 / 5.0.0
    {
        'name'         : 'system.uptime',
        's_type'       : 'absolute',
        'unit'         : 'second',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine', 'HostSystem']
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
        'entity'       : []
    },
    # Virtual Disk Command Aborts
    # Compatibility: UNKNOWN
    {
        'name'         : 'virtualDisk.commandsAborted',
        's_type'       : 'delta',
        'unit'         : 'number',
        'rollup'       : 'summation',
        'entity'       : []
    },
    # Average read requests per second
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'virtualDisk.numberReadAveraged',
        's_type'       : 'rate',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine']
    },
    # Average write requests per second
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'virtualDisk.numberWriteAveraged',
        's_type'       : 'rate',
        'unit'         : 'number',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine']
    },
    # Read rate
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'virtualDisk.read',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine']
    },
    # Read workload metric
    # Compatibility: 5.0.0
    {
        'name'         : 'virtualDisk.readLoadMetric',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine']
    },
    # Average number of outstanding read requests
    # Compatibility: 5.0.0
    {
        'name'         : 'virtualDisk.readOIO',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine']
    },
    # Virtual Disk Throughput Contention
    # Compatibility: UNKNOWN
    {
        'name'         : 'virtualDisk.throughput.cont',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : []
    },
    # Virtual Disk Throughput Usage
    # Compatibility: UNKNOWN
    {
        'name'         : 'virtualDisk.throughput.usage',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : []
    },
    # Read latency
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'virtualDisk.totalReadLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine']
    },
    # Write latency
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'virtualDisk.totalWriteLatency',
        's_type'       : 'absolute',
        'unit'         : 'millisecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine']
    },
    # Write rate
    # Compatibility: 4.1.0 / 5.0.0
    {
        'name'         : 'virtualDisk.write',
        's_type'       : 'rate',
        'unit'         : 'kiloBytesPerSecond',
        'rollup'       : 'average',
        'entity'       : ['VirtualMachine']
    },
    # Write workload metric
    # Compatibility: 5.0.0
    {
        'name'         : 'virtualDisk.writeLoadMetric',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine']
    },
    # Average number of outstanding write requests
    # Compatibility: 5.0.0
    {
        'name'         : 'virtualDisk.writeOIO',
        's_type'       : 'absolute',
        'unit'         : 'number',
        'rollup'       : 'latest',
        'entity'       : ['VirtualMachine']
    },
]


ALL_METRICS = CPU_METRICS + DATASTORE_METRICS + DISK_METRICS + \
    HBR_METRICS + MANAGEMENTAGENT_METRICS + MEM_METRICS + NETWORK_METRICS + \
    POWER_METRICS + RESCPU_METRICS + STORAGEADAPTER_METRICS + \
    STORAGEPATH_METRICS + VIRTUALDISK_METRICS
