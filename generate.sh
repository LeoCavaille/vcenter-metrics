#!/bin/bash

rm -f metrics.py
python transform.py raw_html/cpu_metrics.html cpu >> metrics.py
echo -ne '\n\n' >> metrics.py
python transform.py raw_html/datastore_metrics.html datastore >> metrics.py
echo -ne '\n\n' >> metrics.py
python transform.py raw_html/disk_metrics.html disk >> metrics.py
echo -ne '\n\n' >> metrics.py
python transform.py raw_html/hbr_metrics.html hbr >> metrics.py
echo -ne '\n\n' >> metrics.py
python transform.py raw_html/managementAgent_metrics.html managementAgent >> metrics.py
echo -ne '\n\n' >> metrics.py
python transform.py raw_html/memory_metrics.html mem >> metrics.py
echo -ne '\n\n' >> metrics.py
python transform.py raw_html/network_metrics.html network >> metrics.py
echo -ne '\n\n' >> metrics.py
python transform.py raw_html/power_metrics.html power >> metrics.py
echo -ne '\n\n' >> metrics.py
python transform.py raw_html/rescpu_metrics.html rescpu >> metrics.py
echo -ne '\n\n' >> metrics.py
python transform.py raw_html/storageAdapter_metrics.html storageAdapter >> metrics.py
echo -ne '\n\n' >> metrics.py
python transform.py raw_html/storagePath_metrics.html storagePath >> metrics.py
echo -ne '\n\n' >> metrics.py
python transform.py raw_html/system_metrics.html system >> metrics.py
echo -ne '\n\n' >> metrics.py
python transform.py raw_html/virtualDisk_metrics.html virtualDisk >> metrics.py
echo -ne '\n\n' >> metrics.py

cat >> metrics.py <<-EOF
ALL_METRICS = CPU_METRICS + DATASTORE_METRICS + DISK_METRICS + \\
    HBR_METRICS + MANAGEMENTAGENT_METRICS + MEM_METRICS + NETWORK_METRICS + \\
    POWER_METRICS + RESCPU_METRICS + STORAGEADAPTER_METRICS + \\
    STORAGEPATH_METRICS + VIRTUALDISK_METRICS
EOF
