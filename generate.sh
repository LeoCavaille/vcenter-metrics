#!/bin/bash

rm -f all_metrics.py basic_metrics.py
python transform.py raw_html/cpu_metrics.html cpu >> all_metrics.py
echo -ne '\n\n' >> all_metrics.py
python transform.py raw_html/datastore_metrics.html datastore >> all_metrics.py
echo -ne '\n\n' >> all_metrics.py
python transform.py raw_html/disk_metrics.html disk >> all_metrics.py
echo -ne '\n\n' >> all_metrics.py
python transform.py raw_html/hbr_metrics.html hbr >> all_metrics.py
echo -ne '\n\n' >> all_metrics.py
python transform.py raw_html/managementAgent_metrics.html managementAgent >> all_metrics.py
echo -ne '\n\n' >> all_metrics.py
python transform.py raw_html/memory_metrics.html mem >> all_metrics.py
echo -ne '\n\n' >> all_metrics.py
python transform.py raw_html/network_metrics.html network >> all_metrics.py
echo -ne '\n\n' >> all_metrics.py
python transform.py raw_html/power_metrics.html power >> all_metrics.py
echo -ne '\n\n' >> all_metrics.py
python transform.py raw_html/rescpu_metrics.html rescpu >> all_metrics.py
echo -ne '\n\n' >> all_metrics.py
python transform.py raw_html/storageAdapter_metrics.html storageAdapter >> all_metrics.py
echo -ne '\n\n' >> all_metrics.py
python transform.py raw_html/storagePath_metrics.html storagePath >> all_metrics.py
echo -ne '\n\n' >> all_metrics.py
python transform.py raw_html/system_metrics.html system >> all_metrics.py
echo -ne '\n\n' >> all_metrics.py
python transform.py raw_html/virtualDisk_metrics.html virtualDisk >> all_metrics.py
echo -ne '\n\n' >> all_metrics.py

cat >> all_metrics.py <<-EOF
ALL_METRICS = CPU_METRICS + DATASTORE_METRICS + DISK_METRICS + \\
    HBR_METRICS + MANAGEMENTAGENT_METRICS + MEM_METRICS + NETWORK_METRICS + \\
    POWER_METRICS + RESCPU_METRICS + STORAGEADAPTER_METRICS + \\
    STORAGEPATH_METRICS + VIRTUALDISK_METRICS
EOF

python transform_basic.py
